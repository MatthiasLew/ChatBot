# config.py

# Base URL of the local or remote API endpoint for chat completions.
# Adjust this value if the backend server address or port changes.
API_URL = "http://127.0.0.1:1234/v1/chat/completions"

# List of available language models supported by the application.
# These model names should match those exposed by the API.
AVAILABLE_MODELS = [
    "deepseek-chat",     # Local or custom model
    "gpt-3.5-turbo",     # OpenAI GPT-3.5 model
    "mistral",           # Lightweight transformer model
    "phi",               # Compact Microsoft model
    "zephyr",            # Fast open-weight model (e.g., HuggingFace variant)
]

# Default model to use when the application starts.
# This should be one of the models listed in AVAILABLE_MODELS.
DEFAULT_MODEL = AVAILABLE_MODELS[0]
