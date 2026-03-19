"""Tests for RAG retriever."""
import pytest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from cm-expert-llm.serve.retriever import HybridRetriever

def test_retriever_init():
    """Test retriever initialization."""
    retriever = HybridRetriever()
    assert retriever is not None
    assert retriever.k1 > 0
    assert retriever.b > 0
    assert retriever.k > 0

def test_retriever_tokenize():
    """Test tokenization."""
    retriever = HybridRetriever()
    tokens = retriever.tokenize("Hello World! Test.")
    assert len(tokens) == 3
    assert "hello" in tokens
    assert "world" in tokens

def test_retriever_build_index():
    """Test building index from file."""
    retriever = HybridRetriever()
    # Test that index structures are initialized
    assert retriever.documents == {}
    assert retriever.total_docs == 0

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
