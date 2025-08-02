"""
Interactive Learning Module for AURORA platform
"""

import streamlit as st
import random
import time
from config.settings import QUIZ_QUESTIONS


def gamification():
    """Gamification feature with points system."""
    st.subheader("Gamification - Earn Points!")
    if "points" not in st.session_state:
        st.session_state.points = 0
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Complete a Task & Earn 10 Points"):
            st.session_state.points += 10
            st.success("+10 points earned!")
    
    with col2:
        if st.button("Study Session & Earn 5 Points"):
            st.session_state.points += 5
            st.success("+5 points earned!")
    
    st.write(f"Your Total Points: **{st.session_state.points}**")
    
    # Achievement system
    if st.session_state.points >= 50:
        st.balloons()
        st.success("Achievement Unlocked: Dedicated Learner!")


def quizzes():
    """Interactive quiz system."""
    st.subheader("Quiz Time!")
    
    if "current_question" not in st.session_state:
        st.session_state.current_question = random.choice(list(QUIZ_QUESTIONS.items()))
    
    question, answer = st.session_state.current_question
    user_answer = st.text_input(f"{question}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Submit Answer"):
            if user_answer.strip().lower() == answer.lower():
                st.success("Correct!")
                st.session_state.points = st.session_state.get("points", 0) + 5
            else:
                st.error(f"Wrong! The correct answer is {answer}.")
    
    with col2:
        if st.button("New Question"):
            st.session_state.current_question = random.choice(list(QUIZ_QUESTIONS.items()))
            st.rerun()


def simulations():
    """Virtual lab simulations."""
    st.subheader("Simple Virtual Lab")
    st.write("Simulating a basic experiment...")
    
    experiment_type = st.selectbox("Choose Experiment:", ["Chemical Reaction", "Physics Simulation", "Biology Lab"])
    
    if st.button("Start Experiment"):
        with st.spinner("Running Experiment..."):
            time.sleep(3)
        st.success("Experiment Completed Successfully!")
        
        # Show results based on experiment type
        if experiment_type == "Chemical Reaction":
            st.info("Result: Reaction completed with 85% efficiency")
        elif experiment_type == "Physics Simulation":
            st.info("Result: Gravity simulation completed successfully")
        else:
            st.info("Result: Cell division observed under microscope")


def case_studies():
    """Interactive case studies."""
    st.subheader("Case Study: Data Breach Handling")
    st.write("You are a security analyst in a company that has suffered a data breach.")
    
    step = st.selectbox("What would be your first step?", 
                       ["Ignore the issue", "Investigate logs", "Inform management", "Shut down all systems"])
    
    if st.button("Submit Decision"):
        if step == "Investigate logs":
            st.success("Good choice! Understanding the breach is crucial.")
            st.session_state.points = st.session_state.get("points", 0) + 10
        elif step == "Inform management":
            st.success("Good communication! Keeping stakeholders informed is important.")
            st.session_state.points = st.session_state.get("points", 0) + 8
        elif step == "Shut down all systems":
            st.warning("Caution: This might cause more disruption than necessary.")
            st.session_state.points = st.session_state.get("points", 0) + 3
        else:
            st.error("Not the best decision. Try again!")


def interactive_learning():
    """Main interactive learning interface."""
    st.title("Interactive Learning")
    
    choice = st.selectbox("Choose a learning module", 
                         ["Gamification", "Quizzes & Assessments", "Simulations & Virtual Labs", 
                          "Case Studies", "Personalized Notes"])
    
    if choice == "Gamification":
        gamification()
    elif choice == "Quizzes & Assessments":
        quizzes()
    elif choice == "Simulations & Virtual Labs":
        simulations()
    elif choice == "Case Studies":
        case_studies()
    elif choice == "Personalized Notes":
        from modules.ai_notes import personalized_notes
        personalized_notes() 