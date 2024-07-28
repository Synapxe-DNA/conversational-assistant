from speech_to_text import speech_recognize_continuous_from_file

def test_speech_recognition():
    # Path to the WAV file you want to test
    filename = './sg_lhl_10s_chinese.wav'

    result = speech_recognize_continuous_from_file(filename)
    print(result)

if __name__ == "__main__":
    test_speech_recognition()
