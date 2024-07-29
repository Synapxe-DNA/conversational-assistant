from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.profileRouter import profileRouter
from routes.textChatRouter import textChatRouter
from routes.ttsRouter import ttsRouter
from routes.voiceChatRouter import voiceChatRouter


class AppBuilder:

    @classmethod
    def get_instance(cls) -> FastAPI:
        """
        Produces the FastAPI instance and registers sub-routers
        and necessary middleware to the application.

        :return: FastAPI
        """

        app = FastAPI()

        # Middleware
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # Register routers here
        app.include_router(textChatRouter)
        app.include_router(voiceChatRouter)
        app.include_router(profileRouter)
        app.include_router(ttsRouter)

        return app
