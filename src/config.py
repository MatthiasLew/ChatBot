# config.py
API_URL = "http://127.0.0.1:1234/v1/chat/completions"

AVAILABLE_MODELS = [
    "deepseek-chat",
    "gpt-3.5-turbo",
    "mistral",
    "phi",
    "zephyr",
]

DEFAULT_MODEL = AVAILABLE_MODELS[0]
