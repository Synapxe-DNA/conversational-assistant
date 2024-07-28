import time
from typing import Generator

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from models.text_message import TextMessage

chatRouter = APIRouter(prefix="/textchat")


def file_chunk_generator(
    message: TextMessage, chunk_size: int = 64, delay: float = 0.1
) -> Generator[bytes, None, None]:
    """
    A function to simulate streaming text from an LLM
    """
    file_path = "test/text-response.txt"
    try:
        with open(file_path, "rb") as file:
            while True:
                # Read a chunk of data
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                yield chunk
                time.sleep(delay)
    except Exception as e:
        print(f"Error reading file: {e}")
        raise


@chatRouter.post("/message")
async def chat(message: TextMessage):
    response = StreamingResponse(
        file_chunk_generator(message), media_type="text/event-stream"
    )
    return response
