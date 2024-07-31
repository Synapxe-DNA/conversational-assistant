import threading

import azure.cognitiveservices.speech as speechsdk
from speech_config import get_speech_config


def setup_speech_recognizer():
    """Sets up the speech recognizer with the PushAudioInputStream."""
    speech_config = get_speech_config()
    speech_config.set_property(
        property_id=speechsdk.PropertyId.SpeechServiceConnection_LanguageIdMode,
        value="Continuous",
    )

    # Setup the audio stream
    stream = speechsdk.audio.PushAudioInputStream()
    audio_config = speechsdk.audio.AudioConfig(stream=stream)

    auto_detect_source_language_config = (
        speechsdk.languageconfig.AutoDetectSourceLanguageConfig(
            languages=["en-SG", "zh-CN", "ta-IN", "ms-MY"]
        )
    )
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config,
        auto_detect_source_language_config=auto_detect_source_language_config,
    )

    recognition_done = threading.Event()
    all_results = {"text": [], "language": []}

    # Connect callbacks to the events fired by the speech recognizer
    def handle_final_result(evt):
        if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
            detected_language = evt.result.properties[
                speechsdk.PropertyId.SpeechServiceConnection_AutoDetectSourceLanguageResult
            ]
            all_results["text"].append(evt.result.text)
            all_results["language"].append(detected_language)
        elif evt.result.reason == speechsdk.ResultReason.NoMatch:
            print(
                "No speech could be recognized: {}".format(evt.result.no_match_details)
            )
        # detected_language = evt.result.properties[speechsdk.PropertyId.SpeechServiceConnection_AutoDetectSourceLanguageResult]
        # all_results['text'].append(evt.result.text)
        # all_results['language'].append(detected_language)

    def session_stopped_cb(evt):
        """Callback that signals to stop continuous recognition upon receiving an event `evt`"""
        print("SESSION STOPPED: {}".format(evt))
        recognition_done.set()

    # speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
    speech_recognizer.recognized.connect(handle_final_result)
    speech_recognizer.session_started.connect(
        lambda evt: print("SESSION STARTED: {}".format(evt))
    )
    speech_recognizer.session_stopped.connect(session_stopped_cb)
    speech_recognizer.canceled.connect(lambda evt: print("CANCELED {}".format(evt)))

    return stream, speech_recognizer, recognition_done, all_results
