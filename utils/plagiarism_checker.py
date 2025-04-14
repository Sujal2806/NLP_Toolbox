from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

def preprocess_text(text):
    """
    Preprocess text by tokenizing, removing stopwords, and converting to lowercase.
    """
    # Convert to lowercase
    text = text.lower()
    
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Join tokens back into text
    return ' '.join(tokens)

def check_plagiarism(text1, text2):
    """
    Check for plagiarism between two texts using TF-IDF and cosine similarity.
    
    Args:
        text1 (str): First text to compare
        text2 (str): Second text to compare
        
    Returns:
        dict: Dictionary containing similarity score and analysis
    """
    try:
        # Preprocess texts
        processed_text1 = preprocess_text(text1)
        processed_text2 = preprocess_text(text2)
        
        # Create TF-IDF vectorizer
        vectorizer = TfidfVectorizer()
        
        # Transform the texts
        tfidf_matrix = vectorizer.fit_transform([processed_text1, processed_text2])
        
        # Calculate cosine similarity
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        
        # Convert similarity to percentage
        similarity_percentage = round(similarity * 100, 2)
        
        # Determine plagiarism level
        if similarity_percentage < 30:
            level = "Low"
        elif similarity_percentage < 70:
            level = "Medium"
        else:
            level = "High"
        
        return {
            'similarity_percentage': similarity_percentage,
            'plagiarism_level': level,
            'analysis': f"The texts have {similarity_percentage}% similarity. Plagiarism level: {level}"
        }
    except Exception as e:
        return {'error': str(e)} 