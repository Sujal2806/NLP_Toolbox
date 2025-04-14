from textblob import TextBlob
import re

def check_grammar_and_spell(text):
    """
    Check grammar and spelling in the input text.
    
    Args:
        text (str): Input text to check
        
    Returns:
        dict: Dictionary containing corrections and suggestions
    """
    try:
        # Create TextBlob object
        blob = TextBlob(text)
        
        # Initialize results
        corrections = []
        spell_errors = []
        
        # Check spelling
        for word in blob.words:
            if word.spellcheck()[0][0] != word:
                spell_errors.append({
                    'word': word,
                    'suggestions': [s[0] for s in word.spellcheck()[:3]]
                })
        
        # Get corrected text
        corrected_text = str(blob.correct())
        
        # Compare original and corrected text to find grammar corrections
        if corrected_text != text:
            corrections.append({
                'original': text,
                'corrected': corrected_text
            })
        
        return {
            'spell_errors': spell_errors,
            'grammar_corrections': corrections,
            'corrected_text': corrected_text
        }
    except Exception as e:
        return {'error': str(e)} 