import os
from azure.identity import AzureCliCredential
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk


load_dotenv("./.env")

def get_speech_config():
    resourceId = os.getenv("SPEECH_RESOURCE_ID")
    region = os.getenv("SPEECH_REGION")

    if not resourceId or not region:
        raise ValueError("Azure resource ID or region is not set in environment variables.")

    azure_credential = AzureCliCredential()
    aadToken = azure_credential.get_token("https://cognitiveservices.azure.com/.default")

    # Include the "aad#" prefix and the "#" separator between resource ID and AAD access token
    authorizationToken = "aad#" + resourceId + "#" + aadToken.token
    speech_config = speechsdk.SpeechConfig(auth_token=authorizationToken, region=region)
    
    return speech_config
