from transformers import pipeline
import hashlib
import os
import json
import time

# Create a cache directory if it doesn't exist
CACHE_DIR = "cache"
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

# Cache file for paraphrases
PARAPHRASE_CACHE_FILE = os.path.join(CACHE_DIR, "paraphrase_cache.json")

# Load the cache if it exists
paraphrase_cache = {}
if os.path.exists(PARAPHRASE_CACHE_FILE):
    try:
        with open(PARAPHRASE_CACHE_FILE, 'r', encoding='utf-8') as f:
            paraphrase_cache = json.load(f)
    except:
        paraphrase_cache = {}

def get_cache_key(text, num_return_sequences):
    """Generate a cache key for the input parameters."""
    key_string = f"{text}_{num_return_sequences}"
    return hashlib.md5(key_string.encode()).hexdigest()

def save_cache():
    """Save the cache to disk."""
    with open(PARAPHRASE_CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(paraphrase_cache, f)

def paraphrase_text(text, num_return_sequences=3):
    """
    Paraphrase the input text using transformers.
    
    Args:
        text (str): Input text to paraphrase
        num_return_sequences (int): Number of different paraphrases to generate
        
    Returns:
        list: List of paraphrased versions of the text
    """
    try:
        # Check if the text is too short to paraphrase
        if len(text.split()) < 10:
            return ["Text is too short to paraphrase effectively. Please provide a longer text."]
        
        # Generate cache key
        cache_key = get_cache_key(text, num_return_sequences)
        
        # Check if result is in cache
        if cache_key in paraphrase_cache:
            print("Using cached paraphrases")
            return paraphrase_cache[cache_key]
        
        # Initialize the text generation pipeline with a smaller model
        print("Loading paraphraser model...")
        paraphraser = pipeline(
            "text2text-generation",
            model="tuner007/pegasus_paraphrase",
            device=-1,
            max_length=60,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            num_return_sequences=num_return_sequences
        )
        
        # Generate paraphrases
        print("Generating paraphrases...")
        start_time = time.time()
        paraphrases = paraphraser(text)
        end_time = time.time()
        print(f"Paraphrases generated in {end_time - start_time:.2f} seconds")
        
        # Extract the generated text
        results = [p['generated_text'] for p in paraphrases]
        
        # Cache the result
        paraphrase_cache[cache_key] = results
        save_cache()
        
        return results
    except Exception as e:
        return [f"Error in paraphrasing: {str(e)}"] 