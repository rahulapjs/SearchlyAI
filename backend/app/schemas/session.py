from pydantic import BaseModel


class SessionDeleteResponse(BaseModel):
    success: bool
    message: str
