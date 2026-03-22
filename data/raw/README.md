# Raw Data - cm-expert-llm

This directory contains **real physics content** used to train the domain-expert LLM. All materials are sourced from primary sources: peer-reviewed papers, textbooks, and lecture notes.

## 📚 Contents

### By Subfield

#### 1. **Superconductivity** (`superconductivity/`)
- BCS theory fundamentals
- High-temperature superconductors
- Meissner effect and perfect diamagnetism
- Critical temperature phenomena
- Type I and Type II superconductors

#### 2. **Topology** (`topology/`)
- Topological insulators (2D and 3D)
- Quantum Hall effects
- Weyl and Dirac semimetals
- Z2 invariants and band topology
- Surface states and edge modes

#### 3. **Correlated Electrons** (`correlated/`)
- Hubbard model and Mott physics
- Quantum spin liquids
- Heavy fermion systems
- Kondo effect
- Strongly correlated materials

#### 4. **Recent arXiv Papers** (`recent_arxiv/`)
- **13 papers** from March 2026
- Updated continuously via automated monitoring
- Covers all condensed matter subfields
- Full abstracts, DOIs, and key concepts
- See [`recent_arxiv/README.md`](recent_arxiv/README.md) for complete list

## 📊 Statistics

| Category | Papers/Documents | Last Updated |
|----------|-----------------|--------------|
| Superconductivity | ~15 documents | March 2026 |
| Topology | ~12 documents | March 2026 |
| Correlated Electrons | ~10 documents | March 2026 |
| Recent arXiv | 13 papers | March 22, 2026 |
| **Total** | **~50 documents** | **Continuously updated** |

## 🔬 What Makes This Data Special

### ✅ Real Primary Sources
- **No AI summaries** - All content from actual papers and textbooks
- **Proper citations** - Every document has DOI and bibliographic info
- **Peer-reviewed** - Only published, validated research
- **Diverse subfields** - Broad coverage of condensed matter physics

### ✅ Continuously Updated
- **Automated arXiv monitoring** via `examples/05_continuous_arxiv.ipynb`
- **Daily/weekly updates** with latest research
- **Community contributions** welcome and encouraged

### ✅ Educational Value
- **Structured learning** - Organized by physics subfield
- **Progressive difficulty** - From undergrad to research level
- **Cross-referenced** - Links between related concepts

## 🤝 How to Contribute Data

### Option 1: Add a Paper Summary
1. Create a new file in the appropriate subfolder
2. Use the template below
3. Include full abstract, DOI, and key concepts
4. Submit via PR

### Option 2: Add Textbook Excerions
1. Ensure fair use / educational exception
2. Cite textbook properly (author, edition, page)
3. Add to relevant subfolder
4. Note: Only excerpts, not full chapters (copyright)

### Option 3: Add Lecture Notes
1. Your own notes or with permission
2. Clear attribution
3. Organize by topic
4. Include references to primary sources

## 📝 Template for New Papers

```markdown
## Paper Title

**Authors:** Author names

**arXiv:** arXiv:XXXX.XXXXX [cond-mat.subfield]

**Date:** Month Year

**DOI:** [Link to DOI](https://doi.org/...)

**Abstract:** Full abstract text

**Key Concepts:**
- Concept 1
- Concept 2
- Concept 3

**Relevance to cm-expert-llm:**
- Why this paper matters
- What physics it teaches

**Full Text:** [View PDF](link)

**Comments:** Pages, figures, journal reference
```

## 🔄 Update Schedule

- **Automated**: Daily arXiv fetch (via `examples/05_continuous_arxiv.ipynb`)
- **Manual**: As new papers are discovered or contributed
- **Review**: Monthly check for outdated content

## 📚 Recommended Additions

Priority areas for new content:
- [ ] Topological superconductors
- [ ] Strange metals and non-Fermi liquids
- [ ] 2D materials (graphene, TMDs)
- [ ] Quantum computing materials
- [ ] Machine learning interatomic potentials
- [ ] Time crystals and Floquet systems

## 🔍 Searching the Data

Use the retrieval system to search across all documents:
```bash
python scripts/run_eval.py --query "What is the Meissner effect?"
```

Or use the interactive API:
```bash
python scripts/serve_api.py --config configs/serve.default.yaml
```

Then query at `http://localhost:8000/docs`

## 📊 Data Quality

All content is:
- ✅ From primary sources (papers, textbooks)
- ✅ Properly cited with DOI
- ✅ Verified by physics experts
- ✅ Regularly updated
- ✅ Community-reviewed

## 🙏 Acknowledgments

This data collection grows through contributions from:
- Original paper authors
- Community contributors
- Automated arXiv monitoring
- Educational initiatives

---

**Want to contribute?** See [CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines.

**Questions?** Open an issue or start a discussion on [GitHub](https://github.com/Houchen181/cm-expert-llm).

*Last updated: March 22, 2026*
