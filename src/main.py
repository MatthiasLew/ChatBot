# main.py
import tkinter as tk
from tkinter import ttk
import requests
from config import API_URL, AVAILABLE_MODELS, DEFAULT_MODEL
from chat_modes import CHAT_MODES
from save_utils import save_txt, save_docx
from translations import translations
import re


current_language = "pl"
conversation = []


def get_translation(key):
    return translations[current_language].get(key, key)


def send_message():
    user_input = input_box.get("1.0", tk.END).strip()
    if not user_input:
        return

    conversation.append(("Użytkownik", user_input))
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

        # Usuń think tags jeśli są
        bot_reply = re.sub(r"<think>.*?</think>", "", bot_reply, flags=re.DOTALL).strip()

        # Usuń LaTeX i opakowania typu \boxed{}
        bot_reply = re.sub(r"\\\[.*?\\\]", "", bot_reply, flags=re.DOTALL)
        bot_reply = re.sub(r"\\boxed\{(.*?)\}", r"\1", bot_reply)
        bot_reply = bot_reply.strip()

        # Jeśli chcesz, wyciągnij tylko pierwszą liczbę:
        match = re.search(r"[-+]?\d*\.?\d+", bot_reply)
        if match:
            bot_reply = match.group(0)

    except Exception as e:
        bot_reply = f"Błąd: {e}"

    conversation.append(("Bot", bot_reply))
    display_chat()
    input_box.delete("1.0", tk.END)


def display_chat():
    chat_display.config(state="normal")
    chat_display.delete("1.0", tk.END)
    for speaker, text in conversation:
        chat_display.insert(tk.END, f"{speaker}: {text}\n\n")
    chat_display.config(state="disabled")


def switch_language():
    global current_language
    current_language = "en" if current_language == "pl" else "pl"
    update_labels()


def update_labels():
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


def save_as_txt():
    save_txt(conversation)


def save_as_docx():
    save_docx(conversation)


# GUI
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

update_labels()
root.mainloop()
