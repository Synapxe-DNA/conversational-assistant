import time
from typing import Generator

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from models.text_message import TextMessageRequest, TextMessageResponse

"""
Endpoint for text chat
"""

textChatRouter = APIRouter(prefix="/textchat")


def file_chunk_generator(
    message: TextMessageRequest, chunk_size: int = 64, delay: float = 0.1
) -> Generator[str, None, None]:
    """
    A function to simulate streaming text from an LLM.
    Generates `ChatResponse` formatted chunks.
    """
    file_path = "test/text-response.txt"

    try:
        with open(file_path, "rb") as file:
            chunk = ""
            while True:
                # Read a chunk of data
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                response_data = TextMessageResponse(
                    message=chunk, status="pending", sources=[]
                )
                yield response_data.model_dump_json()
                time.sleep(delay)

            final_response = TextMessageResponse(
                message="", status="completed", sources=[]
            )
            yield final_response.model_dump_json()

    except Exception as e:
        print(f"Error reading file: {e}")
        raise


@textChatRouter.post("/message")
async def chat(message: TextMessageRequest):
    response = StreamingResponse(
        file_chunk_generator(message), media_type="application/json"
    )
    return response
