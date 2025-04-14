# Use Python 3.8 base image
FROM python:3.8

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install Rust using rustup
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Upgrade pip and install wheel
RUN pip install --no-cache-dir --upgrade pip wheel setuptools

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies in stages with specific versions
RUN pip install --no-cache-dir numpy==1.24.3 pandas==2.0.3 scikit-learn==1.3.0 nltk==3.8.1 spacy==3.6.1 streamlit==1.25.0 \
    && pip install --no-cache-dir torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 \
    && pip install --no-cache-dir transformers==4.30.2 tokenizers==0.13.3 \
    && pip install --no-cache-dir sentence-transformers==2.2.2 \
    && pip install --no-cache-dir scipy==1.10.1 matplotlib==3.7.2 seaborn==0.12.2 \
    && pip install --no-cache-dir -r requirements.txt --no-deps

# Copy the rest of the application
COPY . .

# Run setup script to download NLTK data
RUN python setup.py

# Expose the port Streamlit runs on
EXPOSE 8501

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Command to run the application
CMD ["streamlit", "run", "streamlit_app.py"] 