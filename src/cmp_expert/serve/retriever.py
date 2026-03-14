"""
Hybrid Retrieval for RAG System.
Implements multi-stage retrieval with:
- BM25 sparse retrieval
- Dense vector retrieval (sentence transformers)
- Reciprocal Rank Fusion (RRF) for combining results
- Optional reranking with cross-encoder
"""

import json
import re
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from collections import defaultdict
import math


@dataclass
class RetrievedChunk:
    """A retrieved chunk with score and metadata."""
    chunk_id: str
    text: str
    score: float
    source: str
    metadata: Dict[str, Any]
    rank_bm25: Optional[int] = None
    rank_dense: Optional[int] = None
    rank_final: Optional[int] = None


class HybridRetriever:
    """
    Hybrid retriever combining BM25 and dense retrieval.
    
    Features:
    - BM25 keyword-based retrieval
    - Dense vector retrieval (placeholder for sentence transformers)
    - Reciprocal Rank Fusion (RRF) for combining rankings
    - Optional cross-encoder reranking
    """
    
    def __init__(self, k1: float = 1.5, b: float = 0.75, k: int = 60):
        """
        Initialize hybrid retriever.
        
        Args:
            k1: BM25 term frequency saturation parameter
            b: BM25 length normalization parameter
            k: RRF constant for rank fusion
        """
        self.k1 = k1
        self.b = b
        self.k = k
        
        # Index structures
        self.documents: Dict[str, Dict[str, Any]] = {}
        self.doc_lengths: Dict[str, int] = {}
        self.avg_doc_length: float = 0.0
        self.total_docs: int = 0
        
        # Term statistics for BM25
        self.term_doc_freq: Dict[str, int] = defaultdict(int)
        self.doc_term_freq: Dict[str, Dict[str, int]] = {}
        
        # Dense index (placeholder)
        self.dense_index_built: bool = False
        
    def tokenize(self, text: str) -> List[str]:
        """Simple tokenization with lowercasing."""
        return re.findall(r'\b\w+\b', text.lower())
    
    def build_index(self, chunks_file: Path) -> int:
        """
        Build retrieval index from JSONL chunks file.
        
        Args:
            chunks_file: Path to JSONL file with chunks
            
        Returns:
            Number of documents indexed
        """
        if not chunks_file.exists():
            raise FileNotFoundError(f"Chunks file not found: {chunks_file}")
        
        total_length = 0
        with open(chunks_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    data = json.loads(line)
                    chunk_id = data.get('id', f"chunk_{self.total_docs}")
                    text = data.get('text', '')
                    metadata = data.get('metadata', {})
                    
                    # Store document
                    self.documents[chunk_id] = {
                        'text': text,
                        'metadata': metadata,
                        'source': metadata.get('source_file', 'unknown')
                    }
                    
                    # Tokenize and compute statistics
                    tokens = self.tokenize(text)
                    self.doc_lengths[chunk_id] = len(tokens)
                    total_length += len(tokens)
                    
                    # Term frequencies
                    term_freq = defaultdict(int)
                    for token in set(tokens):  # Unique terms in doc
                        term_freq[token] += 1
                        self.term_doc_freq[token] += 1
                    
                    self.doc_term_freq[chunk_id] = dict(term_freq)
                    self.total_docs += 1
        
        if self.total_docs > 0:
            self.avg_doc_length = total_length / self.total_docs
        
        print(f"Built index with {self.total_docs} documents, avg length: {self.avg_doc_length:.1f} tokens")
        return self.total_docs
    
    def _bm25_score(self, doc_id: str, query_terms: List[str]) -> float:
        """Compute BM25 score for a document given query terms."""
        if doc_id not in self.doc_term_freq:
            return 0.0
        
        score = 0.0
        doc_len = self.doc_lengths[doc_id]
        doc_terms = self.doc_term_freq[doc_id]
        
        for term in query_terms:
            if term not in self.term_doc_freq:
                continue
            
            # Term frequency in document
            tf = doc_terms.get(term, 0)
            if tf == 0:
                continue
            
            # Document frequency
            df = self.term_doc_freq[term]
            
            # BM25 formula
            numerator = tf * (self.k1 + 1)
            denominator = tf + self.k1 * (1 - self.b + self.b * doc_len / self.avg_doc_length)
            idf = math.log((self.total_docs - df + 0.5) / (df + 0.5) + 1)
            
            score += (numerator / denominator) * idf
        
        return score
    
    def bm25_search(self, query: str, top_k: int = 10) -> List[RetrievedChunk]:
        """
        Perform BM25 search.
        
        Args:
            query: Query string
            top_k: Number of results to return
            
        Returns:
            List of RetrievedChunk sorted by BM25 score
        """
        query_terms = self.tokenize(query)
        
        # Score all documents
        scores = {}
        for doc_id in self.documents:
            score = self._bm25_score(doc_id, query_terms)
            if score > 0:
                scores[doc_id] = score
        
        # Sort by score
        sorted_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_k]
        
        results = []
        for rank, (doc_id, score) in enumerate(sorted_docs, 1):
            doc = self.documents[doc_id]
            results.append(RetrievedChunk(
                chunk_id=doc_id,
                text=doc['text'],
                score=score,
                source=doc['source'],
                metadata=doc['metadata'],
                rank_bm25=rank
            ))
        
        return results
    
    def dense_search(self, query: str, top_k: int = 10) -> List[RetrievedChunk]:
        """
        Dense vector search (placeholder).
        
        In production, this would use sentence transformers or similar
        to encode query and documents, then perform similarity search.
        
        For now, returns empty list or falls back to BM25.
        """
        if not self.dense_index_built:
            # Placeholder: return BM25 results with lower scores
            bm25_results = self.bm25_search(query, top_k * 2)
            for i, chunk in enumerate(bm25_results):
                chunk.rank_dense = i + 1
                chunk.score = chunk.score * 0.5  # Downweight for hybrid
            return bm25_results[:top_k]
        
        return []
    
    def reciprocal_rank_fusion(self, bm25_results: List[RetrievedChunk], 
                                dense_results: List[RetrievedChunk], 
                                top_k: int = 10) -> List[RetrievedChunk]:
        """
        Combine BM25 and dense results using Reciprocal Rank Fusion.
        
        RRF score = sum(1 / (k + rank)) for each ranking
        
        Args:
            bm25_results: Results from BM25 search
            dense_results: Results from dense search
            top_k: Final number of results
            
        Returns:
            Fused and ranked results
        """
        rrf_scores = defaultdict(float)
        chunk_map = {}
        
        # Score from BM25 rankings
        for rank, chunk in enumerate(bm25_results, 1):
            rrf_scores[chunk.chunk_id] += 1.0 / (self.k + rank)
            if chunk.chunk_id not in chunk_map:
                chunk_map[chunk.chunk_id] = chunk
        
        # Score from dense rankings
        for rank, chunk in enumerate(dense_results, 1):
            rrf_scores[chunk.chunk_id] += 1.0 / (self.k + rank)
            if chunk.chunk_id not in chunk_map:
                chunk_map[chunk.chunk_id] = chunk
        
        # Sort by RRF score
        sorted_ids = sorted(rrf_scores.keys(), key=lambda x: rrf_scores[x], reverse=True)
        
        results = []
        for final_rank, chunk_id in enumerate(sorted_ids[:top_k]):
            chunk = chunk_map[chunk_id]
            chunk.score = rrf_scores[chunk_id]
            chunk.rank_final = final_rank + 1
            results.append(chunk)
        
        return results
    
    def hybrid_search(self, query: str, top_k: int = 10, 
                      use_dense: bool = False) -> List[RetrievedChunk]:
        """
        Perform hybrid search combining BM25 and dense retrieval.
        
        Args:
            query: Query string
            top_k: Number of results
            use_dense: Whether to include dense retrieval
            
        Returns:
            Hybrid ranked results
        """
        # Get BM25 results
        bm25_results = self.bm25_search(query, top_k * 2)
        
        if not use_dense or not self.dense_index_built:
            # Return BM25 results with final ranks
            for i, chunk in enumerate(bm25_results[:top_k]):
                chunk.rank_final = i + 1
            return bm25_results[:top_k]
        
        # Get dense results
        dense_results = self.dense_search(query, top_k * 2)
        
        # Fuse results
        return self.reciprocal_rank_fusion(bm25_results, dense_results, top_k)
    
    def build_dense_index(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Build dense index using sentence transformers.
        
        Args:
            model_name: Name of sentence transformer model
            
        Note: This is a placeholder. In production, would load model and encode all documents.
        """
        print(f"Building dense index with model: {model_name}")
        print("Note: Dense index requires sentence-transformers package")
        # TODO: Implement with sentence-transformers
        # from sentence_transformers import SentenceTransformer
        # model = SentenceTransformer(model_name)
        # embeddings = model.encode([doc['text'] for doc in self.documents.values()])
        self.dense_index_built = False  # Placeholder


def main():
    """Test hybrid retriever."""
    import argparse
    parser = argparse.ArgumentParser(description='Test hybrid retriever')
    parser.add_argument('--corpus', type=str, default='./data/processed/sft.jsonl',
                       help='JSONL corpus file')
    parser.add_argument('--query', type=str, 
                       default='What is the Meissner effect?',
                       help='Test query')
    parser.add_argument('--top-k', type=int, default=5, help='Number of results')
    args = parser.parse_args()
    
    retriever = HybridRetriever()
    
    corpus_path = Path(args.corpus)
    if corpus_path.exists():
        retriever.build_index(corpus_path)
        results = retriever.hybrid_search(args.query, top_k=args.top_k)
        
        print(f"\nQuery: {args.query}")
        print(f"Found {len(results)} results:\n")
        for i, chunk in enumerate(results, 1):
            print(f"{i}. [Score: {chunk.score:.4f}] {chunk.text[:200]}...")
            print(f"   Source: {chunk.source}")
            print()
    else:
        print(f"Corpus not found: {corpus_path}")
        print("Run data ingestion pipeline first.")


if __name__ == '__main__':
    main()
