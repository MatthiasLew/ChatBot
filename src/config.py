"""
config.py

This module defines configuration constants used by the chatbot application,
including API connection details and available language models.

Constants:
- API_URL: The base URL of the backend server for chat completion requests.
- AVAILABLE_MODELS: A list of model identifiers available for selection.
- DEFAULT_MODEL: The default model selected at application startup.

This configuration is used for backend communication and dynamic model switching.
"""

API_URL = "http://127.0.0.1:1234/v1/chat/completions"
"""str: Base URL of the local or remote API endpoint used for chat completions."""

AVAILABLE_MODELS = [
    "deepseek-chat",     # Locally hosted or custom model
    "gpt-3.5-turbo",     # OpenAI GPT-3.5 language model
    "mistral",           # Lightweight open-source transformer model
    "phi",               # Compact Microsoft language model
    "zephyr",            # Optimized open-weight transformer (e.g., HuggingFace)
]
"""list[str]: List of supported language model names exposed by the API."""

DEFAULT_MODEL = AVAILABLE_MODELS[0]
"""str: The default model selected on application launch (first in AVAILABLE_MODELS)."""
