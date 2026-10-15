# Coherence Universalism: Biology
## RC3 Release-Convergence Wave 4 — Technical Supplement

**Status and authority.** This is the released technical supplement for the Wave 4 cumulative manuscript. The [reader-facing manuscript](../papers/04_CU_Biology_v0.10.md) controls current wording, claim status, and canonical cross-references. This supplement exposes the formal derivations, deterministic contrast constructions, claim ledgers, audit materials, scripts, and source records on which the manuscript relies.

- **Evidence directory:** [04_Biology](../evidence/04_Biology/README.md)
- **Archived source package:** [CU_Biology_v0.10_Publication_PC4.zip](../provenance/archival_source_packages/CU_Biology_v0.10_Publication_PC4.zip)
- **Current supplement path:** `technical_supplements/04_Biology_Technical_Supplement_v0.10.md`

Reproducibility of a construction shows only that its output follows from its declared assumptions and code. It does not convert a toy model or simulation into target-domain empirical validation. Where this preserved archive uses historical identifiers or statuses, the Wave 4 normalized registries and current manuscript control.

# Wave 4 evidence-access addendum

Wave 4 makes previously referenced but inaccessible materials available in one package. It includes the substantive legacy supplement below, the independent audit and check script, recorded audit output where available, source ledgers, deterministic scripts and generated results where they existed, and the complete pre-RC3 source package for provenance.

# Preserved substantive technical archive

**Gaura Kiśora Dās Rader**  
**Heaven≡Earth Foundation**  
**September 2026**

---

## Purpose and authority

This supplement preserves the formal propositions, complete claim ledger, principle crosswalk, deterministic models, literature ledger, audit record, and editorial provenance underlying the reader-facing Biology publication candidate.

The principal manuscript is designed for continuous scholarly reading. This supplement is designed for checking. Where wording differs, the frozen C.1.1 authority manuscript controls the exact pre-publication technical content, while the main publication candidate controls reader-facing presentation. Any substantive discrepancy must be resolved against the frozen source and recorded in a later version.

## Contents

- Supplement A — Formal Definitions and Bounded Propositions
- Supplement B — Illustrative Three-Variable Viability-Control Models
- Supplement C — Full Claim and Evidence Ledger
- Supplement D — Biology Principle Crosswalk and B.3 Synchronization
- Supplement E — Revision and Audit Ledger
- Supplement F — Figure and Experiment Program
- Supplement G — Selective Literature Ledger
- Supplement H — Reproducibility and Verification Record
- Supplement I — Independent Audit and Editorial Provenance
- Supplement J — Editorial and Source Map

The executable code, generated results, environment declaration, audits, and integrity records accompany this supplement in the publication package.

---

# Supplement A. Formal definitions and bounded propositions

## A.1 Scope

This appendix records results that follow from the model architecture of Section 3. They are not universal laws of living matter. Each proposition is conditional on its declared state space, dynamics, controls, disturbances, constraints, and horizon.

## A.2 Definition: finite-horizon viability

Let \(X\) be a state space, \(V\subseteq X\) a closed viability region, \(U_1\) an admissible control set, and \(F\) a dynamical law. The finite-horizon viability kernel is

\[
\operatorname{Viab}_{T}(V;F,U_1)
=
\left\{
 x_0\in V:
 \exists\rho\in U_1
 \ \forall t\in[0,T],
 x_t^{\rho}\in V
\right\}.
\]

This definition is policy-relative. Changing the action set changes what can be maintained.

## A.3 Proposition 1: monotonicity in available control

If \(U_1\subseteq U_2\), then

\[
\operatorname{Viab}_{T}(V;F,U_1)
\subseteq
\operatorname{Viab}_{T}(V;F,U_2).
\]

### Proof

Take \(x_0\in\operatorname{Viab}_{T}(V;F,U_1)\). By definition, there exists a policy \(\rho\in U_1\) that keeps the trajectory in \(V\) through \(T\). Since \(U_1\subseteq U_2\), the same policy is available in \(U_2\). Hence \(x_0\in\operatorname{Viab}_{T}(V;F,U_2)\). \(\square\)

### Interpretation

Additional available actions cannot shrink the mathematical viability kernel. Biological costs, cognitive limits, control conflict, or unsafe actions can still make the enlarged action set undesirable. Those considerations must be included in constraints or cost dimensions.

## A.4 Definition: robust viability

For a disturbance class \(\mathcal D\),

\[
\operatorname{RViab}_{T}(V;F,U,\mathcal D)
=
\left\{
 x_0\in V:
 \exists\rho\in U
 \ \forall d\in\mathcal D
 \ \forall t\in[0,T],
 x_t^{\rho,d}\in V
\right\}.
\]

## A.5 Proposition 2: antitonicity in disturbance class

If \(\mathcal D_1\subseteq\mathcal D_2\), then

\[
\operatorname{RViab}_{T}(V;F,U,\mathcal D_2)
\subseteq
\operatorname{RViab}_{T}(V;F,U,\mathcal D_1).
\]

### Proof

Any policy that maintains viability against every disturbance in \(\mathcal D_2\) also maintains it against the subset \(\mathcal D_1\). \(\square\)

### Interpretation

A claim of increased robustness is incomplete unless the disturbance class is fixed. A system can appear robust because the test excludes the disturbances to which it is vulnerable.

## A.6 Proposition 3: recurrence dominance does not imply self-maintenance

There exist passive Markov systems satisfying

\[
P(L_{t+1}\mid L_t)
>
P(L_{t+1}\mid \neg L_t)
\]

without any endogenous regulation, repair, boundary production, or reproduction.

### Proof by construction

Let \(X_t\in\{L,N\}\) follow

\[
P
=
\begin{pmatrix}
0.99&0.01\\
0.10&0.90
\end{pmatrix},
\]

where rows correspond to \(L,N\) and columns to \(L,N\). Then

\[
P(L_{t+1}\mid L_t)=0.99
>
0.10=P(L_{t+1}\mid N_t).
\]

The transition law can be entirely passive. Therefore the inequality is not sufficient for self-maintenance. \(\square\)

## A.7 Proposition 4: local maintenance can oppose organismal maintenance

There exist nested systems in which an intervention improves a component-level outcome and worsens the organism-level outcome.

### Construction

Let component activity \(y\ge0\) produce local benefit

\[
Q_i(y)=y,
\]

while imposing organismal damage above a tolerated level \(y_0\):

\[
Q_B(y)=1-(y-y_0)^2.
\]

For \(y>y_0\), increasing \(y\) gives

\[
\frac{dQ_i}{dy}=1>0,
\qquad
\frac{dQ_B}{dy}=-2(y-y_0)<0.
\]

Thus local and global maintenance can diverge. \(\square\)

### Interpretation

No claim that “coherence increased” is well formed until the system boundary and outcome are named.

## A.8 Proposition 5: Pareto incomparability prevents a context-free scalar optimum

Let two strategies have profile components

\[
\mathbf c_1=(0.9,0.5),
\qquad
\mathbf c_2=(0.7,0.8),
\]

where both components are to be maximized. Neither strategy Pareto-dominates the other.

For weighted sums \(S_w(c)=wc_1+(1-w)c_2\), the preferred strategy changes with \(w\):

\[
S_w(\mathbf c_1)-S_w(\mathbf c_2)
=0.5w-0.3.
\]

Hence \(\mathbf c_1\) is preferred when \(w>0.6\), \(\mathbf c_2\) when \(w<0.6\), and they tie at \(w=0.6\).

### Consequence

The data do not identify one optimum without a priority rule. A universal scalar would add normative or decision assumptions not contained in the profile.

## A.9 Proposition 6: state similarity is neither necessary nor sufficient for token identity

### Not necessary

Let a developmental process carry an organism from larval state \(x_0\) to adult state \(x_T\) with large state-space distance \(d(x_0,x_T)\). Causal continuity can preserve the organism despite \(d\) being large.

### Not sufficient

Let a copying operation produce \(x'_T=x_T\) while the original remains. Then \(d(x_T,x'_T)=0\) but the two are numerically distinct tokens.

### Consequence

Biological identity requires a history-sensitive relation, not only state distance.

## A.10 Definition: endogenous maintenance contribution

For regulatory component \(R_i\), horizon \(T\), matched initial states, and disturbance distribution \(\mathcal P\), define

\[
\Delta_i(T)
=
\Pr_{\mathcal P}(\tau_V>T\mid\operatorname{do}(R_i=\mathrm{intact}))
-
\Pr_{\mathcal P}(\tau_V>T\mid\operatorname{do}(R_i=\mathrm{disabled})).
\]

The comparison is valid only when disabling \(R_i\) does not introduce uncontrolled collateral differences. A component can have positive \(\Delta_i\) without belonging to a closed self-maintaining organization.

## A.11 Proposition 7: positive component contributions do not prove closure

Consider two externally manufactured controllers \(R_1,R_2\) installed in a vessel. Each improves survival, so \(\Delta_1,\Delta_2>0\). Neither controller is produced, repaired, or sustained by the vessel or by the other controller. The contribution graph lacks reciprocal maintenance edges.

Therefore positive maintenance contribution is not sufficient for organizational closure. \(\square\)

## A.12 Definition: a represented closure core

Given a directed maintenance graph \(G_R=(R,E)\), a subset \(S\subseteq R\) is a represented closure core when:

1. the induced subgraph \(G_R[S]\) is strongly connected;
2. every \(R_i\in S\) has interventionally supported outgoing contribution to at least one other member;
3. every \(R_i\in S\) receives a necessary or significant maintenance contribution from at least one other member; and
4. the relevant processes are materially and temporally realizable together.

Strong connectivity alone is not sufficient because arbitrary diagrams can contain cycles that do no causal work.

## A.13 Proposition 8: a phase transition requires more than a threshold label

Suppose an observed output \(Y\) changes rapidly near parameter \(\lambda_0\). This fact alone does not establish a phase transition. The same pattern can be generated by a smooth sigmoid

\[
Y(\lambda)=\frac{1}{1+e^{-k(\lambda-\lambda_0)}}
\]

for finite \(k\).

A phase-transition claim requires additional structure: a thermodynamic or large-system limit, bifurcation, discontinuity, critical scaling, hysteresis, symmetry breaking, or another explicitly defined criterion.

### Consequence

The phrase “abiogenesis phase transition” must be attached to a specific model and order parameter.

## A.14 Proposition 9: post hoc viability sets make the framework vacuous

For any observed trajectory \(x_{0:T}\), define

\[
V^*=\{x_t:0\le t\le T\}.
\]

Then the trajectory remains viable by construction. If viability constraints may always be chosen after observing the data, every trajectory can be classified as coherent.

### Consequence

Viability conditions must be independently motivated, preregistered, or validated on held-out perturbations.

## A.15 Proposition 10: the viability effect of diffusive coupling is configuration-dependent

Let the componentwise viability margins be

\[
m_i(x)=x_i-f_i,
\qquad
M(x)=\min_i m_i(x),
\]

and let

\[
I(x)=\operatorname*{arg\,min}_i m_i(x)
\]

be the set of binding components. For the diffusive coupling vector

\[
c_i(x)=\kappa(\bar x-x_i),
\qquad
\bar x=\frac{1}{n}\sum_i x_i,
\]

its one-sided directional contribution to the minimum margin is

\[
D M(x;c)
=
\min_{i\in I(x)}\kappa(\bar x-x_i).
\]

If the binding component is unique, \(I(x)=\{j\}\), then

\[
D M(x;c)=\kappa(\bar x-x_j).
\]

Therefore the direct instantaneous coupling contribution raises the currently binding margin when \(x_j<\bar x\), lowers it when \(x_j>\bar x\), and is zero when \(x_j=\bar x\). With several tied binding components, the directional derivative is governed by the least favorable member of the binding set.

This is a local statement at a fixed state. It does not by itself determine how the global minimum over a finite controlled trajectory changes as \(\kappa\) changes, because the trajectory, controller allocation, disturbance response, time of minimum, and identity of the binding component can all change.

In Supplement B's first configuration, all floors are equal. A unique binding component is therefore a minimum-state component and cannot lie above the mean. This predisposes the direct coupling term to support, rather than drain, the currently binding margin. The observed strict increase across the full sweep remains a property of the declared simulation, not a theorem for all homogeneous-floor controlled systems.

In the second configuration, the third component has a much higher floor and is binding while its state lies above the mean. The same coupling law drains that component. The sampled minimum margin strictly decreases and crosses zero as \(\kappa\) increases.

Thus stronger coupling need not improve viability, and no theorem permits replacing a multidimensional biological profile with “more integration is better.”

## A.16 Formal boundary audit

For candidate boundaries \(B_1,\ldots,B_m\), define a boundary score vector

\[
\mathbf Z(B_j)
=
\left(
\operatorname{Pred}_j,
\operatorname{Interv}_j,
\operatorname{Closure}_j,
\operatorname{Cost}_j
\right),
\]

where the components report predictive fit, intervention transfer, represented closure, and model complexity or omitted external cost.

No unique scalar is mandated. A boundary is supported when it remains nondominated across reasonable scoring rules and reproduces under new interventions.

## A.17 Formal horizon audit

For a strategy \(\rho\), let \(Q_T(\rho)\) be a maintenance outcome. A horizon reversal occurs when

\[
Q_{T_1}(\rho_1)>Q_{T_1}(\rho_2)
\quad\text{but}\quad
Q_{T_2}(\rho_1)<Q_{T_2}(\rho_2),
\qquad
T_2>T_1.
\]

Such reversals are expected when a strategy trades reserves or environmental integrity for short-run performance. Reporting one horizon can therefore reverse the apparent ordering.

## A.18 Formal status of optimization language

The equation

\[
\rho^*=\arg\max_{\rho}Q_T(\rho)
\]

can be used in three different senses:

1. **designer optimization:** an engineer literally selects \(\rho\);
2. **as-if control analysis:** the equation summarizes observed behavior without asserting an internal solver;
3. **evolutionary outcome:** selection changes the distribution of architectures in a direction correlated with \(Q_T\).

These senses must not be conflated. Neither as-if optimization nor evolutionary filtering proves that an organism represents or consciously chooses the objective.

---

# Supplement B. Illustrative three-variable viability-control models

## B.1 Purpose and status

The original paper claimed that a toy simulation “validated” a biological coherence functional. This paper uses two much narrower deterministic configurations:

1. a homogeneous-floor configuration in which stronger coupling raises the sampled minimum margin while worsening differentiated tracking and raising control cost; and
2. a heterogeneous-floor configuration in which the same coupling law lowers the sampled minimum margin and eventually produces a viability breach.

The purpose is to show that integration, viability, flexibility, and cost have no configuration-independent monotonic ordering. The models are not fitted to biological data.

## B.2 Common dynamics and the local coupling lemma

Let

\[
x(t)=(x_1(t),x_2(t),x_3(t))\in[0,1]^3
\]

represent three regulated capacities. Each receives baseline supply \(s_i\), decays at rate \(d_i x_i\), receives bounded control \(u_i\), experiences coupling toward the mean, and is exposed to deterministic perturbations:

\[
\dot x_i
=
s_i-d_i x_i+u_i
+\kappa(\bar x-x_i)
+\xi_i(t).
\]

For component floors \(f_i\), define

\[
M(x)=\min_i(x_i-f_i).
\]

At a state with unique binding component \(j\), the direct coupling contribution to the instantaneous change of \(M\) is

\[
\kappa(\bar x-x_j).
\]

This sign test is exact at a fixed state. It is not a theorem about the global minimum generated by a family of controlled trajectories with different \(\kappa\).

## B.3 Common controller and numerical method

The unconstrained desired control is

\[
u_i^{\mathrm{des}}
=
\max\{0,0.5(y_i-x_i)\}.
\]

The total instantaneous budget is

\[
\sum_i u_i\le B,
\qquad B=0.12.
\]

If desired control exceeds the budget, it is allocated according to

\[
w_i
=
\exp[-8(x_i-f_i)]
\left[0.15+\max(y_i-x_i,0)\right],
\]

\[
u_i=B\frac{w_i}{\sum_jw_j}.
\]

Both configurations are stepped with forward Euler at

\[
\Delta t=0.01,
\qquad
T=150,
\]

using the sweep

\[
\kappa\in
\{0,0.02,0.05,0.10,0.15,0.25,0.40,0.80\}.
\]

The implementation computes the unclipped next state before applying \([0,1]^3\) bounds and records every step and coordinate on which clipping would alter the trajectory.

The outcome measures are

\[
M_{\min}=\min_{t,i}(x_i(t)-f_i),
\]

\[
J_u=\int_0^T\sum_i u_i(t)\,dt,
\]

and late target RMSE over \(t\ge130\).

## B.4 Configuration I: homogeneous floors and differentiated tracking

The first configuration retains C.1's parameters:

\[
f=(0.24,0.24,0.24),
\qquad
x(0)=(0.72,0.72,0.72),
\]

\[
s=(0.065,0.055,0.060),
\qquad
d=(0.11,0.09,0.10).
\]

Before \(t=100\), the target is

\[
y^{(0)}=(0.75,0.72,0.70),
\]

and it then shifts asymmetrically to

\[
y^{(1)}=(0.88,0.56,0.78).
\]

The deterministic disturbances are

\[
\xi(t)=
\begin{cases}
(-0.075,0,0),&20\le t<28,\\
(-0.035,-0.055,-0.025),&50\le t<60,\\
(0,0,-0.100),&82\le t<88,\\
(0,0,0),&\text{otherwise}.
\end{cases}
\]

Because the floors are homogeneous, a unique binding component is also a minimum-state component and is therefore at or below the mean. This explains why the direct diffusive term is favorably signed at a fixed state. It does not prove the finite-trajectory sweep result.

## B.5 Configuration I results

| \(\kappa\) | Minimum viability margin | Total control cost | Late tracking RMSE |
|---:|---:|---:|---:|
| 0.00 | 0.2811715052 | 7.1992430737 | 0.0467393362 |
| 0.02 | 0.2849524361 | 7.2709721099 | 0.0566120419 |
| 0.05 | 0.2902537462 | 7.3530511929 | 0.0685386360 |
| 0.10 | 0.2982139959 | 7.4472332460 | 0.0824069720 |
| 0.15 | 0.3052341325 | 7.5103262408 | 0.0916364861 |
| 0.25 | 0.3170137752 | 7.5890867215 | 0.1030533350 |
| 0.40 | 0.3305262552 | 7.6530593363 | 0.1123240184 |
| 0.80 | 0.3527559814 | 7.7238403844 | 0.1228401182 |

Across this declared sweep, minimum margin, control cost, and late differentiated tracking error all strictly increase. All controller runs remain viable. Their margins lie between approximately \(0.281\) and \(0.353\), so this sweep demonstrates redistribution of slack well inside the viable region; it does not demonstrate coupling-mediated rescue from failure.

A separate no-controller reference at \(\kappa=0\) crosses the floor at \(t=26.76\), reaches a minimum margin of \(-0.1009342470\), and remains viable for approximately \(95.69\%\) of sampled time points. This reference shows that the declared disturbance schedule can produce failure without control, but it is not part of the coupling sweep.

No clipping operation is active in any controller run.

## B.6 Configuration II: a specialized high-requirement component

The second configuration reverses the relevant geometry while retaining the same controller and coupling law:

\[
f=(0.10,0.10,0.82),
\qquad
x(0)=(0.60,0.60,0.90),
\]

\[
s=(0.18,0.18,0.036),
\qquad
d=(0.30,0.30,0.04).
\]

The uncoupled natural equilibrium is

\[
x^*=s/d=(0.60,0.60,0.90),
\]

which is also the constant target. The third component has the highest state but only \(0.08\) of slack above its floor. A disturbance

\[
\xi(t)=(0,0,-0.020)
\qquad
40\le t<50
\]

acts on that component. Because the third component is binding while remaining above the mean, positive coupling drains it toward the two low-requirement components.

## B.7 Configuration II results

| \(\kappa\) | Minimum viability margin | Viable over full horizon | First failure time | Direct coupling term at minimum |
|---:|---:|:---:|---:|---:|
| 0.00 | 0.0431278138 | Yes | — | 0.0000000000 |
| 0.02 | 0.0369053152 | Yes | — | -0.0033499396 |
| 0.05 | 0.0285644110 | Yes | — | -0.0078440606 |
| 0.10 | 0.0167977155 | Yes | — | -0.0141911234 |
| 0.15 | 0.0070877984 | Yes | — | -0.0194345846 |
| 0.25 | -0.0080077450 | No | 42.01 | -0.0275950011 |
| 0.40 | -0.0237919344 | No | 40.20 | -0.0361348902 |
| 0.80 | -0.0470145357 | No | 0.84 | -0.0487013205 |

The margin strictly decreases across the sweep and crosses zero between \(\kappa=0.15\) and \(\kappa=0.25\). At \(\kappa=0.25\) and \(0.40\), the disturbance precipitates the recorded breach. At \(\kappa=0.80\), coupling alone drains the high-floor third component below its floor before the disturbance begins.

No clipping operation is active in any run. This configuration establishes a model-specific counterexample to the universal claim that stronger diffusive integration improves viability. It does not establish that biological integration generally destroys viability.

## B.8 Joint interpretation

The two configurations use the same coupling operator:

\[
\kappa(\bar x-x_i).
\]

Yet their viability trends are opposite. The relevant difference is not an intrinsic moral or biological value carried by coupling. It is the declared organization of floors, states, targets, control, disturbances, and horizon.

The supported conclusion is therefore:

> Diffusive coupling redistributes state toward a mean. Whether that redistribution supports or undermines viability depends on which components are binding and on the larger controlled trajectory.

The models do not show that intermediate coupling is universally optimal. They show why an empirical study must declare the candidate unit, protected floors, disturbance class, controller, costs, and horizon before interpreting “integration.”

## B.9 Step-size sensitivity and clipping audit

The complete sweeps were repeated at four forward-Euler step sizes.

| \(\Delta t\) | Configuration I margin at \(\kappa=0\) | Configuration I margin at \(\kappa=0.80\) | Configuration II margin at \(\kappa=0\) | Configuration II margin at \(\kappa=0.80\) | Declared trends preserved |
|---:|---:|---:|---:|---:|:---:|
| 0.040 | 0.2810250082 | 0.3527054405 | 0.0431206323 | -0.0470207782 | Yes |
| 0.020 | 0.2811225312 | 0.3527390630 | 0.0431254019 | -0.0470166205 | Yes |
| 0.010 | 0.2811715052 | 0.3527559814 | 0.0431278138 | -0.0470145357 | Yes |
| 0.005 | 0.2811960446 | 0.3527644672 | 0.0431290265 | -0.0470134917 | Yes |

At every tested step size, Configuration I's minimum margin increases across all eight couplings and Configuration II's minimum margin decreases across all eight. Configuration I's cost and late tracking error retain their reported increasing directions. The \(\kappa=0\) viable and \(\kappa=0.25\) nonviable classification in Configuration II is also preserved.

The clipping counter is zero in every default and step-size-sensitivity controller run. Thus the sign reversal is not created by saturation at the numerical bounds.

## B.10 Reproducibility and limitation

The accompanying script `CU_Biology_C1_1_reproducibility.py` generates `CU_Biology_C1_1_verification_results.json`. It contains no stochastic sampling. Regression checks assert both sweep directions, the adverse viability crossing, the pointwise sign recorded at each adverse minimum, step-size robustness, and zero clipping.

The sensitivity checks do not prove convergence of every trajectory feature. More importantly, exact reproduction of these numbers establishes only that the outputs follow from the declared equations. It provides no empirical validation of CU Biology.

# Supplement C. Claim and evidence ledger

## C.1 Purpose

The ledger prevents a conceptual synthesis from being mistaken for a uniform body of evidence. Evidence grades follow Section 12.13.

| ID | Claim | Status | Evidence grade | Scope / condition |
|---|---|---|---|---|
| BIO-C1 | Living systems characteristically exhibit active self-maintenance rather than passive persistence alone. | Bridge principle | E3–E4 | Requires operational boundary and intervention in each case. |
| BIO-C2 | One universal scalar \(C=A I\) measures biological coherence. | Retired | — | No cross-system derivation or calibration. |
| BIO-C3 | A biological coherence profile may include viability, resilience, integration, closure, adaptive reach, continuity, and cost. | Definition / proposal | E0 | Components require domain-specific measures. |
| BIO-C4 | Viability is a trajectory property and can be represented by viability kernels. | Imported formalism / bridge | E1–E3 | Model-specific dynamics and controls. |
| BIO-C5 | Endogenous maintenance can be assessed through intervention and ablation. | Methodological proposal | E0–E3 | Confounding and collateral damage must be controlled. |
| BIO-C6 | Biological individuality is multidimensional and may be nested. | Empirical generalization | E3–E4 | Boundary, physiology, reproduction, and evolution can disagree. |
| BIO-C7 | Organism-relative stake follows from viability-bearing organization and endogenous regulation. | Bridge principle | E0–E3 | Does not imply feeling or moral status. |
| BIO-C8 | Life violates or reverses the second law. | Rejected | — | Open-system entropy accounting applies. |
| BIO-C9 | Biological coherence equals low entropy. | Rejected | — | Entropy and functional organization are distinct. |
| BIO-C10 | Maintenance has a universal energetic lower bound proportional to coherence. | Retired | — | Process-specific thermodynamic bounds may exist. |
| BIO-C11 | Abiogenesis is one universal phase transition. | Retired as universal claim | E0 | Specific models may exhibit transitions. |
| BIO-C12 | Abiogenesis can be decomposed into coupled autonomy transitions. | Research architecture | E0–E3 | Boundary, energy, closure, regulation, heredity, viability, evolvability. |
| BIO-C13 | Recurrence dominance is sufficient for life. | Disproved | E1 | Passive Markov counterexample. |
| BIO-C14 | Autocatalytic closure is relevant but not sufficient for life. | Imported result / synthesis | E1–E3 | Needs boundary, regulation, heredity, and/or viability. |
| BIO-C15 | Morphogenesis is multiscale control under constraints. | Bridge principle | E2–E4 | Requires comparative causal models. |
| BIO-C16 | Transient bioelectric perturbation can alter later planarian polarity. | Imported empirical result | E2 | Species-, treatment-, and timing-specific. |
| BIO-C17 | Bioelectricity is a universal anatomical master code. | Not established | — | Requires cross-system evidence and mechanism. |
| BIO-C18 | Xenopus cell constructs display reconfigurable collective capacities. | Imported empirical result | E2 | Laboratory-scaffolded; no consciousness inference. |
| BIO-C19 | Biological agency is graded. | Analytic framework | E0–E4 | Levels need operational tests. |
| BIO-C20 | Neural tissue is necessary for every form of learning. | Rejected | E2–E3 | Single-cell habituation-like learning has empirical support. |
| BIO-C21 | Basal learning implies consciousness. | Not established | — | Requires separate consciousness criteria. |
| BIO-C22 | Fitness is identical with biological coherence. | Rejected | — | Fitness and organization can diverge across scales. |
| BIO-C23 | Selection can stabilize regulatory architectures. | Empirical generalization | E3–E4 | Conditional on costs, environments, and selection level. |
| BIO-C24 | Evolution universally increases complexity or coherence. | Rejected | — | Simplification, extinction, and parasitism are common possibilities. |
| BIO-C25 | Major transitions involve cooperation plus integration and conflict mediation. | Imported synthesis | E3–E4 | Mechanisms vary by transition. |
| BIO-C26 | Cancer can be modeled partly as local–global regulatory decoupling. | Bridge hypothesis | E1–E3 | Supplements rather than replaces molecular oncology. |
| BIO-C27 | Bioelectric recoupling will normalize every cancer. | Rejected | — | Evidence is model-specific. |
| BIO-C28 | Aging is contraction or reshaping of recoverable trajectories. | Bridge hypothesis | E0–E3 | Multidimensional and not strictly monotonic. |
| BIO-C29 | Death is \(C=0\). | Retired | — | Replaced by intervention-relative irrecoverable organismal failure. |
| BIO-C30 | Nonbiological systems could in principle instantiate self-maintenance and stake. | Possibility claim | E0–E1 | Depends on architecture; not yet a claim about current LLMs. |
| BIO-C31 | Current frontier LLM instances are living organisms. | Rejected in present architecture | E2 | Maintenance, energy, reproduction, and identity remain externally supplied. |
| BIO-C32 | Intelligence, life, consciousness, selfhood, and responsibility are distinct. | Cross-domain principle | E0–E3 | To be refined in Consciousness and AI. |
| BIO-C33 | The CU profile will improve biological prediction. | Open empirical hypothesis | E0 | Must be tested against strong baselines. |
| BIO-C34 | Life is sacred. | Commitment | — | Not a biological derivation. |
| BIO-C35 | Life is matter organized so continuation becomes causally relevant to present activity. | Interpretation | E0–E3 | Naturalized teleonomy; no foresight implied. |
| BIO-C36 | For a unique binding component under diffusive mean coupling, the direct instantaneous contribution to minimum margin is \(\kappa(\bar x-x_j)\). | Formal result | E1 | Local directional statement; does not determine global finite-trajectory monotonicity. |
| BIO-C37 | Stronger diffusive integration universally improves biological viability. | Disproved as a universal claim | E1 | The heterogeneous-floor configuration supplies a deterministic counterexample; empirical direction remains system-specific. |

## C.2 Literature-audit boundary

The literature review is selective. It prioritizes representative primary results and major formal traditions relevant to the reconstruction. It is not a systematic review, meta-analysis, or complete survey of origin-of-life, developmental, evolutionary, cancer, aging, or basal-cognition research.

---

# Supplement D. Biology Principle Crosswalk and B.3 Synchronization

## D.1 Status rule

Metaphysics and Epistemology v0.10 and Foundations v0.10 provide the framework definitions and governance rules. CU Biology owns the detailed content of CU-B1 through CU-B5. “Domain authority” means that these are the controlling CU formulations for biological use; it does not convert bridge principles or conditional empirical claims into universal laws.

## D.2 CU-B1 — Active Biological Self-Maintenance

**Authority class:** Domain authority  
**Claim status:** DOMAIN AUTHORITY

> A candidate living organization is not distinguished by static order or persistence alone, but by a relatively closed network of materially realized processes and constraints whose endogenous activity contributes to maintaining, repairing, reproducing, or adaptively transforming the conditions of that network's continuation. Degree and kind of autonomy are relative to a boundary, environment, perturbation class, and horizon.

**Disposition:** The audited domain registry supplies the current wording and scope. Consolidation preserves domain ownership and prevents the B.2 placeholder from governing the mature paper.

## D.3 CU-B2 — Adaptive Problem Solving Beyond Fixed Programs

**Authority class:** Domain authority  
**Claim status:** DOMAIN AUTHORITY

> Some living systems possess regulatory architectures that generalize beyond fixed stimulus–response mappings: they detect deviations, recruit alternative pathways, modify future responses from history, and solve novel viability-relevant problems within a bounded adaptive reach. Degree must be established through counterfactual flexibility, learning controls, and comparison with passive or preprogrammed alternatives; it does not by itself establish consciousness.

**Disposition:** The audited domain registry supplies the current wording and scope. Consolidation preserves domain ownership and prevents the B.2 placeholder from governing the mature paper.

## D.4 CU-B3 — Multiscale Constraint and Local Process

**Authority class:** Domain authority  
**Claim status:** DOMAIN AUTHORITY

> Biological form and function arise through local physical processes embedded in cross-scale boundary conditions, signaling networks, mechanical relations, and histories. A higher-scale constraint is explanatory when intervention on its realizing relations changes lower-scale trajectories in a way that improves prediction or control beyond local variables alone. Higher scale does not imply a new force, and global stability does not imply a unique optimizer.

**Disposition:** The audited domain registry supplies the current wording and scope. Consolidation preserves domain ownership and prevents the B.2 placeholder from governing the mature paper.

## D.5 CU-B4 — Structured Evolutionary Possibility and the Stabilization of Regulatory Architecture

**Authority class:** Domain authority  
**Claim status:** DOMAIN AUTHORITY

> Evolutionary processes explore a structured and nonuniform possibility space shaped by mutation bias, genotype–phenotype relations, developmental dynamics, physical feasibility, ecological interaction, inheritance, and historical path dependence. Selection nonrandomly changes the frequencies of heritable variants relative to local reproductive consequences. Recurrent constraints can make some forms, functions, and regulatory architectures repeatedly accessible, contributing to convergence, while chance, drift, conflict, changing environments, and historical contingency preserve multiple possible trajectories. Evolution can stabilize, modify, simplify, or dismantle coherent self-maintaining organization; it does not thereby maximize coherence, complexity, consciousness, or moral value.

**Disposition:** The audited domain registry supplies the current wording and scope. Consolidation preserves domain ownership and prevents the B.2 placeholder from governing the mature paper.

## D.6 CU-B5 — Biological Individuation and Stake

**Authority class:** Domain authority  
**Claim status:** DOMAIN AUTHORITY

> A biological individual is a historically continuous, relatively bounded organization whose components are causally integrated into maintaining, repairing, reproducing, or adaptively transforming the conditions of that organization. The organization thereby establishes organism-relative stakes: conditions can be better or worse for it in virtue of their effects on its continued self-maintenance. Individuality is graded, multidimensional, and potentially nested; organism-relative stake does not by itself establish consciousness or moral status.

**Disposition:** The audited domain registry supplies the current wording and scope. Consolidation preserves domain ownership and prevents the B.2 placeholder from governing the mature paper.

## D.7 Framework gateway

CU-D3 is a cross-reference gateway to CU-B1. Applications must specify boundary, environment, perturbation class, endogenous maintenance processes, viability conditions, and horizon rather than treating “biological self-maintenance” as a free-standing universal dynamic.

## D.8 Downstream constraints

Later domains inherit the following boundaries:

- organism-relative stake does not by itself establish phenomenal valence or moral standing;
- learning and adaptive problem solving do not by themselves establish consciousness;
- biological integration does not supply a universal scalar for psychology or society;
- evolutionary selection is not a moral optimizer;
- designer optimization, as-if analysis, and evolutionary selection must remain distinct.

---

# Supplement E. Change ledger from the March 2026 manuscript and C.1 audit

| Legacy element or audit finding | this paper disposition | Reason |
|---|---|---|
| Biology as coherence under constraint | Retained with operational restrictions | Central integrative question remains useful. |
| \(C(x)=A(x)I(x)\) as universal functional | Retired as universal; permitted as declared model | No unique derivation, units, or cross-system calibration. |
| Accessibility as aggregate constraint satisfaction | Recast as viability and control variables | “Accessibility” conflicted with Physics and hid measurement choices. |
| Integration \(I=(\gamma SR)^{1/3}\) | Retired as canonical | Coupling, synergy, and robustness are distinct and model-specific. |
| Universal biological coherence gradient | Retired | No universal scalar or state-space metric. |
| Organisms ascend coherence landscapes | Recast as model-relative control, adaptation, or selection | Avoids as-if optimization becoming mechanism. |
| Constraint manifold \(K_t\) as identity | Replaced by viability sets plus historical causal continuity | Small distance is neither necessary nor sufficient for token identity. |
| Death as \(C=0\) | Retired | Death is multiscale and intervention-relative. |
| Sharp universal coherence-collapse threshold | Restricted | Threshold language requires a specific model and signature. |
| Maintenance cost \(E\ge\lambda C\) | Retired | No universal conversion between energy and profile. |
| Coherence efficiency \(C/\Phi\) | Retired | Costs and benefits form model-specific tradeoffs. |
| Abiogenesis as one coherence phase transition | Reconstructed as coupled autonomy transitions | Life-like capacities can emerge separately. |
| Recurrence dominance criterion | Disproved as sufficient | Passive Markov systems satisfy it. |
| Thermodynamics shows life “counteracts entropy” | Rewritten with open-system entropy balance | Avoids conflict with Physics v0.10. |
| Structured dissipation as explanation of life | Narrowed to necessary background | Dissipation does not supply closure, heredity, or agency. |
| Coherence drive | Replaced by identifiable feedback and policy mechanisms | Prevents metaphor from replacing causal explanation. |
| Morphogenesis as global optimization | Recast as multiscale control hypothesis | Requires interventionally discriminating models. |
| Bioelectric patterns as universal integration carrier | Restricted to supported systems and pathways | Evidence is strong in cases, not universal. |
| Planarian regeneration as attractor re-entry | Retained as model option | Attractor must be demonstrated; target set may be more appropriate. |
| Xenobots as validation of CU | Recast as contrast cases | They show reconfigurable cell capacities under scaffolding. |
| Cancer as coherence disintegration | Recast as multilevel evolution and regulatory decoupling | Supplements rather than replaces oncology. |
| Simulation “validates” coherence dynamics | Replaced by deterministic pedagogical counterexample | A toy model cannot validate biology. |
| Positive margin trend in the original toy configuration | Retained but explicitly marked configuration-dependent | Homogeneous floors make a binding component a minimum-state component, favoring a nonnegative direct diffusive contribution. |
| Adverse effect of integration on viability | Added as a heterogeneous-floor configuration | The same coupling law drains a specialized high-requirement component and crosses its viability floor. |
| Numerical clipping | Audited and recorded as inactive | No default or step-size-sensitivity controller run activates the clip operation. |
| Five biological claim-governance rules | Moved from JSON into §2.7.1 | A rule governing scientific claims must appear in the manuscript, not only in package metadata. |
| *Stentor* learning characterization | Expanded within the source's scope | Records the counterintuitive protein-synthesis result and persistence across cell division without inferring consciousness. |
| Optimization language | Supplement A.18 exported as a downstream corpus rule | Designer choice, as-if analysis, and evolutionary selection must not be conflated. |
| Evolution as coherence flow | Retired | Fitness, drift, constraints, and selection levels must remain explicit. |
| Fitness as coherence persistence | Rejected | Fitness and maintenance diverge. |
| Convergence proves constrained coherence landscape | Narrowed | Convergence supports constraints but coexists with contingency. |
| Major transitions as coherence reorganization | Retained with established transition criteria | Cooperation, integration, conflict mediation, heredity. |
| Minimal biological epistemology | Retained in instrumental, non-propositional form | Signals gain significance through viability-relevant use. |
| Artificial systems externalize costs | Retained as a measurable boundary claim | Must report infrastructure and maintenance support. |
| Life is intrinsically sacred | Moved to commitment register | Not derivable from biology. |
| Biology completes abiogenesis | Withdrawn | Origins remain open and experimentally developing. |

## E.1 Preserved conceptual contributions

The following achievements of the original paper survive:

- biological identity as persistence through change rather than material sameness;
- multi-scale organization and local–global conflict;
- repair, regeneration, and path dependence;
- the importance of bioelectric and other non-genetic control layers;
- basal agency and problem solving;
- synthetic systems as contrast cases;
- falsifiability as a framework obligation; and
- life as a central bridge between physical persistence and later mind.

Their claim strength and formal expression have changed.

---

# Supplement F. Figure and experiment program

## F.1 Figure 1 — From physical persistence to biological self-maintenance

A four-panel diagram:

1. passive stable structure;
2. open dissipative structure;
3. regulated organization with endogenous repair;
4. reproducing and evolving organization.

Arrows should be labeled as candidate autonomy transitions, not a guaranteed historical sequence.

## F.2 Figure 2 — Biological coherence profile

A radar or parallel-coordinate display of

\[
(M_T,R_T,I_{G,T},O_T,A_T,H_T;J_T)
\]

for several systems. The caption must warn that axes are separately normalized and no enclosed area is a canonical coherence score.

## F.3 Figure 3 — Nested individuality

A multilayer graph showing organelle, cell, tissue, organism, symbiont, and environment, with different edge types for metabolism, regulation, reproduction, and historical continuity. Overlapping rather than perfectly nested boundaries should be visible.

## F.4 Figure 4 — Autonomy-transition matrix

Rows: vesicle, autocatalytic set, regulated protocell, minimal cell, bacterium. Columns: boundary, energy, closure, regulation, heredity, viability, evolvability. Use confidence or evidence grades rather than binary checks.

## F.5 Figure 5 — Multiscale morphogenesis

Couple gene-regulatory, biochemical, mechanical, bioelectric, and tissue-geometry layers. Intervention arrows should show which layers are manipulated and which downstream outputs are measured.

## F.6 Figure 6 — Agency ladder

Display A0–A5 with explicit non-implication arrows:

\[
\text{learning}\not\Rightarrow\text{consciousness},
\qquad
\text{stake}\not\Rightarrow\text{moral agency}.
\]

## F.7 Figure 7 — Major transition in individuality

Show independent lower-level reproducers becoming a collective with bottleneck, division of labor, conflict control, and collective heredity. Include the possibility of reversal or stable plural individuality.

## F.8 Figure 8 — Cancer as scale conflict

Show cell-level maintenance and reproduction increasing while tissue and organism profiles deteriorate. Avoid a moralized image of “selfish cells”; label the mechanisms.

## F.9 Figure 9 — Configuration-dependent coupling effects

Plot the two configurations in separate, clearly labeled panels. For Configuration I, plot coupling against minimum margin, tracking error, and control cost without combining the axes into one score. For Configuration II, plot coupling against minimum margin, mark the zero-margin boundary, and identify the first nonviable sweep point. The figure is pedagogical, not empirical.

## F.10 Experiment templates

Each empirical figure should include:

- system boundary;
- intervention and sham;
- local-damage control;
- time course;
- target outcome;
- external cost accounting;
- alternative causal graph; and
- preregistered narrowing condition.

---

# Supplement G. Selective Literature Ledger

**Purpose:** Map representative external sources to the precise claims they support in C.1.1. This is not a systematic review or evidence-certainty assessment.

| Topic | Representative source | What C.1.1 imports | What C.1.1 does not infer |
|---|---|---|---|
| Autopoiesis | Varela, Maturana, & Uribe (1974) | Self-production and boundary constitution as central organizational ideas | That autopoiesis is the universally accepted necessary-and-sufficient definition of life |
| Closure of constraints | Mossio, Saborido, & Moreno (2009); Montévil & Mossio (2015) | Biological functions and organization can be analyzed through mutually maintaining constraints | That graph closure alone is sufficient for life or biological individuality |
| Autocatalytic sets | Hordijk, Kauffman, & Steel (2011) | Catalytically closed reaction subsets can emerge under declared chemical-reaction-system assumptions | That autocatalysis supplies boundary, heredity, regulation, or open-ended evolution by itself |
| Autonomy and evolution | Ruiz-Mirazo, Peretó, & Moreno (2004) | Autonomy and open-ended evolution are distinguishable, jointly important dimensions of life | That one operational threshold has been established for all possible life |
| Active inference | Friston (2013) | Markov-blanket and variational formulations provide one formal model family for self-organization | That every living system literally performs one universal variational computation |
| Thermodynamic replication claims | Kolchinsky (2024) | Universal growth/decay bounds cannot be inferred from dissipation without additional kinetic structure | That thermodynamics is irrelevant to biological maintenance |
| Bioelectric regeneration | Durant et al. (2019) | Early transient membrane-potential interventions can alter later planarian polarity in the stated preparation | A universal electrical blueprint, conscious tissue-level body image, or species-general master code |
| Hybrid morphogenesis | Cortés-Poza (2026) | A contemporary example couples bioelectric, regulatory, adaptive, and memory variables in one morphogenetic model | Empirical validation of CU or uniqueness of that model family |
| Reconfigurable organisms | Kriegman et al. (2020, 2021) | Living cells can be reconfigured into novel collectives, including a scaffold-dependent case of kinematic replication | Full autonomous reproduction, open-ended evolution, or a consciousness claim |
| Robust perfect adaptation | Aoki et al. (2019) | Antithetic integral feedback can implement robust perfect adaptation under specified synthetic-biological conditions | A universal controller for all biological regulation |
| Feedback limits | Dufour et al. (2014) | Biological control faces response–adaptation–noise tradeoffs | That one tradeoff surface applies across taxa and control architectures |
| Single-cell learning | Rajan et al. (2026) | In *Stentor coeruleus*, protein-synthesis inhibition accelerated habituation and prolonged retention; habituation memory persisted in progeny after division; the authors link response recovery to new protein synthesis and memory formation to modification of existing mechanoreceptor machinery through calcium signaling and phosphorylation | Reflective cognition, human-like representation, consciousness, or a general theory of transgenerational cognition |
| Evolutionary transitions | Maynard Smith & Szathmáry (1995); West et al. (2015) | New levels of individuality involve cooperation, dependence, conflict mediation, and relocation of fitness-relevant organization | A predetermined ladder or universal progress toward complexity |
| Ecological scaffolding | Doulcier et al. (2024) | Collective traits can be initiated by ecological scaffolds and stabilized through hysteresis in a declared model | That all transitions follow this route or that “Goldilocks” has one universal quantitative meaning |
| Cancer evolution | Ciriello et al. (2024) | Tumors involve genetic and non-genetic evolution, ecology, immune interaction, and treatment selection | That cancer reduces to one scale-conflict variable |
| Bioelectric tumor models | Chernet et al. (2016); Chernet, Fields, & Levin (2015) | Ion-channel, membrane-potential, and gap-junction interventions can causally modify tumor-like outcomes in amphibian models | Clinical efficacy, universality across tumors, or replacement of molecular oncology |
| Synthetic protocells | Shi et al. (2025); Giessler et al. (2026) | Energy-driven phase behavior and genetically encoded droplet cycles provide modular tests of life-like capacities | A fully autonomous life cycle or open-ended evolution |
| Pre-genetic regulation | Shirt-Ediss et al. (2025) | Models can test how regulation and agency-like behavior arise in evolving protocell ecologies | Empirical demonstration that prebiotic systems historically followed the modeled route |

## Audit notes

The independent C.1 audit verified the bibliographic existence and basic scope of Rajan et al. (2026), Cortés-Poza (2026), and Giessler et al. (2026). It did not verify the remaining references. C.1.1 independently rechecked the Rajan abstract and publication metadata before expanding the manuscript's description.

## Audit rule

Whenever a later version strengthens one of these claims, it must either add stronger evidence or change its claim-status label. Representative evidence must not be treated as exhaustive evidence, and a successful example must not be promoted to a universal law.

# Supplement H. Reproducibility and Verification Record

## H.1 Scope

The deterministic model compares two declared three-variable configurations under the same diffusive coupling form. It is pedagogical, not fitted to biological data, and not evidence for a universal biological optimum.

## H.2 Primary configuration endpoints

At coupling 0.00, the minimum viability margin is 0.2811715052; at coupling 0.80, it is 0.3527559814. Across the declared sweep, margin, control cost, and differentiated tracking error increase together. Every controller run remains viable.

## H.3 Adverse configuration endpoints

At coupling 0.00, the minimum viability margin is 0.0431278138; at coupling 0.80, it is -0.0470145357. The margin decreases across the declared sweep and crosses below zero. The direction reversal demonstrates configuration dependence rather than a law that coupling is good or bad in itself.

## H.4 Numerical controls

The archived suite repeats both sweeps at four forward-Euler step sizes and records clipping before state bounds are applied. Clipping remains inactive in every declared controller and sensitivity run. The executable script, pinned NumPy version, generated JSON, and integrity records accompany this supplement.

---

# Supplement I. Independent Audit and Editorial Provenance

The independent audit reproduced the original deterministic calculations and recommended adoption with bounded repairs. The publication authority incorporates those repairs:

- the local directional effect of coupling is separated from finite-trajectory monotonicity;
- the favorable homogeneous-floor configuration is identified as structurally predisposed toward support of the binding component;
- an adverse heterogeneous-floor configuration is included;
- clipping is measured and shown inactive;
- the five claim-governance rules appear in the manuscript body;
- the *Stentor* description is expanded within the cited source's scope.

The audit did not constitute comprehensive peer review of the life criterion, organizational closure, philosophy of biological individuality, morphogenesis, cancer, aging, all candidate principles, or the complete bibliography. The full independent audit, response, change ledger, patch, authority manuscript, code, and generated outputs are preserved in the publication package.

---

# Supplement J. Editorial and Source Map

The reader-facing manuscript is an editorial transformation of the frozen C.1.1 authority manuscript under the CU v0.10 Publication-Prose Architecture. The transformation:

- preserves the thirteen-section scientific argument;
- updates authority references from B.2 to B.3 / Version 0.10;
- replaces reconstruction narration with direct exposition;
- moves formal appendices, full ledgers, audit history, and figure planning into this supplement;
- records CU-B1 through CU-B5 as Biology-owned domain authorities;
- retains the complete historical record in the archive.

Where a substantive discrepancy is found, the frozen C.1.1 authority controls the pre-publication scientific content until the discrepancy is resolved and recorded in a later candidate.

---


# Supplement K. Structured Evolutionary Possibility Source Map

## K.1 Purpose

This supplement records the evidence boundary for the publication-candidate expansion of Section 9.

## K.2 Source-to-claim map

| Source | Supported claim | Not inferred |
|---|---|---|
| Schaper & Louis (2014) | Biased genotype–phenotype frequency can steer arrival and fixation in an RNA model | Universal dominance of production bias over selection |
| Herrera-Álvarez et al. (2025) | Reconstructed ancestral genotype–phenotype maps were anisotropic, heterogeneous, and causally steered lineage-specific functional evolution | That every molecular map has the same geometry |
| Huang et al. (2005) | Neutrophil differentiation trajectories supported a high-dimensional attractor interpretation | That all development is gradient flow or one Waddington landscape |
| Rohner et al. (2022) | Beetle horn developmental variation aligned with plastic and evolutionary divergence | Universal developmental constraint on all morphology |
| Losos et al. (1998) | Similar ecomorphs evolved independently in replicated island radiations | Inevitability of one adaptive outcome |
| Travisano et al. (1995) | Replicates converged in fitness while chance and history influenced cell size | That convergence or contingency always dominates |
| Blount et al. (2008) | A key innovation depended on historical potentiation | That all novelty requires the same sequence of enabling changes |
| Simões et al. (2019) | Experimental populations broadly converged while retaining trait differences and transient divergence | Complete convergence under every shared environment |
| Storz et al. (2019) | Mutation bias contributed to molecular convergence in avian hemoglobin adaptation | That mutation is directed toward adaptive need |

## K.3 Three uses of attractor language

1. **Developmental attractor:** trajectories of one developmental or regulatory dynamical system converge toward a state or regime.
2. **Adaptive basin:** population or trait dynamics move toward a local evolutionary regime under declared ecology and inheritance.
3. **Convergent recurrence:** independent histories produce similar outcomes; this need not be a literal attractor.

These terms must not be collapsed.

## K.4 Status of CU-B4 refinement

The revised CU-B4 is a domain-authority conditional empirical generalization proposed for synchronization into the Foundations registry after authorial approval of Biology PC2. It does not create a universal law of progress.

# Supplement L. Licensed Commitments Architecture

The reader-facing Section 13 follows the corpus-wide Licensed Commitments Architecture RC1. Its sacredness claim is commitment-register content constrained by the biological record. The section does not infer consciousness, equal moral standing, or inviolability from life alone.


# Commitment Principle Crosswalk

CU-COM8 — **Reverence for Life and Biospheric Care** is the official commitment anchor for the reader-facing manuscript.

**Statement:** Coherence Universalism commits to receiving all life as sacred: each living being is a historically formed, vulnerable organization in which material processes contribute to maintaining a particular continuation. This commitment supports care for organisms, biodiversity, and the biosphere.

**Boundary:** The commitment does not make predation and death cosmic errors, prohibit medicine or agriculture, equalize every obligation, or treat evolution as morally good.

**Revision condition:** Applications must change when they romanticize nature, erase conflict and suffering, ignore ecological tradeoffs, or misuse sacredness against necessary care and intervention.
