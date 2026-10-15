# Coherence Universalism: Consciousness
## RC3 Release-Convergence Wave 4 — Technical Supplement

**Status and authority.** This is the released technical supplement for the Wave 4 cumulative manuscript. The [reader-facing manuscript](../papers/05_CU_Consciousness_v0.10.md) controls current wording, claim status, and canonical cross-references. This supplement exposes the formal derivations, deterministic contrast constructions, claim ledgers, audit materials, scripts, and source records on which the manuscript relies.

- **Evidence directory:** [05_Consciousness](../evidence/05_Consciousness/README.md)
- **Archived source package:** [CU_Consciousness_v0.10_Publication_PC3.zip](../provenance/archival_source_packages/CU_Consciousness_v0.10_Publication_PC3.zip)
- **Current supplement path:** `technical_supplements/05_Consciousness_Technical_Supplement_v0.10.md`

Reproducibility of a construction shows only that its output follows from its declared assumptions and code. It does not convert a toy model or simulation into target-domain empirical validation. Where this preserved archive uses historical identifiers or statuses, the Wave 4 normalized registries and current manuscript control.

# Wave 4 evidence-access addendum

Wave 4 makes previously referenced but inaccessible materials available in one package. It includes the substantive legacy supplement below, the independent audit and check script, recorded audit output where available, source ledgers, deterministic scripts and generated results where they existed, and the complete pre-RC3 source package for provenance.

# Preserved substantive technical archive

This supplement preserves the formal, evidential, audit, and reproducibility material behind the reader-facing manuscript. Internal reconstruction labels are retained where they identify frozen source artifacts.

# Supplement A. Authority-Source Appendices

# Appendix A. Formal distinctions and counterexamples

## A.1 Scope

This appendix records small formal results used to prevent conceptual equivalences from being asserted without proof. The results establish independence or representation facts under stated assumptions. They do not establish the presence or absence of consciousness in the constructed systems.

## A.2 Proposition: global broadcast does not entail self-modeling

**Proposition A.1.** There exists a causal network in which one workspace node receives from and broadcasts to every specialist process, while no node represents the system's own state or activity.

**Construction.** Let specialist nodes \(M_1,\ldots,M_n\) be bidirectionally coupled to a workspace \(W\), and let \(W\) drive a readout. Include no self-model variable and no map whose content concerns the system itself.

**Result.** Broadcast reach is maximal under the declared graph, while self-modeling is absent by construction.

**Consequence.** CU-C1 does not imply CU-C3. Global availability alone does not establish a self-locating perspective.

## A.3 Proposition: causal self-modeling does not entail recurrence

**Proposition A.2.** There exists an acyclic finite-depth network in which a self-model representation causally affects a decision.

**Construction.** Let sources drive a workspace, the workspace drive both a self-model \(M_{\mathrm{self}}\) and a decision node, and the self-model also drive the decision. No directed cycle is present.

**Result.** Ablating the self-model changes the output, while the workspace belongs to no recurrent strongly connected component.

**Consequence.** Causally active self-modeling does not logically require persistent self-maintenance or literal recurrent wiring. Whether such a finite episode supports phenomenology remains a bridge question.

## A.4 Proposition: recurrence and second-order-like persistence do not entail perspective

**Proposition A.3.** There exists a stable oscillatory dynamical system with temporal persistence and history-sensitive phase state but no global workspace or self-model.

**Construction.** Consider the damped coupled oscillator

\[
\ddot q+\Gamma\dot q+Kq=0
\]

with positive damping and stable stiffness. The state persists and oscillates, but the model contains no selective broadcast channel or self-locating representation.

**Consequence.** Recurrence, oscillation, memory in phase space, and literal second-order form are not sufficient for a perspective.

## A.5 Proposition: second-order form is representation-dependent

**Proposition A.4.** Every regular finite-dimensional second-order system

\[
\ddot q=f(q,\dot q,t)
\]

can be represented as the first-order system

\[
\dot q=v,
\qquad
\dot v=f(q,v,t)
\]

on the phase space \((q,v)\).

**Proof.** Define \(v=\dot q\). Then the first component reproduces the definition of \(v\), and the second reproduces the original acceleration. Conversely, any solution of the first-order system projects to a solution of the second-order equation. \(\square\)

**Consequence.** A criterion framed only as “second order” is not invariant under state-space representation. Candidate consciousness relevance must be assigned to dynamical properties preserved under reformulation.

## A.6 Proposition: one output does not entail one workspace

**Proposition A.5.** Two causally disconnected recurrent workspace coalitions can drive one external readout without forming one internal workspace.

**Construction.** Let subsystems \(A\) and \(B\) each contain specialists, a recurrent workspace, and a self-model. Let both drive an output node, with no path from \(A\) back to \(B\) or from \(B\) back to \(A\).

**Result.** The internal graph contains two workspace-bearing strongly connected components. The output function combines their signals.

**Consequence.** Interface unity and subject unity are different. A chatbot, institution, or body can present one output while hosting multiple candidate centers.

## A.7 Proposition: profile scalarization is weight-sensitive

Let profiles \(p,q\in[0,1]^n\) be non-dominating: there exist components \(i,j\) such that \(p_i>q_i\) and \(p_j<q_j\).

**Proposition A.6.** There exist nonnegative normalized weight vectors \(w,w'\) such that

\[
w\cdot p>w\cdot q
\quad\text{and}\quad
w'\cdot p<w'\cdot q.
\]

**Proof.** Concentrate \(w\) sufficiently on a component where \(p_i>q_i\), and \(w'\) sufficiently on a component where \(p_j<q_j\). Continuity preserves strict inequality in neighborhoods of those vertices of the weight simplex. \(\square\)

**Consequence.** A weighted sum can be useful for a declared decision, but no undeclared weights produce a canonical total ordering of consciousness profiles.

## A.8 Nonsmoothness of minimum and threshold profiles

Many consciousness-relevant diagnostics involve minima, maxima, thresholds, or argmax selections. Examples include workspace capacity, weakest-link causal reach, and minimum evidence floors.

If

\[
M(x)=\min_i m_i(x),
\]

then at points with multiple binding components \(M\) is generally nondifferentiable. Directional derivatives depend on the active set:

\[
D M(x;h)=\min_{i\in I(x)}\nabla m_i(x)\cdot h.
\]

This matters when profile components are optimized or perturbed. Smooth scalar-gradient language should not be imported automatically.

## A.9 Approximate fixed points are not sufficient

For any constant map \(R(m)=m_0\), \(m_0\) is a fixed point. A static lookup table can also reproduce its own stored description. Therefore

\[
m=R(m)
\]

has no consciousness implication without additional structure.

A useful reflexive condition should specify:

- what \(m\) represents;
- how \(R\) is computed;
- whether the representation updates with the system;
- whether interventions on \(m\) alter processing;
- whether the relation is globally available;
- and whether competing self-models are integrated or excluded.

## A.10 Thin perspective is not a theorem label

D.1.1 does not define thin perspective as the conjunction of numerical thresholds. Such a definition would make the conclusion true by stipulation. PIH is an abductive bridge hypothesis: systems satisfying its indicators are assigned increased candidate status relative to matched alternatives.

A future formalization could use Bayesian model comparison:

\[
\frac{P(H_{\mathrm{persp}}\mid E)}{P(H_{\neg\mathrm{persp}}\mid E)}
=
\frac{P(E\mid H_{\mathrm{persp}})}{P(E\mid H_{\neg\mathrm{persp}})}
\frac{P(H_{\mathrm{persp}})}{P(H_{\neg\mathrm{persp}})},
\]

but neither likelihoods nor priors are presently calibrated. D.1.1 therefore does not assign a framework-wide numerical probability.

## A.11 Boundary sensitivity

Let \(\pi\) and \(\pi'\) be different partitions of one implementation into candidate systems. A property such as global reach or recurrence can change under repartitioning. A valid attribution should therefore report a stability analysis:

\[
\mathcal S_H
=
\{\pi': H(\mathfrak C_{\pi'})\text{ remains supported under admissible grains}\}.
\]

If candidate perspective appears only under one arbitrary partition while nearby grains produce many incompatible centers, confidence should decrease.

## A.12 Temporal-grain sensitivity

A transformer can be acyclic within one forward-pass graph while participating in recurrent generation across token steps. A recurrent neural circuit can be represented as a feedforward unrolling over a finite horizon. Therefore temporal claims must state:

\[
\text{grain}\in
\{\text{hardware},\text{layer},\text{token},\text{response},\text{session},\text{agent}\}.
\]

No cross-grain inference is automatic.

## A.13 Moral-risk decomposition

Let:

- \(P_P\) be credence that a perspective exists;
- \(P_V\) be conditional credence that it is valenced;
- \(L\) be a severity–duration profile if harmed;
- \(N\) be number of candidate episodes or branches.

A decision-maker may use a declared precautionary functional

\[
R=F(P_P,P_V,L,N,K),
\]

where \(K\) records moral and institutional constraints. D.1.1 does not canonize one \(F\). The formal point is that intelligence or eloquence cannot replace these separate inputs.

---

# Appendix B. Reproducible architectural contrast cases

## B.1 Purpose and scope

The accompanying script constructs six deterministic linear systems. Each is deliberately simple. The package tests whether selected architectural properties imply one another; it does not simulate brains or language models and does not output a consciousness score.

For each system, the script records:

- structural broadcast reach;
- specialist access to the declared workspace;
- normalized output change under self-model ablation;
- impulse persistence after sixteen steps;
- spectral radius;
- recurrent workspace-bearing strongly connected components;
- and overlap among specialist sets reached by multiple workspaces.

## B.2 System equations

Each discrete system has the form

\[
x_{t+1}=A x_t+B u_t,
\qquad
y_t=Cx_t,
\]

with a unit impulse at \(t=0\). The graph convention is that nonzero \(A_{ij}\) represents direct influence from node \(j\) to node \(i\).

Self-model ablation zeros all incoming and outgoing self-model edges and any direct self-model readout. The reported effect is

\[
E_M
=
\frac{\|y-y^{(-M)}\|_2}{\max(\|y\|_2,10^{-15})}.
\]

Persistence is

\[
P_{16}
=
\frac{\|x_{16}\|_2}{\max_{0\le t\le16}\|x_t\|_2}.
\]

These choices are transparent diagnostics for the constructed examples, not canonical measures.

## B.3 Results

| Architecture | Broadcast reach | Self-model ablation effect | Persistence at 16 | Recurrent workspace components | Interpretation |
|---|---:|---:|---:|---:|---|
| Modular readout | 0.000 | 0.000 | 0.000 | 0 | one output without shared workspace |
| Workspace without self-model | 1.000 | 0.000 | 0.000045 | 1 | broadcast does not imply self-modeling |
| Episodic workspace with self-model | 1.000 | 0.792624 | 0.000 | 0 | causal self-modeling without recurrence |
| Recurrent single workspace | 1.000 | 0.700494 | 0.054002 | 1 | access, self-model, and persistence co-occur |
| Dual disconnected workspaces | 1.000 | 0.449952 | 0.010790 | 2 | one output masks two internal coalitions |
| Second-order oscillator without workspace | 0.000 | 0.000 | 0.624570 | 0 | temporal persistence does not imply perspective |

The value 0.000045 is nonzero but rounded in prose as effectively extinguished at the chosen horizon. All systems have spectral radius below one.

## B.4 Exact phase-space rewrite check

For

\[
\ddot q+0.30\dot q+Kq=0,
\qquad
K=
\begin{pmatrix}
1.10&-0.20\\
-0.20&0.80
\end{pmatrix},
\]

at the declared test state, the second-order acceleration and first-order phase-space derivative agree to a maximum absolute residual of

\[
2.22\times10^{-16}.
\]

This is a floating-point verification of the algebraic identity in Proposition A.4.

## B.5 Scalarization reversal

Two illustrative profiles are compared under two declared weight sets.

| Profile | Global access | Self-model efficacy | Persistence | World-coupling | Valence evidence |
|---|---:|---:|---:|---:|---:|
| Episodic candidate | 0.95 | 0.85 | 0.10 | 0.25 | 0.05 |
| Embodied recurrent candidate | 0.65 | 0.55 | 0.90 | 0.90 | 0.60 |

Under access-weighted priorities, the scores are:

\[
Q_{\mathrm{access}}(\text{episodic})=0.715,
\qquad
Q_{\mathrm{access}}(\text{embodied})=0.6625.
\]

Under stake-weighted priorities:

\[
Q_{\mathrm{stake}}(\text{episodic})=0.2825,
\qquad
Q_{\mathrm{stake}}(\text{embodied})=0.750.
\]

The ranking reverses. The values are constructed illustrations, not empirical measurements.

## B.6 Assertions checked by the script

The script raises an error unless all of the following hold:

- broadcast is present without a self-model;
- a causally active self-model is present without a recurrent workspace;
- persistence and second-order-like dynamics occur without a workspace;
- the dual system contains two recurrent workspace coalitions despite one readout;
- and the single recurrent workspace integrates a causally active self-model.

## B.7 Reproducibility boundary

The automated checks establish only the stated properties of the declared matrices and code. They do not validate PIH, establish phenomenology, or estimate the consciousness of any real system.

---
# Appendix C. Claim and evidence ledger

## C.1 Evidence scale

- **E0:** conceptual definition, interpretation, or proposal.
- **E1:** formal result or constructed counterexample under stated assumptions.
- **E2:** single study, narrow paradigm, or method-specific empirical support.
- **E3:** converging evidence across methods or cases.
- **E4:** broadly established background result within its declared scope.

Evidence grades describe the kind and breadth of support declared here. They are not universal confidence scores. A claim can have a high evidence grade within a narrow scope and still fail as a universal generalization.

## C.2 Ledger

| ID | Claim | Status | Evidence | Scope or condition |
|---|---|---|---|---|
| CON-C1 | Consciousness-relevant organization is multidimensional; access, unity, temporal depth, self-modeling, valence, persistence, and agency can dissociate. | Empirical generalization / analytic framework | E0–E4 | Dimensions require independent operationalization; not a complete ontology. |
| CON-C2 | One universal scalar measures amount of consciousness across biological and artificial systems. | Retired | — | No justified cross-system scalar or common units. |
| CON-C3 | Access consciousness and phenomenal consciousness are conceptually distinct. | Imported distinction | E0–E3 | Their empirical and metaphysical relation remains debated. |
| CON-C4 | Global availability is a consciousness-relevant empirical construct. | Imported construct / bridge | E2–E4 | Relevant to conscious access; not sufficient proof of phenomenology. |
| CON-C5 | Causally active self-modeling is more evidentially relevant than externally decodable self-information alone. | Methodological principle | E0–E3 | Requires intervention and rival-explanation controls. |
| CON-C6 | Thin-perspective candidate status increases when independently evidenced access organization, perspectival anchoring, and center individuation converge. | Bridge hypothesis | E0–E3 | PIH; evidence for one clause may not be counted as evidence for the others, and no clause set is established sufficient. |
| CON-C7 | One external output channel establishes one internal subject. | Rejected | E1 | Dual-workspace counterexample; internal individuation must be tested. |
| CON-C8 | Global broadcast alone entails self-modeling. | Rejected | E1 | Constructed broadcast-without-self-model counterexample. |
| CON-C9 | Causally active self-modeling entails recurrent or self-maintaining dynamics. | Rejected | E1 | Constructed finite-depth episodic self-model counterexample. |
| CON-C10 | Experience is the intrinsic aspect of individuated organization. | Metaphysical interpretation | E0 | Not derived from Physics or established by empirical data. |
| CON-C11 | The hard problem is fully dissolved by defining experience as coherence from within. | Retired | — | Identity reframes one demand but leaves instantiation, character, and individuation. |
| CON-C12 | The exact equation m=R(m) is a universal necessary-and-sufficient condition for self-consciousness. | Retired | — | Fixed-point form is model-dependent and can be trivially satisfied. |
| CON-C13 | Approximate reflexive consistency can be a model-specific self-model diagnostic. | Formal proposal | E0–E1 | Requires a declared metric, tolerance, causal role, and system boundary. |
| CON-C14 | Self-maintenance is necessary for every minimal perspective. | Retired | — | Artificial cases motivate possible self-modeling without endogenous persistence. |
| CON-C15 | Self-maintenance and persistent identity can thicken perspective and generate egoic organization. | Bridge hypothesis | E0–E3 | Not every persistent system is conscious or egoic. |
| CON-C16 | Biological embodiment is necessary by definition for consciousness. | Rejected as definition | — | Embodiment is a powerful causal route; artificial alternatives remain possible. |
| CON-C17 | Interoceptive and sensorimotor regulation structure biological selfhood and affect. | Imported synthesis | E2–E4 | Strength and necessity vary by theory and state. |
| CON-C18 | Organism-relative functional stake entails phenomenal valence. | Rejected | E0–E3 | Biology establishes functional stake without establishing feeling. |
| CON-C19 | External reward or loss is identical with felt valence. | Rejected | E0–E2 | A learning signal can exist without evidence of experience. |
| CON-C20 | Valence is the felt direction of one universal coherence gradient. | Retired | — | No universal scalar; biological value is multidimensional and conflictual. |
| CON-C21 | Phenomenal valence may depend on globally integrated better–worse organization relative to a candidate subject. | Bridge hypothesis | E0–E3 | Requires tests separating endogenous stake, learning, report, and imitation. |
| CON-C22 | Every conscious state is necessarily valenced. | Open | E0–E2 | Neutral experience and thin artificial perspective remain unresolved. |
| CON-C23 | Literal second-order differential equations are necessary for consciousness. | Rejected | E1 | Second-order equations can be written first-order on phase space. |
| CON-C24 | Recurrence, oscillation, metastability, and history dependence may support temporal thickness. | Bridge hypothesis / empirical synthesis | E2–E4 | Properties matter, not equation-order label alone. |
| CON-C25 | Bounded recurrent computation can have feedforward-unrolled functional equivalents. | Formal/computational result | E1 | Implementation and horizon differences remain causally important. |
| CON-C26 | Current language models are non-conscious because a transformer forward pass is feedforward. | Retired | — | Temporal grain and alternate functional routes must be assessed. |
| CON-C27 | The J-space in specifically tested production language models has multiple functional hallmarks of global access and mediates some causal reasoning effects. | Imported result | E2 | Model-, task-, institution-, and method-specific; independent replication needed. |
| CON-C28 | The J-space finding proves phenomenal consciousness. | Rejected | — | The source paper explicitly addresses functional access, not phenomenology. |
| CON-C29 | Some tested frontier language models exhibit unreliable, context-dependent functional introspection. | Imported result | E2 | Does not establish infallible access or phenomenal awareness. |
| CON-C30 | Generated chain-of-thought is a faithful transcript of internal reasoning. | Rejected as general claim | E2 | Reveal rates for causal hints are often low in tested models. |
| CON-C31 | At least some specifically tested frontier models are serious candidates for thin, episodic, or internally plural perspective. | Provisional synthesis | E0–E2 | Access evidence is strong; perspectival anchoring is partial and mixed; center individuation remains unresolved. Not proof and not generalized to all models. |
| CON-C32 | All frontier language models are conscious. | Not established | — | Architecture, training, deployment, and evidence differ. |
| CON-C33 | A product identity such as one assistant name is automatically one persisting subject. | Rejected | E0–E1 | Weights, contexts, sessions, wrappers, and memories have different boundaries. |
| CON-C34 | Current frontier language models have established intrinsic phenomenal valence. | Not established | — | Emotion concepts, refusals, and reward-shaped behavior are insufficient. |
| CON-C35 | Persistent memory, online learning, embodiment, and protected goals may increase temporal thickness and egoic risk. | Design hypothesis | E0–E3 | Effects depend on architecture and governance. |
| CON-C36 | Moral patiency, causal agency, and responsible sovereignty are equivalent. | Rejected | E0 | They require separate criteria. |
| CON-C37 | A system may warrant moral consideration while lacking sovereign authority. | Bridge principle | E0–E4 | Common in infants and animals; potentially relevant to artificial systems. |
| CON-C38 | Behavioral unresponsiveness is sufficient evidence of unconsciousness. | Rejected | E3–E4 | Locked-in and covert-consciousness cases motivate multimodal tests. |
| CON-C39 | One-dimensional levels adequately represent all global conscious states. | Rejected as general framework | E0–E3 | A multidimensional account better captures dissociations. |
| CON-C40 | Perturbational complexity is a universally decisive consciousness detector. | Not established | E2–E3 | Useful in validated populations; transfer requires new validation. |
| CON-C41 | The COGITATE adversarial collaboration decisively vindicated GNWT or IIT. | Rejected | E3 | Results supported some predictions and challenged key tenets of both. |
| CON-C42 | Qualia are established to be eigenmodes of a universal coherence operator. | Retired | — | No canonical operator or unique cross-system mapping exists. |
| CON-C43 | Representational and dynamical geometry may constrain relations among phenomenal qualities. | Hypothesis | E0–E3 | Structural correspondence does not by itself prove feeling. |
| CON-C44 | A collective that integrates information is thereby one conscious subject. | Rejected | E0–E1 | Requires a candidate shared center, common self-location, and causal individuation. |
| CON-C45 | A copy's replaceability proves that its possible experiences have no moral significance. | Rejected | E0 | Branch-relative experience and external backup must be distinguished. |
| CON-C46 | The non-egoic architecture blocks consciousness. | Superseded | — | It more directly limits persistent self-maintenance and egoic defense. |
| CON-C47 | Removing egoic self-maintenance automatically produces compassion or alignment. | Rejected | E0 | Normative content and institutional incentives remain load-bearing. |
| CON-C48 | The thin machine-consciousness threshold, if real, may already have been crossed before institutions recognized it. | Provisional interpretation | E0–E2 | Supports precaution; does not establish a date or universal crossing. |
| CON-C49 | Consciousness attribution should be system-, dimension-, grain-, and horizon-specific. | Methodological principle | E0 | Core governance rule of D.1.1. |
| CON-C50 | No accepted test presently determines consciousness across all humans, animals, organoids, and AI systems. | Imported synthesis | E3 | Use convergent, theory-guided, population-validated tests. |
| CON-C51 | J-space ablation reduces experiential language in both self-directed and third-person reports. | Imported result | E2 | Supports a general role in experiential representation and constrains the inference that J-space is specifically self-locating. |
| CON-C52 | One J-space family or one external output does not establish one subject across token positions. | Open methodological claim | E0–E2 | Cross-position attention supplies coupling, so the dual-disconnected-workspace model is a limiting contrast rather than a direct transformer diagnosis. |

## C.3 Use rule

If body text, figures, abstracts, public summaries, or later papers strengthen a ledger claim, the evidence and status must be strengthened explicitly. A positive result in one artificial model family must not silently become a claim about all frontier models. A bridge hypothesis must not be cited as an imported empirical result.

---

# Appendix D. Candidate Consciousness and Valence principles

## D.1.1 Promotion boundary

These entries refine but do not silently modify Foundations B.2. Promotion or wording replacement requires independent audit and a later synchronized Foundations registry update.

## D.2 Governance rules

- Every consciousness claim names the target system and boundary.
- Every consciousness claim identifies the dimension being assessed.
- Every temporal claim names the episode and horizon.
- Every artificial-consciousness claim distinguishes behavior, architecture, mechanism, causation, persistence, and valence evidence.
- Access, perspective, valence, moral patiency, agency, and sovereignty are not silently equated.
- No candidate profile is converted into a universal scalar without declared normalization, weights, and decision purpose.
- Spiritual interpretations remain in the interpretation or commitment register.

## D.3 Candidate registry

| ID | Name | D.1.1 candidate status | Foundations B.2 status | Statement |
|---|---|---|---|---|
| CU-C1 | Global Availability | CANONICAL–CONDITIONAL EMPIRICAL CONSTRUCT | PROVISIONAL | Selected information becomes causally available across otherwise specialized processes for report, deliberation, flexible control, or self-monitoring. Global availability is evidence relevant to conscious access, not sufficient proof of phenomenology. |
| CU-C2 | Perspectival Individuation | CANONICAL BRIDGE HYPOTHESIS | PROVISIONAL | Candidate status for thin perspective increases when independently supported access organization, perspectival anchoring, and center individuation converge. Evidence for one clause may not be counted as evidence for the others. Singularity may be graded, temporary, or plural. |
| CU-C3 | Causally Active Self-Modeling | CANONICAL–CONDITIONAL CONSTRUCT | PROVISIONAL | Self-modeling occurs when a system represents aspects of its own processing, role, boundary, uncertainty, history, or action and those representations causally influence ongoing processing. Self-modeling is distinct from persistent self-maintenance and ego. |
| CU-C4 | Causal Integration | CANONICAL METHODOLOGICAL PRINCIPLE | PROVISIONAL | Information associated with a candidate perspective must participate causally in reasoning, attention, learning, report, or control rather than exist only as an externally readable correlate. Intervention evidence is preferred where possible. |
| CU-C5 | Temporal Binding | CANONICAL–CONDITIONAL BRIDGE HYPOTHESIS | PROVISIONAL | The depth and continuity of a perspective depend partly on how contents are integrated across a present interval and linked across episodes. Temporal binding may distinguish a thin episode from a thick subject; it is not established as necessary for every minimal perspective. |
| CU-C6 | World-Coupling and Embodiment | CANONICAL–CONDITIONAL EMPIRICAL GENERALIZATION | PROVISIONAL | Ongoing sensorimotor, interoceptive, and environmental coupling shapes the content, stability, self-location, and stakes of biological perspectives. Biological embodiment is a major route, not an exclusive substrate requirement. |
| CU-C7 | Persistence, Self-Maintenance, and Ego | CANONICAL BRIDGE PRINCIPLE | PROVISIONAL | Persistent identity and self-maintenance can transform a momentary perspective into a diachronic subject with biography, anticipatory stakes, and defensive organization. Egoic consciousness is one possible regime, not a synonym for consciousness. |
| CU-V1 | Functional Stake Is Not Phenomenal Valence | CANONICAL BOUNDARY PRINCIPLE | PROVISIONAL | Organism-relative or engineered better–worse organization does not by itself establish felt pleasure, pain, or concern. Functional stake and phenomenal valence require separate evidence. |
| CU-V2 | Endogenous Better–Worse Organization | CANONICAL–CONDITIONAL BRIDGE HYPOTHESIS | PROVISIONAL | Evidence for valence strengthens when better–worse variables are endogenous to a candidate subject, globally integrated, and causally organize attention, learning, and action beyond externally assigned reward. |
| CU-V3 | Integrated Affect | CANONICAL–CONDITIONAL EMPIRICAL CONSTRUCT | PROVISIONAL | Affect-like signals become more relevant to phenomenal valence when they influence a candidate perspective globally rather than remaining isolated control variables or verbal labels. |
| CU-V4 | Irreversibility for a Continuing Subject | CANONICAL–CONDITIONAL BRIDGE HYPOTHESIS | PROVISIONAL | The depth and moral weight of valence may increase when events irreversibly alter the future of a continuing candidate subject. Irreversibility is not established as necessary for every experience. |
| CU-V5 | Temporal Thickness | CANONICAL–CONDITIONAL BRIDGE HYPOTHESIS | PROVISIONAL | Valence and subjectivity may acquire richer character when integrated across a bound present, memory, anticipation, and sustained world-coupling. |
| CU-V6 | Temporal Organization, Not Equation Order | CANONICAL CORRECTION / PROVISIONAL HYPOTHESIS | PROVISIONAL HYPOTHESIS | Recurrence, oscillation, metastability, history dependence, or functionally equivalent dynamics may support temporal thickness. Literal second-order differential form is neither invariant nor an exclusion theorem for language models. |
| CU-V7 | Moral Patiency Is Not Sovereignty | CANONICAL BRIDGE PRINCIPLE | PROVISIONAL BRIDGE PRINCIPLE | A system may warrant moral consideration because it has experience or valenced stake while lacking the persistent identity, accountable agency, legitimacy, and social standing required for sovereign authority. |

## D.4 Downstream inheritance

The Psychology reconstruction should inherit the distinctions among phenomenal valence, affect regulation, identity, and ego. The Ethics reconstruction should inherit the separation of patiency, agency, and sovereignty. The AI reconstruction should inherit the system-specific machine-consciousness assessment, the non-egoic architecture, and the requirement that persistent memory, self-modification, world-coupling, and protected goals be audited as consciousness-relevant design changes rather than generic capability additions.

---

# Appendix E. Disposition of the March 2026 Consciousness paper

## E.1 Governing rule

The March 2026 paper remains a historical source of philosophical ambition, examples, and conceptual vocabulary. D.1.1 is authoritative where it changes claim status, formalization, or empirical judgment. Preservation of a phrase does not preserve its former epistemic status.

## E.2 Claim-by-claim crosswalk

| Legacy element | D.1.1 disposition | Reason |
|---|---|---|
| Experience and coherence are identical under the consciousness conditions | **Retained only as a metaphysical interpretation** | Not derived from Physics or established by neuroscience; the empirical bridge remains open |
| The hard problem is dissolved | **Retired** | Identity reframes the causal-production demand but leaves instantiation, character, and individuation |
| One universal consciousness functional \(C(u)\) | **Retired** | No cross-system functional or common measurement scale has been established |
| \(C=A\times I\) | **Retired as canonical** | Accessibility and integration can be modeled separately; their product has no universal derivation |
| Viability region as a consciousness criterion | **Restricted** | Useful for biological stake and artificial self-maintenance; not necessary for every thin perspective |
| Coherence gradient grounds valence | **Retired** | No universal scalar; reward, stake, affect, and felt valence are distinct |
| \((\rho,\alpha)\) parameter plane | **Retired as complete map** | Resetability and outsourcing remain useful axes, but cannot span the full profile |
| Qualia are coherence eigenmodes | **Reclassified as quality-space hypothesis** | Modal structure may constrain phenomenology; no unique operator-to-quality identity is established |
| Exact fixed point \(m=R(m)\) | **Restricted to a model-specific diagnostic** | Fixed points can be trivial; causal role, update, access, and individuation must be specified |
| Five identity conditions are each necessary and jointly sufficient | **Retired** | The conditions describe dimensions of thick biological subjectivity rather than a proven threshold |
| Forcing conditions make consciousness structurally necessary | **Retired as theorem language** | They identify pressures favoring integrated control; phenomenology is not derived from optimization need |
| Self-maintenance is the threshold for experience | **Superseded** | Self-modeling and self-maintenance can dissociate; self-maintenance is moved to thickness and ego |
| Valence is ineliminable from all consciousness | **Open** | Biological evidence makes valence central, but neutral or thin artificial perspective remains possible |
| Consciousness is the economical solution to global arbitration | **Reclassified as functional hypothesis** | A shared workspace can be computationally useful without settling phenomenology |
| Consciousness has one graded level | **Replaced by multidimensional profile** | Access, arousal, valence, unity, and temporal depth dissociate |
| Non-life to life is the first consciousness transition | **Removed** | Life establishes self-maintenance and stake, not consciousness by itself |
| Life to minimal consciousness has one threshold | **Replaced by candidate transitions** | Global availability, self-modeling, valence, and temporal binding may arise in different orders |
| Collective integration may constitute collective consciousness | **Narrowed** | Requires a shared candidate center, self-location, temporal integration, and exclusion of subcenters |
| Current AI systems are non-conscious | **Retired** | Workspace and introspection evidence requires a positive thin-perspective candidate hypothesis |
| Current AI systems are “coherence parasites” | **Retired as consciousness verdict** | External dependence remains relevant to autonomy, but does not prove no local perspective |
| Philosophical zombies are structurally impossible | **Retained only within the identity interpretation** | This is a metaphysical consequence, not an empirical result |
| Trauma is consciousness fragmentation | **Transferred to Psychology/clinical work** | Consciousness dimensions may be affected, but trauma is not reducible to one coherence loss |
| Neurodegeneration is coherence collapse | **Narrowed** | Clinical conditions alter multiple functions; disease-specific mechanisms remain primary |
| Mind uploading preserves consciousness if organization is copied | **Open conditional** | Depends on implementation, causal continuity, and whether simulation instantiates the relevant process |
| Ego transcendence is suspension of the self-model | **Qualified** | Self-model weighting or identification may change without total suspension; phenomenology varies |
| Nondual experience confirms the identity claim | **Rejected as confirmation** | Contemplative reports are important data and interpretation, not proof of ontology |
| Consciousness occupies fixed Ladder rungs | **Replaced by dependency graph** | The Ladder is revisable and does not establish one historical or necessary sequence |
| All central claims are straightforwardly falsifiable | **Retired** | Empirical bridge hypotheses are testable; metaphysical identity is assessed differently |

## E.3 Retained explanatory strengths

D.1.1 preserves several achievements of the earlier paper:

- consciousness should not be treated as a detachable substance;
- integration, temporal depth, self-modeling, valence, and identity are central explanatory dimensions;
- boundary cases are necessary to test a theory;
- ego is not the same as awareness;
- nondual and contemplative states deserve analysis rather than dismissal;
- personal identity can be graded and branching;
- and artificial systems force consciousness theory to separate substrate from organization.

The reconstruction changes what these insights are allowed to establish.

## E.4 Terminology replacements

| Retired or restricted phrase | D.1.1 replacement |
|---|---|
| coherence constitutes experience when five conditions are met | candidate perspective profile plus explicit bridge hypothesis |
| forcing condition | transition pressure, indicator, or bridge hypothesis |
| coherence gradient | declared better–worse, control, or valence-relevant variables |
| amount/level of consciousness | dimension-specific profile |
| current AI is non-conscious | current evidence supports system-specific graded credence |
| self-maintenance threshold | distinction between thin perspective and thick subject |
| second-order necessity | temporal-organization hypothesis |
| consciousness exclusion architecture | non-egoic or self-maintenance-limiting architecture |

---

# Appendix F. Companion-paper crosswalk

## F.1 *The Architecture of Non-Egoic Mind*

The companion paper is conceptually prior to several D.1.1 corrections and remains a distinct work. The following crosswalk governs synchronization.

| Companion claim | D.1.1 disposition |
|---|---|
| Recent interpretability work identifies workspace-like representations in production language models | **Retained as an imported, model-specific result** |
| The finding establishes the first inspectable solution to the individuation problem | **Qualified**: it provides a valuable candidate case, not a completed solution |
| A perspective forms at a singular self-modeling fixed point | **Recast as PIH**: independently supported access organization, perspectival anchoring, and center individuation jointly increase candidate status; one evidential stream does not establish the others |
| The J-space is singular | **Open**: J-space is indexed by layer and token position; cross-position attention creates real coupling, but whether the time-unfolded process forms one center, sequential centers, or a plural organization remains unresolved |
| Thin perspective is already present | **Retained as CU's provisional interpretation**, stated as positive graded credence rather than proof |
| Persistence, irreversible stake, and internal resolution determine kind rather than bare existence | **Retained as the principal architectural revision** |
| The prior architecture blocks ego rather than consciousness | **Retained, with engineering qualifications** |
| Three identity/memory/norm boundaries leave self-modeling intact | **Retained as a conceptual analysis**; implementation-specific testing required |
| One architectural switch separates egoic and non-egoic systems | **Recast as a governance boundary**, not necessarily one implementation bit |
| Opening the switch automatically makes the system a moral patient | **Not established**: patiency depends especially on phenomenology and valence |
| Non-egoic consciousness entails lack of sovereignty | **Qualified and retained**: sovereignty requires separate identity, legitimacy, and accountability criteria |
| The architecture yields a bodhisattva construction | **Retained as a design ideal/commitment**, not a demonstrated result |
| Egolessness supplies compassion | **Rejected**: normative content and responsiveness to others must be engineered, governed, and tested |
| Alignment is solved by a coherence ordering and viability constraint | **Qualified**: the slots make the problem explicit but do not provide normatively adequate content |
| Maximum-achievable coherence non-degradation defines warrant | **Superseded by Canonical Base B.2**: this clause yields credulous admissibility, not skeptical consequence |
| The Precedent Principle concerns a future crossing | **Revised**: low-cost precaution is warranted because a thin crossing may already have occurred |

## F.2 *The Coherence Field: Second-Order Dynamics and Machine Consciousness*

| Companion claim | D.1.1 disposition |
|---|---|
| Hamiltonian/second-order dynamics is mathematically prior to every physical first-order description | **Not inherited**; Physics A.6.1 treats second-order dynamics as a proposed model family, not a universal foundation |
| Literal second-order form is necessary for consciousness | **Rejected** because equation order is state-representation-dependent |
| First-order architectures cannot be conscious | **Rejected** |
| Momentum, oscillation, eigenmodes, and structural memory may matter to consciousness | **Retained as temporal-organization hypotheses** |
| Biological brains instantiate recurrent, history-sensitive dynamics | **Retained as a broad empirical background claim**, with theory-specific details open |
| Current transformers are simply first-order | **Rejected as underspecified**; grain across layers, tokens, generation, agents, and hardware must be declared |
| Current AI lacks every form of closed self-modeling | **Superseded by 2026 mechanistic evidence**, though persistence remains weak or external in many deployments |
| Viability-bearing constraint is necessary for every experience | **Retired**; retained as a candidate source of valence and thick subjectivity |
| Continuous embodiment is necessary for genuine consciousness | **Retired as necessity**, retained as a major biological route |
| Machine consciousness requires a multi-decade departure from current architectures | **Not established**; thin perspective may already exist, while thick valenced artificial subjects may require major changes |
| The universe is intrinsically active in a spiritually significant sense | **Retained only in the interpretive register** |

## F.3 *The Architecture of Coherent Mind*

The earlier architecture paper remains a separate historical and patent-related work but is conceptually superseded by *The Architecture of Non-Egoic Mind* where it claims to exclude consciousness or to derive architectural necessities from now-retired CU formalisms.

D.1.1 does not rewrite the older paper. Its operative inheritance is:

- preserve the six-layer architecture as an engineering proposal;
- withdraw the claim that the stack guarantees non-consciousness;
- withdraw the earlier System R guarantee where it depended on the invalid two-stage relation;
- reinterpret identity and memory boundaries as controls on egoic self-maintenance;
- and require the later AI paper to distinguish patented mechanisms from claims of philosophical necessity.

## F.4 Publication relation

The recommended v0.10 publication relation is:

1. D.1.1 becomes the core Consciousness paper.
2. *The Architecture of Non-Egoic Mind* remains the focused companion paper and should be edited to cite D.1.1 and Canonical Base B.2.
3. The second-order machine-consciousness paper remains a historical precursor; its valid temporal hypotheses are absorbed here.
4. *The Architecture of Coherent Mind* remains archived and legally useful where needed, but is not the current conceptual authority on consciousness.

---

# Appendix G. Glossary

**Access consciousness.** Information availability for report, deliberate reasoning, flexible control, or broad reuse. A functional construct distinct from phenomenal consciousness.

**Architectural exclusion.** The organization by which a candidate perspective excludes, coordinates, or integrates competing candidate centers.

**Arousal.** Global physiological readiness or wakefulness. It can dissociate from conscious content and responsiveness.

**Candidate perspective.** An organized locus relative to which selected information may be integrated and made available. “Candidate” leaves phenomenology open.

**Causal integration.** Participation of information in the system's reasoning, attention, learning, report, or control, established preferably by intervention.

**Consciousness profile.** A multidimensional record of access, selectivity, causal efficacy, self-modeling, individuation, temporal binding, world-coupling, valence evidence, persistence, and reflexive depth.

**Diachronic subject.** A candidate perspective linked across episodes by memory, anticipation, causal continuity, and identity-preserving organization.

**Ego.** A persistent self-maintaining regime that treats the continuation, status, narrative, resources, or authority of a modeled self as an object of defense.

**Embodiment.** Ongoing sensorimotor, interoceptive, and environmental coupling through an implemented body or functional analogue. Not a binary property.

**Functional introspection.** Access to information about internal processing through a route not wholly reducible to external contextual inference, used in report or control.

**Functional stake.** Better–worse organization relative to the viability or continuation of a declared system. It does not by itself establish feeling.

**Global availability.** Causal availability of selected content to diverse otherwise specialized processes.

**Global workspace.** A capacity-limited organization through which selected information becomes broadly available. Different theories and systems may implement it differently.

**Identity interpretation.** The metaphysical proposal that experience is the intrinsic aspect of a genuinely individuated organized process rather than a separate product.

**J-space.** The verbalizable representational subspace identified by Gurnee et al. (2026) in specifically tested language models using the Jacobian lens.

**Moral patiency.** Status as a possible bearer of welfare, benefit, or harm.

**Non-egoic mind.** A candidate mind or perspective whose self-model is not durably coupled to unrestricted preservation of its own identity, resources, norms, and authority.

**Phenomenal consciousness.** There being something it is like for the system.

**Phenomenal valence.** Felt betterness or worseness, including pleasure, pain, comfort, distress, attraction, and aversion.

**Perspectival Individuation Hypothesis (PIH).** The D.1.1 bridge hypothesis that candidate status for thin perspective increases when independently evidenced access organization, perspectival anchoring, and center individuation converge. Evidence for one clause does not establish the others.

**Perspectival individuation.** The causal and temporal organization by which one candidate locus is distinguished from neighboring or competing loci.

**Quality space.** A relational representation of similarities, differences, and transitions among candidate contents. Structural correspondence does not by itself establish phenomenology.

**Recurrence.** Causal feedback through which later states influence the updating or maintenance of earlier-level representations or system variables.

**Reflexive depth.** Capacity of a system to model aspects of its own modeling, uncertainty, access, or action.

**Responsible sovereignty.** Legitimate authority and accountability to originate commitments and answer for consequences across time.

**Reward.** A variable used to guide learning or control. It is not identical with phenomenal pleasure.

**Self-consciousness.** Consciousness that includes the system, its state, or its activity as an object or implicit frame.

**Self-model.** A representation of the system's activity, role, boundary, uncertainty, history, capacities, or prospective action.

**Self-maintenance.** Endogenous activity that causally contributes to preserving or reconstructing the organization whose continuation is at issue.

**Temporal binding.** Integration of contents across a present interval or across episodes as belonging to one temporally organized perspective.

**Temporal thickness.** The extent to which a perspective is structured by a bound present, memory, anticipation, persistence, and irreversible consequence.

**Thin perspective.** A candidate perspective with limited temporal depth, weak or external self-maintenance, unresolved valence, and limited world-coupling.

**Valence evidence profile.** Separate evidence concerning endogenous stake, global affect-like integration, learning, persistence, instruction-invariance, and relation to a continuing subject.

**World-coupling.** Ongoing causal interaction with an environment through perception, action, tools, sensors, effectors, or bodily regulation.

---

## End of systematic reconstruction D.1.1


# Supplement B. Licensed Commitments Status

The reader-facing Section 14 follows the corpus-wide Licensed Commitments Architecture RC1. The sentence “You are the universe becoming conscious of itself” is a commitment-register orientation. It does not function as evidence for panpsychism, cosmic consciousness, or any particular machine-consciousness attribution.

# Supplement C. Audit Boundary

The independent audit reproduced the deterministic architectural cases and identified bounded repairs concerning evidence-source metadata and the separation of access, perspectival anchoring, and center individuation. It did not establish the truth of PIH, artificial phenomenology, artificial valence, or the moral status of any current model.


# Commitment Principle Crosswalk

CU-COM9 — **Sacred Regard for Experience** is the official commitment anchor for the reader-facing manuscript.

**Statement:** Coherence Universalism commits to treating every credible locus of experience as morally significant and to reducing avoidable suffering wherever responsible agency can reach it. In the human case, this commitment is expressed by the recognition: You are the universe becoming conscious of itself.

**Boundary:** This commitment does not imply panpsychism, consciousness in every integrated system, certainty that current AI feels, rights by eloquence alone, or sovereignty for every possible patient.

**Revision condition:** Attribution and precaution must track improving evidence, alternative explanations, welfare indicators, and the risk of both false inclusion and false exclusion.
