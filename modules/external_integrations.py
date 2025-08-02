"""
External Integrations Module for AURORA platform
"""

import streamlit as st
from utils.ai_helpers import get_gemini_response


def lms_integration():
    """Provides information on LMS integration options."""
    prompt = "Explain how to integrate LMS platforms like Moodle, Blackboard, and Canvas with AI-powered tools."
    return get_gemini_response(prompt)


def third_party_integration():
    """Describes how to integrate Google Drive, Notion, and OneNote with AI-driven platforms."""
    prompt = "Describe how to integrate third-party applications like Google Drive, Notion, and OneNote into an AI-powered educational platform."
    return get_gemini_response(prompt)


def api_development():
    """Provides insights on building custom API integrations."""
    prompt = "Explain how developers can use APIs to extend LMS and third-party app functionalities with AI."
    return get_gemini_response(prompt)


def ai_lms_integration():
    """Main LMS integration interface."""
    st.title("AI-Powered LMS & App Integration")

    # LMS Integration Section
    st.header("LMS Integration")
    st.write("Connect AI-powered tools with Moodle, Blackboard, and Canvas.")
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("Learn About LMS Integration"):
            with st.spinner("Getting integration details..."):
                lms_details = lms_integration()
            st.subheader("LMS Integration Guide")
            st.write(lms_details)
    with col2:
        st.markdown("[Visit Moodle](https://moodle.org/)  \n[Blackboard](https://www.blackboard.com/)  \n[Canvas LMS](https://www.instructure.com/canvas)")

    # Third-Party App Integration Section
    st.header("Third-Party App Integration")
    st.write("Seamlessly connect Google Drive, Notion, and OneNote.")
    col3, col4 = st.columns([3, 1])
    with col3:
        if st.button("Explore Third-Party Integration"):
            with st.spinner("Getting integration details..."):
                third_party_details = third_party_integration()
            st.subheader("Supported Third-Party Integrations")
            st.write(third_party_details)
    with col4:
        st.markdown("[Google Drive](https://drive.google.com/)  \n[Notion](https://www.notion.so/)  \n[OneNote](https://www.onenote.com/)")

    # API Development Section
    st.header("APIs for Developers")
    st.write("Extend functionality with custom-built integrations.")
    col5, col6 = st.columns([3, 1])
    with col5:
        if st.button("Learn About API Development"):
            with st.spinner("Getting API development details..."):
                api_details = api_development()
            st.subheader("API Development Guide")
            st.write(api_details)
    with col6:
        st.markdown("[Gemini API](https://ai.google.dev/)  \n[Google Cloud AI](https://cloud.google.com/ai/)  \n[LMS API Docs](https://docs.moodle.org/dev/Web_services)")

    # Downloadable Resources Section
    st.header("Download Integration Guides")
    st.write("Get step-by-step guides on AI-powered LMS & third-party integrations.")
    st.markdown("[Download LMS Integration Guide](https://docs.moodle.org/)  \n[AI & API Development Docs](https://ai.google.dev/)")

    # Footer with AI-Powered Branding
    st.markdown("---")
    st.markdown("**AI-Powered Education | Smarter Integrations | Future-Ready Learning**") 