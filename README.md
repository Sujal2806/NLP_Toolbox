# NLP Toolbox

A comprehensive Natural Language Processing toolbox that combines multiple features in one application.

## Features

1. Text Summarization
2. Grammar and Spell Checker
3. Sentence Auto Completion
4. Plagiarism Checker
5. Text Paraphraser

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Download required NLTK data:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('wordnet')
   ```
4. Download SpaCy model:
   ```
   python -m spacy download en_core_web_sm
   ```

## Running the Application

1. Start the Flask backend:
   ```
   python app.py
   ```
2. Start the Streamlit frontend:
   ```
   streamlit run streamlit_app.py
   ```

## Project Structure

- `app.py`: Flask backend server
- `streamlit_app.py`: Streamlit frontend
- `utils/`: Utility functions for each feature
  - `summarizer.py`
  - `grammar_checker.py`
  - `auto_complete.py`
  - `plagiarism_checker.py`
  - `paraphraser.py`
- `templates/`: HTML templates
- `static/`: Static assets