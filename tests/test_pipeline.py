"""Tests for data pipeline."""
import pytest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from condensai.data.pipeline import chunk_text, load_text_file

def test_chunk_text_short():
    """Test chunking short text."""
    text = "This is a test."
    chunks = chunk_text(text, chunk_size=100, overlap=0)
    assert len(chunks) >= 1
    assert "This is a test." in chunks[0]

def test_chunk_text_long():
    """Test chunking long text."""
    text = "word " * 200
    chunks = chunk_text(text, chunk_size=50, overlap=10)
    assert len(chunks) > 1

def test_chunk_text_empty():
    """Test chunking empty text."""
    chunks = chunk_text("", chunk_size=100)
    assert len(chunks) == 0

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
