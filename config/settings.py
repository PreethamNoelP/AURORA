"""
Configuration settings for AURORA - AI-powered Unified Review and Organization for Resourceful Academics
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    # TODO: Add your Gemini API key to .env file
    GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"

# Model Configuration
GEMINI_MODEL = "gemini-2.0-flash"

# File Paths
# TODO: Update these paths according to your project structure
COVER_IMAGE_PATH = "assets/images/cover_image.jpg"
OUTPUT_DIR = "output/"
TEMP_DIR = "temp/"

# Course Recommendations
COURSE_RECOMMENDATIONS = {
    "Data Science": ["Python for Data Science", "Machine Learning Basics", "Deep Learning with TensorFlow"],
    "Web Development": ["HTML & CSS Fundamentals", "JavaScript for Beginners", "React & Redux"],
    "Cybersecurity": ["Ethical Hacking Basics", "Network Security", "Cyber Threat Intelligence"],
    "AI & ML": ["NLP with Transformers", "AI-Powered Chatbots", "Reinforcement Learning"],
}

# Quiz Questions
QUIZ_QUESTIONS = {
    "What is 2 + 2?": "4",
    "What is the capital of France?": "Paris",
    "Who developed Python?": "Guido van Rossum"
}

# AI/ML Keywords for scoring
AI_ML_KEYWORDS = ["AI", "Machine Learning", "Deep Learning", "Neural Networks"]
GEN_AI_KEYWORDS = ["Generative AI", "Transformer Models", "GPT", "BERT"]

# Supported file types
SUPPORTED_FILE_TYPES = ["pdf", "docx"]

# Email configuration
# TODO: Add your email configuration
EMAIL_CONFIG = {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "sender_email": "YOUR_EMAIL@gmail.com",
    "sender_password": "YOUR_APP_PASSWORD"
} 