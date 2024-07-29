from pydantic import BaseModel
from typing import List, Dict

class ChatResponse(BaseModel):
    message: str
    status: str
    sources: List[Dict[str, str]]
