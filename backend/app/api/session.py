from fastapi import APIRouter
from app.schemas.session import SessionDeleteResponse
from app.utils.session_utils import delete_session

router = APIRouter(tags=["Session"])


@router.delete("/session/{session_id}", response_model=SessionDeleteResponse)
def clear_session(session_id: str):
    deleted = delete_session(session_id)

    if deleted:
        return SessionDeleteResponse(
            success=True,
            message=f"Session {session_id} deleted successfully",
        )

    return SessionDeleteResponse(
        success=False,
        message="Session not found",
    )
