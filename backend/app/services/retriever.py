import numpy as np
from typing import List, Tuple
from app.core.config import settings


def retrieve_chunks(
    index,
    chunks: List[str],
    query_embedding: List[float],
    top_k: int = 5
) -> List[Tuple[str, float]]:

    vector = np.array([query_embedding]).astype("float32")
    scores, indices = index.search(vector, top_k)

    results = []
    for idx, score in zip(indices[0], scores[0]):
        if idx == -1:
            continue
        similarity = 1 / (1 + score)
        if similarity >= settings.SIMILARITY_THRESHOLD:
            results.append((chunks[idx], similarity))

    return results
