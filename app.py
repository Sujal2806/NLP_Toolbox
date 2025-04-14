from flask import Flask, request, jsonify
from flask_cors import CORS
import time
from utils.summarizer import summarize_text
from utils.grammar_checker import check_grammar_and_spell
from utils.auto_complete import auto_complete_text
from utils.plagiarism_checker import check_plagiarism
from utils.paraphraser import paraphrase_text

app = Flask(__name__)
CORS(app)

@app.route('/api/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        text = data.get('text', '')
        max_length = data.get('max_length', 150)
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
            
        start_time = time.time()
        summary = summarize_text(text, max_length)
        end_time = time.time()
        
        return jsonify({
            'summary': summary,
            'time_taken': f"{end_time - start_time:.2f} seconds"
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/grammar-check', methods=['POST'])
def grammar_check():
    data = request.get_json()
    text = data.get('text', '')
    
    result = check_grammar_and_spell(text)
    return jsonify(result)

@app.route('/api/auto-complete', methods=['POST'])
def auto_complete():
    data = request.get_json()
    text = data.get('text', '')
    max_length = data.get('max_length', 50)
    num_sequences = data.get('num_sequences', 3)
    
    result = auto_complete_text(text, max_length, num_sequences)
    return jsonify({'completions': result})

@app.route('/api/check-plagiarism', methods=['POST'])
def check_plagiarism_route():
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
            
        start_time = time.time()
        result = check_plagiarism(text)
        end_time = time.time()
        
        return jsonify({
            'result': result,
            'time_taken': f"{end_time - start_time:.2f} seconds"
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/paraphrase', methods=['POST'])
def paraphrase():
    try:
        data = request.get_json()
        text = data.get('text', '')
        num_variations = data.get('num_variations', 3)
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
            
        start_time = time.time()
        variations = paraphrase_text(text, num_variations)
        end_time = time.time()
        
        return jsonify({
            'variations': variations,
            'time_taken': f"{end_time - start_time:.2f} seconds"
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 