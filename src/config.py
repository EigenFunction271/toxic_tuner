import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# App constants
APP_TITLE = "🔥 Toxicity Tuner"
APP_DESCRIPTION = """
Analyze conversations for toxic behavior and get AI-generated roasts.
Upload text or screenshots to get started.
"""

# Gemini configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-pro"

# OCR configuration
TESSERACT_CONFIG = "--psm 6"  # Assume uniform text orientation

# Rate limiting
MAX_REQUESTS_PER_HOUR = 100

# File paths
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True) 