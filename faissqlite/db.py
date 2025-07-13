"""
db.py: SQLite interface for faissqlite.
"""

import sqlite3
from typing import Any, List, Tuple, Optional

class SQLiteDB:
    """SQLite interface for storing documents and metadata."""
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self._init_tables()

    def _init_tables(self):
        cur = self.conn.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            embedding BLOB
        )
        ''')
        self.conn.commit()

    def add_document(self, text: str, embedding: bytes):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO documents (text, embedding) VALUES (?, ?)", (text, embedding))
        self.conn.commit()
        return cur.lastrowid

    def get_document(self, doc_id: int) -> Optional[Tuple[int, str, bytes]]:
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM documents WHERE id = ?", (doc_id,))
        return cur.fetchone()

    def get_all_embeddings(self) -> List[Tuple[int, bytes]]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, embedding FROM documents")
        return cur.fetchall()

    def close(self):
        self.conn.close()
