from pydantic import BaseModel, HttpUrl
from typing import Optional
from .common import BaseResponse


class WebIngestRequest(BaseModel):
    url: HttpUrl


class IngestResponse(BaseResponse):
    session_id: str
    chunks_added: int
