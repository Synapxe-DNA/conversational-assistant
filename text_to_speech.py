# quickstart.py
import os
from azure.identity import (DefaultAzureCredential,get_bearer_token_provider, InteractiveBrowserCredential)
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

load_dotenv()

# No API Keys used
# azure_credential = DefaultAzureCredential()
# aadToken = azure_credential.get_token("https://cognitiveservices.azure.com/.default")

ibc = InteractiveBrowserCredential()
aadToken = ibc.get_token("https://cognitiveservices.azure.com/.default")

resourceId = os.getenv("SPEECH_RESOURCE_ID")
region = os.getenv("SPEECH_REGION")
# You need to include the "aad#" prefix and the "#" (hash) separator between resource ID and AAD access token.
authorizationToken = "aad#" + resourceId + "#" + aadToken.token

speechConfig = speechsdk.SpeechConfig(auth_token=authorizationToken, region=region)
audioConfig = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

speechConfig.speech_synthesis_voice_name='en-US-AvaMultilingualNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speechConfig, audio_config=audioConfig)

# Get text from the console and synthesize to the default speaker.
print("Enter some text that you want to speak >")
text = input()

speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(text))
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")