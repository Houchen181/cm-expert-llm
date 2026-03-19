# Recent Condensed Matter Physics Papers (arXiv March 2026)

This directory contains **real, current research papers** from arXiv's condensed matter physics section. These are used as primary training data for CondensAI to ensure up-to-date domain knowledge.

---

## Paper 1: Bose-Einstein Condensates & Solitary Waves

**Title:** Systematic solitary waves by linear limit continuation from two anisotropic traps in two-dimensional Bose-Einstein condensates

**Authors:** Wenlong Wang et al.

**arXiv:** arXiv:2603.17996 [cond-mat.quant-gas]

**Date:** March 18, 2026

**DOI:** [10.48550/arXiv.2603.17996](https://doi.org/10.48550/arXiv.2603.17996)

**Abstract:**
Linear limit continuation was recently developed as a systematic and effective method for constructing numerically exact solitary waves from their respective linear limits. In this work, we apply the technique to two typical anisotropic harmonic traps in two-dimensional Bose-Einstein condensates to further establish the method and also to find more solitary waves. Many wave patterns are identified in the near-linear regime and they are subsequently continued into the Thomas-Fermi regime, and then they are further continued into the isotropic trap if possible. Finally, the parametric connectivity of the pertinent solitary waves is also discussed.

**Key Concepts:**
- Bose-Einstein condensates (BEC)
- Solitary waves / solitons
- Linear limit continuation method
- Anisotropic harmonic traps
- Thomas-Fermi regime
- Parametric connectivity

**Relevance to CondensAI:** This paper demonstrates advanced techniques in quantum gases and pattern formation, providing training data on:
- Mathematical methods in condensed matter (continuation techniques)
- Quantum many-body physics
- Nonlinear phenomena in quantum systems

**Full Text:** [View PDF](https://arxiv.org/pdf/2603.17996)

---

## Paper 2: Active Matter & Feedback Control

**Title:** Feedback control and delayed interactions in active matter

**Authors:** Frank Cichos et al.

**arXiv:** arXiv:2603.17894 [cond-mat.soft]

**Date:** March 18, 2026

**DOI:** [10.48550/arXiv.2603.17894](https://doi.org/10.48550/arXiv.2603.17894)

**Abstract:**
Feedback control plays a central role in active matter, yet it is inevitably accompanied by noise and finite perception-action delays. This Perspective reviews recent advances on active systems with delayed interactions, showing how time delay can induce activity, chirality, transport, and collective pattern formation, and can act as an effective control parameter for switching between dynamical states. We discuss representative single-particle and many-body systems, highlight key experimental realizations, and argue that time delay constitutes an underexplored dimension of morphological intelligence—where intrinsic response dynamics, rather than explicit sensors or computation, enable functional behavior in active matter.

**Key Concepts:**
- Active matter
- Feedback control
- Time delay in dynamical systems
- Morphological intelligence
- Collective pattern formation
- Non-equilibrium statistical mechanics

**Relevance to CondensAI:** This perspective article provides insights into:
- Soft condensed matter physics
- Control theory applications in physics
- Emergent behavior in many-body systems
- Time-delayed interactions

**Full Text:** [View PDF](https://arxiv.org/pdf/2603.17894)

---

## Paper 3: Quantum Dots & Spin Physics

**Title:** Strain-driven spin mixing and dark-exciton recombination in a neutral Ni2+ doped quantum dot

**Authors:** Lucien Besombes et al.

**arXiv:** arXiv:2603.17752 [cond-mat.mes-hall]

**Date:** March 18, 2026

**DOI:** [10.48550/arXiv.2603.17752](https://doi.org/10.48550/arXiv.2603.17752)

**Abstract:**
We investigate the optical properties of neutral excitons in CdTe/ZnTe quantum dots containing a single Ni2+ ion. We show that the photoluminescence spectra provide a direct spectroscopic signature of strain induced mixing of the Ni2+ spin states. A misalignment between the principal axis of the local strain tensor and the quantum dot growth direction reorients the spin quantization axis of the magnetic ion, reducing the hole Ni2+ exchange interaction at low magnetic field and giving rise to photoluminescence replicas around the partially linearly polarized bright-exciton transitions. A longitudinal magnetic field restores the circularly polarized optical selection rules, allowing the three spin projections S_z = 0, +-1 of the Ni2+ ion to be spectrally resolved. Dark exciton emission appears on the low energy side of the spectra and is dominated at low field by transitions involving spin flips of the magnetic ion. An effective spin Hamiltonian including strain orientation and valence band mixing reproduces the magnetic field evolution of both bright and dark exciton spectra. These results highlight the key role of the local strain environment in determining the spin exciton coupling of transition metal dopants in semiconductor quantum dots.

**Key Concepts:**
- Quantum dots (CdTe/ZnTe)
- Transition metal doping (Ni2+)
- Spin-exciton coupling
- Strain engineering
- Photoluminescence spectroscopy
- Dark excitons
- Spin Hamiltonian

**Relevance to CondensAI:** This experimental paper demonstrates:
- Mesoscale and nanoscale physics
- Spin physics in semiconductors
- Strain effects in quantum materials
- Optical spectroscopy techniques
- Magnetic field effects in quantum systems

**Full Text:** [View PDF](https://arxiv.org/pdf/2603.17752)

---

## How to Use These Papers

These papers are integrated into CondensAI's retrieval corpus. When users ask questions about:
- Bose-Einstein condensates
- Active matter and feedback
- Quantum dots and spin physics
- Recent advances in condensed matter

CondensAI can retrieve and cite these real papers, providing up-to-date, accurate information grounded in current research.

## Adding More Papers

To add more papers to the training corpus:

1. Fetch recent papers from arXiv condensed matter categories:
   - cond-mat.supr-con (Superconductivity)
   - cond-mat.str-el (Strongly Correlated Electrons)
   - cond-mat.top-hall (Topological materials)
   - cond-mat.quant-gas (Quantum gases)
   - cond-mat.soft (Soft condensed matter)
   - cond-mat.mes-hall (Mesoscale and nanoscale)

2. Extract abstract, key concepts, and relevance

3. Add to this directory with proper citation format

4. Update the retrieval index:
   ```bash
   python scripts/update_index.py data/raw/
   ```

## Citation Format

All papers should include:
- ✅ Full title
- ✅ Author list
- ✅ arXiv identifier with category
- ✅ Submission date
- ✅ DOI link
- ✅ Abstract (full text)
- ✅ Key concepts (extracted)
- ✅ Relevance to domain expertise
- ✅ Link to full PDF

This ensures proper attribution and traceability to primary sources.

---

*Last updated: 2026-03-19*

*These papers represent cutting-edge research in condensed matter physics as of March 2026.*
