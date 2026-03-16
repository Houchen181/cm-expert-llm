# Quick Start Guide - CondensAI

Get your condensed matter physics expert LLM running in 5 minutes!

## Prerequisites

- Python 3.10+
- 8GB+ RAM (16GB recommended)
- Optional: GPU with CUDA for training

## Installation

```bash
# Clone the repository
git clone https://github.com/Houchen181/CondensAI.git
cd CondensAI

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Step 1: Prepare Your Data

Place your condensed matter physics documents in `data/raw/`:
- Research papers (arXiv cond-mat)
- Textbook chapters
- Lecture notes
- Any domain-specific text

Supported formats: `.txt`, `.md`, `.tex`

```bash
# Example: Add a sample paper
echo "# Superconductivity Notes\n\nThe Meissner effect..." > data/raw/superconductivity.md
```

## Step 2: Build the Corpus

```bash
python scripts/build_corpus.py --input-dir ./data/raw --output-file ./data/processed/sft.jsonl
```

This will:
- Chunk documents into 800-word segments
- Extract metadata
- Create JSONL format for training

## Step 3: Train Your Model

### Option A: Quick LoRA Fine-tuning (Recommended)

```bash
python scripts/train_lora.py --config configs/train.default.yaml
```

### Option B: With Domain-Adaptive Pretraining

Edit `configs/train.default.yaml`:
```yaml
dapt:
  enabled: true
  data_file: ./data/processed/dapt_corpus.jsonl
  epochs: 1
```

Then run training as above.

## Step 4: Evaluate

Run benchmark evaluations:

```bash
# Run all evaluations
python scripts/run_eval.py --all

# Or run specific benchmarks
python scripts/run_eval.py --benchmark  # CMPhysBench
python scripts/run_eval.py --grounding  # Grounding metrics
```

## Step 5: Deploy RAG API

Start the RAG serving layer:

```bash
python scripts/serve_api.py --config configs/serve.default.yaml
```

The API will be available at `http://localhost:8080`

### Test the API

```bash
# Health check
curl http://localhost:8080/health

# Retrieve relevant chunks
curl -X POST http://localhost:8080/retrieve \
  -H "Content-Type: application/json" \
  -d '{"query": "What is the Meissner effect?", "top_k": 5}'

# Query with RAG
curl -X POST http://localhost:8080/query \
  -H "Content-Type: application/json" \
  -d '{"query": "Explain superconductivity", "top_k": 5}'
```

## Project Structure

```
CondensAI/
├── src/cmp_expert/
�?  ├── data/          # Data ingestion pipeline
�?  ├── training/      # LoRA training scripts
�?  ├── eval/          # Benchmark evaluations
�?  └── serve/         # RAG API serving
├── configs/           # YAML configurations
├── scripts/           # Command-line tools
├── data/
�?  ├── raw/          # Input documents
�?  └── processed/    # Processed JSONL files
├── examples/          # Jupyter notebooks
└── docs/             # Documentation
```

## Configuration

### Training Config (`configs/train.default.yaml`)

```yaml
base_model: mistralai/Mistral-7B-Instruct-v0.3
lora:
  r: 32              # LoRA rank
  alpha: 64          # Scaling factor
  target_modules: ["q_proj", "v_proj"]
training:
  epochs: 3
  lr: 2e-4
  batch_size: 2
```

### Serving Config (`configs/serve.default.yaml`)

```yaml
host: 0.0.0.0
port: 8080
retriever:
  k1: 1.5            # BM25 parameter
  b: 0.75            # BM25 parameter
  k: 60              # RRF constant
```

## Common Tasks

### Add More Training Data

```bash
# Add new documents to data/raw/
echo "New physics content..." >> data/raw/new_topic.md

# Rebuild corpus
python scripts/build_corpus.py
```

### Customize Chunking

```bash
python scripts/build_corpus.py \
  --chunk-size 1000 \
  --overlap 150
```

### Run Specific Benchmark

```bash
# CMPhysBench only
python scripts/run_eval.py --benchmark --benchmark-file ./custom_bench.jsonl
```

## Troubleshooting

### Out of Memory During Training

Reduce batch size in config:
```yaml
training:
  batch_size: 1
  grad_accum: 32  # Increase to compensate
```

### Poor Retrieval Results

1. Increase corpus size (more domain documents)
2. Adjust chunk overlap:
```bash
python scripts/build_corpus.py --overlap 200
```

### API Not Starting

Check if port 8080 is in use:
```bash
# Windows
netstat -ano | findstr :8080

# Change port in serve.default.yaml if needed
```

## Next Steps

- 📚 Read the [Architecture Guide](architecture.md)
- 📊 Explore [Benchmark Results](results/)
- 🔧 Customize for your domain
- 🤝 Contribute improvements

## Getting Help

- Issues: https://github.com/Houchen181/CondensAI/issues
- Documentation: https://github.com/Houchen181/CondensAI/tree/main/docs
- Examples: https://github.com/Houchen181/CondensAI/tree/main/examples
