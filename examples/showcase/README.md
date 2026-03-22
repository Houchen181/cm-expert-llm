# Physics Showcase Examples

This directory contains real-world examples of cm-expert-llm answering condensed matter physics questions.

## Examples

### 1. Superconductivity Q&A
**File**: `superconductivity_demo.py`
**Topic**: BCS theory, Meissner effect, critical temperature
**Demonstrates**: Basic RAG retrieval with citations

### 2. Topological Insulators
**File**: `topological_insulators_demo.py`
**Topic**: Band structure, Z2 invariant, surface states
**Demonstrates**: Multi-hop reasoning across papers

### 3. Correlated Electrons
**File**: `correlated_electrons_demo.py`
**Topic**: Hubbard model, Mott transition, quantum spin liquids
**Demonstrates**: Complex physics reasoning with equations

## How to Run

```bash
# Run individual example
python examples/showcase/superconductivity_demo.py

# Run all examples
python examples/showcase/run_all.py
```

## Why These Examples Matter

These showcase examples demonstrate:
1. **Domain expertise**: Answers show deep physics understanding
2. **Citation quality**: Every claim backed by sources
3. **Reasoning transparency**: Clear chain of thought
4. **Educational value**: Suitable for students and researchers

## Contributing Examples

Want to add your own physics example? See [CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines.

---

*These examples are automatically tested to ensure reproducibility.*
