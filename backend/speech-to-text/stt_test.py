from speech_to_text import SpeechRecognition

with open("./speech-to-text/samples/sg_lhl_10s_chinese.wav", "rb") as f:
    audio_blob = f.read()
SR = SpeechRecognition()
results = SR.transcribe(audio_blob)
print(results)