"""
Data Ingestion Pipeline for cm-expert-llm.

Ingests raw text/markdown/PDF files from `data/raw`, chunks them, and outputs
a normalized JSONL file for training/evaluation.
"""
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any
import re

def load_text_file(file_path: Path) -> str:
    """Load text content from a file."""
    try:
        return file_path.read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def chunk_text(text: str, chunk_size: int = 800, overlap: int = 120) -> List[str]:
    """
    Split text into overlapping chunks of approximately `chunk_size` tokens/words.
    Simple word-based chunking for scaffold; upgrade to token-based later.
    """
    words = text.split()
    chunks = []
    if len(words) == 0:
        return chunks
    
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]
        if not chunk_words:
            break
        chunks.append(" ".join(chunk_words))
        start += chunk_size - overlap
        if start >= len(words):
            break
    return chunks

def extract_metadata(file_path: Path, content: str) -> Dict[str, Any]:
    """Extract or infer metadata from file content and path."""
    meta = {
        "source_file": str(file_path),
        "char_count": len(content),
        "type": "raw_text"
    }
    # Simple heuristic: if file looks like a paper (has 'Abstract' or 'Authors')
    if re.search(r'abstract|authors|keywords', content[:500].lower()):
        meta["type"] = "scientific_paper"
    return meta

def process_directory(input_dir: Path, output_file: Path, chunk_size: int, overlap: int) -> None:
    """Process all text files in input_dir and write to output_file."""
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    total_chunks = 0
    with open(output_file, 'w', encoding='utf-8') as f_out:
        for file_path in input_dir.rglob('*'):
            if file_path.is_file() and file_path.suffix in ['.txt', '.md', '.tex']:
                content = load_text_file(file_path)
                if len(content.strip()) < 400:
                    continue  # Skip very short files
                
                meta = extract_metadata(file_path, content)
                chunks = chunk_text(content, chunk_size, overlap)
                
                for i, chunk in enumerate(chunks):
                    record = {
                        "id": f"{meta['source_file']}#chunk{i}",
                        "text": chunk,
                        "metadata": {
                            **meta,
                            "chunk_index": i,
                            "total_chunks": len(chunks)
                        }
                    }
                    f_out.write(json.dumps(record, ensure_ascii=False) + '\n')
                    total_chunks += 1
                print(f"Processed {file_path.name}: {len(chunks)} chunks")
    
    print(f"Ingestion complete. Total chunks written: {total_chunks} to {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Ingest raw data for cm-expert-llm')
    parser.add_argument('--input-dir', type=str, default='./data/raw', help='Input directory')
    parser.add_argument('--output-file', type=str, default='./data/processed/sft.jsonl', help='Output JSONL file')
    parser.add_argument('--chunk-size', type=int, default=800, help='Chunk size (words)')
    parser.add_argument('--overlap', type=int, default=120, help='Overlap size (words)')
    
    args = parser.parse_args()
    
    input_path = Path(args.input_dir)
    output_path = Path(args.output_file)
    
    if not input_path.exists():
        print(f"Input directory {input_path} does not exist. Creating placeholder...")
        input_path.mkdir(parents=True, exist_ok=True)
        (input_path / "README.md").write_text("# Raw Data\nPlace your raw text/markdown files here.")
        print(f"Placeholder created at {input_path}. Please add files and re-run.")
        return

    process_directory(input_path, output_path, args.chunk_size, args.overlap)

if __name__ == '__main__':
    main()
