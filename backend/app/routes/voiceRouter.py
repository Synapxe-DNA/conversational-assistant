from fastapi import APIRouter, UploadFile

voiceRouter = APIRouter(prefix="/voicechat")


@voiceRouter.post("/message")
async def chat(voice: UploadFile):
    return f"Uploaded {voice.filename}"
