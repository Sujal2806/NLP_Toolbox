from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import hashlib
import os
import json
import time
import torch

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

def get_cache_key(text, max_length, min_length):
    """Generate a cache key for the input parameters."""
    key_string = f"{text}_{max_length}_{min_length}"
    return hashlib.md5(key_string.encode()).hexdigest()

def save_cache():
    """Save the cache to disk."""
    with open(SUMMARY_CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(summary_cache, f)

def summarize_text(text, max_length=130, min_length=30):
    """
    Summarize the given text using the BART model.
    
    Args:
        text (str): Text to summarize
        max_length (int): Maximum length of the summary
        min_length (int): Minimum length of the summary
        
    Returns:
        str: Summarized text
    """
    try:
        # Initialize model and tokenizer
        model_name = "facebook/bart-large-cnn"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        
        # Tokenize input text
        inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
        
        # Generate summary
        outputs = model.generate(
            **inputs,
            max_length=max_length,
            min_length=min_length,
            num_beams=4,
            length_penalty=2.0,
            early_stopping=True
        )
        
        # Decode and return the summary
        summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return summary
        
    except Exception as e:
        return f"Error in summarization: {str(e)}" 