# Deep Learning (CSL4020)  
## Course Project

# SonicSynapse: Voice-Controlled Music Recommendation

---

## 1. Overview

**SonicSynapse** is a deep learning-based system for **hands-free music discovery**. It combines advanced **speech-to-text** with **text embedding** and **song matching** to deliver personalized recommendations. By harnessing **OpenAI’s Whisper** for transcription, a **fine-tuned DistilBERT** for query understanding, and a **custom MLP** for matching song embeddings, SonicSynapse offers a seamless, voice-driven experience integrated with Spotify.

---

## 2. How It Works

1. **Voice Input**  
   The user records a voice command (e.g., “Play an energetic rock song”).
2. **Transcription (Whisper)**  
   The raw audio is transcribed into text via OpenAI’s **Whisper**.
3. **Query Embedding (DistilBERT)**  
   The text is converted into a semantic **query embedding** by a **fine-tuned DistilBERT** model.
4. **Song Embedding (MLP)**  
   Song metadata (e.g., genres, tags, acoustic features) is fed into a **custom MLP** that produces a **song embedding**.
5. **Matching (Cosine Similarity)**  
   The query embedding is compared to all song embeddings to find the top 5 matches.
6. **Playback**  
   Matched songs are played sequentially using **Spotify preview links**.

---

## 3. Key Features

- **Voice Interaction**  
  Natural, intuitive voice commands for hands-free operation.

- **Advanced Models**  
  - **Whisper** for high-quality transcription  
  - **DistilBERT** (fine-tuned) for robust query embedding  
  - **Custom MLP** to encode song metadata

- **Spotify Integration**  
  Direct playback via Spotify preview URLs.

- **Sequential Playback**  
  Users can control the order or skip through recommended tracks.

---

## 4. Dataset

This system leverages a combined dataset of **song metadata** and **Spotify links**, including columns such as:

| Column                | Description                                  |
|-----------------------|----------------------------------------------|
| `track_id`            | Unique song identifier                       |
| `name`                | Song title                                   |
| `artist`              | Artist name                                  |
| `spotify_preview_url` | Spotify preview link                         |
| `tags`                | Descriptive tags (e.g., "sad", "upbeat")     |
| `genre`               | Song genre                                   |
| `year`                | Release year                                 |
| `danceability`        | Danceability score (0–1)                     |
| `energy`              | Energy score (0–1)                           |
| `valence`             | Mood positivity (0–1)                        |

Additional numeric columns (tempo, loudness, etc.) may also be used for feature engineering in the MLP.

---

## 5. Repository Structure

SonicSynapse/
├── README.md  
├── requirements.txt  
├── data/  
│   ├── raw/                 # Original CSVs or unprocessed data  
│   ├── processed/           # Processed CSVs (tag-encoded, numeric)  
│   ├── triplets.pkl         # (query, pos, neg) used for training  
│   └── audio_samples/       # Optional audio files for demos  
├── scripts/  
│   ├── step1_convert_tags.py  
│   ├── step2_build_triplets.py  
│   ├── step3_train_song_tower.py  
│   └── step4_inference.py  
├── models/  
│   ├── query_encoder_finetuned.pth  
│   └── song_encoder.pth  
├── modules/  
│   ├── query_encoder.py     # DistilBERT-based code  
│   ├── song_encoder.py      # MLP-based code  
│   └── asr_whisper.py       # Whisper-based speech-to-text  
└── main.py                  # (Optional) central script to run the pipeline  

---

## 6. Installation

1. **Clone the Repository**  
   git clone https://github.com/your-username/SonicSynapse.git  
   cd SonicSynapse

2. **Set Up a Virtual Environment**  
   python3 -m venv .venv  
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. **Install Dependencies**  
   pip install -r requirements.txt

4. **Install Whisper**  
   pip install git+https://github.com/openai/whisper.git

---

## 7. Usage

### 7.1 Full Workflow Demo

python scripts/workflow_ui.py

### 7.2 Individual Components

- Record Audio: python scripts/record_audio.py  
- Transcribe Audio: python scripts/voice_to_text.py  
- Generate Recommendations: python scripts/step4_inference.py  
- Play Songs: python scripts/play_songs.py  

---

## 8. Model Training

### Query Encoder  
- **DistilBERT** is fine-tuned on `(query, song)` pairs with a contrastive loss.

### Song Encoder  
- **MLP** with two dense layers, outputting 128D embeddings for metadata.

### Contrastive Loss  
- Maximizes similarity between matching (query, song) pairs.

---

## 9. Future Enhancements

- **Emotion Detection**  
- **Real-time Streaming**  
- **User Profiles**

---

## 10. Contributors

- **Anushk007** – System architecture & implementation  
- **Aatif** – Model training & evaluation  
- **Yashraj** - Workflow Integration & Data Processing

---

## 11. License

Licensed under the **MIT License**.

---

## 12. Acknowledgments

- **OpenAI** – Whisper  
- **Hugging Face** – DistilBERT  
- **Spotify** – Metadata & previews