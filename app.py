from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging
import time
from utils.summarizer import summarize_text
from utils.paraphraser import paraphrase_text
from utils.grammar_checker import check_grammar_and_spell

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Configure rate limiter
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

def validate_text_input(text):
    """Validate text input for all endpoints."""
    if not text or not isinstance(text, str):
        return False, "Text input is required and must be a string"
    if len(text.strip()) < 10:
        return False, "Text must be at least 10 characters long"
    return True, None

@app.route('/api/health', methods=['GET'])
@limiter.exempt
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "timestamp": time.time()
    })

@app.route('/api/summarize', methods=['POST'])
@limiter.limit("30 per minute")
def summarize():
    """Summarize text endpoint."""
    try:
        data = request.get_json()
        text = data.get('text', '')
        max_length = data.get('max_length', 150)
        
        # Validate input
        is_valid, error_message = validate_text_input(text)
        if not is_valid:
            return jsonify({"error": error_message}), 400
        
        # Process request
        start_time = time.time()
        summary = summarize_text(text, max_length=max_length)
        end_time = time.time()
        
        # Log success
        logger.info(f"Summarization completed in {end_time - start_time:.2f} seconds")
        
        return jsonify({
            "summary": summary,
            "original_length": len(text.split()),
            "summary_length": len(summary.split()),
            "time_taken": end_time - start_time
        })
    except Exception as e:
        logger.error(f"Error in summarization: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/paraphrase', methods=['POST'])
@limiter.limit("20 per minute")
def paraphrase():
    """Paraphrase text endpoint."""
    try:
        data = request.get_json()
        text = data.get('text', '')
        num_variations = data.get('num_variations', 3)
        
        # Validate input
        is_valid, error_message = validate_text_input(text)
        if not is_valid:
            return jsonify({"error": error_message}), 400
        
        # Process request
        start_time = time.time()
        variations = paraphrase_text(text, num_return_sequences=num_variations)
        end_time = time.time()
        
        # Log success
        logger.info(f"Paraphrasing completed in {end_time - start_time:.2f} seconds")
        
        return jsonify({
            "variations": variations,
            "original_length": len(text.split()),
            "time_taken": end_time - start_time
        })
    except Exception as e:
        logger.error(f"Error in paraphrasing: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/grammar-check', methods=['POST'])
@limiter.limit("40 per minute")
def grammar_check():
    """Grammar check endpoint."""
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        # Validate input
        is_valid, error_message = validate_text_input(text)
        if not is_valid:
            return jsonify({"error": error_message}), 400
        
        # Process request
        start_time = time.time()
        result = check_grammar_and_spell(text)
        end_time = time.time()
        
        # Log success
        logger.info(f"Grammar check completed in {end_time - start_time:.2f} seconds")
        
        return jsonify({
            "result": result,
            "text_length": len(text.split()),
            "time_taken": end_time - start_time
        })
    except Exception as e:
        logger.error(f"Error in grammar check: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.errorhandler(429)
def ratelimit_handler(e):
    """Handle rate limit errors."""
    return jsonify({"error": "Rate limit exceeded. Please try again later."}), 429

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 