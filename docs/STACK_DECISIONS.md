# Stack Decisions - cm-expert-llm (cm-expert-llm)

This document explains the technology choices behind cm-expert-llm's architecture. These decisions balance performance, accessibility, and research credibility.

## Core Philosophy

**Narrow and deep > Broad and shallow**

cm-expert-llm focuses exclusively on condensed matter physics, enabling it to outperform general LLMs in this domain by:
- Training on primary sources (papers, textbooks) only
- Providing citations to original literature
- Using RAG (Retrieval-Augmented Generation) for factual grounding
- Supporting community validation and corrections

## Training Stack

### Base Framework: Hugging Face Transformers + PEFT

**Why:**
- Industry standard for LLM fine-tuning
- Extensive documentation and community support
- Compatible with most open-source LLMs (Llama, Mistral, Qwen, etc.)
- No vendor lock-in

**Implementation:**
- `transformers` library for model loading
- `peft` for Parameter-Efficient Fine-Tuning (LoRA)
- `accelerate` for multi-GPU support

### Fine-tuning Method: LoRA (Low-Rank Adaptation)

**Why:**
- **Memory efficient**: Only trains 0.1-1% of parameters
- **Consumer GPU friendly**: Works on RTX 3090/4090 (24GB)
- **Fast iteration**: Training completes in hours, not weeks
- **Modular**: Multiple domain adapters can be swapped

**Configuration:**
```yaml
lora_config:
  r: 16              # Rank of LoRA update matrices
  alpha: 32          # LoRA scaling factor
  dropout: 0.05      # Dropout for regularization
  target_modules:    # Layers to adapt (model-specific)
    - q_proj
    - v_proj
    - k_proj
    - o_proj
```

### Quantization: 4-bit (NF4)

**Why:**
- Enables training on consumer GPUs
- Minimal quality loss for domain tasks
- Compatible with LoRA via QLoRA technique

**Implementation:**
- `bitsandbytes` for 4-bit quantization
- NF4 (Normal Float 4) format for optimal precision

## Inference Stack

### Serving: vLLM

**Why:**
- **PagedAttention**: 2-4x throughput vs. naive serving
- **Continuous batching**: Handle variable-length requests efficiently
- **OpenAI-compatible API**: Drop-in replacement for OpenAI client
- **Multi-GPU support**: Tensor parallelism for large models

**Key Features:**
- OpenAI-compatible REST API
- Streaming responses
- Parallel sampling (useful for uncertainty estimation)
- Prefix caching (efficient for repeated queries)

**Alternatives Considered:**
- `text-generation-inference` (HuggingFace): Good, but less throughput
- `llama.cpp`: Great for CPU, but limited GPU optimization
- `TGI`: Solid choice, but vLLM has better community momentum

## Retrieval Stack

### Embedding Model: sentence-transformers

**Why:**
- Purpose-built for semantic similarity
- Fast inference on CPU/GPU
- Compatible with scikit-learn APIs

**Configuration:**
- Model: `all-MPNet-base-v2` or `bge-large-en`
- Dimension: 768 or 1024
- Normalization: L2 (cosine similarity)

### Vector Store: FAISS (optional)

**Why:**
- Fast approximate nearest neighbor search
- Scales to millions of vectors
- Supports GPU acceleration

**For small datasets (<10k docs):**
- Simple cosine similarity with numpy is sufficient
- No need for FAISS overhead

### Reranking: Cross-Encoder (optional)

**Why:**
- Improves retrieval precision by 10-20%
- Captures query-document interaction

**Implementation:**
- `cross-encoder/ms-marco-MiniLM-L-6-v2`
- Rerank top-50 results to top-5

## Evaluation

### Benchmark: CMPhysBench (custom)

**Components:**
1. **Factual accuracy**: Multiple-choice questions from textbooks
2. **Citation grounding**: Does the model cite sources correctly?
3. **Reasoning**: Multi-step physics problems
4. **Uncertainty calibration**: Does the model know what it doesn't know?

**Metrics:**
- Accuracy (%)
- Citation precision/recall
- Expected Calibration Error (ECE)

## Deployment

### Local Deployment (Recommended for researchers)

```bash
# Install
pip install -r requirements.txt

# Run API server
python scripts/serve_api.py --config configs/serve.default.yaml

# Query
curl http://localhost:8000/query?question="What is the Meissner effect?"
```

### Cloud Deployment

**Options:**
- **RunPod / Lambda Labs**: $0.50-1.00/hr for RTX 4090
- **HuggingFace Spaces**: Free tier for demo, paid for production
- **AWS SageMaker**: Enterprise-grade, higher cost

### Docker (Future)

```dockerfile
FROM nvidia/cuda:12.1-runtime-ubuntu22.04
# ... (to be added)
```

## Why This Stack Wins in Condensed Matter Physics

### 1. Primary Source Training
General LLMs are trained on web data (Wikipedia, forums, etc.) which often contains:
- Outdated information
- Hand-wavy explanations
- No citations to original papers

cm-expert-llm trains on:
- arXiv papers (cond-mat)
- Standard textbooks (Ashcroft/Mermin, Kittel, etc.)
- Lecture notes from reputable sources

### 2. Citation Grounding
Every answer includes references to:
- Original paper DOIs
- Textbook chapters
- Specific equations/figures

This enables physicists to:
- Verify claims quickly
- Trace concepts to first principles
- Build on established knowledge

### 3. Community Validation
Unlike closed models (GPT-4, Claude), cm-expert-llm is:
- Open-source (code + weights)
- Auditable (see exactly what it was trained on)
- Correctable (submit PRs to fix errors)

### 4. Narrow Scope Advantage
By focusing only on condensed matter physics:
- Training data is curated, not scraped
- Evaluation is domain-specific
- Performance can exceed general models in this niche

## Roadmap

### Short-term (Q2 2026)
- [ ] Dense vector retrieval (sentence-transformers)
- [ ] Cross-encoder reranking
- [ ] UI frontend (Streamlit/Gradio)
- [ ] Docker deployment

### Mid-term (Q3-Q4 2026)
- [ ] Extended CMPhysBench questions (1000+)
- [ ] Continuous arXiv monitoring (auto-ingest new papers)
- [ ] Multi-model ensemble (Llama + Mistral + Qwen)

### Long-term (2027+)
- [ ] Full pretraining (not just fine-tuning) on CM corpus
- [ ] Interactive derivation checking
- [ ] Integration with computational tools (DFT, Monte Carlo)

---

*Last updated: 2026-03-18*
*Contributors: oc (for hc)*
