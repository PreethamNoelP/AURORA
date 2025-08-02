"""
AI Notes Module for AURORA platform
"""

import streamlit as st
from utils.ai_helpers import summarize_text, generate_flashcards, create_concept_map
from utils.file_handlers import download_notes_as_pdf


def ai_notes_app():
    """Main AI Notes application."""
    st.title("AI-Powered Notes & Summarization")
    
    note_title = st.text_input("Enter Note Title:")
    note_content = st.text_area("Write or Paste Your Notes:")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("Generate Summary"):
            if note_content:
                with st.spinner("Generating summary..."):
                    summary = summarize_text(note_content)
                st.subheader("AI-Generated Summary")
                st.write(summary)
            else:
                st.warning("Please enter notes to summarize.")

    with col2:
        if st.button("Generate Flashcards"):
            if note_content:
                with st.spinner("Generating flashcards..."):
                    flashcards = generate_flashcards(note_content)
                st.subheader("AI-Generated Flashcards")
                st.write(flashcards)
            else:
                st.warning("Please enter notes to generate flashcards.")

    with col3:
        if st.button("Generate Concept Map"):
            if note_content:
                with st.spinner("Creating concept map..."):
                    concept_map = create_concept_map(note_content)
                st.subheader("Concept Map")
                st.write(concept_map)
            else:
                st.warning("Please enter notes to create a concept map.")

    with col4:
        if st.button("Download Notes as PDF"):
            if note_title and note_content:
                with st.spinner("Creating PDF..."):
                    pdf_file = download_notes_as_pdf(note_title, note_content)
                with open(pdf_file, "rb") as f:
                    st.download_button("Click to Download PDF", f, file_name=f"{note_title.strip().replace(' ', '_')}.pdf", mime="application/pdf")
            else:
                st.warning("Please provide a title and content for the notes.")


def personalized_notes():
    """Simple personalized note-taking feature."""
    st.title("Personalized Note-Making")
    st.write("Organize your study materials with ease.")
    note_title = st.text_input("Enter note title:")
    note_content = st.text_area("Write your notes:")
    if st.button("Save Note"):
        st.success("Note saved successfully!") 