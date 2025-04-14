from textblob import TextBlob
import re
import hashlib
import os
import json
import time

# Create a cache directory if it doesn't exist
CACHE_DIR = "cache"
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

# Cache file for grammar checks
GRAMMAR_CACHE_FILE = os.path.join(CACHE_DIR, "grammar_cache.json")

# Load the cache if it exists
grammar_cache = {}
if os.path.exists(GRAMMAR_CACHE_FILE):
    try:
        with open(GRAMMAR_CACHE_FILE, 'r', encoding='utf-8') as f:
            grammar_cache = json.load(f)
    except:
        grammar_cache = {}

def get_cache_key(text):
    """Generate a cache key for the input text."""
    return hashlib.md5(text.encode()).hexdigest()

def save_cache():
    """Save the cache to disk."""
    with open(GRAMMAR_CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(grammar_cache, f)

def check_grammar_and_spell(text):
    """
    Check grammar and spelling in the input text using TextBlob.
    
    Args:
        text (str): Input text to check
        
    Returns:
        str: Grammar and spelling analysis
    """
    try:
        # Check if the text is too short
        if len(text.split()) < 3:
            return "Text is too short to check grammar effectively. Please provide a longer text."
        
        # Generate cache key
        cache_key = get_cache_key(text)
        
        # Check if result is in cache
        if cache_key in grammar_cache:
            print("Using cached grammar check")
            return grammar_cache[cache_key]
        
        # Process the text
        print("Checking grammar and spelling...")
        start_time = time.time()
        
        # Create a TextBlob object
        blob = TextBlob(text)
        
        # Check for spelling errors
        spelling_errors = []
        for word in blob.words:
            if word.spellcheck()[0][0] != word:
                spelling_errors.append(word)
        
        # Check for grammar issues
        grammar_issues = []
        for sentence in blob.sentences:
            # Check for subject-verb agreement
            if sentence.tags:
                has_subject = False
                has_verb = False
                for word, tag in sentence.tags:
                    if tag.startswith('NN'):
                        has_subject = True
                    if tag.startswith('VB'):
                        has_verb = True
                if not (has_subject and has_verb):
                    grammar_issues.append(f"Possible missing subject or verb: '{sentence}'")
        
        # Format the results
        result = "Grammar and Spelling Analysis:\n\n"
        
        if spelling_errors:
            result += "Spelling Issues:\n"
            for word in spelling_errors:
                result += f"- '{word}'\n"
        else:
            result += "No spelling issues found.\n"
        
        result += "\n"
        
        if grammar_issues:
            result += "Grammar Issues:\n"
            for issue in grammar_issues:
                result += f"- {issue}\n"
        else:
            result += "No grammar issues found.\n"
        
        end_time = time.time()
        print(f"Grammar check completed in {end_time - start_time:.2f} seconds")
        
        # Cache the result
        grammar_cache[cache_key] = result
        save_cache()
        
        return result
    except Exception as e:
        return f"Error in grammar check: {str(e)}" 