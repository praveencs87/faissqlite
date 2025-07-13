"""
Basic test for faissqlite core functionality.
"""
import unittest
import numpy as np
from faissqlite import VectorStore

class TestVectorStore(unittest.TestCase):
    def setUp(self):
        self.store = VectorStore(db_path=':memory:', dim=4)

    def tearDown(self):
        self.store.close()

    def test_add_and_search(self):
        emb = np.array([0.1, 0.2, 0.3, 0.4], dtype=np.float32)
        self.store.add_document("doc1", emb)
        res = self.store.search(emb, k=1)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]['text'], "doc1")

if __name__ == '__main__':
    unittest.main()
