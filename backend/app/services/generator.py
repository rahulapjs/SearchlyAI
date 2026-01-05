import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)


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

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()
