# Benchmark Protocol - CMPhysBench

This document describes the evaluation protocol for cm-expert-llm using CMPhysBench (Condensed Matter Physics Benchmark).

## Overview

CMPhysBench evaluates domain-expert LLMs on four dimensions:

1. **Factual Accuracy** - Does the model know basic CM physics?
2. **Citation Grounding** - Can it cite sources correctly?
3. **Reasoning** - Can it solve multi-step problems?
4. **Uncertainty Calibration** - Does it know what it doesn't know?

## Dataset Structure

### Level 1: Undergraduate Fundamentals (100 questions)

**Topics:**
- Crystal structures and lattices
- Free electron gas
- Band theory
- Phonons and thermal properties
- Magnetism (paramagnetism, diamagnetism, ferromagnetism)

**Format:**
```json
{
  "id": "ug_001",
  "question": "What is the coordination number of an FCC lattice?",
  "options": ["6", "8", "12", "14"],
  "answer": "C",
  "difficulty": "easy",
  "source": "Kittel, Ch. 1",
  "explanation": "In FCC, each atom touches 12 nearest neighbors."
}
```

### Level 2: Graduate Core (200 questions)

**Topics:**
- Superconductivity (BCS theory, Meissner effect)
- Topological phases (quantum Hall, topological insulators)
- Correlated electrons (Mott insulators, Hubbard model)
- Broken symmetry and order parameters

**Format:**
```json
{
  "id": "grad_042",
  "question": "Derive the BCS gap equation at T=0.",
  "rubric": {
    "start_with_Hamiltonian": 2,
    "mean_field_approximation": 3,
    "bogoliubov_transformation": 3,
    "self_consistency_condition": 2
  },
  "source": "Tinkham, Ch. 3",
  "expected_answer": "..."
}
```

### Level 3: Research Frontier (100 questions)

**Topics:**
- Recent arXiv papers (2024-2026)
- Open problems in CM physics
- Interpretation of experimental data

**Format:**
```json
{
  "id": "research_017",
  "paper_arxiv": "2401.12345",
  "question": "What is the main claim of this paper?",
  "answer": "...",
  "evidence_paragraphs": ["..."],
  "source_section": "Abstract + Fig. 2"
}
```

## Evaluation Metrics

### 1. Factual Accuracy

**Multiple Choice:**
- Accuracy: % correct answers
- Confidence-weighted accuracy: penalize overconfident wrong answers

**Formula:**
```
Accuracy = (Correct Answers) / (Total Questions)
```

### 2. Citation Grounding

**Citation Precision:**
```
Citation Precision = (Correct Citations) / (Total Citations Given)
```

**Citation Recall:**
```
Citation Recall = (Correct Citations) / (Expected Citations)
```

**F1 Score:**
```
F1 = 2 * (Precision * Recall) / (Precision + Recall)
```

### 3. Reasoning

**Rubric-based scoring (0-10):**
- 0: No relevant content
- 2-4: Partial understanding, major gaps
- 5-7: Correct approach, minor errors
- 8-10: Complete and rigorous

### 4. Uncertainty Calibration

**Expected Calibration Error (ECE):**

Divide predictions into M bins by confidence:
```
ECE = Σ (|Bm| / N) * |acc(Bm) - conf(Bm)|
      m=1
```

Where:
- `|Bm|` = number of samples in bin m
- `acc(Bm)` = accuracy in bin m
- `conf(Bm)` = average confidence in bin m

**Target ECE:** < 0.1 (well-calibrated)

## Running the Benchmark

### Step 1: Install Dependencies

```bash
pip install pytest pytest-cov matplotlib seaborn
pip install cmphysbench  # (to be released)
```

### Step 2: Run Evaluation

```bash
# Full benchmark
python scripts/run_eval.py --all

# Specific level
python scripts/run_eval.py --level ug
python scripts/run_eval.py --level grad
python scripts/run_eval.py --level research

# With detailed output
python scripts/run_eval.py --all --verbose --output results.json
```

### Step 3: Generate Report

```bash
python scripts/generate_report.py --input results.json --output report.pdf
```

## Baseline Targets

| Model | UG Acc | Grad Acc | Citation F1 | ECE |
|-------|--------|----------|-------------|-----|
| GPT-4 | 85% | 65% | 0.45 | 0.25 |
| Claude-3 | 87% | 68% | 0.48 | 0.22 |
| **cm-expert-llm (target)** | **92%** | **78%** | **0.75** | **0.10** |

## Submission Guidelines

To submit results to the leaderboard:

1. Run benchmark with default settings
2. Include commit hash and model checkpoint
3. Submit via GitHub Issues template
4. Results will be verified and added to leaderboard

## Citation

If you use CMPhysBench in your research:

```bibtex
@misc{cmphysbench2026,
  title={CMPhysBench: A Benchmark for Domain-Expert LLMs in Condensed Matter Physics},
  author={cm-expert-llm Team},
  year={2026},
  url={https://github.com/Houchen181/cm-expert-llm}
}
```

---

*Last updated: 2026-03-18*
