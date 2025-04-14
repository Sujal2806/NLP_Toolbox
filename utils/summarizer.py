from transformers import pipeline
import hashlib
import os
import json
import time

# Create a cache directory if it doesn't exist
CACHE_DIR = "cache"
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

# Cache file for summaries
SUMMARY_CACHE_FILE = os.path.join(CACHE_DIR, "summary_cache.json")

# Load the cache if it exists
summary_cache = {}
if os.path.exists(SUMMARY_CACHE_FILE):
    try:
        with open(SUMMARY_CACHE_FILE, 'r', encoding='utf-8') as f:
            summary_cache = json.load(f)
    except:
        summary_cache = {}

def get_cache_key(text, max_length):
    """Generate a cache key for the input parameters."""
    key_string = f"{text}_{max_length}"
    return hashlib.md5(key_string.encode()).hexdigest()

def save_cache():
    """Save the cache to disk."""
    with open(SUMMARY_CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(summary_cache, f)

def summarize_text(text, max_length=150):
    """
    Summarize the input text using a smaller, faster model.
    
    Args:
        text (str): Input text to summarize
        max_length (int): Maximum length of the summary
        
    Returns:
        str: Summarized text
    """
    try:
        # Check if the text is too short to summarize
        if len(text.split()) < 20:
            return "Text is too short to summarize effectively. Please provide a longer text."
        
        # Generate cache key
        cache_key = get_cache_key(text, max_length)
        
        # Check if result is in cache
        if cache_key in summary_cache:
            print("Using cached summary")
            return summary_cache[cache_key]
        
        # Initialize the summarization pipeline with a smaller model
        print("Loading summarizer model...")
        summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn",
            device=-1,  # Use CPU
            max_length=max_length,
            min_length=30,
            do_sample=False  # Deterministic output for faster generation
        )
        
        # Generate summary
        print("Generating summary...")
        start_time = time.time()
        summary = summarizer(text, max_length=max_length, min_length=30)[0]['summary_text']
        end_time = time.time()
        print(f"Summary generated in {end_time - start_time:.2f} seconds")
        
        # Cache the result
        summary_cache[cache_key] = summary
        save_cache()
        
        return summary
    except Exception as e:
        return f"Error in summarization: {str(e)}" 