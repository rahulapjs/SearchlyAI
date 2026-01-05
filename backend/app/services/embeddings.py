from google import genai
from typing import List
from app.core.config import settings


def embed_texts(texts: List[str]) -> List[List[float]]:
    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    embeddings = []
    
    for text in texts:
        result = client.models.embed_content(
            model="text-embedding-004",
            contents=text,
        )
        if hasattr(result, 'embeddings') and result.embeddings:
             embeddings.append(result.embeddings[0].values)
        elif hasattr(result, 'embedding'):
             embeddings.append(result.embedding.values)
        
    return embeddings
