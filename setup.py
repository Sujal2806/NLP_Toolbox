import nltk
import os

def setup():
    # Create cache directory if it doesn't exist
    if not os.path.exists('cache'):
        os.makedirs('cache')
    
    # Download required NLTK data
    print("Downloading required NLTK data...")
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    nltk.download('stopwords')
    nltk.download('omw-1.4')
    
    print("Setup completed successfully!")

if __name__ == "__main__":
    setup() 