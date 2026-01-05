import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    # App
    APP_NAME: str = "SearchlyAI"
    ENV: str = "development"

    # Gemini
    GEMINI_API_KEY: str

    # Chunking
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 80

    # Vector search
    SIMILARITY_THRESHOLD: float = 0.3

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
