from speech_to_text import speech_recognize_continuous_from_file

def test_speech_recognition():
    # Path to the WAV file you want to test
    filename = "./speech-to-text/samples/sg_lhl_12s_malay.wav"

    result = speech_recognize_continuous_from_file(filename)
    # end_time = time.time()
    print(result)


if __name__ == "__main__":
    test_speech_recognition()
