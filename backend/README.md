# RAG Search Engine Backend

This is the backend for a RAG (Retrieval-Augmented Generation) Search Engine built with FastAPI.

## Structure
- `app/api`: API route definitions
- `app/core`: Core configuration and logging
- `app/services`: Business logic (ingestion, chunking, embeddings, etc.)
- `app/schemas`: Pydantic models
- `app/utils`: Helper functions
- `app/llm`: LLM abstractions (OpenAI, Gemini)

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   Copy `.env.example` to `.env` and fill in your API keys.

4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```
