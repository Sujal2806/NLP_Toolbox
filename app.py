from utils.paraphraser import paraphrase
from utils.summarizer import summarize_text
from utils.grammar_checker import correct_grammar

def print_menu():
    print("\n=== NLP Toolbox ===")
    print("1. Paraphraser")
    print("2. Summarizer")
    print("3. Grammar Checker")
    print("4. Exit")
    print("================")

def main():
    while True:
        print_menu()
        choice = input("\nSelect a tool (1-4): ").strip()
        
        if choice == "1":
            text = input("\nEnter text to paraphrase: ")
            if text.lower() == 'exit':
                continue
            num_sequences = int(input("Number of paraphrased versions (1-10) [default: 5]: ") or "5")
            print("\nGenerating paraphrases...")
            paraphrases = paraphrase(text, num_return_sequences=num_sequences)
            print("\nParaphrased versions:")
            for i, para in enumerate(paraphrases, 1):
                print(f"{i}. {para}")
                
        elif choice == "2":
            text = input("\nEnter text to summarize: ")
            if text.lower() == 'exit':
                continue
            max_length = int(input("Maximum summary length (50-200) [default: 130]: ") or "130")
            min_length = int(input("Minimum summary length (10-100) [default: 30]: ") or "30")
            print("\nGenerating summary...")
            summary = summarize_text(text, max_length=max_length, min_length=min_length)
            print("\nSummary:")
            print(summary)
            
        elif choice == "3":
            text = input("\nEnter text to check grammar: ")
            if text.lower() == 'exit':
                continue
            print("\nChecking grammar...")
            corrected = correct_grammar(text)
            print("\nCorrected text:")
            print(corrected)
            
        elif choice == "4":
            print("\nThank you for using NLP Toolbox!")
            break
            
        else:
            print("\nInvalid choice. Please select a number between 1 and 4.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
