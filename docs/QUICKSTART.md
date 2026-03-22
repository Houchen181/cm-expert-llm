# 5-Minute Quick Start Guide

**Goal**: Get cm-expert-llm running and answer your first physics question in 5 minutes.

## ⚡ Prerequisites (1 min)

- Python 3.10+ installed
- Git installed
- Basic command line knowledge

**Already have these?** Skip to Step 1.

## Step 1: Install (1 min)

```bash
# Clone the repository
git clone https://github.com/Houchen181/cm-expert-llm.git
cd cm-expert-llm

# Install dependencies
pip install -r requirements.txt
```

**Windows users:** Use PowerShell or Command Prompt.

## Step 2: Verify Installation (30 sec)

```bash
# Run tests to verify everything works
python -m pytest tests/ -v
```

You should see: `9 passed, 5 skipped`

✅ **Success?** Great! Move to Step 3.  
❌ **Errors?** Check [INSTALL.md](INSTALL.md) for troubleshooting.

## Step 3: Try the Demo (2 min)

### Option A: Google Colab (Easiest - No setup!)
Click here: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Houchen181/cm-expert-llm/blob/main/examples/03_demo.ipynb)

### Option B: Run Locally
```bash
# Open the demo notebook
jupyter notebook examples/03_demo.ipynb

# Or run the demo script
python examples/showcase/run_all.py
```

## Step 4: Ask Your First Question (1 min)

```bash
# Start the API server
python scripts/serve_api.py --config configs/serve.default.yaml

# Then in another terminal, ask a question:
curl http://localhost:8000/query -d '{"question": "What is the Meissner effect?"}'
```

**Expected output**: An answer about superconductivity with citations!

## 🎉 Congratulations!

You've successfully:
- ✅ Installed cm-expert-llm
- ✅ Verified the installation
- ✅ Run the demo
- ✅ Asked your first physics question

## 🚀 What's Next?

### Path 1: Build Your Own Physics Expert
1. **Prepare your data**: Collect physics papers/textbooks
2. **Build corpus**: `python scripts/build_corpus.py --input-dir ./data/raw --output-file ./data/processed/sft.jsonl`
3. **Train LoRA**: `python scripts/train_lora.py --config configs/train.default.yaml`
4. **Deploy**: `python scripts/serve_api.py --config configs/serve.default.yaml`

See [examples/01_data_ingestion.ipynb](../examples/01_data_ingestion.ipynb) for step-by-step.

### Path 2: Learn More
- **Architecture**: [docs/ARCHITECTURE.md](ARCHITECTURE.md) - How the system works
- **Data Guide**: [data/raw/README.md](../data/raw/README.md) - What data to use
- **Training Guide**: [examples/02_training.ipynb](../examples/02_training.ipynb) - Fine-tune your own model
- **Showcase**: [examples/showcase/](../examples/showcase/) - Real physics examples

### Path 3: Contribute
- **Add physics content**: [CONTRIBUTING.md](../CONTRIBUTING.md)
- **Report bugs**: [GitHub Issues](https://github.com/Houchen181/cm-expert-llm/issues)
- **Join discussions**: [GitHub Discussions](https://github.com/Houchen181/cm-expert-llm/discussions) (once enabled)

## 🆘 Common Issues

### "ModuleNotFoundError: No module named 'torch'"
```bash
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

### "CUDA out of memory"
Use CPU mode or reduce batch size:
```bash
python scripts/train_lora.py --config configs/train.default.yaml --batch_size 4
```

### "Port 8000 already in use"
Change the port:
```bash
python scripts/serve_api.py --config configs/serve.default.yaml --port 8001
```

## 📞 Need Help?

1. **Check the FAQ**: [docs/FAQ.md](FAQ.md) (if exists)
2. **Search issues**: https://github.com/Houchen181/cm-expert-llm/issues
3. **Ask in discussions**: https://github.com/Houchen181/cm-expert-llm/discussions
4. **Open a new issue**: https://github.com/Houchen181/cm-expert-llm/issues/new

---

**Time elapsed**: ~5 minutes  
**Next step**: Build your own domain expert LLM! 🚀

*Last updated: March 22, 2026*
