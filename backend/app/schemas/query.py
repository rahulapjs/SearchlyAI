from pydantic import BaseModel
from typing import List
from .common import SourceChunk


class QueryRequest(BaseModel):
    question: str
    top_k: int = 5


class QueryResponse(BaseModel):
    answer: str
    sources: List[SourceChunk]
