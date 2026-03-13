# CM-Expert-LLM

Open-source toolkit for building and deploying **domain-expert LLM assistants for condensed matter physics** from user-provided corpora (papers, textbooks, reviewer comments, notes).

## Goals
- Reproducible domain adaptation pipeline for CMP
- Easy local deployment (API + UI-ready backend)
- Retrieval-first design to reduce hallucinations
- Transparent evaluation on CMP benchmarks

## Project Structure
- `src/cmp_expert/data`: ingestion, parsing, chunking, metadata
- `src/cmp_expert/training`: SFT/LoRA config + training orchestration
- `src/cmp_expert/eval`: benchmark + faithfulness checks
- `src/cmp_expert/serve`: inference + RAG serving wrappers
- `configs`: YAML configs for data/training/eval/serve
- `scripts`: one-command workflows
- `docs`: architecture and usage guides

## Quickstart
```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

python scripts/build_corpus.py --config configs/data.default.yaml
python scripts/train_lora.py --config configs/train.default.yaml
python scripts/run_eval.py --config configs/eval.default.yaml
python scripts/serve_api.py --config configs/serve.default.yaml
```

## Initial Research Signals (2025–2026)
- **Benchmarks:** CMPhysBench, CMT-Benchmark for CMP-specific evaluation
- **Architecture:** Hybrid RAG + LoRA fine-tuning is the 2025-2026 best practice for scientific domains
- **Key Methods:** 
  - Parameter-Efficient Fine-Tuning (LoRA/QLoRA) for domain adaptation
  - Domain-Adaptive Pretraining (DAPT) before SFT for better convergence
  - Multi-stage retrieval with reranking for long-context scientific QA
- **Recommended Base Models (2026):** DeepSeek-R1, Qwen3-235B-A22B, Mistral-7B-Instruct

## License
Apache-2.0
