import streamlit as st
from src.config import APP_TITLE, APP_DESCRIPTION
from src.utils.ocr import process_image
from src.utils.text import format_transcript
from src.llm.gemini import analyze_toxicity
from src.ui.components import display_results

def main():
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon="🔥",
        layout="wide"
    )
    
    st.title(APP_TITLE)
    st.markdown(APP_DESCRIPTION)
    
    # Input section
    with st.container():
        st.subheader("Input")
        input_type = st.radio(
            "Choose input type",
            ["Text", "Screenshot"],
            horizontal=True
        )
        
        if input_type == "Text":
            transcript = st.text_area(
                "Paste your conversation here",
                height=200,
                placeholder="Format: Speaker: Message"
            )
        else:
            uploaded_files = st.file_uploader(
                "Upload screenshots",
                type=["png", "jpg", "jpeg"],
                accept_multiple_files=True
            )
            if uploaded_files:
                transcript = process_image(uploaded_files)
            else:
                transcript = ""
        
        context = st.text_input(
            "Context (optional)",
            placeholder="e.g., co-founders, mentor chat"
        )
    
    # Analysis section
    if transcript:
        if st.button("Analyze", type="primary"):
            with st.spinner("Analyzing..."):
                try:
                    results = analyze_toxicity(transcript, context)
                    display_results(results)
                except Exception as e:
                    st.error(f"Error during analysis: {str(e)}")

if __name__ == "__main__":
    main() 