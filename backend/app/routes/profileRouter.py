from fastapi import APIRouter
from models.profile import Profile

profileRouter = APIRouter(prefix="/profile")

@profileRouter.post("/set")
async def chat( profile: Profile):
    return f'Hi {profile.name} [Age: {profile.age}]!'