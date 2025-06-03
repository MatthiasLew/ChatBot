# translations.py

# Dictionary holding UI string translations for supported interface languages.
# Each top-level key is a language code (e.g., "pl" for Polish, "en" for English).
# Values are nested dictionaries mapping internal UI keys to localized display strings.

translations = {
    "pl": {  # Polish translations
        "title": "Chatbot",               # Window title
        "send": "Wyślij",                 # Label for the "Send" button
        "save_txt": "Zapisz jako TXT",    # Label for the button to save as .txt
        "save_docx": "Zapisz jako DOCX",  # Label for the button to save as .docx
        "mode": "Tryb rozmowy",           # Label for chat mode selector
        "language": "Język",              # Label for language toggle button
        "model": "Model AI"               # Label for model selection dropdown
    },
    "en": {  # English translations
        "title": "Chatbot",
        "send": "Send",
        "save_txt": "Save as TXT",
        "save_docx": "Save as DOCX",
        "mode": "Chat mode",
        "language": "Language",
        "model": "AI Model"
    }
}
