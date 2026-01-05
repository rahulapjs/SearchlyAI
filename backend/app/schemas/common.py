from pydantic import BaseModel
from typing import Optional


class BaseResponse(BaseModel):
    success: bool = True
    message: Optional[str] = None


class SourceChunk(BaseModel):
    content: str
    score: float
    source: str
