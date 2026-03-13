# Architecture (v0 scaffold)

1. Data Ingestion: parse papers/textbooks/reviewer notes -> normalized JSONL
2. Training: instruction SFT + LoRA adaptation
3. Retrieval: hybrid BM25 + dense + reranker
4. Serving: FastAPI endpoint with citation-ready responses
5. Evaluation: benchmark accuracy + grounding/faithfulness metrics
