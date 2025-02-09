import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-api-key-here")
DATA_STORAGE_PATH = os.getenv("DATA_STORAGE_PATH", "./data/")
