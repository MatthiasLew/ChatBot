import tkinter as tk
from tkinter import ttk
import requests
from config import API_URL, AVAILABLE_MODELS, DEFAULT_MODEL
from chat_modes import CHAT_MODES
from save_utils import save_txt, save_docx
from translations import translations
import re

# Global variables
current_language = "pl"  # Default language
conversation = []        # Conversation history as list of (speaker, message) tuples


# Retrieve a localized translation for a given key
def get_translation(key):
    return translations[current_language].get(key, key)


# Send the user's input to the chat API and display the response
def send_message():
    user_input = input_box.get("1.0", tk.END).strip()
    if not user_input:
        return

    # Append user input to conversation
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
        # Send POST request to the API
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        bot_reply = response.json()["choices"][0]["message"]["content"]

        # Remove internal tags or formatting
        bot_reply = re.sub(r"<think>.*?</think>", "", bot_reply, flags=re.DOTALL).strip()
        bot_reply = re.sub(r"\\\[.*?\\]", "", bot_reply, flags=re.DOTALL)  # Remove LaTeX blocks
        bot_reply = re.sub(r"\\boxed\{(.*?)}", r"\1", bot_reply)  # Unwrap boxed math
        bot_reply = bot_reply.strip()

        # Optionally extract the first numeric value from the response
        match = re.search(r"[-+]?\d*\.?\d+", bot_reply)
        if match:
            bot_reply = match.group(0)

    except Exception as e:
        bot_reply = f"Błąd: {e}"  # Show error in Polish regardless of current language

    # Append bot response to conversation
    conversation.append(("Bot", bot_reply))
    display_chat()
    input_box.delete("1.0", tk.END)


# Display the full conversation history in the chat display area
def display_chat():
    chat_display.config(state="normal")
    chat_display.delete("1.0", tk.END)
    for speaker, text in conversation:
        chat_display.insert(tk.END, f"{speaker}: {text}\n\n")
    chat_display.config(state="disabled")


# Toggle the interface language between Polish and English
def switch_language():
    global current_language
    current_language = "en" if current_language == "pl" else "pl"
    update_labels()


# Update UI labels to reflect the current language
def update_labels():
    root.title(get_translation("title"))
    send_button.config(text=get_translation("send"))
    save_txt_button.config(text=get_translation("save_txt"))
    save_docx_button.config(text=get_translation("save_docx"))
    mode_label.config(text=get_translation("mode"))
    model_label.config(text=get_translation("model"))
    lang_button.config(text=get_translation("language"))

    # Update available chat modes based on language
    available_modes = list(CHAT_MODES[current_language].keys())
    mode_menu["values"] = available_modes
    mode_var.set(available_modes[0])


# Export conversation history to a .txt file
def save_as_txt():
    save_txt(conversation)


# Export conversation history to a .docx file
def save_as_docx():
    save_docx(conversation)


# ----- GUI Initialization -----

root = tk.Tk()
root.title(get_translation("title"))

frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

# Text widget for displaying conversation
chat_display = tk.Text(frame, height=20, state="disabled", wrap=tk.WORD)
chat_display.pack(fill=tk.BOTH, expand=True)

# Text input for user messages
input_box = tk.Text(frame, height=3)
input_box.pack(fill=tk.BOTH, expand=True)

# Send button
send_button = ttk.Button(frame, text=get_translation("send"), command=send_message)
send_button.pack(pady=5)

# Save buttons
save_frame = ttk.Frame(frame)
save_frame.pack()

save_txt_button = ttk.Button(save_frame, text=get_translation("save_txt"), command=save_as_txt)
save_txt_button.pack(side=tk.LEFT, padx=5)

save_docx_button = ttk.Button(save_frame, text=get_translation("save_docx"), command=save_as_docx)
save_docx_button.pack(side=tk.LEFT, padx=5)

# Mode selection (e.g., creative, precise)
mode_label = ttk.Label(frame, text=get_translation("mode"))
mode_label.pack(pady=(10, 0))

mode_var = tk.StringVar()
mode_menu = ttk.Combobox(frame, textvariable=mode_var, state="readonly")
mode_menu.pack()

# Model selection (e.g., GPT-4, GPT-3.5)
model_label = ttk.Label(frame, text=get_translation("model"))
model_label.pack(pady=(10, 0))

model_var = tk.StringVar(value=DEFAULT_MODEL)
model_menu = ttk.Combobox(frame, textvariable=model_var, values=AVAILABLE_MODELS, state="readonly")
model_menu.pack()

# Language switch button
lang_button = ttk.Button(frame, text=get_translation("language"), command=switch_language)
lang_button.pack(pady=10)

# Set initial UI text and available options
update_labels()

# Start the GUI event loop
root.mainloop()
