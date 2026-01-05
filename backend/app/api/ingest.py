from fastapi import APIRouter, UploadFile, File, Header, HTTPException
from pathlib import Path

from app.schemas.ingest import IngestResponse
from app.utils.session_utils import ensure_session_dir
from app.utils.file_utils import validate_file, save_upload_file
from app.utils.text_utils import clean_text, is_valid_text

from app.services.loader import load_text_from_pdf, load_text_from_txt
from app.services.chunker import chunk_text
from app.services.embeddings import embed_texts
from app.services.vectorstore import save_vectorstore

from app.schemas.ingest import WebIngestRequest
from app.services.web_loader import load_text_from_web

router = APIRouter(tags=["Ingest"])


@router.post("/ingest/document", response_model=IngestResponse)
async def ingest_document(
    file: UploadFile = File(...),
    x_session_id: str = Header(..., alias="X-Session-ID"),
):
    try:
        validate_file(file)
        session_path = ensure_session_dir(x_session_id)

        file_path = save_upload_file(file, session_path)

        # Load text
        if file_path.suffix.lower() == ".pdf":
            text = load_text_from_pdf(file_path)
        else:
            text = load_text_from_txt(file_path)

        text = clean_text(text)

        if not is_valid_text(text):
            raise HTTPException(status_code=400, detail="File content too small")

        # Chunking
        chunks = chunk_text(text)

        # Embeddings
        embeddings = embed_texts(chunks)

        # Save vector store
        save_vectorstore(session_path, embeddings, chunks)

        return IngestResponse(
            success=True,
            session_id=x_session_id,
            chunks_added=len(chunks),
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail="Document ingestion failed")


@router.post("/ingest/web", response_model=IngestResponse)
async def ingest_web(
    payload: WebIngestRequest,
    x_session_id: str = Header(..., alias="X-Session-ID"),
):
    try:
        session_path = ensure_session_dir(x_session_id)

        # Load web text
        raw_text = load_text_from_web(str(payload.url))
        text = clean_text(raw_text)

        if not is_valid_text(text):
            raise HTTPException(status_code=400, detail="Web page content too small")

        # Chunking
        chunks = chunk_text(text)

        # Embeddings
        embeddings = embed_texts(chunks)

        # Save / overwrite vector store
        save_vectorstore(session_path, embeddings, chunks)

        return IngestResponse(
            success=True,
            session_id=x_session_id,
            chunks_added=len(chunks),
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail="Web ingestion failed")
