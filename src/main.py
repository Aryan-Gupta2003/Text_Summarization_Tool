from summarizer import Summarizer

def main():
    # Load sample text
    with open('data/sample_text.txt', 'r') as file:
        text = file.read()

    summarizer = Summarizer()
    summary = summarizer.summarize(text, num_sentences=3)
    
    print("Original Text:\n", text)
    print("\nSummary:\n", summary)

if __name__ == "__main__":
    main()
