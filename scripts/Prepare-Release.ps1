# Prepare v0.1.0 Release - PowerShell Script
# Run this script to prepare all release artifacts

$VERSION = "0.1.0"
$RELEASE_DATE = Get-Date -Format "yyyy-MM-dd"

Write-Host "🚀 Preparing cm-expert-llm v${VERSION} release..." -ForegroundColor Green
Write-Host "Release date: $RELEASE_DATE"
Write-Host ""

# Step 1: Verify all tests pass
Write-Host "Step 1: Running tests..." -ForegroundColor Cyan
try {
    $testResult = python -m pytest tests/ -v --tb=short
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ All tests passed" -ForegroundColor Green
    } else {
        Write-Host "❌ Tests failed! Please fix before releasing." -ForegroundColor Red
        exit 1
    }
} catch {
    Write-Host "⚠️  Python/pytest not found, skipping tests" -ForegroundColor Yellow
}
Write-Host ""

# Step 2: Check required files
Write-Host "Step 2: Checking required files..." -ForegroundColor Cyan
$REQUIRED_FILES = @(
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "pyproject.toml",
    "requirements.txt"
)

$allPresent = $true
foreach ($file in $REQUIRED_FILES) {
    if (Test-Path $file) {
        Write-Host "  ✓ $file" -ForegroundColor Gray
    } else {
        Write-Host "  ✗ $file MISSING" -ForegroundColor Red
        $allPresent = $false
    }
}

if (-not $allPresent) {
    Write-Host "❌ Missing required files!" -ForegroundColor Red
    exit 1
}
Write-Host "✅ All required files present" -ForegroundColor Green
Write-Host ""

# Step 3: Verify version in files
Write-Host "Step 3: Verifying version consistency..." -ForegroundColor Cyan
$pyprojectContent = Get-Content "pyproject.toml" -Raw
if ($pyprojectContent -match "version = `"$VERSION`"") {
    Write-Host "✅ pyproject.toml version matches" -ForegroundColor Green
} else {
    Write-Host "⚠️  pyproject.toml version may need update" -ForegroundColor Yellow
}
Write-Host ""

# Step 4: Generate release notes
Write-Host "Step 4: Generating release notes..." -ForegroundColor Cyan
$releaseNotes = @"
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
"@

$releaseNotes | Out-File -FilePath "RELEASE_NOTES_v${VERSION}.md" -Encoding utf8
Write-Host "✅ Release notes generated: RELEASE_NOTES_v${VERSION}.md" -ForegroundColor Green
Write-Host ""

# Step 5: Create git tag command
Write-Host "Step 5: Prepare git tag command..." -ForegroundColor Cyan
Write-Host "To create the release tag, run:" -ForegroundColor Yellow
Write-Host "  git tag -a v${VERSION} -m `"cm-expert-llm v${VERSION} - Initial release`""
Write-Host "  git push origin v${VERSION}"
Write-Host ""

# Step 6: Next steps
Write-Host "==========================================" -ForegroundColor Green
Write-Host "✅ Release preparation complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Review RELEASE_NOTES_v${VERSION}.md"
Write-Host "2. Create GitHub release: https://github.com/Houchen181/cm-expert-llm/releases/new"
Write-Host "3. Tag version: git tag -a v${VERSION} -m `"cm-expert-llm v${VERSION}`""
Write-Host "4. Push tag: git push origin v${VERSION}"
Write-Host "5. Publish to PyPI (optional): twine upload dist/*"
Write-Host "6. Announce on social media!"
Write-Host ""
Write-Host "==========================================" -ForegroundColor Green
