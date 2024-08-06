import io
import os
import threading

import azure.cognitiveservices.speech as speechsdk
from azure.identity import AzureCliCredential
from dotenv import load_dotenv

load_dotenv("./.env")


class SpeechRecognition:
    def __init__(self):
        """
        # Azure Config
        # self.resource_id = current_app.config.get(CONFIG_SPEECH_SERVICE_ID)
        # self.region = current_app.config[CONFIG_SPEECH_SERVICE_LOCATION]
        # self.speech_token = speech_token
        # self.auth_token = self.getAuthToken()
        """

        ###
        self.resource_id = os.getenv("SPEECH_RESOURCE_ID")
        self.region = os.getenv("SPEECH_REGION")
        azure_credential = AzureCliCredential()
        aadToken = azure_credential.get_token(
            "https://cognitiveservices.azure.com/.default"
        )
        self.auth_token = "aad#" + self.resource_id + "#" + aadToken.token
        ####

        self.speech_config = speechsdk.SpeechConfig(
            auth_token=self.auth_token, region=self.region
        )
        self.audio_blob = None
        self.recognition_done = threading.Event()

    def setup_speech_recognizer(self):
        speech_config = self.speech_config
        speech_config.set_property(
            property_id=speechsdk.PropertyId.SpeechServiceConnection_LanguageIdMode,
            value="Continuous",
        )

        audio_stream = speechsdk.audio.PushAudioInputStream()
        # audio_format = speechsdk.audio.AudioStreamFormat(samples_per_second=16000, bits_per_sample=16, channels=1)
        audio_config = speechsdk.audio.AudioConfig(stream=audio_stream)

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

        speech_recognizer.recognized.connect(self.handle_final_result(all_results))
        speech_recognizer.session_started.connect(
            lambda evt: print("SESSION STARTED: {}".format(evt))
        )
        speech_recognizer.session_stopped.connect(
            lambda evt: self.recognition_done.set()
        )
        speech_recognizer.canceled.connect(lambda evt: self.recognition_done.set())

        self.push_audio(audio_stream)

        return speech_recognizer, all_results

    def push_audio(self, audio_stream):
        with io.BytesIO(self.audio_blob) as audio_file:
            chunk_size = 1024
            while True:
                chunk = audio_file.read(chunk_size)
                if not chunk:
                    break
                audio_stream.write(chunk)
            audio_stream.close()

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
                print(
                    "No speech could be recognized: {}".format(
                        evt.result.no_match_details
                    )
                )

        return inner

    def transcribe(self, audio_blob):
        self.audio_blob = audio_blob
        self.speech_recognizer, all_results = self.setup_speech_recognizer()
        self.speech_recognizer.start_continuous_recognition()
        self.recognition_done.wait()
        self.speech_recognizer.stop_continuous_recognition()
        return all_results
