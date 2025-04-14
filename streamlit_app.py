import streamlit as st
import time
from utils.summarizer import summarize_text
from utils.paraphraser import paraphrase_text
from utils.grammar_checker import check_grammar_and_spell

# Set page config
st.set_page_config(
    page_title="NLP Toolbox",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .stTextArea textarea {
        font-size: 16px;
    }
    .stButton button {
        width: 100%;
        height: 3em;
        font-size: 16px;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        margin: 1rem 0;
    }
    .warning-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #fff3cd;
        border: 1px solid #ffeeba;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("About")
    st.markdown("""
    This NLP Toolbox provides three main features:
    
    1. **Text Summarization**: Condense long texts into concise summaries
    2. **Text Paraphrasing**: Generate alternative versions of your text
    3. **Grammar Check**: Identify and correct grammar and spelling issues
    
    Select a tab above to get started!
    """)
    
    st.markdown("---")
    st.markdown("### Settings")
    
    # Global settings
    st.markdown("#### Model Settings")
    use_gpu = st.checkbox("Use GPU if available", value=True)
    cache_results = st.checkbox("Cache results", value=True)
    
    st.markdown("---")
    st.markdown("Made with ❤️ by NLP Toolbox Team")

# Add title and description
st.title("NLP Toolbox 📚")
st.markdown("""
    A powerful suite of Natural Language Processing tools powered by state-of-the-art machine learning models.
    Choose a tool from the tabs below to get started.
""")

# Create tabs for better organization
tab1, tab2, tab3 = st.tabs(["📝 Summarization", "🔄 Paraphrasing", "✓ Grammar Check"])

# Text Summarization
with tab1:
    st.header("Text Summarization")
    st.markdown("""
    Enter your text below and get a concise summary. The model will maintain the key points while reducing the length.
    """)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        summarize_text_input = st.text_area(
            "Enter text to summarize",
            height=200,
            placeholder="Paste your text here..."
        )
    
    with col2:
        max_length = st.slider(
            "Maximum summary length",
            min_value=50,
            max_value=500,
            value=150,
            step=50
        )
    
    if st.button("Generate Summary", key="summarize_btn"):
        if summarize_text_input:
            try:
                with st.spinner("Generating summary..."):
                    start_time = time.time()
                    summary = summarize_text(summarize_text_input, max_length=max_length)
                    end_time = time.time()
                
                st.markdown("### Summary")
                st.markdown(f"""
                    <div class="success-box">
                        <p><strong>Time taken:</strong> {end_time - start_time:.2f} seconds</p>
                        <p><strong>Original length:</strong> {len(summarize_text_input.split())} words</p>
                        <p><strong>Summary length:</strong> {len(summary.split())} words</p>
                    </div>
                """, unsafe_allow_html=True)
                st.write(summary)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter some text to summarize")

# Text Paraphrasing
with tab2:
    st.header("Text Paraphrasing")
    st.markdown("""
    Enter your text below and get alternative versions while maintaining the original meaning.
    """)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        paraphrase_text_input = st.text_area(
            "Enter text to paraphrase",
            height=200,
            placeholder="Paste your text here..."
        )
    
    with col2:
        num_variations = st.slider(
            "Number of variations",
            min_value=1,
            max_value=5,
            value=3,
            step=1
        )
    
    if st.button("Generate Variations", key="paraphrase_btn"):
        if paraphrase_text_input:
            try:
                with st.spinner("Generating variations..."):
                    start_time = time.time()
                    variations = paraphrase_text(paraphrase_text_input, num_return_sequences=num_variations)
                    end_time = time.time()
                
                st.markdown("### Variations")
                st.markdown(f"""
                    <div class="success-box">
                        <p><strong>Time taken:</strong> {end_time - start_time:.2f} seconds</p>
                        <p><strong>Number of variations:</strong> {len(variations)}</p>
                    </div>
                """, unsafe_allow_html=True)
                
                for i, variation in enumerate(variations, 1):
                    st.markdown(f"**Variation {i}:**")
                    st.write(variation)
                    st.markdown("---")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter some text to paraphrase")

# Grammar Check
with tab3:
    st.header("Grammar Check")
    st.markdown("""
    Enter your text below to check for grammar and spelling issues.
    The tool will identify potential problems and suggest improvements.
    """)
    
    grammar_text_input = st.text_area(
        "Enter text to check grammar",
        height=200,
        placeholder="Paste your text here..."
    )
    
    if st.button("Check Grammar", key="grammar_btn"):
        if grammar_text_input:
            try:
                with st.spinner("Checking grammar..."):
                    start_time = time.time()
                    result = check_grammar_and_spell(grammar_text_input)
                    end_time = time.time()
                
                st.markdown("### Analysis Results")
                st.markdown(f"""
                    <div class="success-box">
                        <p><strong>Time taken:</strong> {end_time - start_time:.2f} seconds</p>
                        <p><strong>Text length:</strong> {len(grammar_text_input.split())} words</p>
                    </div>
                """, unsafe_allow_html=True)
                st.write(result)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter some text to check grammar") 