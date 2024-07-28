from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.chatRouter import chatRouter
from routes.voiceRouter import voiceRouter


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
        app.include_router(chatRouter)
        app.include_router(voiceRouter)

        return app
