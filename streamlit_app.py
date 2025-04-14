import streamlit as st
import time
from utils.summarizer import summarize_text
from utils.paraphraser import paraphrase_text
from utils.grammar_checker import check_grammar_and_spell

# Set page config
st.set_page_config(
    page_title="NLP Toolbox",
    page_icon="📚",
    layout="wide"
)

# Add title and description
st.title("NLP Toolbox 📚")
st.markdown("Utilized machine learning models and NLP algorithms to improve grammar correction, paraphrasing, and text summarization")

# Create tabs for better organization
tab1, tab2, tab3 = st.tabs(["Summarization", "Paraphrasing", "Grammar Check"])

# Text Summarization
with tab1:
    st.header("Text Summarization")
    summarize_text_input = st.text_area("Enter text to summarize", height=150)
    if st.button("Summarize", key="summarize_btn"):
        if summarize_text_input:
            with st.spinner("Generating summary..."):
                start_time = time.time()
                summary = summarize_text(summarize_text_input, max_length=150)
                end_time = time.time()
                st.success(f"Summary generated in {end_time - start_time:.2f} seconds")
                st.write(summary)
        else:
            st.warning("Please enter some text to summarize")

# Text Paraphrasing
with tab2:
    st.header("Text Paraphrasing")
    paraphrase_text_input = st.text_area("Enter text to paraphrase", height=150)
    if st.button("Paraphrase", key="paraphrase_btn"):
        if paraphrase_text_input:
            with st.spinner("Generating variations..."):
                start_time = time.time()
                variations = paraphrase_text(paraphrase_text_input, num_return_sequences=3)
                end_time = time.time()
                st.success(f"Variations generated in {end_time - start_time:.2f} seconds")
                for i, variation in enumerate(variations, 1):
                    st.write(f"Variation {i}: {variation}")
        else:
            st.warning("Please enter some text to paraphrase")

# Grammar Check
with tab3:
    st.header("Grammar Check")
    grammar_text_input = st.text_area("Enter text to check grammar", height=150)
    if st.button("Check Grammar", key="grammar_btn"):
        if grammar_text_input:
            with st.spinner("Checking grammar..."):
                start_time = time.time()
                result = check_grammar_and_spell(grammar_text_input)
                end_time = time.time()
                st.success(f"Check completed in {end_time - start_time:.2f} seconds")
                st.write(result)
        else:
            st.warning("Please enter some text to check grammar") 