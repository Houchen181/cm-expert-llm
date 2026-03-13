#!/usr/bin/env python3
"""
Script to run the data ingestion pipeline.
Usage:
    python scripts/build_corpus.py --input-dir ./data/raw --output-file ./data/processed/sft.jsonl
"""
import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent.parent / 'src'
sys.path.insert(0, str(src_path))

from cmp_expert.data.pipeline import main as run_pipeline

if __name__ == '__main__':
    run_pipeline()
