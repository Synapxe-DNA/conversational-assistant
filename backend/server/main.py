import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return "Hello!"

if __name__ == "__main__":
    uvicorn.run('main:app',reload=True)
