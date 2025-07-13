# faissqlite

[![PyPI version](https://img.shields.io/pypi/v/faissqlite.svg)](https://pypi.org/project/faissqlite/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/praveencs87/faissqlite/actions/workflows/python-package.yml/badge.svg)](https://github.com/praveencs87/faissqlite/actions)

**faissqlite** is an open-source Python library that seamlessly combines FAISS (Facebook AI Similarity Search) with SQLite for efficient, persistent, and lightweight vector search and storage. It is designed for developers and researchers who want to build scalable semantic search, retrieval-augmented generation (RAG), and hybrid search systems with minimal setup.

---

## 🚀 Features

| Feature                | Description                                                        |
|------------------------|--------------------------------------------------------------------|
| `add_document`         | Store a document and its embedding in SQLite and FAISS              |
| `search`               | Use FAISS to find top-K vectors; retrieve metadata from SQLite      |
| `save_index` / `load_index` | Persist/load the FAISS index to/from disk                     |
| `rebuild_index`        | Rebuild the FAISS index from SQLite if out-of-sync                  |
| CLI Tool (optional)    | Command-line interface for indexing/querying                        |
| REST API (optional)    | FastAPI wrapper for embedding and querying                          |

---

## 📦 Project Structure

```
faissqlite/
├── README.md
├── requirements.txt
├── LICENSE
├── setup.py
├── faissqlite/
│   ├── __init__.py
│   ├── db.py               # SQLite interface
│   ├── vector_store.py     # FAISS interaction
│   ├── utils.py
│   └── config.py
├── examples/
│   └── simple_demo.py
└── tests/
    └── test_core.py
```

---

## 🛠️ Installation

### From PyPI (coming soon)
```bash
pip install faissqlite
```

### From source
```bash
git clone https://github.com/praveencs87/faissqlite.git
cd faissqlite
pip install -e .
```

---

## 🧑‍💻 Basic Usage

```python
from faissqlite import VectorStore

store = VectorStore(db_path="my_vectors.db")

# Add a document
embedding = [0.1, 0.2, 0.3, ...]  # your embedding here
store.add_document("hello world", embedding)

# Search
results = store.search(embedding, k=5)
for doc in results:
    print(doc)
```

---

## 🖥️ CLI Usage

Install with pip (editable or from PyPI), then:

```bash
faissqlite index --db my_vectors.db --dim 1536 --text "hello world" --embedding 0.1 0.2 0.3 ...
faissqlite query --db my_vectors.db --dim 1536 --embedding 0.1 0.2 0.3 ... --k 5
faissqlite rebuild --db my_vectors.db --dim 1536
```

---

## 🌐 REST API (FastAPI)

Run the API:
```bash
uvicorn faissqlite.api:app --reload
```

Example endpoints:
- `POST /add` – Add a document (`{"text": ..., "embedding": [...], "db_path": ..., "dim": ...}`)
- `POST /search` – Search for similar vectors (`{"embedding": [...], "k": 5, "db_path": ..., "dim": ...}`)
- `POST /rebuild` – Rebuild index (`{"db_path": ..., "dim": ...}`)

---

## 🔌 Embedding Plugin System

faissqlite supports pluggable embedding generators (OpenAI, HuggingFace, etc.) via the plugin system. See `faissqlite/plugins.py` for examples and extension points.

---

## ⚖️ License

MIT License. See [LICENSE](LICENSE) for details.

---

## 🤝 Contributing

Contributions are welcome! Please open issues or pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines (coming soon).

---

## 💡 Roadmap & Advanced Ideas
- Embedding generator plugin system (OpenAI, HuggingFace, etc.)
- Hybrid search: combine metadata filtering + semantic match
- REST API (FastAPI)
- UI dashboard (Streamlit)
- Python SDK and CLI

---

## 🌐 Links
- GitHub: https://github.com/yourusername/faissqlite
- PyPI: https://pypi.org/project/faissqlite

---

## Acknowledgements
- [FAISS](https://github.com/facebookresearch/faiss)
- [SQLite](https://www.sqlite.org/index.html)

---

## 👤 Author

Maintained by [Praveen CS](https://www.linkedin.com/in/praveen-cs/)
- GitHub: [praveencs87](https://github.com/praveencs87)

*The 'Author' section is optional for open source projects, but can help users and contributors connect with the maintainer.*

---

*Happy hacking!*
