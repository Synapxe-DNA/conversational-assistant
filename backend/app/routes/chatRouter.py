import time
import json
from typing import Generator

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from models.text_message import TextMessage
from models.chat_response import ChatResponse

"""
Endpoint for text chat
"""

chatRouter = APIRouter(prefix="/textchat")

def file_chunk_generator(
    message: TextMessage, chunk_size: int = 64, delay: float = 0.1
) -> Generator[str, None, None]:
    """
    A function to simulate streaming text from an LLM.
    Generates `ChatResponse` formatted chunks.
    """
    file_path = "test/rag-response.json"
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        
        full_message = data["message"]
        sources = data["sources"]
        accumulated_message = ""

        for i in range(0, len(full_message), chunk_size):
            chunk = full_message[i:i + chunk_size]
            accumulated_message += chunk

            response_data = {
                "message": accumulated_message,
                "status": "pending",
                "sources": sources if i == 0 else []  # Include sources only in the first chunk
            }
            response = ChatResponse(**response_data)
            yield response.json() + "\n"  # JSON lines format

            time.sleep(delay)
        
        # Send the final response with the full concatenated message
        final_response = {
            "message": accumulated_message,
            "status": "complete",
            "sources": sources
        }
        yield (ChatResponse(**final_response)).json() + "\n"

    except Exception as e:
        print(f"Error reading file: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@chatRouter.post("/message")
async def chat(message: TextMessage):
    response = StreamingResponse(
        file_chunk_generator(message), media_type="application/json"
    )
    return response