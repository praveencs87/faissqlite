"""
CLI for faissqlite: index, query, rebuild
"""
import argparse
import numpy as np
from .vector_store import VectorStore

def main():
    parser = argparse.ArgumentParser(description="faissqlite CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Index command
    idx_parser = subparsers.add_parser("index", help="Add a document")
    idx_parser.add_argument("--db", required=True, help="SQLite DB path")
    idx_parser.add_argument("--dim", type=int, default=1536)
    idx_parser.add_argument("--text", required=True, help="Document text")
    idx_parser.add_argument("--embedding", nargs='+', type=float, required=True, help="Embedding values (space separated)")

    # Query command
    qry_parser = subparsers.add_parser("query", help="Search for similar docs")
    qry_parser.add_argument("--db", required=True)
    qry_parser.add_argument("--dim", type=int, default=1536)
    qry_parser.add_argument("--embedding", nargs='+', type=float, required=True)
    qry_parser.add_argument("--k", type=int, default=5)

    # Rebuild command
    reb_parser = subparsers.add_parser("rebuild", help="Rebuild the FAISS index from SQLite")
    reb_parser.add_argument("--db", required=True)
    reb_parser.add_argument("--dim", type=int, default=1536)

    args = parser.parse_args()

    if args.command == "index":
        store = VectorStore(args.db, dim=args.dim)
        doc_id = store.add_document(args.text, args.embedding)
        print(f"Added document with id {doc_id}")
        store.close()
    elif args.command == "query":
        store = VectorStore(args.db, dim=args.dim)
        results = store.search(args.embedding, k=args.k)
        print("Results:")
        for r in results:
            print(r)
        store.close()
    elif args.command == "rebuild":
        store = VectorStore(args.db, dim=args.dim)
        store.rebuild_index()
        print("Index rebuilt from SQLite.")
        store.close()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
