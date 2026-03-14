# BCS Theory of Superconductivity

## Historical Background

The BCS theory, proposed by Bardeen, Cooper, and Schrieffer in 1957, provides the first microscopic explanation of superconductivity in conventional (low-temperature) superconductors. This theory successfully explained the Meissner effect and zero electrical resistance observed in superconducting materials.

## Key Concepts

### Cooper Pairs

The central insight of BCS theory is that electrons in a superconductor form **Cooper pairs**. Despite their mutual Coulomb repulsion, electrons can experience an effective attractive interaction mediated by lattice vibrations (phonons):

1. An electron moving through the lattice attracts positive ions
2. This creates a region of increased positive charge density
3. A second electron is attracted to this region
4. The two electrons become correlated as a Cooper pair

The binding energy of a Cooper pair is typically on the order of millielectronvolts (meV).

### The Energy Gap

BCS theory predicts that superconductors have an **energy gap** Δ in the quasiparticle excitation spectrum. This gap represents the minimum energy required to break a Cooper pair into two independent quasiparticles.

At zero temperature, the energy gap is given by:

$$\Delta(0) = 2\hbar\omega_D \exp\left(-\frac{1}{N(0)V}\right)$$

where:
- $\omega_D$ is the Debye frequency
- $N(0)$ is the density of states at the Fermi level
- $V$ is the effective pairing interaction strength

### Critical Temperature

The critical temperature $T_c$ at which superconductivity emerges is:

$$k_B T_c = 1.14 \hbar\omega_D \exp\left(-\frac{1}{N(0)V}\right)$$

This exponential dependence explains why $T_c$ is typically much smaller than the Debye temperature.

## BCS Gap Equation

The temperature-dependent energy gap satisfies the self-consistency equation:

$$\frac{1}{N(0)V} = \int_0^{\hbar\omega_D} \frac{\tanh\left(\frac{\sqrt{\xi^2 + \Delta^2}}{2k_B T}\right)}{\sqrt{\xi^2 + \Delta^2}} d\xi$$

where $\xi$ is the single-particle energy measured from the Fermi level.

## Key Predictions

1. **Energy Gap**: Exponential temperature dependence of thermodynamic properties
2. **Specific Heat**: $C \propto \exp(-\Delta/k_B T)$ at low temperatures
3. **Tunneling**: Characteristic I-V curves in superconductor-insulator-normal metal junctions
4. **Meissner Effect**: Complete diamagnetism below $T_c$

## Limitations

BCS theory works excellently for:
- Elemental superconductors (Al, Pb, Sn, etc.)
- A-15 compounds (Nb₃Sn, V₃Ga)
- Conventional low-Tc materials

However, it does not fully explain:
- High-temperature cuprate superconductors
- Unconventional pairing symmetries (d-wave, p-wave)
- Strong-coupling superconductors

## Mathematical Formalism

### BCS Hamiltonian

The reduced BCS Hamiltonian is:

$$H = \sum_{k,\sigma} \xi_k c_{k\sigma}^\dagger c_{k\sigma} + \sum_{k,k'} V_{kk'} c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger c_{-k'\downarrow} c_{k'\uparrow}$$

where $c_{k\sigma}^\dagger$ creates an electron with momentum $k$ and spin $\sigma$.

### Bogoliubov Transformation

The Hamiltonian is diagonalized using the Bogoliubov transformation:

$$\gamma_{k\uparrow} = u_k c_{k\uparrow} - v_k c_{-k\downarrow}^\dagger$$
$$\gamma_{-k\downarrow}^\dagger = u_k c_{-k\downarrow}^\dagger + v_k c_{k\uparrow}$$

with coherence factors $u_k^2 + v_k^2 = 1$.

## References

1. Bardeen, J., Cooper, L. N., & Schrieffer, J. R. (1957). Theory of Superconductivity. *Physical Review*, 108(5), 1175.
2. Tinkham, M. (2004). *Introduction to Superconductivity*. Dover Publications.
3. de Gennes, P. G. (1999). *Superconductivity of Metals and Alloys*. Westview Press.

---

**Related Topics**: Meissner Effect, Cooper Pairs, Energy Gap, Critical Temperature, Type-II Superconductors, High-Tc Superconductivity
