# SearchlyAI

SearchlyAI is a powerful Retrieve-Augmented Generation (RAG) search engine that allows users to ingest documents (PDF, TXT) and web pages, and then query them using natural language. It leverages Google's Gemini for embeddings and answer generation, and FAISS for efficient vector similarity search.

## 🚀 Features

-   **Multi-Source Ingestion**: Support for PDF documents, text files, and web pages.
-   **Semantic Search**: Uses vector embeddings to understand the *meaning* behind your query, not just keyword matching.
-   **RAG Architecture**: Retrieves relevant context and generates natural language answers using LLMs.
-   **Session Management**: Keeps data isolated per session.
-   **Efficient Vector Storage**: Uses FAISS for lighting-fast similarity search.

## 🛠️ Tech Stack

### Backend
-   **Framework**: FastAPI
-   **LLM & Embeddings**: Google Gemini (via LangChain/GenerativeAI)
-   **Vector Store**: FAISS
-   **Validation**: Pydantic

### Frontend
-   **Framework**: React (Vite)
-   **Language**: TypeScript
-   **Styling**: (Pending - to be built)

## 📂 Project Structure

```
SearchlyAI/
├── backend/            # FastAPI Backend
│   ├── app/            # Application logic
│   └── data/           # Local vector store data
├── frontend/           # React Frontend (Vite)
├── docker-compose.yml  # Docker orchestration
└── README.md           # This file
```

## 🏎️ Getting Started

### Prerequisites
-   Docker & Docker Compose
-   Node.js (for local frontend dev)
-   Python 3.10+ (for local backend dev)
-   Google Gemini API Key

### Running with Docker

1.  Set up your environment variables:
    ```bash
    cp backend/.env.example backend/.env
    # Edit backend/.env and add your GEMINI_API_KEY
    ```

2.  Run the stack:
    ```bash
    docker-compose up --build
    ```

### Local Development

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## 📄 License
MIT
