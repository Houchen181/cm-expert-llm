# Condensed Matter Physics Data Corpus

This directory contains curated condensed matter physics documents for training domain-expert LLMs.

## Categories

### 1. Superconductivity
- Conventional (BCS) superconductors
- High-Tc cuprates
- Iron-based superconductors
- Topological superconductors

### 2. Topological Phases
- Topological insulators
- Topological semimetals
- Weyl/Dirac materials
- Quantum spin liquids

### 3. Strongly Correlated Systems
- Mott insulators
- Heavy fermion systems
- Quantum criticality
- Non-Fermi liquids

### 4. Low-Dimensional Systems
- 2D materials (graphene, TMDs)
- Quantum wires and dots
- Heterostructures

### 5. Magnetism
- Ferromagnetism
- Antiferromagnetism
- Spin ice
- Skyrmions

## Source Documents

### Textbooks (Open Access)
- Kittel, "Introduction to Solid State Physics" (selected chapters)
- Ashcroft & Mermin, "Solid State Physics" (reference)
- Altland & Simons, "Condensed Matter Field Theory"

### Key Papers (arXiv)
- BCS Theory (1957) - foundational
- Meissner Effect (1933) - historical
- Topological Insulators (Kane & Mele, 2005)
- Graphene (Geim & Novoselov, 2004)

### Lecture Notes
- MIT OpenCourseWare: Condensed Matter Physics
- Cambridge: Advanced Solid State Physics

## Adding Your Data

1. Place raw text/markdown/latex files in subdirectories by category
2. Run the ingestion pipeline:
   ```bash
   python scripts/build_corpus.py --input-dir ./data/raw
   ```
3. The pipeline will chunk, extract metadata, and create JSONL output

## Format Guidelines

- Use `.md` for markdown, `.txt` for plain text, `.tex` for LaTeX
- Include clear section headers
- Preserve equations (LaTeX format preferred)
- Add metadata comments where possible

## Example Structure

```
data/raw/
├── superconductivity/
│   ├── bcs_theory.md
│   ├── high_tc.md
│   └── meissner_effect.md
├── topology/
│   ├── topological_insulators.md
│   └── weyl_semimetals.md
├── correlated/
│   ├── mott_insulators.md
│   └── heavy_fermions.md
└── textbooks/
    ├── kittel_chapters.md
    └── lecture_notes.md
```

## Quality Control

- All documents should be open-access or properly licensed
- Prefer peer-reviewed sources
- Include citations and references
- Verify equations and formulas

---

For more information, see [docs/QUICKSTART.md](../../docs/QUICKSTART.md)
