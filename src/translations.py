"""
translations.py

Provides UI label translations for multilingual support in the chatbot application.
Contains a mapping of interface keys to localized strings for each supported language.
Used for dynamic GUI label updates based on selected language.
"""

translations = {
    "pl": {  # Polish translations
        "title": "Chatbot",
        "send": "Wyślij",
        "save_txt": "Zapisz jako TXT",
        "save_docx": "Zapisz jako DOCX",
        "mode": "Tryb rozmowy",
        "language": "Język",
        "model": "Model AI"
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