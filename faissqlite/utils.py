"""
utils.py: Utility functions for faissqlite.
"""

import numpy as np

def normalize_embedding(embedding: list) -> np.ndarray:
    arr = np.array(embedding, dtype=np.float32)
    norm = np.linalg.norm(arr)
    if norm == 0:
        return arr
    return arr / norm
