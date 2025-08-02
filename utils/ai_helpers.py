"""
AI Helper functions for AURORA platform
"""

import google.generativeai as genai
from config.settings import GEMINI_API_KEY, GEMINI_MODEL
import json
from textblob import TextBlob
from config.settings import AI_ML_KEYWORDS, GEN_AI_KEYWORDS


def configure_gemini():
    """Configure Gemini API with the provided key."""
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        return genai.GenerativeModel(GEMINI_MODEL)
    except Exception as e:
        print(f"Error configuring Gemini: {e}")
        return None


def get_gemini_response(prompt):
    """Fetch AI-generated responses using Gemini API."""
    try:
        model = configure_gemini()
        if model:
            response = model.generate_content(prompt)
            return response.text
        else:
            return "Error: Could not configure AI model"
    except Exception as e:
        return f"Error: {str(e)}"


def perform_sentiment_analysis(text):
    """Performs sentiment analysis on text."""
    try:
        return TextBlob(text).sentiment.polarity
    except Exception as e:
        print(f"Error in sentiment analysis: {e}")
        return 0.0


def score_experience(key_skills):
    """Scores experience based on AI/ML and GenAI keywords."""
    try:
        if isinstance(key_skills, list):
            key_skills = " ".join(key_skills)
        
        ai_ml_score = sum(1 for word in AI_ML_KEYWORDS if word.lower() in key_skills.lower())
        gen_ai_score = sum(1 for word in GEN_AI_KEYWORDS if word.lower() in key_skills.lower())
        
        return {"AI/ML Score": ai_ml_score, "Gen AI Score": gen_ai_score}
    except Exception as e:
        print(f"Error scoring experience: {e}")
        return {"AI/ML Score": 0, "Gen AI Score": 0}


def score_role_fit(key_skills, required_skills):
    """Calculates match percentage between resume skills and required job skills."""
    try:
        if isinstance(key_skills, list):
            key_skills = " ".join(key_skills)
        
        if not required_skills:
            return 0
            
        match_count = sum(1 for skill in required_skills if skill.lower() in key_skills.lower())
        return (match_count / len(required_skills)) * 100
    except Exception as e:
        print(f"Error calculating role fit: {e}")
        return 0


def suggest_role(role_description, key_skills):
    """Suggests job suitability based on role description and key skills."""
    try:
        if not role_description:
            return "Role description is missing. Please provide a description."

        if isinstance(key_skills, list):
            key_skills = " ".join(key_skills)

        match_count = sum(1 for skill in role_description.split() if skill.lower() in key_skills.lower())

        if match_count > 3:
            return "This resume is a good fit for the specified role."
        elif match_count > 1:
            return "This resume has some relevant experience for the role."
        else:
            return "This resume may not be well-suited for the role."
    except Exception as e:
        print(f"Error suggesting role: {e}")
        return "Error analyzing role fit"


def summarize_text(text):
    """Generates a summary of the input text using Gemini API."""
    prompt = f"Summarize this lecture in bullet points:\n{text}"
    return get_gemini_response(prompt)


def generate_flashcards(text):
    """Creates AI-generated flashcards from the given text."""
    prompt = f"Generate 5 flashcards with questions and answers from this text:\n{text}"
    return get_gemini_response(prompt)


def create_concept_map(text):
    """Generates a concept map outline for key topics in the text."""
    prompt = f"Create a concept map structure with main ideas and subtopics based on this text:\n{text}"
    return get_gemini_response(prompt)


def extract_text_insights(text):
    """Extracts key insights from documents using AI."""
    prompt = f"Extract key insights from the following document:\n{text}"
    return get_gemini_response(prompt)


def ai_search_engine(query):
    """Performs AI-powered search for relevant information."""
    prompt = f"Provide relevant research information based on this query:\n{query}"
    return get_gemini_response(prompt)


def rag_based_query(query):
    """Retrieves structured and unstructured data using RAG approach."""
    prompt = f"Retrieve structured and unstructured data insights for:\n{query}"
    return get_gemini_response(prompt) 