"""
AURORA - AI-powered Unified Review and Organization for Resourceful Academics
Main Application File
"""

import streamlit as st
import subprocess
import sys
import spacy

# Set page configuration
st.set_page_config(
    page_title="AURORA – AI-powered Unified Review and Organization for Resourceful Academics", 
    layout="wide"
)

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

# Import modules
from modules.resume_analyzer import resume_analyzer_app
from modules.ai_notes import ai_notes_app
from modules.interactive_learning import interactive_learning
from modules.community_features import educational_platform, chatbot_assistant
from modules.research_tools import ai_research_platform
from modules.accessibility import accessibility_features
from modules.external_integrations import ai_lms_integration
from modules.career_development import ai_career_development
from modules.personalization import ai_personalization

# Main title
st.title("AURORA – AI-powered Unified Review and Organization for Resourceful Academics")

# Sidebar Navigation
tabs = [
    "Home", 
    "AI-Powered Personalization", 
    "Interactive Learning", 
    "AI Notes & Summarization", 
    "Community Features", 
    "AI Research Tools", 
    "Accessibility & Inclusivity", 
    "External Integrations", 
    "Career & Skill Development", 
    "Resume Builder"
]

choice = st.sidebar.radio("Select a Feature", tabs)

# Main application logic
if choice == "Home":
    st.write("Welcome to the next-generation AI-driven educational ecosystem.")
    st.write("**AURORA** is your comprehensive AI-powered learning companion.")
    
    # Feature highlights
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**AI-Powered Personalization**\nAdaptive learning paths tailored to your progress")
    with col2:
        st.info("**Interactive Learning**\nGamified learning with quizzes and simulations")
    with col3:
        st.info("**AI Research Tools**\nAdvanced research and resource curation")

elif choice == "AI-Powered Personalization":
    ai_personalization()

elif choice == "Interactive Learning":
    interactive_learning()

elif choice == "AI Notes & Summarization":
    ai_notes_app()

elif choice == "Community Features":
    educational_platform()

elif choice == "AI Research Tools":
    ai_research_platform()

elif choice == "Accessibility & Inclusivity":
    accessibility_features()

elif choice == "External Integrations":
    ai_lms_integration()

elif choice == "Career & Skill Development":
    ai_career_development()

elif choice == "Resume Builder":
    resume_analyzer_app()

# Footer
st.sidebar.markdown("---")
st.sidebar.write("**Powered by AI** | Tailored for Personalized Learning & Growth")

# Add some helpful information in the sidebar
st.sidebar.markdown("### Quick Tips")
st.sidebar.info("Use the AI features to enhance your learning experience")
st.sidebar.info("Track your progress with personalized analytics")
st.sidebar.info("Connect with peers through community features") 