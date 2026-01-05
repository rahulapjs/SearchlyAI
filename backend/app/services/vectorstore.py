import faiss
import json
import numpy as np
from pathlib import Path
from typing import List
from app.utils.path_utils import faiss_index_path, chunks_path


def save_vectorstore(
    session_path: Path,
    embeddings: List[List[float]],
    chunks: List[str]
):
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)

    vectors = np.array(embeddings).astype("float32")
    index.add(vectors)

    faiss.write_index(index, str(faiss_index_path(session_path)))

    with open(chunks_path(session_path), "w", encoding="utf-8") as f:
        json.dump(chunks, f)


def load_vectorstore(session_path: Path):
    index = faiss.read_index(str(faiss_index_path(session_path)))
    with open(chunks_path(session_path), "r", encoding="utf-8") as f:
        chunks = json.load(f)
    return index, chunks
