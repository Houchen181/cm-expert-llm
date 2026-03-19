# CondensAI Project Roadmap

This document outlines the development roadmap for CondensAI (cm-expert-llm), a domain-expert LLM toolkit for condensed matter physics.

## Vision

Enable physicists to deploy custom LLM assistants trained on their research papers, textbooks, and lecture notes—without requiring ML expertise.

## Status: Pre-Alpha (v0.1.0)

**Current Focus**: Core functionality and documentation

---

## Q2 2026 (April - June)

### ✅ Completed (March 2026)
- [x] Core RAG pipeline (data ingestion, retrieval, generation)
- [x] LoRA fine-tuning support
- [x] Basic evaluation framework (CMPhysBench)
- [x] Documentation (STACK_DECISIONS, BENCHMARK_PROTOCOL)
- [x] CI/CD setup with GitHub Actions
- [x] Community templates (issues, PR templates)
- [x] Streamlit UI example
- [x] Colab-ready demo notebook

### 🔄 In Progress
- [ ] **v0.1.0 Release** (Target: April 15, 2026)
  - [ ] Stable API for data pipeline
  - [ ] Basic training script with LoRA
  - [ ] Evaluation script with CMPhysBench
  - [ ] Documentation website (MkDocs)
  - [ ] Tutorial: "10-minute physics expert"

### 📋 Planned
- [ ] **Dense Retrieval** (sentence-transformers integration)
  - [ ] Add `sentence-transformers` dependency
  - [ ] Implement dense embedding pipeline
  - [ ] Hybrid retrieval (BM25 + dense)
  - [ ] Benchmark dense vs. sparse retrieval

- [ ] **Cross-Encoder Reranking**
  - [ ] Add `cross-encoder` dependency
  - [ ] Rerank top-50 → top-5 results
  - [ ] Evaluate impact on CMPhysBench

- [ ] **UI Improvements**
  - [ ] Streamlit app deployment guide
  - [ ] Gradio alternative example
  - [ ] Docker deployment for UI

---

## Q3 2026 (July - September)

### 🎯 v0.2.0 Release (Target: August 1, 2026)
- [ ] **Multi-Model Support**
  - [ ] Llama 3.x fine-tuning
  - [ ] Mistral fine-tuning
  - [ ] Qwen fine-tuning
  - [ ] Model comparison benchmarks

- [ ] **Advanced RAG**
  - [ ] Multi-hop retrieval
  - [ ] Query expansion
  - [ ] Citation-aware retrieval

- [ ] **Evaluation Enhancements**
  - [ ] Extended CMPhysBench (1000+ questions)
  - [ ] Leaderboard website
  - [ ] Community submission system

### 📋 Planned
- [ ] **Docker Deployment**
  - [ ] Dockerfile for API server
  - [ ] Docker Compose for full stack
  - [ ] Kubernetes manifests (experimental)

- [ ] **Continuous ArXiv Monitoring**
  - [ ] Daily arXiv scrape (cond-mat)
  - [ ] Auto-ingest new papers
  - [ ] Incremental corpus updates

---

## Q4 2026 (October - December)

### 🎯 v0.3.0 Release (Target: November 15, 2026)
- [ ] **Full Pretraining** (not just fine-tuning)
  - [ ] Curate CM corpus (10GB+ text)
  - [ ] Pretrain from scratch (or continue from base)
  - [ ] Compare pretrained vs. fine-tuned performance

- [ ] **Interactive Derivation Checking**
  - [ ] Step-by-step equation verification
  - [ ] Symbolic math integration (SymPy)
  - [ ] Physics unit checking

- [ ] **Integration with Computational Tools**
  - [ ] DFT calculation helpers
  - [ ] Monte Carlo simulation templates
  - [ ] Data visualization tools

### 📋 Planned
- [ ] **Mobile App** (React Native / Flutter)
  - [ ] iOS app
  - [ ] Android app
  - [ ] Offline mode

---

## 2027+ (Long-term)

### Vision Goals
- [ ] **1k Stars on GitHub** (Target: June 2027)
- [ ] **100+ Active Users** (researchers deploying their own experts)
- [ ] **Peer-Reviewed Publication** (describing the approach and benchmarks)
- [ ] **Community Contributions** > 50% of commits
- [ ] **Multi-Language Support** (Chinese, Spanish, etc.)

### Research Directions
- [ ] **Neuro-Symbolic Integration**: Combine LLM reasoning with symbolic physics engines
- [ ] **Multimodal Physics**: Include figures, equations, and diagrams in training
- [ ] **Active Learning**: Model requests clarification when uncertain
- [ ] **Collaborative Editing**: Multiple researchers refine the same expert together

---

## How to Contribute

We welcome contributions at all levels! See:
- **Good First Issues**: https://github.com/Houchen181/cm-expert-llm/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22
- **Contributing Guide**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **Discussions**: https://github.com/Houchen181/cm-expert-llm/discussions

### Priority Areas for Contributions
1. **Physics Content**: Add paper summaries, textbook notes, problem sets
2. **Testing**: Add test cases, especially edge cases
3. **Documentation**: Improve clarity, add tutorials, fix typos
4. **UI/UX**: Improve Streamlit/Gradio interfaces
5. **Benchmarks**: Add new evaluation questions or datasets

---

## Version History

| Version | Release Date | Key Features |
|---------|-------------|--------------|
| v0.1.0 | 2026-04-15 (planned) | Core RAG, LoRA training, CMPhysBench |
| v0.0.1 | 2026-03-18 | Initial release |

---

*Last updated: 2026-03-18*

*This roadmap is a living document and will be updated as the project evolves. Suggestions welcome via GitHub Issues or Discussions.*
