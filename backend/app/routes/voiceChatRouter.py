from fastapi import FastAPI, APIRouter
from fastapi.responses import StreamingResponse
from pydub import AudioSegment
import base64
import json
import io

voiceChatRouter = APIRouter(prefix="/voicechat")

def process_audio(file: io.BytesIO, message: str) -> StreamingResponse:
    try:
        audio = AudioSegment.from_file(file, format="wav")
    except Exception as e:
        print(f"Error reading audio file: {e}")
        raise

    sample_rate = audio.frame_rate
    num_channels = audio.channels
    bits_per_sample = audio.sample_width * 8

    print(f"Audio properties - Sample Rate: {sample_rate}, Channels: {num_channels}, Bits per Sample: {bits_per_sample}")

    chunk_length_ms = 1000
    chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
    print(f"Number of chunks: {len(chunks)}")

    def generate():
        yield f'{{"message":"{message}",'
        yield f'"sample_rate":{sample_rate}, "num_channels":{num_channels}, "bits_per_sample":{bits_per_sample}, "voice":['
        
        first_chunk = True
        for idx, chunk in enumerate(chunks):
            if not first_chunk:
                yield ', '
            first_chunk = False

            chunk_bytes = chunk.raw_data
            chunk_base64 = base64.b64encode(chunk_bytes).decode('utf-8')
            chunk_json = json.dumps([idx, chunk_base64])
            yield chunk_json

        yield ']}'


    return StreamingResponse(generate(), media_type="application/json")

@voiceChatRouter.post("/message")
async def process_wav():
    # Read mock message from file
    with open("./backend/test/text-response.txt", "r") as file:
        raw_message = file.read().strip()
        mock_message = json.dumps(raw_message)[1:-1] 

    # Read mock audio file
    with open("./backend/test/testaudio.wav", "rb") as f:
        mock_audio_file = io.BytesIO(f.read())

    print(f"Mock message: {mock_message}")
    print(f"Size of audio file: {len(mock_audio_file.getvalue())} bytes")

    return process_audio(mock_audio_file, mock_message)
