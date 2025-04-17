from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

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