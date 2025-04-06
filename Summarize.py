from transformers import pipeline

# Initialize the Hugging Face summarizer pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    # Get the summary of the text
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']

def main():
    # Input text (could be a document or user input)
    input_text = input("Enter the text you want to summarize: ")
    
    # Summarize the text
    summary = summarize_text(input_text)
    
    # Output the summary
    print("\nSummary:")
    print(summary)

if __name__ == "__main__":
    main()

