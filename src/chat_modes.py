# chat_modes.py

# Dictionary defining available chat modes per supported language.
# Each mode corresponds to a different conversational style or assistant behavior.
# These prompts are sent as "system" messages to guide the model's tone and purpose.

CHAT_MODES = {
    "pl": {  # Polish language modes
        "Rzeczowy": "Odpowiadaj krótko, jasno, jak profesjonalny doradca techniczny.",
        # Factual and concise responses, suitable for technical and business contexts.

        "Kreatywny": "Bądź kreatywny, wymyślaj ciekawe historie, baw się językiem.",
        # Encourages imaginative and narrative-style responses.

        "Pomoc techniczna": "Zachowuj się jak pomoc techniczna. Dawaj jasne i precyzyjne instrukcje.",
        # Simulates IT or product support with clear problem-solving guidance.
    },
    "en": {  # English language modes
        "Factual": "Respond briefly and clearly, like a professional technical advisor.",
        # Mirrors "Rzeczowy" mode in English for structured, informative replies.

        "Creative": "Be creative, invent interesting stories, and play with language.",
        # Promotes expressive and entertaining dialogue.

        "Tech Support": "Act as tech support. Provide clear and precise instructions.",
        # Provides troubleshooting and assistance in a straightforward manner.
    }
}
