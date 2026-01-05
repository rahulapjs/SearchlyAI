from fastapi import APIRouter, Header, HTTPException

from app.schemas.query import QueryRequest, QueryResponse
from app.schemas.common import SourceChunk
from app.utils.session_utils import get_session_path
from app.services.embeddings import embed_texts
from app.services.vectorstore import load_vectorstore
from app.services.retriever import retrieve_chunks
from app.services.generator import generate_answer

router = APIRouter(tags=["Query"])


@router.post("/query", response_model=QueryResponse)
async def query_search(
    payload: QueryRequest,
    x_session_id: str = Header(..., alias="X-Session-ID"),
):
    session_path = get_session_path(x_session_id)

    if not session_path.exists():
        raise HTTPException(status_code=400, detail="No data found for this session")

    try:
        # Load vector store
        index, chunks = load_vectorstore(session_path)

        # Embed query
        query_embedding = embed_texts([payload.question])[0]

        # Retrieve relevant chunks
        results = retrieve_chunks(
            index=index,
            chunks=chunks,
            query_embedding=query_embedding,
            top_k=payload.top_k,
        )

        if not results:
            return QueryResponse(
                answer="I couldn't find relevant information in the provided data.",
                sources=[],
            )

        context = "\n\n".join([r[0] for r in results])

        answer = generate_answer(context, payload.question)

        sources = [
            SourceChunk(
                content=chunk,
                score=score,
                source="uploaded_document",
            )
            for chunk, score in results
        ]

        return QueryResponse(answer=answer, sources=sources)

    except Exception:
        raise HTTPException(status_code=500, detail="Query processing failed")
