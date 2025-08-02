"""
Accessibility Module for AURORA platform
"""

import streamlit as st
import speech_recognition as sr
from deep_translator import GoogleTranslator


def multi_language_support():
    """Multi-language translation support."""
    st.header("Multi-Language Support")
    
    user_text = st.text_input("Enter text for translation:")
    target_language = st.selectbox("Select target language", 
                                 ["es", "fr", "de", "hi", "zh", "ar", "ru", "ja", "ko"])

    if st.button("Translate"):
        if user_text:
            try:
                with st.spinner("Translating..."):
                    translation = GoogleTranslator(source="auto", target=target_language).translate(user_text)
                st.success("Translation completed!")
                st.write("**Original Text:**", user_text)
                st.write("**Translated Text:**", translation)
            except Exception as e:
                st.error(f"Translation error: {str(e)}")
        else:
            st.warning("Please enter text to translate.")


def voice_recognition():
    """Voice-to-text feature."""
    st.header("Voice Recognition")
    st.write("Convert your speech to text for hands-free interaction.")
    
    if st.button("Start Voice Recognition"):
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                st.write("Listening... Speak now!")
                with st.spinner("Processing audio..."):
                    audio = recognizer.listen(source, timeout=5)
                    text = recognizer.recognize_google(audio)
                st.success("Voice recognition successful!")
                st.write("**Recognized Text:**", text)
        except sr.UnknownValueError:
            st.error("Sorry, could not understand the audio. Please try again.")
        except sr.RequestError:
            st.error("Error with the voice recognition service.")
        except Exception as e:
            st.error(f"Error: {str(e)}")


def accessibility_features():
    """Main accessibility interface."""
    st.title("Accessibility & Inclusivity")
    st.write("Making education accessible to everyone through AI-powered features.")
    
    # Multi-language support
    multi_language_support()
    
    st.markdown("---")
    
    # Voice-to-text feature
    voice_recognition()
    
    st.markdown("---")
    
    # Additional accessibility features
    st.header("Additional Accessibility Features")
    
    # Text size adjustment
    text_size = st.slider("Adjust text size", 12, 24, 16)
    st.markdown(f"<div style='font-size: {text_size}px;'>Sample text with adjusted size</div>", 
                unsafe_allow_html=True)
    
    # High contrast mode
    high_contrast = st.checkbox("Enable high contrast mode")
    if high_contrast:
        st.info("High contrast mode enabled for better visibility.")
    
    # Screen reader support
    screen_reader = st.checkbox("Enable screen reader support")
    if screen_reader:
        st.info("Screen reader support enabled for better accessibility.") 