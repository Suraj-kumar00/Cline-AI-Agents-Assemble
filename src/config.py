"""Configuration management for InfraAgent"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# AI Model Configuration - Using Gemini 2.5 Flash
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
GEMINI_MAX_TOKENS = int(os.getenv("GEMINI_MAX_TOKENS", "8192"))

# Output Configuration
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "/app/output")
DEFAULT_NAMESPACE = os.getenv("DEFAULT_NAMESPACE", "default")

# Validation
if not GEMINI_API_KEY:
    print("⚠️  WARNING: GEMINI_API_KEY not set. Please set it in .env file or environment.")
