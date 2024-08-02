import threading
import os
import azure.cognitiveservices.speech as speechsdk
from azure.identity import AzureCliCredential
from dotenv import load_dotenv

load_dotenv("./.env")


class SpeechRecognition:
    def __init__(self, filename):
        self.filename = filename
        self.speech_recognizer, self.all_results, self.recognition_done = self.setup_speech_recognizer()

    @staticmethod
    def get_speech_config():
        resourceId = os.getenv("SPEECH_RESOURCE_ID")
        region = os.getenv("SPEECH_REGION")

        if not resourceId or not region:
            raise ValueError("Azure resource ID or region is not set in environment variables.")

        azure_credential = AzureCliCredential()
        aadToken = azure_credential.get_token("https://cognitiveservices.azure.com/.default")

        authorizationToken = "aad#" + resourceId + "#" + aadToken.token
        speech_config = speechsdk.SpeechConfig(auth_token=authorizationToken, region=region)

        return speech_config

    def setup_speech_recognizer(self):
        speech_config = self.get_speech_config()
        speech_config.set_property(
            property_id=speechsdk.PropertyId.SpeechServiceConnection_LanguageIdMode,
            value="Continuous",
        )

        audio_config = speechsdk.audio.AudioConfig(filename=self.filename)

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

        all_results = {"text": [], "language": []}
        recognition_done = threading.Event()

        speech_recognizer.recognized.connect(self.handle_final_result(all_results))
        speech_recognizer.session_started.connect(lambda evt: print("SESSION STARTED: {}".format(evt)))
        speech_recognizer.session_stopped.connect(lambda evt: recognition_done.set())
        speech_recognizer.canceled.connect(lambda evt: recognition_done.set())

        return speech_recognizer, all_results, recognition_done

    @staticmethod
    def handle_final_result(all_results):
        def inner(evt):
            if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
                detected_language = evt.result.properties[
                    speechsdk.PropertyId.SpeechServiceConnection_AutoDetectSourceLanguageResult
                ]
                all_results["text"].append(evt.result.text)
                all_results["language"].append(detected_language)
            elif evt.result.reason == speechsdk.ResultReason.NoMatch:
                print("No speech could be recognized: {}".format(evt.result.no_match_details))
        return inner

    def run(self):
        self.speech_recognizer.start_continuous_recognition()
        self.recognition_done.wait()  
        self.speech_recognizer.stop_continuous_recognition()
        return self.all_results


if __name__ == "__main__":
    filename = "./speech-to-text/samples/sg_lhl_10s_chinese.wav"
    speech_recognition = SpeechRecognition(filename)
    results = speech_recognition.run()
    print(results)
