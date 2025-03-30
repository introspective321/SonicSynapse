import re
import spacy

def clean_text(text):
    nlp = spacy.load("en_core_web_sm")
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    doc = nlp(text)
    cleaned_text = " ".join([token.lemma_ for token in doc if not token.is_stop])
    return cleaned_text

def process_transcription(input_file="transcription.txt", output_file="cleaned_transcription.txt"):
    with open(input_file, "r") as file:
        text = file.read()
    
    cleaned_text = clean_text(text)
    
    with open(output_file, "w") as file:
        file.write(cleaned_text)
    
    print(f"Cleaned transcription saved to {output_file}")
    return cleaned_text

if __name__ == "__main__":
    process_transcription()
