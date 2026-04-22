import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    EMR_BASE_URL = os.getenv("EMR_BASE_URL")
    EMR_TOKEN = os.getenv("EMR_TOKEN")
    EMR_TIMEOUT = int(os.getenv("EMR_TIMEOUT", 5))

    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
    OLLAMA_TEMPERATURE = float(os.getenv("OLLAMA_TEMPERATURE", 0.2))

settings = Settings()