from transformers import PegasusForConditionalGeneration, PegasusTokenizer

# Load model and tokenizer
model_name = 'tuner007/pegasus_paraphrase'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name)

def paraphrase(text, num_return_sequences=5, num_beams=10):
    """
    Generate paraphrased versions of the input text.

    Args:
        text (str): The input text to be paraphrased.
        num_return_sequences (int): Number of paraphrased outputs to return.
        num_beams (int): Beam search width.

    Returns:
        list of str: List of paraphrased sentences.
    """
    batch = tokenizer.prepare_seq2seq_batch([text], truncation=True, padding='longest', return_tensors="pt")
    translated = model.generate(**batch,
                             max_length=60,
                             num_beams=num_beams,
                             num_return_sequences=num_return_sequences,
                             temperature=1.5)
    paraphrases = tokenizer.batch_decode(translated, skip_special_tokens=True)
    return paraphrases


if __name__ == "__main__":
    print("Enter a sentence to paraphrase (type 'exit' to quit):")
    while True:
        user_input = input("\nText: ")
        if user_input.lower() == "exit":
            break
        results = paraphrase(user_input)
        print("\nParaphrased Sentences:")
        for i, sentence in enumerate(results, 1):
            print(f"{i}. {sentence}")