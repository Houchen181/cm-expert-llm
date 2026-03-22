# Examples - cm-expert-llm

This directory contains practical examples demonstrating how to use cm-expert-llm for various condensed matter physics tasks.

## 📚 Tutorial Notebooks

### Beginner Level
1. **[01_data_ingestion.ipynb](01_data_ingestion.ipynb)** - Learn how to prepare and ingest physics data
   - Text chunking and preprocessing
   - Metadata extraction
   - JSONL format conversion

2. **[02_training.ipynb](02_training.ipynb)** - Introduction to LoRA fine-tuning
   - Configuration setup
   - Training pipeline walkthrough
   - Dry-run mode for validation

3. **[03_demo.ipynb](03_demo.ipynb)** - Quick start demo (Colab-ready)
   - One-click Google Colab deployment
   - Basic Q&A with citations
   - Perfect for first-time users

### Intermediate Level
4. **[04_eval_report_template.ipynb](04_eval_report_template.ipynb)** - Generate evaluation reports
   - CMPhysBench benchmark execution
   - Accuracy and citation metrics
   - Visualization and export

5. **[05_continuous_arxiv.ipynb](05_continuous_arxiv.ipynb)** - Automated arXiv monitoring
   - Fetch latest papers automatically
   - Parse and categorize by subfield
   - Update training corpus

## 💻 Python Scripts

### **[05_streamlit_ui.py](05_streamlit_ui.py)** - Interactive Chat Interface
Deploy a user-friendly chat interface for non-technical users:
```bash
streamlit run examples/05_streamlit_ui.py
```

Features:
- Chat-based Q&A with citations
- Confidence scores
- Conversation history
- Model configuration

## 🎯 Showcase Examples

The **[showcase/](showcase/)** directory contains real-world physics examples:

- **Superconductivity Demo** - BCS theory, Meissner effect, critical temperature
- **Topological Insulators Demo** - Z2 invariants, surface states, Weyl semimetals
- **Correlated Electrons Demo** - Hubbard model, Mott transition, quantum spin liquids

Run all showcase examples:
```bash
python examples/showcase/run_all.py
```

## 🚀 Quick Start

**New to cm-expert-llm?** Start here:
1. Open [03_demo.ipynb](03_demo.ipynb) in Google Colab (click "Open In Colab" badge in README)
2. Run through the notebook step-by-step
3. Try modifying the questions to test your own physics knowledge

**Ready to build your own expert LLM?**
1. Follow [01_data_ingestion.ipynb](01_data_ingestion.ipynb) to prepare your data
2. Use [02_training.ipynb](02_training.ipynb) to train your model
3. Deploy with [05_streamlit_ui.py](05_streamlit_ui.py)

## 📊 Evaluation

To reproduce benchmark results:
```bash
# Run evaluation
python scripts/run_eval.py --all

# Generate report
python examples/04_eval_report_template.ipynb
```

## 🔧 Requirements

All examples require:
```bash
pip install -r ../requirements.txt
```

For Streamlit UI:
```bash
pip install streamlit
```

## 💡 Tips

- **Dry-run mode**: Set `DRY_RUN=1` before training to validate config without using GPU
- **Colab**: Examples 01-04 work great in Google Colab (free GPU available)
- **Custom data**: Replace `data/raw/` with your own physics papers and notes

## 🤝 Contributing Examples

Have a cool use case? Contribute it! See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

Ideal example contributions:
- New physics subfields (magnetism, optics, etc.)
- Educational use cases (homework helper, exam prep)
- Research workflows (paper summarization, citation search)
- Integration with other tools (Jupyter, VS Code, etc.)

---

**Need Help?** Open an issue or start a discussion on [GitHub](https://github.com/Houchen181/cm-expert-llm).
