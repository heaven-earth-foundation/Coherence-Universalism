# CU Biology C.1.1 — Cumulative Reconstruction and Audit-Repair Ledger

**Legacy source:** `CU_Biology.md` (March 2026)  
**C.1 source:** `CU_Biology_Systematic_Reconstruction_Kaya_C1.md`  
**C.1.1 manuscript:** `CU_Biology_Systematic_Reconstruction_Kaya_C1_1.md`  
**Canonical dependencies:** Physics A.6.1; M&E B.2; Foundations B.2  
**Independent review:** `CU_Biology_C1_Independent_Audit.md`  
**Date:** September 2026

## 1. Governing reconstruction

The March paper treated biological coherence as a universal scalar and used that quantity to connect origins, development, evolution, pathology, and death. C.1 replaced the single-number architecture with declared biological models, multidimensional profiles, intervention-based causal tests, and explicit claim statuses. C.1.1 preserves that reconstruction and applies a bounded repair prompted by independent audit.

## 2. Claims retired or rejected in C.1

- \(C(x)=A(x)I(x)\) as a universal measure of biological coherence.
- \(I=(\gamma S R)^{1/3}\) as a canonical integration functional.
- A universal biological coherence gradient inherited directly from Foundations.
- A universal energetic inequality \(E\ge\lambda C\) or efficiency ratio \(C/\Phi\).
- Life as reversal, cancellation, or violation of the second law.
- Low entropy as sufficient for biological organization.
- One sharp, universal abiogenesis phase transition.
- Recurrence dominance as sufficient for life.
- Evolution as monotone “coherence ascent” or fitness as coherence.
- Death as \(C=0\).
- A universal bioelectric master code or general electrical normalization theory of cancer.
- Numerical toy models as validation of the biological framework.

## 3. Replacement architecture retained in C.1.1

A candidate biological model is declared by

\[
\mathcal B=(X,E,U,F,K,G,R,H,\pi,T),
\]

with state space, environment, actions, dynamics, constraints, relational organization, maintenance processes, history, boundary/scale, and horizon. The principal objects are viability regions and kernels, robust viability under a declared disturbance class, counterfactual maintenance contributions, resilience, causal integration under interventions, organizational closure, adaptive reach, historical continuity, and material or energetic cost. They form a profile rather than a universal scalar.

## 4. Independent-audit disposition

The independent audit recommended **adopt with bounded repairs**. It independently reproduced the C.1 toy model, confirmed the declared update, budget, disturbance schedule, floors, and step-size behavior, found no covert return of a universal scalar, and verified that clipping was inactive. It identified one substantive framing problem: the positive viability-margin trend arose in a configuration predisposed to benefit from mean coupling and was not a general effect of integration.

C.1.1 accepts that finding and sharpens it.

## 5. C.1.1 formal repair

For margins

\[
m_i(x)=x_i-f_i,
\qquad
M(x)=\min_i m_i(x),
\]

and diffusive coupling

\[
c_i(x)=\kappa(\bar x-x_i),
\]

C.1.1 adds the exact one-sided directional relation

\[
D M(x;c)
=
\min_{i\in I(x)}\kappa(\bar x-x_i),
\qquad
I(x)=\operatorname*{arg\,min}_i m_i(x).
\]

For a unique binding component \(j\), the direct contribution is \(\kappa(\bar x-x_j)\). This is explicitly limited to the local contribution at a fixed state; it does not determine the global minimum of a family of controlled trajectories as \(\kappa\) changes.

## 6. C.1.1 numerical repair

### Configuration I — retained and relabeled

The original homogeneous-floor sweep is retained. It shows increasing minimum margin together with increasing control cost and late differentiated tracking error. C.1.1 now states that:

- the equal floors make a unique binding component a minimum-state component and therefore not above the mean;
- the positive margin direction is a property of the declared trajectory family, not a law of coupling;
- every controller run remains well inside the viable region, so the sweep demonstrates redistribution of margin rather than coupling-mediated rescue; and
- clipping is inactive.

### Configuration II — added

A second configuration uses

\[
f=(0.10,0.10,0.82),
\quad
x(0)=(0.60,0.60,0.90),
\]

\[
s=(0.18,0.18,0.036),
\quad
d=(0.30,0.30,0.04),
\]

with a constant target equal to the uncoupled equilibrium and a disturbance \((0,0,-0.020)\) over \(40\le t<50\). The high-state third component is closest to its much higher floor and lies above the mean. Coupling drains it. Across the declared sweep, minimum margin falls from \(0.0431278138\) to \(-0.0470145357\), first becoming negative at \(\kappa=0.25\).

The sign reversal persists over \(\Delta t\in\{0.04,0.02,0.01,0.005\}\), and clipping remains inactive.

## 7. Claim-governance repair

The following rules previously existed only in the machine-readable principle registry. C.1.1 moves them into §2.7.1 of the manuscript:

1. every biological coherence claim names the candidate unit and scale;
2. every maintenance claim names the temporal horizon;
3. every robustness claim names the disturbance class;
4. scalarization declares weights, protected floors, and aggregation rules; and
5. organism-relative stake is not promoted directly into phenomenal or moral value.

## 8. Optimization-language repair

Appendix A.18's distinction among designer optimization, as-if control analysis, and evolutionary selection is retained and explicitly exported to downstream Consciousness, Psychology, Social Dynamics, Ethics, and AI reconstructions.

## 9. Literature repair

The *Stentor coeruleus* discussion and literature ledger now record that Rajan et al. (2026) found protein-synthesis inhibition accelerated habituation and prolonged retention, and that habituation memory could persist in progeny following division. The manuscript retains conservative boundaries: the result supports history-dependent non-neural regulation but does not establish consciousness, human-like representation, or a general theory of inherited cognition.

## 10. Claim and principle registries

Two claim-ledger entries are added:

- **BIO-C36:** the local directional coupling lemma;
- **BIO-C37:** rejection of a universal viability benefit from stronger diffusive integration.

CU-B1 through CU-B5 remain candidates. The independent audit explicitly did not assess their conceptual adequacy in detail, so C.1.1 does not promote them into Foundations B.2.

## 11. Files and reproducibility

C.1.1 provides:

- a revised manuscript;
- updated claim, principle, and literature ledgers;
- a deterministic two-configuration verification script;
- generated JSON results;
- a C.1-to-C.1.1 patch;
- structural and numerical QA;
- an audit-response memo;
- and an integrity manifest.

The numerical package establishes reproducibility of the declared toy models. It is not biological validation or expert peer review.
