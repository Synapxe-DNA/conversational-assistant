from typing import Optional

from models.profile import Profile
from pydantic import BaseModel


class TextMessage(BaseModel):
    message: str
    profile: Optional[Profile]
