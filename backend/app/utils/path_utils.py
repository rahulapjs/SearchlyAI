from pathlib import Path


def faiss_index_path(session_path: Path) -> Path:
    return session_path / "index.faiss"


def chunks_path(session_path: Path) -> Path:
    return session_path / "chunks.json"
