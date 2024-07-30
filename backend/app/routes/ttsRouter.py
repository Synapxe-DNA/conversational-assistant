import time
from typing import Generator

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from models.tts_message import TTSMessage

"""
Endpoint for text to speech
"""

ttsRouter = APIRouter(prefix="/tts")


async def audio_chunk_generator(
    chunk_size: int = 1024, delay: float = 0.0001
) -> Generator[bytes, None, None]:
    """
    Generator that yields audio file chunks directly from the uploaded file.
    """
    file_path = "test/testaudio.wav"

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


@ttsRouter.post("/message")
async def chat(message: TTSMessage):
    return StreamingResponse(audio_chunk_generator(), media_type="audio/wav")
