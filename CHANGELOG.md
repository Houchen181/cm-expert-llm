# Changelog

All notable changes to the **cm-expert-llm** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- CI status and Colab badges to README
- Docker deployment support with `Dockerfile` and `.dockerignore`
- `examples/05_continuous_arxiv.ipynb` for automated arXiv paper monitoring
- 12 recent arXiv papers (March 2026) to training corpus
  - Hubbard model thermal entropy computation
  - Honeycomb lattice antiferromagnet Co3ZnNb2O9
  - Perovskite nanocrystal heterostructures
  - Photoferroelectric coupling in van der Waals ferroelectrics
  - Ferroelectric p-wave magnets
  - Molecular tweezer array quantum simulator
  - Three-component BEC instabilities
  - Matrix Product States with modulated symmetries
  - Magnetic heterostructures LSMO/SRO

### Changed
- README.md enhanced with Docker deployment instructions
- Production-ready structure for v0.1.0 release

### Fixed
- README emoji encoding (UTF-8 compliance)
- pyproject.toml content-type specification for proper PyPI metadata

---

## [0.1.0] - 2026-03-21 (Initial Release)

### Added
- **Data Pipeline**
  - Automatic chunking with configurable size/overlap
  - Metadata extraction (source, type, char count)
  - JSONL output format for HuggingFace compatibility
  - Support for `.txt`, `.md`, `.tex` files

- **Training**
  - LoRA fine-tuning (r=32, alpha=64)
  - Optional DAPT (Domain Adaptive Pre-Training) stage
  - YAML-based configuration
  - Dry-run mode for safe validation
  - GPU detection and graceful degradation

- **Evaluation**
  - CMPhysBench benchmark (5 sample questions)
  - Grounding evaluation (hallucination detection)
  - Citation accuracy metrics
  - By-difficulty and by-topic breakdowns

- **Serving**
  - HybridRetriever (BM25 + dense placeholder)
  - Reciprocal Rank Fusion for combining rankings
  - FastAPI endpoints (`/health`, `/retrieve`, `/query`, `/stats`)
  - Interactive API docs

- **Documentation**
  - Comprehensive README with quick start guide
  - Tutorial notebooks (data ingestion, training, demo, eval report)
  - CONTRIBUTING.md with physics content guidelines
  - ROADMAP.md with development timeline
  - SECURITY.md for responsible disclosure
  - CITATION.cff for academic citations

- **Infrastructure**
  - GitHub Actions CI/CD workflows (multi-Python testing)
  - Unit test suite (30+ tests)
  - Issue templates (bug report, feature request, physics contribution, good first issue)
  - Pull request template
  - CODEOWNERS configuration
  - FUNDING.yml placeholder

### Technical Details
- **Base Model**: Mistral-7B-Instruct-v0.3 (configurable)
- **LoRA Config**: r=32, alpha=64, target_modules=[q_proj, v_proj, k_proj, o_proj]
- **Retrieval**: BM25 (k1=1.5, b=0.75, k=60) + Dense (planned)
- **Evaluation**: CMPhysBench, CMT-Benchmark compatible
- **API**: FastAPI with Pydantic models
- **Python**: 3.10+ compatible

### Known Issues
- Dense vector retrieval is a placeholder (requires sentence-transformers installation)
- Cross-encoder reranking not yet implemented
- Limited to 5 sample CMPhysBench questions (extended benchmark pending)

---

## Version History
- **v0.1.0** - 2026-03-21 - Initial release with complete RAG pipeline
