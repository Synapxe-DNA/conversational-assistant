from dataclasses import dataclass

from fastapi import UploadFile
from pydantic import BaseModel


@dataclass
class VoiceMessageRequest(BaseModel):
    message: UploadFile


class VoiceMessageResponse(BaseModel):
    message: str
    sources: str
    status: str
    audio: bytearray
