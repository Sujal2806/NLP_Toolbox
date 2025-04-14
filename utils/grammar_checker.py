from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the pretrained model and tokenizer
model_name = "vennify/t5-base-grammar-correction"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def correct_grammar(text):
    """
    Correct grammar and spelling errors in the input text.

    Args:
        text (str): The text to be corrected.

    Returns:
        str: The corrected version of the input text.
    """
    input_text = "gec: " + text
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=128, num_beams=5, early_stopping=True)
    corrected_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return corrected_text


if __name__ == "__main__":
    print("Enter text to correct grammar and spelling (type 'exit' to quit):")
    while True:
        user_input = input("\nText: ")
        if user_input.lower() == "exit":
            break
        result = correct_grammar(user_input)
        print("\nCorrected:", result)
