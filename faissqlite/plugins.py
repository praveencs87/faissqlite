"""
Embedding plugin system for faissqlite.
"""
from typing import Protocol, List

class EmbeddingGenerator(Protocol):
    def embed(self, text: str) -> List[float]:
        ...

# Example: Dummy embedding generator
class DummyEmbeddingGenerator:
    def embed(self, text: str) -> List[float]:
        """Return a fixed dummy embedding based on input text (for testing)."""
        return [float(ord(c)) for c in text][:10]

# Stub for OpenAI embedding generator
class OpenAIEmbeddingGenerator:
    def __init__(self, api_key: str = "sk-..."):
        """
        Usage:
            plugin = OpenAIEmbeddingGenerator(api_key="sk-...")
            emb = plugin.embed("your text")
        Requires: openai package (`pip install openai`)
        """
        self.api_key = api_key
        # import openai
        # openai.api_key = api_key
    def embed(self, text: str) -> List[float]:
        raise NotImplementedError("Install openai and implement API call here.")

# Stub for HuggingFace embedding generator
class HuggingFaceEmbeddingGenerator:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Usage:
            plugin = HuggingFaceEmbeddingGenerator(model_name="...")
            emb = plugin.embed("your text")
        Requires: sentence-transformers (`pip install sentence-transformers`)
        """
        self.model_name = model_name
        # from sentence_transformers import SentenceTransformer
        # self.model = SentenceTransformer(model_name)
    def embed(self, text: str) -> List[float]:
        raise NotImplementedError("Install sentence-transformers and implement model inference here.")

# Registry for plugins
embedding_plugins = {
    "dummy": DummyEmbeddingGenerator(),
    "openai": OpenAIEmbeddingGenerator,  # Usage: OpenAIEmbeddingGenerator(api_key)
    "hf": HuggingFaceEmbeddingGenerator, # Usage: HuggingFaceEmbeddingGenerator(model_name)
}

def get_embedding_generator(name: str, **kwargs) -> EmbeddingGenerator:
    """Get embedding generator by name. kwargs passed to constructor for openai/hf."""
    plugin = embedding_plugins[name]
    if callable(plugin):
        return plugin(**kwargs)
    return plugin
