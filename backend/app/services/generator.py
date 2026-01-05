from google import genai
from app.core.config import settings


def generate_answer(context: str, question: str) -> str:
    prompt = f"""
You are an AI search assistant.
Answer ONLY using the provided context.
If the answer is not present, say you don't know.

Context:
{context}

Question:
{question}
"""

    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text
