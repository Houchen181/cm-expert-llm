"""Tests for RAG retriever."""
import pytest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from cmp_expert.serve.retriever import HybridRetriever

def test_retriever_init():
    """Test retriever initialization."""
    retriever = HybridRetriever()
    assert retriever is not None
    assert retriever.k1 > 0
    assert retriever.b > 0

def test_retriever_add_docs():
    """Test adding documents."""
    retriever = HybridRetriever()
    docs = [
        {"id": "1", "text": "Superconductivity basics"},
        {"id": "2", "text": "Topological insulators"}
    ]
    retriever.add_documents(docs)
    assert len(retriever.documents) == 2

def test_retriever_search():
    """Test search functionality."""
    retriever = HybridRetriever()
    retriever.add_documents([
        {"id": "1", "text": "Superconductivity is quantum phenomenon"},
        {"id": "2", "text": "Topology in condensed matter"}
    ])
    results = retriever.search("superconductivity", k=1)
    assert len(results) > 0
    assert results[0]['id'] == '1'

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
