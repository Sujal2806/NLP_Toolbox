import streamlit as st
from utils.paraphraser import paraphrase
from utils.summarizer import summarize_text
from utils.grammar_checker import correct_grammar

st.set_page_config(page_title="NLP Toolbox", page_icon="📚", layout="wide")

st.title("📚 NLP Toolbox")
st.markdown("A collection of powerful NLP tools for text processing and enhancement.")

# Sidebar for tool selection
tool = st.sidebar.selectbox(
    "Select Tool",
    ["Paraphraser", "Summarizer", "Grammar Checker"]
)

# Main content area
if tool == "Paraphraser":
    st.header("🔄 Text Paraphraser")
    st.markdown("Generate different versions of your text while maintaining the same meaning.")
    
    text = st.text_area("Enter text to paraphrase:", height=150)
    num_sequences = st.slider("Number of paraphrased versions:", 1, 10, 5)
    
    if st.button("Generate Paraphrases"):
        if text:
            with st.spinner("Generating paraphrases..."):
                paraphrases = paraphrase(text, num_return_sequences=num_sequences)
                for i, para in enumerate(paraphrases, 1):
                    st.write(f"{i}. {para}")
        else:
            st.warning("Please enter some text to paraphrase.")

elif tool == "Summarizer":
    st.header("📝 Text Summarizer")
    st.markdown("Create concise summaries of long texts.")
    
    text = st.text_area("Enter text to summarize:", height=200)
    col1, col2 = st.columns(2)
    with col1:
        max_length = st.slider("Maximum summary length:", 50, 200, 130)
    with col2:
        min_length = st.slider("Minimum summary length:", 10, 100, 30)
    
    if st.button("Generate Summary"):
        if text:
            with st.spinner("Generating summary..."):
                summary = summarize_text(text, max_length=max_length, min_length=min_length)
                st.subheader("Summary:")
                st.write(summary)
        else:
            st.warning("Please enter some text to summarize.")

else:  # Grammar Checker
    st.header("✍️ Grammar Checker")
    st.markdown("Check and correct grammar and spelling errors in your text.")
    
    text = st.text_area("Enter text to check:", height=150)
    
    if st.button("Check Grammar"):
        if text:
            with st.spinner("Checking grammar..."):
                corrected = correct_grammar(text)
                st.subheader("Corrected Text:")
                st.write(corrected)
        else:
            st.warning("Please enter some text to check.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit and Transformers")
