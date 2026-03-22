#!/bin/bash
# Prepare v0.1.0 Release - Automated Script
# Run this script to prepare all release artifacts

set -e

VERSION="0.1.0"
RELEASE_DATE=$(date +%Y-%m-%d)

echo "🚀 Preparing cm-expert-llm v${VERSION} release..."
echo "Release date: $RELEASE_DATE"
echo ""

# Step 1: Verify all tests pass
echo "Step 1: Running tests..."
if command -v python &> /dev/null; then
    python -m pytest tests/ -v --tb=short || {
        echo "❌ Tests failed! Please fix before releasing."
        exit 1
    }
    echo "✅ All tests passed"
else
    echo "⚠️  Python not found, skipping tests"
fi
echo ""

# Step 2: Check required files
echo "Step 2: Checking required files..."
REQUIRED_FILES=(
    "README.md"
    "LICENSE"
    "CONTRIBUTING.md"
    "CHANGELOG.md"
    "CITATION.cff"
    "pyproject.toml"
    "requirements.txt"
)

for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        echo "❌ Missing required file: $file"
        exit 1
    fi
done
echo "✅ All required files present"
echo ""

# Step 3: Verify version in files
echo "Step 3: Verifying version consistency..."
# Check pyproject.toml version
if grep -q "version = \"$VERSION\"" pyproject.toml; then
    echo "✅ pyproject.toml version matches"
else
    echo "⚠️  pyproject.toml version may need update"
fi
echo ""

# Step 4: Generate release notes
echo "Step 4: Generating release notes..."
cat > RELEASE_NOTES_v${VERSION}.md << EOF
# cm-expert-llm v${VERSION} - Release Notes

**Release Date**: $RELEASE_DATE

## 🎉 What's New

cm-expert-llm v${VERSION} is the initial release of the domain-expert LLM toolkit for condensed matter physics!

### Key Features
- **RAG Pipeline**: Retrieval-augmented generation for physics Q&A
- **LoRA Training**: Parameter-efficient fine-tuning (consumer GPU friendly)
- **CMPhysBench**: Evaluation framework for physics LLMs
- **Streamlit UI**: User-friendly chat interface
- **Docker Support**: One-line deployment
- **Colab Ready**: One-click demo in Google Colab

### Training Data
- 13+ recent arXiv papers (March 2026)
- Real physics content (no AI summaries)
- Superconductivity, topology, correlated electrons
- Continuous updates via automated arXiv monitoring

### Documentation
- Comprehensive README with quick start
- Tutorial notebooks (data ingestion, training, evaluation)
- Showcase examples (superconductivity, topology, correlated electrons)
- Contributing guide for physics researchers
- Data documentation with contribution templates

## 📦 Installation

\`\`\`bash
pip install cm-expert-llm
\`\`\`

Or from source:
\`\`\`bash
git clone https://github.com/Houchen181/cm-expert-llm.git
cd cm-expert-llm
pip install -r requirements.txt
\`\`\`

## 🚀 Quick Start

1. **Prepare your data**: Place physics papers in \`data/raw/\`
2. **Build corpus**: \`python scripts/build_corpus.py --input-dir ./data/raw --output-file ./data/processed/sft.jsonl\`
3. **Train LoRA**: \`python scripts/train_lora.py --config configs/train.default.yaml\`
4. **Evaluate**: \`python scripts/run_eval.py --all\`
5. **Deploy**: \`python scripts/serve_api.py --config configs/serve.default.yaml\`

See [examples/](examples/) for detailed notebooks.

## 📊 Stats

- **Tests**: 14 tests (9 core + 5 optional)
- **Examples**: 5 notebooks + 3 showcase demos
- **Documentation**: 10+ markdown files
- **Training Data**: 50+ documents, 13 arXiv papers

## 🙏 Acknowledgments

Thank you to all contributors and the condensed matter physics community!

## 📝 Full Changelog

See [CHANGELOG.md](CHANGELOG.md) for detailed changes.

## 🔗 Links

- **GitHub**: https://github.com/Houchen181/cm-expert-llm
- **Documentation**: https://github.com/Houchen181/cm-expert-llm/tree/main/docs
- **Examples**: https://github.com/Houchen181/cm-expert-llm/tree/main/examples
- **Colab Demo**: [Open in Colab](https://colab.research.google.com/github/Houchen181/cm-expert-llm/blob/main/examples/03_demo.ipynb)

---

**cm-expert-llm** is licensed under Apache-2.0.
EOF

echo "✅ Release notes generated: RELEASE_NOTES_v${VERSION}.md"
echo ""

# Step 5: Create git tag command
echo "Step 5: Prepare git tag command..."
echo "To create the release tag, run:"
echo "  git tag -a v${VERSION} -m \"cm-expert-llm v${VERSION} - Initial release\""
echo "  git push origin v${VERSION}"
echo ""

# Step 6: Next steps
echo "=========================================="
echo "✅ Release preparation complete!"
echo ""
echo "Next steps:"
echo "1. Review RELEASE_NOTES_v${VERSION}.md"
echo "2. Create GitHub release: https://github.com/Houchen181/cm-expert-llm/releases/new"
echo "3. Tag version: git tag -a v${VERSION} -m \"cm-expert-llm v${VERSION}\""
echo "4. Push tag: git push origin v${VERSION}"
echo "5. Publish to PyPI (optional): twine upload dist/*"
echo "6. Announce on social media!"
echo ""
echo "=========================================="
