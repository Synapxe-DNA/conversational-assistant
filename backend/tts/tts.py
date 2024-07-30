# quickstart.py
import os

import azure.cognitiveservices.speech as speechsdk
from azure.identity import AzureCliCredential
from dotenv import load_dotenv

load_dotenv("./.env")

# Ensure you have logged using `az login` before running this code


class TextToSpeech:

    def __init__(self) -> None:
        self.azure_credential = AzureCliCredential()
        self.aadToken = self.azure_credential.get_token(
            "https://cognitiveservices.azure.com/.default"
        )
        self.resourceId = os.getenv("SPEECH_RESOURCE_ID")
        self.region = os.getenv("SPEECH_REGION")
        self.speechConfig = speechsdk.SpeechConfig(
            auth_token=self.getAuthToken(), region=self.region
        )
        self.speechConfig.speech_synthesis_voice_name = "en-US-AvaMultilingualNeural"
        self.audioConfig = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=self.speechConfig, audio_config=self.audioConfig
        )

    def getAuthToken(self):
        return "aad#" + self.resourceId + "#" + self.aadToken.token

    def readText(self, text):
        speech_synthesis_result = self.speech_synthesizer.speak_text_async(text).get()
        if (
            speech_synthesis_result.reason
            == speechsdk.ResultReason.SynthesizingAudioCompleted
        ):
            print("Speech synthesized for text [{}]".format(text))
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print(
                        "Error details: {}".format(cancellation_details.error_details)
                    )
                    print("Did you set the speech resource key and region values?")
    
    def getAudio(self,text):
        speech_synthesis_result = self.speech_synthesizer.speak_text_async(text).get()
        stream = speechsdk.AudioDataStream(speech_synthesis_result)
        print("running")
        return stream.read_data()



# # Get text from the console and synthesize to the default speaker.
# tts = TextToSpeech()
# print("Enter some text that you want to speak >")
# text = input()
# tts.readText(text)
