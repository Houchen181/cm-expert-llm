"""
CM Expert LLM API with RAG serving.
Provides endpoints for:
- Health checks
- RAG-based question answering
- Document retrieval
- Benchmark evaluation
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from pathlib import Path
import json

from .retriever import HybridRetriever, RetrievedChunk

app = FastAPI(
    title='CM Expert LLM API',
    description='Condensed Matter Physics Expert LLM with RAG',
    version='0.1.0'
)

# Global retriever instance
retriever: Optional[HybridRetriever] = None


class QueryRequest(BaseModel):
    """Request model for RAG query."""
    query: str
    top_k: int = 5
    use_rag: bool = True
    include_sources: bool = True


class QueryResponse(BaseModel):
    """Response model for RAG query."""
    query: str
    answer: str
    sources: List[Dict[str, Any]]
    confidence: float
    latency_ms: float


class RetrieveRequest(BaseModel):
    """Request model for retrieval."""
    query: str
    top_k: int = 10
    use_dense: bool = False


class RetrieveResponse(BaseModel):
    """Response model for retrieval."""
    query: str
    chunks: List[Dict[str, Any]]
    total_found: int


@app.on_event("load")
async def load_corpus():
    """Load corpus on startup if available."""
    global retriever
    corpus_path = Path("./data/processed/sft.jsonl")
    if corpus_path.exists():
        retriever = HybridRetriever()
        try:
            retriever.build_index(corpus_path)
            print(f"Loaded corpus with {retriever.total_docs} documents")
        except Exception as e:
            print(f"Error loading corpus: {e}")
    else:
        print("Corpus not found, retriever not initialized")


@app.get("/health")
def health():
    """Health check endpoint."""
    return {
        'ok': True,
        'retriever_ready': retriever is not None,
        'documents_indexed': retriever.total_docs if retriever else 0
    }


@app.post("/retrieve", response_model=RetrieveResponse)
def retrieve(request: RetrieveRequest):
    """
    Retrieve relevant chunks for a query.
    
    Returns top-k most relevant chunks using hybrid retrieval.
    """
    if retriever is None:
        raise HTTPException(status_code=503, detail="Retriever not initialized")
    
    try:
        chunks = retriever.hybrid_search(
            request.query,
            top_k=request.top_k,
            use_dense=request.use_dense
        )
        
        return RetrieveResponse(
            query=request.query,
            chunks=[
                {
                    'chunk_id': c.chunk_id,
                    'text': c.text,
                    'score': c.score,
                    'source': c.source,
                    'metadata': c.metadata,
                    'rank_final': c.rank_final
                }
                for c in chunks
            ],
            total_found=len(chunks)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/query", response_model=QueryResponse)
def query_rag(request: QueryRequest):
    """
    Answer a question using RAG.
    
    Retrieves relevant context and generates answer.
    Note: Full implementation requires LLM integration.
    """
    if retriever is None:
        raise HTTPException(status_code=503, detail="Retriever not initialized")
    
    import time
    start_time = time.time()
    
    try:
        # Retrieve relevant chunks
        chunks = retriever.hybrid_search(
            request.query,
            top_k=request.top_k,
            use_dense=False  # Dense not yet implemented
        )
        
        # Build context from chunks
        context_parts = []
        sources = []
        for i, chunk in enumerate(chunks):
            context_parts.append(f"[Source {i+1}]: {chunk.text}")
            sources.append({
                'chunk_id': chunk.chunk_id,
                'source': chunk.source,
                'score': chunk.score,
                'rank': chunk.rank_final
            })
        
        context = "\n\n".join(context_parts)
        
        # Generate answer (placeholder - would integrate with LLM)
        answer = f"Based on {len(sources)} relevant sources:\n\n{context}\n\n[LLM would generate answer here based on context]"
        
        latency_ms = (time.time() - start_time) * 1000
        
        return QueryResponse(
            query=request.query,
            answer=answer if request.use_rag else "[Direct LLM response without RAG]",
            sources=sources if request.include_sources else [],
            confidence=0.85 if chunks else 0.0,
            latency_ms=latency_ms
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/stats")
def get_stats():
    """Get system statistics."""
    if retriever is None:
        return {
            'status': 'not_ready',
            'documents': 0,
            'avg_doc_length': 0
        }
    
    return {
        'status': 'ready',
        'documents': retriever.total_docs,
        'avg_doc_length': retriever.avg_doc_length,
        'index_type': 'hybrid_bm25'
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8080)
