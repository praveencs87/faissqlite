"""
A simple demo of faissqlite usage.
"""
from faissqlite import VectorStore
import numpy as np

# Example embedding (dim=4 for demo; use 1536+ for real use)
emb1 = np.random.rand(4).astype(np.float32)
emb2 = np.random.rand(4).astype(np.float32)
emb3 = np.random.rand(4).astype(np.float32)

store = VectorStore(db_path='demo_vectors.db', dim=4)

store.add_document("hello world", emb1)
store.add_document("foo bar", emb2)
store.add_document("baz qux", emb3)

query = emb1 + 0.01  # Slightly different
results = store.search(query, k=2)
print("Search results:", results)

store.close()
