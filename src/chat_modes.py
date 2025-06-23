"""
chat_modes.py

This module defines the supported chat modes for different languages used in the chatbot system.
Each mode maps to a predefined assistant behavior or conversational tone, which is sent as a
"system" message to influence the AI model's response style.

Structure:
- CHAT_MODES: A nested dictionary mapping language codes (e.g., "pl", "en") to mode labels
  and their corresponding prompt instructions.

Intended for use in user interface mode selection and AI behavior customization.
"""

CHAT_MODES = {
    "pl": {
        # Polish language modes
        "Rzeczowy": "Odpowiadaj krótko, jasno, jak profesjonalny doradca techniczny.",
        "Kreatywny": "Bądź kreatywny, wymyślaj ciekawe historie, baw się językiem.",
        "Pomoc techniczna": "Zachowuj się jak pomoc techniczna. Dawaj jasne i precyzyjne instrukcje.",
    },
    "en": {
        # English language modes
        "Factual": "Respond briefly and clearly, like a professional technical advisor.",
        "Creative": "Be creative, invent interesting stories, and play with language.",
        "Tech Support": "Act as tech support. Provide clear and precise instructions.",
    }
}
