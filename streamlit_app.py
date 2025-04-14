import streamlit as st
import time
from utils.summarizer import summarize_text
from utils.paraphraser import paraphrase_text
from utils.auto_complete import auto_complete_text
from utils.plagiarism_checker import check_plagiarism

st.set_page_config(
    page_title="NLP Toolbox",
    page_icon="📚",
    layout="wide"
)

st.title("NLP Toolbox 📚")

# Text Summarization
st.header("Text Summarization")
summarize_text_input = st.text_area("Enter text to summarize", height=150)
if st.button("Summarize"):
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
st.header("Text Paraphrasing")
paraphrase_text_input = st.text_area("Enter text to paraphrase", height=150)
if st.button("Paraphrase"):
    if paraphrase_text_input:
        with st.spinner("Generating variations..."):
            start_time = time.time()
            variations = paraphrase_text(paraphrase_text_input, num_variations=3)
            end_time = time.time()
            st.success(f"Variations generated in {end_time - start_time:.2f} seconds")
            for i, variation in enumerate(variations, 1):
                st.write(f"Variation {i}: {variation}")
    else:
        st.warning("Please enter some text to paraphrase")

# Text Completion
st.header("Text Completion")
complete_text_input = st.text_area("Enter text to complete", height=150)
if st.button("Complete"):
    if complete_text_input:
        with st.spinner("Generating completions..."):
            start_time = time.time()
            completions = auto_complete_text(complete_text_input, max_length=50, num_completions=3)
            end_time = time.time()
            st.success(f"Completions generated in {end_time - start_time:.2f} seconds")
            for i, completion in enumerate(completions, 1):
                st.write(f"Completion {i}: {completion}")
    else:
        st.warning("Please enter some text to complete")

# Plagiarism Check
st.header("Plagiarism Check")
plagiarism_text_input = st.text_area("Enter text to check for plagiarism", height=150)
if st.button("Check Plagiarism"):
    if plagiarism_text_input:
        with st.spinner("Checking for plagiarism..."):
            start_time = time.time()
            result = check_plagiarism(plagiarism_text_input)
            end_time = time.time()
            st.success(f"Check completed in {end_time - start_time:.2f} seconds")
            st.write(result)
    else:
        st.warning("Please enter some text to check for plagiarism") 