"""
Test for embedding plugin system (dummy plugin).
"""
import unittest
from faissqlite.plugins import get_embedding_generator

class TestDummyPlugin(unittest.TestCase):
    def test_dummy_embed(self):
        plugin = get_embedding_generator("dummy")
        out = plugin.embed("abc")
        self.assertEqual(out, [97.0, 98.0, 99.0])

if __name__ == "__main__":
    unittest.main()
