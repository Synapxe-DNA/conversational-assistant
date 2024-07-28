from typing import Optional

from models.profile import Profile
from pydantic import BaseModel


class VoiceMessage(BaseModel):
    message: bytearray
    profile: Optional[Profile]
