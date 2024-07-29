from pydantic import BaseModel


class TTSMessage(BaseModel):
    message: str
