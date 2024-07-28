from pydantic import BaseModel


class TextMessage(BaseModel):
    message: str
