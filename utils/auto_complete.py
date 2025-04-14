from transformers import pipeline
import hashlib
import os
import json
import time

# Create a cache directory if it doesn't exist
CACHE_DIR = "cache"
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

# Cache file for completions
COMPLETION_CACHE_FILE = os.path.join(CACHE_DIR, "completion_cache.json")

# Load the cache if it exists
completion_cache = {}
if os.path.exists(COMPLETION_CACHE_FILE):
    try:
        with open(COMPLETION_CACHE_FILE, 'r', encoding='utf-8') as f:
            completion_cache = json.load(f)
    except:
        completion_cache = {}

def get_cache_key(text, max_length, num_return_sequences):
    """Generate a cache key for the input parameters."""
    key_string = f"{text}_{max_length}_{num_return_sequences}"
    return hashlib.md5(key_string.encode()).hexdigest()

def save_cache():
    """Save the cache to disk."""
    with open(COMPLETION_CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(completion_cache, f)

def auto_complete_text(text, max_length=50, num_return_sequences=3):
    """
    Generate text completions for the input text.
    
    Args:
        text (str): Input text to complete
        max_length (int): Maximum length of the completion
        num_return_sequences (int): Number of different completions to generate
        
    Returns:
        list: List of possible completions
    """
    try:
        # Check if the text is too short
        if len(text.split()) < 3:
            return ["Please provide a longer text for better completions."]
        
        # Generate cache key
        cache_key = get_cache_key(text, max_length, num_return_sequences)
        
        # Check if result is in cache
        if cache_key in completion_cache:
            print("Using cached completions")
            return completion_cache[cache_key]
        
        # Initialize the text generation pipeline with a smaller model
        print("Loading auto-completion model...")
        generator = pipeline('text-generation', model='gpt2', device=-1)
        
        # Generate completions
        print("Generating completions...")
        start_time = time.time()
        completions = generator(
            text,
            max_length=len(text.split()) + max_length,
            num_return_sequences=num_return_sequences,
            pad_token_id=50256,
            do_sample=True,
            temperature=0.7
        )
        end_time = time.time()
        print(f"Completions generated in {end_time - start_time:.2f} seconds")
        
        # Extract and clean the generated text
        results = []
        for completion in completions:
            generated_text = completion['generated_text']
            # Remove the input text from the completion
            completion_text = generated_text[len(text):].strip()
            if completion_text:
                results.append(completion_text)
        
        # Cache the result
        completion_cache[cache_key] = results
        save_cache()
        
        return results
    except Exception as e:
        return [f"Error in auto-completion: {str(e)}"] 