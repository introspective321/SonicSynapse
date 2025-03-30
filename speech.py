import whisper


model = whisper.load_model("base")
audio = "audio.mp3"
result = model.transcribe(audio)


print(result["text"])
