from typing import Dict, List

from pydantic import BaseModel


class TextMessageRequest(BaseModel):
    message: str


class TextMessageResponse(BaseModel):
    message: str
    status: str
    sources: List[Dict[str, str]]
