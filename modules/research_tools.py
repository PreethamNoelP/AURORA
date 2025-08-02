"""
AI Research Tools Module for AURORA platform
"""

import streamlit as st
from utils.ai_helpers import extract_text_insights, ai_search_engine, rag_based_query


def ai_research_platform():
    """Main AI research platform interface."""
    st.title("AI-Driven Research & Resource Curation")
    
    # Automated Text Extraction
    st.header("Automated Text Extraction")
    st.write("AI extracts key insights from documents.")

    text_input = st.text_area("Paste Document Text:")
    if st.button("Extract Insights"):
        if text_input:
            with st.spinner("Extracting insights..."):
                insights = extract_text_insights(text_input)
            st.subheader("Extracted Key Insights")
            st.write(insights)
        else:
            st.warning("Please enter text to extract insights.")

    # AI-Powered Search Engine
    st.header("AI-Powered Search Engine")
    st.write("Smart search understanding natural queries.")

    search_query = st.text_input("Enter Search Query:")
    if st.button("Search AI Knowledge Base"):
        if search_query:
            with st.spinner("Searching..."):
                search_results = ai_search_engine(search_query)
            st.subheader("AI Search Results")
            st.write(search_results)
        else:
            st.warning("Please enter a search query.")

    # RAG-Based Information Retrieval
    st.header("RAG-Based Information Retrieval")
    st.write("AI-driven structured and unstructured data queries.")

    rag_query = st.text_input("Enter Query for RAG-based Retrieval:")
    if st.button("Retrieve Information"):
        if rag_query:
            with st.spinner("Retrieving information..."):
                rag_results = rag_based_query(rag_query)
            st.subheader("AI-Generated Information")
            st.write(rag_results)
        else:
            st.warning("Please enter a query for retrieval.")

    # Research Analytics
    st.header("Research Analytics")
    st.write("Track your research progress and insights.")
    
    research_topic = st.text_input("Enter your research topic:")
    if st.button("Analyze Research"):
        if research_topic:
            st.info(f"Research analysis for '{research_topic}' would be displayed here.")
            st.progress(0.75)
            st.success("Research analysis completed!")
        else:
            st.warning("Please enter a research topic.") 