import time

import azure.cognitiveservices.speech as speechsdk
from speech_config import get_speech_config


def speech_recognize_continuous_from_file(filename):
    """Performs continuous speech recognition with input from an audio file"""
    audio_config = speechsdk.audio.AudioConfig(filename=filename)
    speech_config = get_speech_config()
    auto_detect_source_language_config = (
        speechsdk.languageconfig.AutoDetectSourceLanguageConfig(
            languages=["en-SG", "zh-CN", "ta-IN", "ms-MY"]
        )
    )

    # Initialize the speech recognizer
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        auto_detect_source_language_config=auto_detect_source_language_config,
        audio_config=audio_config,
    )

    all_results = {"text": [], "language": []}
    done = False

    def handle_final_result(evt):
        detected_language = evt.result.properties[
            speechsdk.PropertyId.SpeechServiceConnection_AutoDetectSourceLanguageResult
        ]
        all_results["text"].append(evt.result.text)
        all_results["language"].append(detected_language)

    def stop_cb(evt):
        nonlocal done
        print("CLOSING on {}".format(evt))
        done = True

    # Connect callbacks to the events fired by the speech recognizer
    speech_recognizer.recognized.connect(handle_final_result)
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(0.5)

    return all_results
