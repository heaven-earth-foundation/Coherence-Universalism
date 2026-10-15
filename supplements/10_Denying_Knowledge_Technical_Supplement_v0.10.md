# Denying Knowledge to Make Room for Commitment
## RC3 Release-Convergence Wave 4 — Technical Supplement

**Status and authority.** This is the released technical supplement for the Wave 4 cumulative manuscript. The [reader-facing manuscript](../papers/10_Denying_Knowledge_v0.10.md) controls current wording, claim status, and canonical cross-references. This supplement exposes the formal derivations, deterministic contrast constructions, claim ledgers, audit materials, scripts, and source records on which the manuscript relies.

- **Evidence directory:** [10_Denying_Knowledge](../evidence/10_Denying_Knowledge/README.md)
- **Archived source package:** [CU_Denying_Knowledge_v0.10_Publication_PC3.zip](../provenance/archival_source_packages/CU_Denying_Knowledge_v0.10_Publication_PC3.zip)
- **Current supplement path:** `technical_supplements/10_Denying_Knowledge_Technical_Supplement_v0.10.md`

Reproducibility of a construction shows only that its output follows from its declared assumptions and code. It does not convert a toy model or simulation into target-domain empirical validation. Where this preserved archive uses historical identifiers or statuses, the Wave 4 normalized registries and current manuscript control.

# Wave 4 evidence-access addendum

Wave 4 makes previously referenced but inaccessible materials available in one package. It includes the substantive legacy supplement below, the independent audit and check script, recorded audit output where available, source ledgers, deterministic scripts and generated results where they existed, and the complete pre-RC3 source package for provenance.

# Preserved substantive technical archive

## Version 0.10 Publication Candidate 2 — Technical Supplement

**Gaura Kiśora Dās Rader**  
**Heaven≡Earth Foundation**  
**September 2026**

---

## Purpose and authority

This supplement records the formal architecture, audit dispositions, countermodels, case safeguards, bibliography normalization, and source-to-publication history supporting *Denying Knowledge to Make Room for Commitment*, Version 0.10 Publication Candidate 2.

The reader-facing paper is the principal publication manuscript. This supplement is the place to inspect assumptions that would overburden its argumentative flow. It distinguishes:

- imported nonmonotonic-logic results;
- elementary set-theoretic consequences;
- finite regression checks;
- adopted semantic conventions;
- philosophical theses;
- practical governance proposals;
- and open problems.

The independent audit recommended adoption with bounded repairs. Its decisive finding was not that the fixed-base formal architecture had failed, but that the paper had located its novelty at the wrong level. Preferential consequence presupposes a language with stable satisfaction or realization conditions; it does not itself solve the compositional problem associated with Frege–Geach. Publication Candidate 2 accepts that result and narrows the thesis accordingly.

---

# 1. Three levels that must not be conflated

The revised paper distinguishes three analytical levels.

## 1.1 Content and realization

Let \(L_D\) be a descriptive language with truth-satisfaction relation \(\vDash_D\), and let \(L_R\) be a representable commitment fragment with realization relation \(\Vdash_R\).

For descriptive content:

\[
w\vDash_D\alpha
\]

means that descriptive proposition \(\alpha\) is true at world, state, or trajectory \(w\).

For commitment content:

\[
w\Vdash_R\varphi
\]

means that \(w\) realizes, supports, or instantiates commitment content \(\varphi\) under the declared interpretation.

This notational separation prevents the same satisfaction sign from silently doing two different philosophical jobs. It does not by itself establish that descriptive and commitment contents belong to disjoint semantic species. Publication Candidate 2 adopts a more modest position: stable proposition-like content may appear in both registers, while speech-act force, principal function, and standard of assessment differ.

## 1.2 Defeasible consequence

Given stable realization conditions, preferential consequence asks which commitment contents hold throughout the best viable realizations compatible with the premises.

This is a metalinguistic relation over an already interpreted language. It is not the meaning of an object-language conditional, promise, vow, imperative, prayer, or religious expression.

## 1.3 Practical adoption

Practical expansion warrant asks whether an agent or institution may responsibly adopt a commitment after considering:

- descriptive facts and uncertainty;
- protected floors;
- affected parties;
- distributions of benefit and burden;
- option-set adequacy;
- power and authority;
- reversibility;
- independent challenge;
- exit;
- and revision conditions.

The KLM structure does not provide this normative or institutional content.

---

# 2. Representable commitment contents

## 2.1 Boolean-closed fragment

The complete System P claim applies only to a fragment \(L_R\) closed under the Boolean operations used by the theorem. For formulas \(\varphi,\psi\in L_R\):

\[
\llbracket\neg\varphi\rrbracket_R
=
W\setminus\llbracket\varphi\rrbracket_R,
\]

\[
\llbracket\varphi\land\psi\rrbracket_R
=
\llbracket\varphi\rrbracket_R\cap\llbracket\psi\rrbracket_R,
\]

\[
\llbracket\varphi\lor\psi\rrbracket_R
=
\llbracket\varphi\rrbracket_R\cup\llbracket\psi\rrbracket_R.
\]

The **Or** rule depends on the final clause. Where the objects under consideration are unformalized sets of practices, rituals, identities, or commitments and no disjunction has been defined, the full System P theorem is not claimed.

## 2.2 Adopted stable-content assumption

The formalism assumes that the contents represented in \(L_R\) remain stable across assertion, negation, conjunction, conditional embedding, and premise use.

That assumption is not derived by the preferential layer. Assigning a content an extension supplies exactly the stability that the Frege–Geach problem asks an expressivist semantics to explain. The paper therefore does not claim to solve Frege–Geach while preserving a semantics that denies proposition-like content. It adopts stable realization conditions for a declared fragment and asks what defeasible consequence structure follows once those conditions are available.

## 2.3 Residue outside the formalization

The following may be meaningful without possessing a complete representation in \(L_R\):

- ritual performance;
- prayer;
- lament;
- blessing;
- myth;
- poetry;
- embodied contemplative practice;
- first-person avowal;
- indexical or context-bound utterance;
- and forms of communal participation whose content cannot be separated from their enactment.

“Outside this formalization” does not mean meaningless. It means that the present KLM results do not apply until an adequate representational bridge has been supplied.

---

# 3. Fixed-base preferential models

Let:

\[
M=(W,V_F,\prec,\Vdash_R)
\]

be a declared preferential model.

- \(W\) is a set of worlds, states, or trajectories.
- \(F\) is the established descriptive background.
- \(K\) is the protected-constraint set.
- \(A\) is the affected-agent scope.
- \(H\) is the temporal horizon.
- \(V_F\equiv V_{F,K,A,H}\subseteq W\) is the fixed viability base.
- \(\prec\) is a fixed strict preference relation.
- \(\Vdash_R\) interprets the representable commitment language.

For a finite premise theory \(\Gamma\subseteq L_R\):

\[
W_{F,\Gamma}
=
V_F\cap\operatorname{Mod}_R(\Gamma).
\]

Let:

\[
B(F,\Gamma)
=
\operatorname{Min}_{\prec}(W_{F,\Gamma}).
\]

Premises filter a fixed base by intersection. They do not silently alter protected floors, affected-agent scope, horizon, viability criterion, or ordering.

## 3.1 System P

Define the underlying skeptical relation:

\[
\Gamma\sim_C\varphi
\quad\Longleftrightarrow\quad
\operatorname{Min}_{\prec}
\bigl(V_F\cap\operatorname{Mod}_R(\Gamma)\bigr)
\subseteq
\llbracket\varphi\rrbracket_R.
\]

On the relevant definability domain, smooth preferential models yield the KLM System P rules:

- Reflexivity;
- Left Logical Equivalence;
- Right Weakening;
- And;
- Or;
- Cautious Monotony;
- Cut.

This is an imported theorem applied to the declared formal structure. The finite regression suite protects the implementation from accidental drift; it is not a proof of the representation theorem.

## 3.2 Ranked models and Rational Monotony

When the preference is ranked and every relevant nonempty definable set attains a minimum rank, Rational Monotony is supported:

\[
\alpha\sim_C\beta
\text{ and }
\alpha\not\sim_C\neg\gamma
\quad\Longrightarrow\quad
\alpha\land\gamma\sim_C\beta.
\]

Minimum attainment is explicit. A total ordering of ranks is not sufficient if relevant infima are never attained.

## 3.3 Fixed-base control and premise-responsive failure

A premise-responsive selection rule may recompute viability after a premise is added:

\[
V(F,\Gamma\cup\{\varphi\})
\neq
V(F,\Gamma)\cap\operatorname{Mod}_R(\varphi).
\]

Such a relation need not satisfy Cautious Monotony. The regression package contains:

1. a three-world countermodel in which Cautious Monotony fails under non-intersective recomputation;
2. a control using the same worlds and ordering under a fixed base, where the failure disappears.

The paired exhibit isolates premise-responsive model change as the cause.

---

# 4. Five practical verdicts

## 4.1 Strong warrant

\[
F,\Gamma\models_C^{\forall}\varphi
\quad\Longleftrightarrow\quad
B(F,\Gamma)\neq\varnothing
\land
B(F,\Gamma)\subseteq\llbracket\varphi\rrbracket_R.
\]

Every best viable realization supports the commitment.

## 4.2 Admissibility and mere admissibility

\[
F,\Gamma\models_C^{\exists}\varphi
\quad\Longleftrightarrow\quad
B(F,\Gamma)\neq\varnothing
\land
B(F,\Gamma)\cap\llbracket\varphi\rrbracket_R\neq\varnothing.
\]

Admissibility includes strong warrant. **Mere admissibility** is the strict middle case:

\[
B(F,\Gamma)\cap\llbracket\varphi\rrbracket_R\neq\varnothing
\quad\text{and}\quad
B(F,\Gamma)\nsubseteq\llbracket\varphi\rrbracket_R.
\]

At least one best realization supports the commitment, and at least one does not.

Credulous admissibility fails **And**. Two tied best worlds may separately support \(\varphi\) and \(\psi\) while no best world supports \(\varphi\land\psi\).

## 4.3 Exclusion

\[
F,\Gamma\models_C^{\bot}\varphi
\quad\Longleftrightarrow\quad
B(F,\Gamma)\neq\varnothing
\land
B(F,\Gamma)\cap\llbracket\varphi\rrbracket_R=\varnothing.
\]

No best viable realization supports the commitment.

Within the adopted classical Boolean fragment:

\[
F,\Gamma\models_C^{\bot}\varphi
\quad\Longleftrightarrow\quad
F,\Gamma\models_C^{\forall}\neg\varphi.
\]

This extensional duality is a simplifying semantic choice. It can flatten a practical distinction between “the commitment is absent from every best realization” and “ceasing the practice is positively undertaken.” A non-classical account of commitment negation may preserve that distinction, but it lies outside Publication Candidate 2.

## 4.4 Infeasibility

A case is infeasible within the declared model when:

\[
W_{F,\Gamma}=\varnothing.
\]

No premise-compatible viable realization survives. Infeasibility is not underdetermination and not permission by default.

## 4.5 Underdetermination

A case is underdetermined when premise-compatible possibilities remain but the model cannot responsibly return a verdict. Sources include:

- failure of minimum attainment in an infinite model;
- an ordering too incomplete for the intended decision;
- unsettled descriptive facts;
- incomplete affected-agent scope;
- omitted options;
- disputed protected floors;
- unresolved model comparison;
- or uncertainty too large for the practical stakes.

Underdetermination is a demand for inquiry, caution, reversible action, or transparent cross-model disagreement.

---

# 5. Finite regression results

The deterministic suite examines all nineteen strict partial orders on three labeled worlds.

## 5.1 System P

The suite evaluates 390,336 finite rule instances and finds no violation of the tested System P rules under fixed-base intersective filtering.

## 5.2 Rational Monotony

The ranked-model suite evaluates 110,592 finite cases. Because the models are finite, every relevant nonempty set attains a minimum.

## 5.3 Verdict partition

Across 9,728 complete finite cases:

| Verdict | Count | Share |
|---|---:|---:|
| Strong warrant | 2,665 | 27.4% |
| Mere admissibility | 294 | 3.0% |
| Exclusion | 2,665 | 27.4% |
| Infeasible | 4,104 | 42.2% |
| Underdetermined | 0 | 0% |

The independent audit initially described the 4,104 no-best-set cases as a mixture of infeasibility and underdetermination. The revised suite makes a useful correction. In a finite strict partial order, every nonempty candidate set has a minimal element. Therefore every empty-best-set case in this particular regression is caused by an empty candidate set and is exactly **infeasible**. Underdetermination is conceptually essential but is not generated by these complete finite models; the suite tests it through a separate model-adequacy guard.

## 5.4 Non-singleton best-set stratum

The middle verdict cannot occur when the best set is a singleton. To protect the paper’s central distinction, Publication Candidate 2 adds a targeted stratum containing every evaluated model configuration with at least two best worlds:

| Quantity | Result |
|---|---:|
| Non-singleton best-set configurations | 73 |
| Commitment-content cases | 584 |
| Strong warrant | 145 |
| Mere admissibility | 294 |
| Exclusion | 145 |

Every middle-verdict case in the complete finite enumeration occurs in this stratum.

## 5.5 Scope

The regression results establish internal consistency of the finite implementation. They do not show that the middle verdict is empirically frequent, socially important, or uniquely modeled by this architecture. Its practical importance rests on the conceptual difference between:

> every best way of inhabiting the background supports this commitment

and:

> at least one best way supports it.

---

# 6. The maximum-preservation correction

The original draft asked whether restricting the feasible set by adding \(\varphi\) preserved or increased the maximum achievable score:

\[
\max_{S\cap\llbracket\varphi\rrbracket_R} C
\ge
\max_S C.
\]

Because:

\[
S\cap\llbracket\varphi\rrbracket_R\subseteq S,
\]

the restricted maximum cannot exceed the original maximum. If maxima are attained, equality holds exactly when at least one old maximizer realizes \(\varphi\):

\[
\operatorname{Argmax}_S C
\cap
\llbracket\varphi\rrbracket_R
\neq\varnothing.
\]

This is credulous admissibility, not skeptical consequence.

The correction preserves the original intuition that some commitments remain available without being compulsory. It removes the stronger claim that the old clause itself supplied System P consequence.

---

# 7. Transformative commitments and model revision

## 7.1 Trajectory lifting

Let worlds be trajectories \(\omega\in\Omega\). A trajectory may contain:

- temporary destabilization;
- grief;
- loss of role;
- a bounded decline in functioning;
- changed relationships;
- new support;
- later recovery;
- acquired capacities;
- and foreclosed possibilities.

The fixed-base form becomes:

\[
W^{\Omega}_{F,\Gamma}
=
V_F^{\Omega}
\cap
\operatorname{Mod}^{\Omega}_R(\Gamma).
\]

The proposition representing adoption selects trajectories on which the commitment is adopted. The trajectory-level viability predicate evaluates the whole path.

## 7.2 Trough-sensitive evaluation

No universal scalar trajectory score is canonized. Applications may use:

- protected floors;
- vector profiles;
- lexicographic orderings;
- partial orders;
- discounted profiles;
- robust comparison across model sets.

Temporary suffering is not free merely because a later endpoint is favorable. Nor does every temporary loss of integration make transformation unwarranted.

## 7.3 Model revision disclosure

If an analyst changes:

- protected floors;
- affected-agent scope;
- horizon;
- viability criterion;
- ordering;
- option set;
- or realization semantics,

then the evaluation model has changed.

The change must be declared, dated, and justified. A verdict in model \(M_0\) does not inherit authority in model \(M_1\) without a bridge argument. This is a central safeguard against commitments that redefine harm, agency, or viability whenever they are challenged.

---

# 8. Practical expansion warrant and model capture

The formal relation is model-relative. It cannot by itself determine whether the model is normatively legitimate or institutionally trustworthy.

Let practical adoption review be represented schematically by:

\[
\mathcal W_C
(\varphi\mid F,\Gamma,K,H,A,M,U,G),
\]

where:

- \(M\) is the model or model set;
- \(U\) is the presented and feasible option structure;
- \(G\) is the governance and challenge structure.

A complete disclosure should identify:

| Field | Required question |
|---|---|
| Descriptive base | Which facts and uncertainties constrain the case? |
| Existing commitments | What is already operative? |
| Protected floors | What may not be traded away? |
| Affected scope | Who bears consequences, including omitted and future parties? |
| Horizon | Over what period are trajectories assessed? |
| Option set | Who generated and excluded alternatives? |
| Ordering | How are viable trajectories compared? |
| Evidence provenance | Who controls records and testimony? |
| Challenge | Who can contest the model and with what standing? |
| Correctability | Who can stop, reverse, correct, compensate, and track recurrence? |
| Noncompensation | Which severe harms cannot be offset by aggregate gains? |
| Revision | What triggers re-evaluation? |
| Exit | Can persons leave without catastrophic penalty? |

## 8.1 Publicity versus contestability

Public specification makes a captured model visible. It does not make the model contestable.

Whoever controls \(V_F\), \(\prec\), affected scope, and the option set controls the verdicts. Institutions can manufacture apparent underdetermination by refusing to represent alternatives or by using an ordering too coarse to discriminate.

The formal apparatus therefore depends on the wider CU governance architecture:

- affected-party standing;
- option-set integrity;
- independent challenge;
- practical correctability;
- responsibility–authority alignment;
- protected floors;
- and noncompensation.

These safeguards are not derived from KLM semantics. They are explicit normative and institutional commitments.

## 8.2 Cross-model disagreement

Where parties use different models and no justified bridge selects among them, transparent disagreement may be the responsible endpoint.

The framework can require:

- clear assumptions;
- comparative predictions;
- disclosed value choices;
- affected-party participation;
- and revision conditions.

It cannot promise adjudication where the descriptive and normative premises remain genuinely contested.

---

# 9. Frege–Geach: exact scope of the result

## 9.1 What KLM does not do

KLM preferential consequence takes a satisfaction or realization relation as given. It does not explain how contents acquire identity across embedding.

Therefore the paper does not claim:

- to derive compositional commitment content from attitude expression;
- to solve Frege–Geach for all religious or practical language;
- to show that ritual, myth, prayer, and poetry are Boolean formulas;
- or to establish a new expressivist semantics.

## 9.2 What the paper does claim

For commitment contents representable in a declared Boolean-closed language with stable realization conditions, fixed-base preferential semantics supplies a defeasible consequence structure that preserves those contents through embedded inference.

This is a claim about **consequence**, not a complete theory of **meaning**.

## 9.3 Speech-act reframing

The two-register distinction need not rest on two semantic species. It can instead distinguish:

- stable content;
- speech-act force;
- principal function;
- and assessment standard.

A promise, plan, vow, imperative, or declaration can contain stable proposition-like material without being evaluated primarily for truth. On this reading, the classic Frege–Geach problem does not arise from the register distinction itself, because stable content is not denied.

## 9.4 Relation to existing literature

The paper does not claim novelty for:

- Boolean or possible-worlds semantics for practical discourse;
- plan-laden or imperative semantics;
- formal expressivist responses to embedding;
- KLM preferential consequence;
- or two-register treatments of religion.

Its proposed contribution is the combination of:

1. stable commitment contents;
2. fixed-base nonmonotonic consequence;
3. skeptical versus credulous best-realization verdicts;
4. practical expansion review;
5. asymmetric factual constraint;
6. and explicit governance against captured model choice.

---

# 10. Case safeguards

## 10.1 The two widows

The case is:

- schematic;
- stipulated;
- non-clinical;
- culturally non-universal;
- and conditional on the declared facts.

Behavioral signs alone do not establish suppression. Quiet, delayed, nonexpressive, private, culturally unfamiliar, or spiritually framed grief may be healthy. Expressive grief is not the sole legitimate trajectory.

The formal conclusion has the form:

> On the declared model, if every best viable trajectory rejects the suppression commitment, the commitment is excluded relative to that model.

The story does not diagnose any real bereaved person.

## 10.2 Deferred inquiry

Deferral is responsibly available only when it includes:

1. preservation of the anomaly rather than rationalization;
2. expiry or scheduled review;
3. capacity-building;
4. independent material and relational support;
5. protected exit;
6. attention to costs imposed on others;
7. and review outside the community that benefits from continued deferral.

A community may not indefinitely declare a member “not ready” while controlling the conditions of readiness.

## 10.3 Political identity

The diagnostic is symmetric in method:

> Does the community preserve the trajectories through which it could discover that it is wrong?

Symmetry of method does not imply symmetry of evidence. Equal evidential standards applied to unequal evidence properly yield unequal verdicts.

## 10.4 Compassion

Compassion does not:

- alter truth values;
- erase responsibility;
- require trust;
- compel forgiveness or reconciliation;
- or impose educational labor on people who have been harmed.

The last condition is independent and explicit. Understanding the constraints on a mistaken agent does not create an obligation for affected people to provide that understanding.

---

# 11. Independent audit disposition

The independent audit recommended **adopt with bounded repairs**. Publication Candidate 2 accepts the audit’s central findings.

| Audit item | Disposition in PC2 |
|---|---|
| R1 — KLM appears to solve Frege–Geach | Accepted. KLM is stated to presuppose stable realization conditions and to govern consequence, not compositional meaning. |
| R2 — One satisfaction sign used for truth and realization | Accepted. PC2 distinguishes \(\vDash_D\) and \(\Vdash_R\). |
| R3 — Scope of embedding claim too broad | Accepted. Result restricted to already-representable Boolean-closed contents; residue named outside formalization. |
| R4 — Public specification treated as sufficient | Accepted. Publicity gives visibility, not contestability; governance dependencies are load-bearing. |
| R5 — Infeasible and underdetermined combined | Accepted. Verdicts split. Finite-regression counts are further clarified: all 4,104 no-best cases in that suite are infeasible. |
| R6 — Exclusion / negation duality unremarked | Accepted. Classical-negation duality stated as an adopted choice and practical limitation. |
| R7 — Cases risk diagnosis | Accepted. Widow case made explicitly stipulated and non-clinical; deferred inquiry gains external review; political symmetry clarified. |
| R8 — Novelty located in semantics | Accepted. Novelty moved to stable contents plus fixed-base nonmonotonic consequence and practical taxonomy. |
| R9 — Middle verdict weakly protected by regression | Accepted. New non-singleton-best stratum covers 584 cases and all 294 middle verdicts. |
| R10 — Bibliography gaps | Accepted. Hume, Clifford, Wisdom, and Geach added; formal-source metadata normalized; Charlow engagement added. |

## 11.1 One respectful correction to the audit

The auditor inferred that the 4,104 empty-best cases in the finite suite mixed infeasibility, non-attainment, and underdetermination. In the actual finite strict-partial-order enumeration, every nonempty candidate set has a minimal element. The 4,104 cases are therefore all empty candidate sets and exactly infeasible. The audit’s recommendation to separate the verdicts remains correct; the revised regression simply locates the finite counts more precisely.

## 11.2 Audit boundary retained

The auditor did not receive the frozen manuscript or technical supplement. Publication Candidate 2 therefore rechecked every wording-dependent item against the actual PC1 text before revision.

The audit did not assess in full:

- the fairness of the historical philosophical landscape;
- the lived adequacy of the register distinction in religious practice;
- the widow case from bereavement or affected-community perspectives;
- the principal-function analysis;
- practical expansion warrant;
- or the complete bibliography.

Philosophy-of-language, philosophy-of-religion, grief/bereavement, and affected-community reviews remain blocking for final publication.

---

# 12. Bibliography normalization

Publication Candidate 2 adds or normalizes the load-bearing sources identified in the audit packet:

- Hume on miracle testimony;
- Clifford on the ethics of belief;
- Wisdom’s invisible-gardener parable;
- Geach’s “Ascriptivism”;
- KLM and Lehmann–Magidor DOI metadata;
- Nielsen and Yalcin DOI metadata;
- Schroeder’s focused Frege–Geach article;
- Charlow on the Frege–Geach problem and imperative semantics;
- specific editions of Kant and Wittgenstein.

Alston and Plantinga remain because PC2 now gives their truth-apt religious-epistemology projects an explicit role in the argument.

Bibliography normalization does not imply endorsement of each source’s position. It makes the paper’s lineage and points of disagreement auditable.

---

# 13. Source-to-publication disposition

## 13.1 Preserved

- the two-widows opening;
- the insulation objection;
- the Kantian title and limiting project;
- the two-register discipline;
- asymmetric permeability;
- reflexivity;
- transformative commitment;
- deferred inquiry;
- political identity;
- and the compassion corollary.

## 13.2 Reconstructed

- semantic-type language became a speech-act/function and assessment-standard account;
- one satisfaction sign became descriptive truth plus commitment realization;
- one warrant relation became five practical verdicts plus expansion review;
- premise-responsive viability became fixed-base filtering plus declared model revision;
- public specification became a necessary but insufficient condition of contestability;
- the Frege–Geach claim became a bounded consequence claim;
- novelty moved from semantics to nonmonotonic practical consequence;
- case conclusions became explicitly conditional and non-diagnostic.

## 13.3 Retired

- the claim that KLM supplies commitment content;
- the claim that the paper gives a general Frege–Geach solution for non-truth-apt discourse;
- the claim that public specification alone blocks relativism or capture;
- the combined “infeasible or underdetermined” verdict;
- and the claim that the original maximum-preservation clause is a System P consequence relation.

---

# 14. Publication boundary

This supplement establishes:

- consistency with the fixed-base preferential architecture;
- explicit semantic and metalinguistic levels;
- five distinct practical verdicts;
- an expanded finite regression suite;
- audit-responsive case safeguards;
- and transparent governance dependencies.

It does not establish:

- that the two-register distinction is the unique analysis of religious discourse;
- that every commitment has Boolean-representable content;
- that realization semantics defeats every expressivist objection;
- that KLM supplies normative content;
- that any real person is diagnosed by the illustrative cases;
- that model-relative verdicts settle cross-model disagreement;
- or that the manuscript has completed expert and affected-community review.
