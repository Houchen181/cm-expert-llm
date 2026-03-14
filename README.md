# CM-Expert-LLM

<div align="center">
  <img src="docs/logo.svg" alt="CM-Expert-LLM Logo" width="200"/>
  <br>
  <strong>Build Domain-Expert LLMs for Condensed Matter Physics</strong>
</div>

<p align="center">
  <a href="https://github.com/Houchen181/cm-expert-llm/stargazers"><img alt="GitHub Stars" src="https://img.shields.io/github/stars/Houchen181/cm-expert-llm?style=flat"/></a>
  <a href="https://github.com/Houchen181/cm-expert-llm/issues"><img alt="Issues" src="https://img.shields.io/github/issues/Houchen181/cm-expert-llm"/></a>
  <a href="https://github.com/Houchen181/cm-expert-llm/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/Houchen181/cm-expert-llm"/></a>
  <a href="https://arxiv.org/abs/2508.18124"><img alt="CMPhysBench" src="https://img.shields.io/badge/CMPhysBench-evaluation-blue"/></a>
</p>

**CM-Expert-LLM** is an open-source toolkit for building and deploying **domain-expert LLM assistants** specialized in condensed matter physics. Turn your research papers, textbooks, and notes into an intelligent, retrieval-augmented Q&A system.

## 🌟 Features

- 📚 **Data Pipeline**: Automatically chunk and process physics documents (papers, textbooks, notes)
- 🎯 **LoRA Fine-tuning**: Parameter-efficient domain adaptation with DAPT support
- 🔍 **Hybrid RAG**: BM25 + dense retrieval with Reciprocal Rank Fusion
- 📊 **Benchmark Evaluation**: CMPhysBench & CMT-Benchmark compatible
- 🛡️ **Grounding Checks**: Detect hallucinations and verify citations
- 🚀 **FastAPI Serving**: Production-ready API with health checks & metrics

## 📖 Quick Start

### 1. Install

```bash
git clone https://github.com/Houchen181/cm-expert-llm.git
cd cm-expert-llm
pip install -r requirements.txt
```

### 2. Prepare Your Data

Place condensed matter physics documents in `data/raw/`:
- arXiv papers (cond-mat)
- Textbook chapters
- Lecture notes
- Research summaries

```bash
# Example: Add a sample file
echo "# Superconductivity\n\nThe Meissner effect..." > data/raw/superconductivity.md
```

### 3. Build Corpus

```bash
python scripts/build_corpus.py --input-dir ./data/raw --output-file ./data/processed/sft.jsonl
```

### 4. Train LoRA Adapter

```bash
python scripts/train_lora.py --config configs/train.default.yaml
```

### 5. Evaluate

```bash
python scripts/run_eval.py --all
```

### 6. Deploy RAG API

```bash
python scripts/serve_api.py --config configs/serve.default.yaml
```

Access the API at `http://localhost:8080/docs`

## 📚 Tutorials

### Tutorial 1: Data Ingestion
See [`examples/01_data_ingestion.ipynb`](examples/01_data_ingestion.ipynb) for an interactive guide.

### Tutorial 2: Training
See [`examples/02_training.ipynb`](examples/02_training.ipynb) for LoRA fine-tuning.

### Tutorial 3: Evaluation
Run benchmarks with `scripts/run_eval.py --benchmark`

### Tutorial 4: RAG Deployment
Start the API and test endpoints at `/docs`

## 🏗️ Project Structure

```
cm-expert-llm/
├── src/cmp_expert/
│   ├── data/          # Data ingestion pipeline
│   ├── training/      # LoRA training with DAPT
│   ├── eval/          # CMPhysBench + Grounding
│   └── serve/         # RAG API (FastAPI)
├── configs/           # YAML configurations
├── scripts/           # CLI tools
├── data/
│   ├── raw/          # Input documents
│   └── processed/    # JSONL corpus
├── examples/          # Jupyter notebooks
├── docs/              # Documentation + logo
└── tests/             # Unit tests
```

## 📊 Benchmarks

CM-Expert-LLM is evaluated on:
- **CMPhysBench**: Condensed matter physics problems
- **CMT-Benchmark**: Theory understanding
- **Grounding Metrics**: Hallucination detection

See [`docs/architecture.md`](docs/architecture.md) for detailed metrics.

## 🔧 Configuration

### Training Config (`configs/train.default.yaml`)

```yaml
base_model: mistralai/Mistral-7B-Instruct-v0.3
dapt:
  enabled: true  # Domain-Adaptive Pretraining
  epochs: 1
lora:
  r: 32
  alpha: 64
  target_modules: ["q_proj", "v_proj", "k_proj", "o_proj"]
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
  k1: 1.5  # BM25
  b: 0.75
  k: 60    # RRF
```

## 📦 Example Usage

### Query the RAG API

```bash
curl -X POST http://localhost:8080/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is the Meissner effect?", "top_k": 5}'
```

### Run Custom Benchmark

```bash
python scripts/run_eval.py --benchmark --benchmark-file ./custom_bench.jsonl
```

## 🎓 Research Basis

This project implements best practices from 2025-2026:
- **Hybrid RAG**: BM25 + dense retrieval + reranking
- **LoRA/QLoRA**: Parameter-efficient fine-tuning
- **DAPT**: Domain-Adaptive Pretraining for scientific domains
- **CMPhysBench**: Condensed matter physics benchmark

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Submit a pull request

## 📄 License

Apache-2.0

## 🙏 Acknowledgments

- CMPhysBench team for the benchmark
- HuggingFace for transformers/peft/trl
- FastAPI team for the web framework

## 📬 Contact

- Issues: https://github.com/Houchen181/cm-expert-llm/issues
- Discussions: https://github.com/Houchen181/cm-expert-llm/discussions

---

<div align="center">
  <strong>CM-Expert-LLM</strong> - Building domain experts for condensed matter physics
</div>
