"""
Data ingestion pipeline for CM-Expert-LLM.

Ingests raw text files (papers, textbooks, notes) and converts them to
a normalized JSONL format suitable for training/fine-tuning.

Features:
- Recursive directory scanning
- Minimum length filtering
- Metadata extraction (source, timestamp)
- Optional chunking for long documents
"""

from pathlib import Path
import json
from datetime import datetime
from typing import List, Dict, Any


def chunk_text(text: str, tokens: int = 800, overlap: int = 120) -> List[str]:
    """
    Split text into overlapping chunks.
    
    Args:
        text: Input text to chunk
        tokens: Target tokens per chunk (approximate, using char ratio)
        overlap: Overlap between chunks
    
    Returns:
        List of text chunks
    """
    # Simple character-based chunking (approximate tokens)
    # 1 token ≈ 4 characters for English
    chars_per_token = 4
    chunk_size = tokens * chars_per_token
    overlap_size = overlap * chars_per_token
    
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        
        # Try to break at sentence/paragraph boundaries
        if end < len(text) and not chunk.endswith('\n'):
            # Look for sentence boundary
            for sep in ['. ', '\n\n', '.\n', '! ', '? ']:
                last_sep = chunk.rfind(sep)
                if last_sep > chunk_size // 2:
                    chunk = chunk[:start + last_sep + len(sep)]
                    break
        
        if chunk.strip():
            chunks.append(chunk.strip())
        
        # Move with overlap
        if len(chunk) < chunk_size:
            break
        start += chunk_size - overlap_size
    
    return chunks if chunks else [text]


def extract_metadata(source_path: Path) -> Dict[str, Any]:
    """Extract metadata from source file path and content."""
    return {
        "source_file": str(source_path),
        "source_type": "text_file",
        "timestamp": datetime.now().isoformat(),
    }


def build_corpus(
    input_dir: str,
    output_file: str,
    min_chars: int = 400,
    chunk_tokens: int = 800,
    chunk_overlap: int = 120,
    enable_chunking: bool = True
) -> int:
    """
    Build a corpus from raw text files.
    
    Args:
        input_dir: Directory containing raw .txt files
        output_file: Output JSONL file path
        min_chars: Minimum characters for a valid document
        chunk_tokens: Target tokens per chunk (if chunking enabled)
        chunk_overlap: Overlap between chunks
        enable_chunking: Whether to chunk long documents
    
    Returns:
        Number of records written
    """
    in_path = Path(input_dir)
    output_path = Path(output_file)
    
    if not in_path.exists():
        print(f"Input directory {input_dir} does not exist. Creating empty corpus.")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text("", encoding="utf-8")
        return 0
    
    records_written = 0
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for txt_file in sorted(in_path.rglob('*.txt')):
            try:
                text = txt_file.read_text(encoding='utf-8', errors='ignore').strip()
            except Exception as e:
                print(f"Warning: Could not read {txt_file}: {e}")
                continue
            
            if len(text) < min_chars:
                print(f"Skipping {txt_file}: too short ({len(text)} < {min_chars} chars)")
                continue
            
            metadata = extract_metadata(txt_file)
            
            if enable_chunking and len(text) > chunk_tokens * 4:
                # Chunk long documents
                chunks = chunk_text(text, chunk_tokens, chunk_overlap)
                for i, chunk in enumerate(chunks):
                    if len(chunk) >= min_chars:
                        record = {
                            "text": chunk,
                            "source": metadata["source_file"],
                            "chunk_id": i,
                            "total_chunks": len(chunks),
                            "metadata": metadata
                        }
                        f.write(json.dumps(record, ensure_ascii=False) + '\n')
                        records_written += 1
            else:
                # Keep as single record
                record = {
                    "text": text,
                    "source": metadata["source_file"],
                    "chunk_id": 0,
                    "total_chunks": 1,
                    "metadata": metadata
                }
                f.write(json.dumps(record, ensure_ascii=False) + '\n')
                records_written += 1
    
    print(f"Corpus built: {records_written} records written to {output_file}")
    return records_written


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Build corpus from raw text files')
    parser.add_argument('--input', '-i', default='./data/raw', help='Input directory')
    parser.add_argument('--output', '-o', default='./data/processed/sft.jsonl', help='Output file')
    parser.add_argument('--min-chars', type=int, default=400, help='Minimum characters')
    parser.add_argument('--chunk-tokens', type=int, default=800, help='Tokens per chunk')
    parser.add_argument('--chunk-overlap', type=int, default=120, help='Chunk overlap')
    parser.add_argument('--no-chunking', action='store_true', help='Disable chunking')
    
    args = parser.parse_args()
    
    build_corpus(
        input_dir=args.input,
        output_file=args.output,
        min_chars=args.min_chars,
        chunk_tokens=args.chunk_tokens,
        chunk_overlap=args.chunk_overlap,
        enable_chunking=not args.no_chunking
    )
