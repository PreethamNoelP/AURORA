"""
Community Features Module for AURORA platform
"""

import streamlit as st
import urllib.parse
from utils.ai_helpers import get_gemini_response


def mailing_strategies():
    """Returns effective mailing strategies for educational communities."""
    return """
**Effective Mailing Strategies for Educational Communities**
- **Weekly Updates:** Send newsletters with upcoming events, discussions, and expert sessions.
- **Personalized Notifications:** Notify users about relevant Q&A sessions or project updates.
- **Peer Engagement Emails:** Encourage participation through interactive emails.
- **Performance Reports:** Share insights on engagement and learning progress.

**Email Strategy for Effective Communication**
- **Subject Line:** Keep it short & engaging (e.g., "Join Our Live Q&A with Experts!")
- **Personalization:** Address recipients by their name for a personal touch.
- **Call to Action (CTA):** Include links for signing up, joining discussions, or attending live sessions.
- **Timing:** Send emails at optimal times (e.g., Monday mornings or Friday afternoons).
"""


def generate_gmail_link(to_email, subject, message):
    """Creates a direct Gmail compose link with pre-filled recipient, subject, and message."""
    base_url = "https://mail.google.com/mail/?view=cm&fs=1"
    params = {
        "to": to_email,
        "su": subject,
        "body": message
    }
    encoded_params = urllib.parse.urlencode(params)
    return f"{base_url}&{encoded_params}"


def educational_platform():
    """Main educational platform interface."""
    st.title("AI-Powered Educational Hub")
    
    # Discussion Forums
    st.header("Discussion Forums")
    st.write("Engage with peers and mentors in knowledge-sharing discussions.")
    
    forum_topic = st.text_input("Start a new discussion topic:")
    if st.button("Create Discussion"):
        if forum_topic:
            st.success(f"Discussion '{forum_topic}' created successfully!")
        else:
            st.warning("Please enter a discussion topic.")

    # Group Projects
    st.header("Group Projects")
    st.write("Collaborate on assignments, share documents, and enhance teamwork.")
    
    project_name = st.text_input("Create a new group project:")
    if st.button("Create Project"):
        if project_name:
            st.success(f"Project '{project_name}' created! Invite team members to collaborate.")
        else:
            st.warning("Please enter a project name.")

    # Live Expert Q&A
    st.header("Live Expert Q&A")
    st.write("Join industry leaders for insightful Q&A sessions.")
    
    expert_session = st.selectbox("Choose an expert session:", 
                                 ["AI/ML Expert Session", "Data Science Q&A", "Career Guidance"])
    if st.button("Join Session"):
        st.success(f"Successfully joined {expert_session}!")

    # Mailing Strategies
    st.header("Mailing Strategies")
    st.write(mailing_strategies())

    # Email Sending Feature
    st.subheader("Generate Email Link")
    recipient_email = st.text_input("Recipient Email:")
    email_subject = st.text_input("Email Subject:")
    email_body = st.text_area("Email Content:")

    if st.button("Generate Email Link"):
        if recipient_email and email_subject and email_body:
            gmail_link = generate_gmail_link(recipient_email, email_subject, email_body)
            st.markdown(f"[Click here to open Gmail with your email pre-filled]({gmail_link})", 
                       unsafe_allow_html=True)
        else:
            st.warning("Please fill in all email details before generating the link.")

    # AI-Powered Educational Assistance
    st.header("AI-Powered Educational Assistance")
    user_query = st.text_area("Ask AI about any educational concern:")
    if st.button("Get AI Response"):
        if user_query:
            with st.spinner("Getting AI response..."):
                response = get_gemini_response(user_query)
            st.subheader("AI Response:")
            st.write(response)
        else:
            st.warning("Please enter a question.")


def chatbot_assistant():
    """AI Chatbot Assistant feature."""
    st.title("AI Chatbot Assistant")
    st.write("Ask your academic questions and get AI-powered answers.")
    
    user_query = st.text_input("Ask a question:")
    if user_query:
        with st.spinner("Processing your question..."):
            response = get_gemini_response(user_query)
        st.subheader("AI Response:")
        st.write(response)
    else:
        st.info("Type your question above to get started!") 