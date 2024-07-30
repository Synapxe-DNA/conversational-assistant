import time
from typing import Iterator

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from LLM.llama3 import LLM
from models.text_message import TextMessageRequest, TextMessageResponse

"""
Endpoint for text chat
"""

textChatRouter = APIRouter(prefix="/textchat")


def generator(iter: Iterator[str], delay: float = 0.01) -> Iterator[str]:
    for text in iter:
        if text != "<|eot_id|>":
            response_data = TextMessageResponse(
                message=text, status="pending", sources=[]
            )
            yield response_data.model_dump_json()
            time.sleep(delay)  # delay introduced as the response is too fast

    final_response = TextMessageResponse(message="", status="completed", sources=[])
    yield final_response.model_dump_json()


@textChatRouter.post("/message")
async def chat(message: TextMessageRequest):
    llm = LLM()
    response = StreamingResponse(
        generator(llm.ask(message.message)), media_type="application/json"
    )
    return response
