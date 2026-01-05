# SearchlyAI Backend

This is the backend API for SearchlyAI, built with FastAPI.

## Structure
- `app/api`: API route definitions
- `app/core`: Core configuration and logging
- `app/services`: Business logic (ingestion, chunking, embeddings, etc.)
- `app/schemas`: Pydantic models
- `app/utils`: Helper functions

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
   Copy `.env.example` to `.env` and fill in your API keys (Gemini API Key is required).

4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```
