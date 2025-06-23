"""
chat_gui_app.py

Main graphical user interface (GUI) for the chatbot application.
Integrates user interaction, language switching, message processing,
and AI integration through an API. Uses Tkinter for GUI components.
"""

import tkinter as tk
from tkinter import ttk
import requests
import re

from config import API_URL, AVAILABLE_MODELS, DEFAULT_MODEL
from chat_modes import CHAT_MODES
from save_utils import save_txt, save_docx, TxtSaver
from translations import translations
from chat_manager import ChatManager
from analysis import plot_lengths
from functional_utils import (
    uppercase_conversation, only_user_messages, total_chars,
    get_unique_speakers, search_messages
)

# Global state
current_language = "pl"
chat_manager = ChatManager()


def get_translation(key: str) -> str:
    """Fetch localized UI string based on the current language."""
    return translations[current_language].get(key, key)


def countdown(n: int) -> list[str]:
    """Recursive countdown generator for /countdown command."""
    if n <= 0:
        return ["Start!"]
    return [str(n)] + countdown(n - 1)


def log_call(func):
    """Decorator that logs function calls for debugging."""

    def wrapper(*args, **kwargs):
        print(f"🛠️ Wywołanie funkcji: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@log_call
def save_as_txt() -> None:
    """Save current conversation to a TXT file."""
    save_txt(chat_manager.get())


@log_call
def save_as_docx() -> None:
    """Save current conversation to a DOCX file."""
    save_docx(chat_manager.get())


def send_message() -> None:
    """Handle message submission, including custom commands and API call."""
    user_input = input_box.get("1.0", tk.END).strip()
    if not user_input:
        return

    if user_input.startswith("/countdown"):
        try:
            n = int(user_input.split()[1])
            for line in countdown(n):
                chat_manager.add("Bot", line)
            display_chat()
            return
        except:
            chat_manager.add("Bot", "Użyj: /countdown liczba")
            display_chat()
            return

    if user_input.startswith("/repeat"):
        try:
            n = int(user_input.split()[1])
            for i in range(n):
                chat_manager.add("Bot", f"To jest powtórzenie {i + 1}")
            display_chat()
            return
        except:
            chat_manager.add("Bot", "Użyj: /repeat liczba")
            display_chat()
            return

    chat_manager.add("Użytkownik", user_input)
    display_chat()

    headers = {"Content-Type": "application/json"}
    mode_prompt = CHAT_MODES[current_language][mode_var.get()]
    payload = {
        "model": model_var.get(),
        "messages": [
            {"role": "system", "content": mode_prompt},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        bot_reply = response.json()["choices"][0]["message"]["content"]
        bot_reply = re.sub(r"<think>.*?</think>", "", bot_reply, flags=re.DOTALL).strip()
        bot_reply = re.sub(r"\\\\\[.*?\\\\", "", bot_reply, flags=re.DOTALL)
        bot_reply = re.sub(r"\\boxed\{(.*?)}", r"\1", bot_reply).strip()
        match = re.search(r"[-+]?\d*\.?\d+", bot_reply)
        if match:
            bot_reply = match.group(0)
    except Exception as e:
        bot_reply = f"Błąd: {e}"

    chat_manager.add("Bot", bot_reply)
    display_chat()
    input_box.delete("1.0", tk.END)


def display_chat() -> None:
    """Update the chat display with the current conversation."""
    chat_display.config(state="normal")
    chat_display.delete("1.0", tk.END)
    for speaker, text in chat_manager.get():
        chat_display.insert(tk.END, f"{speaker}: {text}\n\n")
    chat_display.config(state="disabled")


def switch_language() -> None:
    """Toggle the UI language between Polish and English."""
    global current_language
    current_language = "en" if current_language == "pl" else "pl"
    update_labels()


def update_labels() -> None:
    """Update all UI labels based on the selected language."""
    root.title(get_translation("title"))
    send_button.config(text=get_translation("send"))
    save_txt_button.config(text=get_translation("save_txt"))
    save_docx_button.config(text=get_translation("save_docx"))
    mode_label.config(text=get_translation("mode"))
    model_label.config(text=get_translation("model"))
    lang_button.config(text=get_translation("language"))

    available_modes = list(CHAT_MODES[current_language].keys())
    mode_menu["values"] = available_modes
    mode_var.set(available_modes[0])


# GUI setup
root = tk.Tk()
root.title(get_translation("title"))
frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

chat_display = tk.Text(frame, height=20, state="disabled", wrap=tk.WORD)
chat_display.pack(fill=tk.BOTH, expand=True)

input_box = tk.Text(frame, height=3)
input_box.pack(fill=tk.BOTH, expand=True)

send_button = ttk.Button(frame, text=get_translation("send"), command=send_message)
send_button.pack(pady=5)

save_frame = ttk.Frame(frame)
save_frame.pack()

save_txt_button = ttk.Button(save_frame, text=get_translation("save_txt"), command=save_as_txt)
save_txt_button.pack(side=tk.LEFT, padx=5)

save_docx_button = ttk.Button(save_frame, text=get_translation("save_docx"), command=save_as_docx)
save_docx_button.pack(side=tk.LEFT, padx=5)

plot_button = ttk.Button(frame, text="Wykres długości", command=lambda: plot_lengths(chat_manager.get()))
plot_button.pack(pady=5)

mode_label = ttk.Label(frame, text=get_translation("mode"))
mode_label.pack(pady=(10, 0))

mode_var = tk.StringVar()
mode_menu = ttk.Combobox(frame, textvariable=mode_var, state="readonly")
mode_menu.pack()

model_label = ttk.Label(frame, text=get_translation("model"))
model_label.pack(pady=(10, 0))

model_var = tk.StringVar(value=DEFAULT_MODEL)
model_menu = ttk.Combobox(frame, textvariable=model_var, values=AVAILABLE_MODELS, state="readonly")
model_menu.pack()

lang_button = ttk.Button(frame, text=get_translation("language"), command=switch_language)
lang_button.pack(pady=10)


def apply_uppercase():
    """Convert all messages in chat to uppercase."""
    chat_manager.convo = uppercase_conversation(chat_manager.get())
    display_chat()


def filter_user_msgs():
    """Filter the conversation to include only user messages."""
    chat_manager.convo = only_user_messages(chat_manager.get())
    display_chat()


def show_char_count():
    """Display total number of characters in the conversation."""
    count = total_chars(chat_manager.get())
    chat_manager.add("Bot", f"Łączna liczba znaków: {count}")
    display_chat()


def show_unique_speakers():
    """Display a list of unique speakers."""
    unique = get_unique_speakers(chat_manager.get())
    chat_manager.add("Bot", f"Unikalni rozmówcy: {', '.join(unique)}")
    display_chat()


def save_using_class():
    """Save conversation using an OOP-style TxtSaver class."""
    saver = TxtSaver(chat_manager.get())
    saver.save()
    chat_manager.add("Bot", "Zapisano czat przez klasę dziedziczącą.")
    display_chat()


search_entry = ttk.Entry(frame)
search_entry.pack(pady=2)


def perform_search():
    """Search for a keyword in messages and show matching results."""
    keyword = search_entry.get()
    if keyword:
        results = search_messages(chat_manager.get(), keyword)
        chat_manager.clear()
        for who, msg in results:
            chat_manager.add(who, msg)
        display_chat()


button_frame = ttk.Frame(frame)  # nowy pod-frame w istniejącym frame
button_frame.pack(pady=10)       # tutaj możesz użyć pack

buttons = [
    ttk.Button(button_frame, text="Szukaj słowa", command=perform_search),
    ttk.Button(button_frame, text="Zapisz (dziedziczenie)", command=save_using_class),
    ttk.Button(button_frame, text="Unikalni rozmówcy", command=show_unique_speakers),
    ttk.Button(button_frame, text="WIELKIE LITERY", command=apply_uppercase),
    ttk.Button(button_frame, text="Tylko użytkownik", command=filter_user_msgs),
    ttk.Button(button_frame, text="Policz znaki", command=show_char_count),
]

for i, btn in enumerate(buttons):
    row = i // 3
    col = i % 3
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="ew")


update_labels()
root.mainloop()
