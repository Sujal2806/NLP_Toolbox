from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqGeneration
import hashlib
import os
import json
import time
import torch

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
        
        # Initialize the model and tokenizer
        print("Loading paraphraser model...")
        model_name = "facebook/bart-large-cnn"  # Using BART model which is more stable
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqGeneration.from_pretrained(model_name)
        
        # Move model to CPU (device=-1)
        device = -1
        if device >= 0 and torch.cuda.is_available():
            model = model.to(f"cuda:{device}")
        
        # Tokenize input
        inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
        if device >= 0 and torch.cuda.is_available():
            inputs = {k: v.to(f"cuda:{device}") for k, v in inputs.items()}
        
        # Generate paraphrases
        print("Generating paraphrases...")
        start_time = time.time()
        
        outputs = model.generate(
            **inputs,
            max_length=60,
            min_length=10,
            num_beams=4,
            num_return_sequences=num_return_sequences,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            do_sample=True
        )
        
        # Decode outputs
        paraphrases = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
        
        end_time = time.time()
        print(f"Paraphrases generated in {end_time - start_time:.2f} seconds")
        
        # Cache the result
        paraphrase_cache[cache_key] = paraphrases
        save_cache()
        
        return paraphrases
    except Exception as e:
        return [f"Error in paraphrasing: {str(e)}"] 