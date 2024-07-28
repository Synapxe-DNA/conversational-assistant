from dataclasses import dataclass

from fastapi import UploadFile
from pydantic import BaseModel


@dataclass
class VoiceMessage(BaseModel):
    message: UploadFile
