# Mott Insulators and Strongly Correlated Electron Systems

## Introduction

Mott insulators represent one of the most fascinating failures of conventional band theory. Despite having a partially filled band (which should make them metallic according to band theory), these materials are insulators due to strong electron-electron correlations.

## Historical Context

The phenomenon was first explained by Nevill Mott in the 1940s-1960s. The key insight was that strong Coulomb repulsion between electrons can localize them, creating an insulating state even when band theory predicts metallic behavior.

## The Mott Transition

### Band Theory vs. Mott Physics

**Band Theory Prediction**:
- Partially filled band → Metal
- Electron density determines conductivity

**Mott Reality**:
- Strong correlations can override band filling
- Electrons become localized due to repulsion
- Insulator emerges despite partially filled bands

### Hubbard Model

The simplest model for Mott physics is the **Hubbard model**:

$$H = -t \sum_{\langle ij \rangle, \sigma} (c_{i\sigma}^\dagger c_{j\sigma} + \text{h.c.}) + U \sum_i n_{i\uparrow} n_{i\downarrow}$$

where:
- $t$: Hopping amplitude (kinetic energy)
- $U$: On-site Coulomb repulsion
- $c_{i\sigma}^\dagger$: Creates electron at site $i$ with spin $\sigma$

### Mott Criterion

A material becomes a Mott insulator when:

$$U/W > (U/W)_c$$

where:
- $U$: Coulomb repulsion energy
- $W$: Bandwidth (W ~ zt, where z is coordination number)
- $(U/W)_c$: Critical ratio (~1-2 depending on lattice)

## Key Characteristics

### Magnetic Properties

Mott insulators typically exhibit:
- **Antiferromagnetic ordering** at low temperatures
- Local magnetic moments from unpaired electrons
- Superexchange interactions via virtual hopping

### Charge Gap

The insulating behavior arises from a **Mott-Hubbard gap**:

$$\Delta_{Mott} \approx U - W$$

This is distinct from:
- Band insulators (gap from filled bands)
- Anderson insulators (gap from disorder)

### Spectral Function

The single-particle spectral function shows:
- **Lower Hubbard Band (LHB)**: Occupied states
- **Upper Hubbard Band (UHB)**: Unoccupied states
- Gap of size ~U between them

## Material Classes

### Transition Metal Oxides

**Classic examples**:
- **NiO**: Prototype Mott insulator
- **MnO**: Antiferromagnetic Mott insulator
- **FeO**: High-pressure Mott transition
- **V₂O₃**: Temperature-driven Mott transition

### Organic Mott Insulators

- **κ-(BEDT-TTF)₂Cu₂(CN)₃**: Organic superconductor parent
- Pressure-tuned Mott transition
- Quantum spin liquid candidates

### Iron Pnictides and Chalcogenides

- Parent compounds of Fe-based superconductors
- **BaFe₂As₂**: Antiferromagnetic Mott insulator
- Becomes superconducting upon doping

## Metal-Insulator Transition

### Tuning Parameters

The Mott transition can be controlled by:

1. **Pressure**: Reduces interatomic spacing, increases W
2. **Doping**: Changes electron density
3. **Temperature**: Thermal excitation across gap
4. **Electric field**: Dielectric breakdown

### Critical Behavior

Near the Mott transition:
- Non-Fermi liquid behavior
- Divergent effective mass
- Strange metal phase
- Quantum criticality

## High-Temperature Superconductivity Connection

### Cuprate Superconductors

The parent compounds of high-Tc cuprates are Mott insulators:
- **La₂CuO₄**: Antiferromagnetic Mott insulator
- Doping with Sr or O creates superconductivity
- Pseudogap phase emerges

### Doping Evolution

1. **Undoped**: Mott insulator with AF order
2. **Light doping**: Pseudogap, strange metal
3. **Optimal doping**: High-Tc superconductivity
4. **Overdoping**: Fermi liquid behavior

## Theoretical Approaches

### Dynamical Mean-Field Theory (DMFT)

DMFT successfully captures Mott physics:
- Maps lattice problem to impurity model
- Captures local correlations exactly
- Predicts quasiparticle peak near Fermi level

### Gutzwiller Approximation

Variational approach:
- Projects out double occupancy
- Renormalizes hopping: t → g_t t
- g_t < 1 due to correlations

### Slave Boson Methods

Represent electron as composite:
- Spinon (carries spin)
- Holon (carries charge)
- Spin-charge separation in 1D

## Experimental Signatures

### Photoemission (ARPES)

- Lower and upper Hubbard bands
- Quasiparticle peak near EF (Kondo resonance)
- Momentum-dependent spectral weight

### Optical Conductivity

- Transfer of spectral weight with temperature
- Mid-infrared peak from Hubbard bands
- Drude peak suppression

### Transport

- Resistivity upturn at low T (insulating)
- Activated behavior: ρ ∝ exp(Δ/2k_BT)
- Non-Fermi liquid temperature dependence

## Advanced Topics

### Quantum Spin Liquids

Some Mott insulators avoid magnetic ordering:
- **Herbertsmithite**: ZnCu₃(OH)₆Cl₂
- **κ-(BEDT-TTF) salts**: Organic QSL
- Fractionalized excitations

### Hund's Metals

Multi-orbital systems:
- Strong Hund's coupling
- Bad metal behavior
- Iron-based superconductors

### Mottness and Topology

Recent developments:
- Topological Mott insulators
- Correlated topological phases
- Interaction-driven topology

## References

1. Mott, N. F. (1990). *Metal-Insulator Transitions*. Taylor & Francis.
2. Imada, M., Fujimori, A., & Tokura, Y. (1998). Metal-insulator transitions. *Reviews of Modern Physics*, 70(4), 1039.
3. Georges, A., Kotliar, G., Krauth, W., & Rozenberg, M. J. (1996). Dynamical mean-field theory of strongly correlated fermion systems. *Reviews of Modern Physics*, 68(1), 13.

---

**Related Topics**: Hubbard Model, High-Tc Superconductivity, Quantum Spin Liquids, Non-Fermi Liquids, Dynamical Mean-Field Theory, Strong Correlations, Metal-Insulator Transition
