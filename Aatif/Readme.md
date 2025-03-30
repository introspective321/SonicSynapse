## Installation

Before running the project, ensure you have installed all the required dependencies and downloaded the necessary models.

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

---

## Steps to Run

Follow these steps to use the project:

### 1. Record Your Audio
Run the following script to record your voice:

```bash
python record_audio.py
```

- Speak into the microphone for **5 seconds**.
- The recording will be saved as `output.wav`.

---

### 2. Transcribe Into Text
Convert your recorded audio into text using the following command:

```bash
python voice_to_text.py
```

- The transcription will be saved in a file named `transcription.txt`.

---

### 3. Preprocess the Text
Clean the transcribed text by running the preprocessing script:

```bash
python preprocessing.py
```

- The cleaned text will be saved in a file named `cleaned_transcriptions.txt`.

---

### 4. Extract Keywords
Extract important keywords from the cleaned text using the following command:

```bash
python keyword_extraction.py
```

- The extracted keywords will be saved in a file named `keywords.txt`.

---