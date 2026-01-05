import google.generativeai as genai
from typing import List
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)


def embed_texts(texts: List[str]) -> List[List[float]]:
    embeddings = []
    for text in texts:
        result = genai.embed_content(
            model="models/embedding-001",
            content=text,
            task_type="retrieval_document"
        )
        embeddings.append(result["embedding"])
    return embeddings
