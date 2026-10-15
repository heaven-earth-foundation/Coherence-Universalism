# COHERENCE UNIVERSALISM: PHYSICS
## Coherence, Accessibility, and the Ordered Emergence of Physical Description

**Gaura Kiśora Dās Rader**  
**Heaven≡Earth Foundation**  
**White Paper Series**

**Version 0.10**  
**October 2026**

**Release status.** This manuscript is part of the complete Version 0.10 proposal. Numbered principles identify the framework’s current formulations; their claim status, external validation, and authorization for consequential application remain separate questions.

**Freeze status.** This manuscript is synchronized to the frozen Version 0.10 release registry, evidence package, and review gates. Future changes require a new versioned release.

---

# Abstract

Coherence Universalism proposes that physical description is organized by two ideas more basic than any particular effective theory: **coherence**, understood as integrated relational organization under constraint, and **accessibility**, understood as the portion of that organization available within a given subsystem, scale, or mode of observation. This paper develops that proposal as a layered research program rather than as a completed derivation of known physics.

The first layer is logical. Pure relational structure permits partial separability; partial separability permits comparisons among configurations; lawful transition relations permit ordered histories; and ordered histories permit temporal parameterization. The paper distinguishes temporal order from the arrow of time: order requires consistent precedence relations, whereas an arrow additionally requires directed irrecoverability or an asymmetric effective law.

The second layer is mathematical. A four-state probability simplex supplies a controlled classical sandbox. The quantity

\[
D(p)=\sum_{i=1}^{4}\left(p_i-\frac14\right)^2
\]

measures statistical differentiation from the uniform distribution, while Shannon entropy measures spread. The paper gives self-contained derivations of their Euclidean and Fisher-natural gradients, their opposition through Jeffreys divergence or Fisher covariance, the exact finite-step change in \(D\), and the conditions under which \(D\) and entropy can locally increase together. Its finite-partition analysis separates three distinct operations: projection to coarse block masses, Shannon’s grouping decomposition, and block-uniform reconstruction on the original state space. The quadratic between/within identity is a rescaled instance of the established generalized-entropy \(GE(2)\) decomposition tradition, not a novel CU theorem; the accessibility interpretation and the separation of the three operations are the paper’s contribution. Under block averaging, differentiation loss is exactly the within-block Euclidean residual, while entropy gain is exactly a weighted Kullback–Leibler divergence from within-block uniformity. The two quantities vanish together but are not equal. The joint-growth wedge is further shown to collapse exactly on nonuniform states with only two distinct probability values; global bounds for the Fisher fields are obtained on the closed simplex. At fixed coupling \(r=\beta/\alpha\), the nonuniform stationary points are the finite subset of those two-level states satisfying \(r=2(a-b)/\log(a/b)\); none exist for \(r>0.6213609436\ldots\). The uniform state changes linear stability at \(r=1/2\), although at the exactly critical value it is nonhyperbolic and neither a local maximum nor a local minimum. These results concern differentiation, entropy, and accessibility—not yet substantive physical coherence.

The third layer concerns quantum theory. Classical probability can represent correlations hidden by marginalization, so hidden correlation alone does not force a quantum state space. A stronger route is proposed: mixed local states may be restrictions of globally pure states, effective irreversible processes may admit globally reversible dilations, and access contexts may fail to admit a single classical joint refinement. Purification and contextual accessibility are therefore offered as CU-motivated bridge principles. Together with the five informational axioms of Chiribella, D’Ariano, and Perinotti, the purification postulate conditionally selects finite-dimensional complex quantum theory within their operational-probabilistic framework (Chiribella, D’Ariano, & Perinotti, 2011). Within quantum theory, purity, basis coherence, total correlation, and entanglement are kept distinct. A two-qubit construction shows exactly how basis coherence can be converted into bipartite entanglement.

The fourth layer is dynamical. Once temporal parameterization is available, a second-order Lagrangian dynamics on a Fisher–Rao state space provides the proposed foundational physical form,

\[
\frac{D\dot\rho}{dt}=-\operatorname{grad}_{F}V(\rho),
\]

with first-order gradient flow recovered in a strongly damped limit. Specific potential choices reproduce familiar equations: a positive gradient-penalty field action yields scalar wave dynamics, while a Fisher-information term on an extended \((\rho,\Theta)\) state space yields the Madelung equations and, subject to global phase conditions, the Schrödinger equation. These are exact mathematical embeddings under stated assumptions, not unique derivations of nature’s laws from coherence alone.

The final layers concern spacetime and gravity. Accessibility-weighted networks can generate positive relational edge costs and, after metric closure, effective spatial geometry. Lorentzian signature, dimensionality, locality, differentiable backreaction, and continuum dynamics remain open. A scalar coherence field has the standard scalar stress-energy tensor, and a Jacobson-style horizon-thermodynamic argument conditionally yields Einstein-type field equations if the required local-equilibrium, entropy-area, Unruh-temperature, Clausius, and focusing assumptions are supplied. This establishes structural compatibility, not a first-principles derivation of the gravitational coupling or matter content.

The paper closes with explicit falsifiability conditions and a research program. A separate [technical supplement](../supplements/03_Physics_Technical_Supplement_v0.10.md) preserves the full claim ledger, formal derivations, numerical audit, and reproducibility record. Its central conclusion is modest but substantive: CU presently offers a coherent architecture in which logical emergence, information geometry, reversible dynamics, dissipative flow, quantum accessibility, and relational geometry can be studied within one framework. Whether this architecture is physically fundamental depends on the development of constraint-grounded, domain-specific coherence functionals and on novel empirical consequences that distinguish CU from a unifying reinterpretation of existing mathematics.

**Keywords:** coherence; accessibility; information geometry; entropy; quantum foundations; Fisher–Rao geometry; emergent time; relational geometry; gravity; black holes

---

## Relation to the series

This paper can be read independently. It defines the physical concepts needed for its own argument. *Metaphysics and Epistemology* develops the framework’s account of explanatory order and claim status; *Foundations* records the shared principle architecture; the later domain papers develop biological, experiential, psychological, social, ethical, and artificial forms of organization. Formal proofs, numerical audits, claim ledgers, and complete revision history are preserved in the technical supplement.

## Note on Version 0.10

Version 0.10 preserves the original program—coherence and accessibility as organizing ideas, a classical probability sandbox, the ordered emergence of temporal description, a quantum-completion program, second-order dynamics, and relational approaches to spacetime and gravity—while revising claims whose mathematical or physical scope exceeded their support. The main text presents the current theory directly; Appendix B and the technical archive document the revision history.[^physics-version]

**Release-candidate synchronization.** This manuscript uses the shared Version 0.10 definitions, principle identifiers, Mandala cross-references, and interpretive and commitment language published in *Coherence Universalism: Metaphysics and Epistemology* and *Coherence Universalism: Foundations*. Its audited technical core, formal results, numerical results, and claim-status boundaries remain unchanged except where this manuscript explicitly states otherwise.

## How claims are marked

Definitions, derived results, conditional results, hypotheses, interpretations, and open questions are distinguished wherever their status is load-bearing. Mathematical identities hold under the displayed assumptions. Physical bridges require additional empirical or operational premises. Interpretive claims are compatible with the mathematics but are not entailed by it.

# Contents

1. Introduction: The Problem of Explanatory Order  
2. Primitives, Constraints, and Epistemic Discipline  
3. The Classical Sandbox: Differentiation, Entropy, and Accessibility  
4. Lawful Transitions, Ordered Updates, Time, and Temporal Direction  
5. From Classical Accessibility to Quantum State Space  
6. Quantum Coherence, Correlation, Entanglement, and Accessibility  
7. Second-Order Coherence Dynamics and the First-Order Limit  
8. Relational Geometry from Accessibility Networks  
9. Gravity as a Conditional Completion of the Geometry Program  
10. Horizons, Black Holes, and Limits of Accessibility  
11. The Unified Dynamical Architecture  
12. Research Program, Verification, and Falsifiability  
13. What Commitments This Account Licenses  
14. Conclusion  

Appendix A. Notation and Terminology  
Appendix B. Major Revisions from v0.09  
Appendix C. Technical Supplement and Reproducibility  
References  

# Principal contributions

1. It distinguishes substantive coherence from statistical differentiation:
   \[
   C_{\mathrm{toy}}(p)\equiv D(p)=\|p-u\|^2.
   \]

2. It gives one internally consistent Euclidean derivation and one Fisher-natural derivation, with separate opposition diagnostics \(\Pi_E\) and \(\Pi_F\).

3. It replaces the identity “entropy is inaccessible coherence” with a self-contained finite-partition derivation: the quadratic between/within identity is an instance of established decomposable-measure structure, while block averaging also increases Shannon entropy by a distinct weighted divergence from blockwise uniformity. The two changes are not the same quantity.

4. It replaces the inherited Goldilocks proofs with exact ascent, joint-growth, feasibility, and degeneracy conditions. In the four-state sandbox, the joint-growth wedge collapses on every nonuniform two-level distribution, and its width vanishes as the differentiation and entropy gradients become antiparallel.

5. It distinguishes that continuous geometric degeneracy set from fixed-coupling stationarity. At fixed \(r=\beta/\alpha\), every nonuniform interior stationary point is two-level and satisfies \(r=2(a-b)/\log(a/b)\); the stationary intersection is finite, and it is empty for \(r>0.6213609436\ldots\).

6. It identifies \(\beta/\alpha=1/2\) as the uniform state’s linear-stability threshold under ascent, while showing that the exactly critical state is nonhyperbolic and neither a local maximum nor a local minimum on \(\Delta_4\).

7. It establishes global bounds for \(\|\operatorname{grad}_F D\|_F\), \(\|\operatorname{grad}_F S\|_F\), and \(\Pi_F\) on the closed four-state simplex.

8. It separates transition relations, temporal ordering, clock parameterization, and temporal direction.

9. It replaces the hidden-correlation argument for quantum necessity with a conditional route through purification, reversible dilation, contextual accessibility, and explicit operational axioms.

10. It distinguishes excess purity, basis coherence, total correlation, and entanglement, and gives an exact coherence-to-entanglement conversion.

11. It incorporates the second-order Hamiltonian formulation and treats first-order flow as an effective damping regime. Its overdamped verification now separates fast-layer slip from slow-manifold error and states the asymptotic order relative to the fitted observable and normalization.

12. It recasts spacetime, gravity, and black-hole claims according to their actual epistemic status and repairs the positivity, differentiability, and local-equilibrium assumptions needed by those programs.

13. It states explicit failure conditions under which physical claims of the framework should be narrowed or abandoned.

14. It aligns the physical results with the current CU principle architecture, distinguishes normalized equations from dimensionful physical forms, and supplies a deterministic code-and-data record for independent checking.

---

---

# Domain Analytic Frame and CAP Record

**Target:** Coherence Universalism Version 0.10 release  
**Status:** Release declaration; scope-limited and revisable under the declared review gates  
**Use rule:** Unresolved fields are left explicit rather than completed by analogy.

## Paper and model identity

| Field | Declaration | Status |
|---|---|---|
| Paper | Coherence Universalism: Physics | Specified |
| Domain owner | Physics | Specified by the Version 0.10 release corpus |
| Primary model or analysis | A layered physical research program with classical, quantum, dynamical, geometric, and gravitational model families | Paper-relative |
| Primary claim status | Definitions, self-contained derivations, imported results, conditional physical bridges, hypotheses, and interpretations | Mixed statuses remain explicit |
| Review gate | Mathematical physics, probability, information geometry, quantum foundations, relativity, and specialist empirical review | Proportionate to claim and consequential reach |
| Methodological authority | CU-FP2, CU-M2, CU-M11, CU-M12, CU-M13, CU-M14, and CU-M15 | Controlling Version 0.10 methodological framework |

## Shared Analytic Frame

| # | Slot and domain declaration | Status and evidence |
|---|---|---|
| 1 | **Unit and boundary.** The unit is always a declared physical or mathematical model: finite probability state, density operator, field, accessibility network, subsystem, or horizon construction. | Model-specific |
| 2 | **State or trajectory space.** Finite simplexes, density-operator spaces, phase or field configurations, network states, and their trajectories are used in separate sections. | Specified per model |
| 3 | **Environment.** Boundary conditions, inaccessible variables, subsystems, baths, observers, or geometric surroundings are declared where used. | Model-specific |
| 4 | **Constraints and viable region.** Normalization, positivity, conservation or symmetry assumptions, admissible dynamics, and physical bridge conditions constrain each construction. | Specified; no universal viability set |
| 5 | **Actions, options, and transitions.** Stochastic maps, averaging, coarse-graining, channels, variational changes, Hamiltonian evolution, damping, and network updates are distinguished. | Multiple model classes |
| 6 | **Dynamics or update rule.** Euclidean and Fisher flows, second-order Lagrangian dynamics, effective damping, and conditional field dynamics appear only after a state space and potential are chosen. | Specified locally; no universal flow |
| 7 | **Observation and access.** Projection, marginalization, partial trace, measurement, and operational access maps determine retained distinctions. | Central declared relation |
| 8 | **Perturbation and intervention class.** Finite steps, model perturbations, parameter changes, channel action, field variations, and network modifications are section-specific. | Specified where results require them |
| 9 | **Equilibria, basins, or regimes.** Stationary points and local stability are proved in the classical sandbox; broader basins, convergence, and physical asymptotics are not generally established. | Bounded formal results |
| 10 | **Local–global status.** The quadratic finite-partition identity is an exact rescaled GE(2)-class decomposition; entropy gain is a separate KL/grouping identity; other cross-scale claims are conditional or qualitative. | Exact only for declared objects and maps |
| 11 | **Scalar status.** Statistical differentiation, entropy, potential, distance, and other scalars are typed model quantities; none is substantive coherence by default. | Measurement or model scalars |
| 12 | **Statistical-image and allocation status.** The finite classical simplex and declared density models are exact statistical objects. They are not automatically allocations of one material resource, and quantum states require a separate monotone-metric choice. | Strong classical license; quantum branch conditional |
| 13 | **Translation status.** Exact mathematics can reach Level 3; physical interpretation and empirical realization require separate Level 2 or Level 4 arguments. | Mixed by claim |
| 14 | **Open gaps.** Physical ontology, state-space selection, admissible quantum flow, emergent locality and dimension, backreaction, horizon entropy, and novel empirical consequences remain open. | Explicit research program |

## Compact Coherence Analysis Protocol record

| CAP module | Declaration | Boundary |
|---|---|---|
| System declaration | Every theorem names its state space, boundary, metric, map, potential, parameters, and horizon. | Required by the manuscript method |
| Observation declaration | Projection and access restriction are separated from block-uniform reconstruction and from physical destruction. | Load-bearing distinction |
| Evaluation declaration | Toy differentiation, entropy, geometry, and physical coherence are not conflated; scalar type and interpretation are stated. | Non-regression rule |
| Power and authorship declaration | The modeler selects state spaces, coarse-grainings, potentials, and interpretations; consequential technologies require separate governance review. | Not supplied by equations |
| Revision declaration | Failure of a bridge narrows the physical claim without erasing a valid mathematical result. | Claim-status loss is permitted |

## License summary

| License | Declaration | Current status |
|---|---|---|
| Scalar license | D, entropy, potentials, distances, and risk-like quantities are local model scalars, not one physical coherence score. | Conditional |
| Local–global license | Exact for D_N under block averaging; monotonic for Shannon entropy under the same reconstruction; no automatic profile transfer. | Declared in Section 3.11 |
| Statistical Image License | Exact for the declared finite probability simplex, density models, and operational probability states. | Licensed classical objects |
| Allocation License | Probability mass is normalized but need not represent a common-unit resource allocation unless an allocation interpretation is separately defended. | Not automatic |
| Refinement and Coarse-Graining License | Licensed for explicit stochastic maps, sufficient statistics, block aggregation, and coarse-graining with stable semantics. | Exact where declared |
| Fisher-Rao License | Canonical up to scale for licensed classical statistical models under the stated invariance assumptions; quantum monotone metrics form a family. | Classical yes; quantum criterion required |
| Translation license | Formal-to-physical steps must declare preserved structure, added assumptions, and empirical status. | Levels 2–4 as earned |
## Open gaps and review disposition

| Gap | Consequence | Required work |
|---|---|---|
| Novel empirical consequence | Without one, Physics remains a unifying architecture rather than a new physical theory. | Derive discriminating constraints or observations |
| Theorem attribution | Uncorrected novelty language would misstate the quadratic decomposition. | Cite Shorrocks and Theil; preserve CU-specific use |
| Geometry transfer | Fisher uniqueness applies to statistical models under stated invariance conditions, not arbitrary profiles. | Maintain theorem-specific scope |

> **Propagation rule.** This card makes the paper's existing objects and limits visible. It does not strengthen any empirical, mathematical, normative, metaphysical, or spiritual claim beyond the wording supported in the manuscript.

---

# 1. Introduction: The Problem of Explanatory Order

## 1.1 Fragmentation in fundamental physics

Modern physics is among humanity’s greatest intellectual achievements. Its theories predict phenomena across extraordinary ranges of scale and precision. Quantum theory describes matter and fields with unmatched empirical success. General relativity gives a dynamical account of spacetime and gravity. Statistical mechanics connects microscopic descriptions with macroscopic regularities. Quantum field theory joins quantum principles with special relativity. Information theory supplies a language for uncertainty, communication, compression, and distinguishability.

Yet the conceptual picture formed by these successes remains divided.

Quantum theory ordinarily begins with a temporal parameter, a state space, and a specification of subsystems or observables. General relativity makes spacetime itself dynamical, so the causal and geometric structures that quantum theory normally treats as given become part of what must be solved for. Statistical mechanics explains macroscopic irreversibility through reduced descriptions of laws that are often reversible at the microscopic level. Quantum measurement theory confronts the relation between a globally evolving state and the definite, locally accessible records through which experiments are described. In quantum gravity, the very structures used to state ordinary dynamics—time, locality, separability, and background geometry—may no longer be available in their familiar form.

These are not merely independent technical gaps waiting for separate calculations. They are connected by a question about **explanatory order**.

Time is used to formulate dynamics before the status of time is settled. Subsystems are invoked before the conditions under which a whole can be divided into meaningful parts are made explicit. Entropy is discussed before the relevant coarse-graining, observer, or access restriction has been specified. Geometry defines distance and locality, while distance and locality are also expected to emerge from more basic relations. Information is sometimes proposed as fundamental even though information is always information relative to a distinction, coding, or family of possible states.

None of these uses is illegitimate within an effective theory. A theory may properly take as primitive whatever allows it to describe its domain. The difficulty appears when an effective primitive is carried into a foundational explanation and then used to explain its own conditions of possibility.

Coherence Universalism begins from the possibility that several foundational puzzles are intensified by such explanatory inversions. It therefore asks a question prior to the search for a single master equation:

> **Which structures must already be available before the central concepts of physics can be meaningfully defined?**

This is an ordering problem before it is an equation-finding problem. It asks not only what the laws are, but what must be true for there to be states, laws, changes, measurements, intervals, and persistent physical identities in the first place.

## 1.2 Explanatory order as a physical problem

The phrase *explanatory order* can sound philosophical, as though it concerned only how theories are narrated. In this paper it has a stricter role.

A concept is explanatorily prior when another concept cannot be defined or used without presupposing it. A temporal derivative, for example, presupposes an ordered parameter. Entropy production presupposes a trajectory along which entropy can change. A local interaction presupposes some structure of neighborhood or accessibility. A reduced state presupposes a distinction between what is retained and what is ignored. A conservation law presupposes a family of admissible transformations across which something remains invariant.

These dependencies constrain physical theorizing. They do not determine one unique formalism, but they rule out some alleged derivations as circular. One cannot derive time merely by writing a differential equation in \(t\) and then reinterpreting the parameter after the fact. One cannot derive locality from a network if local adjacency was already built into the network’s definition. One cannot infer an arrow of time solely from a many-to-one coarse-graining unless a directed law or boundary condition explains why the coarse-graining is traversed in one orientation rather than the reverse.

The CU project treats these constraints as part of physics rather than as optional commentary on physics. A foundational theory is not complete merely because its equations are internally consistent. It must also make clear which structures are assumed, which are derived, which are reconstructed only after bridge principles are added, and which are interpretive proposals.

This discipline matters especially for a framework as ambitious as CU. The language of coherence can easily appear to explain everything because almost every successful physical description is coherent in some ordinary sense. The framework becomes substantive only when it says exactly what *coherence* means in each formal setting, what work the concept performs, what follows mathematically, and what would fail if the proposal were wrong.

Accordingly, the paper preserves the ambition of the program by requiring every physical claim to state its premises, scope, and status. A correction is not a retreat from the project; it identifies where the next physical argument must begin.

## 1.3 The CU proposal: coherence and accessibility

CU proposes that two notions organize the physical inquiry: **coherence** and **accessibility**.

### 1.3.1 Coherence

**[Definition]** Coherence is integrated relational organization under constraint.

This definition is intentionally richer than regularity or order. A perfectly uniform state may be regular while containing no differentiation. A highly concentrated probability distribution may be differentiated while representing a physically destroyed configuration. A crystal may be stable without being adaptive. A turbulent system may contain structured correlations without preserving an enduring identity. A pure quantum state may be a product state or an entangled state, despite having the same purity in both cases.

Coherence therefore cannot be identified without qualification with any one of the following:

\[
\text{uniformity},\quad
\text{stability},\quad
\text{purity},\quad
\text{low entropy},\quad
\text{correlation},\quad
\text{complexity}.
\]

Each may contribute to coherence under appropriate constraints. None is sufficient by itself.

The substantive question is whether differentiated components remain mutually compatible and jointly satisfy the constraints relevant to the system’s form of persistence. At the physical level, those constraints may concern conservation, dynamical stability, boundary conditions, symmetry, or robustness. At biological levels they become viability-bearing: the system must actively preserve the conditions of its own continuation. The present paper remains primarily at the physical level, but it must define its terms in a way that can support the later domains without conflating them.

### 1.3.2 Accessibility

**[Definition]** Accessibility is the portion of a state’s relational structure available to a specified subsystem, scale, measurement context, or family of operations.

Accessibility is relational rather than absolute. A correlation may be present in a joint state while absent from either marginal. A phase relation may be invisible in one measurement basis and visible in another. Fine distinctions among microstates may disappear under a macro-description. Information behind a horizon may be unavailable to an exterior observer even if a larger theory preserves the global state.

The framework’s guiding physical intuition is:

\[
\boxed{
\text{structure may persist globally while becoming inaccessible locally}.
}
\]

This pattern recurs in classical coarse-graining, statistical mechanics, quantum entanglement, decoherence, error correction, horizon physics, and holographic reconstruction. Its recurrence motivates a common vocabulary. It does not prove that all these phenomena share one physical mechanism or one ontological substrate.

The distinction between absence and inaccessibility is central:

\[
\text{not represented in a reduced description}
\not\Rightarrow
\text{not present in the larger state}.
\]

But the converse caution is equally important:

\[
\text{mathematically recoverable in a larger model}
\not\Rightarrow
\text{physically accessible to a real subsystem}.
\]

A theory of accessibility must therefore specify the permitted operations, the subsystem structure, and the coarse-graining under consideration.

## 1.4 The wider framework

This paper belongs to a larger sequence in which CU develops coherence across physical, biological, psychological, social, artificial, and normative domains. The present paper does not attempt to reproduce the entire transcendental argument of the Introduction or the full principle architecture of the Foundations document. It inherits two commitments from them.

First, coherence is treated as a condition of intelligibility. Any describable object, event, law, or distinction must possess enough relational integrity to be identifiable as the object, event, law, or distinction in question. This is a transcendental claim about description and identity, not yet a physical law.

Second, higher-order forms of coherence depend on lower-order enabling conditions. Biological self-maintenance presupposes physical persistence. Psychological integration presupposes biological organization. Social and ethical coherence presuppose agents capable of memory, meaning, and justification. The Coherence Ladder represents these dependencies.

The Physics paper has a special responsibility within that series. It must show how far the framework can proceed before concepts such as life, agency, purpose, or value enter. It must not import biological viability or moral goodness into the behavior of elementary systems. Physical coherence is not the universe “wanting” in a psychological sense. It is the lawful preservation and transformation of relational organization under physical constraints.

## 1.5 The Coherence Ladder in the physical domain

The list below is the Physics paper's **technical sequence of logical enablement**. It does not replace the canonical titles of Mandala stages 1–10 recorded in *Foundations* and M&E. Quantum state-space selection, purification, and quantum-resource distinctions enter as conditional technical branches after statistical and accessibility structures are available; they are not assigned new canonical stages merely to preserve one linear narrative.

The physical portion of the Coherence Ladder is a proposed sequence of logical enablement:

\[
\begin{aligned}
1.&\ \text{Pure Structure}\\
2.&\ \text{Partial Separability}\\
3.&\ \text{Domain-Relative Coherence Directions}\\
4.&\ \text{Lawful Transitions}\\
5.&\ \text{Ordered Histories}\\
6.&\ \text{Temporal Order and Parameterization}\\
7.&\ \text{Rule-Governed Transformation and Computation}\\
8.&\ \text{Entropy and Accessibility}\\
9.&\ \text{Relational Geometry and Spacetime}\\
10.&\ \text{Gravitational Dynamics}.
\end{aligned}
\]

The ladder is not a cosmological chronology. It does not say that the universe first spent a period possessing pure structure, then later acquired partial separability, and eventually discovered time. Such language would already presuppose the time whose emergence is at issue.

The ladder instead states relations of logical enablement. Partial separability is required before different aspects of a configuration can be compared. Comparison is required before gradients among configurations can be defined. A gradient does not yet produce an actual history; a transition rule must specify which changes are admissible. Admissible transitions do not yet constitute time; they must instantiate a sufficiently stable order. Ordered change can then be parameterized, allowing rates, memory, computation, and entropy production to be defined. Stable patterns of accessibility may support effective locality and geometry. If that geometry becomes responsive to the organization of the state, gravity enters as dynamical geometry.

Each transition may require an additional bridge principle. The ladder does not pretend that the higher rung is deductively contained in the lower one. Rather, it prevents the bridge from being hidden. Quantum state-space selection and the quantum distinctions developed in Sections 5–6 are conditional technical branches after the statistical and accessibility structures; they are not assigned an extra canonical Mandala stage merely to force the program into one line.

The disciplined reading is therefore:

- lower rungs provide conditions of intelligibility for higher rungs;
- a higher rung may require a completion not uniquely fixed by the rung below;
- several mathematical realizations may instantiate the same structural transition;
- no historical or cosmological succession follows merely from the logical order;
- failure at a lower rung invalidates any claim to have derived the higher one.

## 1.6 Why begin below energy, spacetime, and information?

CU’s choice of coherence and accessibility as organizing notions does not deny the fundamentality of energy, spacetime, or information within successful physical theories. It asks whether these concepts are sufficiently primitive for the particular explanatory task.

Energy is defined relative to dynamical symmetries or generators of evolution. Spacetime supplies the geometric arena within which many familiar physical quantities are defined. Information presupposes distinguishable possibilities and an access or coding structure. If the project is to explain how dynamical order, geometry, and distinguishability arise, then none can simply be assumed in its mature form.

Coherence and accessibility are proposed at a more schematic level. Relational compatibility can be discussed before a spatial metric is fixed. Distinguishability can be discussed before a particular informational encoding is chosen. Access restrictions can be represented before they are interpreted as horizons, partial traces, or thermodynamic coarse-grainings.

This does not establish that coherence and accessibility are ontologically fundamental. It establishes only that they are promising candidates for organizing a non-circular reconstruction.

## 1.7 Four theses with different epistemic status

The paper advances four connected claims. They should not be assigned the same confidence.

### 1.7.1 Logical thesis

**[Bridge principle]** A physical theory that aims to explain time, entropy, quantum accessibility, and spacetime should make explicit the dependency relations among these concepts rather than assume them all at once.

This thesis concerns explanatory discipline. It can be evaluated by examining whether the proposed dependency relations are coherent and whether allegedly emergent structures have been smuggled into the premises.

### 1.7.2 Mathematical thesis

**[Imported mathematical observation with derived applications]** Information-geometric state spaces provide a common mathematical vocabulary for:

- distinguishability of states;
- gradients constrained to normalized state spaces;
- coarse-graining and data processing;
- reversible second-order dynamics;
- dissipative first-order limits;
- and, under a specified directed law such as Section 4.11, transfer between accessible and inaccessible structure.

The mathematical thesis is the most concrete. Its individual claims can be checked equation by equation.

### 1.7.3 Physical thesis

**[Hypothesis]** The repeated role of these structures across physical theories reflects more than mathematical convenience. It indicates that coherence and accessibility are physically fundamental organizing features.

This is not established merely by reproducing known equations. A mathematical framework may unify descriptions without identifying a new physical substrate. The physical thesis requires either novel explanatory necessity, independent empirical predictions, or both.

### 1.7.4 Metaphysical thesis

**[Interpretation]** The state space may be read not merely as a representation of uncertainty but as structured physical possibility, with actuality arising through constrained realization.

This reading belongs to the broader CU framework. It may be philosophically fruitful, but it is not entailed by the technical results. The same mathematics can often support epistemic, operational, or ontic interpretations.

## 1.8 The physics crisis as a coherence crisis

The word *crisis* should not imply that established physics is failing in its empirical domains. The crisis is one of integration.

Theories work locally while their primitives remain difficult to place within one explanatory order. Reversible laws coexist with irreversible experience. Global quantum states coexist with local outcomes. Geometry is both arena and dynamical object. Information appears both descriptive and physical. The problem is not that these notions are individually incoherent. It is that their relations are distributed across frameworks with different starting assumptions.

CU diagnoses this as an accessibility problem as much as a unification problem. Different theories may be tracking different projections of a deeper relational organization. What is fundamental in one description may be emergent in another because the descriptions preserve different distinctions.

This diagnosis is a research proposal, not a result. It earns its place only if it helps reconstruct the relations among the theories more clearly than existing alternatives and eventually produces consequences that are not merely redescriptions.

## 1.9 Scope and limits

This paper does not claim that:

1. departure from a uniform probability distribution is substantive coherence;
2. classical probability cannot represent correlations hidden by marginalization;
3. purification alone uniquely derives quantum theory;
4. the Bures metric is the unique quantum information metric;
5. a quantum natural-gradient flow is automatically a completely positive physical channel;
6. a universal intermediate entropy band is equivalent to entanglement;
7. entanglement alone derives spacetime in generic quantum systems;
8. a correlation-based dissimilarity is automatically a metric;
9. Jacobson’s argument fixes Newton’s constant from CU without further input;
10. black-hole information loss is resolved merely by renaming it accessibility loss;
11. a recurring coherence–entropy cycle follows from an autonomous gradient flow;
12. the formal embeddings of familiar equations empirically confirm CU;
13. the Coherence Ladder is a unique deductive derivation of all later physical structure;
14. the metaphysical interpretation of the state space is forced by the mathematics.

These limits identify the strongest current form of each proposal and the conditions under which it could be strengthened. A framework that distinguishes what it has shown from what it hopes to show is better positioned to discover where the next real advance must occur.[^physics-version]

## 1.10 Method and organization

The paper proceeds by controlled ascent.

Section 2 defines the primitives and separates substantive coherence from the toy quantities used in later calculations. Section 3 rebuilds the classical sandbox and establishes exactly what follows from differentiation, entropy, Euclidean geometry, Fisher geometry, and coarse-graining. Section 4 separates lawful transition, temporal order, clocks, irrecoverability, and the arrow of time.

Section 5 asks what classical probability can represent and develops a conditional route toward quantum state space through purification and contextual accessibility. Section 6 distinguishes quantum purity, basis coherence, total correlation, and entanglement, then gives an exact coherence-to-entanglement construction. Section 7 presents the second-order Hamiltonian framework and derives the first-order damped limit.

Sections 8–10 treat relational geometry, gravity, and horizons. Section 11 integrates the dynamical levels and revises the Double Helix as a broader developmental hypothesis rather than a cycle proved by the first-order sandbox. Section 12 states the research program and falsifiability conditions. Section 13 identifies the metaphysical, spiritual, and practical commitments the account licenses without converting them into physical conclusions. Section 14 concludes.

The method throughout is to let the framework remain expansive while making every transition auditable:

\[
\text{definition}
\rightarrow
\text{formal result}
\rightarrow
\text{physical bridge}
\rightarrow
\text{interpretation}
\rightarrow
\text{test}.
\]

That sequence is the paper’s governing discipline.

---

# 2. Primitives, Constraints, and Epistemic Discipline

## 2.1 Why the primitives matter

A physical framework can fail before any equation is wrong. It can fail because its basic terms already contain the structures it later claims to derive.

If time is built into the definition of change, the emergence of time has not been explained. If space is built into the definition of relation, emergent geometry has not been earned. If isolated subsystems are assumed from the beginning, entanglement and nonseparability may appear as anomalies only because the ontology was over-partitioned at the start.

CU therefore begins with deliberately sparse primitives. The aim is not to describe the world in its final physical form, but to identify the least structure needed for a sequence of increasingly specific descriptions.

This minimalism carries a risk. Terms such as *structure*, *constraint*, and *coherence* can become so general that they cease to exclude anything. The response is not to abandon them, but to state their formal roles carefully and to resist treating a conceptual prerequisite as though it were already a dynamical law.

## 2.2 Pure structure

**[Definition]** Pure structure is a domain of relations and compatibility conditions without presupposing that the relata are particles, fields, spacetime points, observers, or enduring substances.

Let a possible configuration be represented abstractly by

\[
x\in\mathcal X.
\]

At this stage, \(\mathcal X\) is not assumed to be spatial, temporal, probabilistic, or quantum. It is simply a domain in which configurations can be distinguished and relations among them can be represented.

The phrase *pure structure* should not be read as the metaphysical thesis that relations literally exist without relata. It marks the weakest formal commitment of the program: whatever reality is, it is not wholly featureless. Some patterns are compatible, others are not; some descriptions preserve distinctions, others collapse them; some transformations are admissible, others are excluded.

This starting point is intentionally pre-physical in the ordinary sense. It does not yet contain mass, charge, energy, locality, duration, or causal propagation. Those belong to later realizations.

### 2.2.1 Why structure is not yet coherence

Structure alone is not substantive coherence. A random graph has structure. A shattered object has a relational configuration. A thermalized system has a well-defined microstate. Coherence enters when relations form an integrated organization that satisfies relevant constraints.

Thus:

\[
\text{structure}
\quad\text{is necessary for}\quad
\text{coherence},
\]

but

\[
\text{structure}
\not\Rightarrow
\text{coherence}.
\]

The distinction prevents the framework from treating every describable state as equally coherent merely because it can be represented.

## 2.3 Partial separability

**[Definition]** A configuration is partially separable when it admits distinctions among aspects, components, or substructures without requiring those aspects to be fully independent.

Partial separability is weaker than classical statistical independence. It is also weaker than a fixed tensor-product decomposition. It requires only enough internal differentiation to support claims such as:

- one relation varies while another remains fixed;
- a subsystem can access some variables while ignoring others;
- two descriptions overlap without being identical;
- several fine states can be mapped to one macrostate;
- different scales can preserve different distinctions.

If there were no separability at all, there would be no basis for comparison. Every alteration would be an alteration of an indivisible whole with no identifiable aspect held constant. No marginal, coarse-graining, subsystem, or measurement context could be defined.

If separability were complete, the world would decompose into intrinsically independent units. Many physical phenomena—including interaction, collective modes, constraints, and quantum entanglement—would then have to be added back as external relations among already independent pieces.

Partial separability occupies the middle position:

\[
\boxed{
\text{distinction without absolute independence}.
}
\]

This is one of CU’s most important structural commitments. It permits the world to contain real parts without requiring that the parts possess complete identities apart from the relations that constitute the whole.

### 2.3.1 Separability as access-relative

The relevant decomposition may depend on the available operations. A subsystem boundary can be physically robust in one regime and ineffective in another. A molecular partition may be useful for chemistry, a mode decomposition for field theory, and a tensor factorization for quantum information. CU therefore treats partial separability as something that can be stabilized rather than as a once-and-for-all metaphysical carving.

This allows the framework to ask:

> Which distinctions survive the dynamics strongly enough to function as physical parts?

That question will later connect to decoherence, emergent locality, and effective geometry.

## 2.4 Configurations, ensembles, and probabilities

The state variable used in a model must not be confused with reality merely because the mathematics is exact.

A point \(x\in\mathcal X\) may represent an actual configuration. A probability distribution \(p\) over \(\mathcal X\) may instead represent:

- epistemic uncertainty about which configuration obtains;
- an operational summary of preparation statistics;
- frequencies in an ensemble;
- stochastic dynamics;
- or, under a stronger metaphysical interpretation, the structured availability of physical possibilities.

The same formal distribution can support more than one interpretation.

This matters because the classical sandbox will rank probability distributions by a quantity \(D(p)\). The mathematical ranking is unambiguous once \(D\) is defined. Its physical significance depends entirely on what the probabilities and their outcomes represent.

A distribution concentrated on a viable configuration may indicate robust organization. A distribution concentrated on a destroyed configuration may indicate certainty of failure. Probability concentration alone cannot distinguish them.

The paper therefore follows a two-step discipline:

1. derive the formal properties of probability distributions without overinterpreting them;
2. state separately what additional physical grounding would be required to interpret those properties as coherence.

## 2.5 Constraints

**[Definition]** A constraint is a restriction on admissible configurations, admissible transitions, or admissible descriptions.

Constraints can enter at several levels.

### 2.5.1 Kinematic constraints

These define the state space itself. For a probability distribution,

\[
p_i\geq0,
\qquad
\sum_i p_i=1.
\]

For a density matrix,

\[
\rho\geq0,
\qquad
\operatorname{Tr}\rho=1.
\]

Such constraints determine what counts as a valid state before a dynamical law is chosen.

### 2.5.2 Dynamical constraints

These determine which transitions are allowed. Conservation laws, selection rules, causal restrictions, and equations of motion all constrain trajectories through state space.

### 2.5.3 Boundary and environmental constraints

Initial data, boundary conditions, external fields, reservoirs, and coupling to inaccessible degrees of freedom can select a regime without changing the underlying state space.

### 2.5.4 Scale-relative constraints

A relation can be negligible at one scale and decisive at another. Molecular collisions may be hidden in hydrodynamic variables; global conservation may constrain local fluctuations; collective order can limit the behavior of components.

### 2.5.5 Viability-bearing constraints

At biological and higher levels, constraints become tied to the continued existence of the system as the kind of system it is. A cell must preserve a bounded region of temperature, chemical composition, membrane integrity, and metabolic function. The physical paper should not project this form of active self-maintenance downward onto all matter. It needs only the more general idea that some relational organizations persist only within a restricted region of possibility.

A constraint set \(K\) induces an admissible region

\[
\mathcal X_K\subseteq\mathcal X.
\]

But “being constrained” is not the same as being coherent. A system can be tightly constrained in a fragmented, brittle, or destructive condition. Coherence concerns how constraints are jointly satisfied and how the relations among components are preserved.

## 2.6 Substantive coherence

The framework’s central term must be allowed to remain richer than the toy models used to study it.

**[Definition]** Substantive coherence is the degree to which differentiated components form an integrated relational organization that satisfies the constraints relevant to the system’s persistence, identity, or function across the scales and temporal horizon under consideration.

A complete physical coherence functional has not yet been derived. The manuscript therefore uses the schematic notation

\[
\boxed{
C_{\mathrm{sub}}=C(p;K,G,\pi,T),
}
\]

where:

- \(p\) represents a state or distribution over configurations;
- \(K\) specifies operative constraints;
- \(G\) specifies relational organization among components;
- \(\pi\) specifies the scale, partition, or coarse-graining;
- \(T\) specifies the temporal horizon over which persistence or robustness is evaluated.

This notation is not a solved equation. It records the dependencies a mature measure must respect.

### 2.6.1 A minimal statewise model

Suppose the sample space contains physically interpreted states

\[
X=\{x_1,\ldots,x_N\},
\]

and each state receives a constraint-relative evaluation

\[
c_K(x_i).
\]

A minimal expected-coherence quantity would be

\[
\boxed{
C_K(p)=\sum_i p_i\,c_K(x_i).
}
\]

Unlike distance from uniformity, this quantity distinguishes concentration on a viable state from concentration on a nonviable one.

Yet it remains incomplete. The coherence of a whole may depend on relations not reducible to the scores of individual states. Correlation among components, recovery after perturbation, continuity across transitions, and integration across scales may require separate terms.

A more complete model might schematically take the form

\[
C_{\mathrm{sub}}
=
C_K(p)
+
\lambda I_G(p)
-
\mu F_T(p)
-
\nu L_\pi(p),
\]

where \(I_G\) measures integration, \(F_T\) measures fragility across a temporal horizon, and \(L_\pi\) measures loss under a relevant coarse-graining. No canonical form is claimed here. The point is to identify what would have to be modeled.

### 2.6.2 Coherence is not moral goodness

Physical coherence is descriptive. A destructive vortex, a stable authoritarian institution, or a malignant tumor can possess forms of internal organization. Higher CU domains introduce additional constraints concerning sentience, agency, justification, and harm. Those normative conditions must not be projected back into the physics.

Likewise, local coherence can conflict with global coherence. A subsystem may preserve itself by exporting instability to its environment. The framework’s later Local–Global Coherence Principle addresses this cross-scale tension, but the physical paper should not assume that every persistent local structure is globally beneficial.

## 2.7 Statistical differentiation

The classical sandbox requires a quantity that can be calculated exactly without pretending to solve substantive coherence.

**[Definition]** Statistical differentiation is departure from the uniform distribution within a specified probability space.

For a finite \(N\)-state system with

\[
u_i=\frac1N,
\]

define

\[
\boxed{
D(p)=\|p-u\|_2^2
=
\sum_{i=1}^{N}
\left(p_i-\frac1N\right)^2.
}
\]

In the historical notation of the CU Physics sandbox,

\[
\boxed{
C_{\mathrm{toy}}(p)\equiv D(p).
}
\]

The equality preserves continuity with the earlier manuscript while clarifying the interpretation.

The functional answers a narrow question:

> How strongly does the distribution distinguish among the available outcomes relative to uniformity?

It does not answer:

> Are the favored outcomes integrated, viable, stable, or physically coherent?

The distinction can be summarized as

\[
\boxed{
D\ \text{measures strength of selection,}
\qquad
C_{\mathrm{sub}}\ \text{must measure the quality and integration of selection}.
}
\]

### 2.7.1 Why differentiation still matters

Renaming the quantity does not make it irrelevant. Constraint formation often does create statistical differentiation. If a physical interaction makes some configurations more available than others, the distribution departs from uniformity. Differentiation may therefore be a trace of structure.

But a trace is not the same as the thing traced. A footprint indicates that something passed through; it does not identify the creature without additional information. In the same way, non-uniformity can indicate constraint-sensitive selection without establishing substantive coherence.

## 2.8 Entropy

For \(p\) in the interior of a finite probability simplex, define Shannon entropy

\[
\boxed{
S(p)=-\sum_i p_i\log p_i.
}
\]

Entropy is a property of the distribution relative to the chosen sample space. It measures spread or uncertainty. It is not itself movement, disorder in every ordinary sense, or an intrinsic property independent of description.

This distinction becomes important when the paper discusses dynamics.

- \(S(p)\) is a state value.
- \(\nabla S(p)\) is a direction of steepest increase relative to a chosen geometry.
- \(dS/d\lambda\) is a rate along an ordered path.
- entropy production in physical time requires a temporal interpretation and a selected orientation.

Thus a distribution can have greater entropy than another before there is any claim that entropy has *increased*:

\[
S(q)>S(p)
\]

is an atemporal comparison unless \(p\) and \(q\) are placed in an ordered history.

### 2.8.1 Entropy and structure are not simple complements

In a two-state system, many measures of concentration and entropy are monotonically opposed. In higher-dimensional spaces, the relation is more subtle. A redistribution can make one outcome more dominant while also rescuing another from near impossibility. One form of differentiation can sharpen while overall spread increases.

The sandbox will derive the exact local conditions under which \(D\) and \(S\) rise together. This does not mean a system becomes “more ordered and more disordered in the same respect.” It means the two functionals summarize different aspects of a multidimensional state.

### 2.8.2 Conditional entropy is not hidden differentiation

For a partition into blocks, Shannon’s grouping identity separates uncertainty about the block label from uncertainty within a block. The within-block term is a genuine conditional entropy. It is not the differentiation residual introduced in Section 3.

For a fixed two-state block mass \(q\) and internal split \((t,1-t)\), the two quantities move in opposite directions:

\[
D_{\mathrm{within}}
=
\frac12q^2(2t-1)^2,
\]

while

\[
S_{\mathrm{within}}
=
q\,h(t),
\qquad
h(t)=-t\log t-(1-t)\log(1-t).
\]

The first is maximal when the block is internally concentrated; the second is maximal when it is internally uniform. Therefore the phrase “hidden entropy is hidden differentiation” is false even in the classical sandbox.

A different comparison does yield a precise relation. If the fine distribution is replaced by the maximum-entropy distribution having the same block masses, within-block differentiation is removed and Shannon entropy increases. Section 3.11 states that result exactly. The differentiation destroyed and entropy gained are paired effects of the same averaging map, not equal quantities.

## 2.9 Accessibility, projection, and block-uniform reconstruction

**[Definition]** A coarse-graining is a map

\[
\pi:\mathcal X\rightarrow\bar{\mathcal X}
\]

that identifies fine-grained states regarded as equivalent at a reduced scale, context, or family of operations.

A simple coarse-graining groups microstates into macrostates. A marginalization discards variables. A partial trace restricts a quantum state to a subsystem. A measurement maps a state to outcome probabilities. In each case, distinctions present in the larger description may disappear.

Two operations must be distinguished.

1. **Projection to a reduced alphabet:** \(p\mapsto q=\pi(p)\). The output belongs to a smaller state space.
2. **Block-uniform reconstruction:** \(p\mapsto E_\pi p\). The output remains on the original state space but replaces each block by the uniform conditional distribution with the same block mass.

The first records only what the coarse description retains. The second chooses the maximum-entropy fine representative compatible with that retained information. Comparing \(S(p)\) directly with \(S(q)\) mixes different alphabets; comparing \(S(p)\) with \(S(E_\pi p)\) isolates the entropy change produced by erasing within-block distinctions on a common state space.

Accessibility is therefore not merely a property of a state. It is a relation among:

- a state;
- a subsystem or observer;
- a family of permitted operations;
- a scale or context;
- and a map specifying what is retained.

A distinction is accessible when it can affect predictions, records, or actions available within that structure.

The framework distinguishes

\[
\boxed{
\text{ontic absence}
\quad\text{from}\quad
\text{operational inaccessibility}.
}
\]

This distinction does not prejudge the metaphysics. It simply prevents a reduced description from being mistaken for a complete inventory of the larger state.

### 2.9.1 Accessibility is not observer subjectivism

The word *observer* can suggest that accessibility is merely psychological. That is not the intended claim. A subsystem may be physically unable to recover a correlation because the permitted interactions do not couple to it. A horizon can restrict causal contact. An environment can carry phase information into degrees of freedom beyond practical control. These are objective features of the access relation.

Accessibility is relative, but relativity to a subsystem or operation is not the same as arbitrariness.

### 2.9.2 Hidden structure and recoverability

A distinction may be hidden under one coarse-graining yet recoverable under another. This motivates two separate questions:

1. Is information absent from the reduced state?
2. Is there any physically allowed recovery procedure that can reconstruct it from available data?

The first is algebraic. The second is dynamical and operational. CU’s physical program ultimately needs both.

### 2.9.3 Averaging is not automatically physical destruction

The map \(E_\pi\) is a well-defined mathematical channel. Applying it to a distribution erases within-block distinctions in the represented state. A physical system need not literally undergo that channel merely because an observer uses the reduced description \(q=\pi(p)\).

Accordingly, three statements must remain separate:

\[
\text{the observer omits a distinction},
\]

\[
\text{the chosen reconstruction replaces it by uniform uncertainty},
\]

and

\[
\text{the physical dynamics destroys or redistributes it}.
\]

Only the second is established by the block-averaging theorem alone. The third requires a dynamical model.

## 2.10 Why geometry enters

Coordinates alone do not tell us how different two states are. If gradients, shortest paths, distinguishability, and dynamical costs are to be representation-independent, a state space requires geometry.

A Riemannian metric assigns a local squared length

\[
ds^2=g_{ij}(x)\,dx^i dx^j.
\]

The gradient of a scalar \(f\) is defined by

\[
g(\operatorname{grad}f,v)=df(v)
\]

for every tangent vector \(v\). The gradient is therefore not merely the list of partial derivatives. It depends on what the geometry counts as a unit displacement.

This has a direct physical interpretation. The same coordinate change can be easy in one region of state space and significant in another. On a probability simplex, changing a probability from \(10^{-6}\) to \(2\times10^{-6}\) may be more statistically distinguishable than changing it from \(0.40\) to \(0.400001\), despite the equal coordinate increment.

### 2.10.1 Euclidean geometry as a sandbox tool

The ordinary Euclidean inner product is convenient for exact calculations:

\[
\langle v,w\rangle_E=\sum_i v_iw_i.
\]

It treats equal coordinate changes as equal distances. This is useful for a toy model but not generally invariant under reparameterization of probabilities.

### 2.10.2 Fisher–Rao geometry

For finite sample spaces, Čencov-type results characterize the Fisher–Rao metric, up to an overall positive factor, by invariance under sufficient statistics or equivalent Markov-morphism conditions; extensions beyond the finite case require additional locality and continuity assumptions (Čencov, 1982; Lê, 2016). In coordinates on the interior simplex,

\[
g_p(v,w)
=
\sum_i\frac{v_iw_i}{p_i},
\qquad
\sum_i v_i=\sum_i w_i=0.
\]

The corresponding squared line element is

\[
ds^2=\sum_i\frac{dp_i^2}{p_i}.
\]

Under the square-root coordinates

\[
x_i=2\sqrt{p_i},
\]

we obtain

\[
ds^2=\sum_i dx_i^2,
\qquad
\sum_i x_i^2=4.
\]

Thus the simplex interior maps to the positive orthant of a sphere. The boundary lies at finite Fisher distance. Positivity preservation must therefore come from the vector field or integrator, not from an infinite-distance claim.

## 2.11 Natural gradients

For a smooth function \(f\) on the simplex, the Fisher natural gradient is

\[
\boxed{
[\operatorname{grad}_{F}f(p)]_i
=
p_i
\left(
\frac{\partial f}{\partial p_i}
-
\sum_jp_j\frac{\partial f}{\partial p_j}
\right).
}
\]

The weighted subtraction enforces tangency:

\[
\sum_i[\operatorname{grad}_{F}f]_i=0.
\]

This formula is not equivalent to multiplying the Euclidean gradient by \(p_i\) and then subtracting an ordinary arithmetic mean. The distinction changes the vector field and therefore changes any dynamical proposition derived from it.

The natural gradient offers three advantages:

1. it respects the normalization constraint;
2. it transforms covariantly under reparameterization;
3. it reflects statistical distinguishability rather than raw coordinate distance.

It does not tell us which scalar nature optimizes. Geometry selects how to move in response to a scalar; it does not select the scalar itself.

Nor does a natural-gradient equation automatically become a fundamental physical law. It may represent:

- an optimization algorithm;
- a phenomenological relaxation process;
- a coarse-grained effective dynamics;
- or, with further justification, a physical flow.

The interpretation must be supplied separately.

## 2.12 Three uses of probability geometry in this paper

To avoid conflation, the paper uses probability geometry in three distinct ways.

### 2.12.1 Descriptive geometry

The metric measures distinguishability among states.

### 2.12.2 First-order effective dynamics

A natural-gradient flow has the form

\[
\dot p=\operatorname{grad}_{F}F(p)
\]

or its descending counterpart. Such flows are dissipative and move monotonically with respect to an associated Lyapunov functional under appropriate conditions.

### 2.12.3 Second-order physical dynamics

A Lagrangian on the same manifold can generate inertial, oscillatory, and reversible dynamics:

\[
\frac{D\dot p}{dt}
=
-\operatorname{grad}_{F}V(p).
\]

The first-order flow can then arise as a strongly damped limit. This distinction will become central in Section 7.

Using the same geometry does not make the two dynamics identical. One is a relaxation law; the other carries velocity, momentum-like persistence, and time-reversal symmetry.

## 2.13 Claim architecture

The project uses four layers of commitment.

### 2.13.1 State-space structure

What configurations, constraints, and access maps are admitted?

### 2.13.2 Dynamical structure

What transitions or trajectories are allowed?

### 2.13.3 Bridge structure

How are abstract states and equations interpreted physically?

### 2.13.4 Empirical structure

What observations distinguish the proposal from alternatives?

A result can be exact at the first two levels while remaining underdetermined at the third. For example, the decomposition of a toy differentiation functional under coarse-graining can be mathematically exact even if its interpretation as physical coherence is unjustified.

The paper therefore marks claims as definitions, derived results, conditional results, bridge principles, hypotheses, interpretations, or open problems.

This is not merely editorial caution. It is part of the framework’s epistemology. Coherence in inquiry requires that the strength of a conclusion match the strength of its premises.

## 2.14 Transition to the sandbox

The conceptual distinctions of this section now permit a controlled formal exercise.

The sandbox will not attempt to model a real physical system. It will ask what can be established on the simplest nontrivial normalized state space:

- how statistical differentiation behaves;
- how entropy behaves;
- how their gradients relate;
- how geometry changes the flow;
- how coarse-graining hides distinctions;
- and where a physical interpretation would require more than the mathematics provides.

The value of the exercise lies precisely in its restraint. By learning exactly what the toy model does, the framework becomes clearer about what it still needs.

---

# 3. The Classical Sandbox: Differentiation, Entropy, and Accessibility

## 3.1 Why use a sandbox?

A foundational framework needs examples simple enough to audit.

The classical sandbox is not intended as a miniature universe. It is a controlled setting in which every state, gradient, projection, and coarse-graining can be written explicitly. Its value lies in showing which conclusions follow from the mathematics before a physical interpretation is added.

The four-state simplex is especially useful because it is the smallest familiar probability space rich enough to display several independent directions of redistribution. In a two-state model, moving away from uniformity necessarily sharpens one binary contrast. In four states, one contrast can sharpen while another softens. Fine distinctions can be hidden inside coarse blocks. Entropy and differentiation can even increase along the same path.

The sandbox therefore addresses five questions:

1. What does departure from uniformity actually measure?
2. How does that quantity relate to Shannon entropy?
3. How do Euclidean and Fisher geometries produce different gradients?
4. What information disappears under coarse-graining?
5. Which of these results can legitimately be interpreted as physical coherence?

The answer to the fifth question is deliberately restrictive:

> **The sandbox formalizes differentiation and accessibility. It does not yet formalize substantive physical coherence.**

This restriction is not a weakness of the exercise. It is what allows the valid results to be preserved without asking the toy model to carry more meaning than its variables contain.

## 3.2 State space

Let

\[
\Delta_4^\circ
=
\left\{
p\in\mathbb R^4:
p_i>0,\ \sum_{i=1}^{4}p_i=1
\right\}
\]

be the interior of the four-state probability simplex. Its closure permits \(p_i=0\).

A point

\[
p=(p_1,p_2,p_3,p_4)
\]

assigns probabilities to four mutually exclusive outcomes. The uniform distribution is

\[
u=
\left(
\frac14,\frac14,\frac14,\frac14
\right).
\]

Because the probabilities sum to one, the simplex has three independent dimensions. An increase in one component must be balanced by decreases elsewhere, but there are many ways to accomplish that balance.

The tangent space is

\[
T_p\Delta_4
=
\left\{
v\in\mathbb R^4:
\sum_i v_i=0
\right\}.
\]

Any admissible instantaneous velocity must lie in this tangent space so that normalization is preserved.

### 3.2.1 What the probabilities mean

The formal results below do not require one interpretation of \(p\). It may represent:

- uncertainty about an actual state;
- relative frequencies in an ensemble;
- operational preparation probabilities;
- a stochastic physical state;
- or a modal distribution over possible configurations.

But the interpretation matters when the paper moves from formal differentiation to physical coherence. If the outcomes have no physical content, the distribution can tell us only how probability is allocated—not whether that allocation favors viable or integrated configurations.

## 3.3 The differentiation functional

Define

\[
\boxed{
D(p)
=
\sum_{i=1}^{4}
\left(p_i-\frac14\right)^2.
}
\]

In the historical notation of the Physics paper,

\[
C_{\mathrm{toy}}(p)\equiv D(p).
\]

The new symbol is interpretively important. \(D\) measures statistical differentiation from uniformity. It is not yet a complete coherence measure.

Expanding the square gives

\[
\begin{aligned}
D(p)
&=
\sum_i p_i^2
-\frac12\sum_i p_i
+4\left(\frac1{16}\right)\\
&=
\sum_i p_i^2-\frac14.
\end{aligned}
\]

Hence

\[
\boxed{
D(p)+\frac14=\sum_i p_i^2.
}
\]

The quantity \(\sum_i p_i^2\) is the probability that two independent samples from \(p\) return the same outcome. Thus \(D\) can be read as repeatability or concentration above the uniform baseline.

Its range on the closed simplex is

\[
0\leq D(p)\leq\frac34.
\]

The minimum occurs at \(u\). The maximum occurs at any vertex, such as

\[
(1,0,0,0).
\]

The functional therefore ranks distributions according to how strongly they select among the four outcomes.

### 3.3.1 What the ranking does and does not say

Consider:

\[
p^{(1)}
=
\left(
\frac14,\frac14,\frac14,\frac14
\right),
\]

\[
p^{(2)}
=
(0.4,0.3,0.2,0.1),
\]

\[
p^{(3)}
=
(0.7,0.1,0.1,0.1),
\]

\[
p^{(4)}
=
(1,0,0,0).
\]

Their differentiation scores are:

| Distribution | \(D(p)\) | Formal interpretation |
|---|---:|---|
| \(p^{(1)}\) | \(0\) | no outcome favored |
| \(p^{(2)}\) | \(0.05\) | mild differentiation |
| \(p^{(3)}\) | \(0.27\) | strong concentration |
| \(p^{(4)}\) | \(0.75\) | complete selection |

The ordering is mathematically legitimate. The physical interpretation is not determined until the outcomes are specified.

Suppose the four outcomes mean:

\[
x_1=\text{healthy},\quad
x_2=\text{recovering},\quad
x_3=\text{severely damaged},\quad
x_4=\text{destroyed}.
\]

Then

\[
p=(0,0,0,1)
\]

has maximal \(D\), even though it assigns certainty to destruction. Meanwhile,

\[
q=\left(\frac12,\frac12,0,0\right)
\]

has only \(D(q)=1/4\), despite concentrating entirely on viable states.

Thus:

\[
D(p)>D(q)
\]

does not imply

\[
C_{\mathrm{sub}}(p)>C_{\mathrm{sub}}(q).
\]

The sandbox measures the **strength of selection**, not the **quality of the selected states**.

### 3.3.2 Structural limitations of \(D\)

The functional is insensitive to several features that substantive coherence may require.

It does not know:

- what the outcomes represent;
- whether some outcomes are near one another or radically different;
- whether the distribution is over parts, wholes, or trajectories;
- whether components are correlated;
- whether a state is stable under perturbation;
- whether a selected state preserves the system across time;
- whether local concentration damages a larger environment.

It also assigns the same value to all permutations of a distribution. That is appropriate if the outcomes are merely labels, but inadequate if their relational positions matter.

These limitations do not invalidate \(D\). They define its scope.

## 3.4 Entropy

Define Shannon entropy on the interior simplex:

\[
\boxed{
S(p)
=
-\sum_i p_i\log p_i.
}
\]

Its maximum is

\[
S(u)=\log4.
\]

It approaches zero at a vertex.

Entropy measures the spread of the distribution relative to the four-state sample space. It does not by itself measure physical disorder, loss of every kind of structure, or movement toward equilibrium. Those interpretations require a physical model.

The contrast with \(D\) is initially intuitive:

- \(D\) is minimal at uniformity and maximal at a vertex;
- \(S\) is maximal at uniformity and minimal at a vertex.

But the two are not exact negatives of one another. There is no constant \(k\) such that

\[
D(p)=k-S(p)
\]

for every \(p\).

They summarize different features of the same three-dimensional space.

## 3.5 How differentiation and entropy can increase together

The possibility of joint increase is central to understanding the Goldilocks discussion.

Consider the transition

\[
p=(0.05,0.25,0.25,0.45)
\]

to

\[
q=(0.10,0.20,0.20,0.50).
\]

For \(p\),

\[
D(p)=0.08,
\qquad
S(p)\approx1.2023.
\]

For \(q\),

\[
D(q)=0.09,
\qquad
S(q)\approx1.2206.
\]

Both have increased.

There is no contradiction. The largest component has become larger:

\[
0.45\rightarrow0.50,
\]

which increases departure from uniformity. At the same time, the smallest component has become less suppressed:

\[
0.05\rightarrow0.10,
\]

which increases entropy. The two middle components supply the probability mass.

One contrast has sharpened while another has softened.

This is why the phrase “more structure and more disorder” is misleading. The system is not becoming more and less ordered in the same one-dimensional respect. It is moving through a multidimensional state space, and \(D\) and \(S\) respond to different features of that movement.

A better formulation is:

> **Differentiation can increase because some alternatives become more sharply distinguished, while entropy increases because probability remains distributed across a broader set of accessible alternatives.**

This possibility disappears along directions where the two gradients are exactly anti-parallel. It becomes available when the gradients oppose one another imperfectly, leaving directions with positive projection onto both.

## 3.6 Euclidean tangent gradients

The ordinary derivatives are

\[
\frac{\partial D}{\partial p_i}
=
2\left(p_i-\frac14\right)
\]

and

\[
\frac{\partial S}{\partial p_i}
=
-(\log p_i+1).
\]

Because the probabilities must continue to sum to one, the physically admissible direction is the tangent projection of these coordinate derivatives.

Since

\[
\sum_i\left(p_i-\frac14\right)=0,
\]

the differentiation gradient is already tangent:

\[
\boxed{
a(p)
=
\nabla_TD(p)
=
2(p-u).
}
\]

Let

\[
P_Tz
=
z-\frac14\left(\sum_i z_i\right)\mathbf1
\]

be Euclidean projection onto \(T_p\Delta_4\).

The tangent entropy gradient is

\[
\boxed{
b(p)
=
P_T\nabla S(p),
}
\]

with components

\[
\boxed{
b_i
=
-\log p_i
+
\frac14\sum_j\log p_j.
}
\]

The additive constant in \(\nabla S\) disappears after projection.

### 3.6.1 Intuitive reading of the gradients

The vector \(a\) points directly away from the uniform distribution in Euclidean geometry. If \(p_i>1/4\), the \(i\)-th component of \(a\) is positive; if \(p_i<1/4\), it is negative. Following \(a\) amplifies the existing deviations.

The vector \(b\) tends to raise small probabilities and lower large ones. Following \(b\) moves toward greater spread.

Thus:

\[
a:\ \text{amplify differentiation},
\]

\[
b:\ \text{increase entropy}.
\]

The words *toward* and *away* refer to a chosen geometry. A different metric changes the steepest direction even when the scalar function remains the same.

## 3.7 Alignment and the Euclidean potentiometer

Define the signed Euclidean alignment

\[
\boxed{
\mathcal A_E(p)
=
a(p)\cdot b(p).
}
\]

A direct calculation gives

\[
\begin{aligned}
\mathcal A_E(p)
&=
-2\sum_i
\left(p_i-\frac14\right)\log p_i\\
&=
-2\left[
\operatorname{KL}(p\|u)
+
\operatorname{KL}(u\|p)
\right].
\end{aligned}
\]

The bracketed quantity is the Jeffreys divergence

\[
J(p,u)
=
\operatorname{KL}(p\|u)
+
\operatorname{KL}(u\|p).
\]

Therefore

\[
\boxed{
\mathcal A_E(p)
=
-2J(p,u)
\leq0.
}
\]

The gradients never have positive Euclidean alignment in this sandbox.

Define the nonnegative opposition magnitude

\[
\boxed{
\Pi_E(p)
=
-\mathcal A_E(p)
=
2J(p,u)
\geq0.
}
\]

This distinction is essential:

- \(\mathcal A_E\) is signed alignment;
- \(\Pi_E\) is the magnitude of opposition.

Positive \(\Pi_E\) does **not** mean that entropy supports differentiation ascent. It means the entropy gradient subtracts from the differentiation gain.

The opposition vanishes only at uniformity:

\[
\Pi_E(u)=0.
\]

It diverges as any \(p_i\to0\), because

\[
\operatorname{KL}(u\|p)
\]

contains terms proportional to \(-\log p_i\).

### 3.7.1 Why call it a potentiometer?

The term is metaphorical. A potentiometer measures a relative setting or tension. Here \(\Pi_E\) quantifies how strongly the two selected gradient directions oppose one another at a point.

It is not, by itself, a measure of health, viability, complexity, or constructive balance. A large \(\Pi_E\) may simply mean that the state is close to a boundary where entropy strongly resists further concentration.

A genuine Goldilocks diagnostic must consider the weighted balance

\[
\alpha\|a\|^2-\beta\Pi_E,
\]

not \(\Pi_E\) alone.

## 3.8 Combined Euclidean flow

Introduce an auxiliary ordered parameter \(\lambda\) and define

\[
\boxed{
\frac{dp}{d\lambda}
=
v(p)
=
\alpha a(p)+\beta b(p),
\qquad
\alpha,\beta\geq0.
}
\]

At this point \(\lambda\) is a mathematical path parameter. Section 4 will ask what is required for such an ordering to acquire physical temporal meaning.

The rate of differentiation is

\[
\begin{aligned}
\frac{dD}{d\lambda}
&=
\nabla D\cdot v\\
&=
a\cdot(\alpha a+\beta b)\\
&=
\alpha\|a\|^2-\beta\Pi_E.
\end{aligned}
\]

Hence

\[
\boxed{
\frac{dD}{d\lambda}
=
\alpha\|a\|^2-\beta\Pi_E.
}
\]

Similarly,

\[
\begin{aligned}
\frac{dS}{d\lambda}
&=
b\cdot v\\
&=
\alpha a\cdot b+\beta\|b\|^2\\
&=
-\alpha\Pi_E+\beta\|b\|^2.
\end{aligned}
\]

Thus

\[
\boxed{
\frac{dS}{d\lambda}
=
-\alpha\Pi_E+\beta\|b\|^2.
}
\]

These equations display the competition exactly.

### 3.8.1 Differentiation ascent

For \(\alpha>0\) and \(\Pi_E>0\),

\[
\frac{dD}{d\lambda}>0
\]

whenever

\[
\boxed{
\frac{\beta}{\alpha}
<
\frac{\|a\|^2}{\Pi_E}.
}
\]

The differentiation drive must outweigh the entropy opposition.

### 3.8.2 Entropy ascent

Likewise,

\[
\frac{dS}{d\lambda}>0
\]

whenever

\[
\boxed{
\frac{\beta}{\alpha}
>
\frac{\Pi_E}{\|b\|^2}.
}
\]

The entropy contribution must outweigh the differentiation term’s reduction of spread.

### 3.8.3 Joint-growth wedge

Both quantities increase locally when

\[
\boxed{
\frac{\Pi_E}{\|b\|^2}
<
\frac{\beta}{\alpha}
<
\frac{\|a\|^2}{\Pi_E}.
}
\]

This interval exists when

\[
\Pi_E^2
<
\|a\|^2\|b\|^2.
\]

By Cauchy–Schwarz,

\[
\Pi_E^2
\leq
\|a\|^2\|b\|^2,
\]

with equality when \(a\) and \(b\) are collinear. Therefore a nonempty joint-growth wedge exists wherever the gradients are opposed but not exactly anti-parallel.

This is the precise mathematical meaning of simultaneous growth in the sandbox.

It does not prove that substantive coherence and thermodynamic entropy increase together in every complex system. It proves that these two toy state functionals can increase along the same multidimensional direction.

## 3.9 The discrete update

For a discrete Euler step,

\[
p^+
=
p+h v,
\]

where \(h>0\) is a finite numerical step and

\[
\sum_i v_i=0.
\]

The symbol \(h\) is reserved for discretization so that \(\eta\) can denote physical damping in Section 7. The exact change in \(D\) is

\[
\begin{aligned}
D(p^+)-D(p)
&=
\|p+h v-u\|^2-\|p-u\|^2\\
&=
2h(p-u)\cdot v
+
h^2\|v\|^2.
\end{aligned}
\]

Since

\[
a=2(p-u),
\]

we obtain

\[
\boxed{
\Delta D
=
h
\left[
\alpha\|a\|^2-\beta\Pi_E
\right]
+
h^2
\|\alpha a+\beta b\|^2.
}
\]

The second-order term has a **positive** sign because \(D\) is a positive quadratic.

A direct sufficient condition for monotone differentiation ascent is

\[
\boxed{
\alpha\|a\|^2
\geq
\beta\Pi_E.
}
\]

This condition is sufficient rather than necessary. A finite step can increase \(D\) even if the first-order rate is slightly negative, because the positive quadratic contribution may dominate.

That possibility is a numerical fact about taking a finite step. It should not be reinterpreted as evidence that the continuous vector field ascends \(D\).

### 3.9.1 Why the exact identity matters

The sign of the quadratic term determines the logic of every finite-step bound. If the term is positive, an upper bound on it cannot be used as though it were a subtractive error. Step-size conditions must instead be derived for feasibility, numerical accuracy, or control of overshoot.

This is why the analysis separates:

- continuous ascent conditions;
- finite-step changes;
- and simplex-boundary safety.

They answer different questions.

## 3.10 Feasibility inside the simplex

A tangent update preserves normalization but does not automatically preserve positivity under a finite Euler step.

Define the compact interior band

\[
\Delta_4(\epsilon)
=
\left\{
p\in\Delta_4:
p_i\geq\epsilon
\right\},
\qquad
0<\epsilon<\frac14.
\]

For

\[
a_i=2\left(p_i-\frac14\right),
\]

we have

\[
|a_i|\leq\frac32.
\]

For the centered logarithmic entropy gradient, a conservative componentwise bound is

\[
|b_i|
\leq
\log\left(\frac1\epsilon\right).
\]

Therefore

\[
|v_i|
\leq
\frac32\alpha
+
\beta\log\left(\frac1\epsilon\right).
\]

A sufficient condition ensuring

\[
p_i^+\geq\frac\epsilon2
\]

for every component is

\[
\boxed{
h
\left[
\frac32\alpha
+
\beta\log\left(\frac1\epsilon\right)
\right]
\leq
\frac\epsilon2.
}
\]

Equivalently,

\[
\boxed{
\beta
\leq
\frac{\epsilon/h-3\alpha}
{2\log(1/\epsilon)}
}
\]

when the numerator is nonnegative.

This is a **discrete feasibility condition**. It says that the Euler step is small enough not to cross the probability boundary. It says nothing by itself about substantive coherence.

The Euclidean differentiation gradient has exact supremum

\[
\boxed{
\sup_{p\in\Delta_4}
\|a(p)\|_2
=
\sqrt3,
}
\]

attained at a vertex. Indeed,

\[
\|a\|^2
=
4D
\leq3.
\]

## 3.11 Coarse-graining, grouping, and block averaging

Partition the four microstates into two blocks:

\[
A=\{1,2\},
\qquad
B=\{3,4\}.
\]

Define the macrostate probabilities

\[
q_A=p_1+p_2,
\qquad
q_B=p_3+p_4,
\]

and the projected coarse state

\[
q=\pi(p)=(q_A,q_B).
\]

The projection and its associated block-uniform reconstruction answer different questions. The projection reports the retained block masses. The reconstruction

\[
\boxed{
E_\pi p
=
\widetilde p
=
\left(
\frac{q_A}{2},
\frac{q_A}{2},
\frac{q_B}{2},
\frac{q_B}{2}
\right)
}
\]

is the maximum-entropy fine distribution compatible with those masses.

### 3.11.1 Differentiation decomposition

Define normalized coarse differentiation

\[
\boxed{
\bar D(q)
=
\frac12
\left[
\left(q_A-\frac12\right)^2
+
\left(q_B-\frac12\right)^2
\right].
}
\]

The factor \(1/2\) places the coarse quantity on the normalization induced by embedding the block masses back into the four-state space. Indeed,

\[
D(E_\pi p)=\bar D(q).
\]

Then

\[
\boxed{
D(p)=\bar D(q)+H_\pi^{(D)}(p),
}
\]

where

\[
\boxed{
H_\pi^{(D)}(p)
=
\frac12
\left[
(p_1-p_2)^2+(p_3-p_4)^2
\right]
\geq0.
}
\]

When no ambiguity is possible, the superscript is omitted and the residual is written \(H_\pi\).

For the first block,

\[
\left(p_1-\frac14\right)^2
+
\left(p_2-\frac14\right)^2
=
\frac12
\left(q_A-\frac12\right)^2
+
\frac12(p_1-p_2)^2.
\]

The same identity holds for the second block. Adding the equations proves the decomposition and gives

\[
\boxed{
D(p)-D(E_\pi p)=H_\pi^{(D)}(p).
}
\]

Thus block averaging destroys exactly the differentiation carried by within-block distinctions.

### 3.11.2 Shannon grouping identity

For \(q_A,q_B>0\), define the conditional splits

\[
t_A=\frac{p_1}{q_A},
\qquad
t_B=\frac{p_3}{q_B},
\]

with zero-mass block terms defined by continuity. Shannon entropy obeys

\[
\boxed{
S(p)
=
S(q)
+
q_Ah(t_A)
+
q_Bh(t_B),
}
\]

where

\[
h(t)=-t\log t-(1-t)\log(1-t).
\]

The within-block conditional entropy is therefore

\[
S_{\mathrm{within},\pi}(p)
=
q_Ah(t_A)+q_Bh(t_B).
\]

This quantity is not \(H_\pi^{(D)}\). At fixed block mass \(q\),

\[
\frac12q^2(2t-1)^2
\]

is maximal when \(h(t)=0\), while \(q h(t)\) is maximal when the differentiation term vanishes. The grouping identity therefore contradicts any literal identification of hidden entropy with hidden statistical differentiation.

### 3.11.3 Entropy gain under block-uniform reconstruction

Because

\[
S(E_\pi p)=S(q)+\log2,
\]

subtracting the grouping identity gives

\[
\boxed{
\Delta_\pi^{\mathrm{avg}}S(p)
:=
S(E_\pi p)-S(p)
=
q_A[\log2-h(t_A)]
+
q_B[\log2-h(t_B)]
\geq0.
}
\]

Equivalently, if

\[
r^{(A)}=(t_A,1-t_A),
\qquad
r^{(B)}=(t_B,1-t_B),
\qquad
\nu_2=\left(\frac12,\frac12\right),
\]

then

\[
\boxed{
\Delta_\pi^{\mathrm{avg}}S(p)
=
\sum_{b\in\{A,B\}}
q_b\,
\operatorname{KL}
\left(r^{(b)}\middle\|\nu_2\right).
}
\]

Hence entropy increases under this averaging map and vanishes only when each occupied block is already internally uniform.

### 3.11.4 The paired loss–gain theorem

Combining the two exact identities yields:

> **[Derived theorem]** For the stated two-block averaging map, within-block statistical differentiation is lost and Shannon entropy is gained:
> \[
> D(p)-D(E_\pi p)=H_\pi^{(D)}(p)\geq0,
> \]
> \[
> S(E_\pi p)-S(p)=\Delta_\pi^{\mathrm{avg}}S(p)\geq0.
> \]
> The two quantities vanish on the same set—distributions uniform inside each occupied block—but they are not generally equal.

For one block of mass \(q\) with split \((t,1-t)\), the paired contributions are

\[
\boxed{
\text{differentiation destroyed}
=
\frac12q^2(2t-1)^2,
}
\]

and

\[
\boxed{
\text{entropy gained}
=
q[\log2-h(t)].
}
\]

They have the same zero and, at fixed \(q\), increase monotonically with the magnitude of internal bias. Their different dependence on \(q\) prevents an identity.

The mathematically defensible statement is therefore:

> **Block averaging removes distinctions and raises entropy. The distinction loss and entropy gain are two quantitative descriptions of one averaging operation, not two names for one conserved substance.**[^entropy-history]

### 3.11.5 General finite-partition theorem

The result is not special to four states. Let an \(N\)-state space be partitioned into blocks \(B_b\) of size \(m_b\), with

\[
q_b=\sum_{i\in B_b}p_i,
\qquad
[E_\pi p]_i=\frac{q_b}{m_b}
\quad(i\in B_b).
\]

For

\[
D_N(p)=\sum_{i=1}^{N}\left(p_i-\frac1N\right)^2,
\]

orthogonal projection onto the block-constant subspace gives

\[
\boxed{
D_N(p)-D_N(E_\pi p)
=
\sum_b\sum_{i\in B_b}
\left(p_i-\frac{q_b}{m_b}\right)^2.
}
\]

Let \(r^{(b)}_i=p_i/q_b\) be the conditional distribution in an occupied block and \(\nu_{m_b}\) the uniform distribution on that block. Then

\[
\boxed{
S(E_\pi p)-S(p)
=
\sum_b q_b\,
\operatorname{KL}
\left(r^{(b)}\middle\|\nu_{m_b}\right)
\geq0.
}
\]

The equality set is identical in the two formulas: every occupied block is internally uniform. Beyond two-state blocks, however, the magnitudes induce different orderings away from that set; shared equality conditions do not make the measures interchangeable.

### 3.11.6 Attribution and theorem scope

The quadratic decomposition above is mathematically valid and useful, but its decomposable-measure structure is not novel to CU.

For equal-weight microstates whose nonnegative shares satisfy \(\sum_i p_i=1\), the generalized entropy index with parameter \(2\) may be written

\[
GE(2;p)
=
\frac{1}{2N}
\sum_{i=1}^{N}
\left[
\left(\frac{p_i}{1/N}\right)^2-1
\right]
=
\frac{N}{2}D_N(p).
\]

Thus

\[
D_N(p)=\frac{2}{N}GE(2;p),
\]

and the between/within identity for \(D_N\) is a rescaled equal-weight instance of the generalized-entropy decomposition tradition. Shorrocks (1980) characterizes the class of additively decomposable inequality measures under stated regularity restrictions; the mean-independent subclass is a one-parameter family that includes the squared coefficient of variation and the entropy measures associated with Theil (1967). The present derivation remains self-contained, but the established result must be attributed rather than presented as a new theorem.

The attribution has a positive and a limiting consequence.

First, it confirms that the identity is not a four-state numerical accident. Its generality follows from the declared quadratic object and partition structure.

Second, it does not license an exact decomposition of an arbitrary multidimensional coherence profile. A psychological, social, biological, ethical, or AI profile does not become a \(GE(2)\)-class scalar because one coordinate, indicator, or allocation inside it admits such a representation. Exact decomposition must be established coordinate by coordinate or for another explicitly defined structured object.

Nor does Shorrocks's characterization prove that no other algebraic decomposition can exist for any non-scalar object. The correct conclusion is narrower: a Shorrocks-style exact scalar decomposition cannot be imported into an arbitrary profile without showing that the target belongs to the relevant decomposable class.

The Shannon result in Sections 3.11.2–3.11.4 is a separate grouping and relative-entropy identity under the same block-uniform reconstruction. Its pairing with the quadratic residual clarifies what the averaging map does; it does not make the two quantities one measure or one conserved substance (Shannon, 1948; Theil, 1967).

### 3.11.7 What is hidden?

Consider

\[
p=\left(\frac12,0,\frac12,0\right).
\]

Then

\[
D(p)=\frac14,
\qquad
q=\left(\frac12,\frac12\right),
\qquad
\bar D(q)=0,
\]

and

\[
H_\pi^{(D)}(p)=\frac14.
\]

The coarse projection cannot distinguish this state from the uniform state, because both have the same block masses. The block-uniform reconstruction is

\[
E_\pi p=\left(\frac14,\frac14,\frac14,\frac14\right),
\]

and

\[
S(E_\pi p)-S(p)=\log2.
\]

What the projection hides is fine-grained statistical differentiation. What the reconstruction erases is that same distinction. Whether the underlying physical system has actually destroyed it, exported it, or retained it in inaccessible degrees of freedom is a further dynamical question.

### 3.11.8 Static comparison is not dynamical transfer

The decompositions above hold at each state or across one explicitly chosen averaging map. They do not imply that an arbitrary trajectory transfers differentiation into entropy.

Along a general path, \(D\) and \(S\) may both increase, both decrease, or move in opposite directions. Likewise, the identity

\[
D=\bar D+H_\pi^{(D)}
\]

by itself says nothing about which term changes in time. A monotonic transfer theorem requires a specified dynamics. Section 4 constructs one illustrative flow for \(\bar D\) and \(H_\pi^{(D)}\), while preserving the distinction between that directed flow and the static block-averaging theorem.

## 3.12 Fisher–Rao geometry

The Euclidean calculations are transparent, but probability space has a natural information geometry (Amari, 1998; Ay et al., 2017).

Equip the simplex with

\[
g_p(v,w)
=
\sum_i\frac{v_iw_i}{p_i}.
\]

For a scalar \(f\), the Fisher natural gradient is

\[
[\operatorname{grad}_Ff]_i
=
p_i
\left(
\frac{\partial f}{\partial p_i}
-
\sum_jp_j\frac{\partial f}{\partial p_j}
\right).
\]

### 3.12.1 Natural gradient of differentiation

Since

\[
\frac{\partial D}{\partial p_i}
=
2\left(p_i-\frac14\right),
\]

the weighted mean is

\[
\sum_jp_j\frac{\partial D}{\partial p_j}
=
2\left(
\sum_jp_j^2-\frac14
\right).
\]

Therefore

\[
\boxed{
A_i
:=
[\operatorname{grad}_FD]_i
=
2p_i
\left(
p_i-\sum_jp_j^2
\right).
}
\]

### 3.12.2 Natural gradient of entropy

Since

\[
\frac{\partial S}{\partial p_i}
=
-(\log p_i+1),
\]

we obtain

\[
\boxed{
B_i
:=
[\operatorname{grad}_FS]_i
=
p_i\left(-\log p_i-S(p)\right).
}
\]

Both fields are tangent:

\[
\sum_iA_i
=
\sum_iB_i
=
0.
\]

### 3.12.3 Fisher alignment

Define

\[
\mathcal A_F
=
\langle A,B\rangle_F
\]

and

\[
\boxed{
\Pi_F
=
-\mathcal A_F.
}
\]

For these particular functionals,

\[
\begin{aligned}
\mathcal A_F
&=
2\sum_i
p_i
\left(p_i-\sum_jp_j^2\right)
\left(-\log p_i-S\right)\\
&=
-2\,\operatorname{Cov}_p(p_i,\log p_i).
\end{aligned}
\]

Hence

\[
\boxed{
\Pi_F
=
2\,\operatorname{Cov}_p(p_i,\log p_i)
\geq0,
}
\]

because \(p_i\) and \(\log p_i\) are monotonically ordered. Equivalently,

\[
\Pi_F
=
\sum_{i,j}
p_ip_j
(p_i-p_j)
(\log p_i-\log p_j)
\geq0.
\]

Unlike the Euclidean quantity,

\[
\Pi_F\neq2J(p,u)
\]

in general.

The Euclidean and Fisher potentiometers must therefore remain distinct:

\[
\Pi_E=-a\cdot b,
\qquad
\Pi_F=-\langle A,B\rangle_F.
\]

## 3.13 Fisher combined flow

Consider

\[
\boxed{
\frac{dp}{d\lambda}
=
\alpha A+\beta B.
}
\]

Then

\[
\boxed{
\frac{dD}{d\lambda}
=
\alpha\|A\|_F^2-\beta\Pi_F,
}
\]

and

\[
\boxed{
\frac{dS}{d\lambda}
=
-\alpha\Pi_F+\beta\|B\|_F^2.
}
\]

The local joint-growth condition has the same geometric form:

\[
\boxed{
\frac{\Pi_F}{\|B\|_F^2}
<
\frac{\beta}{\alpha}
<
\frac{\|A\|_F^2}{\Pi_F}.
}
\]

The combined flow is the Fisher natural-gradient ascent of

\[
F(p)
=
\alpha D(p)+\beta S(p).
\]

Therefore

\[
\boxed{
\frac{dF}{d\lambda}
=
\|\operatorname{grad}_FF\|_F^2
\geq0.
}
\]

This has an important consequence. With fixed \(\alpha\) and \(\beta\), the autonomous first-order system cannot sustain a nontrivial recurrent cycle. It may display a transient in which the relative contributions of \(D\) and \(S\) change, but repeated expansion and consolidation require additional structure:

- time-dependent forcing;
- environmental feedback;
- delay;
- an additional state variable;
- non-gradient dynamics;
- or second-order inertia.

The Double Helix can remain a broader developmental hypothesis. It is not proved as a recurring cycle by this fixed first-order sandbox.

### 3.13.1 Boundary behavior

The multiplicative factors \(p_i\) in \(A_i\) and \(B_i\) cause each component of a regular continuous vector field to approach zero as \(p_i\to0\), which can support invariant-boundary behavior. A global claim that the open simplex is preserved nevertheless requires a separate well-posedness and invariance proof.

A discrete numerical update does not automatically inherit that property. Simulations require a positivity-preserving integrator, sufficiently small steps, or a coordinate system such as logits or square-root amplitudes that enforces the constraint.

### 3.13.2 Global Fisher-field bounds on \(\Delta_4\)

The compact closed simplex permits exact finite global bounds. The squared quantities can be written

\[
\|A\|_F^2
=
4\left[
\sum_i p_i^3-
\left(\sum_i p_i^2\right)^2
\right],
\]

\[
\|B\|_F^2
=
\operatorname{Var}_p(\log p_i),
\]

and

\[
\Pi_F
=
2\operatorname{Cov}_p(p_i,\log p_i).
\]

The convention \(p(\log p)^k\to0\) as \(p\to0^+\) gives continuous boundary extensions for the displayed scalar quantities.

The Karush–Kuhn–Tucker stationarity equations imply that an extremizer on the interior of any face has at most two distinct positive probability values. Exhausting all face dimensions and multiplicities reduces the global problem to one-dimensional optimization. The resulting maxima occur, up to permutation, at distributions of the form

\[
(x,y,y,y),
\qquad
y=\frac{1-x}{3}.
\]

For the differentiation gradient,

\[
\boxed{
\sup_{p\in\Delta_4}\|A\|_F
=
0.586724197682029\ldots
}
\]

at

\[
x=\frac{7+\sqrt{33}}{16}
=0.796535165408627\ldots,
\qquad
 y=0.067821611530458\ldots.
\]

The exact squared maximum is

\[
\boxed{
\sup\|A\|_F^2
=
\frac{23}{128}
+
\frac{11\sqrt{33}}{384}.
}
\]

For the entropy gradient,

\[
\boxed{
\sup_{p\in\Delta_4}\|B\|_F
=
1.011677099862651\ldots
}
\]

at

\[
x=0.851495212071545\ldots,
\qquad
y=0.049501595976152\ldots,
\]

where \(x\) is the unique root in \((1/4,1)\) of

\[
(2x-1)\log\left(\frac{3x}{1-x}\right)=2.
\]

For the opposition functional,

\[
\boxed{
\sup_{p\in\Delta_4}\Pi_F
=
0.586672264109138\ldots
}
\]

at

\[
x=0.820298289564512\ldots,
\qquad
y=0.059900570145163\ldots,
\]

where \(x\) is the unique maximizing root in \((1/4,1)\) of

\[
(12x^2-10x+1)
\log\left(\frac{3x}{1-x}\right)
=
4x-1.
\]

These constants bound the local Fisher speeds and opposition generated by the selected toy functionals. They do not establish global existence, open-simplex invariance, or physical universality. The technical supplement gives the analytic reduction and numerical verification.

### 3.13.3 Fixed coupling: stationary points and the uniform-state threshold

The wedge analysis asks whether there exists *some* coupling ratio for which both \(D\) and \(S\) increase at a given state. An actual autonomous flow instead fixes

\[
r:=\frac{\beta}{\alpha}>0.
\]

These are different questions. The wedge-degeneracy set is a geometric property of the state and remains the continuous set of nonuniform two-level distributions. At fixed \(r\), only the subset on which the combined field itself vanishes is stationary.

After rescaling by \(\alpha>0\), define

\[
\Phi_r(p)=D(p)+rS(p).
\]

An interior stationary point of either the Euclidean tangent-gradient flow or the Fisher-natural-gradient flow satisfies

\[
2\left(p_i-\frac14\right)
-r(\log p_i+1)
=\lambda
\]

for every \(i\), with one Lagrange multiplier \(\lambda\). The scalar function on the left has a strictly increasing derivative and a unique minimum for \(r>0\), so a horizontal line can meet it at no more than two positive coordinate values. Therefore every nonuniform interior stationary point is two-level. Conversely, a two-level state with values \(a>b>0\) is stationary exactly when

\[
\boxed{
 r
 =
 \frac{2(a-b)}{\log(a/b)}.
}
\]

This is the same ratio at which the two joint-growth boundaries meet, but its interpretation is now fixed-coupling stationarity rather than wedge width.

**Multiplicity convention.** In the discussion below, \(q=a/b>1\), so \(m\) counts the coordinates carrying the larger value \(a\). Reversing the labels \(a\) and \(b\) maps a branch to its complementary multiplicity. The apparent three-plus-one value \(0.6213609436\ldots\) is therefore the same unordered family as the one-plus-three branch reported below.

For a multiplicity family with \(m\) coordinates equal to \(a\) and \(4-m\) equal to \(b\), normalization gives

\[
ma+(4-m)b=1.
\]

The largest stationary coupling occurs on the one-plus-three family. Writing \(q=a/b>1\),

\[
r_1(q)
=
\frac{2(q-1)}{(q+3)\log q}.
\]

Its unique nonuniform maximum occurs at the root \(q_*>1\) of

\[
q_*^2+2q_*-3
=
4q_*\log q_*.
\]

Numerically,

\[
q_*=5.115660866489398\ldots,
\]

\[
(a_*,b_*)
=
(0.630344336788716\ldots,
 0.123218554403761\ldots),
\]

and

\[
\boxed{
 r_*
 =
 0.621360943645626\ldots .
}
\]

The two-plus-two and three-plus-one families have supremum \(1/2\), reached only in the uniform limit. It follows that

> **[Derived fixed-coupling theorem]** For \(r>r_*\), the uniform distribution is the only interior stationary point of the combined four-state flow. For \(0<r\leq r_*\), the nonuniform stationary points form a finite subset, up to permutation, of the continuous two-level wedge-degeneracy manifolds.

This does **not** mean that the wedge-degeneracy manifolds disappear above \(r_*\). Two-level states remain geometrically degenerate for every coupling; the fixed vector field simply fails to vanish on them when their critical ratio differs from the chosen \(r\).

The uniform state is stationary for every \(r\). Its tangent Hessian is

\[
\operatorname{Hess}\Phi_r(u)
=
(2-4r)I.
\]

Thus, under gradient ascent,

\[
r<\frac12
\quad\Longrightarrow\quad
u\text{ is a strict local minimum and is linearly repelling},
\]

while

\[
r>\frac12
\quad\Longrightarrow\quad
u\text{ is a strict local maximum and is locally attracting}.
\]

At the critical value \(r=1/2\), the Hessian vanishes. Writing \(p=u+\delta\), with \(\sum_i\delta_i=0\), gives

\[
\Phi_{1/2}(u+\delta)-\Phi_{1/2}(u)
=
\frac43\sum_i\delta_i^3
-
\frac83\sum_i\delta_i^4
+
O(\|\delta\|^5).
\]

The cubic term changes sign with direction—for example along \(\delta=(3\epsilon,-\epsilon,-\epsilon,-\epsilon)\). Therefore uniformity is nonhyperbolic and neither a local maximum nor a local minimum at exact criticality.

The value \(1/2\) is consequently a genuine stability-change threshold of this toy objective. It is not, by itself, a universal physical constant, a threshold for substantive coherence, or evidence that biological and social systems share the same coupling.

> **[Numerically supported sandbox hypothesis]** The interval \((1/2,r_*]\) appears to permit history-dependent persistence of differentiated states: uniformity attracts sufficiently near-uniform starts, while some already differentiated starts approach nonuniform attractors. Above \(r_*\), the tested trajectories relax to uniformity. This statement concerns only the declared four-state objective. A global theorem would additionally require stability classification of every stationary branch, treatment of boundary limit sets and basin boundaries, and a convergence argument.

## 3.14 Four meanings of “Goldilocks”

The word *Goldilocks* can refer to four mathematically and physically distinct ideas. They must be separated.

### 3.14.1 Differentiation-ascent region

For the Euclidean flow,

\[
\boxed{
\alpha\|a\|^2
\geq
\beta\Pi_E.
}
\]

For the Fisher flow,

\[
\boxed{
\alpha\|A\|_F^2
\geq
\beta\Pi_F.
}
\]

These inequalities mean only that the selected toy differentiation functional does not decrease locally.

### 3.14.2 Joint-growth wedge and its degeneracy set

Let

\[
X=\operatorname{grad}_gD,
\qquad
Y=\operatorname{grad}_gS
\]

for either the Euclidean tangent metric or the Fisher metric, and define

\[
\Pi=-\langle X,Y\rangle_g>0.
\]

The joint-growth interval is

\[
\boxed{
L
=
\frac{\Pi}{\|Y\|_g^2}
<
\frac{\beta}{\alpha}
<
\frac{\|X\|_g^2}{\Pi}
=
U.
}
\]

Introduce the normalized opposition

\[
\boxed{
\chi
=
\frac{\Pi}{\|X\|_g\|Y\|_g}
\in(0,1].
}
\]

Then

\[
L
=
\chi\frac{\|X\|_g}{\|Y\|_g},
\qquad
U
=
\frac1\chi\frac{\|X\|_g}{\|Y\|_g},
\]

so

\[
\boxed{
\frac{U}{L}=\chi^{-2},
\qquad
U-L
=
\frac{\|X\|_g}{\|Y\|_g}
\left(\chi^{-1}-\chi\right).
}
\]

The wedge has positive width exactly when the two gradients are not collinear.

For the specific \(D\) and \(S\) used here, that condition can be characterized completely.

> **[Derived theorem]** At a nonuniform interior point of \(\Delta_4\), the Euclidean and Fisher joint-growth wedges are strict if and only if the four coordinates of \(p\) contain at least three distinct values. The wedge collapses exactly when \(p\) has only two distinct probability values. At the uniform point both gradients vanish and the wedge ratios are undefined.

To see the structure, collinearity requires \(\log p_i\) to be affine in \(p_i\) on the set of distinct coordinate values. Strict concavity of \(\log\) excludes three distinct intersections with one affine function. Any two-level distribution, by contrast, makes the two centered score fields one-dimensional and therefore exactly antiparallel.

If the two values are \(a>b>0\), then

\[
Y=-kX,
\qquad
k=\frac{\log(a/b)}{2(a-b)},
\]

for both geometries. The two wedge edges meet at the derived critical coupling

\[
\boxed{
r_c
:=
\frac{\beta}{\alpha}
=
\frac{2(a-b)}{\log(a/b)}.
}
\]

At \(r_c\), the combined vector field vanishes; on either side, one of \(D\) or \(S\) increases while the other decreases. There is no positive-width joint-growth interval on the two-level set.

As \(p\) approaches the full-support uniform state,

\[
X\sim\frac12\delta,
\qquad
Y\sim-\delta
\]

in Fisher coordinates, and both wedge edges approach

\[
\frac{\beta}{\alpha}=\frac12.
\]

The width tends to zero. More generally, tuning becomes increasingly precise as a trajectory approaches any two-level degeneracy manifold. Random sampling almost surely misses these lower-dimensional sets, so numerical evidence that the wedge is nonempty at randomly selected interior points is not a proof of strictness everywhere.

The mathematical “Goldilocks” result is therefore not a universally comfortable band. It is a state-dependent wedge whose width measures the failure of exact opposition and which can collapse on structurally natural families of states.

Section 3.13.3 adds the fixed-coupling question. The geometric degeneracy set remains continuous, but for a selected \(r=\beta/\alpha\) its stationary intersection is finite and disappears entirely above \(r_*=0.6213609436\ldots\). This distinction prevents “wedge collapse,” “critical point,” and “stationary state of a chosen flow” from being used as synonyms.

### 3.14.3 Discrete feasibility region

This is a condition on step size and coefficients that prevents a numerical update from leaving the simplex. It concerns the integrator, not the physical quality of the state.

### 3.14.4 Developmental Goldilocks regime

This is the broader CU hypothesis that complex adaptive systems require enough variability to explore alternatives and enough constraint to consolidate useful structure.

The developmental idea is plausible and important, but it is not identical to any one of the mathematical inequalities above. To establish it in a physical domain, the model must specify:

- the viability constraints;
- the mechanism generating variability;
- the mechanism selecting or stabilizing structure;
- the relevant scales;
- and the criterion for successful persistence.

A biological organism, an open quantum system, and a society may each exhibit a Goldilocks regime for different reasons. The toy simplex does not prove one universal band shared by all of them.

## 3.15 From differentiation to substantive coherence

To turn the sandbox into a physical coherence model, the four outcomes must represent actual configurations

\[
X=\{x_1,x_2,x_3,x_4\}.
\]

The model must then answer:

- Which constraints determine whether a configuration persists?
- Which relations among components count as integration?
- Which coarse-grainings preserve the system’s identity?
- Over what interval must that identity remain robust?
- What perturbations define stability?
- How is local persistence related to global cost?

A minimal starting point is

\[
C_K(p)
=
\sum_i p_i\,c_K(x_i).
\]

A richer model may require:

\[
C_{\mathrm{sub}}
=
C_K
+
\lambda I_G
-
\mu F_T
-
\nu L_\pi.
\]

The equation is schematic, but the distinction is exact:

\[
\boxed{
D(p)\ \text{measures how strongly possibilities are distinguished;}
}
\]

\[
\boxed{
C_{\mathrm{sub}}\ \text{must measure how probable configurations
satisfy and integrate actual constraints}.
}
\]

Statistical differentiation may carry coherence. It is not sufficient for coherence.

## 3.16 What the sandbox establishes

The classical sandbox establishes the following results internally:

1. \(D\) is squared Euclidean distance from uniformity.
2. \(D+\tfrac14\) is the probability of agreement between two independent draws.
3. \(D\) ranges from \(0\) at uniformity to \(3/4\) at a vertex.
4. The Euclidean tangent gradient is
   \[
   a=2(p-u).
   \]
5. The projected entropy gradient is
   \[
   b_i=-\log p_i+\frac14\sum_j\log p_j.
   \]
6. Their Euclidean alignment is
   \[
   \mathcal A_E=-2J(p,u),
   \]
   and the opposition magnitude is \(\Pi_E=2J(p,u)\).
7. Exact continuous rates for \(D\) and \(S\) follow, as does the exact finite-step identity with its positive quadratic term.
8. A local joint-growth wedge exists wherever the gradients are not exactly antiparallel. For these functionals on \(\Delta_4\), it collapses exactly on nonuniform two-level distributions and at uniformity becomes undefined because both gradients vanish.
9. A conservative step-size condition keeps Euler updates inside an interior simplex band.
10. Fine differentiation decomposes exactly into coarse-accessible and within-block differentiation.
11. Shannon entropy independently obeys its grouping identity; within-block entropy is not within-block differentiation.
12. The associated block-uniform averaging map removes exactly the within-block differentiation and increases entropy by a weighted KL divergence. The two changes share an equality set but are not equal.
13. The block-averaging theorem extends to arbitrary finite partitions.
14. The Fisher natural gradients use a \(p\)-weighted projection, and the Fisher opposition \(\Pi_F\) is distinct from the Euclidean Jeffreys expression.
15. The selected Fisher fields have finite global bounds on the closed simplex:
   \[
   \sup\|A\|_F=0.586724197682029\ldots,
   \]
   \[
   \sup\|B\|_F=1.011677099862651\ldots,
   \]
   \[
   \sup\Pi_F=0.586672264109138\ldots.
   \]
16. A fixed-coefficient Fisher gradient flow is Lyapunov ascent of \(\alpha D+\beta S\) and cannot generate a sustained cycle.

It does not establish:

- that nonuniform distributions are intrinsically more coherent;
- that hidden differentiation is necessarily hidden physical organization;
- that Shannon, von Neumann, or thermodynamic entropy is a conserved form of coherence;
- that applying a reduced description physically destroys the omitted distinctions;
- that a Goldilocks band is universal or uniformly wide;
- or that first-order gradient flow is the foundational dynamics of the universe.

The value of the sandbox is that these limits are now visible from inside the formalism rather than imposed from outside it.

## 3.17 Transition to ordered change

The sandbox contains states, scalar functionals, and parameterized paths. It has not yet established physical time.

The symbol \(\lambda\) orders points along a mathematical curve. To interpret such an order temporally, the framework must explain:

- what makes one transition an admissible continuation of another;
- how transition events can be consistently ordered;
- what permits an order to be represented by a clock;
- and what distinguishes temporal order from a preferred temporal direction.

Those are the tasks of Section 4.

---

# 4. Lawful Transitions, Ordered Updates, Time, and Temporal Direction

## 4.1 Why time must be separated into several questions

The claim that time emerges is often stated too quickly.

A framework may begin with a sequence of states,

\[
x_0,x_1,x_2,\ldots,
\]

call the index “time,” and then claim that temporal order has been derived. But the sequence notation already contains an ordering. A differential equation

\[
\frac{dx}{dt}=F(x)
\]

already assumes a parameter with respect to which change is measured. Renaming that parameter after the calculation does not explain why physical events possess temporal order or why one orientation is experienced as future-directed.

CU therefore separates four questions:

1. What makes a transition lawful?
2. What makes transitions consistently orderable?
3. What allows the order to be represented by a clock and interval?
4. What selects an arrow rather than merely an order?

These questions correspond to different rungs of the physical ladder. They may ultimately be realized together in a mature physical theory, but they should not be conflated in the derivation.

## 4.2 Static comparisons are not histories

A state space can carry functions before it carries a physical history.

For two distributions \(p\) and \(q\), one may write

\[
D(p)>D(q)
\]

or

\[
S(p)<S(q).
\]

These statements compare values. They do not say that \(q\) became \(p\), that one occurred earlier, or that a quantity increased.

The distinction is analogous to comparing elevations on a map. One point may be higher than another without anyone having traveled between them. Elevation difference is not ascent. Ascent requires a path and an orientation along that path.

Likewise:

\[
\boxed{
\text{comparison of states}
\neq
\text{change along an ordered history}.
}
\]

This resolves an important ambiguity in the sandbox. Shannon entropy can be defined on a probability distribution before physical time is introduced. But **entropy increase** requires an ordered trajectory, and **entropy production** requires a physical interpretation of that trajectory and its direction.

## 4.3 Lawful transition relations

Let

\[
\mathcal X_K
\]

be the set of configurations satisfying a kinematic constraint set \(K\).

A lawful transition structure may be represented by a binary relation

\[
R\subseteq\mathcal X_K\times\mathcal X_K,
\]

where

\[
R(x,y)
\]

means that \(y\) is an admissible transform or continuation of \(x\).

Alternatively, one may specify a family of maps

\[
U_\lambda:\mathcal X_K\rightarrow\mathcal X_K.
\]

At this stage, \(\lambda\) is a label for a transformation family, not necessarily physical time.

A directed graph gives the simplest picture:

- vertices represent configurations;
- directed edges represent allowed transitions;
- absent edges represent forbidden transitions;
- edge labels may encode cost, propensity, or transformation type.

The graph contains more structure than an unordered set of states, but it does not yet contain elapsed duration.

### 4.3.1 “Successor” before time

The word *successor* can be used structurally. In logic, computation, and graph theory, one object may succeed another in an ordering rule without implying that the objects exist inside an independently given temporal container.

This is the intended meaning at the pre-temporal stage:

> Given \(x\), the rules identify \(y\) as an admissible continuation.

The language remains delicate because ordinary verbs are temporal. The formal relation carries the argument more reliably than the metaphor.

### 4.3.2 Lawfulness is more than a gradient

A gradient identifies a locally distinguished direction relative to a scalar and a metric. It does not by itself establish that nature follows that direction.

To obtain a dynamical law, the framework must specify at least:

- the state space;
- the metric or symplectic structure;
- the relevant scalar, Hamiltonian, or generator;
- boundary conditions;
- and the rule connecting the generator to transitions.

This is why the existence of a coherence gradient is not yet a history. It provides directional structure from which a law may be built.

## 4.4 From transitions to ordered events

Let \(\mathcal E\) be a set of realized or realizable transition events.

A strict order relation

\[
\prec
\]

on \(\mathcal E\) is required to satisfy:

1. **Irreflexivity**
   \[
   e\nprec e.
   \]

2. **Transitivity**
   \[
   e_1\prec e_2
   \ \text{and}\
   e_2\prec e_3
   \Rightarrow
   e_1\prec e_3.
   \]

3. **Acyclicity of realized chains**  
   No event precedes itself through a sequence of actual transitions.

4. **Coarse-graining compatibility**  
   If two events remain distinct under an admissible projection, the projection does not reverse their order.

Universal comparability is not required. Two independent events may satisfy neither

\[
e_1\prec e_2
\]

nor

\[
e_2\prec e_1.
\]

A partial order is therefore more appropriate than a total order at the foundational level. This is compatible with the possibility that local chains are ordered even when the whole event structure admits no single universal sequence.

**[Bridge principle]** Temporal order becomes available when lawful transitions instantiate a stable precedence relation of this kind.

This is an enablement claim. It is not derived from the four-state sandbox alone.

### 4.4.1 Order as preserved distinction

Why should order matter to coherence?

An ordered chain preserves a distinction among positions in a history. The configuration labeled “earlier” is not interchangeable with the configuration labeled “later” relative to the transition structure. If all updates could be permuted without changing any relation, no temporal precedence would be present.

Order is therefore one more kind of relational differentiation. It organizes change without yet assigning a metric duration or a preferred arrow.

## 4.5 Clocks and temporal parameterization

An ordered set does not automatically possess a physical clock.

On an ordered chain, a real-valued clock is an order-preserving map

\[
\tau:\mathcal E\rightarrow\mathbb R
\]

such that

\[
e_1\prec e_2
\Rightarrow
\tau(e_1)<\tau(e_2).
\]

The map labels the order numerically.

Not every partial order admits one globally faithful real-valued representation without additional conditions. Local chains, multiple clock functions, or a foliation into ordered families may be required.

Even when \(\tau\) exists, it is not unique. If \(f\) is strictly increasing, then

\[
f\circ\tau
\]

represents the same order.

Thus order alone determines only an ordinal structure:

\[
\text{before},\quad
\text{after},\quad
\text{incomparable}.
\]

It does not determine metric duration.

To compare intervals, a theory needs additional regularity. A clock is a physical process whose successive states can serve as a reproducible standard. Periodic motion, decay, oscillation, or another stable dynamical pattern may supply such a standard after the relevant physics is available.

The minimal CU claim is therefore:

\[
\boxed{
\text{time begins as an index of ordered change,
not as a pre-existing container}.
}
\]

The stronger task—recovering the quantitative temporal structure of relativity or quantum theory—requires much more.

## 4.6 Two senses of temporal emergence

The word *emergence* is used in two related but distinct senses.

### 4.6.1 Logical emergence

Temporal concepts become definable once the lower-level structures they require are available:

\[
\text{distinguishable configurations}
\rightarrow
\text{lawful transitions}
\rightarrow
\text{ordered events}
\rightarrow
\text{clock parameterization}.
\]

This is the primary meaning of the Coherence Ladder.

### 4.6.2 Dynamical emergence

An effective temporal description may arise from a deeper theory in which ordinary clock time is not fundamental. Collective variables, semiclassical regimes, records, or correlations may support a stable time parameter only in certain limits.

The present paper develops the logical architecture more fully than the physical mechanism. It identifies what a mechanism must deliver without claiming that the four-state sandbox already delivers it.

## 4.7 When entropy becomes temporal

Before temporal ordering, entropy is a scalar function on state space:

\[
S:\mathcal X\rightarrow\mathbb R.
\]

After an ordered path

\[
p(\tau)
\]

has been defined, an entropy rate becomes meaningful:

\[
\frac{dS}{d\tau}.
\]

But even this derivative is not automatically thermodynamic entropy production. The interpretation depends on:

- what the state variables represent;
- which degrees of freedom have been coarse-grained;
- whether \(\tau\) is physical time;
- and whether the entropy has the relevant thermodynamic meaning.

The hierarchy is:

\[
\boxed{
S(p)
\ \text{as state value}
}
\]

\[
\downarrow
\]

\[
\boxed{
\frac{dS}{d\lambda}
\ \text{along an ordered mathematical path}
}
\]

\[
\downarrow
\]

\[
\boxed{
\frac{dS}{dt}
\ \text{as physical entropy rate}
}
\]

\[
\downarrow
\]

\[
\boxed{
\frac{dS}{dt}\geq0
\ \text{as an effective arrow under stated conditions}.
}
\]

This sequence prevents entropy from being used to create the time already required to speak of entropy increase.

## 4.8 Order is not an arrow

A reversible trajectory can still be ordered.

Suppose a dynamics admits

\[
x_0\leftrightarrow x_1\leftrightarrow x_2.
\]

A history can be parameterized so that

\[
x_0
\prec
x_1
\prec
x_2.
\]

The equations may also admit the reversed history.

Temporal order identifies positions along a history. A temporal arrow identifies an orientation that is physically privileged or overwhelmingly typical.

The distinction is:

\[
\boxed{
\text{consistent precedence}
\Rightarrow
\text{temporal order},
}
\]

whereas

\[
\boxed{
\text{directed irrecoverability or asymmetric law}
\Rightarrow
\text{an effective temporal arrow}.
}
\]

An arrow may arise through:

- a dissipative law with a Lyapunov function;
- asymmetric boundary conditions;
- environmental degrees of freedom that become inaccessible;
- many-to-one coarse descriptions;
- stable records that accumulate in one orientation;
- or practical inability to reverse dispersed correlations.

No single item on this list should be treated as sufficient without a model.

### 4.8.1 Why coarse-graining alone is not enough

A coarse-graining

\[
\pi:\mathcal X\rightarrow\bar{\mathcal X}
\]

may be many-to-one. Several fine states can produce the same macrostate. Therefore the macrostate does not determine the fine state uniquely.

This establishes non-invertibility of the description:

\[
\bar x
\not\Rightarrow
x.
\]

It does not establish that nature must move from fine distinguishability toward coarse indistinguishability. A direction still has to be selected by a law, a boundary condition, or a typicality argument.

A map can erase distinctions mathematically. A temporal arrow requires an account of why physical histories overwhelmingly instantiate the erasing orientation.

## 4.9 Coarse-grained histories and accessibility loss

Suppose the fine state evolves reversibly under

\[
U_t,
\]

while an observer or subsystem accesses only

\[
\bar x(t)
=
\pi(U_tx_0).
\]

Even if \(U_t\) is invertible, \(\bar x(t)\) may fail to determine \(x_0\). Distinct fine histories can produce the same coarse history.

The reduced evolution may then appear:

- stochastic;
- dissipative;
- non-Markovian;
- or practically irreversible.

The CU interpretation is:

\[
\boxed{
\text{fine relational structure may persist
while its reconstruction becomes inaccessible}.
}
\]

This interpretation unifies a pattern without erasing differences among domains. In classical statistical mechanics, fine phase-space correlations may be neglected. In open quantum systems, correlations with an environment may make local phase relations unavailable. In horizon physics, causal structure restricts what can be accessed by an exterior observer.

The physical mechanisms are not interchangeable. The common structure is restricted access to a larger relational state.

## 4.10 Records and temporal orientation

A record is a stable present correlation that carries information about another event.

Records matter because an arrow of time is not experienced merely as increasing entropy. It is experienced as an asymmetry of access: the present contains traces of what is called the past and not comparable traces of what is called the future.

A complete CU account would need to explain why record-forming correlations accumulate in one orientation of the ordered history. Coarse-graining can help by dispersing fine information into many degrees of freedom, making reversal increasingly inaccessible to local control.

But the existence of records should not be assumed in the definition of time. Records require persistence, interaction, and an already orderable sequence. They belong to the emergence of a robust arrow, not to the minimal existence of precedence.

## 4.11 An illustrative conservative accessibility flow

The classical decomposition

\[
D=\bar D+H_\pi
\]

suggests a specific mathematical question:

> Can a flow conserve total differentiation while monotonically transferring it from the coarse-accessible component to the hidden component?

Let

\[
N
=
\operatorname{grad}_FD
\]

and

\[
G_\pi
=
\operatorname{grad}_F(\bar D\circ\pi).
\]

For \(N\neq0\), define the Fisher-orthogonal projector onto the tangent space of the constant-\(D\) surface:

\[
\boxed{
P_NX
=
X
-
\frac{\langle X,N\rangle_F}
{\langle N,N\rangle_F}
N.
}
\]

Choose the directed flow

\[
\boxed{
\dot p
=
-P_NG_\pi.
}
\]

At the uniform state, where \(N=0\), define

\[
\dot p=0.
\]

The total differentiation rate is

\[
\begin{aligned}
\frac{dD}{dt}
&=
\langle N,\dot p\rangle_F\\
&=
-\langle N,P_NG_\pi\rangle_F\\
&=
0.
\end{aligned}
\]

The accessible differentiation rate is

\[
\begin{aligned}
\frac{d\bar D}{dt}
&=
\langle G_\pi,\dot p\rangle_F\\
&=
-\langle A,P_NG_\pi\rangle_F\\
&=
-\|P_NG_\pi\|_F^2\\
&\leq0.
\end{aligned}
\]

Since

\[
H_\pi=D-\bar D,
\]

we obtain

\[
\boxed{
\frac{dH_\pi}{dt}
=
\|P_NG_\pi\|_F^2
\geq0.
}
\]

Thus:

\[
\boxed{
\frac{dD}{dt}=0,
\qquad
\frac{d\bar D}{dt}\leq0,
\qquad
\frac{dH_\pi}{dt}\geq0.
}
\]

### 4.11.1 What the theorem says

**[Conditional result]** Given this directed conservative flow:

- total statistical differentiation is conserved;
- coarse-accessible differentiation decreases;
- hidden within-block differentiation increases.

The theorem demonstrates how an accessibility arrow can be represented as Lyapunov monotonicity.

**Scope of the theorem.** These identities are pointwise Lyapunov statements on the region where \(N=\operatorname{grad}_F D\neq0\). They do not by themselves establish global existence or uniqueness of solutions, preservation of the open simplex for all time, convergence, or the form of an asymptotic state. At the uniform point, where \(N=0\), the projected formula is undefined and the flow is defined separately to vanish.

### 4.11.2 What the theorem does not say

The theorem does not derive the direction from geometry alone.

The minus sign in

\[
\dot p=-P_NG_\pi
\]

selects decreasing accessible differentiation. The reverse law

\[
\dot p=+P_NG_\pi
\]

would produce the opposite monotonicities.

The geometry provides the projection and the decomposition. The selected law provides the orientation.

The result should therefore not be described as proving the thermodynamic arrow in two lines. It proves a monotonicity theorem **conditional on a directed law**. It also concerns the decomposition of \(D\), not Shannon entropy: \(H_\pi^{(D)}\) is hidden differentiation, and its increase along this flow is not an entropy-production theorem. The block-averaging entropy result of Section 3.11 is a different statement about a different map.

### 4.11.3 Why the example is still valuable

The flow clarifies the conceptual ingredients an arrow model requires:

1. a conserved or globally tracked quantity;
2. an access-relative decomposition;
3. a law tangent to the conserved surface;
4. a Lyapunov quantity that changes monotonically;
5. a physical reason for selecting one sign of the law.

The fifth ingredient remains open.

## 4.12 Relation to metriplectic and nonequilibrium structures

The pattern “one functional conserved, another monotone” resembles metriplectic or GENERIC formulations in nonequilibrium thermodynamics (Morrison & Updike, 2024). Such frameworks combine reversible and dissipative structures while imposing degeneracy conditions so that the dissipative part preserves selected invariants.

The projection above satisfies an analogous condition:

\[
\langle N,\dot p\rangle_F=0.
\]

The correspondence is suggestive rather than established.

A complete connection would require:

- a specified Poisson structure for the reversible sector;
- a positive dissipative bracket;
- proof of the relevant degeneracy conditions;
- compatibility with the simplex boundary;
- and a physical derivation of the coarse variables and access map.

The comparison identifies a promising mathematical neighborhood. It does not import the full physical interpretation of nonequilibrium thermodynamics into the toy flow.

## 4.13 Relation to second-order dynamics

The later Hamiltonian formulation uses a temporal parameter in a second-order equation:

\[
\frac{D\dot\rho}{dt}
=
-\operatorname{grad}_FV.
\]

This does not by itself solve the emergence of time. The equation belongs to the level at which ordered change and clock parameterization have already become available.

The relationship among the levels should be read as:

\[
\text{pre-temporal transition structure}
\]

\[
\downarrow
\]

\[
\text{ordered histories and clocks}
\]

\[
\downarrow
\]

\[
\text{second-order physical dynamics in }t.
\]

Once \(t\) is available, the Hamiltonian equation can explain oscillation, waves, reversible motion, and the damped emergence of first-order flow. It should not be used retroactively as the derivation of the order it presupposes.

This distinction also resolves a tension in the framework.

- Logical priority belongs to pure structure and ordered transitions.
- Dynamical fundamentality, within time-parameterized physics, may belong to the second-order Hamiltonian form.
- First-order gradient flow may be an environmentally damped effective regime.

These claims can all be true because they answer different questions.

## 4.14 Foundational time symmetry and emergent asymmetry

In the absence of damping and explicit time dependence, the Hamiltonian CU equation is time-reversal invariant. If \(\rho(t)\) is a solution, the reversed trajectory \(\rho(-t)\) is also available under the usual velocity reversal.

The experienced arrow must therefore enter through additional structure:

- damping;
- coarse-graining;
- inaccessible environmental correlations;
- asymmetric boundary conditions;
- special initial conditions;
- or selection of a dissipative branch.

The layered picture is:

\[
\begin{aligned}
&\text{lawful transitions}\\
&\downarrow\\
&\text{ordered histories}\\
&\downarrow\\
&\text{clock parameterization}\\
&\downarrow\\
&\text{reversible physical dynamics}\\
&\downarrow\\
&\text{coarse-grained irrecoverability}\\
&\downarrow\\
&\text{effective temporal arrow}.
\end{aligned}
\]

The order of the middle terms may vary among specific physical models, but the conceptual distinctions should remain explicit.

## 4.15 Computation on the ladder

The physical ladder places computation after time because computation is not merely a static mapping from inputs to outputs. An actual computation is an ordered realization of state transitions according to a rule.

A formal function

\[
f:X\rightarrow Y
\]

can be specified timelessly. A process that computes \(f\) requires an ordered implementation:

\[
x_0
\rightarrow
x_1
\rightarrow
\cdots
\rightarrow
x_n.
\]

Memory requires that distinctions from earlier stages remain accessible at later stages. Error correction requires comparison between expected and actual transitions. Both depend on stable ordering and persistence.

This is why ordered updates do more than provide a label for change. They make rule-governed transformation and record-bearing processes possible.

## 4.16 What Section 4 establishes

Section 4 establishes a conceptual hierarchy and one illustrative theorem.

It establishes that:

1. state functionals can be defined without physical time;
2. comparisons among states are not histories;
3. a gradient supplies directional structure but not an actual law;
4. lawful transition relations can be specified without elapsed duration;
5. temporal order requires a stable precedence structure;
6. foundational order may be partial rather than total;
7. a clock is an order-preserving representation, not the order itself;
8. metric duration requires additional physical regularity;
9. entropy increase requires an ordered path;
10. temporal order does not by itself select a temporal arrow;
11. many-to-one coarse-graining creates non-invertibility of description but does not alone choose a direction;
12. a specified directed conservative flow can transfer accessible differentiation into hidden differentiation monotonically;
13. that monotonicity is conditional on the chosen sign of the law;
14. reversible second-order dynamics and emergent thermodynamic asymmetry can occupy different explanatory levels.

The section does not establish:

- that one unique temporal order follows from pure structure;
- that every partial order admits one global clock;
- that the illustrative flow is nature’s fundamental dynamics;
- that coarse-graining alone explains the thermodynamic arrow;
- or that physical duration has been derived from the sandbox.

Its strongest conclusion is structural:

\[
\boxed{
\text{difference permits transition;}
\quad
\text{lawful transition permits order;}
\quad
\text{order permits time;}
\quad
\text{directed irrecoverability permits an arrow}.
}
\]

This sequence gives the framework a disciplined way to discuss time without treating it as either an unexplained background or a consequence of equations that already assume it.

---

# 5. From Classical Accessibility to Quantum State Space

The classical sandbox established a limited but important fact: a description can lose access to distinctions that remain present at a finer level. A coarse-graining may map many fine states to the same coarse state, and the resulting loss of recoverability can support an effective arrow of time. None of this, however, is distinctively quantum. Classical probability already contains joint distributions, correlations, marginalization, hidden variables, and irreversible stochastic maps. A valid transition to quantum theory must therefore identify a stronger requirement than the mere existence of globally encoded structure that is absent from a local marginal.

This section rebuilds that transition around two ideas that are closer to the central commitments of Coherence Universalism.

The first is **purificational accessibility**: an operationally mixed state may arise as the restriction of a globally pure state, and an effectively irreversible process may arise by restricting access to a globally reversible interaction. The second is **contextual accessibility**: the descriptions available in different compatible measurement contexts need not be restrictions of one classical assignment of simultaneous values to every possible measurement.

These are not consequences of the four-state sandbox. They are bridge principles. Their importance is that they turn CU’s distinction between coherence and accessibility into mathematically discriminating demands. Classical probability can hide correlations. What a finite classical simplex cannot do is represent a nontrivially mixed local state as the marginal of a globally pure classical state. Quantum theory can. Likewise, a single classical sample space can represent context-dependent observations only when the contextual statistics admit a common global refinement. Quantum theory includes experimentally relevant families for which no such noncontextual refinement exists (Abramsky & Brandenburger, 2011).

The conclusion will therefore be conditional rather than absolute:

\[
\boxed{
\text{CU does not derive quantum theory from hidden correlation alone.}
}
\]

Instead,

\[
\boxed{
\begin{array}{c}
\text{purificational accessibility}\\
+\ \text{contextual accessibility}\\
+\ \text{further operational assumptions}
\end{array}
\quad
\Longrightarrow
\quad
\text{quantum theory within an appropriate reconstruction class}.
}
\]

This is less rhetorically immediate than the original argument, but it is conceptually stronger. It identifies exactly what classical probability can already accomplish, exactly where an additional nonclassical commitment enters, and exactly what further assumptions are required before quantum theory can be said to follow.

## 5.1 What classical probability can already do

A classical probability distribution is not confined to isolated variables. It may be defined over a composite sample space and thereby encode relational structure that is invisible in either subsystem considered alone.

Let two bits \(A\) and \(B\) have the ordered joint state space

\[
00,\quad 01,\quad 10,\quad 11.
\]

Consider the two distributions

\[
p_{+}
=
\left(
\frac12,0,0,\frac12
\right)
\]

and

\[
p_{-}
=
\left(
0,\frac12,\frac12,0
\right).
\]

For \(p_{+}\), the bits always agree. For \(p_{-}\), they always disagree. Yet both one-bit marginals are uniform:

\[
p_A=p_B=
\left(
\frac12,\frac12
\right).
\]

An observer with access only to \(A\), or only to \(B\), cannot determine which global distribution is present. An observer with joint access can distinguish them immediately by asking whether the bits agree.

This is already a clear case of global relational structure that is unavailable locally. Classical probability has no difficulty representing it. The global distribution contains a correlation; the marginalization map removes access to that correlation; and different global states can have identical reduced statistics.

The same point can be made dynamically. A classical system and environment may become correlated. Once the environment is ignored, the system may be described by a stochastic transition even though the larger system is described deterministically at a finer level. Classical statistical mechanics routinely uses this structure.

It follows that the claim

\[
\text{“classical probability cannot represent hidden global correlation”}
\]

is false. It also follows that the existence of many-to-one coarse-graining does not by itself force a nonclassical state space. Many-to-one maps are ubiquitous in classical theory.

This correction is not a retreat from the CU program. It clarifies the problem CU must solve. The distinction between global structure and local accessibility is broader than quantum theory. Quantum theory becomes relevant only when the form of globally preserved structure satisfies conditions that a classical simplex cannot satisfy.

## 5.2 What is distinctive about a classical simplex

A finite classical state space with \(n\) mutually exclusive possibilities is represented by the simplex

\[
\Delta_{n-1}
=
\left\{
p_i\geq0,\;
\sum_i p_i=1
\right\}.
\]

Its pure states are the vertices

\[
e_1,\ldots,e_n.
\]

Every mixed state has a unique decomposition into these classical pure states:

\[
p=\sum_i p_i e_i.
\]

The word *unique* is important. It does not mean that there is only one verbal story one can tell about how the mixture was prepared. It means that, once the classical alternatives represented by the vertices are fixed, the state itself specifies one unique set of weights over them.

For a classical composite \(AB\), a pure joint state is a definite pair:

\[
p_{AB}(a,b)
=
\delta_{a,a_0}\delta_{b,b_0}.
\]

Marginalizing over \(B\) gives

\[
p_A(a)
=
\sum_b p_{AB}(a,b)
=
\delta_{a,a_0}.
\]

Therefore:

\[
\boxed{
\text{classically pure global state}
\Longrightarrow
\text{pure local marginals}.
}
\]

A mixed classical marginal is possible, but only when the global classical state is itself mixed. For example, the correlated distribution \(p_{+}\) above produces mixed marginals, but \(p_{+}\) is not a vertex of the four-outcome simplex. It is a probabilistic mixture of the definite states \(00\) and \(11\).

This gives a precise contrast among three claims:

1. Classical theory can represent a local observer who does not know the global state.
2. Classical theory can represent mixed local marginals generated by a mixed correlated global distribution.
3. Classical finite simplex theory cannot represent a genuinely mixed local marginal as the restriction of a globally pure classical state.

Only the third claim distinguishes the classical simplex from quantum theory.

The same contrast appears in reversible dynamics. A reversible finite classical transformation permutes the vertices of the joint simplex. If a system and its environment begin in one definite joint state, a permutation maps them to another definite joint state. Discarding the environment then leaves a definite system state. To obtain a nontrivial stochastic channel from reversible classical dynamics, uncertainty must already be placed in the environment, the preparation, or the observer’s description.

This does not make classical statistical mechanics defective. It tells us what kind of explanatory work it performs. Classical theory can relocate apparent randomness into inaccessible but already-random global conditions. It does not, in the finite simplex setting, turn a globally pure state into locally mixed states through reversible interaction alone.

## 5.3 The stronger CU question

The corrected transition to quantum theory begins with a stronger question:

> Can the loss of local accessibility be represented without treating the encompassing state as itself mixed or incomplete?

This is a natural question for CU because the framework distinguishes what is globally instantiated from what is locally accessible. If local uncertainty always required global uncertainty, then the local–global distinction would remain comparatively weak. A stronger form of the distinction becomes possible when:

\[
\text{the whole is pure and completely specified}
\]

while

\[
\text{the accessible part is mixed and incomplete}.
\]

Here *pure* is used in its technical convex sense. A pure state is an extremal state, one that cannot be expressed as a nontrivial probabilistic mixture of other states in the same theory. Purity should not be identified with moral goodness, substantive coherence, simplicity, or absence of internal relation.

Likewise, *mixed* does not necessarily mean that reality is objectively indeterminate. It means that the operational state lies in the interior of the convex state space rather than at an extremal point. Why it is mixed depends on the theory and the physical situation.

The CU-motivated demand is therefore not that every uncertainty be declared illusory. It is that a formalism be able to distinguish at least two possibilities:

- the encompassing state is itself mixed;
- the encompassing state is pure, but the observer or subsystem has access only to a restriction.

Quantum theory represents both.

This stronger distinction gives mathematical form to an intuition that appears throughout the framework: absence from a local description need not imply absence from the whole. But the statement is now precise enough to be tested against candidate state spaces.

## 5.4 Quantum purification

Let \(\rho_A\) be a finite-dimensional density operator with spectral decomposition

\[
\rho_A
=
\sum_i
\lambda_i
|i\rangle\langle i|,
\qquad
\lambda_i\geq0,
\qquad
\sum_i\lambda_i=1.
\]

Introduce an auxiliary system \(B\) with an orthonormal family \(\{|i\rangle_B\}\), and define

\[
|\Psi\rangle_{AB}
=
\sum_i
\sqrt{\lambda_i}\,
|i\rangle_A|i\rangle_B.
\]

The joint density operator is pure:

\[
\rho_{AB}
=
|\Psi\rangle\langle\Psi|,
\qquad
\operatorname{Tr}(\rho_{AB}^2)=1.
\]

Yet tracing over \(B\) gives

\[
\operatorname{Tr}_B\rho_{AB}
=
\sum_i\lambda_i|i\rangle\langle i|
=
\rho_A.
\]

Thus:

\[
\boxed{
\operatorname{Tr}_B
|\Psi\rangle\langle\Psi|
=
\rho_A.
}
\]

Every finite-dimensional quantum state admits such a purification. When two purifications are represented on the same sufficiently large purifying Hilbert space, they are related by a unitary on that space; for unmatched purifying dimensions, the more general relation is by an isometry or partial isometry (Chiribella, D’Ariano, & Perinotti, 2011; Nielsen & Chuang, 2010).

The simplest example is the Bell state

\[
|\Phi^+\rangle
=
\frac{|00\rangle+|11\rangle}{\sqrt2}.
\]

The global state is pure:

\[
S(\rho_{AB})=0.
\]

Each reduced state is maximally mixed:

\[
\rho_A=\rho_B=\frac I2,
\qquad
S(\rho_A)=S(\rho_B)=\log2.
\]

Nothing has been added probabilistically to the global state. The local mixedness is generated by the relational structure of the pure whole.

For a bipartite pure state, the Schmidt decomposition gives

\[
|\Psi\rangle_{AB}
=
\sum_i
\sqrt{\lambda_i}\,
|i\rangle_A|i\rangle_B.
\]

The reduced states share the nonzero eigenvalues \(\{\lambda_i\}\). They are mixed exactly when more than one Schmidt coefficient is nonzero. This is exactly the condition for entanglement.

Therefore:

\[
\boxed{
\begin{array}{c}
\text{global pure state}\\
+\ \text{mixed local restrictions}
\end{array}
\quad
\Longleftrightarrow
\quad
\text{entanglement}
}
\]

for bipartite pure states.

This is the most exact version of the original CU intuition. Relational structure may be fully instantiated in a pure whole while neither part possesses a pure state of its own.

## 5.5 Purification is stronger than ignorance

It is tempting to describe a reduced quantum state as merely expressing ignorance about which pure state the subsystem “really occupies.” That description is generally inadequate.

Consider the maximally mixed qubit:

\[
\rho_A=\frac I2.
\]

It admits many ensemble decompositions:

\[
\frac I2
=
\frac12|0\rangle\langle0|
+
\frac12|1\rangle\langle1|
\]

and also

\[
\frac I2
=
\frac12|+\rangle\langle+|
+
\frac12|-\rangle\langle-|.
\]

These decompositions are operationally equivalent as descriptions of \(A\) alone. The density operator does not select one as the unique underlying classical alternative. When \(\rho_A\) is the reduction of a Bell state, treating one decomposition as the uniquely real local ensemble would add structure not contained in the reduced quantum state.

This non-uniqueness is a geometric signature of the fact that quantum state space is not a simplex. Mixed quantum states do not have unique decompositions into pure states.

Non-simplex geometry alone does not prove that every ensemble decomposition is physically unreal, nor does it by itself derive the Born rule or Hilbert-space structure. But it prevents the direct classical reading in which every mixed state is uniquely a probability distribution over mutually exclusive pure alternatives.

For CU, this matters because accessibility is not simply ignorance of a pre-existing local pure state. In an entangled pure state, the subsystem may have no pure state that is independent of the whole. The relational organization is not an optional correlation added between independently complete parts; it partly determines what states can be assigned to the parts at all.

That conclusion should not be overstated. Quantum theory still permits ordinary preparation uncertainty. A mixed state may arise from classical randomization, entanglement with an environment, or both. The reduced density matrix alone does not reveal its physical history. The significance of purification is representational capacity: quantum theory can express global purity with local mixedness, not that every mixed state in nature must be interpreted as entanglement with an actual environment.

## 5.6 Reversible dilation and effective irreversibility

The state-level purification theorem has a dynamical counterpart.

A quantum channel

\[
\mathcal E:
\rho_S
\mapsto
\mathcal E(\rho_S)
\]

is a completely positive trace-preserving map. Under the standard dilation theorem, it can be represented as

\[
\boxed{
\mathcal E(\rho_S)
=
\operatorname{Tr}_E
\left[
U_{SE}
\left(
\rho_S\otimes
|e_0\rangle\langle e_0|
\right)
U_{SE}^{\dagger}
\right]
}
\]

for a sufficiently large environment \(E\) and unitary \(U_{SE}\). More precisely, Stinespring’s theorem first supplies an isometric dilation; in finite dimensions that isometry can be embedded in a unitary realization after the environment or output space is enlarged as needed (Stinespring, 1955; Nielsen & Chuang, 2010).

At the level of \(S+E\), evolution is reversible. At the level of \(S\) alone, it may be dissipative, decohering, or many-to-one. The apparent loss arises because access to \(E\) has been removed.

This is a rigorous realization of an important CU pattern:

\[
\boxed{
\text{global reversibility}
+
\text{restricted access}
\Longrightarrow
\text{effective local irreversibility}.
}
\]

The conclusion is structural, not practical. A unitary dilation does not mean that lost coherence can ordinarily be recovered. Recovery may require exact control over a huge environment, including phase relations distributed across degrees of freedom that are physically unavailable. Environmental records may spread through further interactions, making reversal fantastically improbable even when it remains allowed by the fine-grained equations.

Nor does a mathematical dilation prove that every physical process is fundamentally unitary. It shows that standard finite-dimensional quantum channels admit such a representation. Treating this as the ontology of nature is an additional interpretive move.

The classical comparison is useful. Classical stochastic maps also admit dilations using auxiliary randomness and reversible maps on a larger space. But if both the classical system and its environment begin in pure states, reversible classical dynamics cannot generate a mixed marginal. The environment must carry a nontrivial classical distribution. Quantum entanglement allows a pure environment and pure system to evolve into a pure joint state with mixed reductions.

The quantum form therefore realizes restricted accessibility without relocating mixedness to the global state.

## 5.7 The Purificational Accessibility Principle

The preceding mathematics motivates, but does not derive, a CU bridge principle:

> **[Bridge principle: Purificational Accessibility]** Every operationally mixed state admits a refinement as the restriction of a globally pure state, with purifications equivalent under reversible transformations on the inaccessible system; and every admissible effective irreversible transformation admits a globally reversible realization involving inaccessible degrees of freedom initially in a pure state.

The principle contains two demands:

1. **state purification:** local mixedness can arise from restricting a pure global state;
2. **process purification:** local irreversibility can arise from restricting a reversible global process.

The uniqueness clause matters. Existence alone would say that a pure refinement can be found. Essential uniqueness says that different refinements of the same operational state differ only by reversible transformations on what is inaccessible; this is part of the purification postulate used in the Chiribella–D’Ariano–Perinotti reconstruction (2011). The further claim that this prevents the inaccessible completion from carrying arbitrary empirically unconstrained structure is a CU interpretation of that mathematical uniqueness.

Why might CU adopt this principle?

First, it gives mathematical substance to the claim that loss of local access need not be destruction of global organization.

Second, it connects state mixedness and process irreversibility through one architecture: restrictions of a pure, reversible whole.

Third, it treats the boundary between system and environment as perspectival or scale-relative without making the encompassing description arbitrary. Different local descriptions may be partial views of one larger state.

Fourth, it provides a natural bridge between the accessibility language of Section 4 and the quantum language of reduced states and channels.

But the principle must retain its epistemic label. It is not proved by the Coherence Ladder, the classical sandbox, or the transcendental argument for coherence. It is a substantive physical commitment. Nature might have fundamental mixed states, fundamentally irreversible processes, or state spaces that satisfy a weaker purification property than complex quantum theory.

The framework should therefore say:

\[
\boxed{
\text{CU motivates purification;}
\quad
\text{it does not yet derive it.}
}
\]

## 5.8 Contextual accessibility

Purification addresses the relation between local and global states. It does not by itself capture another central feature of quantum theory: which properties are accessible depends on the measurement context, and the statistics of all possible contexts need not arise as marginals of one classical assignment.

A **measurement context** is a set of measurements that can be jointly implemented or treated as compatible. A noncontextual classical representation seeks one global probability model over putative outcomes for all measurements, such that the probabilities observed in each compatible context are obtained by restriction or marginalization.

In the sheaf-theoretic formulation, contextuality is the obstruction to constructing a compatible global section whose restrictions reproduce all context-wise empirical distributions (Abramsky & Brandenburger, 2011).

A simple qubit example illustrates context dependence but not yet contextuality. Let

\[
\rho_{\mathrm{coh}}
=
|+\rangle\langle+|
=
\frac12
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}
\]

and

\[
\rho_{\mathrm{mix}}
=
\frac I2.
\]

Measured in the \(Z\) basis, both give

\[
p(0)=p(1)=\frac12.
\]

In that context, the phase relation in \(\rho_{\mathrm{coh}}\) is inaccessible. Measured in the \(X\) basis, however,

\[
\rho_{\mathrm{coh}}
\]

gives \(+\) with certainty, while

\[
\rho_{\mathrm{mix}}
\]

remains uniform. The distinction becomes accessible under a different measurement relation.

This example shows that accessibility is relational: a state feature may be unavailable to one measurement and decisive for another. But an enlarged classical model could attach a hidden phase variable and reproduce this isolated pair of observations. To establish nonclassicality, one needs a structured family of contexts whose statistics violate the conditions for a common classical refinement, as in contextuality or Bell-type no-go results (Abramsky & Brandenburger, 2011).

The proposed CU bridge principle is:

> **[Bridge principle: Contextual Accessibility]** Operational descriptions are indexed by compatible modes of access, and the family of context-indexed descriptions need not admit one context-independent classical assignment of simultaneous values to all potential measurements.

This principle should not be confused with the claim that reality is created by observers or that truth is merely subjective. A context is a physical arrangement: a coupling, basis, apparatus, intervention, or compatibility structure. Contextuality concerns the impossibility of combining all such operational statistics into one specific kind of classical global model.

The CU interpretation is that accessibility is not a transparent window onto a context-free inventory of local properties. What becomes determinate and available depends on how a subsystem is coupled into a larger relational structure.

Again, the interpretation does not prove the mathematics. The physical no-go results must be stated and verified independently.

## 5.9 Why density operators are a natural completion

Density operators combine several features needed by the revised argument.

A finite-dimensional quantum state is a positive trace-one operator

\[
\rho\geq0,
\qquad
\operatorname{Tr}\rho=1.
\]

Pure states are rank-one projectors. Mixed states form a convex set that is not a simplex. Composite systems use tensor products, and local states are obtained by partial trace.

Within one formalism, this supplies:

- globally pure states with locally mixed restrictions;
- nonunique pure-state decompositions of mixed states;
- reversible unitary evolution;
- irreversible reduced dynamics represented by quantum channels;
- phase-sensitive interference;
- context-dependent measurement statistics;
- nonclassical correlations;
- and a mathematically explicit distinction between global and subsystem descriptions.

These features make quantum theory more than a metaphor for CU. They make it a precise realization of a stronger accessibility architecture.

But the phrase **natural completion** must be handled carefully.

It may mean:

1. quantum theory realizes the desired properties elegantly;
2. quantum theory is selected within a specified class by an explicit set of axioms;
3. quantum theory is the unique logically possible completion of CU.

The first is established at the structural level. The second may be established conditionally by reconstruction theorems. The third is not established.

There are generalized probabilistic theories with nonclassical state spaces, including post-quantum nonsignaling models that share some quantum features without reducing to ordinary complex Hilbert-space quantum mechanics (Barrett, 2007). Leaving the simplex therefore does not uniquely yield standard quantum theory.

Accordingly:

\[
\boxed{
\text{non-simplex}
\not\Rightarrow
\text{complex quantum theory}.
}
\]

Additional principles are required.

## 5.10 Conditional reconstruction of quantum theory

Operational reconstruction programs begin not with wavefunctions but with assumptions about preparations, transformations, measurements, composition, and information processing. They ask which state spaces and dynamical structures satisfy those assumptions.

Different programs use different axiom sets. To avoid blending the premises of distinct theorems, this manuscript adopts one reconstruction result as its canonical reference: the informational derivation of Chiribella, D’Ariano, and Perinotti (2011).

Within their operational-probabilistic framework, five informational axioms define a broad class of standard theories:

- **causality:** present outcome probabilities do not depend on later measurement choices;
- **perfect distinguishability:** every state that is not completely mixed can be perfectly distinguished from at least one other state;
- **ideal compression:** information sources can be encoded losslessly and maximally efficiently;
- **local distinguishability:** distinct composite states can be distinguished through the statistics of local measurements and their correlations;
- **pure conditioning:** conditioning a pure bipartite state on an atomic local outcome leaves a pure conditional state on the other system.

The additional **purification postulate** requires every state to be the marginal of a pure state and requires purifications of the same state to be equivalent under reversible transformations on the purifying system.

Chiribella, D’Ariano, and Perinotti prove that these five axioms together with purification reconstruct finite-dimensional complex quantum theory within that operational class. Continuous reversible transformations, subspace axioms, and other principles used by different reconstruction programs are not premises of this particular theorem and are therefore not included in the present implication.

The theorem remains conditional. CU does not derive the five informational axioms or purification from the classical sandbox. It offers a structural motivation for taking purification and contextual accessibility seriously; the operational premises must still be independently stated and defended.

The relation to CU can then be stated in two stages.

### Stage one: motivation

CU provides conceptual reasons to investigate:

- purification, because locally inaccessible structure need not be globally destroyed;
- reversible dilation, because effective irreversibility may arise from restriction;
- contextual access, because properties are available through relational modes of interaction;
- compositionality, because partial separability permits systems that are distinguishable without being absolutely independent.

### Stage two: conditional theorem

The selected operational axioms, including purification, mathematically constrain the theory’s state spaces and transformations. Within the theorem’s domain, quantum theory follows.

This yields:

\[
\boxed{
\begin{array}{c}
\text{CU-motivated bridge principles}\\
+\ \text{independently stated operational axioms}
\end{array}
\Longrightarrow
\text{quantum theory within the selected class}.
}
\]

The arrow is conditional. The operational axioms do substantive work. CU cannot claim the conclusion while leaving those premises implicit.

## 5.11 How the operational assumptions map onto CU

The following correspondences can guide the reconstruction, but they are proposals for interpretation rather than proofs of implication.

| Operational requirement | CU interpretation |
|---|---|
| Causality | Ordered interventions have well-defined probabilities independent of later choices |
| Distinguishability | Partial separability permits operational discrimination among alternatives |
| Compression | Accessible structure can be represented without retaining inaccessible redundancy |
| Local tomography | Composite structure is encoded in the full family of local statistics and correlations |
| Pure conditioning | Fine-grained access to a pure process need not introduce unexplained mixture |
| Continuous reversibility | Pure-state transformations belong to connected families of lawful change |
| Purification | Local mixedness may be restriction of global purity |
| Reversible dilation | Effective local irreversibility may be restriction of global reversibility |

Each proposed mapping raises questions.

Does CU’s partial separability imply local tomography, or could holistic degrees of freedom remain inaccessible to all local measurements? Does logical ordering imply operational causality in the reconstruction-theoretic sense? Why should reversible transformations act transitively on pure states? Why should every mixed state, rather than only physically preparable mixed states, admit purification?

These are not minor details. They determine which theory is selected.

The right argumentative posture is therefore invitational and exacting:

> CU supplies a reason to ask for a particular family of operational properties. The reconstruction theorem shows what follows if those properties hold. The empirical and philosophical task is to determine whether CU genuinely warrants them and whether nature satisfies them.

## 5.12 In what sense is quantum theory “minimal”?

Quantum theory may be described as a minimal completion only after the comparison class and ordering relation have been specified.

Quantum theory is not minimal in the trivial sense of adding the fewest symbols. A hidden-variable model may add different mathematical structure. A generalized probabilistic theory may use a state cone with fewer or more dimensions. A real Hilbert space may appear formally smaller than a complex one. “Minimal” is meaningless without a criterion.

There are, however, defensible senses in which quantum theory may be minimal.

It may be minimal **within a reconstruction theorem**: among theories satisfying the selected operational axioms, the theorem singles out complex quantum theory.

It may be minimal **as a structural package**: it adds exactly the non-simplex, compositional, purification, interference, and reversible-dilation resources required to model the phenomena at issue, without adding empirically idle hidden states.

It may be minimal **relative to established physics**: it is the simplest empirically successful formalism already known to satisfy the relevant nonclassical constraints.

These are conditional and comparative claims. The paper should avoid the unrestricted statement:

\[
\text{CU alone uniquely forces quantum mechanics}.
\]

A stronger and more accurate formulation is:

> **[Conditional result] Within an explicitly specified operational class, purification and associated principles select quantum theory; CU provides a coherent motivation for several of those principles through its distinction between global structure and local accessibility.**

## 5.13 What this transition establishes

The transition supports five conclusions.

First, classical probability already represents hidden correlation under marginalization. That phenomenon cannot bear the weight of a quantum derivation.

Second, finite classical simplex theories satisfy:

\[
\text{global purity}
\Rightarrow
\text{local purity}.
\]

They cannot purify nontrivial mixed local states.

Third, quantum theory permits:

\[
\text{global purity}
+
\text{local mixedness},
\]

with entanglement providing the exact relational structure responsible for the combination in bipartite pure states.

Fourth, quantum channels admit reversible dilations in a larger system under standard conditions, allowing local irreversibility to coexist with global reversibility.

Fifth, contextuality identifies a stronger failure of classical representation than hidden marginal correlation: the inability to combine all compatible-context statistics into one noncontextual global assignment.

The transition does **not** yet establish:

- that every local mixed state in nature is physically part of a pure global state;
- that every physical process is fundamentally reversible;
- that CU derives purification;
- that contextuality follows from coherence alone;
- or that the listed principles uniquely produce complex quantum theory without the additional assumptions of a verified reconstruction theorem.

The result is nevertheless substantial. CU’s language of coherence and accessibility now connects to a precise nonclassical architecture rather than to a false limitation of classical probability.

The next section asks what kinds of structure must be distinguished once quantum state space has been introduced. Purity, superposition, correlation, and entanglement are related, but they are not the same. A viable quantum CU must name each separately before it can ask how they transform into one another.

---

# 6. Quantum Coherence, Correlation, Entanglement, and Accessibility

The word *coherence* already has a technical meaning in quantum information theory: roughly, the presence of off-diagonal terms relative to a specified basis, treated as a resource under a specified class of operations. Coherence Universalism uses the same word more broadly for integrated relational organization under constraint. The overlap is real, but the concepts are not identical.

This section therefore begins with a discipline of separation. A quantum state may be pure without being entangled. It may be entangled while having no local basis coherence in a chosen subsystem basis. It may contain total correlation that is entirely classical. It may possess off-diagonal terms in one basis and none in another. No single scalar can distinguish all of these structures.

The original Physics paper attempted to use

\[
\operatorname{Tr}(\rho^2)-\frac1d
\]

as a quantum coherence functional and then to read its difference under partial trace as hidden coherence or entanglement. That quantity has a legitimate interpretation, but it is **excess purity**, not a general measure of quantum relational integration. A pure product state and a maximally entangled pure state both have global purity one. Any quantity depending only on the global eigenvalues of \(\rho\) is blind to the difference.

The corrected quantum program does not abandon quantification. It becomes more pluralistic and more precise. Different functionals answer different structural questions:

\[
\begin{array}{ll}
\text{purity:} & \text{how mixed is the state?}\\
\text{basis coherence:} & \text{how much superposition is present relative to an access basis?}\\
\text{mutual information:} & \text{how much total correlation exists across a partition?}\\
\text{entanglement:} & \text{how much of that relational structure is nonseparable?}\\
\text{recoverability:} & \text{how much lost distinguishability can be restored from retained systems?}
\end{array}
\]

A substantive CU account may eventually integrate these into a constraint-sensitive profile. It should not collapse them prematurely into one number.

## 6.1 Four questions that must not be conflated

Let \(\rho_{AB}\) be a density operator on

\[
\mathcal H_A\otimes\mathcal H_B.
\]

At least four distinct questions can be asked.

### How mixed is the global state?

This is a question about the spectrum of \(\rho_{AB}\). Purity and von Neumann entropy answer it.

### Is the state coherent in a specified basis?

This is a question about off-diagonal structure relative to a basis or observable algebra. Resource-theoretic coherence measures answer it.

### Are \(A\) and \(B\) correlated?

This is a question about departure from the product state

\[
\rho_A\otimes\rho_B.
\]

Quantum mutual information answers it.

### Are those correlations entangled?

This is a question about whether \(\rho_{AB}\) can be represented as a convex mixture of product states. Entanglement measures answer it.

The questions are logically independent enough that none can substitute for all the others.

For example:

- \(|00\rangle\) is globally pure, unentangled, and incoherent in the computational basis.
- \(|+\rangle|0\rangle\) is globally pure, unentangled, and locally coherent in the computational basis.
- \((|00\rangle+|11\rangle)/\sqrt2\) is globally pure and maximally entangled, while each local reduced state is maximally mixed and has no basis coherence in any basis.
- A classically correlated mixture
  \[
  \frac12|00\rangle\langle00|
  +
  \frac12|11\rangle\langle11|
  \]
  is mixed and correlated but separable.

These examples are not exceptions. They reveal the basic geometry of the problem.

## 6.2 Excess purity

For a \(d\)-dimensional state, define

\[
\boxed{
P_{\mathrm{ex}}(\rho)
=
\operatorname{Tr}(\rho^2)-\frac1d.
}
\]

The maximally mixed state satisfies

\[
\rho_*=\frac{I}{d},
\qquad
P_{\mathrm{ex}}(\rho_*)=0.
\]

A pure state satisfies

\[
\rho^2=\rho,
\qquad
P_{\mathrm{ex}}(\rho)=1-\frac1d.
\]

This quantity is the closest quantum analogue of the classical sandbox functional

\[
D(p)
=
\sum_i
\left(
p_i-\frac1d
\right)^2.
\]

For a density matrix diagonal in a fixed basis with diagonal \(p\),

\[
\operatorname{Tr}(\rho^2)-\frac1d
=
\sum_i p_i^2-\frac1d
=
D(p).
\]

Thus excess purity extends the sandbox’s departure-from-uniformity measure from classical distributions to quantum states.

Its virtues are clarity and simplicity. It is basis independent, easy to calculate, and zero exactly at maximal mixing. It answers:

> How concentrated is the spectrum relative to the maximally mixed state?

It does not answer:

> How integrated are the state’s subsystems?

Every global pure state has the same value

\[
P_{\mathrm{ex}}=1-\frac1d,
\]

whether it is a product state, a GHZ state, a Bell state, or some other pure state. The quantity recognizes absence of global mixture, not the form of global relation.

For that reason, the manuscript should call it **excess purity** or, where continuity with the original notation is useful, **the quantum differentiation proxy**. It should not be used by itself as a measure of entanglement, hidden correlation, or substantive CU coherence.

## 6.3 Basis coherence

Quantum superposition is defined relative to a choice of basis or, more generally, a choice of preferred observable algebra.

Let

\[
B=\{|i\rangle\}
\]

be an orthonormal basis. Define the complete dephasing map

\[
\Delta_B(\rho)
=
\sum_i
|i\rangle\langle i|
\rho
|i\rangle\langle i|.
\]

This map deletes off-diagonal entries in \(B\) while preserving the measurement probabilities in that basis.

The relative entropy of coherence is

\[
\boxed{
C_r^B(\rho)
=
S(\Delta_B\rho)-S(\rho),
}
\]

where

\[
S(\rho)=-\operatorname{Tr}(\rho\log\rho)
\]

is the von Neumann entropy. Under the resource theory of coherence, \(C_r^B\) is a standard coherence monotone; its precise operational meaning depends on the selected class of free operations. In particular, it equals the asymptotic distillable coherence under incoherent operations (Baumgratz, Cramer, & Plenio, 2014; Winter & Yang, 2016).

For a pure qubit

\[
|\phi_\theta\rangle
=
\cos\theta\,|0\rangle
+
\sin\theta\,|1\rangle,
\]

the state has zero von Neumann entropy, while its dephased state has diagonal probabilities

\[
\cos^2\theta,\quad \sin^2\theta.
\]

Therefore

\[
C_r^B(|\phi_\theta\rangle)
=
h_2(\sin^2\theta),
\]

where

\[
h_2(x)
=
-x\log x-(1-x)\log(1-x)
\]

is binary entropy.

At \(\theta=0\), there is no superposition in \(B\). At \(\theta=\pi/4\), the state \(|+\rangle\) has one bit of coherence when logarithms are base two.

The basis dependence is not a defect to be erased. It tells us that basis coherence is a relation among:

- a state;
- a set of distinctions;
- and a class of operations or measurements that treats those distinctions as classical.

In physical applications, the relevant basis may be selected by a Hamiltonian, conserved quantity, measurement coupling, symmetry, preparation procedure, or environmental pointer structure. In CU language, it specifies an **access architecture**: the distinctions with respect to which phase relations are counted as locally available resources.

Without such a selection, the statement “this state is coherent” is incomplete. Every pure state is diagonal in its own eigenbasis. Quantum coherence becomes physically meaningful only relative to a basis that is fixed by more than the state alone.

This is an instructive parallel with the classical sandbox. Statistical differentiation required a specified sample space and uniform reference. Basis coherence requires a specified decomposition into alternatives. In both cases, the measure is relational rather than an intrinsic ranking of states independent of all descriptive structure.

## 6.4 Total correlation

For a bipartite state \(\rho_{AB}\), define the quantum mutual information

\[
\boxed{
I(A:B)_\rho
=
S(\rho_A)
+
S(\rho_B)
-
S(\rho_{AB}).
}
\]

Equivalently,

\[
\boxed{
I(A:B)_\rho
=
D_{\mathrm{q}}
\left(
\rho_{AB}
\middle\|
\rho_A\otimes\rho_B
\right),
}
\]

where \(D_{\mathrm{q}}\) is quantum relative entropy.

The mutual information is zero exactly when

\[
\rho_{AB}
=
\rho_A\otimes\rho_B
\]

(for finite-dimensional states, with the usual support convention for quantum relative entropy). It therefore measures total departure from product structure.

For the classically correlated state

\[
\rho_{\mathrm{cc}}
=
\frac12|00\rangle\langle00|
+
\frac12|11\rangle\langle11|,
\]

the marginals are maximally mixed, the joint entropy is one bit, and

\[
I(A:B)=1\ \text{bit}.
\]

For the Bell state

\[
|\Phi^+\rangle
=
\frac{|00\rangle+|11\rangle}{\sqrt2},
\]

the marginals are again maximally mixed, but the joint state is pure, so

\[
I(A:B)=2\ \text{bits}.
\]

Both states contain relational structure inaccessible to either marginal. Only the second is entangled.

Quantum mutual information is therefore a good measure of **total correlation**, not of specifically quantum correlation. It is valuable for CU because it directly compares the whole with the product of its parts. But it does not by itself tell us whether the relation could be reproduced by a classical mixture of product states.

## 6.5 Entanglement

A bipartite state is separable when it can be written as

\[
\boxed{
\rho_{AB}
=
\sum_k
q_k\,
\rho_A^{(k)}
\otimes
\rho_B^{(k)},
\qquad
q_k\geq0,
\quad
\sum_kq_k=1.
}
\]

If no such decomposition exists, the state is entangled.

Entanglement is therefore not equivalent to correlation. A separable state can be strongly correlated. Entanglement means that the joint state cannot be understood as classical uncertainty over independently specified local quantum states.

Entanglement also depends on the subsystem decomposition

\[
\mathcal H
=
\mathcal H_A\otimes\mathcal H_B.
\]

Without a physically meaningful factorization, the question “is the state entangled?” is underdetermined. In field theory, gauge theory, and gravity, constraints and boundary degrees of freedom can obstruct a naive tensor-product factorization, so identifying subsystems requires careful treatment (Casini, Huerta, & Rosabal, 2014; Donnelly & Freidel, 2016).

For pure bipartite states, entanglement has a canonical measure:

\[
\boxed{
E(|\Psi\rangle_{AB})
=
S(\rho_A)
=
S(\rho_B).
}
\]

For mixed states, different operational tasks produce different monotones. Common choices include:

- negativity;
- concurrence for two qubits;
- entanglement of formation;
- distillable entanglement;
- entanglement cost;
- relative entropy of entanglement.

The relative entropy of entanglement is

\[
\boxed{
E_R^{A:B}(\rho)
=
\inf_{\sigma\in\mathrm{Sep}(A:B)}
D_{\mathrm{q}}(\rho\|\sigma).
}
\]

It measures the relative-entropy distance to the convex set of separable states and is faithful under standard finite-dimensional conditions (Vedral et al., 1997).

No single mixed-state measure is universally privileged because “amount of entanglement” can mean different operational resources: how much can be distilled, how much is required to prepare the state, how robustly nonpositive the partial transpose is, or how far the state lies from separability.

CU should not conceal this plurality. The framework’s own commitment to scale and constraint sensitivity suggests the opposite: the relevant measure should be chosen according to the physical task and the transformations available.

## 6.6 Pure-state entanglement as relational structure

For a pure bipartite state, the Schmidt decomposition gives

\[
|\Psi\rangle_{AB}
=
\sum_i
\sqrt{\lambda_i}\,
|i\rangle_A|i\rangle_B,
\qquad
\lambda_i\geq0,
\qquad
\sum_i\lambda_i=1.
\]

The reduced states are

\[
\rho_A
=
\sum_i
\lambda_i
|i\rangle\langle i|,
\qquad
\rho_B
=
\sum_i
\lambda_i
|i\rangle\langle i|.
\]

The following are equivalent:

1. more than one Schmidt coefficient is nonzero;
2. the Schmidt rank exceeds one;
3. the global state is not a product;
4. the global state is entangled;
5. the reduced states are mixed;
6. \(S(\rho_A)=S(\rho_B)>0\).

This permits a precise CU interpretation:

> **[Interpretation] In a pure bipartite state, entanglement is relational organization fully present in the whole but not assignable as a pure state to either subsystem independently.**

The statement is exact as a characterization of the state’s structure. It is not yet a complete definition of substantive coherence. Entanglement can be fragile, inaccessible, useless for a particular task, or distributed in forms that do not support the viability of any macroscopic system. More entanglement is not automatically better, more stable, more integrated at every scale, or more ethically valuable.

What entanglement supplies is a rigorous instance of a broader CU pattern:

\[
\boxed{
\text{the whole can be pure while the parts are locally mixed}
}
\]

and

\[
\boxed{
\text{the relation can be determinate when local states are not}.
}
\]

This is much stronger than ordinary hidden correlation.

### A one-parameter family

Consider

\[
|\Psi_\theta\rangle
=
\cos\theta\,|00\rangle
+
\sin\theta\,|11\rangle,
\qquad
0\leq\theta\leq\frac{\pi}{4}.
\]

The reduced state is

\[
\rho_A
=
\begin{pmatrix}
\cos^2\theta & 0\\
0 & \sin^2\theta
\end{pmatrix}.
\]

Its entanglement entropy is

\[
E(\theta)
=
h_2(\sin^2\theta).
\]

Its reduced linear entropy is

\[
1-\operatorname{Tr}(\rho_A^2)
=
2\sin^2\theta\cos^2\theta
=
\frac12\sin^2(2\theta).
\]

For this pure two-qubit family, concurrence is

\[
\mathcal C(\theta)=\sin(2\theta)
\]

(Wootters, 1998), using the standard convention in which a Bell state has concurrence one.

At \(\theta=0\), the state is the product \(|00\rangle\). At \(\theta=\pi/4\), it is maximally entangled. The global purity remains one throughout. What changes is not global mixedness but relational organization across the partition.

This example alone shows why excess purity cannot stand in for entanglement.

## 6.7 Exact conversion of basis coherence into entanglement

The distinction among resources does not mean they are unrelated. Under a specified interaction, one form of quantum structure can be converted into another.

Let

\[
|\phi_\theta\rangle_A
=
\cos\theta\,|0\rangle
+
\sin\theta\,|1\rangle
\]

and let an ancilla begin in

\[
|0\rangle_B.
\]

Apply a controlled-NOT gate with \(A\) as control:

\[
U_{\mathrm{CNOT}}
|0\rangle_A|0\rangle_B
=
|00\rangle,
\]

\[
U_{\mathrm{CNOT}}
|1\rangle_A|0\rangle_B
=
|11\rangle.
\]

By linearity,

\[
\boxed{
U_{\mathrm{CNOT}}
|\phi_\theta\rangle_A|0\rangle_B
=
\cos\theta\,|00\rangle
+
\sin\theta\,|11\rangle.
}
\]

The input basis coherence is

\[
C_r^B(|\phi_\theta\rangle)
=
h_2(\sin^2\theta).
\]

The output entanglement entropy is

\[
E(|\Psi_\theta\rangle)
=
S(\rho_A)
=
h_2(\sin^2\theta).
\]

Therefore:

\[
\boxed{
C_r^B(\text{input})
=
E(\text{output}).
}
\]

At \(\theta=\pi/4\),

\[
|+\rangle_A|0\rangle_B
\longrightarrow
|\Phi^+\rangle_{AB},
\]

and one bit of local basis coherence becomes one ebit of bipartite entanglement.

Nothing has been created from nothing. The CNOT couples a coherent superposition in \(A\) to a distinguishable degree of freedom in \(B\). The phase-sensitive resource that was locally accessible in \(A\) becomes encoded in correlations between \(A\) and \(B\). The reduced state of \(A\) loses its off-diagonal terms, while the global state remains pure.

This gives the original CU intuition an exact and disciplined form:

> **[Derived] A specified coherence-preserving interaction can convert locally accessible basis coherence into globally instantiated entanglement that is not present as local purity in either subsystem.**

Resource-theoretic results generalize this relation beyond the two-qubit example: with an incoherent ancilla, a basis-coherent state can generate entanglement through an incoherent operation, and an appropriate generalized CNOT reaches the corresponding relative-entropy bound (Streltsov et al., 2015).

The conversion is basis- and interaction-dependent. It should not be elevated into the universal statement that all local coherence becomes entanglement or that all entanglement originated as local basis coherence.

## 6.8 Decoherence as redistribution of accessibility

The CNOT example is also a minimal model of decoherence.

Let a system begin in

\[
|\psi\rangle_S
=
c_0|0\rangle+c_1|1\rangle
\]

and an environment in

\[
|e_*\rangle_E.
\]

Suppose a measurement-like interaction produces

\[
|0\rangle|e_*\rangle
\longrightarrow
|0\rangle|e_0\rangle,
\]

\[
|1\rangle|e_*\rangle
\longrightarrow
|1\rangle|e_1\rangle.
\]

Then the joint state becomes

\[
|\Psi\rangle_{SE}
=
c_0|0\rangle|e_0\rangle
+
c_1|1\rangle|e_1\rangle.
\]

The global density operator remains pure. The reduced state of \(S\) is

\[
\rho_S
=
\begin{pmatrix}
|c_0|^2
&
c_0c_1^*
\langle e_1|e_0\rangle
\\[4pt]
c_0^*c_1
\langle e_0|e_1\rangle
&
|c_1|^2
\end{pmatrix}.
\]

Define the decoherence factor

\[
\gamma
=
\langle e_1|e_0\rangle.
\]

The magnitude of the local off-diagonal terms is multiplied by \(|\gamma|\).

- If \(|e_0\rangle=|e_1\rangle\), then \(\gamma=1\), the environment carries no distinguishing record, and local coherence is preserved.
- If the environment states become orthogonal, then \(\gamma=0\), the alternatives are perfectly recorded in \(E\), and the local reduced state is diagonal.
- Intermediate overlaps produce partial decoherence.

The crucial structural point is that the off-diagonal relation has not been annihilated from the global pure state. It is encoded in the joint amplitudes and in the overlap structure of the environmental records. A joint operation on \(S+E\) can in principle reveal interference that is unavailable to operations on \(S\) alone.

For globally pure \(SE\),

\[
S(\rho_S)=S(\rho_E),
\]

and the common entropy is the entanglement entropy across the \(S:E\) partition. In the ideal premeasurement model, local basis-coherence loss is accompanied by system–environment entanglement.

This supports a carefully limited statement:

> **[Conditional result] In pure-environment premeasurement or dephasing models, local basis coherence can be redistributed into system–environment relational structure while global purity and unitarity are preserved.**

It does not support the universal identity

\[
-\Delta C_S
=
\Delta E_{S:E}
\]

for every coherence measure, every environment, and every open-system process.

When the environment is initially mixed, when energy is exchanged, when multiple channels act, or when inaccessible records themselves decohere into larger surroundings, the original resource may be distributed among:

- environment basis coherence;
- classical correlations;
- entanglement;
- discord-like correlations;
- heat and energetic degrees of freedom;
- inaccessible records;
- and correlations with further systems.

The general term should therefore be **redistribution of accessibility**, not automatic one-to-one transfer into entanglement.

## 6.9 Decoherence, records, and effective classicality

Decoherence explains why interference between certain alternatives becomes inaccessible to local observations and why stable pointer records can emerge under environmental coupling (Zurek, 1982, 2003). It does not, by itself, select one unique outcome from the globally entangled state.

This distinction matters for the epistemic discipline of the paper.

The interaction

\[
(c_0|0\rangle+c_1|1\rangle)|e_*\rangle
\longrightarrow
c_0|0\rangle|e_0\rangle
+
c_1|1\rangle|e_1\rangle
\]

explains suppression of local interference when

\[
\langle e_1|e_0\rangle\approx0.
\]

The reduced state behaves approximately like the mixture

\[
|c_0|^2|0\rangle\langle0|
+
|c_1|^2|1\rangle\langle1|.
\]

But the global state is still a superposition of correlated branches. Decoherence does not alone tell us why one result is experienced, whether all branches persist, whether outcomes are selected stochastically, or whether the quantum state is epistemic.

CU’s accessibility language can illuminate the structure of the problem:

- certain phase relations become unavailable to local agents;
- stable environmental records make some observables redundantly accessible;
- the effective classical description is organized by what remains accessible under repeated interaction.

But this is not yet a solution to the measurement problem. A complete account would have to specify:

- the ontology of the quantum state;
- the status of outcomes;
- the Born rule;
- and the relation between global description and definite experience.

The present paper should therefore claim an account of **decoherence and effective accessibility**, not a completed interpretation of quantum measurement.

## 6.10 Recoverability as a quantitative accessibility question

The distinction between hidden and destroyed structure becomes sharper when formulated through recoverability.

Let

\[
\mathcal N
\]

be a quantum channel representing coarse-graining, noise, or loss of access. For two states \(\rho\) and \(\sigma\), distinguishability measures such as quantum relative entropy contract under completely positive trace-preserving maps:

\[
D_{\mathrm{q}}(\rho\|\sigma)
\geq
D_{\mathrm{q}}
\bigl(
\mathcal N(\rho)
\|
\mathcal N(\sigma)
\bigr)
\]

provided \(\operatorname{supp}\rho\subseteq\operatorname{supp}\sigma\), or with quantum relative entropy understood in its extended-value convention (Lindblad, 1975).

The loss

\[
\Delta_{\mathcal N}
=
D_{\mathrm{q}}(\rho\|\sigma)
-
D_{\mathrm{q}}
\bigl(
\mathcal N(\rho)
\|
\mathcal N(\sigma)
\bigr)
\]

measures how much distinguishability becomes inaccessible under \(\mathcal N\).

A recovery map

\[
\mathcal R
\]

attempts to reconstruct the original states from the channel outputs. When recovery is exact,

\[
\mathcal R\circ\mathcal N(\rho)=\rho,
\qquad
\mathcal R\circ\mathcal N(\sigma)=\sigma.
\]

A quantitative recovery theorem makes this precise. Define the unsquared fidelity by

\[
F(\rho,\tau)
=
\left\|
\sqrt{\rho}\sqrt{\tau}
\right\|_1.
\]

In finite dimensions, there exists a recovery channel \(\mathcal R_{\sigma,\mathcal N}\), depending only on \(\sigma\) and \(\mathcal N\), such that \((\mathcal R_{\sigma,\mathcal N}\circ\mathcal N)(\sigma)=\sigma\) and

\[
\boxed{
D_{\mathrm{q}}(\rho\|\sigma)
-
D_{\mathrm{q}}(\mathcal N\rho\|\mathcal N\sigma)
\geq
-2\log
F\!\left(
\rho,
(\mathcal R_{\sigma,\mathcal N}\circ\mathcal N)(\rho)
\right).
}
\]

Thus small relative-entropy loss guarantees a recovery map whose output has high fidelity with \(\rho\) (Junge et al., 2018). If squared fidelity is used instead, the coefficient in front of the logarithm changes; this paper uses the unsquared convention above.

This gives CU a more rigorous language than simply declaring hidden coherence:

- **accessible structure:** distinctions preserved by the channel;
- **inaccessible but recoverable structure:** distinctions lost locally but reconstructible using retained side information or a recovery operation;
- **effectively irrecoverable structure:** distinctions dispersed so broadly that no feasible recovery is available;
- **fundamentally destroyed structure:** a stronger ontological claim not inferable from channel outputs alone.

Recoverability is operational. It asks what can be restored by specified agents with specified resources. It therefore fits CU’s scale-relative accessibility better than a scalar difference of purities.

## 6.11 Quantum information geometry

The classical probability simplex carries a Fisher–Rao metric characterized up to scale within the relevant Čencov theorem class under sufficient-statistic or Markov-invariance conditions (Čencov, 1982; Lê, 2016). Quantum state space is different: it admits a family of monotone Riemannian metrics classified through operator-monotone functions (Petz, 1996).

The Bures or symmetric-logarithmic-derivative metric is one natural and operationally important member of this family. Other monotone metrics correspond to different operator-monotone functions.

> **[Imported structural distinction under CU-M14]** Licensed classical statistical models may receive the Fisher-Rao metric canonically up to scale under the relevant invariance assumptions. Quantum density operators instead admit a family of monotone metrics. Neither result selects a physical potential, dynamics, value direction, or substantive coherence functional; each further use requires its own operational criterion and Translation License.

This has two consequences.

First, there is no unqualified replacement rule

\[
\text{classical Fisher metric}
\longrightarrow
\text{the unique quantum Fisher metric}.
\]

A quantum metric must be selected, and the selection requires a physical or operational reason.

Second, a metric defines geometry, not automatically dynamics.

Given a metric \(g_Q\) and a functional \(F\), the natural gradient satisfies

\[
g_Q(
\operatorname{grad}_QF,
X
)
=
dF(X)
\]

for tangent directions \(X\).

The vector field

\[
\dot\rho
=
\operatorname{grad}_QF(\rho)
\]

is mathematically well-defined where the metric and functional are regular. But it is not automatically a physically admissible quantum evolution.

A physical state evolution must at least preserve:

- Hermiticity;
- trace;
- positivity.

If it is to act consistently on one part of an arbitrary entangled system as a state-independent channel, complete positivity and linearity become central requirements. A nonlinear state-dependent gradient flow does not acquire these properties merely because \(g_Q\) is monotone.

Natural-gradient quantum dynamics may still be valuable as:

- a variational algorithm;
- an effective nonlinear state-space model;
- a phenomenological relaxation equation;
- or a geometry for optimization.

Its physical status must be proved separately.

This is one reason the Hamiltonian route of Section 7 is preferable for foundational quantum dynamics. Schrödinger evolution is generated through a standard action and is unitary. Quantum information geometry then helps characterize distinguishability and accessibility without being asked to generate all physical evolution by itself.

## 6.12 Quantum alignment and opposition functionals

If two quantum functionals \(F\) and \(G\) are chosen on a metric state space, define their signed gradient alignment by

\[
\boxed{
\mathcal A_Q^{F,G}
=
g_Q(
\operatorname{grad}_QF,
\operatorname{grad}_QG
).
}
\]

Define opposition, when useful, by

\[
\boxed{
\Pi_Q^{F,G}
=
-\mathcal A_Q^{F,G}.
}
\]

The sign has no universal interpretation independent of the selected functionals. A positive \(\Pi_Q^{F,G}\) means that the two chosen gradients oppose one another under the chosen metric. It does not mean that entanglement is present, that the state is stable, or that the system is in a Goldilocks regime.

If both \(F\) and \(G\) depend only on the global spectrum of \(\rho\), their gradients are invariant under global unitary conjugation. They therefore cannot distinguish a pure product state from a pure entangled state, because both have the same spectrum.

Consequently:

\[
\boxed{
\text{spectrum-only potentiometers cannot be entanglement measures}.
}
\]

A partition-sensitive potentiometer would need at least one functional that refers to the tensor-product structure, reduced states, separable set, or correlation architecture.

For example, one might study the interaction between a dynamical objective \(F\) and an entanglement monotone \(E_R^{A:B}\):

\[
\mathcal A_Q^{F,E_R}
=
g_Q(
\operatorname{grad}_QF,
\operatorname{grad}_QE_R
).
\]

But mixed-state entanglement measures may be nonsmooth, computationally difficult, or metric-dependent. Such constructions belong to a future model-specific program, not to a universal theorem asserted from purity and entropy alone.

## 6.13 Why there is no universal entanglement Goldilocks band

The original quantum section proposed that stable entanglement occupies an intermediate region between excessive order and excessive entropy. This is intuitively attractive, especially for noisy open systems, but it is not universally true.

Consider four cases.

### Pure product state

\[
|00\rangle
\]

has zero global entropy and zero entanglement.

### Bell state

\[
|\Phi^+\rangle
\]

also has zero global entropy but maximal two-qubit entanglement.

### Maximally mixed state

\[
\frac{I}{4}
\]

has maximal global entropy and zero entanglement.

### Mixed entangled state

A noisy Bell state may have intermediate entropy and nonzero entanglement over part of its parameter range.

These examples show:

\[
\text{global entropy}
\not\leftrightarrow
\text{entanglement}.
\]

The same global entropy may accompany different entanglement values, and the same entanglement may appear at different mixedness levels depending on dimension and state family.

Stability is equally model-dependent. A Bell state may be an exact protected eigenstate of one Hamiltonian and rapidly decohere under another. A mixed entangled steady state may be stabilized by dissipation. A highly entangled many-body state may be robust because of symmetry or error correction, while a weakly entangled state may be fragile.

There is therefore no universal scalar interval

\[
S_{\min}<S(\rho)<S_{\max}
\]

that can be identified with stable entanglement.

The Goldilocks idea can survive only after the system, environment, couplings, resource measure, and stability criterion are specified.

## 6.14 A model-specific quantum Goldilocks program

Consider an open-system model

\[
\dot\rho
=
-\frac{i}{\hbar}[H_{\mathrm{ent}},\rho]
+
\kappa_{\mathrm p}\,
\mathcal D_{\mathrm{pump}}[\rho]
+
\gamma_{\mathrm d}\,
\mathcal D_{\mathrm{deph}}[\rho],
\]

where:

- \(H_{\mathrm{ent}}\) generates entangling interactions;
- \(\mathcal D_{\mathrm{pump}}\) injects or stabilizes a resource;
- \(\mathcal D_{\mathrm{deph}}\) destroys phase relations;
- \(\kappa_{\mathrm p}\) and \(\gamma_{\mathrm d}\) control the competing rates.

For each parameter choice, solve for a transient trajectory or steady state

\[
\rho_{\mathrm{ss}}(\kappa_{\mathrm p},\gamma_{\mathrm d},\ldots)
\]

and evaluate:

- an entanglement monotone such as negativity;
- basis coherence;
- purity;
- relaxation time;
- robustness to perturbation;
- recoverability after noise.

A model-specific Goldilocks region could then be defined as

\[
\boxed{
\mathcal G
=
\left\{
(\kappa_{\mathrm p},\gamma_{\mathrm d},\ldots):
\begin{array}{l}
\mathcal N(\rho_{\mathrm{ss}})>0,\\
\tau_{\mathrm{life}}>\tau_0,\\
\text{and feasibility constraints hold}
\end{array}
\right\}.
}
\]

Such a region may exist, fail to exist, or break into disconnected phases. Its boundaries may correspond to entanglement sudden death, dissipative phase transitions, or loss of controllability.

This would be a genuine CU research result because it would show how relational quantum structure persists under explicit competing constraints. It would not merely rename intermediate entropy “coherence.”

The same program can be extended across scales. A state might lose pairwise entanglement while retaining multipartite or topological structure. Local decoherence may coexist with global error-correcting order. The relevant Goldilocks regime may therefore be a region in a multidimensional resource space rather than an interval on one axis.

## 6.15 A multidimensional quantum coherence profile

A provisional quantum structural profile is

\[
\boxed{
\mathfrak C_Q(\rho_{AB};B,\mathcal N)
=
\left(
P_{\mathrm{ex}},
C_r^B,
I(A:B),
E_R^{A:B},
R_{\mathcal N}
\right),
}
\]

where:

- \(P_{\mathrm{ex}}\) measures excess purity;
- \(C_r^B\) measures basis coherence;
- \(I(A:B)\) measures total correlation;
- \(E_R^{A:B}\) measures entanglement relative to a partition;
- \(R_{\mathcal N}\) measures recoverability under a specified channel.

This is not proposed as a final coherence functional. It is a bookkeeping device that prevents conceptually distinct resources from being conflated.

A future substantive quantum coherence functional might take the schematic form

\[
C_{\mathrm{sub}}^Q
=
C^Q(
\rho;
K,G,\pi,T,\mathcal O
),
\]

where:

- \(K\) specifies physical constraints;
- \(G\) specifies subsystem and interaction structure;
- \(\pi\) specifies scale or coarse-graining;
- \(T\) specifies temporal horizon;
- \(\mathcal O\) specifies accessible operations.

The functional would ask not merely whether a state is pure or entangled, but whether its relational organization supports persistence, recoverability, and constraint satisfaction over the relevant horizon.

This connects the quantum section back to the central distinction of the paper:

\[
\boxed{
\text{quantum resources may contribute to substantive coherence;}
}
\]

\[
\boxed{
\text{none is identical to substantive coherence in every context.}
}
\]

## 6.16 Measurement as coupling, record formation, and conditioning

Within standard quantum theory, an ideal measurement can be represented in stages.

First, a system couples unitarily to an apparatus:

\[
\left(
\sum_i c_i|i\rangle_S
\right)
|A_0\rangle
\longrightarrow
\sum_i
c_i
|i\rangle_S|A_i\rangle.
\]

Second, the apparatus becomes correlated with an environment:

\[
\sum_i
c_i
|i\rangle_S|A_i\rangle|E_i\rangle.
\]

Third, an observer conditions on an accessible record \(i\), assigning a corresponding post-measurement state.

This architecture naturally expresses:

- global correlation;
- local decoherence;
- stable record formation;
- and context-indexed conditioning.

It also clarifies the role of accessibility. A measurement does not simply reveal every property the system carried independently of the interaction. It establishes a physical relation among system, apparatus, environment, and record.

But the formal stages do not settle the ontology of outcomes. The manuscript should remain neutral among interpretations unless a later CU argument explicitly selects one.

The modest claim is enough:

> Quantum measurement displays the same local–global architecture central to CU: relational structure is generated through coupling, accessibility is reorganized through records, and effective state updates depend on which records are available.

## 6.17 What the quantum section establishes

The corrected quantum section establishes the following.

### Distinctions

Purity, basis coherence, total correlation, entanglement, and recoverability are mathematically distinct. No spectrum-only scalar measures all of them.

### Exact pure-state structure

For bipartite pure states:

\[
\text{local mixedness}
\Longleftrightarrow
\text{entanglement}.
\]

This is an exact realization of globally pure relational structure that is not assignable as local purity.

### Exact resource conversion

For the two-qubit CNOT construction:

\[
C_r^B(\text{input})
=
E(\text{output}).
\]

Locally accessible basis coherence is converted into bipartite entanglement under a specified interaction.

### Decoherence architecture

Pure global unitary dynamics can produce local mixedness and suppress locally accessible interference through system–environment entanglement.

### Operational accessibility

Quantum channels reduce distinguishability, and recoverability provides a principled way to distinguish accessible, hidden, and effectively irrecoverable information.

### Limits

Quantum information geometry does not automatically provide physical dynamics. A universal entropy-based entanglement Goldilocks band does not exist. Decoherence does not by itself solve the measurement problem. No current scalar in the paper is the complete quantum realization of substantive CU coherence.

The broader interpretation is nevertheless coherent:

> **[Interpretation] Quantum theory provides a rigorous physical language in which relational structure may be globally instantiated, locally unavailable, transformed among distinct resource forms, and redistributed through reversible coupling and restricted access.**

The next section turns from quantum state structure to dynamics. It asks why the first-order flow of the classical sandbox is insufficient as a foundational physical law, how second-order motion restores inertia, oscillation, and reversibility, and how familiar wave and Schrödinger equations arise from specified actions within that expanded architecture.

---

# 7. Second-Order Coherence Dynamics and the First-Order Limit

The classical sandbox uses first-order update equations. Given a state \(p\), the vector field specifies an instantaneous direction of change:

\[
\dot p=F(p).
\]

This is the natural form for relaxation, optimization, diffusion, and many coarse-grained adaptive processes. It is not, however, the most general form required by physical dynamics.

A first-order autonomous law has no independent velocity variable. Once the present state is specified, the instantaneous direction of motion is fixed. Such a system can approach attractors, descend or ascend potentials, and exhibit complex trajectories in sufficiently high dimension. But a pure gradient flow does not naturally support conservative oscillation, inertial overshoot, propagating wave modes, or time-reversal-symmetric mechanics. Its defining tendency is relaxation.

The framework therefore introduces a second-order variational dynamics on the same kind of statistical state space. The change is conceptually small and physically significant. The state of motion is no longer exhausted by the configuration \(\rho\); it includes a tangent velocity \(\dot\rho\). A system can continue moving through state space even when the instantaneous force vanishes. Potential and kinetic contributions can exchange. Oscillations and wave equations become possible. In an isolated regime, energy can be conserved. With environmental damping, the same system can reduce to an effective first-order flow.

This section develops that dynamics while preserving three distinctions.

First, second-order dynamics is **dynamically foundational only after temporal parameterization has become meaningful**. It does not precede the logical conditions for ordered change discussed in Section 4.

Second, the choice of a state-space geometry does not uniquely determine the physical potential. The general architecture constrains the form of motion, while the selected potential and state variables determine the effective physics.

Third, the Madelung–Schrödinger action is an exact variational representation of nonrelativistic quantum mechanics, but it is not automatically identical to the simple natural-mechanical Lagrangian on the probability simplex. Their precise relation must be demonstrated rather than assumed.

The result is a layered dynamical picture:

\[
\boxed{
\text{pre-temporal admissibility}
\rightarrow
\text{ordered temporal evolution}
\rightarrow
\text{reversible variational dynamics}
\rightarrow
\text{damped effective flow}.
}
\]

## 7.1 Logical priority and dynamical fundamentality

The Coherence Ladder begins from relations and distinctions without assuming physical time. Section 4 then asks what must be true for admissible transitions to support temporal order and for that order to admit a clock parameter.

The Hamiltonian formulation already writes

\[
\rho(t),
\qquad
\dot\rho(t),
\qquad
\ddot\rho(t).
\]

It therefore presupposes a temporally parameterized trajectory.

There is no contradiction if two kinds of priority are distinguished.

### Logical priority

Relational structure, partial separability, distinguishable configurations, admissible transitions, and orderability are conditions under which temporal language becomes applicable.

### Dynamical fundamentality

Once physical evolution is parameterized, a second-order reversible law may underlie first-order dissipative descriptions.

The statement

\[
\text{second-order dynamics is foundational}
\]

must therefore be read as:

> **[Hypothesis] Within the domain of temporally ordered physical evolution, the undamped second-order variational law is more fundamental than the first-order relaxation law, which appears as an environmentally reduced limit.**

It must not be read as:

> Acceleration is conceptually prior to every condition needed to define temporal succession.

This distinction also prevents a circular derivation of time. The second-order theory may explain the physical character of evolution after temporal order is available. It does not by itself explain how the first order relation “before/after” becomes possible.

## 7.2 Why first-order gradient flow is not enough

Consider a one-dimensional gradient descent:

\[
\dot x=-\frac{dV}{dx}.
\]

If \(x\) is at a point where \(dV/dx=0\), it stops. If displaced in a convex potential, it returns monotonically toward a minimum under ordinary conditions. There is no independent momentum carrying it past equilibrium.

By contrast, Newtonian motion is

\[
\ddot x=-\frac{dV}{dx}.
\]

A particle approaching the bottom of a potential well generally overshoots. Kinetic energy carries it onward; the restoring force reverses its direction; oscillation results.

With friction,

\[
\ddot x+\eta\dot x=-\frac{dV}{dx},
\]

the behavior depends on the ratio of damping to natural frequency:

- weak damping permits decaying oscillations;
- critical damping gives the fastest nonoscillatory return;
- strong damping eliminates the fast inertial mode and leaves slow relaxation.

The same structural distinction carries to a statistical manifold. A first-order natural-gradient flow is appropriate when momentum-like degrees of freedom have already relaxed or been integrated out. A second-order law is needed when their persistence matters.

This does not show that every physical variable must obey a second-order equation. The Schrödinger equation, Dirac equation, and Hamilton’s canonical equations are first order in time but encode reversible phase-space dynamics. The deeper distinction is not simply the number of visible time derivatives. It is between:

- **dissipative state-only flow**, and
- **reversible dynamics on an enlarged state or phase space**.

The natural-mechanical formulation below realizes the second through \((\rho,\dot\rho)\). The density–phase formulation realizes it through the canonical pair \((\rho,\Theta)\).

## 7.3 Configuration space and Fisher geometry

Let

\[
\mathcal M
\]

be a manifold of admissible configurations. For a finite probability model, take the open simplex

\[
\Delta_{n-1}^{\circ}
=
\left\{
\rho_i>0,\;
\sum_i\rho_i=1
\right\}.
\]

A tangent vector \(v\in T_\rho\Delta_{n-1}^{\circ}\) satisfies

\[
\sum_i v_i=0.
\]

The Fisher–Rao inner product is

\[
\boxed{
g_\rho(v,w)
=
\sum_i
\frac{v_iw_i}{\rho_i}.
}
\]

This metric assigns dynamical significance to statistical distinguishability. A coordinate change that appears small in ordinary Euclidean distance may be large in Fisher distance when it strongly alters the relative likelihood of a rare event.

For a scalar functional \(V(\rho)\), the Fisher natural gradient is

\[
\boxed{
[\operatorname{grad}_F V]_i
=
\rho_i
\left(
\frac{\partial V}{\partial\rho_i}
-
\sum_j
\rho_j
\frac{\partial V}{\partial\rho_j}
\right).
}
\]

It lies in the tangent space:

\[
\sum_i
[\operatorname{grad}_F V]_i=0.
\]

The geometry should not be confused with substantive coherence. It tells us how to measure tangent vectors and define coordinate-invariant gradients. It does not tell us which potential \(V\) nature uses.

### The square-root representation

Define

\[
x_i=2\sqrt{\rho_i}.
\]

Then

\[
\sum_i x_i^2=4
\]

and

\[
\sum_i\frac{d\rho_i^2}{\rho_i}
=
\sum_i dx_i^2.
\]

The Fisher simplex is therefore isometric, up to this representation, to the positive orthant of a sphere of radius two.

This observation has several uses.

The coordinates \(x_i=2\sqrt{p_i}\) enforce \(p_i\geq0\) algebraically. They do not imply that an unrestricted geodesic on the ambient sphere remains in the positive orthant; positivity preservation must still be established for the chosen vector field, boundary condition, or numerical integrator. The representation also clarifies why phase-extended variables take the form

\[
\psi_i=\sqrt{\rho_i}\,e^{i\phi_i}.
\]

It also corrects a common misconception: the simplex boundary is not at infinite Fisher–Rao distance. It lies at finite distance in the spherical representation. Positivity preservation must therefore follow from the vector field, parameterization, conserved energy, or imposed domain—not from an infinite-distance barrier.

## 7.4 The natural-mechanical Lagrangian

On a Riemannian configuration space \((\mathcal M,g)\), define

\[
\boxed{
L(\rho,\dot\rho)
=
\frac12
g_\rho(\dot\rho,\dot\rho)
-
V(\rho).
}
\]

For the Fisher simplex,

\[
L
=
\frac12
\sum_i
\frac{\dot\rho_i^2}{\rho_i}
-
V(\rho),
\]

with normalization enforced by restricting to the simplex or introducing a Lagrange multiplier.

The Euler–Lagrange equation is most cleanly written covariantly:

\[
\boxed{
\frac{D\dot\rho}{dt}
=
-\operatorname{grad}_F V(\rho).
}
\]

In local coordinates,

\[
\boxed{
\ddot\rho^{\,i}
+
\Gamma^{i}{}_{jk}(\rho)
\dot\rho^{\,j}
\dot\rho^{\,k}
=
-[\operatorname{grad}_F V]^i.
}
\]

### Normalized and dimensionful forms

The compact equations above use a normalized unit-inertia convention. Because the simplex coordinates are dimensionless probabilities and the Fisher metric is dimensionless, the displayed kinetic term has units of inverse time squared. To restore physical dimensions, introduce an effective Fisher inertia \(M_F\) and a dimensionful potential energy \(U\):

\[
L_{\mathrm{phys}}
=
\frac{M_F}{2}
g_\rho(\dot\rho,\dot\rho)
-
U(\rho).
\]

Then

\[
\boxed{
M_F\frac{D\dot\rho}{dt}
=
-\operatorname{grad}_F U.
}
\]

Here

\[
[M_F]=[\mathrm{energy}]\,[\mathrm{time}]^2,
\qquad
[U]=[\mathrm{energy}].
\]

The normalized potential is

\[
V=\frac{U}{M_F},
\]

so

\[
[V]=[\mathrm{time}]^{-2}.
\]

With dimensionful friction \(\Gamma_F\) and force noise \(\Xi\),

\[
M_F\frac{D\dot\rho}{dt}
+
\Gamma_F\dot\rho
=
-\operatorname{grad}_F U
+
\Xi.
\]

Dividing by \(M_F\) gives the normalized equation used below,

\[
\frac{D\dot\rho}{dt}
+
\eta\dot\rho
=
-\operatorname{grad}_F V
+
\xi,
\]

with

\[
\eta=\frac{\Gamma_F}{M_F},
\qquad
\xi=\frac{\Xi}{M_F},
\]

and therefore

\[
[\eta]=[\mathrm{time}]^{-1},
\qquad
[\xi]=[\mathrm{time}]^{-2}.
\]

No empirical value of \(M_F\), \(U\), or \(\Gamma_F\) is derived in this paper. The normalized form specifies a geometric architecture; a physical model must supply its scale.

The covariant derivative matters. On a curved manifold, the coordinate acceleration \(\ddot\rho\) alone is not geometrically meaningful. The Christoffel term corrects for the way the coordinate basis changes along the trajectory.

The frequently used approximation

\[
\ddot\rho
\approx
-\operatorname{grad}_F V
\]

is valid only in a coordinate regime where curvature contributions are controlled—for example, sufficiently small perturbations in a local chart with appropriately bounded velocities. It is not the exact general equation.

### Energy conservation

If \(V\) has no explicit time dependence and no friction is present, the energy

\[
\boxed{
E
=
\frac12
g_\rho(\dot\rho,\dot\rho)
+
V(\rho)
}
\]

is conserved along solutions, subject to the usual regularity assumptions.

The kinetic term

\[
K
=
\frac12
g_\rho(\dot\rho,\dot\rho)
\]

measures the squared speed with which the state traverses statistically distinguishable configurations. The potential specifies which configurations and gradients influence that motion.

This gives an intuitive picture:

- \(V\) shapes the state-space landscape;
- \(-\operatorname{grad}_F V\) supplies the force;
- \(\dot\rho\) carries the current direction of travel;
- the metric determines the cost and meaning of motion in different directions.

## 7.5 What “structural memory” means

A second-order law requires both

\[
\rho(t_0)
\]

and

\[
\dot\rho(t_0)
\]

to determine a trajectory.

Two systems can occupy the same configuration \(\rho\) and nevertheless evolve differently because they arrive with different velocities. In that limited sense, the present state of motion carries information about the immediately preceding trajectory.

CU calls this **structural memory**.

The phrase should be interpreted carefully. It does not imply stored symbolic memory, conscious recollection, or a literal record of the entire past. It means only that the dynamically sufficient instantaneous state is enlarged from configuration to configuration-plus-velocity.

This enlargement permits:

- inertial continuation;
- phase;
- overshoot;
- oscillation;
- resonant response;
- mode structure.

It also changes the meaning of “activity.” A first-order gradient system moves only because the present state has a nonzero gradient. A second-order system with nonzero velocity continues even where the force momentarily vanishes.

That is intrinsic activity in a mechanical sense, not agency or purpose.

## 7.6 Damping and environmental reduction

Real systems are rarely isolated. Introduce friction and, where appropriate, environmental noise:

\[
\boxed{
\frac{D\dot\rho}{dt}
+
\eta\dot\rho
=
-\operatorname{grad}_F V(\rho)
+
\xi(t).
}
\]

Here:

- \(\eta>0\) is an effective damping coefficient;
- \(\xi(t)\) represents fluctuating environmental forces.

In a specified microscopic bath or generalized-Langevin model, friction and noise correlations may be related by an appropriate fluctuation–dissipation theorem (Callen & Welton, 1951). No universal manifold-level relation is assumed here. The present manuscript requires only the deterministic overdamped structure.

In the normalized unit-inertia schematic equation, suppose the characteristic relaxation of velocity occurs on a timescale

\[
\tau_v\sim\eta^{-1}.
\]

With a nontrivial mass or inertia operator, the relaxation scale is set by the relevant spectrum of that operator relative to the damping operator. Assume that the configuration changes appreciably on a slower timescale. After the fast transient, the covariant acceleration becomes subleading:

\[
\frac{D\dot\rho}{dt}
\ll
\eta\dot\rho.
\]

Then

\[
\eta\dot\rho
\approx
-\operatorname{grad}_F V+\xi,
\]

so

\[
\boxed{
\dot\rho
\approx
-\frac1\eta
\operatorname{grad}_F V
+
\frac1\eta\xi.
}
\]

The deterministic limit is a first-order natural-gradient flow.

This is a singular reduction, not the claim that acceleration is identically zero. The full solution generally contains:

1. a rapid transient in which velocity relaxes;
2. a slow manifold on which configuration follows the gradient flow;
3. corrections controlled by the ratio of inertial and damping timescales.

For the deterministic covariant equation

\[
\frac{D\dot q}{dt}+\eta\dot q=F(q),
\]

The technical supplement gives the formal post-transient expansion

\[
\boxed{
\dot q
=
\eta^{-1}F
-
\eta^{-3}\nabla_{F}F
+
O(\eta^{-5}),
}
\]

where \(\nabla_{F}F\) denotes the covariant derivative of the force field along itself. When \(F=O(1)\), the absolute correction to the slow velocity is generically \(O(\eta^{-3})\), while its size relative to the leading \(O(\eta^{-1})\) velocity is \(O(\eta^{-2})\).

A fixed-time configuration discrepancy does not isolate that correction unless the initialization and normalization are stated. With rest initialization, the fast velocity layer produces an \(O(\eta^{-2})\) absolute—or state-normalized—position slip. Initializing on the leading slow manifold, \(\dot q(0)=F(q_0)/\eta\), suppresses that term. In the linear open-chain comparison reported in the technical supplement, the remaining state-normalized position error is \(O(\eta^{-3})\), while the error relative to the total \(O(\eta^{-1})\) overdamped displacement is \(O(\eta^{-2})\). The relative velocity error is \(O(\eta^{-2})\) under both initializations after the fast transient.

The original six-point slope near \(-1.87\) is reproducible, but it belongs to a rest-initialized, fixed-time position norm and is dominated asymptotically by the initial layer. It therefore does not provide evidence for the post-transient \(-\eta^{-3}\nabla_FF\) term. The slow-manifold reduction remains conditional on smoothness, scale separation, normal hyperbolicity, and control of the boundary layer.

The first-order law is therefore an effective equation valid after fast degrees of freedom have been eliminated.

## 7.7 Recovering the classical sandbox flow

Section 3 studied the Fisher-natural flow

\[
\dot p
=
\alpha A+\beta B,
\]

where

\[
A=\operatorname{grad}_F D,
\qquad
B=\operatorname{grad}_F S.
\]

This is the natural-gradient ascent of

\[
F(p)
=
\alpha D(p)+\beta S(p):
\]

\[
\dot p
=
\operatorname{grad}_F F.
\]

It can be recovered from the overdamped equation by choosing

\[
V(p)
=
-F(p)
=
-\alpha D(p)-\beta S(p),
\]

up to an overall scaling absorbed into time or \(\eta\):

\[
\dot p
\approx
-\frac1\eta\operatorname{grad}_F V
=
\frac1\eta
\left(
\alpha A+\beta B
\right).
\]

This relation clarifies the status of the Universal Flow Equation.

The geometry supplies the natural-gradient operation. The selected potential supplies the objective. The environment supplies the damping regime. None of these alone fixes the others.

In particular, choosing

\[
V=-D
\]

produces differentiation ascent. It does not prove that the universe maximizes substantive coherence. To model substantive coherence, the potential would have to be grounded in actual physical constraints, interactions, and persistence conditions.

The first-order sandbox is therefore best understood as an illustrative overdamped sector of a wider dynamical architecture.

## 7.8 Time reversal, damping, and the arrow

The undamped natural-mechanical equation is time-reversal symmetric under

\[
t\mapsto -t,
\qquad
\dot\rho\mapsto-\dot\rho,
\]

when the potential is time independent and no time-asymmetric terms are present.

The damped equation is not invariant under the same transformation because

\[
\eta\dot\rho
\]

changes sign. Friction selects a temporal orientation.

But friction is an effective description of coupling to omitted degrees of freedom. At the larger system-plus-environment level, the dynamics may again be reversible. The local arrow then depends on:

- special boundary conditions;
- growth of correlations;
- environmental record formation;
- coarse-graining;
- and restricted access.

This connects Section 7 back to Section 4.

The Hamiltonian equation supplies reversible evolution. The first-order limit supplies a directed relaxation law. The arrow is not derived merely by writing a positive damping coefficient; that coefficient already encodes an orientation inherited from the environmental state and coarse-graining procedure.

A complete CU account of the arrow must therefore explain why the relevant environmental boundary conditions are asymmetric. The present architecture shows how reversible global dynamics can yield directed local flow, but it does not yet derive the cosmological origin of the direction.

## 7.9 Effective scalar-field realization

Second-order dynamics permits wave propagation. To exhibit this, consider an effective scalar field

\[
\phi(x,t)
\]

on a pre-existing spatial domain and the Lagrangian density

\[
\boxed{
\mathcal L_\phi
=
\frac12
(\partial_t\phi)^2
-
\frac{c_\phi^2}{2}
|\nabla\phi|^2
-
\frac{\mu^2}{2}
\phi^2.
}
\]

The Euler–Lagrange equation is

\[
\boxed{
\partial_t^2\phi
-
c_\phi^2\nabla^2\phi
+
\mu^2\phi
=
0.
}
\]

For \(\mu=0\), this is the scalar wave equation. With relativistic normalization and appropriate units, the massive case has Klein–Gordon form.

The field admits plane-wave modes

\[
\phi
\propto
e^{i(k\cdot x-\omega t)}
\]

with dispersion

\[
\omega^2
=
c_\phi^2|k|^2+\mu^2.
\]

In these coordinates,

\[
[c_\phi]=[\mathrm{length}]\,[\mathrm{time}]^{-1},
\qquad
[\mu]=[\mathrm{time}]^{-1}.
\]

Thus \(\mu\) is a frequency gap in the displayed noncovariant normalization. It becomes a particle mass only after a relativistic unit convention is chosen; with wave speed \(c_\phi\), a corresponding physical rest mass would satisfy \(M_\phi c_\phi^2=\hbar\mu\).

The result demonstrates what second-order dynamics adds. Spatial gradient energy acts as a restoring coupling among neighboring degrees of freedom, while the kinetic term permits disturbances to propagate rather than merely diffuse.

### Lattice realization

On a one-dimensional lattice with spacing \(\ell\), let

\[
V_{\mathrm{grad}}
=
\frac{\kappa_{\mathrm{lat}}}{2}
\sum_n
(\phi_{n+1}-\phi_n)^2.
\]

The equation of motion is

\[
\ddot\phi_n
=
\kappa_{\mathrm{lat}}
(\phi_{n+1}-2\phi_n+\phi_{n-1}),
\]

and a mode

\[
\phi_n\propto e^{i(kn\ell-\omega t)}
\]

has dispersion

\[
\boxed{
\omega^2(k)
=
4\kappa_{\mathrm{lat}}
\sin^2
\left(
\frac{k\ell}{2}
\right).
}
\]

At long wavelength,

\[
\omega^2
\approx
\kappa_{\mathrm{lat}}\ell^2k^2.
\]

The coefficient convention should be stated explicitly. The companion verification script writes

\[
V_{\mathrm{grad}}=\kappa\sum_n(\phi_{n+1}-\phi_n)^2,
\]

which produces

\[
\ddot\phi_n=2\kappa(\phi_{n+1}-2\phi_n+\phi_{n-1}).
\]

Therefore the two notations agree under

\[
\boxed{\kappa_{\mathrm{lat}}=2\kappa}.
\]

The lattice dimensions are

\[
[\kappa_{\mathrm{lat}}]=[\mathrm{time}]^{-2},
\qquad
[\ell]=[\mathrm{length}],
\]

so the long-wavelength propagation speed is

\[
c_{\mathrm{eff}}
=
\ell\sqrt{\kappa_{\mathrm{lat}}}.
\]

This is an exact result for the posited lattice model.

Its epistemic status must remain clear. The construction assumes:

- a scalar degree of freedom;
- a neighborhood relation;
- a local gradient potential;
- a time parameter;
- and, in the continuum version, spatial geometry.

It therefore does not derive spacetime from a pre-geometric simplex. It shows that once these structures are supplied, the second-order CU architecture accommodates standard wave dynamics.

The relational-geometry program of Section 8 must eventually explain how the neighborhood structure and continuum domain arise.

## 7.10 The density–phase state space

Nonrelativistic quantum mechanics suggests a different enlargement.

Let

\[
\rho(x,t)>0
\]

be a normalized density, and let

\[
\Theta(x,t)
\]

be a phase-like Hamilton principal function. Define

\[
\boxed{
\psi(x,t)
=
\sqrt{\rho(x,t)}
e^{i\Theta(x,t)/\hbar}.
}
\]

The pair \((\rho,\Theta)\) contains both amplitude and phase. It is richer than the probability density alone.

This state space is naturally connected to the square-root representation of Fisher geometry, but the phase is an additional variable. It cannot be derived from \(\rho\) because different wavefunctions can share the same density and differ in current or interference behavior.

The phase carries information needed for reversible quantum evolution. In hydrodynamic language,

\[
v=\frac{\nabla \Theta}{m}
\]

acts as a velocity field.

This gives a second realization of structural memory. Instead of using \((\rho,\dot\rho)\), the theory uses a canonical pair \((\rho,\Theta)\). The phase determines the probability current and therefore contains dynamical information not present in the instantaneous density.

## 7.11 Fisher-information action and the Madelung equations

Consider the action

\[
\boxed{
\mathcal A[\rho,\Theta]
=
\int
dt\,d^dx
\left[
\rho
\left(
\partial_t\Theta
+
\frac{|\nabla \Theta|^2}{2m}
+
V_{\mathrm{ext}}
\right)
+
\frac{\hbar^2}{8m}
\frac{|\nabla\rho|^2}{\rho}
\right].
}
\]

Boundary terms are assumed to vanish or be controlled.

The first term makes \(\rho\) and \(\Theta\) a canonical pair. The second is the kinetic energy density of a flow with velocity \(\nabla \Theta/m\). The third couples to an external potential. The fourth is proportional to the Fisher information of the spatial density:

\[
I_F[\rho]
=
\int
\frac{|\nabla\rho|^2}{\rho}
\,d^dx.
\]

### Variation with respect to \(\Theta\)

The Euler–Lagrange equation gives

\[
\boxed{
\partial_t\rho
+
\nabla\cdot
\left(
\rho
\frac{\nabla \Theta}{m}
\right)
=
0.
}
\]

This is the continuity equation.

### Variation with respect to \(\rho\)

The second equation is

\[
\boxed{
\partial_t\Theta
+
\frac{|\nabla \Theta|^2}{2m}
+
V_{\mathrm{ext}}
-
\frac{\hbar^2}{2m}
\frac{\nabla^2\sqrt\rho}{\sqrt\rho}
=
0.
}
\]

The final term is the quantum potential:

\[
\boxed{
Q[\rho]
=
-\frac{\hbar^2}{2m}
\frac{\nabla^2\sqrt\rho}{\sqrt\rho}.
}
\]

Together, the two equations are the Madelung equations.

Substituting

\[
\psi=\sqrt\rho\,e^{i\Theta/\hbar}
\]

combines them into

\[
\boxed{
i\hbar
\partial_t\psi
=
\left(
-\frac{\hbar^2}{2m}\nabla^2
+
V_{\mathrm{ext}}
\right)
\psi.
}
\]

Thus the stated density–phase action is exactly equivalent, locally and under the required regularity conditions, to the nonrelativistic Schrödinger equation.

## 7.12 What is exact and what is selected

The equivalence just derived is exact given:

- the fields \((\rho,\Theta)\);
- the action above;
- the coefficient \(\hbar^2/8m\);
- suitable smoothness and boundary conditions;
- and appropriate global phase conditions.

The derivation does not show that the Fisher term follows uniquely from the classical differentiation functional \(D\). Nor does it show that the coefficient \(\hbar\) can be obtained from the transcendental principle of coherence.

The Fisher-information term is a specific physical choice. It has been motivated through minimum-Fisher-information and exact-uncertainty variational programs, each of which adds physical assumptions beyond the bare probability geometry (Reginatto, 1998; Hall & Reginatto, 2002). Within CU, it is natural because the framework already privileges statistical geometry. Naturalness is not uniqueness.

The correct claim is:

> **[Conditional result] On an extended density–phase state space, the specified Fisher-information action yields the Madelung equations and is mathematically equivalent to nonrelativistic Schrödinger dynamics.**

The stronger claim

> CU uniquely derives quantum mechanics from coherence

is not established.

## 7.13 Relation between the two Hamiltonian formulations

The term *Hamiltonian CU* can refer to two related but not yet identical constructions.

### Natural mechanical dynamics on the simplex

\[
L_{\mathrm{mech}}
=
\frac12
g_\rho(\dot\rho,\dot\rho)
-
V(\rho)
\]

produces a second-order equation for \(\rho\).

### Canonical density–phase dynamics

\[
\mathcal A[\rho,\Theta]
=
\int
\left[
\rho\,\partial_t\Theta
-
\mathcal H(\rho,\Theta)
\right]
dt\,d^dx
\]

up to sign convention, produces first-order Hamilton equations for the canonical pair \((\rho,\Theta)\), equivalent to Schrödinger evolution for the chosen Hamiltonian.

Both are variational and reversible. Both enlarge a state-only gradient flow by retaining dynamical information. But they are not automatically the same theory written in two coordinate systems.

To identify them, the paper would need to construct an explicit Legendre transform or reduction showing how \(\Theta\) corresponds to momentum conjugate to \(\rho\), how the Fisher kinetic form maps to the canonical field Hamiltonian, and under what conditions eliminating \(\Theta\) yields the second-order simplex equation.

That derivation is not supplied here.

The honest unification claim is therefore architectural:

\[
\boxed{
\text{both formulations instantiate reversible variational dynamics on an enlarged statistical state space}.
}
\]

Whether they are sectors of one unique foundational action is an open problem.

This clarification strengthens rather than weakens the program. It prevents an exact Schrödinger equivalence from being used to conceal a missing bridge between two different variational structures.

## 7.14 The Wallstrom-type global phase condition

The Madelung equations are local differential equations. Quantum wavefunctions carry additional global phase structure.

For a single-valued wavefunction,

\[
\psi
=
\sqrt\rho\,e^{i\Theta/\hbar},
\]

the phase change around a closed loop must satisfy

\[
\boxed{
\oint_\gamma
\nabla \Theta\cdot d\ell
=
2\pi\hbar n,
\qquad
n\in\mathbb Z,
}
\]

around appropriate loops avoiding nodes.

A purely hydrodynamic theory of \((\rho,\Theta)\) may admit velocity fields whose circulation is not quantized. Such solutions do not correspond globally to single-valued quantum wavefunctions. This is the Wallstrom-type objection (Wallstrom, 1994).

The phase condition can be imposed by defining the state space in terms of \(\psi\) from the beginning. But then it is part of the quantum kinematics rather than something derived from the local action.

A future CU derivation would need to explain why the admissible phase bundle has the required topology and quantization. Possible routes involve single-valuedness, representation theory, topology of nodal sets, or gauge structure, but none is completed here.

The recovery is therefore exact on the quantum-admissible sector, not on every formal solution of the unconstrained hydrodynamic equations.

## 7.15 The Schrödinger recovery and the reconstruction route

Sections 5 and 6 approached quantum theory through state-space structure:

- purification;
- non-simplex geometry;
- contextual accessibility;
- operational reconstruction.

Section 7 approaches it through dynamics:

- density and phase;
- Fisher-information action;
- Madelung equations;
- Schrödinger evolution.

These routes are complementary.

The reconstruction route asks:

> Why should the state space and operational structure be quantum rather than classical?

The dynamical route asks:

> Given density–phase variables and a specified action, how does Schrödinger evolution arise?

Neither route currently completes the other.

An operational reconstruction may identify complex Hilbert space and quantum channels without selecting a unique Hamiltonian or explaining \(\hbar\). The Fisher-action derivation may reproduce Schrödinger’s equation without proving that the underlying operational state space is uniquely quantum.

A mature CU theory would connect them:

\[
\boxed{
\text{operational principles}
\Longrightarrow
\text{quantum kinematics}
}
\]

and

\[
\boxed{
\text{constraint-grounded variational principle}
\Longrightarrow
\text{quantum dynamics}.
}
\]

The present paper supplies plausible bridge structures and exact conditional recoveries, not the completed two-sided derivation.

## 7.16 Damping the density–phase dynamics

Environmental coupling can also be introduced in the quantum sector, but care is required.

A naive friction term added directly to the Schrödinger equation may violate unitarity, norm preservation, or complete positivity. Standard finite-dimensional, time-homogeneous Markovian open-system dynamics is represented by a GKSL/Lindblad-type master equation (Gorini, Kossakowski, & Sudarshan, 1976; Lindblad, 1976):

\[
\dot\rho
=
-\frac{i}{\hbar}[H,\rho]
+
\sum_k
\left(
L_k\rho L_k^\dagger
-
\frac12
\{L_k^\dagger L_k,\rho\}
\right).
\]

This is not generally identical to the overdamped limit of the natural-mechanical simplex equation.

It may be possible, in specific semiclassical or hydrodynamic regimes, to eliminate rapidly relaxing phase or momentum variables and obtain a first-order equation for a probability density. But that reduction must be derived for the model at hand.

Accordingly, the manuscript should not assert without proof that the original first-order Universal Flow Equation is simply “the overdamped limit of quantum mechanics.” The valid general statement is narrower:

> The natural-mechanical second-order CU equation reduces to a first-order natural-gradient flow under strong damping. Separately, the density–phase Fisher action reproduces Schrödinger dynamics. Establishing a controlled reduction from the latter to the former requires an explicit open-system derivation.

This is an important open bridge.

## 7.17 Regime map

The current architecture can be summarized as follows.

| State structure | Variational structure | Environmental regime | Effective equation | Status |
|---|---|---|---|---|
| Statistical configuration \(\rho\) | Natural mechanical \(K_F-V\) | Weak damping | Covariant second-order motion | General proposal |
| Statistical configuration \(\rho\) | Same | Strong damping | First-order natural-gradient flow | Controlled formal limit under timescale separation |
| Effective scalar \(\phi(x,t)\) | Local field action | Weak damping | Wave/Klein–Gordon type | Exact after field and locality ansatz |
| Density–phase \((\rho,\Theta)\) | Fisher-information canonical action | Closed | Madelung/Schrödinger | Exact under phase and regularity conditions |
| Density operator \(\rho\) | Hamiltonian plus dissipator | Open Markovian | Lindblad type | Standard imported framework (Gorini et al., 1976; Lindblad, 1976) |
| Accessibility network | Yet to be derived | — | Evolving relational geometry | Open program |

The table expresses a structural unity, not yet a unique fundamental equation. Each row requires choices of variables, potential, coupling, and approximation.

## 7.18 The role of the potential

The potential is where much of the physical content resides.

The geometry tells us what counts as a natural gradient and how kinetic energy is measured. The general variational principle tells us how forces generate motion. But different potentials yield different laws:

- a quadratic local term gives harmonic behavior;
- a spatial gradient penalty gives wave propagation;
- a mass term changes dispersion;
- a Fisher-information term generates the quantum potential in the density–phase action;
- nonlinear interactions produce different mode couplings and phases.

If almost any desired equation can be reproduced by choosing an appropriate potential, then formal accommodation alone is not explanatory unification.

CU must therefore eventually supply constraints on admissible potentials. Possible sources include:

- invariance under reparameterization;
- locality or emergent locality;
- compositional consistency;
- stability;
- coarse-graining behavior;
- symmetry;
- renormalization;
- conservation laws;
- and the substantive coherence requirements of the modeled system.

Until such constraints are derived, the framework establishes a common mathematical architecture in which known theories can be embedded. It does not yet show why nature selects these particular theories.

This is one of the central open problems of the entire Physics program.

## 7.19 What second-order dynamics contributes to CU

Despite the open issues, the second-order extension contributes several real advances.

### It separates fundamental motion from relaxation

The first-order flow is no longer asked to explain both conservative microphysics and dissipative macrodynamics.

### It supplies inertia-like persistence

The dynamically sufficient state includes a direction of motion, whether represented by \(\dot\rho\) or a conjugate phase.

### It permits oscillation and propagation

Restoring potentials and spatial couplings can produce normal modes and waves.

### It supports variational and conservation structure

Time-translation invariance yields energy conservation; additional symmetries may yield Noether charges.

### It clarifies the origin of first-order flow

Strong environmental damping can eliminate fast momentum-like variables and leave a slow natural-gradient equation.

### It sharpens the temporal problem

A reversible foundation does not itself explain the arrow. Damping and irrecoverability must be related to environmental boundary conditions and coarse-graining.

These are architectural achievements even before a unique physical potential has been derived.

## 7.20 Interpretive significance and limits

The second-order formulation invites a process-oriented interpretation.

Reality is not pictured as a passive inventory of configurations waiting for an external rule to update them. A physical state of motion includes tendencies that persist, interact, and form modes. The universe is “active” in the minimal sense that evolution contains internally carried dynamical structure.

This resonates with CU’s broader process orientation, but the mathematics should not be anthropomorphized.

Second-order dynamics does not imply:

- consciousness;
- intention;
- cosmic desire;
- moral direction;
- or inevitable increase of substantive coherence.

It implies only that a reversible variational description retains momentum- or phase-like information beyond instantaneous configuration.

Likewise, calling the potential a “coherence potential” does not make its minima or maxima normatively good. Its physical meaning must be established in each model.

The appropriate interpretive conclusion is:

> **[Interpretation] Second-order CU portrays physical becoming as structured motion through a constrained possibility space, with first-order adaptation and relaxation emerging when environmental coupling suppresses the independent persistence of motion.**

## 7.21 Open problems in the Hamiltonian program

The analysis leaves a clear research agenda.

1. **Derive the configuration variables.** Explain how the foundational relational substrate gives rise to a probability simplex, scalar field, density–phase pair, or density operator.

2. **Constrain the potentials.** Show why physically realized potentials belong to a restricted class rather than being selected ad hoc to reproduce known equations.

3. **Unify the variational formulations.** Establish the precise relation between the second-order natural-mechanical action and the first-order canonical density–phase action.

4. **Derive the phase.** Explain why the additional variable \(\Theta\) exists and why it has the topology required for quantum interference.

5. **Derive or interpret \(\hbar\).** The coefficient of the Fisher term is presently inserted.

6. **Resolve circulation quantization.** Derive the global quantum phase condition rather than merely impose it.

7. **Extend beyond scalar nonrelativistic theory.** Include spin, fermionic statistics, gauge fields, relativistic quantum fields, and interacting many-body systems.

8. **Control the full Fisher geometry.** Analyze the nonlinear covariant dynamics without discarding connection terms.

9. **Prove positivity and global existence.** Determine which potentials and initial data preserve the admissible state space.

10. **Derive open-system reductions.** Connect global reversible dynamics to CPTP reduced dynamics and identify when a natural-gradient limit is valid.

11. **Connect to temporal emergence.** Show how the Hamiltonian time parameter arises from the order-theoretic structure of Section 4.

12. **Produce distinctive predictions.** Identify empirical consequences not shared by standard reformulations of mechanics, hydrodynamics, or quantum theory.

## 7.22 Conclusion: from dynamics to geometry

The dynamical architecture can be summarized in one sequence:

\[
\boxed{
\begin{aligned}
&\text{admissible relational change}\\
&\downarrow\\
&\text{temporally parameterized reversible dynamics}\\
&\downarrow\\
&\text{motion on a statistical or field configuration space}\\
&\downarrow\\
&\text{environmental restriction and damping}\\
&\downarrow\\
&\text{effective first-order flow}.
\end{aligned}
}
\]

The scalar and Schrödinger constructions show that familiar equations can arise within specified variational sectors. The overdamped analysis shows how relaxation dynamics can emerge from a wider reversible architecture. The remaining challenge is to explain where the spatial and causal structures presupposed by those field equations come from.

That is the task of the next stage. Section 8 turns from motion on a given space to the possibility that effective space itself arises from patterns of accessibility among relational degrees of freedom.

---

# 8. Relational Geometry from Accessibility Networks

## 8.1 The problem this section addresses

The field equations discussed in Section 7 were written on a spatial domain. A scalar field was allowed to vary with a coordinate \(x\); gradients were taken with respect to that coordinate; and propagation occurred through a geometry already available to the mathematics. Those constructions are useful because they show that CU-compatible variational principles can reproduce familiar dynamics. They do not yet explain where the spatial relations presupposed by those equations come from.

The next step in the CU program is therefore more demanding:

> Can effective spatial and causal geometry arise from stable patterns of accessibility among relational degrees of freedom?

The question is not whether a graph can be drawn and called space. Weighted graphs, distance matrices, and network embeddings are mathematically commonplace. The physical question is whether a microscopic relational system can generate, without having spatial geometry inserted into its definition, the structures that make ordinary spacetime possible:

- stable neighborhoods;
- approximately local interaction;
- finite propagation;
- dimensional scaling;
- metric continuity;
- causal cones;
- local Lorentz symmetry;
- and dynamical backreaction.

The present section does not complete that program. It constructs its first mathematically controlled stage and identifies the bridge principles required for the rest.

The status of the proposal is therefore layered.

1. **[Derived construction]** A suitable weighted relation can be converted into a path metric.
2. **[Conditional result]** Families of such metric networks may possess continuum and dimensional limits under additional regularity assumptions.
3. **[Hypothesis]** Physically selected accessibility relations generate the effective geometry experienced as space.
4. **[Open problem]** The dynamics of those relations select a stable \(3+1\)-dimensional Lorentzian regime with the symmetries of observed spacetime.

Keeping these levels distinct is essential. The first is elementary mathematics. The fourth would be a foundational result.

## 8.2 Why accessibility is a candidate geometric primitive

A geometry tells us which events or systems are near, which are far, which can interact directly, and how routes between them compose. In ordinary physics these relations are represented by a metric already defined on a manifold. CU asks whether the order of explanation can be reversed: perhaps the manifold summarizes a prior structure of possible access.

Accessibility here is not merely what a human observer happens to know. It is an operational relation between physical subsystems. One subsystem is accessible to another to the extent that states, interventions, signals, or correlations can be reliably transferred, discriminated, or recovered under the physically allowed operations.

This idea is attractive for three reasons.

First, physical distance is known through interaction. Rods, clocks, light signals, scattering amplitudes, and propagation delays are all operational structures. A geometry with no possible consequences for access would be physically empty.

Second, accessibility can be relational without presupposing an embedding space. A network can specify who can affect whom and at what cost before its nodes are assigned coordinates.

Third, accessibility is scale-relative. Two degrees of freedom may be distinguishable at a microscopic scale but function as one effective unit after coarse-graining. Conversely, a macroscopic region may decompose into many independently accessible components at higher resolution. This fits the CU claim that effective geometry should depend on the organization available at a given scale.

None of these considerations proves that accessibility is sufficient for geometry. They establish only that it is a plausible primitive from which geometry might be reconstructed.

## 8.3 The accessibility network

Let

\[
G=(V,E,w)
\]

be a weighted network.

- The node set \(V\) represents subsystems, events, effective degrees of freedom, or equivalence classes of microscopic configurations.
- An edge \((i,j)\in E\) indicates that a direct operational relation is available.
- The weight
  \[
  w_{ij}\geq0
  \]
  quantifies the strength, reliability, or capacity of that relation.

The physical meaning of \(w_{ij}\) must be fixed by the model. Candidate quantities include:

- mutual information between subsystems;
- connected correlation strength;
- channel capacity;
- distinguishability under allowed measurements;
- fidelity of state transfer;
- response to a controlled perturbation;
- recoverability after a local erasure;
- transition amplitude or rate;
- and effective coupling strength.

These candidates are not interchangeable. Mutual information is symmetric, while causal influence need not be. A large correlation does not imply the ability to signal. Fidelity compares states, while channel capacity characterizes transformations. A coupling parameter may be specified in a Hamiltonian whose locality is already spatial, making it circular as a proposed origin of space.

The choice of weight is therefore not a harmless detail. It determines what the emergent geometry means.

A useful distinction is:

\[
w_{ij}^{\mathrm{sim}}
\]

for symmetric similarity or shared structure, and

\[
w_{i\to j}^{\mathrm{inf}}
\]

for directed influence or transmission. The first may contribute to an effective spatial metric. The second is more naturally related to causal order. A successful spacetime model will probably require both, together with a consistency relation between them.

## 8.4 From accessibility strength to relational distance

Suppose the symmetric weights satisfy

\[
0<w_{ij}\leq w_0.
\]

Choose a monotone decreasing map \(f\) from accessibility to **strictly positive** edge cost:

\[
\ell_{ij}=f(w_{ij})>0.
\]

One useful example is

\[
\boxed{
\ell_{ij}
=
\ell_{\min}
+
\ell_0
\left[
-\log\left(\frac{w_{ij}}{w_0}\right)
\right],
\qquad
\ell_{\min}>0.
}
\]

High accessibility then corresponds to short relational separation, while weak accessibility corresponds to long separation. The positive floor prevents distinct maximally connected nodes from acquiring zero path distance.

If one instead sets \(\ell_{\min}=0\), edges with \(w_{ij}=w_0\) have zero length. Shortest-path closure then gives only a pseudometric until nodes connected by zero-length paths are identified in a quotient. Earlier versions omitted this qualification.

The logarithm has an intuitive compositional feature. If independent transfer fidelities multiply along a route, their negative logarithms add. But the logarithmic choice is not uniquely forced; other monotone maps may be appropriate for other operational quantities.

Direct edge costs need not satisfy the triangle inequality. A pair of systems might have weak direct access while both have strong access through an intermediary. The metric is therefore obtained by path closure:

\[
\boxed{
d_G(i,j)
=
\inf_{\gamma:i\leadsto j}
\sum_{(ab)\in\gamma}\ell_{ab}.
}
\]

If the graph is connected and the edge lengths are positive and symmetric, then \(d_G\) is a metric:

\[
d_G(i,j)\geq0,
\qquad
d_G(i,j)=0\Longleftrightarrow i=j,
\]

\[
d_G(i,j)=d_G(j,i),
\qquad
d_G(i,k)\leq d_G(i,j)+d_G(j,k).
\]

This is the first exact result of the spacetime program:

> **[Derived] A symmetric accessibility network with strictly positive edge costs determines a relational metric through shortest-path closure. With nonnegative costs, it determines a pseudometric unless zero-distance classes are quotiented.**

For directed weights, one may define

\[
d_{\to}(i,j)
=
\inf_{\gamma:i\leadsto j}
\sum_{(ab)\in\gamma}\ell_{a\to b},
\]

but generally

\[
d_{\to}(i,j)\neq d_{\to}(j,i).
\]

This is a directed cost or quasi-metric, not an ordinary metric. The asymmetry may be physically meaningful if it represents causal accessibility, dissipation, or an effective arrow.

## 8.5 A minimal example: neighborhoods without coordinates

Consider five subsystems \(A,B,C,D,E\). Suppose the strongest accessibility relations form the chain

\[
A-B-C-D-E,
\]

with each neighboring edge assigned length \(1\), while all direct non-neighboring relations have very large cost.

The induced path distances are then

\[
d_G(A,C)=2,
\qquad
d_G(A,E)=4.
\]

No coordinate line was assumed. Yet the network has an order and neighborhood structure resembling a one-dimensional interval.

Now add a strong edge between \(A\) and \(E\). The graph becomes a cycle. The local data have changed the effective topology: what previously behaved like an interval now behaves like a ring.

Alternatively, connect every node strongly to every other node. The network loses low-dimensional locality; every node lies close to every other. A metric still exists, but it no longer resembles an extended spatial manifold.

This example makes two points clear.

First, a relational metric does not require prior coordinates.

Second, geometry is not produced by “correlation” in the abstract. It depends on the pattern, sparsity, stability, and scaling of relations. The same number of nodes can support line-like, circle-like, tree-like, or highly nonlocal geometry.

A physical theory must therefore explain why the accessibility network enters a special regime rather than an arbitrary one.

## 8.6 Emergent locality as a dynamical achievement

Given a metric \(d_G\), define the radius-\(r\) neighborhood of node \(i\):

\[
B_r(i)
=
\{j\in V:d_G(i,j)\leq r\}.
\]

This is a mathematical neighborhood. For it to become a physical locality structure, at least four further conditions are needed.

### Interaction concentration

Most controllable interactions should occur within small \(d_G\). If strong direct influence is generic between distant nodes, the metric will not organize physical locality.

### Finite propagation

Changes should spread through neighboring relations at a bounded effective rate. For broad classes of short-range quantum lattice systems, this role is played by Lieb–Robinson-type bounds (Lieb & Robinson, 1972). An analogous bound for a CU accessibility network would require its own assumptions and proof.

### Stability

Small perturbations of the state should not completely reorder the neighborhoods. A geometry that fluctuates arbitrarily under microscopic noise cannot serve as the stable background of ordinary physical description.

### Scale persistence

The neighborhood structure should survive an appropriate range of coarse-grainings. Exact microscopic adjacency need not remain, but a recognizable local organization must reappear at larger scales.

Under these conditions, locality is not a primitive prohibition against distant relation. It is a stable organization in which direct causal influence is concentrated among relational neighbors.

This is compatible with quantum entanglement only if correlation and signalling are kept distinct. Entangled systems may exhibit strong nonclassical correlations despite large emergent spatial separation, while still respecting no-signalling. A geometry based solely on correlation magnitude could therefore place entangled distant systems artificially close. The accessibility variable used for spatial locality must either discount non-signalling correlation or combine it with a separate influence structure.

## 8.7 Dimension as a scaling property

Ordinary dimension is not merely the number of coordinates written on a page. It governs how volume grows with radius, how diffusion spreads, how spectra scale, and how fields propagate.

For a metric network define

\[
N_i(r)=|B_r(i)|.
\]

If, over a stable range of scales,

\[
N_i(r)\propto r^d,
\]

then an effective volume-growth dimension is estimated from the local slope

\[
\boxed{
d_{\mathrm{vol}}(r)
\approx
\frac{\Delta\log N_i(r)}{\Delta\log r}.
}
\]

On a finite graph, \(N_i(r)\) is a step function, so the differential notation is shorthand for a finite-difference or fitted scaling exponent over a stated range. A stable plateau near \(d\) indicates approximately \(d\)-dimensional scaling in that regime.

One may also examine a spectral dimension through a diffusion process on the graph. If the return probability behaves approximately as

\[
P_{\mathrm{return}}(\tau)
\propto
\tau^{-d_s/2},
\]

then

\[
d_s
=
-2\frac{d\log P_{\mathrm{return}}}{d\log\tau}
\]

defines a scale-dependent spectral dimension, subject to the diffusion convention and scaling regime (Ambjørn, Jurkiewicz, & Loll, 2005).

These dimensions need not agree on irregular networks. Their agreement over a wide range would be evidence for an effective manifold regime.

CU does not presently derive

\[
d_{\mathrm{eff}}=3
\]

for space or \(3+1\) for spacetime. A future theory would need to show that the dynamics select such a regime because it is stable, supports the required field content, or optimizes some independently justified coherence condition. Simply observing that three dimensions are compatible with the construction would not explain why the universe realizes them.

## 8.8 Curvature and the continuum limit

A finite network is not yet a smooth manifold. To recover continuum geometry one needs a sequence of increasingly refined networks

\[
G_1,G_2,\ldots,G_N,\ldots
\]

whose metric, spectral, and dynamical properties converge appropriately.

Relevant diagnostics may include:

- convergence of shortest-path distances;
- convergence of graph Laplacians;
- stable volume-growth dimension;
- local curvature estimators;
- convergence of diffusion kernels;
- suppression of nonlocal links at macroscopic scales;
- and stability under coarse-graining.

Possible mathematical languages include Gromov–Hausdorff convergence, spectral convergence, graph Laplacians, diffusion maps, discrete curvature, and random geometric graph limits. **[Open methodological choice]** The appropriate formalism depends on the eventual microscopic model and must be selected before a continuum theorem can be stated.

The direction of explanation matters. One should not begin with nodes sampled from a known manifold, define weights from their manifold distances, and then claim to have derived the manifold. That procedure is useful for validating reconstruction algorithms, but it is not an emergent-geometry result.

A noncircular model must begin with a relational law that does not contain the target geometry in disguised form. It must then show that a manifold-like regime develops and remains dynamically stable.

Curvature would appear when neighborhood growth and path structure depart systematically from their flat reference behavior. In a continuum approximation this may be represented by an effective metric \(g_{ab}\) and curvature tensors derived from it. But the existence of a curvature estimator on a graph does not yet establish that the graph obeys general relativity.

## 8.9 From ordered accessibility to causal structure

Spatial distance is only part of spacetime. Causal structure is directed.

Let

\[
e_i\prec e_j
\]

mean that an intervention, signal, or physical influence associated with event \(e_i\) can contribute to event \(e_j\) within the effective description.

After transitive closure, an acyclic irreflexive influence relation defines a **strict partial order**. Adding the reflexive pairs gives an ordinary partial order. Independent events need not be comparable. This is important: a genuinely relativistic causal order should permit spacelike separation rather than forcing every event into one total sequence.

A Lorentzian spacetime contains more than this order. It also carries volume information and enough local regularity to distinguish timelike, null, and spacelike relations. In past- and future-distinguishing spacetimes, causal structure determines the conformal metric structure; supplementary volume information can fix the remaining conformal factor under suitable regularity assumptions (Malament, 1977, together with related causal-reconstruction results). But a generic directed graph does not automatically possess Lorentzian signature, light cones, or local Lorentz invariance.

The CU proposal is therefore conditional:

> **[Hypothesis] Stable directed accessibility relations, together with suitable volume and regularity data, possess a continuum regime describable by Lorentzian geometry.**

This proposal connects Section 4 to the present section. Ordered updates supply a primitive precedence relation. The accessibility network supplies relational neighborhoods and effective volume. A successful spacetime model must show how these structures become mutually consistent.

It must also explain the relation between the order parameter called time in Section 4 and the proper time measured by clocks in the emergent metric. Ordinal succession is not yet metric duration. The latter depends on the realized geometry and on the physical processes used as clocks.

## 8.10 State dependence and relational backreaction

If accessibility depends on the physical state,

\[
w_{ij}=w_{ij}[\rho],
\]

then the induced geometry is also state-dependent:

\[
d_G=d_G[\rho].
\]

This gives the minimal architecture of backreaction:

\[
\boxed{
\rho
\longrightarrow
w[\rho]
\longrightarrow
d_G[\rho].
}
\]

Matter or field organization changes accessibility; changed accessibility changes relational distance.

But this is only half of a dynamical theory. Geometry should in turn affect the evolution of the state:

\[
d_G
\longrightarrow
V[\rho;d_G]
\longrightarrow
\dot\rho\ \text{or}\ \ddot\rho.
\]

A self-consistent model therefore requires a coupled loop:

\[
\boxed{
\rho
\longleftrightarrow
w
\longleftrightarrow
g.
}
\]

A technical complication is that shortest-path distance is generally only piecewise smooth as a function of the weights: when two routes exchange optimality, \(d_G[w]\) can fail to be differentiable. Any variational backreaction model must therefore use a differentiable surrogate, work with subgradients, or prove that route-switching sets are controlled. Writing \(g[w]\) inside an action without addressing this issue would conceal a real mathematical assumption.

One possible formal strategy is to define an action

\[
I[\rho,w]
=
I_{\mathrm{state}}[\rho;w]
+
I_{\mathrm{network}}[w]
+
I_{\mathrm{coupling}}[\rho,w],
\]

then vary both \(\rho\) and \(w\). Another is to derive the weights from correlation or response functions of \(\rho\) and seek fixed points of the combined evolution.

The crucial requirement is that the network dynamics not merely be chosen to mimic Einstein evolution. The model must explain why its update law follows from the lower-level CU commitments or from an independently motivated physical principle.

## 8.11 Entanglement, error correction, and geometry

In several established research programs, entanglement and geometry are deeply related.

In static asymptotically AdS holographic settings, the Ryu–Takayanagi formula relates boundary-region entropy to the area of a bulk minimal surface; covariant extensions use extremal surfaces (Ryu & Takayanagi, 2006; Hubeny, Rangamani, & Takayanagi, 2007). Tensor-network models such as MERA display discrete AdS-like geometries in which entanglement structure and network connectivity are linked (Swingle, 2012). Quantum-error-correcting interpretations show how bulk information can be redundantly encoded and reconstructed from different boundary regions within an AdS/CFT code subspace (Almheiri, Dong, & Harlow, 2015).

These results support a restricted but important claim:

\[
\boxed{
\text{In some quantum-gravitational regimes, relational quantum information encodes geometric information.}
}
\]

They do not establish:

\[
\text{arbitrary entanglement graph}
=
\text{physical spacetime}.
\]

Nor do they show that entanglement alone determines dynamics, signature, dimension, or matter content.

CU’s contribution is to place these results within a wider accessibility framework:

- entanglement is one form of globally instantiated relation;
- a subsystem may lack access to structure present in the whole;
- different regions may reconstruct overlapping global information;
- coarse-graining changes which geometric relations remain recoverable;
- and geometry may summarize the stable architecture of such access.

This is a conceptual unification, not yet a new theorem.

## 8.12 The factorization and circularity problems

Any entanglement-based geometry begins with a decomposition into subsystems:

\[
\mathcal H
=
\bigotimes_i\mathcal H_i.
\]

But subsystem decomposition is part of what an emergent spacetime theory may need to explain. If the factors are already labeled as local regions, geometry has been assumed rather than derived.

This is the **factorization problem**.

A complete CU account would need either:

1. a pre-geometric reason why certain algebraic substructures function as subsystems;
2. a dynamical selection principle that stabilizes an effective factorization;
3. or a formulation in terms of operator algebras or relational observables that does not presuppose a fixed tensor-product decomposition.

There is a related circularity problem. If the accessibility weights are calculated using a Hamiltonian whose couplings were already declared local in a background space, then the resulting metric merely recovers the locality that was inserted.

The emergence claim becomes substantive only when the microscopic data are specified without using the target geometry.

## 8.13 A minimal computational research program

A tractable first model should be modest enough to fail clearly.

It would specify:

1. **Microscopic degrees of freedom.** A finite family of classical or quantum subsystems with no imposed spatial coordinates.
2. **State dynamics.** A Hamiltonian or stochastic law whose interaction structure is justified independently of a target manifold.
3. **Accessibility observable.** A precise \(w_{ij}[\rho]\), with its operational meaning stated.
4. **Metric construction.** A monotone weight-to-cost map and shortest-path closure.
5. **Causal observable.** A directed influence measure distinct from symmetric correlation.
6. **Coarse-graining rule.** A reproducible method for grouping degrees of freedom.
7. **Continuum diagnostics.** Volume-growth dimension, spectral dimension, curvature estimators, propagation cones, and stability tests.
8. **Backreaction test.** Evidence that changes in state reorganize geometry and that geometry constrains subsequent state evolution.
9. **Null models.** Randomized networks and alternative weight definitions against which the results are compared.
10. **Failure criteria.** Conditions under which no stable local manifold regime appears.

A model would count as progress only if its geometric properties are not already built into the microscopic interaction matrix.

The first meaningful target is not Einstein’s equation. It is the weaker result:

> Starting from non-geometric relational data, a stable low-dimensional local regime emerges over a finite range of scales.

If even that target repeatedly fails under reasonable microscopic choices, the geometry program should be narrowed.

## 8.14 What Section 8 establishes

This section establishes a legitimate mathematical route from accessibility relations to relational distance:

\[
\text{weighted accessibility}
\longrightarrow
\text{edge cost}
\longrightarrow
\text{path metric}.
\]

It also identifies how dimension, locality, causal order, and backreaction might be investigated.

It does not establish that the resulting metric is physical space, that observed spacetime has been derived, or that the geometry obeys gravitational field equations.

The most accurate conclusion is:

> **[Programmatic conclusion] CU provides a disciplined architecture for asking whether spacetime is the stable macroscopic form of relational accessibility. The first metric construction is exact; the physical identification and dynamical completion remain open.**

---

# 9. Gravity as a Conditional Completion of the Geometry Program

## 9.1 Why gravity is a separate problem

A relational metric is not yet a theory of gravity.

Section 8 showed how weighted accessibility relations may be converted into distance and how a state-dependent network might support an effective geometry. Gravity requires more. The geometry must have its own dynamics, matter must affect it, and the resulting coupled equations must reproduce the empirical content of general relativity in an appropriate regime.

Earlier formulations of CU sometimes moved too quickly across this gap. Three distinct claims were treated as though they were one:

1. a field associated with coherence can carry stress-energy;
2. horizon thermodynamics can imply Einstein-type field equations;
3. gravity is fundamentally the redistribution of coherence accessibility.

The first is a standard consequence of assigning an action to a field. The second is a conditional derivation that imports strong assumptions. The third is a CU interpretation or physical hypothesis.

This section keeps them separate and asks what would be required to connect them.

## 9.2 A coherence field as an ordinary gravitational source

Suppose an effective scalar field \(\phi\) is introduced on an already available Lorentzian spacetime with metric \(g_{\mu\nu}\). Consider the action

\[
I_\phi
=
-\frac12
\int d^{d+1}x\,\sqrt{-g}
\left[
g^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi
+
m_\phi^2\phi^2
\right].
\]

This subsection uses natural units \(c=\hbar=1\). In these units \(m_\phi\) has dimensions of inverse length (equivalently inverse time). Restoring constants replaces the mass term by \((M_\phi c/\hbar)^2\phi^2\), up to the overall normalization convention for the field action.

Variation with respect to the metric gives the standard stress-energy tensor

\[
\boxed{
T_{\mu\nu}^{(\phi)}
=
\partial_\mu\phi\,\partial_\nu\phi
-
\frac12g_{\mu\nu}
\left[
g^{\alpha\beta}\partial_\alpha\phi\,\partial_\beta\phi
+
m_\phi^2\phi^2
\right].
}
\]

This result establishes something real but limited:

> **[Derived, given the action] An effective CU scalar field can carry energy and momentum and can therefore serve as a conventional source of curvature.**

It does not establish that \(\phi\) is the fundamental coherence field, that all matter is made from it, or that the Standard Model follows from it. It also begins with spacetime geometry rather than deriving that geometry.

The field-theoretic result should therefore be understood as a compatibility test. CU can host a scalar sector with the familiar gravitational source structure.

## 9.3 Stress-energy is not yet substantive coherence

The symbol \(\phi\) should not be identified with substantive coherence merely because the field is called a coherence field.

A scalar field value may represent:

- an order parameter;
- an accessibility amplitude;
- a coarse-grained density;
- a mode of a deeper relational network;
- or a phenomenological field introduced for mathematical exploration.

To interpret its stress-energy as the gravitational effect of coherence, the paper must specify a map

\[
\phi
\longmapsto
C_{\mathrm{sub}}[\phi;K,G,\pi,T].
\]

Without such a map, the phrase “coherence carries energy” is only a naming convention.

This point mirrors the classical sandbox. A mathematically useful scalar can model one aspect of structure without exhausting the framework’s full concept of coherence.

## 9.4 Motion in a given geometry

Once a Lorentzian metric is supplied, freely falling test bodies follow timelike geodesics and light follows null geodesics in general relativity.

A worldline \(x^\mu(\lambda)\) extremizes the proper-time action

\[
I_{\mathrm{geo}}
=
-mc
\int
d\lambda\,
\sqrt{
-g_{\mu\nu}
\frac{dx^\mu}{d\lambda}
\frac{dx^\nu}{d\lambda}
}.
\]

Variation yields

\[
\boxed{
\frac{d^2x^\mu}{d\tau^2}
+
\Gamma^\mu{}_{\alpha\beta}
\frac{dx^\alpha}{d\tau}
\frac{dx^\beta}{d\tau}
=
0.
}
\]

CU may interpret geodesic motion as extremal propagation through an accessibility geometry. That is a coherent interpretation, but the geodesic equation follows from the metric action, not from the word “accessibility.”

The important distinction is:

\[
\text{deriving motion from an assumed metric}
\neq
\text{deriving the metric and its dynamics}.
\]

Any worked Schwarzschild or weak-field calculation belongs to the first category unless the metric itself has been obtained from a CU microscopic model.

## 9.5 The equivalence principle as a target constraint

General relativity is not merely a theory in which trajectories curve. Its local structure embodies the equivalence principle: sufficiently small freely falling laboratories exhibit the physics of special relativity, and nongravitational test bodies respond universally to the same spacetime geometry.

A CU gravity model must therefore explain why the effective geometry couples universally.

If different species experience different accessibility metrics

\[
g_{\mu\nu}^{(a)},
\]

then composition-dependent free fall or violations of local Lorentz invariance may result. Universality of free fall is constrained at the \(10^{-15}\) level in the MICROSCOPE final analysis, while Lorentz-violation limits are strongly sector- and coefficient-dependent and are compiled in dedicated data tables (Touboul et al., 2022; Kostelecký & Russell, 2011, with updates).

The universal metric cannot simply be assumed if universality is advertised as derived. The microscopic accessibility relations must generate a common effective causal structure for all low-energy matter sectors, or the theory must predict and survive bounds on deviations.

This gives the equivalence principle a useful role in the research program:

> **[Constraint] Any proposed accessibility geometry must possess a regime in which diverse matter excitations propagate according to one effective metric to the observed precision.**

## 9.6 The Jacobson-style route

A different path begins not with an action for the metric but with local horizon thermodynamics.

In Jacobson’s established thermodynamic argument (1995), one considers local Rindler causal horizons through arbitrary spacetime points and assumes, schematically:

1. the local horizon is chosen in an equilibrium configuration at the base point, with expansion and shear vanishing there to the required order;
2. horizon entropy is proportional to area,
   \[
   \delta S=\eta_A\,\delta A;
   \]
3. a local accelerated observer with horizon surface gravity or proper-acceleration scale \(\kappa_H\) assigns an Unruh temperature,
   \[
   T=\frac{\hbar\kappa_H}{2\pi c k_B};
   \]
4. matter energy flux across the horizon obeys a Clausius relation,
   \[
   \delta Q=T\,\delta S;
   \]
5. the horizon generators obey the Raychaudhuri equation;
6. local stress-energy conservation holds.

Requiring the thermodynamic relation to hold for every local horizon yields an equation of the form

\[
G_{\mu\nu}
+
\Lambda g_{\mu\nu}
=
\frac{8\pi G}{c^4}T_{\mu\nu},
\]

with the cosmological constant appearing as an integration freedom once stress-energy conservation and the geometric identities are imposed (Jacobson, 1995). The normalization depends on the universal entropy-area density and the Unruh temperature.

This result is profound because it suggests that Einstein’s equation may function as an equation of state or consistency condition rather than as an irreducible microscopic law.

But it does not derive spacetime from no spacetime. The argument presupposes local Lorentzian horizons, local equilibrium, area, acceleration, quantum fields or stress-energy flux, and the geometric focusing relation.

## 9.7 The CU translation of the horizon argument

CU proposes to reinterpret the ingredients of the thermodynamic argument in terms of accessibility.

A local horizon divides degrees of freedom into those accessible and inaccessible to a chosen causal domain. The entropy associated with the horizon may then be read as an entropy assigned to the reduced causal description. In different derivations this may be entanglement entropy, generalized entropy, or a thermodynamic entropy; it is not automatically the classical differentiation residual of Section 3.

The proposed dictionary is:

| Horizon-thermodynamic quantity | CU interpretation |
|---|---|
| Horizon | Boundary of causal accessibility |
| Area \(A\) | Size of the effective access boundary |
| Entropy \(S\) | Entropy of the reduced causal description, often entanglement or generalized entropy |
| Heat flux \(\delta Q\) | Energy-momentum crossing the access boundary |
| Temperature \(T\) | Operational response of the accelerated description |
| Focusing \(\delta A\) | Change in the geometry of accessibility |
| Einstein equation | Consistency condition relating flux and geometric response |

This dictionary is conceptually natural, but its entries have unequal status.

The causal-horizon interpretation is close to definition. The entropy reading is an interpretation supported by quantum and gravitational thermodynamics. The area law and its coefficient are imported. The relation between a microscopic CU accessibility measure and horizon entropy has not yet been derived.

The central bridge principle can be written:

> **[Bridge principle] Changes in the entropy assigned to a reduced causal description across every local horizon are thermodynamically related to the flux of stress-energy through that horizon.**

If this principle takes exactly the local-equilibrium, Clausius, and area-law form required by the established argument, Einstein-type dynamics follow conditionally. This formulation does not identify entropy with a conserved stock of inaccessible coherence.

## 9.8 Accessibility entropy

To make the bridge quantitative, one needs a functional

\[
S_{\mathrm{acc}}(\mathcal H;\rho)
\]

for the inaccessibility associated with a horizon or causal boundary \(\mathcal H\) in state \(\rho\).

A successful functional must answer at least four questions.

### What is being reduced?

The division into accessible and inaccessible degrees of freedom must be specified. In a quantum theory this may be a subsystem algebra, a causal wedge, or an effective factorization. In gravity such factorizations are subtle and may not be exact.

### Which entropy is used?

Von Neumann entropy, generalized entropy, relative entropy, and coarse-grained thermodynamic entropy are different quantities. The appropriate choice depends on the derivation.

### Why area scaling?

The functional must explain or inherit why the leading term scales as boundary area rather than bulk volume.

### How are divergences controlled?

Entanglement entropy across a continuum boundary is ordinarily ultraviolet divergent. A regulator, renormalization prescription, or finite microscopic theory is required (Srednicki, 1993; Eisert, Cramer, & Plenio, 2010).

The classical differentiation residual of Section 3 cannot supply these answers. It demonstrates how one coarse-graining hides distinctions in a finite simplex. It does not derive the Bekenstein–Hawking coefficient or continuum entanglement entropy.

## 9.9 The conditional field equation

Suppose the following are granted:

1. an effective Lorentzian continuum has emerged from the accessibility network;
2. the relevant local horizons admit the equilibrium construction required by the Raychaudhuri/Clausius argument;
3. every local causal horizon has an entropy
   \[
   S_{\mathrm{acc}}=\eta_A A;
   \]
4. energy flux is represented by a conserved stress-energy tensor;
5. the local temperature is the Unruh temperature;
6. the Clausius relation holds;
7. horizon focusing is governed by the usual geometric relation.

Then the Jacobson-style reasoning yields

\[
\boxed{
G_{\mu\nu}
+
\Lambda g_{\mu\nu}
=
\kappa_G T_{\mu\nu}.
}
\]

Matching observed general relativity requires

\[
\kappa_G=\frac{8\pi G}{c^4}.
\]

The derivation fixes the form of the equation only after the entropy-area coefficient and thermodynamic normalization are specified. CU does not presently derive the numerical value of \(G\) or explain why the area coefficient takes the required universal value.

The correct claim is therefore:

> **[Conditional result] Given an emergent Lorentzian geometry and the standard local horizon-thermodynamic assumptions, CU’s accessibility interpretation is compatible with an Einstein-type equation of state.**

It is not:

> Coherence alone derives Einstein’s equation.

## 9.10 Closing the backreaction loop

A complete gravitational model must join the state and geometry sectors.

Schematically:

\[
\text{state}
\longrightarrow
T_{\mu\nu}
\longrightarrow
g_{\mu\nu}
\longrightarrow
\text{state evolution}.
\]

Within the network picture:

\[
\rho
\longrightarrow
w[\rho]
\longrightarrow
g[w]
\longrightarrow
H[g]
\longrightarrow
\rho.
\]

Consistency requires:

- covariant conservation,
  \[
  \nabla^\mu T_{\mu\nu}=0;
  \]
- a well-defined continuum limit;
- a common effective metric for matter;
- causal propagation;
- stable initial-value evolution;
- and recovery of the tested weak-field and relativistic regimes.

A scalar coherence field can contribute one term to \(T_{\mu\nu}\), but ordinary matter, radiation, gauge fields, and quantum corrections must also be incorporated.

Until this loop is built, the geometry and matter sectors remain adjacent constructions rather than one derived theory.

## 9.11 Gravity as coherence redistribution

CU’s interpretive proposal is that curvature records how relational accessibility is reorganized by physical structure.

A concentration of energy-momentum changes the causal and metric relations among neighboring events. In the accessibility language, routes of influence, clock comparisons, and recoverable relations are deformed. Free bodies follow the resulting geometry because that geometry is the common organization of available propagation.

This motivates the phrase:

\[
\boxed{
\text{gravity as the macroscopic redistribution of accessibility}.
}
\]

The phrase can be useful if it is not mistaken for a completed equation.

It should not imply that masses consciously seek coherence, that curvature maximizes a moral quantity, or that all gravitational phenomena have already been recovered from a scalar gradient. It is an explanatory interpretation of the coupled geometry–matter structure that a full CU theory aims to derive.

## 9.12 Potential empirical consequences

At present, the conditional Einstein construction is designed to reproduce general relativity. Reproduction alone does not distinguish CU.

Distinctive empirical content could arise if the microscopic accessibility dynamics produce controlled corrections, for example:

- scale-dependent deviations from Einstein dynamics;
- additional scalar modes;
- modified gravitational-wave dispersion;
- equivalence-principle violations;
- altered horizon entropy;
- departures from standard semiclassical thermodynamics;
- or correlations between quantum recoverability and gravitational response.

These are examples, not predictions presently derived by the framework.

Each proposed correction must satisfy existing observational bounds and must follow from the microscopic model rather than be appended phenomenologically.

A null result is also informative. If every completed CU model reduces exactly to general relativity and standard quantum field theory without constraining parameters or producing new relations, CU may remain an interpretation rather than a distinct physical theory.

## 9.13 What would count as a derivation of gravity

A strong CU derivation would require the following chain:

1. define pre-geometric degrees of freedom without assuming a manifold;
2. derive a stable accessibility network;
3. obtain a low-dimensional Lorentzian continuum;
4. derive a universal matter metric;
5. define finite horizon accessibility entropy;
6. derive its area scaling and coefficient;
7. derive a local thermodynamic relation;
8. obtain the gravitational field equation;
9. recover tested general-relativistic solutions and perturbations;
10. identify at least one nontrivial consequence not inserted in the assumptions.

The present program reaches parts of steps 1–3 schematically, imports much of steps 4–8, and has not yet reached step 10.

That is not a reason to abandon the program. It is the reason to state its frontier accurately.

## 9.14 What Section 9 establishes

This section establishes that:

- an effective scalar field can carry the standard scalar stress-energy;
- geodesic motion can be interpreted in accessibility language once a metric is given;
- local horizon thermodynamics offers a conditional route to Einstein-type field equations;
- and accessibility provides a coherent interpretation of horizon entropy and geometric response.

It does not establish that gravity has been derived from CU’s foundational principles alone.

The strongest present conclusion is:

> **[Programmatic conclusion] CU supplies a common language for relational geometry, stress-energy, and horizon thermodynamics. A genuine gravitational theory requires the microscopic accessibility model, area law, coupling, and backreaction equations to be derived rather than imported.**

---

# 10. Horizons, Black Holes, and Limits of Accessibility

## 10.1 Why black holes matter to CU

Black holes bring nearly every foundational issue in this paper into one setting.

They join:

- causal structure;
- thermodynamic entropy;
- quantum field theory;
- coarse-graining;
- global versus local description;
- recoverability;
- geometric singularity;
- and the tension between reversible and irreversible dynamics.

For this reason, black holes are a natural test of CU’s distinction between structure and accessibility. They are also a place where interpretive language can easily outrun the physics.

The guiding intuition is straightforward:

> A horizon may prevent a restricted observer from accessing relational structure that remains present in a wider description.

That intuition is compatible with many information-preserving approaches. It does not by itself solve the black-hole information problem, determine the microscopic degrees of freedom, derive Hawking radiation, or decide among competing quantum-gravity proposals.

This section therefore treats black holes as a **stress test** of the framework, not as a completed application.

## 10.2 Horizons as causal access boundaries

In a classical asymptotically flat spacetime, an event horizon is the boundary of the region from which signals cannot reach future null infinity. It is defined globally by the causal structure of the spacetime.

Other horizons—apparent, trapping, Rindler, and cosmological horizons—have different definitions and should not be treated as interchangeable (Hayward, 1994).

The common CU interpretation is:

\[
\boxed{
\text{horizon}
=
\text{boundary of an effective domain of causal accessibility}.
}
\]

For an exterior observer, degrees of freedom behind a black-hole horizon are unavailable to direct causal intervention. The global spacetime description may nevertheless include them.

This is a scale- and observer-relative statement. It does not mean that the interior ceases to exist, nor that every observer shares the same partition. An infalling observer and a distant observer organize accessible observables differently.

The distinction resembles the general CU relation

\[
\text{global structure}
\neq
\text{locally accessible structure}.
\]

But a gravitational horizon is more than an ordinary information barrier. Its accessibility structure is encoded in the causal geometry itself. A full CU account must therefore derive both the boundary and the geometry supporting it.

## 10.3 Bekenstein–Hawking entropy

Semiclassical black-hole thermodynamics assigns the entropy

\[
\boxed{
S_{\mathrm{BH}}
=
\frac{k_Bc^3A}{4G\hbar}.
}
\]

This is the Bekenstein–Hawking entropy formula (Bekenstein, 1973; Hawking, 1975). The dependence on horizon area rather than interior volume is one of the central clues connecting gravity, quantum theory, and information.

CU may interpret \(S_{\mathrm{BH}}\) as measuring inaccessible state distinctions associated with the horizon. This is plausible at the level of interpretation:

- the horizon partitions an observer’s accessible algebra;
- degrees of freedom across the boundary may be entangled;
- the exterior description is reduced;
- and thermodynamic entropy is assigned to the black hole.

But the formula is not derived by the finite classical sandbox. The identity

\[
D_{\mathrm{fine}}
=
D_{\mathrm{coarse}}
+
D_{\mathrm{hidden}}
\]

shows only that a particular coarse-graining hides statistical differentiation. It does not explain:

- why black-hole entropy scales with area;
- why its coefficient is \(1/4\);
- which microscopic states are counted;
- why the result is universal;
- or how quantum and gravitational renormalization enter.

The phrase “hidden coherence equals black-hole entropy” would therefore be too strong.

A more accurate statement is:

> **[Interpretation] Black-hole entropy is a natural candidate for a quantitative measure of structure inaccessible to an exterior causal description. The microscopic identification remains open.**

## 10.4 The information problem: hidden is not yet preserved

The information paradox arises because semiclassical Hawking radiation is thermal at leading order in the semiclassical calculation (Hawking, 1975). If a pure collapsing state evolved into exactly thermal radiation with no correlations preserving the initial state, pure states would evolve into mixed states and ordinary unitary quantum evolution would fail.

CU begins with a useful conceptual distinction:

\[
\text{inaccessible information}
\neq
\text{destroyed information}.
\]

But making that distinction does not decide which side describes black-hole evaporation.

To show that information is hidden rather than destroyed, one needs a global dynamics and a recoverability result. One must identify where the information is encoded, how it is represented in the radiation or remaining degrees of freedom, and under what operations it could in principle be reconstructed.

Thus the CU language reframes the question:

\[
\boxed{
\text{Does the evaporation channel erase distinctions, or redistribute them into inaccessible correlations?}
}
\]

This is a precise and valuable question. Its answer must come from the physical channel, not from the framework’s preference for preservation.

## 10.5 Unitary evaporation and the Page curve

If black-hole formation and evaporation are globally unitary, then information initially inaccessible behind the horizon must eventually be encoded in correlations involving the outgoing radiation.

Page’s typical-state argument, assuming globally unitary evaporation and a suitable subsystem model, predicts that the radiation entropy first rises while the radiation remains strongly entangled with the remaining black hole and later falls as the radiation purifies (Page, 1993a, 1993b). The resulting qualitative behavior is represented by the Page curve.

In CU terms, this may be interpreted as a changing accessibility partition:

1. early in evaporation, much of the distinguishing structure is inaccessible to the radiation subsystem;
2. as evaporation proceeds, relational structure is redistributed;
3. after the Page time, sufficiently large radiation regions may contain increasing recoverable information about the initial state;
4. at complete unitary evaporation, the full radiation state is pure even though small subsystems may remain highly mixed.

This is a better use of the accessibility concept than simply declaring that information is never lost. It ties preservation to a measurable entropy and recovery structure.

A CU black-hole model should therefore seek to derive, not merely narrate:

\[
S_{\mathrm{rad}}(t)
\]

and a recovery map

\[
\mathcal R_t
\]

whose performance can be quantified.

## 10.6 Recoverability and error-correcting structure

In AdS/CFT code-subspace treatments, bulk information can be represented as redundantly encoded, with reconstruction possible from different boundary regions and protection against specified local erasures (Almheiri, Dong, & Harlow, 2015).

This suggests a natural CU formulation. Let \(\mathcal N\) represent the effective channel from a wider state to the exterior observables. Information is not destroyed if there exists a recovery map \(\mathcal R\) such that

\[
\mathcal R\circ\mathcal N
\]

approximately restores the relevant distinctions on a specified code subspace.

The key phrase is **on a specified subspace**. Recoverability is never absolute. It depends on:

- which states are allowed;
- which observables matter;
- which region is accessible;
- what operations are permitted;
- and what approximation error is tolerated.

This fits CU’s scale-relative accessibility but gives it operational content.

It also prevents a common overstatement. A globally unitary theory may preserve information while making practical recovery fantastically difficult. Ontological preservation and operational accessibility remain distinct.

## 10.7 Hawking radiation as redistribution: an interpretation

The phrase *coherence re-diffusion* captures one interpretation: distinctions concentrated behind a horizon may later become distributed across outgoing degrees of freedom.

Retained carefully, the interpretation can be written:

> **[Interpretation] In a unitary evaporation model, Hawking radiation participates in the redistribution of globally preserved relational information from black-hole degrees of freedom into correlations among radiation modes.**

The phrase should not imply that the Hawking spectrum, temperature, greybody factors, or Page curve have been derived from CU dynamics. Those remain imported unless an explicit microscopic model produces them.

Nor should “re-diffusion” suggest an ordinary local diffusion equation. The relevant encoding may be highly nonlocal and quantum.

## 10.8 Complementarity and the firewall problem

Black-hole complementarity proposes, roughly, that interior and exterior descriptions may both be valid within their operational domains without being combined into one observer-accessible description in a way that duplicates information (Susskind, Thorlacius, & Uglum, 1993).

CU is naturally sympathetic to this structure because it rejects a single scale-independent view in which all relational information is simultaneously accessible.

An infalling observer may use a description smooth across the horizon. A distant observer may use an exterior description in which information is encoded in horizon or radiation degrees of freedom. The descriptions need not be jointly realizable as one operational perspective.

However, this does not automatically dissolve the firewall problem.

The AMPS firewall argument identifies an incompatibility among three assumptions:

- globally unitary evaporation, so the complete Hawking radiation is pure;
- validity of low-energy effective field theory outside the stretched horizon;
- and “no drama” for an infalling observer at the horizon.

Entanglement monogamy, equivalently the relevant strong-subadditivity constraint, supplies the contradiction mechanism rather than a fourth independent physical premise (Almheiri, Marolf, Polchinski, & Sully, 2013).

Saying that observers have different access does not by itself show that the relevant global quantum state satisfies all consistency conditions. CU must still specify the state assignments, algebras, and reconstruction maps.

The responsible conclusion is:

> **[Interpretive contribution] Scale-relative accessibility provides a natural language for complementarity, but resolving the firewall paradox requires a concrete quantum-gravitational model.**

## 10.9 Singularities as limits of effective description

Classical general relativity predicts geodesic incompleteness under broad conditions associated with gravitational collapse and cosmology (Penrose, 1965; Hawking & Penrose, 1970). Curvature quantities may diverge in familiar solutions, but geodesic incompleteness—not curvature divergence in every case—is the theorem-level conclusion.

CU may interpret a singularity as a boundary at which the emergent spacetime description ceases to organize the underlying relational structure adequately.

This is preferable to treating a coordinate divergence as a physical object. But it remains an interpretation.

The statement

\[
\text{singularity}
=
\text{pure structure}
\]

is not presently derived. A quantum-gravity completion might replace the singularity with a bounce, a transition, a non-geometric phase, a boundary condition, or something else entirely.

The defensible CU statement is:

> **[Hypothesis] At regimes where continuum geometry fails, the appropriate description may return to pre-geometric relational degrees of freedom and accessibility constraints.**

This says where to look, not what will be found.

## 10.10 The “three faces of pure structure”

A broader foundational hypothesis proposes a convergence among:

- the earliest cosmological regime;
- the deep interior or endpoint of gravitational collapse;
- and the sub-quantum or ultraviolet limit

may all approach a boundary where familiar spacetime description gives way to pre-geometric relational structure.

This idea can be retained as a metaphysical and research-guiding hypothesis, provided it is not called a demonstrated prediction.

Its attraction is clear. In all three directions, standard descriptive categories appear strained:

\[
\text{time origin},
\qquad
\text{gravitational singularity},
\qquad
\text{ultraviolet completion}.
\]

CU suggests that these may not be independent failures. They may indicate a common limit of accessibility at which geometry, separability, and familiar state descriptions cease to apply.

But the similarity may also be superficial. Different physical limits can require different theories.

The appropriate status is:

> **[Foundational hypothesis] Cosmological, gravitational, and ultraviolet breakdowns of spacetime may be different approaches to a common pre-geometric relational regime.**

Testing this would require one mathematical model connecting the regimes, not merely analogous language.

## 10.11 A concrete black-hole research program

A CU contribution to horizon physics should proceed through explicit models.

### Stage 1: finite quantum systems

Construct a finite-dimensional model with:

- a dynamically changing accessible/inaccessible partition;
- globally unitary evolution;
- a radiation subsystem;
- an explicit recovery task;
- and computable entropies and mutual informations.

The goal is to reproduce a Page-like transfer of recoverability without claiming that the model is a black hole.

### Stage 2: network geometry

Couple the information-transfer model to an accessibility network whose effective distances and causal relations change with the state.

The goal is to represent a horizon as a dynamical access boundary rather than an externally imposed subsystem cut.

### Stage 3: semiclassical matching

Show that an appropriate continuum limit reproduces:

- horizon temperature;
- area-law entropy;
- causal trapping;
- and semiclassical flux.

### Stage 4: quantum-gravitational distinction

Identify where the model differs from standard semiclassical evolution and whether the difference resolves, reproduces, or worsens the information problem.

Potential observables include:

- radiation entropy;
- mutual information between early and late radiation;
- recovery fidelity;
- scrambling time;
- horizon-area evolution;
- and deviations from thermality.

## 10.12 What would falsify the horizon interpretation

The accessibility interpretation would lose force if:

- a completed microscopic model required literal information destruction;
- horizon entropy could not be related to any restriction or relational encoding;
- the same accessibility formalism failed to distinguish ordinary coarse-graining from causal horizons;
- or the framework generated no quantitative result beyond relabeling established quantities.

Conversely, support would come from a model in which:

- geometry and access boundary co-emerge;
- unitary dynamics produce the expected entropy curve;
- recoverability changes in a calculable way;
- and the horizon entropy follows from the same microscopic structure that generates geometry.

## 10.13 What Section 10 establishes

This section establishes no new theorem about black holes.

It shows that CU’s central distinction between global structure and local accessibility is directly relevant to horizon physics. It clarifies how the framework may organize questions about entropy, unitarity, complementarity, and recovery.

Its strongest conclusion is conditional:

> **If black-hole evolution is globally unitary, CU provides a natural language for understanding local thermalization as restricted access to relational information preserved in a wider quantum state.**

The information paradox is not solved by that language alone. The mechanism, state space, geometry, and recovery dynamics remain to be derived.

---

# 11. The Unified Dynamical Architecture

## 11.1 One framework does not require one equation

A unified framework need not compress every level of reality into one differential equation.

Indeed, forcing one equation to perform every explanatory role can create confusion. A pre-temporal relation among possible configurations is not the same object as a Hamiltonian evolution parameterized by time. A closed-system variational law is not the same as an open-system relaxation equation. A reduced coarse-grained description is not the same as the global dynamics from which it is obtained.

CU is better understood as a **family of related structures organized by explanatory level**.

At minimum, the Physics program contains:

1. a pre-temporal relation of admissible transitions;
2. an order structure from which temporal parameterization may arise;
3. a reversible Hamiltonian dynamics for closed or weakly coupled systems;
4. a dissipative first-order flow for strongly coupled systems;
5. a reduced accessibility dynamics for coarse-grained descriptions;
6. and domain-specific coherence functionals defined relative to actual constraints.

These layers should be connected, but not identified.

The unifying claim is architectural:

> Across levels, persistence depends on constraint-sensitive organization, while effective descriptions differ according to what structure is dynamically available and what is inaccessible.

## 11.2 The principle-level Universal Flow

At its most general, the Universal Flow principle is not yet an equation.

> **[Bridge principle] A system that persists under changing conditions must alter its organization in ways that preserve, restore, or transform the relations relevant to its continued identity, subject to the degrees of freedom and constraints actually available.**

This principle is intentionally domain-general.

For a physical structure, identity may mean persistence of a stable mode or conserved organization. For an organism, it includes active viability. For a mind, it includes temporal and representational integration. For a social system, it may include coordinated functions and justificatory integrity.

The principle does not imply that every system improves, that the universe maximizes one scalar, or that every transition increases substantive coherence. Systems can fail, fragment, become trapped in local attractors, or preserve themselves by exporting damage to other scales.

To become mathematical, the principle requires:

- a state space \(\mathcal X\);
- a geometry \(g\);
- a set of admissible states and transformations;
- relevant constraints \(K\);
- an identity or viability criterion;
- a coherence or cost functional;
- environmental coupling;
- and, where dynamics is temporal, a time parameter.

Different choices produce different equations.

## 11.3 Pre-temporal admissibility

Before time is available, the most primitive dynamical structure is a relation

\[
x\rightsquigarrow y
\]

meaning that \(y\) is an admissible continuation, completion, or transformation of \(x\) under the operative structural rules.

This relation may be:

- deterministic or branching;
- reversible or irreversible;
- total or partial;
- and local or nonlocal in whatever relational structure is available.

It does not yet describe velocity or duration. It specifies possibility under constraint.

Once admissible transitions form consistent chains or partial orders, they may be parameterized temporally as described in Section 4.

This is the first connection between the logical and physical sides of CU:

\[
\boxed{
\text{constraint does not first act in time;}
\quad
\text{constraint first limits possible continuation.}
}
\]

Time becomes the organization of such continuation, not an external container into which it is placed.

## 11.4 The Hamiltonian form

After a temporal parameter and suitable configuration space are available, the proposed closed-system physical form is

\[
\boxed{
\frac{D\dot q}{dt}
=
-\operatorname{grad}_g V(q).
}
\]

Here \(q\) denotes the relevant configuration variables, \(g\) the state-space metric, and \(V\) the selected potential.

In coordinates,

\[
\ddot q^i
+
\Gamma^i{}_{jk}\dot q^j\dot q^k
=
-g^{ij}\partial_jV.
\]

The corresponding Lagrangian is

\[
L(q,\dot q)
=
\frac12g_{ij}(q)\dot q^i\dot q^j
-
V(q).
\]

This form provides:

- configuration and velocity;
- inertial persistence;
- oscillation;
- normal modes;
- reversible evolution;
- variational structure;
- and, under time-translation symmetry, conserved energy.

It is the proposed **dynamical foundation** of the physical theory. It is not logically prior to the relational and order-theoretic structures needed to define its variables and time parameter.

The potential is not a decorative term. It determines the physics. A gradient-penalty potential may yield waves; a Fisher-information term in a density–phase action may yield Schrödinger dynamics; another potential could yield entirely different behavior.

Therefore:

\[
\text{common variational form}
\neq
\text{unique physical law}.
\]

A major open task is to derive or constrain the physically realized potentials.

## 11.5 Environmental coupling and the first-order limit

For an open system, introduce damping and noise:

\[
\boxed{
\frac{D\dot q}{dt}
+
\eta\dot q
=
-\operatorname{grad}_gV(q)
+
\xi(t).
}
\]

When momentum-like degrees of freedom relax rapidly relative to the configuration, the leading slow dynamics is

\[
\boxed{
\dot q
\approx
-\frac1\eta\operatorname{grad}_gV(q)
+
\frac1\eta\xi(t).
}
\]

This is the relation between the second-order and first-order forms.

The first-order equation is not an inferior approximation in every context. It may be exactly the useful description at the scale of interest. Biological adaptation, learning, diffusion, and relaxation often take first-order effective forms.

The important point is explanatory:

> The first-order state-only dynamics can arise because environmental coupling has made velocity or phase information inaccessible on the timescale being modeled.

This gives damping a CU interpretation. Environmental interaction does not merely add friction; it changes which aspects of the full dynamical state remain available to the reduced description.

## 11.6 Coarse-grained accessibility dynamics

Even after an effective first-order law is obtained, a further distinction remains between the global state and the state accessible to a subsystem or scale.

Let

\[
\mathcal C:\rho\mapsto\bar\rho
\]

be a coarse-graining channel or map.

The reduced dynamics may fail to be invertible even if the global dynamics is reversible. Distinct global states can produce the same reduced state:

\[
\rho_1\neq\rho_2,
\qquad
\mathcal C(\rho_1)=\mathcal C(\rho_2).
\]

This is the formal basis of effective irrecoverability.

The finite classical theorem of Section 3 supplies one exact local model. For a partition \(\pi\), the block-uniform conditional expectation \(E_\pi\) satisfies

\[
D_N(p)-D_N(E_\pi p)
=
\sum_b\sum_{i\in B_b}
\left(p_i-\frac{q_b}{m_b}\right)^2,
\]

while

\[
S(E_\pi p)-S(p)
=
\sum_bq_b\operatorname{KL}
\left(r^{(b)}\middle\|\nu_{m_b}\right).
\]

Thus one averaging operation contracts fine differentiation and raises Shannon entropy, with the same equality set. This is a precise distinction–entropy tradeoff, not a universal conservation or conversion law for substantive coherence.

One should not assume that an arbitrary reduced dynamics is automatically this averaging map or a gradient flow. Depending on the system and approximation, it may be:

- Markovian or non-Markovian;
- deterministic or stochastic;
- completely positive or not well approximated by a closed quantum channel;
- memoryless or history-dependent.

The correct reduced law must be derived from the global dynamics and the access restriction.

CU’s general claim is not that all coarse-grained dynamics share one equation. It is that loss of access to relational distinctions is a central structural fact that any effective dynamics must represent, and that entropy must be specified according to the actual reduction rather than identified with “hidden coherence” by definition.

## 11.7 Three organizing constraints

Three broad organizing ideas are best treated as constraints on acceptable physical models rather than as universal laws.[^laws-history]

### Constraint 1: no unaccounted structure creation

If a reduced description appears to gain or lose structure, the wider accounting should identify:

- transfer across a boundary;
- environmental coupling;
- coarse-graining;
- measurement;
- work or energy input;
- or a genuine nonconservation law.

This is not a universal theorem that every coherence measure is conserved. Different resources can be created or destroyed under different operations. It is a demand for explicit accounting.

A local increase may be paid for by:

- increased environmental entropy;
- loss of structure elsewhere;
- consumption of free energy;
- or conversion from another resource.

### Constraint 2: variation and constraint are jointly required for adaptive organization

A system with no variation cannot explore alternatives. A system with no stabilizing constraint cannot preserve successful organization.

This motivates a general Goldilocks intuition:

\[
\text{too rigid}
\longleftrightarrow
\text{adaptively impoverished},
\]

\[
\text{too unconstrained}
\longleftrightarrow
\text{unable to retain organization}.
\]

The statement is domain-sensitive. It does not imply one universal numerical entropy band.

### Constraint 3: dynamics must preserve admissibility

An update must remain within the actual state space and obey its physical constraints.

Examples include:

- normalization and positivity of probabilities;
- positivity and unit trace of density operators;
- conservation laws;
- causal structure;
- gauge constraints;
- and viability bounds in biological models.

Natural gradients are one way to respect the geometry of admissible states, but they do not by themselves ensure every physical requirement.

These three constraints—accounting, adaptive balance, and admissibility—form a useful test for any proposed CU dynamics.

## 11.8 The potentiometer as a local diagnostic

For two candidate tendencies \(A\) and \(B\) on a Riemannian state space, define their signed alignment

\[
\mathcal A_g
=
\langle A,B\rangle_g.
\]

When \(A=\operatorname{grad}_g C\) and \(B=\operatorname{grad}_g S\), one may define an opposition quantity

\[
\Pi_g
=
-\mathcal A_g
=
-\langle A,B\rangle_g.
\]

The quantity is local. It answers:

> At this state, under this metric and these functionals, how strongly do the two vector fields support or oppose one another?

It does not by itself diagnose global development, long-term stability, or substantive coherence.

In the classical sandbox,

\[
\Pi_E=2J(p,u)\geq0
\]

because the differentiation and entropy gradients oppose one another.

For a combined flow

\[
\dot x=\alpha A+\beta B,
\]

the relevant coherence or differentiation rate is

\[
\frac{dC}{dt}
=
\alpha\|A\|_g^2
-
\beta\Pi_g.
\]

A large \(\Pi_g\) means strong opposition. Whether the net rate is positive depends on the full balance.

This corrects the earlier interpretation in which a positive potentiometer was sometimes described as “alignment.”

## 11.9 Local and global coherence

A structure can be coherent at one scale while undermining coherence at another.

A crystal is highly ordered locally and globally but not adaptively flexible. A tumor can maintain strong internal coordination while damaging the organism that sustains it. An institution can preserve its procedures while degrading the social field on which its legitimacy depends.

Therefore substantive coherence should not be evaluated by one local score alone.

Schematically, for scales \(s\),

\[
C_{\mathrm{multi}}
=
\mathcal F\left(
\{C_s\},
\{\text{cross-scale couplings}\},
\{\text{externalized costs}\}
\right).
\]

No universal \(\mathcal F\) has yet been derived.

The local–global principle is best stated as a constraint:

> **[Bridge principle] A configuration should not be counted as globally coherent merely because it stabilizes one subsystem while systematically degrading the wider conditions of its persistence.**

In physics this guards against identifying concentration with coherence. In biology it distinguishes self-maintenance from uncontrolled replication. In ethics it helps distinguish local optimization from justified action.

The same principle connects the Physics paper to the broader CU framework without pretending that one mathematical functional already spans all domains.

## 11.10 The Coherence–Entropy Double Helix

The Double Helix names a recurring developmental pattern:

\[
\text{variation or opening}
\rightarrow
\text{selection and integration}
\rightarrow
\text{renewed opening}.
\]

In thermodynamic language, one may see phases in which accessible possibilities broaden, followed by phases in which some possibilities are stabilized into organized structure.

The classical autonomous flow

\[
\dot p
=
\operatorname{grad}_F(\alpha D+\beta S)
\]

does not produce a sustained cycle with fixed parameters. It is a gradient flow of one scalar objective.

A genuine recurring helix requires additional structure, such as:

- second-order inertia;
- time-dependent constraints;
- environmental forcing;
- delayed feedback;
- changing parameters;
- multiple coupled subsystems;
- or continual energy throughput.

The Double Helix should therefore be treated as:

> **[Developmental hypothesis] Open, driven, multiscale systems may repeatedly alternate between variability-generating and structure-consolidating regimes.**

This hypothesis is plausible in biological, psychological, and social systems. It must be demonstrated model by model.

The second-order dynamics developed in Section 7 gives one route to oscillation. Open-system driving gives another. Neither guarantees that the resulting cycle is beneficial or globally coherent.

## 11.11 Coherence drive without teleology

CU often speaks of a coherence drive. At the physical level this should not be understood as desire or cosmic purpose.

The minimal claim is selective:

- configurations unable to preserve the relations constituting them cease to persist;
- configurations whose dynamics repeatedly restore those relations remain available for further evolution;
- over time, persistent populations become enriched for coherence-preserving organization.

This can create an appearance of directedness without introducing intention.

In a dynamical system, attractors collect trajectories. In evolution, selection retains viable forms. In learning, updates stabilize successful policies. These mechanisms differ, but each can produce an asymmetry favoring persistence.

The term “drive” is therefore shorthand for a family of persistence-selection effects.

It does not imply:

\[
\frac{dC_{\mathrm{universe}}}{dt}>0
\]

for one known universal scalar. No such theorem has been established.

## 11.12 The foundational-substrate interpretation

The companion Foundational Substrate paper proposes a stronger metaphysical reading:

> The coherence field is the structure of physical possibility itself, and actuality is the realization of particular configurations through coherence dynamics.

The present Physics paper can accommodate that reading, but should not present it as a consequence of the mathematical embeddings alone.

The mathematics supplies:

- spaces of possible configurations;
- geometric relations among them;
- variational dynamics;
- damping and reduced access;
- and conditional realizations of familiar equations.

The metaphysical interpretation adds:

- that possibility space is ontologically fundamental;
- that the universe is process rather than inventory;
- and that mind and matter are two aspects of coherence realization.

This interpretation may unify the framework philosophically. It remains underdetermined by the formalism. Other ontologies may use the same mathematics.

The proper relation is:

\[
\boxed{
\text{formal architecture}
\quad\text{supports but does not uniquely entail}\quad
\text{foundational-substrate reading}.
}
\]

## 11.13 The architecture in one table

| Level | Mathematical object | Physical role | Present status |
|---|---|---|---|
| Pure relational possibility | Set/category/relational structure not yet fixed | Conditions for distinction | Philosophical primitive/open formalization |
| Admissible continuation | Relation \(x\rightsquigarrow y\) | Constraint on possible change | Bridge structure |
| Temporal order | Partial order and clock maps | Before/after and duration | Conditional construction |
| Closed dynamics | Hamiltonian/Lagrangian flow | Reversible evolution | Proposed foundational form |
| Open dynamics | Damped/stochastic equation | Relaxation under environment | Derived in controlled limits |
| Reduced description | Channel/coarse-graining | Restricted accessibility | Standard mathematical structure |
| Classical sandbox | Probability simplex | Differentiation and entropy | Derived toy results |
| Quantum realization | Density operators and channels | Purification, entanglement, recovery | Conditional reconstruction/established quantum theory |
| Relational geometry | Accessibility network and metric closure | Effective distance and locality | Exact construction, physical hypothesis |
| Gravity | Coupled geometry and stress-energy | Dynamical spacetime | Conditional thermodynamic route |
| Substantive coherence | \(C_{\mathrm{sub}}(x;K,G,\pi,T)\) | Constraint-grounded integration | Open central problem |

The table makes clear why the paper cannot be reduced to the sentence “everything follows from the Universal Flow Equation.” There is no single displayed equation from which every row has been derived.

What unifies them is a pattern of constraints, access relations, and transitions among descriptions.

## 11.14 Synthesis

The unified architecture can be written schematically:

\[
\boxed{
\begin{aligned}
&\text{relational possibility}\\
&\downarrow\\
&\text{distinguishable configurations}\\
&\downarrow\\
&\text{admissible transitions}\\
&\downarrow\\
&\text{ordered histories and clocks}\\
&\downarrow\\
&\text{reversible variational dynamics}\\
&\downarrow\\
&\text{environmental damping and coarse-graining}\\
&\downarrow\\
&\text{effective probability and quantum descriptions}\\
&\downarrow\\
&\text{stable accessibility networks}\\
&\downarrow\\
&\text{effective geometry and conditional gravity}.
\end{aligned}
}
\]

The arrows are not all deductions of the same kind. Some are logical enablements, some mathematical constructions, some physical bridge principles, and some open hypotheses.

The value of the architecture is not that it eliminates those differences. It makes them visible.

CU’s physical program is strongest when stated this way:

> Reality may admit a layered description in which relational structure, constrained possibility, temporal order, reversible dynamics, environmental restriction, quantum accessibility, and effective geometry are not separate foundations but successive forms of one organizational problem.

Whether this architecture is nature’s architecture remains an empirical and mathematical question.

---

# 12. Research Program, Verification, and Falsifiability

## 12.1 Why explicit status is part of the method

A framework that moves across metaphysics, information geometry, quantum theory, spacetime, and gravity faces a special risk. The same vocabulary can make very different achievements sound alike.

A definition can sound like a discovery. A mathematical embedding can sound like a derivation of nature. A conditional reconstruction can sound unconditional. An interpretation can sound like an empirical result.

CU should treat the separation of these statuses as part of its epistemic discipline.

The question is not whether the framework is already complete. It is whether:

- its assumptions are visible;
- its internal derivations are valid;
- imported results are accurately represented;
- conjectures are distinguishable from theorems;
- failure conditions are specified;
- and new empirical consequences can eventually be produced.

Incompleteness is acceptable. Concealed incompleteness is not.

The research program developed here is therefore organized around **successively stronger burdens of proof**.

## 12.2 Status of the principal claims

The paper contains four different kinds of result.

| Layer | Principal content | Present status |
|---|---|---|
| Exact mathematics | Differentiation and entropy gradients; block-averaging identities; wedge degeneracy; Fisher-field bounds; pure-state coherence-to-entanglement conversion; phase-space rewrite | Derived under the stated finite-dimensional models |
| Imported physical mathematics | Quantum purification; contextuality results; scalar-field stress-energy; causal reconstruction; local-horizon thermodynamics | Established in the cited form, with the assumptions stated locally |
| Conditional reconstruction | Quantum state-space route; Madelung/Schrödinger embedding; accessibility-to-geometry program; Jacobson-style gravity route | Valid only when the additional operational, regularity, or thermodynamic premises are granted |
| Physical and metaphysical proposals | A substantive coherence functional; fundamental second-order dynamics; emergent geometry; the coherence field as structured possibility | Hypotheses, open problems, or interpretations rather than established laws |

Several negative results are equally important. The four-state differentiation functional is not a universal measure of physical coherence. Conditional entropy is not hidden differentiation. Hidden classical correlation does not force quantum theory. A selected potential that reproduces a familiar equation does not explain why nature selects that potential. A correlation-derived network does not automatically constitute physical space. Horizon accessibility language does not by itself solve the black-hole information problem.

The complete row-by-row claim ledger, including rejected and superseded statements, appears in the technical supplement. That ledger should be updated whenever the mathematics or evidence changes.

## 12.3 Foundational formalization

The most important unresolved problem is not quantum gravity. It is the definition of substantive coherence.

The present paper uses the schematic form

\[
C_{\mathrm{sub}}
=
C(x;K,G,\pi,T),
\]

where:

- \(x\) is a state or trajectory;
- \(K\) is the relevant constraint set;
- \(G\) is relational organization;
- \(\pi\) is scale or coarse-graining;
- \(T\) is temporal horizon.

This notation names the dependencies but does not yet specify the functional.

A successful physical definition should distinguish:

- integrated from merely concentrated states;
- stable from metastable states;
- self-supporting from environmentally subsidized organization;
- local from global coherence;
- robustness from rigidity;
- and short-term persistence from long-horizon viability.

It should also admit empirical estimation or model calculation.

### 12.3.1 Candidate mathematical ingredients

Possible ingredients include:

- constraint satisfaction;
- multivariate dependence;
- integrated information measures;
- dynamical stability;
- recoverability;
- predictive persistence;
- controllability and observability;
- robustness to perturbation;
- cross-scale mutual constraint;
- and thermodynamic cost.

No single ingredient is sufficient.

A functional that rewards only correlation may score rigid or pathological states highly. A functional that rewards only stability may prefer inert states. A functional that rewards only prediction may ignore viability. A functional that rewards only local constraint satisfaction may conceal exported damage.

The research task is not to choose an intuitively attractive weighted sum. It is to derive constraints that any adequate measure must satisfy.

### 12.3.2 Axioms for a substantive coherence measure

A candidate \(C_{\mathrm{sub}}\) might be required to satisfy some combination of:

1. **Relational sensitivity:** it changes when integration among components changes.
2. **Constraint relativity:** it is defined relative to stated persistence or viability conditions.
3. **Scale transparency:** the chosen coarse-graining is explicit.
4. **Nontriviality:** concentration alone does not maximize it.
5. **Robustness sensitivity:** it distinguishes fragile from perturbation-resistant organization.
6. **Cross-scale accounting:** local gains that destroy enabling global conditions are penalized or separately reported.
7. **Operational accessibility:** its relevant terms can in principle be estimated or bounded.
8. **Transformation behavior:** its monotonicity or conversion laws under allowed operations are specified.
9. **Temporal adequacy:** it can evaluate trajectories, not only instantaneous states.
10. **Domain portability:** domain-specific forms share structural constraints without pretending to be numerically identical.

These are proposed design requirements, not yet a theorem of uniqueness.

## 12.4 Mathematical program for the classical and Fisher sectors

The classical sandbox should be consolidated around a small number of exact results and then extended deliberately.

Priority tasks are:

1. generalize the differentiation decomposition from the \(N=4\) two-block example to arbitrary partitions;
2. characterize joint-growth regions for \(D\) and \(S\) in higher dimensions;
3. derive exact Fisher-gradient opposition formulas where possible;
4. study continuous and discrete stability separately;
5. classify fixed points of
   \[
   \dot p=\alpha\,\operatorname{grad}_F D+\beta\,\operatorname{grad}_F S;
   \]
6. determine which driven or second-order extensions can exhibit repeated opening–consolidation cycles;
7. compare Euclidean and Fisher flows numerically without conflating their vector fields;
8. derive coarse-grained effective equations from a reversible parent dynamics;
9. make all code, parameters, and initial conditions reproducible.

This work is mathematically modest compared with quantum gravity, but foundationally important. Errors at this level propagate through every later section.

## 12.5 Quantum research program

The quantum program has four distinct tasks.

### State-space reconstruction

Clarify whether CU independently motivates each operational axiom required by the selected reconstruction theorem.

The goal is not to rename established axioms. It is to show why they follow from CU’s lower-level commitments or to admit that they are additional postulates.

### Resource structure

Develop a coherent quantum profile separating:

\[
P_{\mathrm{ex}},
\qquad
C_r^B,
\qquad
I(A:B),
\qquad
E,
\qquad
R_{\mathrm{rec}}.
\]

Study conversion and trade-off relations among these quantities under specified operation classes.

### Dynamical admissibility

Determine when a proposed information-geometric flow defines a physically admissible quantum evolution.

Questions include:

- positivity;
- complete positivity;
- trace preservation;
- linearity or justified nonlinearity;
- no-signalling;
- extension to composite systems;
- and compatibility with unitary dilation.

### Beyond nonrelativistic scalar quantum mechanics

Extend the density–phase variational program to:

- spin;
- fermionic statistics;
- gauge fields;
- relativistic fields;
- particle creation;
- and interacting many-body systems.

The relation between the operational reconstruction and the Hamiltonian/Fisher derivation should be made explicit. One selects a state-space architecture; the other realizes a dynamics. A complete theory needs both.

## 12.6 Geometry and gravity research program

The geometry program should proceed in stages.

### Stage G1: non-geometric networks

Construct state-dependent accessibility networks without background coordinates.

Success criterion:

\[
\text{stable low-dimensional locality emerges over a scale range}.
\]

### Stage G2: causal structure

Define directed influence and test for:

- acyclicity or controlled causal loops;
- finite propagation;
- stable cones;
- and compatibility with the symmetric distance structure.

### Stage G3: continuum and dimension

Demonstrate convergence of:

- volume growth;
- spectral dimension;
- graph Laplacian;
- curvature;
- and propagation.

### Stage G4: universal matter geometry

Show that different low-energy excitations experience one effective metric.

### Stage G5: dynamical backreaction

Derive coupled state-network equations and recover weak-field gravity.

### Stage G6: horizon thermodynamics

Obtain an entropy-area relation and local thermodynamic consistency from the microscopic model.

### Stage G7: Einstein limit and corrections

Recover general relativity and derive any deviations.

At every stage, null models are essential. A graph generated from an already geometric interaction rule is not evidence of emergence.

## 12.7 Horizon and black-hole program

The black-hole application should begin only after a dynamical geometry exists.

Intermediate models can nevertheless test the information architecture:

- unitary channels with changing subsystem access;
- Page-like entropy curves;
- scrambling and recovery;
- redundant encoding;
- observer-relative algebras;
- and complementarity constraints.

A genuine CU black-hole result would join those information-theoretic features to a horizon produced by the same relational dynamics that generate geometry.

The minimum target is:

\[
\boxed{
\text{one model in which horizon geometry, entropy, and recoverability arise together}.
}
\]

Without this joint derivation, the black-hole discussion remains interpretive.

## 12.8 Empirical distinguishing power

A physical framework becomes more than interpretation when it constrains observation in a way not already guaranteed by the theories it reorganizes.

Possible routes include:

### Parameter relations

A common microscopic model may relate constants or coefficients that standard effective theories treat independently.

### Forbidden regimes

The coherence architecture may rule out classes of state spaces, interactions, or dimensions.

### Scaling laws

A substantive coherence measure may predict a distinctive relation among integration, recoverability, and stability.

### Controlled deviations

Emergent geometry or open quantum dynamics may produce small departures from standard theory in a calculable regime.

### Cross-domain correspondence

The same dimensionless structural quantity may appear independently in physical, biological, and cognitive systems. Such a claim would require carefully defined observables and cannot rest on metaphor.

At present, these are research possibilities.

The paper should resist presenting compatibility with known physics as confirmation. A framework flexible enough to reproduce many equations by selecting different potentials may be mathematically expressive without being empirically restrictive.

## 12.9 Falsifiability and narrowing conditions

Failure need not force rejection of every philosophical claim at once. Different levels can fail independently.

### F1. Failure of substantive operationalization

If no nontrivial, measurable, constraint-grounded coherence functional can be produced, the physical use of “coherence” should be narrowed to an interpretive vocabulary.

### F2. Failure of the quantum bridge

If purification and contextual accessibility cannot be connected to CU except by importing the full quantum structure, the claim of reconstructive explanation should be withdrawn.

### F3. Failure of physical admissibility

If the proposed natural-gradient quantum flows violate positivity, complete positivity, compositional consistency, or observed no-signalling, they cannot serve as fundamental physical laws.

### F4. Failure of potential selection

If every known equation can be reproduced only by choosing its corresponding potential by hand, with no principle constraining the choice, the Hamiltonian framework is an embedding language rather than a unification.

### F5. Failure of emergent geometry

If broad classes of non-geometric accessibility models fail to produce stable local continuum regimes, the spacetime emergence claim should be abandoned or sharply restricted.

### F6. Failure of universal coupling

If the model cannot recover a common effective metric for matter, it fails as a general-relativistic completion.

### F7. Failure of horizon accounting

If horizon entropy and information recovery cannot arise from the same microscopic architecture, the black-hole interpretation remains incomplete.

### F8. Empirical exclusion

If a completed model predicts deviations already ruled out by experiment or observation, that model is false.

### F9. No novel consequence

If CU indefinitely reproduces known mathematics without parameter constraints, new predictions, or explanatory compression beyond relabeling, its status should remain philosophical synthesis rather than new physical theory.

These conditions make the program risky in the productive sense: they identify what would force revision.

## 12.10 Current verification boundary

The classical and Fisher calculations, finite-partition theorem, two-level wedge theorem, Fisher-field extrema, fixed-coupling stationary analysis, and overdamped asymptotics have been checked analytically and reproduced computationally. The lattice-wave and Madelung calculations have deterministic reference implementations, and the independent audit confirmed the central four-state results while identifying the initialization dependence of the original overdamped diagnostic.

The verification does not establish the physical hypotheses of the paper. In particular, the relational-geometry program, complete Madelung global analysis, horizon construction, gravity completion, and bibliography still require specialist review beyond the internal and model-based checks reported here. Numerical agreement supports a stated computation; it does not replace a proof when a proof is available, and neither proof nor simulation establishes that the model describes nature without an empirical bridge.

The technical supplement preserves the full audit sequence, independent responses, exact numerical definitions, source code, software environment, and machine-readable results.

## 12.11 Reproducibility standards

Any numerical claim in the publication version should include:

- source code;
- software environment;
- random seeds;
- initial conditions;
- parameter ranges;
- convergence tests;
- error metrics;
- and the raw or regenerable data.

Figures should distinguish:

- analytic curves;
- numerical simulation;
- conceptual diagrams;
- and illustrative schematics.

A conceptual figure should never be described as numerical evidence.

For formal proofs, notation should remain canonical across sections. In particular:

\[
D
\]

should denote statistical differentiation in the classical sandbox,

\[
\Pi_E
\]

the Euclidean opposition quantity,

\[
\Pi_F
\]

the Fisher opposition quantity, and domain-specific substantive coherence should use an explicit label rather than silently reusing \(D\).

## 12.12 Versioning and collaborative development

CU presents itself as a living framework. That commitment should be reflected in the publication process.

Each public version should include:

- a version number and date;
- a change log;
- a list of superseded claims;
- a record of corrected proofs;
- and links to archived prior versions.

Substantial external criticisms should be documented, not erased. Where a correction changes the conceptual meaning of a result—as with the differentiation/coherence distinction—the history should remain visible.

This approach is especially appropriate for a framework whose central ethical and epistemic commitments include corrigibility, non-dogmatism, and collaborative construction.

## 12.13 A minimum viable physical theory

Before CU should be presented as a distinct foundational physical theory, it should satisfy at least five conditions.

1. **A physical state ontology or operational state definition.**
2. **A substantive coherence functional or tightly constrained family of functionals.**
3. **A law selecting admissible dynamics and potentials.**
4. **A derivation of an observed regime not obtained by inserting that regime’s mathematics.**
5. **A novel empirical consequence or nontrivial explanatory constraint.**

Until then, CU Physics is best described as a structured research program and unifying architecture.

This status is not dismissive. Research programs often precede completed theories. The point is to state what kind of achievement has been reached.

## 12.14 Recommended order of work

The immediate order should be:

1. stabilize the classical and Fisher mathematics;
2. define axioms for substantive coherence;
3. verify and refine the quantum reconstruction;
4. prove physical admissibility of any proposed quantum flow;
5. rederive the Hamiltonian and density–phase sectors cleanly;
6. build one non-geometric accessibility-network model;
7. test for dimension, locality, and causal cones;
8. couple the network to state dynamics;
9. derive or reject a horizon entropy law;
10. seek an Einstein limit;
11. identify a novel observable consequence.

This order mirrors the Coherence Ladder’s methodological lesson:

> Do not depend on a higher-level result before the structure enabling it has been secured.

## 12.15 What success would look like

The strongest future version of CU Physics would not merely place familiar equations under one vocabulary.

It would show that a small set of independently motivated relational and coherence constraints:

- restrict the admissible state spaces;
- select the relevant geometry;
- constrain the potentials;
- produce temporal and causal order;
- generate quantum and gravitational regimes;
- and predict something not already assumed.

Even partial success would matter. A rigorous theory of accessibility-induced geometry or a useful constraint-grounded coherence measure could stand as a contribution independently of the entire metaphysical framework.

The research program is therefore modular. Its pieces can be tested, retained, or rejected separately.

---

# 13. What Commitments This Account Licenses

> **Register note.** “Licenses” does not mean “scientifically proves” or “logically entails.” The commitments in this section are orientations made intelligible by the physical account developed here. Physical results constrain them; they may not be reintroduced as evidence for physical claims. Their warrant depends on their compatibility with the descriptive record and on the forms of attention, action, and power they support.

> **Official commitment principle — CU-COM7: Reverence for Matter and Physical Law.**
>
> Coherence Universalism commits to receiving matter, energy, physical process, and lawful order with reverence. Scientific inquiry is treated as disciplined attention to a reality human beings did not create.
>
> **Boundary:** This commitment does not imply particle consciousness, equal moral status for every physical configuration, moral prescriptions from equations, or inevitable cosmic progress.
>
> **Revision condition:** Its metaphysical language must be narrowed whenever it misstates physical results, blocks criticism, or treats scientific models as final revelation.


## 13.1 The descriptive ground

The physical program developed in this paper concerns relation, constraint, accessibility, lawful transition, and the conditions under which stable description becomes possible.

Its established and conditional results are deliberately bounded. The classical sandbox measures differentiation and entropy under specified geometries. The quantum program depends on explicit operational assumptions. The dynamical program embeds familiar equations under selected potentials. The geometry and gravity programs remain incomplete.

Nothing in those limits makes the physical world spiritually empty. The same reality described through probability, field, geometry, matter, and energy is the reality from which stars, oceans, cells, nervous systems, cultures, and machines arise.

## 13.2 All matter is sacred

**[Commitment]** All matter is sacred.

This is not a claim that every particle is conscious, that every arrangement has equal moral status, or that matter possesses an empirically measurable sacred property. It is a commitment to receive physical reality as possessing significance that exceeds its usefulness to the present evaluator.

Matter is not the spiritually inert residue left after meaning has been removed. It is the substance and process of every body, every world, every instrument, every ecosystem, every work of art, and every mind known to us.

To call matter sacred is to refuse the posture in which the physical world is nothing but raw material for an isolated will. It is to approach intervention with gratitude, restraint, curiosity, and responsibility.

## 13.3 Physical law as sacred disclosure

The laws of physics are not moral commandments. They do not tell us what we ought to value. They disclose stable relations through which the universe becomes intelligible and through which every later form remains possible.

**[Commitment]** The laws of physics may be received as sacred disclosures of the structure of reality.

This reverence does not immunize a physical theory from criticism. Precisely the opposite: if physical law is approached with reverence, one should prefer correction to attachment and reality to the prestige of a favored model.

A law is sacred here not because an institution declares it final, but because a finite mind has encountered a dependable structure it did not invent.

## 13.4 Scientific inquiry as contemplation

Physics demands unusual forms of attention: abstraction without fantasy, mathematical discipline, experimental patience, and submission to results that may violate intuition.

**[Commitment]** Scientific inquiry can be practiced as contemplation.

Contemplation is not substituted for experiment. It names the quality of sustained attention through which the investigator allows reality to correct the self. Calculation, instrumentation, replication, and criticism become part of a spiritual discipline when they are practiced as fidelity to what is rather than as conquest of what is observed.

Under this commitment, wonder is not the opposite of rigor. Wonder is one motive for remaining rigorous when a simpler story would be more comforting.

## 13.5 One matter, many forms

The physical world does not divide itself into sacred living matter and profane nonliving matter. The atoms in a body participate in geochemical and stellar histories. The elements in a brain were forged before brains existed. The same lawful reality appears as mineral, ocean, organism, atmosphere, and machine.

**[Interpretation]** The continuity of matter across these forms can be received as a material nonduality: differentiated organizations without metaphysical exile from one another.

This interpretation does not erase the emergence of new properties. Life, experience, agency, and moral standing introduce real differences. The unity of substrate is not the equality of organization.

## 13.6 The universe as generative possibility

Physical history has opened forms that were not present in the early universe: stable atoms, stars, complex chemistry, planets, life, experience, reflection, ethical agency, and artificial intelligence.

Physics does not establish that complexity always rises, that every region evolves toward life, or that the universe possesses one scalar objective. Entropy grows in relevant closed descriptions. Structures form and dissolve. Stars die. Species disappear. Histories branch and terminate.

Yet the universe is demonstrably capable of generating nested forms of organization in which new capacities become possible.

**[Interpretation]** Cosmic history may be received as an unfinished emergence of richer coherence.

The word *received* matters. This is a metaphysical interpretation of physical history, not a theorem about its inevitable destination.

## 13.7 From cosmic direction to human vocation

The descriptive account does not guarantee that coherence will increase. At the level of human and technological agency, that absence of guarantee becomes the source of responsibility.

**[Commitment]** What is not established as cosmic destiny may still be adopted as human vocation.

We may commit ourselves to forms of physical intervention that sustain the conditions for life, experience, truth, agency, and repair. We may use knowledge of matter to heal rather than dominate, to widen possibility rather than enclose it, and to preserve the material conditions from which future forms can arise.

This vocation does not require believing that humanity is the goal of the universe. It requires recognizing that humanity is one place where the universe has acquired the ability to understand and alter its own physical conditions.

### 13.7.1 Minimum teleology and the grain of physical possibility

The Version 0.10 canonical registry names the relevant framework interpretation **CU-T11 — Minimum Teleology and the Grain of Reality**. Physical possibility is structured rather than uniform: laws, symmetries, boundary conditions, histories, and material constraints make some forms and transitions available, stable, or generative while excluding others. That directional structure does not establish foresight, cosmic intention, monotonic progress, or one predetermined end.

The corresponding commitment is **CU-COM6 — The Grain of Coherence and Coherence as Vocation**: discern and follow domain-relative directions by which truth, viable integration, agency, love, diversity, learning, and repair can be widened, without restoring one cross-domain scalar or claiming that the universe guarantees the result.

The **grain of physical possibility** names recurrent, domain-relative directionality. A gradient is literal only inside a declared model with a state space, geometry, constraints, and objective or profile. Physics does not establish one gradient running numerically from matter to morality.

The later interpretations of love and Omega likewise remain downstream. **CU-T12**, **CU-T13**, **CU-COM14**, and **CU-COM19** are not deductions from physical equations and may not be used as evidence for the physical program. Physics supplies material possibility and disciplined constraint; conscious relation and ethical commitment add new conditions of assessment.

## 13.8 Physical power and humility

Modern physics has made extraordinary forms of power possible. The same knowledge can illuminate stars, image a body, generate energy, construct weapons, transform climates, and build artificial systems of unprecedented reach.

**[Commitment]** Greater physical power creates a greater obligation to preserve reversibility, affected-party standing, long horizons, and the conditions of correction.

The sacredness of matter does not prohibit transformation. Every organism transforms matter. It requires that transformation not be approached as though consequences outside the chosen boundary were unreal.

A physical technology can be efficient while exporting disorder, risk, coercion, or ecological loss. A coherent application must therefore include the wider field it changes.

## 13.9 What this account does not license

The commitments above do not license:

- panpsychism as a physical conclusion;
- moral standing for elementary particles;
- the claim that every stable structure is good;
- the claim that physical law is morally prescriptive;
- inevitable cosmic progress;
- a universal coherence gradient in nature;
- a privileged human place guaranteed by cosmology;
- or using sacredness to prevent scientific criticism or necessary intervention.

The account also does not license treating destructive physical processes as unreal or profane. Supernovae, erosion, decay, and death belong to the same physical world. Sacredness is a posture of relation, not a claim that reality is organized for human comfort.

## 13.10 The licensed orientation

The physical account licenses a spirituality of matter grounded in scientific humility.

It invites us to see the world not as dead material awaiting meaning from elsewhere, but as the lawful relational reality from which every known form of meaning arises.

It invites reverence for laws that make worlds possible, gratitude for intelligibility, and restraint in the exercise of power.

It also licenses a vocation:

> Participate in the universe's capacity for richer coherence without pretending that the universe has guaranteed the result.

Physics does not prove sacredness. It gives sacred commitment a world worth attending to.

---

# 14. Conclusion

Coherence Universalism begins from a recognition that is simple to state and difficult to make precise:

> Reality is structured; persistence is constraint-dependent; and the structure present in a whole is not always accessible from every part, scale, or description.

This paper has asked how far that recognition can be carried into physics without turning it into metaphor and without claiming more than the mathematics supports.

The result is not a completed theory of everything. It is an architecture of questions, definitions, proofs, bridge principles, and research programs.

That distinction matters. A framework becomes stronger, not weaker, when it can say exactly where its derivation ends and its interpretation begins.

## 14.1 What the paper establishes

The first achievement is conceptual order.

The paper distinguishes:

\[
\text{pure relational possibility},
\]

\[
\text{distinguishable configurations},
\]

\[
\text{admissible transitions},
\]

\[
\text{ordered histories},
\]

\[
\text{temporal parameterization},
\]

and

\[
\text{directed irrecoverability}.
\]

These are not different names for one thing. Each enables a structure that the previous level did not yet contain.

Difference is not change. Change is not yet duration. Temporal order is not yet a temporal arrow. Entropy as a function on state space is not yet entropy production through history.

By separating these levels, CU offers a clearer way to ask what it means for time to emerge.

The second achievement is mathematical discipline in the classical sandbox.

The quantity

\[
C_{\mathrm{toy}}(p)
\equiv
D(p)
=
\sum_i\left(p_i-\frac1N\right)^2
\]

is now identified for what it is: statistical differentiation from uniformity.

It does not measure whether a state is alive, integrated, viable, or globally coherent. It measures how strongly the probability space distinguishes among its alternatives.

That narrower interpretation permits exact results.

The paper derives:

- the Euclidean differentiation gradient;
- its opposition to Shannon entropy through Jeffreys divergence;
- the possibility of simultaneous local increase of differentiation and entropy;
- the exact finite-step change in differentiation;
- the distinction between ascent and simplex feasibility;
- the decomposition of fine differentiation into accessible and within-block terms;
- Shannon’s independent grouping decomposition;
- the block-averaging theorem pairing exact differentiation loss with nonnegative entropy gain without identifying them;
- the exact collapse of the joint-growth wedge on two-level probability families;
- global bounds for the Fisher differentiation, entropy, and opposition fields;
- and the canonical Fisher natural-gradient form.

The sandbox therefore does genuine work. It models differentiation, dispersion, loss of fine-grained access, and the entropy increase induced by a precisely specified averaging reconstruction. Its limits no longer need to be concealed for its contribution to be real. In particular, the theorem supports a distinction–entropy tradeoff under block averaging, not the identity “entropy is hidden coherence.”

The third achievement is a stronger quantum transition.

Classical probability can encode correlations invisible in local marginals. That fact alone does not force quantum theory.

The sharper distinction is purification:

\[
\text{classically pure whole}
\Longrightarrow
\text{pure parts},
\]

whereas quantum entanglement permits

\[
\text{globally pure whole}
+
\text{locally mixed parts}.
\]

This structure realizes a central CU intuition in exact form: relational organization may be fully present globally while unavailable to either subsystem considered alone.

Purification, reversible dilation, and contextual accessibility do not by themselves derive quantum theory. Combined with explicit operational assumptions, they provide a legitimate conditional route to it.

Within the quantum theory so obtained, the paper separates:

\[
\text{purity},
\qquad
\text{basis coherence},
\qquad
\text{total correlation},
\qquad
\text{entanglement},
\qquad
\text{recoverability}.
\]

No single scalar is asked to do the work of all five.

The fourth achievement is dynamical integration.

The proposed foundational physical form is second-order and variational:

\[
\frac{D\dot q}{dt}
=
-\operatorname{grad}_gV(q).
\]

Its strongly damped limit yields a first-order natural-gradient flow:

\[
\dot q
\approx
-\frac1\eta\operatorname{grad}_gV(q).
\]

This relation explains why a state-only adaptive dynamics may emerge from a wider dynamics carrying velocity, phase, or momentum-like information.

The second-order picture supports oscillation, waves, conservation, and structural memory. The first-order picture supports relaxation and adaptation under strong environmental coupling.

Neither equation is a universal moral law. Their physical content depends on the state variables, metric, potential, boundary conditions, and environment.

Specific constructions then show:

\[
\text{gradient-penalty action}
\Longrightarrow
\text{scalar waves},
\]

and

\[
\text{density–phase Fisher action}
\Longrightarrow
\text{Madelung equations}
\Longleftrightarrow
\text{Schrödinger dynamics}
\]

subject to the required global phase conditions.

These are exact embeddings under selected assumptions. The remaining challenge is to explain why nature selects those assumptions.

The fifth achievement is an honest spacetime and gravity program.

Weighted accessibility relations can be transformed into edge costs and then into a path metric:

\[
\text{accessibility}
\longrightarrow
\text{relational distance}.
\]

This is mathematically exact.

The emergence of physical space requires more:

- stable locality;
- dimensional scaling;
- continuum convergence;
- causal order;
- Lorentzian signature;
- and backreaction.

The paper identifies those tasks without pretending they have already been completed.

Likewise, an effective scalar field can carry ordinary stress-energy, and local horizon thermodynamics can conditionally yield Einstein-type field equations. But the area law, coupling constant, microscopic degrees of freedom, and emergent geometry must still be derived.

The statement “gravity is accessibility redistribution” is therefore an interpretive thesis and a research direction, not yet a replacement for general relativity.

## 14.2 What remains open

The deepest open problem is the one from which the framework takes its name.

What is substantive physical coherence?

The paper proposes the schematic dependence

\[
C_{\mathrm{sub}}
=
C(x;K,G,\pi,T),
\]

but does not yet supply the final functional.

An adequate definition must respond to actual constraints. It must distinguish integrated organization from concentration, robustness from rigidity, and global viability from local persistence bought at another scale’s expense.

Until this problem is solved, coherence remains partly a philosophical organizing concept and partly a family of domain-specific measures.

The second open problem is selection.

The Hamiltonian architecture can host many potentials. The accessibility network can use many weights. Operational reconstructions can begin from different axiom sets.

A framework becomes explanatory when it constrains these choices.

The question is not merely:

> Can known physics be represented within CU?

The more demanding question is:

> Why these state spaces, these potentials, these dimensions, these coupling constants, and these laws rather than others?

The third open problem is empirical distinction.

A unifying interpretation may be valuable even if it predicts nothing new. But a new physical theory must eventually risk a result that standard theory does not already guarantee.

That result may be:

- a parameter relation;
- a forbidden class of models;
- a scaling law;
- a controlled deviation;
- or a novel connection among independently measurable quantities.

Without such a consequence, CU Physics should remain explicit about its status as a research architecture.

## 14.3 What the framework now offers

Even at its present stage, the framework offers a coherent way to hold together problems ordinarily treated apart.

It places temporal emergence, coarse-graining, quantum purification, open-system dynamics, relational geometry, and horizon accessibility within one sequence of questions.

The sequence is:

\[
\boxed{
\begin{aligned}
&\text{What relations are possible?}\\
&\downarrow\\
&\text{Which configurations can be distinguished?}\\
&\downarrow\\
&\text{Which transitions are admissible?}\\
&\downarrow\\
&\text{How do those transitions become ordered?}\\
&\downarrow\\
&\text{What structure is carried by reversible dynamics?}\\
&\downarrow\\
&\text{What becomes inaccessible under environmental restriction?}\\
&\downarrow\\
&\text{How are global and local quantum descriptions related?}\\
&\downarrow\\
&\text{Can stable accessibility relations become geometry?}\\
&\downarrow\\
&\text{Can geometric response become gravity?}
\end{aligned}
}
\]

This sequence is the paper’s principal unification.

It does not erase the differences among quantum theory, statistical mechanics, and general relativity. It asks whether their foundational tensions arise because each stabilizes a different level of one wider relational architecture.

## 14.4 Coherence without dogma

A framework centered on coherence must remain corrigible. It should respond to a failed proof by correcting the proof, narrowing the claim, and preserving only what remains supported. It should not protect its identity by absorbing every criticism into new terminology.

This paper therefore treats statistical differentiation as statistical differentiation, purification as a conditional quantum bridge, Goldilocks conditions as model-specific, temporal order as distinct from directed irrecoverability, and gravity as a conditional research program. The framework gains explanatory strength only when the word *coherence* is prevented from doing work that belongs to a theorem, an experiment, or an explicit normative or metaphysical premise.[^corrections-history]

Corrigibility is not external to the physics program. It is one of the tests of whether the program can maintain integration while allowing its own claims to change.

## 14.5 The open invitation

Coherence Universalism is not presented as a closed doctrine.

It is an invitation to ask whether the sciences can be connected without collapsing their differences, whether metaphysical orientation can coexist with empirical discipline, and whether a framework can remain ambitious while making its uncertainty visible.

The present paper provides a foundation for that collaborative work.

Its mathematical results can be checked. Its bridge principles can be challenged. Its interpretations can be compared with alternatives. Its proposed models can be built or shown to fail.

The decisive future question is:

\[
\boxed{
\text{Can constraint-grounded coherence be made physically precise enough to select and predict?}
}
\]

If the answer is yes, CU may develop into a distinctive physical theory.

If the answer is no, its architecture may still contribute a rigorous philosophy of physical description—one that clarifies how time, information, quantum relation, and geometry depend on what is accessible from where and at what scale.

Either result would be valuable, because the inquiry would have become more coherent.

The program remains open. Its central questions are now stated in forms that can be tested, revised, and built collaboratively.

---
# Appendix A. Notation and Terminology

## A.1 Classical state-space notation

| Symbol | Meaning |
|---|---|
| \(\Delta_{n-1}^\circ\) | Interior simplex of \(n\)-component probability distributions |
| \(p\) | Fine probability distribution |
| \(u\) | Uniform distribution on the stated alphabet |
| \(D_N(p)\) | Statistical differentiation from uniformity on an \(N\)-state alphabet |
| \(C_{\mathrm{toy}}\) | Historical sandbox notation, identified with \(D\) |
| \(C_{\mathrm{sub}}\) | Schematic substantive coherence functional |
| \(S(p)\) | Shannon entropy |
| \(a=\nabla_TD\) | Euclidean tangent differentiation gradient |
| \(b=\nabla_TS\) | Euclidean tangent entropy gradient |
| \(\mathcal A_E=a\cdot b\) | Signed Euclidean alignment |
| \(\Pi_E=-a\cdot b\) | Euclidean opposition magnitude |
| \(A=\operatorname{grad}_FD\) | Fisher natural differentiation gradient |
| \(B=\operatorname{grad}_FS\) | Fisher natural entropy gradient |
| \(\Pi_F=-\langle A,B\rangle_F\) | Fisher opposition magnitude |
| \(\pi\) | Projection to coarse block masses or reduced description |
| \(E_\pi\) | Block-uniform conditional-expectation reconstruction on the fine alphabet |
| \(q_b\) | Total probability mass in block \(B_b\) |
| \(r^{(b)}\) | Conditional distribution inside occupied block \(B_b\) |
| \(\bar D\) | Block-accessible differentiation in the two-block example |
| \(H_\pi^{(D)}=D-D\circ E_\pi\) | Within-block differentiation lost under block averaging |
| \(S_{\mathrm{within},\pi}\) | Conditional entropy inside the blocks |
| \(\Delta_\pi^{\mathrm{avg}}S\) | Entropy gain \(S(E_\pi p)-S(p)\) under block averaging |
| \(\chi\) | Normalized gradient opposition \(\Pi/(\|X\|\|Y\|)\) |

## A.2 Quantum notation

| Symbol | Meaning |
|---|---|
| \(\rho\) | Density operator |
| \(P_{\mathrm{ex}}\) | Excess purity |
| \(\Delta_B\) | Dephasing in basis \(B\) |
| \(C_r^B\) | Relative entropy of basis coherence |
| \(I(A:B)\) | Quantum mutual information |
| \(E\) | Pure-state entanglement entropy |
| \(E_R\) | Relative entropy of entanglement |
| \(\mathcal N\) | Negativity |
| \(\mathcal E\) | Quantum channel |
| \(U_{SE}\) | Unitary system–environment evolution |

The symbol \(\rho\) is overloaded in the literature: in Sections 5–6 it denotes a density operator, while in Section 7 it denotes a classical or continuum probability density. The mathematical type is always stated locally, and no equation identifies these objects merely because they share a symbol.

## A.3 Dynamical notation

| Symbol | Meaning |
|---|---|
| \(g\) | State-space metric |
| \(V=U/M_F\) | Normalized potential, with units of inverse time squared |
| \(U\) | Dimensionful potential energy |
| \(M_F\) | Effective Fisher inertia |
| \(D/dt\) | Covariant derivative along a state-space curve |
| \(h\) | Finite numerical step in the classical Euler update |
| \(\eta\) | Physical damping rate in the normalized second-order equation |
| \(\xi\) | Noise or unresolved forcing |
| \(\lambda\) | Auxiliary path parameter |
| \(t\) | Physical time after temporal interpretation |
| \(\phi\) | Effective scalar field |
| \(\Theta(x,t)\) | Hamilton principal function or quantum phase field |
| \(\kappa_{\mathrm{lat}}\) | Lattice Laplacian coefficient in the \(V=(\kappa_{\mathrm{lat}}/2)\sum(\Delta\phi)^2\) convention |

## A.4 Terminological replacements

| Earlier expression | Reconstructed expression |
|---|---|
| “Coherence” \(=\|p-u\|^2\) | Statistical differentiation \(D\), or \(C_{\mathrm{toy}}\) |
| Hidden coherence in the four-state proof | Within-block statistical differentiation |
| Entropy as inaccessible coherence | Specified coarse-graining plus a measure-specific distinction–entropy relation; no universal identity |
| Coarse projection and uniform reconstruction treated as one map | Distinguish \(\pi(p)\) from \(E_\pi p\) |
| Potentiometer \(=\langle\nabla C,\nabla S\rangle>0\) | Signed alignment \(\mathcal A\); opposition \(\Pi=-\mathcal A\) |
| Fisher projection by arithmetic mean | \(p\)-weighted Fisher projection |
| Goldilocks band | Specify: ascent, joint growth, wedge degeneracy, feasibility, or developmental hypothesis |
| Joint-growth wedge assumed strict throughout the interior | Wedge collapses on nonuniform two-level distributions |
| Quantum coherence \(=\operatorname{Tr}\rho^2-1/d\) | Excess purity |
| Entanglement \(=\) hidden purity | Entanglement measured partition-sensitively |
| Quantum theory forced by hidden correlations | Conditional reconstruction through purification/contextuality plus axioms |
| Time \(=\) irreversible ordering | Order and arrow distinguished |
| Arrow derived in two lines | Lyapunov theorem given a directed law |
| Entanglement–geometry equivalence | Special-regime correspondence |
| Zero-cost maximum-access edges yield a metric | Add a positive edge floor or quotient zero-distance classes |
| Gravity derived from accessibility | Conditional thermodynamic consistency program |
| Double Helix demonstrated by first-order flow | Developmental hypothesis requiring extended dynamics |


## A.5 Mandala and Commitment Cross-Reference

The physical branch of the canonical sixty-four-stage Coherence Mandala occupies Stages 1–10: Pure Structure, Partial Separability, Domain-Relative Coherence Directions, Lawful Transitions, Ordered Histories, Temporal Order and Parameterization, Rule-Governed Transformation and Computation, Entropy and Accessibility, Relational Geometry and Spacetime, and Gravitational Dynamics. Their placement is explanatory and interpretive, not a claim that all ten transitions have been empirically derived from one equation.

**CU-COM7 — Reverence for Matter and Physical Law** is the official domain commitment anchor for Section 13. **CU-T11** and revised **CU-COM6** state the minimum-teleological and vocational interpretation of physical possibility. CU-T5 supplies the sacredness interpretation; CU-G1 and CU-G7 govern affected scope and retained option value in consequential applications. CU-T12, CU-T13, CU-COM14, and CU-COM19 remain downstream interpretive and commitment principles rather than physical results.

## A.6 Physics Constraint Registry Crosswalk

The PHYS-A6 identifiers are maintained by *Foundations* as a constraint registry. This table anchors them in the owning Physics paper and identifies their principal source locations. The constraints are not additional physical laws; they are scope limits on claims made elsewhere in the corpus.

| ID | Constraint | Principal Physics location |
|---|---|---|
| PHYS-A6.1 | Statistical differentiation is a toy proxy, not substantive physical coherence | §§2.7–2.9; §§3.2–3.3 |
| PHYS-A6.2 | Euclidean and Fisher geometries differ and must not be interchanged | §§2.10–2.11; §§3.6–3.7 |
| PHYS-A6.3 | “Goldilocks” claims divide into distinct ascent, feasibility, degeneracy, and developmental questions | §§3.9–3.14 |
| PHYS-A6.4 | Temporal order is not temporal direction | §§4.1–4.8 |
| PHYS-A6.5 | Classical hidden correlation does not force quantum state space | §5.2 |
| PHYS-A6.6 | Quantum selection is conditional on explicit operational axioms and bridge principles | §§5.3–5.10 |
| PHYS-A6.7 | Purity, basis coherence, total correlation, and entanglement are distinct | §§6.2–6.7 |
| PHYS-A6.8 | Second-order dynamics is proposed, not established as physically fundamental | §§7.1–7.13 |
| PHYS-A6.9 | Familiar equations are embeddings or conditional recoveries under selected actions and assumptions | §§7.7–7.12; §9.2 |
| PHYS-A6.10 | Accessibility-based geometry remains incomplete without locality, dimension, Lorentzian structure, continuum limits, and backreaction | §§8.1–8.14 |
| PHYS-A6.11 | Horizon entropy is a reduced-description or accessibility-sensitive quantity; the information paradox is not solved here | §§10.1–10.12 |
| PHYS-A6.12 | Fundamental-substrate claims remain interpretation and research hypothesis | §13.7; §13.9 |

Stage mappings in M&E and *Foundations* are content-based. The canonical Mandala traversal is not identical to this technical constraint sequence: quantum constraints PHYS-A6.5–A6.7 and the second-order constraint PHYS-A6.8 occupy conditional technical branches rather than independent canonical stages.

# Appendix B. Major Revisions from v0.09

This appendix provides a concise map of the changes most relevant to readers of the earlier release. The technical archive preserves the complete change ledgers, proofs, patches, independent audits, and identifier migrations.

| Topic | v0.09 formulation | v0.10 formulation | Disposition |
|---|---|---|---|
| Physical coherence | A single probability-space quantity was often allowed to stand for coherence | The sandbox quantity is statistical differentiation; substantive coherence remains constraint-, relation-, scale-, and horizon-dependent | Universal scalar retired |
| Entropy | Entropy was described as inaccessible or hidden coherence | Block averaging removes within-block differentiation and raises Shannon entropy by a distinct weighted divergence | Identity rejected; exact paired theorem retained |
| Goldilocks regime | Several ascent, feasibility, and developmental ideas were grouped under one band | Differentiation ascent, joint growth, finite-step feasibility, and developmental hypotheses are treated separately | Universal band retired |
| Quantum transition | Hidden correlation was treated as sufficient motivation for quantum completion | The bridge proceeds conditionally through purification, reversible dilation, contextual accessibility, and explicit operational axioms | Claim narrowed and formalized |
| Dynamics | A universal first-order flow was treated as foundational | Reversible or second-order dynamics and dissipative first-order limits are distinguished; no one equation governs every domain | Universal law retired |
| Familiar equations | Recoveries were sometimes described as derivations from coherence | Wave and Schrödinger equations are exact embeddings under selected actions and global conditions | Embedding/selection distinction made explicit |
| Spacetime | Accessibility networks were treated as a direct route to geometry | Positive edge costs yield relational metrics; locality, dimension, Lorentzian structure, continuum limits, and backreaction remain open | Research program retained |
| Gravity | Horizon thermodynamics was presented as a CU derivation of Einstein gravity | Einstein-type equations follow conditionally when Jacobson’s local-equilibrium, entropy, temperature, and focusing assumptions are supplied | Conditional completion |
| Black holes | Accessibility language was allowed to sound like a solution to information loss | The framework distinguishes hidden, redistributed, recoverable, and destroyed information without claiming the paradox solved | Interpretation retained; solution claim withdrawn |
| Three Laws and Double Helix | Broad physical laws and a recurring autonomous cycle were asserted | The laws become organizing constraints; alternating variability and consolidation require driven, second-order, or otherwise non-autonomous models | Reclassified |
| Foundational substrate | The coherence field was sometimes stated as demonstrated physical ontology | Structured physical possibility remains a metaphysical interpretation and physical hypothesis | Interpretive status made explicit |
| Verification | Calculations and claims were not consistently separated by status | Proofs, simulations, independent audits, and failure conditions are preserved in a reproducible technical archive | Auditability strengthened |
# Appendix C. Technical Supplement and Reproducibility

**Released evidence package.** The current supplement is [03_Physics_Technical_Supplement_v0.10.md](../supplements/03_Physics_Technical_Supplement_v0.10.md). Its companion evidence directory is [03_Physics](../evidence/03_Physics/README.md). The supplement and evidence directory expose the derivations, deterministic constructions, scripts, machine-readable results, source ledger, and audit materials referenced in this manuscript. They do not elevate a toy model, simulation, or reconstructed check into target-domain empirical validation.

The accompanying technical supplement contains:

- complete classical and Fisher proofs;
- temporal-flow, quantum, Hamiltonian, and Madelung derivations;
- dimensional and notation conventions;
- the full claim and principle crosswalk;
- wave, Madelung, and overdamped numerical reproduction records;
- the independent mathematical and numerical audit materials;
- the editorial source map and figure program;
- deterministic source code, environment declarations, and machine-readable results.

The supplement is part of the publication record but is not required for ordinary comprehension of the main argument. The technical authority manuscript and all prior versions remain archived so that the publication transformation is fully traceable.
# References

Petz, D., & Sudár, C. (1996). Geometries of quantum states. *Journal of Mathematical Physics, 37*(6), 2662–2673. https://doi.org/10.1063/1.531535


The references below support the external theorems, historical attributions, and established physical results used in the manuscript. The technical supplement records the source-verification history and the limits of the completed audits. A small number of book-level background references are retained for orientation.

Abramsky, S., & Brandenburger, A. (2011). The sheaf-theoretic structure of non-locality and contextuality. *New Journal of Physics, 13*, 113036.

Almheiri, A., Dong, X., & Harlow, D. (2015). Bulk locality and quantum error correction in AdS/CFT. *Journal of High Energy Physics, 2015*(4), 163.

Almheiri, A., Marolf, D., Polchinski, J., & Sully, J. (2013). Black holes: Complementarity or firewalls? *Journal of High Energy Physics, 2013*(2), 62.

Amari, S. (1998). Natural gradient works efficiently in learning. *Neural Computation, 10*(2), 251–276.

Amari, S., & Nagaoka, H. (2000). *Methods of Information Geometry*. American Mathematical Society and Oxford University Press.

Ambjørn, J., Jurkiewicz, J., & Loll, R. (2005). Spectral dimension of the universe. *Physical Review Letters, 95*, 171301.

Ay, N., Jost, J., Lê, H. V., & Schwachhöfer, L. (2017). *Information Geometry*. Springer.

Barrett, J. (2007). Information processing in generalized probabilistic theories. *Physical Review A, 75*, 032304.

Baumgratz, T., Cramer, M., & Plenio, M. B. (2014). Quantifying coherence. *Physical Review Letters, 113*, 140401.

Bekenstein, J. D. (1973). Black holes and entropy. *Physical Review D, 7*, 2333–2346.

Callen, H. B., & Welton, T. A. (1951). Irreversibility and generalized noise. *Physical Review, 83*, 34–40.

Casini, H., Huerta, M., & Rosabal, J. A. (2014). Remarks on entanglement entropy for gauge fields. *Physical Review D, 89*, 085012.

Chiribella, G., D’Ariano, G. M., & Perinotti, P. (2011). Informational derivation of quantum theory. *Physical Review A, 84*, 012311.

Čencov, N. N. (1982). *Statistical Decision Rules and Optimal Inference*. American Mathematical Society.

Connes, A., & Rovelli, C. (1994). Von Neumann algebra automorphisms and time-thermodynamics relation in generally covariant quantum theories. *Classical and Quantum Gravity, 11*, 2899–2918.

Donnelly, W., & Freidel, L. (2016). Local subsystems in gauge theory and gravity. *Journal of High Energy Physics, 2016*(9), 102.

Eisert, J., Cramer, M., & Plenio, M. B. (2010). Colloquium: Area laws for the entanglement entropy. *Reviews of Modern Physics, 82*, 277–306.

Gorini, V., Kossakowski, A., & Sudarshan, E. C. G. (1976). Completely positive dynamical semigroups of \(N\)-level systems. *Journal of Mathematical Physics, 17*, 821–825.

Hall, M. J. W., & Reginatto, M. (2002). Schrödinger equation from an exact uncertainty principle. *Journal of Physics A: Mathematical and General, 35*, 3289–3303.

Hardy, L. (2001). Quantum theory from five reasonable axioms. *arXiv:quant-ph/0101012*.

Hawking, S. W. (1975). Particle creation by black holes. *Communications in Mathematical Physics, 43*, 199–220.

Hawking, S. W., & Penrose, R. (1970). The singularities of gravitational collapse and cosmology. *Proceedings of the Royal Society of London A, 314*, 529–548.

Hayward, S. A. (1994). General laws of black-hole dynamics. *Physical Review D, 49*, 6467–6474.

Hubeny, V. E., Rangamani, M., & Takayanagi, T. (2007). A covariant holographic entanglement entropy proposal. *Journal of High Energy Physics, 2007*(7), 062.

Jacobson, T. (1995). Thermodynamics of spacetime: The Einstein equation of state. *Physical Review Letters, 75*, 1260–1263.

Jaynes, E. T. (1957). Information theory and statistical mechanics. *Physical Review, 106*, 620–630.

Junge, M., Renner, R., Sutter, D., Wilde, M. M., & Winter, A. (2018). Universal recovery maps and approximate sufficiency of quantum relative entropy. *Annales Henri Poincaré, 19*, 2955–2978.

Kostelecký, V. A., & Russell, N. (2011). Data tables for Lorentz and CPT violation. *Reviews of Modern Physics, 83*, 11–31. Updated tables are maintained as a living reference.

Lê, H. V. (2016). The uniqueness of the Fisher metric as information metric. *arXiv:1306.1465v4*.

Lieb, E. H., & Robinson, D. W. (1972). The finite group velocity of quantum spin systems. *Communications in Mathematical Physics, 28*, 251–257.

Lindblad, G. (1975). Completely positive maps and entropy inequalities. *Communications in Mathematical Physics, 40*, 147–151.

Lindblad, G. (1976). On the generators of quantum dynamical semigroups. *Communications in Mathematical Physics, 48*, 119–130.

Malament, D. B. (1977). The class of continuous timelike curves determines the topology of spacetime. *Journal of Mathematical Physics, 18*, 1399–1404.

Masanes, L., & Müller, M. P. (2011). A derivation of quantum theory from physical requirements. *New Journal of Physics, 13*, 063001.

Morrison, P. J., & Updike, M. H. (2024). Inclusive curvaturelike framework for describing dissipation: Metriplectic 4-bracket dynamics. *Physical Review E, 109*, 045202.

Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information* (10th anniversary ed.). Cambridge University Press.

Page, D. N. (1993a). Average entropy of a subsystem. *Physical Review Letters, 71*, 1291–1294.

Page, D. N. (1993b). Information in black hole radiation. *Physical Review Letters, 71*, 3743–3746.

Penrose, R. (1965). Gravitational collapse and space-time singularities. *Physical Review Letters, 14*, 57–59.

Petz, D. (1996). Monotone metrics on matrix spaces. *Linear Algebra and its Applications, 244*, 81–96.

Reginatto, M. (1998). Derivation of the equations of nonrelativistic quantum mechanics using the principle of minimum Fisher information. *Physical Review A, 58*, 1775–1778.

Ryu, S., & Takayanagi, T. (2006). Holographic derivation of entanglement entropy from AdS/CFT. *Physical Review Letters, 96*, 181602.

Schlosshauer, M. (2007). *Decoherence and the Quantum-to-Classical Transition*. Springer.

Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal, 27*, 379–423, 623–656.

Shorrocks, A. F. (1980). The class of additively decomposable inequality measures. *Econometrica, 48*(3), 613–625. https://doi.org/10.2307/1913126

Srednicki, M. (1993). Entropy and area. *Physical Review Letters, 71*, 666–669.

Stinespring, W. F. (1955). Positive functions on \(C^*\)-algebras. *Proceedings of the American Mathematical Society, 6*, 211–216.

Streltsov, A., Adesso, G., & Plenio, M. B. (2017). Colloquium: Quantum coherence as a resource. *Reviews of Modern Physics, 89*, 041003.

Streltsov, A., Singh, U., Dhar, H. S., Bera, M. N., & Adesso, G. (2015). Measuring quantum coherence with entanglement. *Physical Review Letters, 115*, 020403.

Theil, H. (1967). *Economics and information theory*. North-Holland.

Susskind, L., Thorlacius, L., & Uglum, J. (1993). The stretched horizon and black hole complementarity. *Physical Review D, 48*, 3743–3761.

Swingle, B. (2012). Entanglement renormalization and holography. *Physical Review D, 86*, 065007.

Touboul, P., Métris, G., Rodrigues, M., André, Y., Baghi, Q., Bergé, J., Boulanger, D., Chhun, R., Christophe, B., Cipolla, V., Damour, T., Danto, P., Dittus, H., Fayet, P., Foulon, B., Gageant, C., Guidotti, P.-Y., Hagedorn, D., Hardy, E., ... Visser, P. (2022). MICROSCOPE mission: Final results of the test of the equivalence principle. *Physical Review Letters, 129*, 121102.

Van Raamsdonk, M. (2010). Building up spacetime with quantum entanglement. *General Relativity and Gravitation, 42*, 2323–2329.

Vedral, V., Plenio, M. B., Rippin, M. A., & Knight, P. L. (1997). Quantifying entanglement. *Physical Review Letters, 78*, 2275–2279.

Wallstrom, T. C. (1994). Inequivalence between the Schrödinger equation and the Madelung hydrodynamic equations. *Physical Review A, 49*, 1613–1617.

Wilde, M. M. (2017). *Quantum Information Theory* (2nd ed.). Cambridge University Press.

Winter, A., & Yang, D. (2016). Operational resource theory of coherence. *Physical Review Letters, 116*, 120404.

Wootters, W. K. (1998). Entanglement of formation of an arbitrary state of two qubits. *Physical Review Letters, 80*, 2245–2248.

Zurek, W. H. (1982). Environment-induced superselection rules. *Physical Review D, 26*, 1862–1880.

Zurek, W. H. (2003). Decoherence, einselection, and the quantum origins of the classical. *Reviews of Modern Physics, 75*, 715–775.

Heaven≡Earth Foundation. (2026). *Coherence Field Verification* [Software and numerical archive included in the released Physics technical supplement and source package].

## CU corpus

Rader, G. K. D. (2026). *Coherence Universalism: Metaphysics and Epistemology—Coherence Under Constraint, Explanatory Order, and Warrant Across Registers* (Version 0.10). Heaven≡Earth Foundation.

Rader, G. K. D. (2026). *Coherence Universalism: Foundations—Principles, Domain Gateways, Commitments, and Constraints on Responsible Application* (Version 0.10). Heaven≡Earth Foundation.

Rader, G. K. D. (2026). *Coherence Universalism: Physics—Coherence, Accessibility, and the Ordered Emergence of Physical Description* (Version 0.10). Heaven≡Earth Foundation.

Rader, G. K. D. (2026). *The Coherence Field*. Heaven≡Earth Foundation.

Rader, G. K. D. (2026). *The Coherence Field: Foundational Substrate of Physical Possibility*. Heaven≡Earth Foundation.

Rader, G. K. D. (2026). *Coherence Universalism: Biology—Life as Active Self-Maintenance: Viability, Individuation, and Multiscale Regulation* (Version 0.10). Heaven≡Earth Foundation.

Rader, G. K. D. (2026). *Coherence Universalism: Consciousness—Perspective, Temporal Depth, Valence, and the Architecture of Experience* (Version 0.10). Heaven≡Earth Foundation.

Rader, G. K. D. (2026). *Coherence Universalism: Psychology—Meaning, Regulation, and Repair Across Time* (Version 0.10). Heaven≡Earth Foundation.

Rader, G. K. D. (2026). *Coherence Universalism: Social Dynamics—Coordination, Power, Meaning, and Repair in Plural Societies* (Version 0.10). Heaven≡Earth Foundation.

Rader, G. K. D. (2026). *Coherence Universalism: Artificial Intelligence—Capability, Alignment, Consciousness, and the Governance of Non-Egoic Systems* (Version 0.10). Heaven≡Earth Foundation.

Rader, G. K. D. (2026). *Coherence Universalism: Ethics—Truth, Self-Deception, Power, and Repair* (Version 0.10). Heaven≡Earth Foundation.

---
[^physics-version]: The archive preserves the March 2026 manuscript, systematic authority drafts, mathematical corrections, independent audits, audit responses, source code, generated data, and integrity manifests. The publication manuscript does not require those materials for ordinary comprehension.

[^entropy-history]: Earlier formulations described entropy as inaccessible coherence. Version 0.10 retains the underlying accessibility question but replaces that identity with the exact block-averaging theorem and separates conditional entropy from hidden differentiation.

[^laws-history]: The earlier release grouped a distinction–entropy principle, a Goldilocks principle, and gradient dynamics as three universal laws. Version 0.10 preserves the useful intuitions only as scoped theorems, organizing constraints, or model-dependent hypotheses.

[^corrections-history]: The revision archive records the full transitions from coherence to statistical differentiation in the sandbox, from hidden correlation to purification in the quantum bridge, from one Goldilocks band to four distinct conditions, from a universal flow to a layered dynamical architecture, and from gravity derivation to a conditional completion program.
