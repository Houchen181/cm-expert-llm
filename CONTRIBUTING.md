# Contributing to CondensAI

Thank you for your interest in contributing! This project aims to build domain-expert LLMs for condensed matter physics, and we welcome contributions from physicists, ML engineers, educators, and enthusiasts.

## 🎯 Where You Can Contribute

- **Physics Content**: Add paper summaries, textbook notes, or lecture materials
- **Code**: Improve training pipelines, retrieval, or evaluation
- **Documentation**: Fix typos, add examples, improve clarity
- **Testing**: Add test cases, especially for edge cases
- **Community**: Help others in discussions, report bugs, suggest features

## 📋 Quick Start

1. **Fork** the repository
2. **Clone** your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/CondensAI.git
   cd CondensAI
   ```
3. **Set up environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   pip install -e .
   ```
4. **Create a branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 🔧 Development Workflow

### For Code Contributions

1. **Make changes** with clear commit messages
2. **Run tests**:
   ```bash
   python -m pytest tests/ -v
   ```
3. **Check code style**:
   ```bash
   flake8 src/ scripts/
   ```
4. **Test training** (dry-run mode):
   ```bash
   DRY_RUN=1 python scripts/train_lora.py --config configs/train.default.yaml
   ```
5. **Push and create PR**

### For Physics Content

1. **Add files** to `data/raw/<domain>/`:
   - Use Markdown format
   - Include proper citations
   - No AI summaries — use original sources only
2. **Verify format**:
   ```bash
   python scripts/build_corpus.py --input-dir ./data/raw --output-file ./data/processed/test.jsonl
   ```
3. **Submit PR** with physics-content label

## 📝 Commit Message Guidelines

Follow conventional commits:

```
feat: add cross-encoder reranking
fix: handle empty retrieval results gracefully
docs: update QUICKSTART with Windows instructions
test: add unit tests for data pipeline
physics: add BCS theory notes from textbook ch.3
```

## 🧪 Testing

### Running Tests
```bash
# All tests
python -m pytest tests/ -v

# With coverage
python -m pytest tests/ -v --cov=src/cmp_expert --cov-report=html

# Specific test file
python -m pytest tests/test_pipeline.py -v
```

### Testing Training Pipeline
```bash
# Dry run (safe, no actual training)
DRY_RUN=1 python scripts/train_lora.py --config configs/train.default.yaml

# Full test (if you have GPU)
python scripts/train_lora.py --config configs/train.default.yaml --epochs 1
```

### Testing Retrieval
```bash
python scripts/serve_api.py --config configs/serve.default.yaml
# Then query the API
curl http://localhost:8000/query?question="What is the Meissner effect?"
```

## 📚 Code Style

- **PEP 8**: Follow Python style guidelines
- **Type hints**: Use them for function signatures
- **Docstrings**: Google-style for all public functions
- **Line length**: Max 100 characters (127 for tests)
- **Imports**: Grouped (stdlib, third-party, local)

Example:
```python
from typing import List, Dict, Optional
import numpy as np

from cmp_expert.data import CorpusBuilder


def build_corpus(
    input_dir: str,
    output_file: str,
    max_length: int = 512
) -> Dict[str, int]:
    """Build a corpus from raw physics documents.
    
    Args:
        input_dir: Directory containing raw markdown files
        output_file: Path to output JSONL file
        max_length: Maximum sequence length
        
    Returns:
        Dictionary with corpus statistics
    """
    # Implementation here
    pass
```

## 🏷️ Pull Request Process

1. **Ensure CI passes**: All tests and linting must pass
2. **Update documentation**: README, docs/, or docstrings as needed
3. **Add tests**: For new features or bug fixes
4. **Request review**: Tag relevant maintainers
5. **Address feedback**: Respond to review comments
6. **Squash commits**: If needed, before merging

## 🎓 Physics Content Guidelines

If contributing physics content (papers, notes, etc.):

### Quality Standards
- ✅ **Primary sources only**: No AI-generated summaries
- ✅ **Accurate**: Content must be technically correct
- ✅ **Cited**: Include DOI, arXiv ID, or textbook reference
- ✅ **Clear**: Well-organized, readable structure

### Format
```markdown
# Topic Name

## Source
- Paper: [Title](arXiv link or DOI)
- Authors: Name et al.
- Year: 2024

## Summary
Clear, concise explanation of the physics.

## Key Equations
If applicable, include with proper LaTeX formatting.

## Key Concepts
- Concept 1: Brief explanation
- Concept 2: Brief explanation

## Related Topics
- Link to related topics in the repo
```

## 💬 Getting Help

- **Discussions**: Use GitHub Discussions for questions
- **Issues**: Report bugs or request features
- **Discord**: Join our community server (link in README)

## 🎉 Recognition

Contributors will be:
- Listed in README.md contributors section
- Mentioned in release notes
- Tagged in relevant announcements
- Added as code owners for their contributions

## ❓ Questions?

Open an issue or start a discussion for any questions about contributing. We're happy to help!

---

Thanks for contributing to CondensAI! 🚀
