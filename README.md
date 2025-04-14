# NLP Toolbox

A powerful Natural Language Processing toolbox that provides text processing features through both a web interface and API endpoints.

Working link: https://sujal2806-nlp-toolbox-streamlit-app-lhdeak.streamlit.app/
## Features

- **Text Summarization**: Condense long texts into concise summaries
- **Text Paraphrasing**: Generate alternative versions of text while preserving meaning
- **Grammar Checking**: Identify and correct grammar and spelling issues

## Installation

### Option 1: Local Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/nlp-toolbox.git
cd nlp-toolbox
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Run the setup script to download necessary data:
```bash
python setup.py
```

### Option 2: Docker Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/nlp-toolbox.git
cd nlp-toolbox
```

2. Build the Docker image:
```bash
docker build -t nlp-toolbox .
```

3. Run the Docker container:
```bash
docker run -p 8501:8501 -p 5000:5000 nlp-toolbox
```

## Usage

### Web Interface (Streamlit)

1. Start the Streamlit application:
```bash
streamlit run streamlit_app.py
```

2. Open your web browser and navigate to http://localhost:8501

3. Use the three tabs to access different features:
   - **Summarization**: Enter text to generate a concise summary
   - **Paraphrasing**: Enter text to get alternative versions
   - **Grammar Check**: Enter text to check for grammar and spelling issues

### API Endpoints (Flask)

The API is available at http://localhost:5000 with the following endpoints:

1. **Text Summarization**
```bash
POST /api/summarize
Content-Type: application/json

{
    "text": "Your text here",
    "max_length": 150
}
```

2. **Grammar Check**
```bash
POST /api/grammar-check
Content-Type: application/json

{
    "text": "Your text here"
}
```

3. **Text Paraphrasing**
```bash
POST /api/paraphrase
Content-Type: application/json

{
    "text": "Your text here",
    "num_variations": 3
}
```

4. **Health Check**
```bash
GET /api/health
```

## Technical Details

### Models and Libraries
- **Grammar Check**: TextBlob + spaCy for comprehensive grammar analysis
- **Summarization**: BART model for text summarization
- **Paraphrasing**: Pegasus model for text paraphrasing

### Performance Features
- GPU support when available
- Caching system for improved performance
- Rate limiting for API endpoints
- Progress tracking for long operations
- Comprehensive error handling

### System Requirements
- Python 3.8+
- 4GB RAM minimum (8GB recommended)
- GPU optional but recommended for better performance

## API Rate Limits
- Summarization: 30 requests per minute
- Grammar Check: 30 requests per minute
- Paraphrasing: 30 requests per minute
- Plagiarism Check: 20 requests per minute
- Global limit: 200 requests per day

## Error Handling
The API returns appropriate HTTP status codes:
- 200: Success
- 400: Bad Request (invalid input)
- 429: Too Many Requests (rate limit exceeded)
- 500: Internal Server Error

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.