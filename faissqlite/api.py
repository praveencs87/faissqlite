"""
FastAPI REST API for faissqlite
"""
from fastapi import FastAPI
from pydantic import BaseModel
from .vector_store import VectorStore

app = FastAPI()

class AddRequest(BaseModel):
    text: str
    embedding: list
    db_path: str = "vectors.db"
    dim: int = 1536

class SearchRequest(BaseModel):
    embedding: list
    k: int = 5
    db_path: str = "vectors.db"
    dim: int = 1536

class RebuildRequest(BaseModel):
    db_path: str = "vectors.db"
    dim: int = 1536

@app.post("/add")
def add_doc(req: AddRequest):
    store = VectorStore(req.db_path, dim=req.dim)
    doc_id = store.add_document(req.text, req.embedding)
    store.close()
    return {"doc_id": doc_id}

@app.post("/search")
def search(req: SearchRequest):
    store = VectorStore(req.db_path, dim=req.dim)
    results = store.search(req.embedding, k=req.k)
    store.close()
    return {"results": results}

@app.post("/rebuild")
def rebuild(req: RebuildRequest):
    store = VectorStore(req.db_path, dim=req.dim)
    store.rebuild_index()
    store.close()
    return {"status": "rebuilt"}
