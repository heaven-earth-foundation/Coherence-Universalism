# Coherence Universalism: Psychology
## RC3 Release-Convergence Wave 4 — Technical Supplement

**Status and authority.** This is the released technical supplement for the Wave 4 cumulative manuscript. The [reader-facing manuscript](../papers/06_CU_Psychology_v0.10.md) controls current wording, claim status, and canonical cross-references. This supplement exposes the formal derivations, deterministic contrast constructions, claim ledgers, audit materials, scripts, and source records on which the manuscript relies.

- **Evidence directory:** [06_Psychology](../evidence/06_Psychology/README.md)
- **Archived source package:** [CU_Psychology_v0.10_Publication_PC3.zip](../provenance/archival_source_packages/CU_Psychology_v0.10_Publication_PC3.zip)
- **Current supplement path:** `technical_supplements/06_Psychology_Technical_Supplement_v0.10.md`

Reproducibility of a construction shows only that its output follows from its declared assumptions and code. It does not convert a toy model or simulation into target-domain empirical validation. Where this preserved archive uses historical identifiers or statuses, the Wave 4 normalized registries and current manuscript control.

# Wave 4 evidence-access addendum

Wave 4 makes previously referenced but inaccessible materials available in one package. It includes the substantive legacy supplement below, the independent audit and check script, recorded audit output where available, source ledgers, deterministic scripts and generated results where they existed, and the complete pre-RC3 source package for provenance.

The manuscript now includes a concise reader-facing summary of the Appendix F horizon-reversal construction; this supplement retains the full equations, exact results, sensitivity grid, mechanism removals, alternative initial states, and clinical non-inference boundary.

# Preserved substantive technical archive

This supplement preserves the formal propositions, full claim and principle registries, application-governance rules, disposition ledger, deterministic contrast model, references, glossary, independent-audit boundary, and reproducibility record underlying the reader-facing Psychology publication candidate.

The publication manuscript controls exposition. The audited E.1.1 source, machine-readable ledgers, and reproducibility files preserve exact provenance. The technical model is pedagogical and does not constitute clinical evidence.

---

# Appendix A. Formal results and contrast cases

## A.1 Profile non-dominance

Let a psychological profile be a vector \(p\in[0,1]^n\), with larger values representing better performance on declared dimensions after orientation has been fixed. Let

\[
p=(0.9,0.4),
\qquad
q=(0.6,0.8).
\]

Neither profile dominates the other. Profile \(p\) is better on the first dimension and \(q\) on the second. No total order follows from the profile alone.

**[Formal result]** Any ranking of non-dominating profiles requires additional assumptions such as weights, floors, lexicographic priority, or a decision rule.

## A.2 Scalarization reversal

For positive weights \(w=(w_1,w_2)\), define

\[
S_w(p)=w_1p_1+w_2p_2.
\]

Using the profiles above:

\[
S_{(0.8,0.2)}(p)=0.80,
\qquad
S_{(0.8,0.2)}(q)=0.64,
\]

while

\[
S_{(0.2,0.8)}(p)=0.50,
\qquad
S_{(0.2,0.8)}(q)=0.76.
\]

The ranking reverses. This is not a paradox. The weights encode different purposes.

## A.3 Protected floors are not weights

Suppose dimension 2 is safety and must satisfy \(p_2\ge0.5\). Then \(p\) is inadmissible regardless of its advantage on dimension 1. No sufficiently large weight on dimension 1 should compensate if the decision rule declares safety noncompensable.

The distinction between weighted preference and protected floor must be explicit in treatment, research, and policy.

## A.4 Internal consistency does not entail truth

Let a belief set \(B\) be internally consistent but contain a false premise \(r\). Let every conclusion in \(B\) follow validly from \(r\) and auxiliary assumptions. Then \(B\) can have high internal consistency and low descriptive adequacy.

Therefore:

\[
\text{internal consistency}
\not\Rightarrow
\text{truth}.
\]

This blocks the use of felt or formal coherence as an epistemic substitute.

## A.5 Symptom reduction does not entail repair

Let an intervention reduce reported distress \(d\) while decreasing agency \(g\) and relational capacity \(r\):

\[
(d,g,r):
(0.8,0.6,0.7)
\longrightarrow
(0.3,0.3,0.4).
\]

The symptom improvement is real. The global judgment remains underdetermined until goals, adverse effects, safety, horizon, and alternatives are declared.

## A.6 Distress does not entail pathology

Let a person accurately perceive ongoing danger. Elevated fear and vigilance may be costly but calibrated. Removing the distress without changing danger could reduce descriptive adequacy and safety.

Thus:

\[
\text{distress}
\not\Rightarrow
\text{disorder},
\]

and

\[
\text{low distress}
\not\Rightarrow
\text{health}.
\]

## A.7 Difference does not entail dysfunction

Let two attentional profiles solve different task families. Profile \(a\) excels at sustained narrow focus and has high switching cost; profile \(b\) switches readily and has lower sustained depth. Neither is globally superior without a task distribution and person-relevant goals.

This is the formal core of the neurodiversity boundary.

## A.8 Protection can be locally rational and globally costly

Let strategy \(u\) reduce current loss \(L_t\) but increase expected future loss \(L_{t+1:T}\):

\[
L_t(u)<L_t(v),
\qquad
\sum_{s=t+1}^{T}L_s(u)>
\sum_{s=t+1}^{T}L_s(v).
\]

No contradiction follows. The strategies are ordered differently by horizon.

The reverse can also occur: a long-horizon strategy may impose intolerable present risk. Horizon does not erase protected floors.

## A.9 Compartmentalization tradeoff

Suppose two contexts require incompatible responses. A gate \(g\in[0,1]\) reduces interference between contexts while also reducing transfer of learning. Let

\[
P(g)=g
\]

measure protection from cross-context interference and

\[
L(g)=1-g
\]

measure cross-context transfer. Increasing \(g\) improves one dimension and worsens the other.

The construction is deliberately minimal. It proves only that compartmentalization need not be globally good or bad.

## A.10 Falsity does not entail self-deception

Two agents believe the same false proposition \(r\). Agent 1 searched relevant evidence symmetrically and updated when corrected. Agent 2 avoided disconfirming evidence, changed standards when identity was threatened, and accepted weaker evidence when it favored \(r\).

The belief content is identical. The process differs. Self-deception is therefore not reducible to falsity.

## A.11 Defensive function does not entail conscious intention

A pattern can protect identity or attachment without being consciously planned. “Motivated” refers to functional organization around a stake, not necessarily explicit intent to deceive oneself.

This prevents the framework from requiring the paradoxical image of a person simultaneously knowing and hiding the same proposition in the same way.

## A.12 Narrative integration does not entail psychological health

A highly integrated life story can organize grandiosity, persecution, or domination. A fragmented story can accompany honest recovery after overwhelming disruption.

Narrative measures therefore require cross-checking with reality adequacy, agency, affect, relationship, and consequence.

## A.13 Observation underdetermination

Suppose the same outward withdrawal can be produced by fear, fatigue, sensory overload, grief, depression, strategic boundary-setting, cultural norm, or lack of interest. Behavior alone underdetermines mechanism.

Likewise, identical self-report can arise through different causal processes. Multimethod evidence narrows but does not always eliminate underdetermination.

## A.14 Aggregation can conceal binding constraints

Let two persons have the same average profile score:

\[
p=(0.9,0.9,0.3,0.9),
\qquad
q=(0.75,0.75,0.75,0.75).
\]

Both average to \(0.75\), but \(p\) contains a severe deficit on one dimension. If that dimension is safety or reality contact, the average is clinically misleading.

## A.15 Group-to-individual non-equivalence

A covariance pattern estimated across people need not equal the temporal process operating within one person. Between-person and within-person relations can differ in magnitude or sign.

Accordingly, a population factor, symptom network, or treatment mediator cannot be assumed to be the causal mechanism of every individual case.

## A.16 Attractor language

A mathematical attractor is a set toward which trajectories converge under specified dynamics. A recurring psychological pattern is not an attractor merely because it is stable or familiar.

When no state variables, transition rule, basin, and perturbation structure are given, “attractor” is a systems metaphor and must be labeled accordingly.

## A.17 Optimization-language rule

Psychology inherits Biology C.1.1's distinction:

1. **designer optimization:** an investigator or institution explicitly chooses an objective;
2. **as-if optimization:** behavior can be compactly modeled as if optimizing an objective; and
3. **evolutionary selection:** population processes change the prevalence of architectures.

None proves that a person consciously represents the fitted objective.

## A.18 Psychological entropy

Several literatures use entropy to model uncertainty, choice diversity, neural dynamics, language, or behavioral variability. These quantities are not interchangeable with thermodynamic entropy or with one another.

A valid use must specify:

- the probability distribution;
- the events or states;
- the estimator;
- the scale and time window;
- and the psychological interpretation.

“More entropy means more stress” and “more entropy means more flexibility” can both be true in different models. Neither is a universal law.

## A.19 Common factor is not common mechanism

Suppose alliance correlates with outcome across therapies. This can arise because alliance causes engagement, early improvement strengthens alliance, therapist skill affects both, client characteristics affect both, or several routes coexist.

A robust common association does not by itself identify one causal mechanism.

## A.20 Horizon reversal and dominance in the illustrative model

Appendix F constructs three regulation regimes. Immediate suppression produces the lowest acute distress. Supported engagement produces higher acute distress but better later functioning, capacity, and response to a common probe. These two profiles are non-dominating and reverse rank under two declared weight sets.

Unbuffered confrontation exceeds the protected acute-distress threshold and is strictly dominated by supported engagement on all four declared profile coordinates. It therefore illustrates a floor-and-dominance exclusion rather than participating in the scalarization reversal. This demonstrates why horizon, weighting, dominance, and protected floors belong in the model declaration.

---

# Appendix B. Claim and evidence ledger

The following ledger governs the manuscript. Evidence grades are ordinal bookkeeping for this project, not a universal hierarchy:

- **E0:** definition, analytic construction, or conceptual proposal;
- **E1:** formal result or controlled illustration;
- **E2:** limited empirical evidence or convergent small literature;
- **E3:** substantial replicated or meta-analytic support with important qualifications;
- **E4:** broad consensus or mature evidence within scope.

| ID | Claim | Status | Evidence | Scope or condition |
|---|---|---|---|---|
| PSY-C1 | Psychological explanation often improves when perception, affect, memory, identity, relationship, action, and environment are modeled jointly. | Bridge hypothesis | E0–E3 | Must outperform simpler models for the target question. |
| PSY-C2 | Psychology is literally the science of one universal coherence quantity. | Retired | — | No universal scalar or dynamics established. |
| PSY-C3 | A psychological model should declare state, environment, actions, dynamics, constraints, relations, meaning maps, history, scale, horizon, and observations. | Methodological proposal | E0 | Declaration schema, not mandatory ontology. |
| PSY-C4 | Meaning space is universal and has fixed axes. | Rejected | — | Axes are model- and task-dependent. |
| PSY-C5 | Meaning maps can include explicit, implicit, affective, embodied, narrative, social, and commitment relations. | Analytic framework | E0–E3 | Forms may overlap and need operationalization. |
| PSY-C6 | A person is reducible to one inner meaning map. | Rejected | — | Persons are embodied, relational, historical, and environmentally scaffolded. |
| PSY-C7 | Psychological organization should be represented by a profile rather than one default score. | Bridge principle | E0–E3 | Profile content depends on purpose and evidence. |
| PSY-C8 | The Field Coherence Score is an established universal measure of mental health. | Retired | — | No validation or justified universal weighting. |
| PSY-C9 | Non-dominating profiles can reverse rank under different weights. | Formal result | E1 | Exact for the declared constructions. |
| PSY-C10 | Protected safety or agency floors should not be treated as ordinary compensable weights. | Normative-methodological constraint | E0 | Floors require ethical and clinical justification. |
| PSY-C11 | Stress is literal inverse entropy. | Retired | — | Psychological entropy constructs are model-specific. |
| PSY-C12 | Integration overload can be modeled as demands falling outside current regulatory capacity. | Model family | E0–E2 | Requires declared dimensions and observations. |
| PSY-C13 | Distress always indicates disorder. | Rejected | E0–E4 | Distress can be calibrated to loss, threat, injustice, or change. |
| PSY-C14 | Low distress always indicates health. | Rejected | E0–E4 | Numbing, mania, intoxication, or compliance can reduce distress. |
| PSY-C15 | Perception is actively organized by expectation, attention, body, and task. | Empirical generalization | E3–E4 | Does not imply arbitrariness. |
| PSY-C16 | Predictive processing is the established universal theory of psychology. | Not established | E0–E3 | Retained as a model family. |
| PSY-C17 | Memory is reconstructive and cue-dependent. | Imported empirical result | E4 | Does not imply pervasive unreliability. |
| PSY-C18 | Memory reconsolidation is the universal mechanism of psychotherapy. | Not established | E1–E3 | Boundary conditions and clinical translation remain disputed. |
| PSY-C19 | Meaning in life is multidimensional, commonly including comprehension, purpose, and significance or mattering. | Imported construct synthesis | E3 | Measurement and culture matter. |
| PSY-C20 | Narrative themes can relate to well-being beyond broad traits. | Imported empirical result | E2–E3 | Association is not deterministic causation. |
| PSY-C21 | Narrative coherence entails truth or health. | Rejected | E0–E3 | Narratives require external and profile checks. |
| PSY-C22 | Emotion coordinates attention, learning, bodily preparation, communication, and action. | Empirical generalization | E3–E4 | Theories differ on mechanism. |
| PSY-C23 | Valence is the felt sign of one universal coherence gradient. | Retired | — | D.1.1 separates affect, reward, stake, and phenomenal valence. |
| PSY-C24 | Emotion-regulation difficulties are transdiagnostic but not identical across disorders. | Imported meta-analytic result | E3 | Much evidence is self-report. |
| PSY-C25 | Strategy effects depend on context, timing, culture, intensity, and goal. | Empirical generalization | E3 | No strategy is globally adaptive. |
| PSY-C26 | People optimize one universal psychological objective. | Rejected | — | Motivation is plural and often conflicted. |
| PSY-C27 | Embodied state constrains psychological regulation. | Empirical bridge | E3–E4 | No one bodily marker captures mental health. |
| PSY-C28 | Insight automatically changes procedural and affective response. | Rejected | E1–E4 | Learning and embodied access can lag explicit understanding. |
| PSY-C29 | Psychological agency is graded and environmentally constrained. | Analytic and empirical framework | E0–E4 | Agency is not moral worth. |
| PSY-C30 | Identity has one criterion across legal, bodily, narrative, relational, and moral uses. | Rejected | E0 | Identity is use- and horizon-relative. |
| PSY-C31 | Self-modeling is identical with egoic self-maintenance. | Rejected | E0–E2 | D.1.1 distinguishes them. |
| PSY-C32 | Personality is a patterned profile, not one coherence strategy. | Bridge synthesis | E0–E4 | Traits, adaptations, narratives, and context differ. |
| PSY-C33 | High self-concept clarity entails accurate self-knowledge. | Rejected | E0–E3 | Clarity, adequacy, flexibility, and integration differ. |
| PSY-C34 | Self-deception is motivated asymmetric processing that protects a stake against relevant reasons. | Bridge principle | E0–E3 | Requires convergent evidence and alternatives. |
| PSY-C35 | False belief or disagreement alone establishes self-deception. | Rejected | E0 | Process evidence is required. |
| PSY-C36 | Attachment relationships can provide co-regulation and scaffold later capacities. | Empirical bridge | E3–E4 | Taxonomies are not exhaustive or destiny. |
| PSY-C37 | Dependence is always immaturity. | Rejected | E0–E4 | Interdependence is ordinary; coercive dependence differs. |
| PSY-C38 | Sexuality universally integrates psychological coherence. | Retired | — | Functions and consequences vary. |
| PSY-C39 | Consent can be inferred from apparent harmony or absence of resistance. | Rejected | E0–E4 | Capacity, voluntariness, power, and revocability matter. |
| PSY-C40 | Potentially traumatic events produce one universal response trajectory. | Rejected | E3–E4 | Resilience, recovery, chronic, delayed, and mixed courses occur. |
| PSY-C41 | Protective compartmentalization can be adaptive in one regime and costly in another. | Bridge principle | E0–E3 | Function, context, and horizon must be assessed. |
| PSY-C42 | Trauma is literally stored as episodic memory in bodily tissue. | Not established | E0–E3 | Bodily and procedural persistence is not tissue-level narrative storage. |
| PSY-C43 | Repair is identical with symptom suppression or return to baseline. | Rejected | E0–E4 | Repair may involve transformation, accommodation, and boundary. |
| PSY-C44 | Post-traumatic growth is universal or justifies suffering. | Rejected | E2–E3 | Growth can coexist with injury and is not required. |
| PSY-C45 | Neurodivergence is either pure disorder or pure difference. | Rejected dichotomy | E0–E4 | Difference, disability, distress, strengths, and injustice can coexist. |
| PSY-C46 | Reciprocal neurotype fit contributes to some communication outcomes. | Empirical hypothesis | E2–E3 | Results vary by task and study; not settled. |
| PSY-C47 | Masking can carry both benefits and costs. | Empirical generalization | E2–E3 | Definitions and causal direction remain variable. |
| PSY-C48 | Diagnostic categories are useless because profiles exist. | Rejected | E0–E4 | Categories retain clinical and institutional functions. |
| PSY-C49 | A general psychopathology factor proves one underlying disease or global incoherence. | Rejected inference | E0–E3 | Statistical factors depend on model and sample. |
| PSY-C50 | Symptom networks estimated between persons identify each person's causal dynamics. | Rejected inference | E0–E3 | Idiographic and intervention evidence required. |
| PSY-C51 | Therapeutic alliance is robustly associated with outcome. | Imported meta-analytic result | E3 | Causal direction and mechanisms remain plural. |
| PSY-C52 | Common factors make specific techniques irrelevant. | Rejected | E0–E4 | Relationship and technique interact. |
| PSY-C53 | Psychotherapies are generally beneficial relative to controls, but complete response is far from universal. | Imported meta-analytic result | E3 | Rates vary by condition, trial, and outcome. |
| PSY-C54 | Therapy is one universal coherence-modulation mechanism. | Retired | — | Requires process-specific accounts. |
| PSY-C55 | Somatic practices are universally effective or prove trauma storage in the body. | Not established | E1–E3 | Evidence varies by intervention and outcome. |
| PSY-C56 | Neurotransmitters map one-to-one onto motivation, stability, or threat. | Rejected | E0–E4 | Systems are receptor-, circuit-, and context-dependent. |
| PSY-C57 | Psychedelic experience automatically produces truth or healing. | Rejected | E1–E3 | Expectancy, setting, risk, and interpretation matter. |
| PSY-C58 | Development follows one universal hierarchy ending in epistemic-spiritual integration. | Retired | — | Development is plural, asynchronous, and cultural. |
| PSY-C59 | Earlier states and environments can alter later transition costs and options. | Bridge principle | E0–E4 | Path dependence does not imply destiny. |
| PSY-C60 | Social and material conditions are causally relevant to mental health. | Imported empirical generalization | E3–E4 | Mechanisms and effect sizes vary. |
| PSY-C61 | A single global meaning crisis has been empirically established. | Not established | E0–E2 | Decompose into measurable hypothesis families. |
| PSY-C62 | Religious and contemplative practices can support or undermine regulation and meaning. | Empirical generalization | E2–E4 | Tradition, practice, person, and power matter. |
| PSY-C63 | A profile architecture will improve person-specific prediction over symptom totals and categories. | Research hypothesis | E0 | Requires preregistered comparison. |
| PSY-C64 | CU language authorizes clinical diagnosis or treatment. | Rejected | — | E.1.1 is a research architecture only. |
| PSY-C65 | In Appendix F, supported engagement strictly dominates unbuffered confrontation on all four declared profile coordinates. | Formal result | E1 | Constructed baseline model only; no clinical inference. |
| PSY-C66 | The identities of the short- and long-horizon winners persist under five single-mechanism sign ablations, removal of support from the learning gate, and four declared alternative initial states. | Numerical robustness result | E1 | Robustness of the construction, not treatment evidence or parameter identification. |
| PSY-C67 | Appendix F establishes a three-way empirical tradeoff among regulation strategies. | Rejected interpretation | — | Its Pareto frontier contains suppression and supported engagement, plus an unbuffered regime dominated by supported engagement; the regime definitions deliberately create the long-horizon advantage. |

---

# Appendix C. Candidate psychology principles for v0.10

The following principles preserve the identifiers reserved in Foundations B.2 while revising their content to match the non-scalar architecture of this reconstruction. They are **candidate domain principles**. Their appearance here does not alter the canonical registry in Foundations B.2. Promotion requires independent audit, resolution of the objections listed below, and a later synchronized Foundations revision.

## CU-Ψ1 — Meaning Space

**Candidate status:** Definition / analytic construction.

For a declared psychological question, a **meaning space** is a model-dependent set of distinctions along which events, actions, relationships, memories, identities, and possibilities can matter to a person or group:

\[
\mathcal M_{\Psi}=\mathcal M_{\Psi}(\text{person},\text{context},\pi,T,\mathcal O).
\]

Its coordinates may include expected consequence, bodily salience, social significance, autobiographical relevance, moral implication, practical affordance, or sacred orientation. No universal dimensionality or fixed axis set is assumed. A meaning space is an analyst's construct unless evidence establishes that its distinctions are represented or enacted by the person.

**Principal failure mode:** Treating the researcher's vocabulary as the person's phenomenology.

## CU-Ψ2 — Meaning Maps

**Candidate status:** Analytic bridge principle.

A **meaning map** is a structured, revisable relation among cues, interpretations, affective responses, bodily states, memories, commitments, predicted consequences, and action tendencies. Meaning maps may be explicit or implicit, proposition-like or procedural, individually carried or socially scaffolded. Their psychological importance lies in how they organize attention, expectation, action, and revision—not in their conformity to one canonical map.

**Principal failure mode:** Assuming that internal consistency, narrative elegance, or social stability establishes descriptive truth.

## CU-Ψ3 — Psychological Coherence Profile

**Candidate status:** Canonical-conditional methodological principle.

Psychological organization should ordinarily be represented by a declared profile rather than one universal scalar. A default research profile may include descriptive adequacy, affect tolerance and regulation, regulatory flexibility, identity and narrative integration, relational capacity, agency, embodied regulation, meaning or purpose, and repair capacity:

\[
\mathbf P_{\Psi}
=
\langle
A_d,A_f,F_r,I_n,R_c,G_a,B_r,M_p,Q_r
\rangle.
\]

The dimensions, observations, scales, and horizons must be justified for the question. Scalarization is permitted only when its weights, normalization, protected floors, affected persons, and decision purpose are declared. Non-dominating profiles may remain incomparable.

**Principal failure mode:** Smuggling a moral or clinical ideal into an apparently neutral score.

## CU-Ψ4 — Integration Load and Regulatory Capacity

**Candidate status:** Model family / bridge hypothesis.

At a given time and scale, a person confronts a demand profile \(d_t\) and possesses a context-sensitive capacity region \(\mathcal C_t\). **Integration overload** occurs when relevant demands cannot be metabolized, coordinated, deferred, delegated, escaped, or safely compartmentalized within that capacity:

\[
d_t\notin\mathcal C_t.
\]

Stress and distress depend not only on demand magnitude but on predictability, controllability, meaning, bodily condition, social support, prior learning, structural power, and temporal horizon. Overload is not identical with disorder, and low expressed distress is not sufficient evidence that demands have been integrated.

**Principal failure mode:** Locating in the individual a burden produced by an unsafe or unjust environment.

## CU-Ψ5 — Psychological Regulation and Meaning-Seeking

**Candidate status:** Empirical bridge hypothesis.

Human psychological activity is organized by multiple, sometimes conflicting regulatory tendencies, including safety, attachment, exploration, competence, status, identity protection, truth-seeking, care, belonging, autonomy, pleasure, pain avoidance, and sacred or long-horizon commitment. People often seek interpretations and practices that make action possible, but there is no established universal psychological drive to maximize one coherence quantity.

**Principal failure mode:** Redescribing every motive after the fact as coherence-seeking and thereby making the principle unfalsifiable.

## CU-Ψ6 — Local–Global and Short–Long Tension

**Candidate status:** Bridge principle.

A pattern may be adaptive for one subsystem, relationship, role, or short horizon while undermining another subsystem, wider context, or longer horizon. Psychological evaluation must therefore specify at least:

\[
(\text{part or whole},\ \text{context},\ \text{horizon},\ \text{protected floors}).
\]

Suppression, avoidance, compartmentalization, conformity, disclosure, confrontation, and self-revision can each reverse their profile effects as these declarations change. No local gain or immediate relief licenses an inference to global or durable health.

**Principal failure mode:** Treating the analyst's preferred horizon as uniquely rational while ignoring acute safety.

## CU-Ψ7 — Repair Capacity

**Candidate status:** Bridge principle / empirical hypothesis.

**Repair capacity** is the context-sensitive ability to detect consequential mismatch or rupture, remain or return within a tolerable range of engagement, revise models or strategies, recruit support, make restitution where appropriate, restore workable coordination, and learn in ways that reduce future recurrence. Repair need not restore the prior state. It may require grief, accommodation, boundary, identity change, or transformation of the environment.

**Principal failure mode:** Equating repair with reconciliation, forgiveness, symptom elimination, productivity, or return to a harmful baseline.

## CU-Ψ8 — Protective Compartmentalization and Fragmentation

**Candidate status:** Conditional bridge principle.

Psychological separation among memories, affects, roles, self-states, or action systems can protect functioning when full integration would exceed present capacity or threaten safety. The same separation can become costly when it blocks reality contact, agency, flexible access, relationship, or repair after the original conditions change. The distinction between **protection** and **fragmentation** is therefore functional, contextual, and horizon-relative rather than purely structural.

**Principal failure mode:** Pathologizing survival adaptations or romanticizing costly dissociation.

## CU-Ψ9 — Developmental Path Dependence and Plasticity

**Candidate status:** Empirical bridge principle.

Psychological development is path-dependent: earlier relationships, bodily states, learning histories, institutions, and material conditions alter the accessibility, cost, and meaning of later transitions. Development nevertheless remains plastic. Similar adult patterns can arise by different paths, and different outcomes can arise from similar beginnings. Attractor language is legitimate only when a model specifies states, transitions, perturbations, and evidence of return or basin structure.

**Principal failure mode:** Turning statistical regularities or culturally preferred biographies into destiny.

## CU-Ψ10 — Attachment and Co-Regulation

**Candidate status:** Empirical bridge principle.

Human regulation is partly distributed across relationships. Attachment figures and other trusted partners can alter perceived threat, attention, effort, affect tolerance, exploration, and recovery. Repeated co-regulation can scaffold capacities later enacted more independently, but healthy adulthood is not independence from others. Attachment categories are probabilistic summaries, not fixed essences or exhaustive identities.

**Principal failure mode:** Using attachment labels as retrospective total explanations or as grounds for blame.

## CU-Ψ11 — Self-Deception as Motivated Meaning-Map Distortion

**Candidate status:** Bridge principle.

Self-deception is a pattern of motivated, asymmetric information processing in which a person protects an identity, attachment, advantage, policy, or other stake by selectively excluding, reframing, discounting, or neutralizing relevant reasons. False belief, uncertainty, bias, trauma adaptation, sincere disagreement, or ordinary inconsistency is not sufficient. Attribution should rely on convergent process evidence, plausible motive, counterfactual asymmetry, and serious comparison with alternatives.

**Principal failure mode:** Converting disagreement with the analyst into diagnosis of corruption.

## CU-Ψ12 — Psychological Coherence Infrastructure

**Candidate status:** Social-psychological bridge hypothesis.

Psychological capacities are materially and socially scaffolded. Stable housing, bodily safety, time, income, accessible care, trustworthy information, reciprocal relationships, cultural intelligibility, legal standing, and opportunities for meaningful participation can expand or contract what a person can regulate, revise, and repair. Population distress should therefore be analyzed through both individual mechanisms and the infrastructure that distributes exposure, burden, support, and agency.

**Principal failure mode:** Using social explanation to erase individual differences, biology, or the value of person-level treatment.

## C.13 Promotion criteria

Before any candidate is promoted into Foundations, the following must be completed:

1. an independent conceptual audit of the profile architecture and its relation to existing psychological frameworks;
2. primary-source verification of every load-bearing empirical claim;
3. clarification of construct overlap with psychological flexibility, personality functioning, resilience, meaning in life, emotion regulation, attachment, and recovery;
4. explicit safeguards against pathologizing neurodivergence, minority identity, grief, dissent, disability, trauma adaptation, dissociation, or culturally unfamiliar forms of life;
5. participatory review with people directly affected by the relevant classifications, with substantive authority rather than symbolic consultation—especially before promoting CU-Ψ8 or principles governing neurodiversity, compartmentalization, disclosure, or fragmentation;
6. tests showing whether the profile predicts or explains anything beyond established measures;
7. evidence that the self-deception construct can be applied with acceptable reliability and without ideological asymmetry;
8. separation of descriptive psychological principles from ethical judgments and spiritual commitments; and
9. synchronized review with Social Dynamics, Ethics, and AI so that downstream papers do not silently strengthen the claims.

---

# Appendix D. Governance rules for psychological coherence claims

These rules apply to the manuscript and to later uses of its vocabulary. A claim that violates them should be treated as underspecified even when its prose is intuitively compelling.

## D.1 Person and target rule

Name the person, population, relationship, institution, or model being evaluated. Do not move silently between an individual's experience, a clinician's objective, a family's preference, an employer's demand, and a society's norm.

## D.2 Boundary and context rule

Declare the relevant boundary and context. A pattern can be adaptive at home and costly at work, protective during danger and restrictive after danger, or functional for a role while harmful to the person who performs it.

## D.3 Horizon rule

Name the time horizon. Acute survival, short-term symptom relief, developmental learning, relationship continuity, and lifelong flourishing are different evaluative problems.

## D.4 Profile rule

Name the dimensions being assessed and those deliberately left unmeasured. Do not use “coherence,” “integration,” “functioning,” or “well-being” as though each were self-measuring.

## D.5 Protected-floor rule

Declare noncompensable or specially protected conditions, including immediate safety, consent, reality contact where relevant, bodily viability, freedom from coercion, basic agency, and risk of severe deterioration. A gain elsewhere does not automatically compensate for crossing such a floor.

## D.6 Observation-channel rule

Distinguish self-report, behavior, performance, physiology, informant report, ecological context, and longitudinal course. Their disagreement is information; it should not be resolved automatically in favor of one privileged channel.

## D.7 Register rule

Separate descriptive claims from commitments and values. That a practice supplies meaning does not establish its cosmology. That a belief is factually unsupported does not by itself determine how a person should grieve, love, worship, or orient a life. Established facts constrain commitments; commitments do not establish facts.

## D.8 Power and affected-person rule

Identify who bears costs, who defines improvement, who controls the setting, and who can refuse. Apparent interpersonal or institutional “coherence” can be produced by silencing, dependence, masking, exclusion, or coercion.

## D.9 Clinical-scope rule

Do not infer diagnosis, prognosis, or treatment from CU terminology alone. Clinical decisions require appropriate professional assessment, condition-specific evidence, risk evaluation, consent, and awareness of local standards of care.

## D.10 Alternative-explanation rule

Before attributing a pattern to trauma, attachment, self-deception, ego defense, meaning-map distortion, or regulatory failure, compare plausible alternatives: ordinary disagreement, neurodivergence, cultural difference, material constraint, medication effect, illness, sleep loss, pain, role conflict, rational caution, and measurement error.

## D.11 Difference-without-defect rule

Deviation from a statistical norm, cultural expectation, narrative ideal, or communication style does not establish dysfunction. Demonstrate distress, impairment, danger, involuntary restriction, or failure relative to the person's own viable aims and context.

## D.12 Intervention and agency rule

Evaluate interventions not only by symptom or performance change but by consent, burden, understanding, agency, accessibility, adverse effects, maintenance, and distribution of benefit and harm. Repair imposed without voice may reproduce the conditions of injury.

## D.13 Self-deception attribution rule

Because the concept is morally and politically dangerous, self-deception requires process evidence rather than confidence about another person's hidden motive. Stronger attributions require stronger convergent evidence and symmetric willingness to test the interpreter's own protected commitments.

## D.14 Optimization-language rule

Distinguish:

1. **designer optimization**, in which a clinician, researcher, institution, or person explicitly selects an objective;
2. **as-if analysis**, in which behavior is modeled as though it minimized or maximized a quantity; and
3. **developmental or evolutionary selection**, in which histories change the prevalence of strategies.

None by itself establishes that the person represents, endorses, or consciously chooses the objective. Accordingly, distinguish designer optimization, as-if analysis, and developmental or evolutionary selection.

## D.15 Spiritual-safety rule

Religious and contemplative practices may support meaning, attention, compassion, community, and tolerance of experience. They may also be used to suppress grief, deny abuse, intensify shame, legitimate hierarchy, or avoid needed care. Spiritual interpretation must never cancel risk assessment, factual correction, consent, or the person's right to leave a practice or community.

---

# Appendix E. Disposition of the March 2026 Psychology architecture

The following table records how the major constructs of the source paper are treated in E.1.1. “Retained” does not mean unchanged; “retired” does not mean the motivating observation was worthless.

| Legacy construct or claim | E.1.1 disposition | Reason and replacement |
|---|---|---|
| Psychology is, at foundation, the science of coherence | **Narrowed** | Retained as an integrative research proposal; rejected as a literal reduction to one quantity. |
| Psychological coherence as system-level integration | **Retained with declarations** | Replaced by a profile relative to person, context, constraints, observations, scale, and horizon. |
| Meaning space | **Retained and scoped** | Model-dependent construct; no universal axes or direct readout of phenomenology. |
| Meaning map | **Retained and expanded** | Includes explicit, implicit, bodily, affective, narrative, social, and commitment relations. |
| Field Coherence Score | **Retired** | No validated universal weighting or construct identity. Scalar scores remain task-specific decisions. |
| Inverse Entropic Stress | **Retired as canonical measure** | Stress is not literal inverse entropy; replaced by demand-capacity and uncertainty models. |
| Universal coherence drive | **Retired** | Replaced by plural motives and conditional tendencies toward safety, meaning, identity, attachment, exploration, and repair. |
| Local–global tension | **Retained and expanded** | Now includes part–whole, context, affected-person, and short–long horizon reversals. |
| Perception as coherence construction | **Retained with realism constraint** | Perception is active and expectation-sensitive but answerable to external structure and correction. |
| Memory as temporal coherence | **Retained metaphorically; formal identity retired** | Memory supports continuity but is reconstructive, cue-dependent, and not one substrate-independent constraint deformation. |
| Emotion as coherence assessment | **Narrowed** | Emotion coordinates multiple functions; no universal scalar assessment or valence gradient is claimed. |
| Motivation as gradient navigation | **Retired as universal formalism** | Gradient language requires a declared objective and geometry; plural conflict is primary. |
| Identity as long-horizon coherence | **Retained as one lens** | Identity has bodily, legal, narrative, relational, practical, and moral criteria that need not coincide. |
| Personality as stable coherence strategy | **Narrowed** | Personality is a profile of traits, adaptations, narratives, motives, and contextual patterns. |
| Self-deception as coherence defense | **Retained and disciplined** | Recast as motivated asymmetric processing with evidential safeguards and alternatives. |
| Attachment as distributed regulation | **Retained** | Co-regulation and social baseline ideas remain, without making dependence immature or styles fixed essences. |
| Sexuality as amplified coherence dynamics | **Retired** | Sexuality is heterogeneous; analysis now focuses on function, consent, power, identity, pleasure, risk, and relationship. |
| Trauma as coherence catastrophe | **Retired as universal account** | Replaced by heterogeneous alterations in threat, memory, affect, body, identity, relationship, and agency. |
| Failed recovery as a downward spiral | **Retained as possible pattern, not law** | Feedback can sustain distress, but trajectories are heterogeneous and structurally conditioned. |
| Recovery as phase transition | **Conditional metaphor only** | Nonlinear change is possible; phase language requires an explicit model and evidence. |
| Memory reconsolidation as the mechanism of phase-leap recovery | **Not established** | Reconsolidation remains one research program with boundary and translation questions. |
| Neurodiversity as coherence divergence | **Revised** | Difference, disability, distress, strength, and social mismatch can coexist; “divergence” is not a complete account. |
| Psychopathology as persistent coherence failure | **Retired as essence claim** | Retained only as one profile description among biomedical, developmental, learning, network, social, and phenomenological models. |
| Therapy as coherence modulation | **Retired as common mechanism** | Replaced by treatment-specific and cross-cutting processes with comparative evidence. |
| Borrowed coherence | **Retained as a relational metaphor** | Reformulated as co-regulation, alliance, modeling, structure, and scaffolded agency. |
| Pharmacology as coherence tradeoff | **Narrowed** | Benefits and burdens can be profiled, but mechanisms remain receptor-, circuit-, dose-, person-, and context-specific. |
| Psychedelics as constraint relaxers | **Conditional model only** | Altered precision, flexibility, entropy, and belief updating are research hypotheses, not automatic truth or healing. |
| Moral and political beliefs as psychological coherence constraints | **Partly relocated** | Psychology studies their functions and processing; normative validity belongs to Ethics and descriptive accuracy to M&E. |
| Shared coherence fields | **Revised to psychological infrastructure** | Replaced by measurable relational, informational, material, institutional, and cultural scaffolds. |
| Religion as long-horizon coherence technology | **Retained with dual-use analysis** | Practices can support or harm; truth, warrant, power, and outcome must be separately assessed. |
| Radicalization as coherence capture | **Narrowed** | Retained as one hypothesis involving identity, threat, network, status, narrative, and information dynamics. |
| Five developmental attractor profiles | **Retired as universal hierarchy** | Replaced by multidimensional, asynchronous, culturally situated development and path dependence. |
| Masculinity and femininity as universal coherence strategies | **Removed from scientific core** | Archetypal language may remain interpretive; it is not an empirical sex or gender taxonomy. |
| Dopamine as gradient sensitizer; serotonin as baseline stabilizer; norepinephrine as threat prioritizer | **Retired as one-to-one mappings** | Replaced by circuit-, receptor-, timescale-, and context-sensitive neurobiology. |
| Mental-health crisis as one coherence crisis | **Decomposed into hypotheses** | Test social determinants, loneliness, insecurity, care access, information conditions, identity threat, and reporting separately. |
| Exact ladder placement and fixed rung count | **Deferred** | The Ladder remains a revisable dependency graph until all domain papers are synchronized. |
| Healing as restoration of coherence | **Retained in interpretive register** | Scientific sections use specific outcomes; healing may include grief, accommodation, transformation, or environmental repair. |

## E.1 Material preserved from the source

The reconstruction retains the source paper's most important experiential and conceptual insights:

- that psychological life cannot be understood by isolating cognition from affect, body, identity, relationship, and meaning;
- that immediate stability can conflict with longer-horizon truth or agency;
- that self-deception protects something before it corrupts inquiry;
- that trauma responses are intelligible adaptations rather than mere defects;
- that relationship can provide capacities unavailable in isolation;
- that symptom relief and healing are not synonyms;
- that social conditions enter into the architecture of mental life; and
- that compassion and truthfulness must be held together.

What has changed is the status of these insights. E.1.1 no longer presents them as consequences of one universal equation. It turns them into separable constructs, conditional bridge principles, empirical hypotheses, and interpretive commitments that can succeed or fail independently.

---

# Appendix F. Illustrative horizon-reversal model

## F.1 Purpose and limits

This appendix constructs a deterministic four-variable model to demonstrate four logical possibilities:

1. the strategy that minimizes acute distress can produce the poorer later response to a common challenge;
2. two non-dominating profiles can reverse rank when the declared weights and horizon change;
3. a third profile can be excluded both by a protected acute-safety floor and by ordinary profile dominance; and
4. robustness of a constructed ranking need not constitute evidence for a clinical intervention.

The model is not fitted to clinical data or patient observations, does not represent a treatment protocol, and does not imply that exposure, suppression, acceptance, or support has one universal effect. The regime labels are evocative names for analyst-defined controls. They were deliberately selected to construct a contrast among immediate relief, supported learning, and unbuffered load. The appendix therefore tests the internal consequences of those declarations; it does not discover which strategy is best for actual people.

## F.2 State variables

At discrete time \(t\), let

\[
x_t=(d_t,s_t,f_t,c_t),
\]

where:

- \(d_t\geq 0\) is acute distress;
- \(s_t\geq 0\) is sensitization to the declared cue class;
- \(f_t\in[0,1]\) is valued functioning;
- \(c_t\in[0.05,1]\) is regulatory capacity available in the model.

A cue schedule \(q_t\geq 0\) presents three bounded challenge episodes. A strategy supplies three control terms:

- \(a_t\): avoidance or suppression;
- \(e_t\): engagement with the cue;
- \(h_t\): support or buffering.

The terms are analyst-defined. They do not imply that an actual person solves an optimization problem or represents the variables.

## F.3 Update equations

Define overload

\[
o_t=\max(0,d_t-0.9c_t).
\]

The updates are

\[
\begin{aligned}
d_{t+1}
&=
\max\bigl(
0,
0.72d_t
+0.36q_t(0.5+s_t)
-0.42a_t
+0.18e_t
-0.16c_t
-0.10h_t
+0.04
\bigr),\\[4pt]
s_{t+1}
&=
\max\bigl(
0,
0.985s_t
+0.07q_ta_t
-0.055q_te_t\min(1,c_t+h_t)
+0.025o_t
\bigr),\\[4pt]
f_{t+1}
&=
\operatorname{clip}_{[0,1]}
\bigl(
f_t
+0.012e_t\min(1,c_t+h_t)
-0.014a_t
-0.006d_t
\bigr),\\[4pt]
c_{t+1}
&=
\operatorname{clip}_{[0.05,1]}
\bigl(
c_t
+0.010h_t
+0.006e_t(1-\min(1,o_t))
-0.012o_t
+0.002(0.6-c_t)
\bigr).
\end{aligned}
\]

The bounds are part of the definition, not numerical repairs. A **boundary hit** is counted only when the unconstrained pre-clamp update lies outside the variable's declared interval. A post-update value that merely equals a boundary is not counted unless clipping was active. This is the convention that yields twenty sensitization-bound hits for supported engagement and nineteen for unbuffered confrontation.

## F.4 Three declared regimes

### Suppression-dominant

\[
a_t=\min(1,0.75q_t+0.45d_t),
\qquad
e_t=0.05q_t,
\qquad
h_t=0.10q_t.
\]

### Supported engagement

\[
a_t=\min(0.35,0.15q_t+0.15d_t),
\qquad
e_t=0.60q_t,
\qquad
h_t=0.65q_t.
\]

### Unbuffered confrontation

\[
a_t=0,
\qquad
e_t=0.90q_t,
\qquad
h_t=0.
\]

All regimes begin from

\[
x_0=(0.15,0.25,0.80,0.55).
\]

The supported-engagement regime is the only one defined with both substantial engagement and substantial support. The equations reward that combination through supported desensitization, functioning gain, capacity gain, distress relief, and overload reduction. Its later advantage is consequently a designed property of the construction.

## F.5 Evaluation profile and exact probe schedule

The primary outcome profile is

\[
\mathbf z
=
\langle
1-\overline d_{\mathrm{acute}},
 f_{\mathrm{final}},
 c_{\mathrm{final}},
 1-d_{\mathrm{probe}}^{\max}
\rangle,
\]

where higher is better on every coordinate and \(\overline d_{\mathrm{acute}}\) is the mean of the first twenty-five post-update training states, spanning the first cue episode and early recovery.

After the 160-step learning phase, the common probe begins from the final state of each regime with no strategy-specific avoidance, engagement, or support:

\[
q_t^{\mathrm{probe}}=
\begin{cases}
1.0,&0\leq t<10,\\
0,&10\leq t<30.
\end{cases}
\]

Thus the probe is a ten-step cue episode at intensity \(1.0\), followed by twenty recovery steps, for thirty steps total.

A protected acute-distress floor is declared as

\[
d_t\leq 0.80.
\]

This is an illustrative threshold, not a clinical standard.

## F.6 Baseline results, boundary activity, and dominance

| Regime | Mean acute distress | Peak distress | Final sensitization | Final functioning | Final capacity | Probe peak distress | Probe distress area |
|---|---:|---:|---:|---:|---:|---:|---:|
| Suppression-dominant | 0.00445 | 0.23013 | 0.42401 | 0.49283 | 0.59470 | 0.93557 | 8.72668 |
| Supported engagement | 0.15415 | 0.41251 | 0.00000 | 0.88518 | 0.80450 | 0.31532 | 2.61065 |
| Unbuffered confrontation | 0.43371 | 1.11379 | 0.01018 | 0.80464 | 0.56113 | 0.45874 | 4.08332 |

The suppression-dominant regime produces the least early-window distress but the largest later probe response, lowest final functioning, and highest sensitization. Supported engagement produces more distress during the learning episodes but the stronger later profile. Unbuffered confrontation crosses the declared acute-safety floor.

Under the boundary-hit convention in F.3, the non-negativity clamp on sensitization is active for twenty training updates in supported engagement and nineteen in unbuffered confrontation; no functioning or capacity clamp is active. These counts report actual pre-clamp crossings, not every step whose post-update sensitization equals zero.

Supported engagement also strictly dominates unbuffered confrontation on all four evaluation coordinates:

| Coordinate | Supported minus unbuffered |
|---|---:|
| Acute comfort | \(+0.27956\) |
| Final functioning | \(+0.08054\) |
| Final capacity | \(+0.24337\) |
| Probe resilience | \(+0.14342\) |

Because each difference is strictly positive, every nonzero weighting with nonnegative coefficients ranks supported engagement above unbuffered confrontation. The floor and ordinary profile dominance therefore agree in excluding the unbuffered regime. It cannot be optimal under any such weighting, although it remains pairwise non-dominating with suppression. The Pareto frontier of the three-profile set therefore contains only suppression and supported engagement.

## F.7 Scalarization reversal for the non-dominating pair

For a short-horizon weighting

\[
w^{(S)}=(0.90,0.04,0.02,0.04),
\]

the resulting scores are approximately

\[
\begin{aligned}
S_{w^{(S)}}(\text{suppression})&=0.93018,\\
S_{w^{(S)}}(\text{supported})&=0.84015,\\
S_{w^{(S)}}(\text{unbuffered})&=0.57472.
\end{aligned}
\]

For a longer-horizon weighting

\[
w^{(L)}=(0.10,0.30,0.25,0.35),
\]

the order is

\[
\begin{aligned}
S_{w^{(L)}}(\text{supported})&=0.79090,\\
S_{w^{(L)}}(\text{unbuffered})&=0.62774,\\
S_{w^{(L)}}(\text{suppression})&=0.41863.
\end{aligned}
\]

The scalarization-winning reversal is between suppression and supported engagement, the two regimes on the Pareto frontier. Their profiles are non-dominating: suppression is better on acute comfort, while supported engagement is better on the three later dimensions. Suppression and unbuffered confrontation are also pairwise non-dominating, but unbuffered is globally Pareto-dominated by supported engagement and can never be the maximizing regime under a nonzero nonnegative weighting. The first weighting does not prove that suppression is preferable, and the second does not prove that supported engagement is clinically preferable. Each score expresses a declared decision perspective. Unbuffered confrontation appears in the numerical ordering but cannot outrank supported engagement under any nonzero nonnegative weighting and is independently inadmissible under the protected floor.

## F.8 Robustness checks and their limits

### F.8.1 Local coefficient grid

Five coefficients—distress retention, avoidance relief, support relief, avoidance-driven sensitization, and supported learning—were independently multiplied by \(0.9\), \(1.0\), or \(1.1\), producing \(3^5=243\) combinations. In all 243 combinations, suppression retained the higher short-horizon score, supported engagement retained the higher long-horizon score, and unbuffered confrontation exceeded the protected distress threshold. The smallest short-horizon score gap was approximately \(0.0594\); the smallest long-horizon gap was approximately \(0.3129\); and the smallest unbuffered threshold excess was approximately \(0.0856\).

### F.8.2 Single-mechanism removals

A \(\pm10\%\) grid varies magnitudes without testing whether a sign assumption is individually necessary. E.1.1 therefore sets five load-bearing coefficients to zero one at a time:

| Removed modeled pathway | Suppression minus supported, short score | Supported minus suppression, long score | Long-horizon winner |
|---|---:|---:|---|
| Avoidance-driven sensitization | 0.09959 | 0.19652 | Supported engagement |
| Engagement-driven desensitization | 0.14453 | 0.31109 | Supported engagement |
| Overload cost to capacity | 0.09029 | 0.37005 | Supported engagement |
| Avoidance cost to functioning | 0.09942 | 0.30187 | Supported engagement |
| Distress cost to functioning | 0.08845 | 0.38411 | Supported engagement |

Suppression remains the short-horizon winner in all five cases. No single one of these five sign assumptions is necessary for the identities of the two winners.

A sixth check removes support from both learning gates by replacing \(\min(1,c_t+h_t)\) with \(\min(1,c_t)\), while retaining support's direct distress and capacity effects. Suppression still wins under the short weights by approximately \(0.11273\), and supported engagement still wins under the long weights by approximately \(0.34970\).

### F.8.3 Explicit alternative initial states

The independent audit reported robustness across alternative initial states but did not specify their exact values. E.1.1 therefore supplies a separate reproducible suite:

| Case | Initial state \((d,s,f,c)\) | Short-horizon winner | Long-horizon winner |
|---|---|---|---|
| Low capacity | \((0.15,0.25,0.80,0.25)\) | Suppression | Supported engagement |
| High distress | \((0.65,0.25,0.80,0.55)\) | Suppression | Supported engagement |
| High sensitization | \((0.15,0.80,0.80,0.55)\) | Suppression | Supported engagement |
| Reduced functioning | \((0.15,0.25,0.45,0.55)\) | Suppression | Supported engagement |

These checks show that the winner identities are not carried by one coefficient or by the baseline initial state. They do not show parameter identification, clinical generality, or structural neutrality.

### F.8.4 Why this robustness is not clinical evidence

The supported regime is uniquely assigned substantial engagement and substantial support, while the equations reward their combination across several pathways. It is therefore unsurprising that its long-horizon advantage survives removal of any one pathway. The robustness checks establish internal redundancy in a deliberately constructed example. They do not establish that actual supported engagement has these effects, that the state variables measure clinical processes, or that the regime labels map onto named therapies.

## F.9 What the construction establishes

The construction establishes only that:

- immediate relief and later challenge response can diverge in a declared model;
- two non-dominating profiles can reverse rank under different declared weights;
- a third profile can be excluded independently by a protected floor and by strict dominance;
- support can change the modeled profile effect of engagement;
- protected floors are not ordinary weights; and
- robust behavior inside a constructed model can reflect the redundancy built into its regime definitions.

It does not establish that one regime maps onto a named psychotherapy, that supported engagement is clinically superior, that distress should be maximized, that avoidance should always be reduced, or that the equations describe trauma treatment. The winning long-horizon regime was defined to combine the variables that the model rewards. That fact explains why the construction cannot serve as evidence for the intervention it evokes.

---

# References

Ainsworth, M. D. S., Blehar, M. C., Waters, E., & Wall, S. (1978). *Patterns of attachment: A psychological study of the strange situation*. Erlbaum.

Alegría, M., NeMoyer, A., Falgàs Bagué, I., Wang, Y., & Alvarez, K. (2018). Social determinants of mental health: Where we are and where we need to go. *Current Psychiatry Reports, 20*, 95.

Bartlett, F. C. (1932). *Remembering: A study in experimental and social psychology*. Cambridge University Press.

Billings, J., & Nicholls, H. (2025). PTSD and complex PTSD, current treatments and debates: A review of reviews. *British Medical Bulletin, 156*(1), ldaf015. https://doi.org/10.1093/bmb/ldaf015

Bonanno, G. A., & Burton, C. L. (2013). Regulatory flexibility: An individual-differences perspective on coping and emotion regulation. *Perspectives on Psychological Science, 8*(6), 591–612.

Borsboom, D. (2017). A network theory of mental disorders. *World Psychiatry, 16*(1), 5–13.

Bowlby, J. (1969). *Attachment and loss: Vol. 1. Attachment*. Basic Books.

Campbell, J. D., Trapnell, P. D., Heine, S. J., Katz, I. M., Lavallee, L. F., & Lehman, D. R. (1996). Self-concept clarity: Measurement, personality correlates, and cultural boundaries. *Journal of Personality and Social Psychology, 70*(1), 141–156.

Candia-Rivera, D., Engelen, T., Babo-Rebelo, M., & Salamone, P. C. (2024). Interoception, network physiology and the emergence of bodily self-awareness. *Neuroscience & Biobehavioral Reviews, 165*, 105864. https://doi.org/10.1016/j.neubiorev.2024.105864

Carhart-Harris, R. L., & Friston, K. J. (2019). REBUS and the anarchic brain: Toward a unified model of the brain action of psychedelics. *Pharmacological Reviews, 71*(3), 316–344.

Clark, A. (2013). Whatever next? Predictive brains, situated agents, and the future of cognitive science. *Behavioral and Brain Sciences, 36*(3), 181–204.

Clamor, A., Lincoln, T. M., & Schulze, L. (2026). Emotion regulation in mental disorders: A systematic review and multilevel meta-analysis of transdiagnostic and disorder-specific impairments. *Psychological Bulletin, 152*(2), 157–200. https://doi.org/10.1037/bul0000512

Clemente, R., Murphy, A., & Murphy, J. (2024). The relationship between self-reported interoception and anxiety: A systematic review and meta-analysis. *Neuroscience & Biobehavioral Reviews, 167*, 105923. https://doi.org/10.1016/j.neubiorev.2024.105923

Coan, J. A., & Sbarra, D. A. (2015). Social baseline theory: The social regulation of risk and effort. *Current Opinion in Psychology, 1*, 87–91.

Crompton, C. J., Ropar, D., Evans-Williams, C. V. M., Flynn, E. G., & Fletcher-Watson, S. (2020). Autistic peer-to-peer information transfer is highly effective. *Autism, 24*(7), 1704–1712. https://doi.org/10.1177/1362361320919286

Crompton, C. J., Foster, S. J., Wilks, C. E. H., Dodd, M., Efthimiou, T. N., Ropar, D., Sasson, N. J., Lages, M., & Fletcher-Watson, S. (2025). Information transfer within and between autistic and non-autistic people: A registered report. *Nature Human Behaviour, 9*(7), 1488–1500. https://doi.org/10.1038/s41562-025-02163-z

Cuijpers, P., Miguel, C., Ciharova, M., Harrer, M., Basic, D., Cristea, I. A., et al. (2024). Absolute and relative outcomes of psychotherapies for eight mental disorders: A systematic review and meta-analysis. *World Psychiatry, 23*(2), 267–275. https://doi.org/10.1002/wps.21203

Deci, E. L., & Ryan, R. M. (2000). The “what” and “why” of goal pursuits: Human needs and the self-determination of behavior. *Psychological Inquiry, 11*(4), 227–268.

Elsey, J. W. B., Van Ast, V. A., & Kindt, M. (2018). Human memory reconsolidation: A guiding framework and critical review of the evidence. *Psychological Bulletin, 144*(8), 797–848.

Festinger, L. (1957). *A theory of cognitive dissonance*. Stanford University Press.

Fisher, A. J., Medaglia, J. D., & Jeronimus, B. F. (2018). Lack of group-to-individual generalizability is a threat to human subjects research. *Proceedings of the National Academy of Sciences, 115*(27), E6106–E6115.

Flückiger, C., Del Re, A. C., Wampold, B. E., & Horvath, A. O. (2018). The alliance in adult psychotherapy: A meta-analytic synthesis. *Psychotherapy, 55*(4), 316–340.

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience, 11*, 127–138.

Galatzer-Levy, I. R., Huang, S. H., & Bonanno, G. A. (2018). Trajectories of resilience and dysfunction following potential trauma: A review and statistical evaluation. *Clinical Psychology Review, 63*, 41–55.

Greig, L., Coundouris, S. P., & Henry, J. D. (2026). Autistic traits and camouflaging: A meta-analysis. *Autism, 30*(6), 1398–1415. https://doi.org/10.1177/13623613261437500

Gross, J. J. (2002). Emotion regulation: Affective, cognitive, and social consequences. *Psychophysiology, 39*(3), 281–291.

Gross, J. J. (2015). Emotion regulation: Current status and future prospects. *Psychological Inquiry, 26*(1), 1–26.

Hofmann, S. G., & Hayes, S. C. (2019). The future of intervention science: Process-based therapy. *Clinical Psychological Science, 7*(1), 37–50.

Hohwy, J. (2013). *The predictive mind*. Oxford University Press.

Kashdan, T. B., & Rottenberg, J. (2010). Psychological flexibility as a fundamental aspect of health. *Clinical Psychology Review, 30*(7), 865–878.

King, L. A., & Hicks, J. A. (2021). The science of meaning in life. *Annual Review of Psychology, 72*, 561–584.

Kotov, R., Krueger, R. F., Watson, D., Achenbach, T. M., Althoff, R. R., Bagby, R. M., et al. (2017). The Hierarchical Taxonomy of Psychopathology (HiTOP): A dimensional alternative to traditional nosologies. *Journal of Abnormal Psychology, 126*(4), 454–477.

Lee, J. L. C., Nader, K., & Schiller, D. (2017). An update on memory reconsolidation updating. *Trends in Cognitive Sciences, 21*(7), 531–545.

Lind, M., Ture, S., McAdams, D. P., & Cowan, H. R. (2024). Narrative identity, traits, and trajectories of depression and well-being: A 9-year longitudinal study. *Psychological Science, 35*(12), 1325–1339. https://doi.org/10.1177/09567976241296512

Lindahl, J. R., Fisher, N. E., Cooper, D. J., Rosen, R. K., & Britton, W. B. (2017). The varieties of contemplative experience: A mixed-methods study of meditation-related challenges in Western Buddhists. *PLOS ONE, 12*(5), e0176239.

Loftus, E. F. (2005). Planting misinformation in the human mind: A 30-year investigation of the malleability of memory. *Learning & Memory, 12*(4), 361–366.

Lund, C., Brooke-Sumner, C., Baingana, F., Baron, E. C., Breuer, E., Chandra, P., et al. (2018). Social determinants of mental disorders and the Sustainable Development Goals: A systematic review of reviews. *The Lancet Psychiatry, 5*(4), 357–369.

Lunansky, G., Bonanno, G. A., Blanken, T. F., van Borkulo, C. D., Cramer, A. O. J., & Borsboom, D. (2025). Bouncing back from life's perturbations: Formalizing psychological resilience from a complex systems perspective. *Psychological Review, 132*(6), 1396–1409. https://doi.org/10.1037/rev0000497

Macri, J. A., & Rogge, R. D. (2024). Examining domains of psychological flexibility and inflexibility as treatment mechanisms in acceptance and commitment therapy: A comprehensive systematic and meta-analytic review. *Clinical Psychology Review, 110*, 102432. https://doi.org/10.1016/j.cpr.2024.102432

Martela, F., & Steger, M. F. (2016). The three meanings of meaning in life: Distinguishing coherence, purpose, and significance. *The Journal of Positive Psychology, 11*(5), 531–545.

McAdams, D. P. (2001). The psychology of life stories. *Review of General Psychology, 5*(2), 100–122.

McAdams, D. P., & McLean, K. C. (2013). Narrative identity. *Current Directions in Psychological Science, 22*(3), 233–238.

Nel, J., Spedding, M., & Malcolm-Smith, S. (2025). Consolidating a framework of autistic camouflaging strategies: An integrative systematic review. *Autism, 29*(10), 2379–2394. https://doi.org/10.1177/13623613251335472

Nejadghaderi, S. A., Mousavi, S. E., Fazlollahi, A., Motlagh Asghari, K., & Garfin, D. R. (2024). Efficacy of yoga for posttraumatic stress disorder: A systematic review and meta-analysis of randomized controlled trials. *Psychiatry Research, 340*, 116098. https://doi.org/10.1016/j.psychres.2024.116098

Pellicano, E., & den Houting, J. (2022). Annual research review: Shifting from “normal science” to neurodiversity in autism science. *Journal of Child Psychology and Psychiatry, 63*(4), 381–396.

Rader, G. K. D. (2026a). *Coherence Universalism: Physics—Coherence, accessibility, and the ordered emergence of physical description* (Systematic Reconstruction A.6.1). Heaven≡Earth Foundation.

Rader, G. K. D. (2026b). *Coherence Universalism: Metaphysics and epistemology* (Version 0.10). Heaven≡Earth Foundation.

Rader, G. K. D. (2026c). *Coherence Universalism: Foundations* (Version 0.10). Heaven≡Earth Foundation.

Rader, G. K. D. (2026d). *Coherence Universalism: Biology—Life as active self-maintenance* (Systematic Reconstruction C.1.1). Heaven≡Earth Foundation.

Rader, G. K. D. (2026e). *Coherence Universalism: Consciousness* (Systematic Reconstruction D.1.1). Heaven≡Earth Foundation.

Rader, G. K. D. (2026f). *Denying knowledge to make room for commitment: A coherence-based warrant relation for non-truth-apt discourse* (Working draft). Heaven≡Earth Foundation.

Salkovskis, P. M., Sighvatsson, M. B., & Sigurdsson, J. F. (2024). How effective psychological treatments work: Mechanisms of change in cognitive behavioural therapy and beyond. *Behavioural and Cognitive Psychotherapy, 51*(6), 595–615. https://doi.org/10.1017/S1352465823000590

Sbarra, D. A., & Hazan, C. (2008). Coregulation, dysregulation, self-regulation: An integrative analysis and empirical agenda for understanding adult attachment, separation, loss, and recovery. *Personality and Social Psychology Review, 12*(2), 141–167.

Schacter, D. L. (1996). *Searching for memory: The brain, the mind, and the past*. Basic Books.

Schaug, J. P., Møller, L., Reinholt, N., Illum, D. B., Græbe, F. L., Mikkelsen, L. B., et al. (2025). Psychotherapies for adults with complex presentations of PTSD: A clinical guideline and five systematic reviews with meta-analyses. *BMJ Mental Health, 28*(1), e301158. https://doi.org/10.1136/bmjment-2024-301158

Schumacher, L., Burger, J., Echterhoff, J., & Kriston, L. (2024). Methodological and statistical practices of using symptom networks to evaluate mental health interventions: A review and reflections. *Multivariate Behavioral Research, 59*(4), 663–676. https://doi.org/10.1080/00273171.2024.2335401

Steger, M. F., Frazier, P., Oishi, S., & Kaler, M. (2006). The Meaning in Life Questionnaire: Assessing the presence of and search for meaning in life. *Journal of Counseling Psychology, 53*(1), 80–93.

U.S. Department of Veterans Affairs & U.S. Department of Defense. (2023). *VA/DoD clinical practice guideline for management of posttraumatic stress disorder and acute stress disorder*. Authors.

Wampold, B. E., & Imel, Z. E. (2015). *The great psychotherapy debate: The evidence for what makes psychotherapy work* (2nd ed.). Routledge.

Westhoff, M., Berg, M., Reif, A., Rief, W., & Hofmann, S. G. (2024). Major problems in clinical psychological science and how to address them: Introducing a multimodal dynamical network approach. *Cognitive Therapy and Research, 48*(5), 791–807. https://doi.org/10.1007/s10608-024-10487-9

World Health Organization. (2022). *World mental health report: Transforming mental health for all*. Author.

World Health Organization. (2024). *Clinical descriptions and diagnostic requirements for ICD-11 mental, behavioural and neurodevelopmental disorders*. Author.

---

# Glossary

**Acute relief.** Reduction in immediate distress or arousal. It is one outcome dimension and does not by itself establish recovery, safety, or long-horizon benefit.

**Affected-person scope.** The set of people whose benefits, burdens, agency, and risks are included in an evaluation.

**Agency.** Graded capacity to perceive options, form or endorse aims, initiate action, monitor consequences, revise strategy, and act under conditions not wholly controlled by coercion or incapacity.

**Attractor language.** A dynamical description that is warranted only when states, transitions, perturbations, return tendencies, and basin structure are operationalized.

**Commitment register.** The register in which utterances principally orient value, identity, trust, practice, or action and are evaluated by warrant and integrity rather than truth alone. Commitments remain constrained by established descriptive facts.

**Co-regulation.** Regulation distributed across interaction with another person or group, including modulation of threat, attention, affect, effort, interpretation, and recovery.

**Description register.** The register of truth-apt claims answerable to evidence, valid inference, calibration, and correction.

**Descriptive adequacy.** Fit between a person's or model's representations and the relevant world, including responsiveness to disconfirming evidence. It is not equivalent to internal consistency.

**Developmental path dependence.** The dependence of later possibilities, costs, sensitivities, and meanings on prior states and histories, without implying determinism.

**Egoic self-maintenance.** Durable coupling of a self-model to protection of its identity, status, resources, authority, narrative, or continued control. It is distinct from minimal self-location or task-relative self-modeling.

**Embodied regulation.** Psychological regulation as constrained and enabled by interoceptive, autonomic, sensorimotor, energetic, pain, sleep, illness, and environmental conditions.

**Field Coherence Score.** A scalar proposed in the March 2026 Psychology paper. It is retired as a universal measure in E.1.1.

**Fragmentation.** Separation among processes, memories, affects, roles, or self-states that substantially restricts flexible access, reality contact, agency, relationship, or repair in the declared context and horizon. Structural separation alone is not sufficient.

**Integration load.** The profile of demands requiring coordination, tolerance, interpretation, action, deferral, delegation, escape, or compartmentalization.

**Integration overload.** A condition in which declared demands fall outside the person's context-sensitive regulatory capacity region for the relevant horizon.

**Inverse Entropic Stress.** A proposed cross-domain metric from the source paper. E.1.1 retires it as a canonical psychological quantity.

**Local–global tension.** Conflict between effects on a subsystem or narrow role and effects on the wider person, relationship, context, or affected population.

**Meaning.** A relation through which an event, state, symbol, action, person, or possibility bears consequence, salience, purpose, significance, identity relevance, practical affordance, or sacred orientation.

**Meaning crisis.** In E.1.1, a family of testable hypotheses concerning loss or conflict of comprehension, purpose, mattering, belonging, trusted institutions, feasible agency, and future orientation—not one established population-level latent entity.

**Meaning map.** A structured, revisable relation among cues, interpretations, affective and bodily responses, memories, commitments, expected consequences, and action tendencies.

**Meaning space.** A model-dependent set of distinctions along which things can matter to a person or group for a declared question.

**Non-dominance.** A relation between profiles in which each is better on at least one dimension and worse on at least one other dimension; neither is unconditionally superior.

**Phenomenal valence.** Felt pleasantness, unpleasantness, attraction, aversion, or affective better–worse character. It is distinct from reward signals, functional stake, behavioral preference, and verbal emotion concepts.

**Protected floor.** A threshold that is not treated as ordinarily compensable by gains on other profile dimensions, such as immediate safety, consent, or basic agency.

**Protective compartmentalization.** Context-sensitive separation that preserves functioning or safety when fuller access or integration would exceed capacity or produce unacceptable risk.

**Psychological coherence.** Integrated psychological organization under declared constraints. It is an umbrella relational concept in E.1.1, not a universal scalar, diagnosis, or synonym for conformity.

**Psychological coherence infrastructure.** Material, relational, informational, institutional, and cultural conditions that scaffold or burden psychological regulation, meaning, agency, and repair.

**Psychological coherence profile.** A declared vector or structured profile of psychological dimensions used for a particular research, clinical, or policy question.

**Psychological flexibility.** Capacity to vary attention, interpretation, emotion-regulation strategy, action, and commitment in context-sensitive service of viable aims and values.

**Reality contact.** Responsiveness of belief and interpretation to relevant external constraints and corrective evidence. It should not be reduced to conformity with a group or authority.

**Regulatory capacity.** The context-sensitive set of demands and responses that a person can tolerate, coordinate, transform, defer, delegate, or escape without crossing declared protected floors.

**Repair.** Detection and workable response to mismatch, injury, or rupture through revision, support, restitution, accommodation, boundary, environmental change, or transformation. Repair need not restore the prior state.

**Resilience.** A family of trajectory properties involving maintenance, recovery, adaptation, or transformation under specified challenges and horizons. It is not a permanent trait or absence of distress.

**Scalarization.** Conversion of a multidimensional profile into one score by applying declared normalizations and weights. Scalarization is a decision procedure, not discovery of a natural total order.

**Self-deception.** Motivated asymmetric processing that protects a stake by selectively excluding, reframing, discounting, or neutralizing relevant reasons. It is not synonymous with false belief, disagreement, bias, or unconscious defense.

**Self-model.** A representation or enacted organization concerning the system's own state, role, boundary, capacities, uncertainty, or prospective action. It need not constitute a persistent ego.

**Social scaffold.** A relationship, practice, institution, material resource, or information structure that expands or stabilizes capacities not available to the person in isolation.

**Stake.** A condition under which outcomes are better or worse relative to maintenance of an organization or pursuit of an endorsed aim. Functional stake does not by itself establish phenomenal feeling or moral status.

**Symptom network.** A model representing symptoms or related variables as mutually interacting nodes. Network estimation does not automatically reveal individual causal structure.

**Thin perspective.** In Consciousness D.1.1, a candidate form of limited, episodic, or internally plural perspective with unresolved temporal depth, unity, self-maintenance, and valence.

**Trauma-related adaptation.** A change in threat processing, memory, affect, body, identity, relationship, or agency associated with overwhelming or persistent conditions. The phrase does not imply one universal mechanism or trajectory.

**Viable aim.** An aim that remains compatible with declared protected constraints and affected-person scope. Psychological desire or commitment alone does not establish viability or moral permissibility.

---

# Closing status statement

E.1.1 is a systematic working reconstruction. It does not authorize clinical diagnosis or treatment, establish a universal theory of mind, or show that the profile dimensions form one natural kind. Its contribution is architectural: it preserves the integrative ambitions of the March 2026 Psychology paper while making the constructs explicit, separating the registers, exposing tradeoffs, and specifying where evidence can confirm, qualify, or defeat the framework.

The independent audit has closed the Appendix F reproducibility cycle and confirmed that the retired scalar architecture did not return. It did not constitute clinical, community, or comprehensive conceptual review. CU-Ψ1 through CU-Ψ12 therefore remain provisional, Foundations B.2 remains unchanged, and promotion of CU-Ψ8 or neurodiversity-related principles requires affected-community participation with substantive authority. Downstream papers may cite E.1.1 as the working Psychology authority while preserving these review boundaries.


# Commitment Principle Crosswalk

CU-COM10 — **Healing as Sacred Repair** is the official commitment anchor for the reader-facing manuscript.

**Statement:** Coherence Universalism commits to treating psychological healing as sacred work: the restoration or widening of a person’s capacity to encounter reality, inhabit the body, bear feeling, remember, choose, relate, and imagine a future beyond what once had to be survived.

**Boundary:** Sacred healing never sanctifies harm, forces disclosure or integration, requires forgiveness or reconciliation, or replaces evidence-based medical and clinical care.

**Revision condition:** The commitment must be revised when its language pressures survivors, pathologizes protective difference, erases structural conditions, or privileges spiritual meaning over safety and autonomy.
