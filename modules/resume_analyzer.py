"""
Resume Analyzer Module for AURORA platform
"""

import json
import streamlit as st
from utils.ai_helpers import get_gemini_response, perform_sentiment_analysis, score_experience, score_role_fit, suggest_role
from utils.file_handlers import parse_file, write_to_excel, create_temp_file
from config.settings import SUPPORTED_FILE_TYPES


def analyze_resume(file_path):
    """Extracts key details from resume using AI model."""
    try:
        resume_text = parse_file(file_path)
        prompt = f"""
        Extract the following mandatory details from this resume in JSON format:
        - Name
        - Contact details
        - University
        - Year of Study
        - Course
        - Discipline
        - CGPA/Percentage
        - Key Skills
        - Gen AI Experience Score
        - AI/ML Experience Score
        - Supporting Information (certifications, internships, projects)

        Resume text:
        {resume_text}
        """
        response = get_gemini_response(prompt)
        response_text = response.strip()

        # Handle JSON Parsing
        try:
            extracted_data = json.loads(response_text)
        except json.JSONDecodeError:
            json_str = response_text[response_text.find('{'): response_text.rfind('}') + 1]
            extracted_data = json.loads(json_str)

        # Sentiment Analysis
        extracted_data["Sentiment Score"] = perform_sentiment_analysis(resume_text)

        # Experience Scoring
        extracted_data["Experience Scores"] = score_experience(extracted_data.get("Key Skills", ""))

        # Remove Unnecessary Fields
        if "NER" in extracted_data:
            del extracted_data["NER"]

        # Deduplicate Contact Details
        if isinstance(extracted_data.get("Contact details"), list):
            extracted_data["Contact details"] = list(set(extracted_data["Contact details"]))

        return extracted_data

    except Exception as e:
        return {"error": str(e)}


def resume_analyzer_app():
    """Streamlit UI for Resume Analysis."""
    st.title("Resume Builder & Analyzer")

    role_description = st.text_area("Enter Role Description (optional)")
    required_skills_input = st.text_area("Enter Required Skills (comma-separated)", "AI, Machine Learning, Python, SQL")
    uploaded_files = st.file_uploader("Upload Resumes", accept_multiple_files=True, type=SUPPORTED_FILE_TYPES)

    if uploaded_files and st.button("Start Processing"):
        st.write("Processing resumes...")
        results = []
        required_skills = [skill.strip() for skill in required_skills_input.split(",")]

        for uploaded_file in uploaded_files:
            temp_file_path = create_temp_file(uploaded_file)
            if temp_file_path:
                extracted_data = analyze_resume(temp_file_path)
                extracted_data["Role Fit Score"] = score_role_fit(extracted_data.get("Key Skills", ""), required_skills)
                extracted_data["Suggested Role"] = suggest_role(role_description, extracted_data.get("Key Skills", ""))
                results.append(extracted_data)

        if results:
            output_path = write_to_excel(results)
            st.success("Processing complete!")
            
            # Download button
            with open(output_path, "rb") as f:
                st.download_button("Download Results", f.read(), "extracted_resume_data.xlsx")
            
            # Display results
            for result in results:
                st.json(result)
        else:
            st.error("No valid results to process.") 