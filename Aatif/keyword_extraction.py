import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords_from_file(input_file="cleaned_transcription.txt", output_file="keywords.txt"):
    with open(input_file, "r") as file:
        text = file.read()
    
    doc = nlp(text)
    
    keywords = set(token.text for token in doc if token.pos_ in ["ADJ", "NOUN", "PROPN"])
    
    with open(output_file, "w") as file:
        file.write(" ".join(sorted(keywords)))
    
    print("Extracted Unique Keywords:", sorted(keywords))
    print(f"Keywords saved to {output_file}")
    
    return sorted(keywords)

extract_keywords_from_file()
