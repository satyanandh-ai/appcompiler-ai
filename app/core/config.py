from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = "AppCompiler AI"
VERSION = "1.0.0"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")