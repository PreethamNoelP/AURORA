"""
AI-Powered Personalization Module for AURORA platform
"""

import streamlit as st
import random
from utils.ai_helpers import get_gemini_response
from config.settings import COURSE_RECOMMENDATIONS


def adaptive_learning_paths():
    """Adaptive learning paths based on user progress."""
    st.subheader("Adaptive Learning Paths")
    st.write("AI analyzes your learning behavior and customizes a personalized learning roadmap.")
    
    user_progress = st.slider("How much progress have you made in your current course?", 0, 100, 50)
    
    if user_progress < 30:
        st.info("Recommendation: Start with foundational topics and introductory quizzes.")
    elif user_progress < 70:
        st.info("Recommendation: Engage in hands-on projects and interactive simulations.")
    else:
        st.info("Recommendation: Move to advanced topics and real-world case studies.")


def ai_tutors_chatbots():
    """AI Tutors & Chatbots feature."""
    st.subheader("AI Tutors & Chatbots")
    user_query = st.text_input("Ask your AI Tutor a question:")

    if st.button("Get AI Answer"):
        if user_query.strip():
            with st.spinner("Getting AI response..."):
                ai_response = get_gemini_response(user_query)
            st.success("AI Response:")
            st.write(ai_response)
        else:
            st.warning("Please enter a question.")


def personalized_recommendations():
    """Personalized course recommendations."""
    st.subheader("Personalized Recommendations")
    user_interest = st.selectbox("Select Your Area of Interest:", list(COURSE_RECOMMENDATIONS.keys()))

    if st.button("Get AI Recommendations"):
        with st.spinner("Generating recommendations..."):
            recommended_courses = random.sample(COURSE_RECOMMENDATIONS[user_interest], 
                                            len(COURSE_RECOMMENDATIONS[user_interest]))
        st.success("Recommended Courses for You:")
        for course in recommended_courses:
            st.write(f"• {course}")


def ai_personalization():
    """Main AI personalization interface."""
    st.title("AI-Powered Personalization")
    st.write("Harness AI-driven solutions to enhance your learning experience.")

    # Adaptive Learning Paths
    adaptive_learning_paths()
    
    st.markdown("---")
    
    # AI Tutors & Chatbots
    ai_tutors_chatbots()
    
    st.markdown("---")
    
    # Personalized Course Recommendations
    personalized_recommendations()
    
    st.markdown("---")
    
    # Learning Analytics
    st.subheader("Learning Analytics")
    st.write("Track your learning progress and get personalized insights.")
    
    # Sample analytics dashboard
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Study Hours", "24", "2")
    with col2:
        st.metric("Courses Completed", "3", "1")
    with col3:
        st.metric("Quiz Score", "85%", "5%")
    
    # Learning path visualization
    st.subheader("Your Learning Path")
    st.progress(0.65)
    st.info("You're 65% through your personalized learning journey!") 