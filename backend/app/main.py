import uvicorn
from utils.app_builder.app_builder import AppBuilder

app = AppBuilder.get_instance()


@app.get("/")
async def hello():
    return "Hello!"


def dev():
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
        workers=1,
        timeout_keep_alive=0,
    )


if __name__ == "__main__":
    dev()
