import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv(override=True)  # Force reload of env vars

# App constants
APP_TITLE = "🔥 Toxicity Tuner"
APP_DESCRIPTION = """
Analyze conversations for toxic behavior and get AI-generated roasts.
Upload text or screenshots to get started.
"""

# Gemini configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY not found in environment variables. "
        "Please check your .env file exists and contains GEMINI_API_KEY=your_key_here"
    )

# Print first few characters of API key for debugging (safely)
print(f"API Key loaded (starts with): {GEMINI_API_KEY[:8]}...")

GEMINI_MODEL = "gemini-2.0-flash-lite"  # For text analysis
GEMINI_VISION_MODEL = "gemini-2.0-flash-lite"  # For image processing

# Gemini safety settings - using correct enum values
SAFETY_SETTINGS = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE"
    }
]

# OCR configuration
TESSERACT_CONFIG = "--psm 6"  # Assume uniform text orientation

# Rate limiting
MAX_REQUESTS_PER_HOUR = 100

# File paths
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True) 