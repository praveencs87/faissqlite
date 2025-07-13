"""
vector_store.py: FAISS interaction for faissqlite.
"""

import faiss
import numpy as np
from .db import SQLiteDB

class VectorStore:
    """Main interface for vector search using FAISS and SQLite."""
    def __init__(self, db_path: str, dim: int = 1536):
        self.db = SQLiteDB(db_path)
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.id_map = []  # Maps FAISS index to SQLite doc id
        self._load_embeddings()

    def _load_embeddings(self):
        """Load all embeddings from SQLite into FAISS index."""
        rows = self.db.get_all_embeddings()
        if not rows:
            return
        embeddings = [np.frombuffer(emb, dtype=np.float32) for _, emb in rows]
        if embeddings:
            mat = np.vstack(embeddings)
            self.index.add(mat)
            self.id_map = [doc_id for doc_id, _ in rows]

    def add_document(self, text: str, embedding: list):
        emb_np = np.array(embedding, dtype=np.float32)
        emb_bytes = emb_np.tobytes()
        doc_id = self.db.add_document(text, emb_bytes)
        self.index.add(emb_np.reshape(1, -1))
        self.id_map.append(doc_id)
        return doc_id

    def search(self, embedding: list, k: int = 5):
        emb_np = np.array(embedding, dtype=np.float32).reshape(1, -1)
        D, I = self.index.search(emb_np, k)
        results = []
        for idx in I[0]:
            if idx < 0 or idx >= len(self.id_map):
                continue
            doc_id = self.id_map[idx]
            doc = self.db.get_document(doc_id)
            if doc:
                results.append({"id": doc[0], "text": doc[1]})
        return results

    def save_index(self, path: str):
        faiss.write_index(self.index, path)

    def load_index(self, path: str):
        self.index = faiss.read_index(path)

    def rebuild_index(self):
        self.index = faiss.IndexFlatL2(self.dim)
        self.id_map = []
        self._load_embeddings()

    def close(self):
        self.db.close()
