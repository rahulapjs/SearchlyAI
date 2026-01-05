from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

print("Gemini key loaded:", bool(settings.GEMINI_API_KEY))

from app.api import ingest, query, session

from app.core.logging import setup_logging

setup_logging()

app = FastAPI(
    title="SemanticSearch AI",
    description="AI-powered semantic search engine using RAG",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(ingest.router, prefix="/api")
app.include_router(query.router, prefix="/api")
app.include_router(session.router, prefix="/api")


@app.get("/health")
def health_check():
    return {"status": "ok"}
