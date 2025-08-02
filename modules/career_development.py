"""
Career Development Module for AURORA platform
"""

import streamlit as st
from utils.ai_helpers import get_gemini_response


def job_matching():
    """Generates AI-powered job and internship recommendations."""
    prompt = "Suggest top AI-driven job and internship matching strategies for students and professionals."
    return get_gemini_response(prompt)


def resume_portfolio_builder():
    """Provides insights on building strong resumes and portfolios."""
    prompt = "Explain how to create an AI-optimized resume and portfolio with key elements for job applications."
    return get_gemini_response(prompt)


def skill_certifications():
    """Suggests micro-certifications for AI, Data Science, and emerging tech fields."""
    prompt = "Recommend top skill-based micro-certifications for AI, Data Science, and emerging technologies."
    return get_gemini_response(prompt)


def ai_career_development():
    """Main career development interface."""
    st.title("Career & Skill Development")

    # AI-Driven Job Matching Section
    st.header("AI-Driven Internship & Job Matching")
    st.write("Leverage AI to find the best job and internship opportunities tailored to your skills.")
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("Find AI-Powered Job Matches"):
            with st.spinner("Finding job matches..."):
                job_details = job_matching()
            st.subheader("Job & Internship Recommendations")
            st.write(job_details)
    with col2:
        st.markdown("[LinkedIn Jobs](https://www.linkedin.com/jobs/)  \n[AI Job Portal](https://ai.google.dev/)  \n[Indeed](https://www.indeed.com/)")

    # Resume & Portfolio Builder Section
    st.header("Resume & Portfolio Builder")
    st.write("Create professional resumes and portfolios with AI-powered suggestions.")
    col3, col4 = st.columns([3, 1])
    with col3:
        if st.button("Generate Resume & Portfolio Tips"):
            with st.spinner("Generating tips..."):
                resume_details = resume_portfolio_builder()
            st.subheader("AI Resume & Portfolio Guide")
            st.write(resume_details)
    with col4:
        st.markdown("[Resume Templates](https://zety.com/resume-builder)  \n[Portfolio Hosting](https://www.github.io/)  \n[Canva Resume Builder](https://www.canva.com/resumes/templates/)")

    # Skill-Based Micro-Certifications Section
    st.header("Skill-Based Micro-Certifications")
    st.write("Earn industry-recognized certifications in AI, Data Science, and more.")
    col5, col6 = st.columns([3, 1])
    with col5:
        if st.button("Discover Certification Programs"):
            with st.spinner("Finding certification programs..."):
                certification_details = skill_certifications()
            st.subheader("AI & Data Science Certifications")
            st.write(certification_details)
    with col6:
        st.markdown("[Coursera AI Courses](https://www.coursera.org/)  \n[Udacity Nanodegrees](https://www.udacity.com/)  \n[Google AI Certifications](https://cloud.google.com/training/)")

    # Downloadable Resources Section
    st.header("Download Career Guides")
    st.write("Get expert career guides, resume templates, and certification roadmaps.")
    st.markdown("[AI Career Guide](https://ai.google.dev/)  \n[Resume Writing Tips](https://www.linkedin.com/pulse/resume-tips/)")

    # Footer with AI Branding
    st.markdown("---")
    st.markdown("**AI-Powered Careers | Smart Matching | Future-Ready Skills**") 