# NLP Toolbox

A powerful collection of Natural Language Processing tools for text processing and enhancement.

Working link: https://sujal2806-nlp-toolbox-streamlit-app-lhdeak.streamlit.app/

![NLP Toolbox](https://img.shields.io/badge/NLP-Toolbox-blue)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.24.0-red)
![Transformers](https://img.shields.io/badge/Transformers-4.30.0-orange)
![Docker](https://img.shields.io/badge/Docker-Available-blue)

## Features

- **Text Paraphraser**: Generate different versions of your text while maintaining the same meaning
- **Text Summarizer**: Create concise summaries of long texts
- **Grammar Checker**: Check and correct grammar and spelling errors in your text

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Docker (optional, for containerized deployment)

# Installation

## Local Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nlp-toolbox.git
   cd nlp-toolbox
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     .\.venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:
   ```bash
   streamlit run streamlit_app.py
   ```

## Docker Installation

1. Build the Docker image:
   ```bash
   docker build -t nlp-toolbox .
   ```

2. Run the container:
   ```bash
   docker run -p 8501:8501 nlp-toolbox
   ```

# Usage

## Web Interface

1. Open your browser and navigate to `http://localhost:8501`
2. Select a tool from the sidebar
3. Enter your text and adjust parameters as needed
4. Click the action button to process your text

# Development

## Project Structure

```
nlp-toolbox/
├── streamlit_app.py        # Web interface
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── .github/                # GitHub configuration
│   └── workflows/          # CI/CD workflows
└── utils/                  # Utility modules
    ├── paraphraser.py      # Text paraphrasing
    ├── summarizer.py       # Text summarization
    └── grammar_checker.py  # Grammar correction
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments

- [Streamlit](https://streamlit.io/) for the web interface
- [Hugging Face Transformers](https://huggingface.co/transformers/) for the NLP models
- [Docker](https://www.docker.com/) for containerization 
