import os
import shutil
from pathlib import Path

DATA_DIR = Path("data")


def get_session_path(session_id: str) -> Path:
    """
    Returns the folder path for a session.
    """
    return DATA_DIR / session_id


def ensure_session_dir(session_id: str) -> Path:
    """
    Creates session directory if not exists.
    """
    session_path = get_session_path(session_id)
    session_path.mkdir(parents=True, exist_ok=True)
    return session_path


def delete_session(session_id: str) -> bool:
    """
    Deletes all data for a session.
    """
    session_path = get_session_path(session_id)
    if session_path.exists():
        shutil.rmtree(session_path)
        return True
    return False
