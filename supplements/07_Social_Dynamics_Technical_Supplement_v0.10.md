# Coherence Universalism: Social Dynamics
## RC3 Release-Convergence Wave 4 — Technical Supplement

**Status and authority.** This is the released technical supplement for the Wave 4 cumulative manuscript. The [reader-facing manuscript](../papers/07_CU_Social_Dynamics_v0.10.md) controls current wording, claim status, and canonical cross-references. This supplement exposes the formal derivations, deterministic contrast constructions, claim ledgers, audit materials, scripts, and source records on which the manuscript relies.

- **Evidence directory:** [07_Social_Dynamics](../evidence/07_Social_Dynamics/README.md)
- **Archived source package:** [CU_Social_Dynamics_v0.10_Publication_PC2.zip](../provenance/archival_source_packages/CU_Social_Dynamics_v0.10_Publication_PC2.zip)
- **Current supplement path:** `technical_supplements/07_Social_Dynamics_Technical_Supplement_v0.10.md`

Reproducibility of a construction shows only that its output follows from its declared assumptions and code. It does not convert a toy model or simulation into target-domain empirical validation. Where this preserved archive uses historical identifiers or statuses, the Wave 4 normalized registries and current manuscript control.

# Wave 4 evidence-access addendum

Wave 4 makes previously referenced but inaccessible materials available in one package. It includes the substantive legacy supplement below, the independent audit and check script, recorded audit output where available, source ledgers, deterministic scripts and generated results where they existed, and the complete pre-RC3 source package for provenance.

The manuscript now includes a concise reader-facing summary of the institutional-correction construction, including the distributed shift, emergency, false-alarm, scalarization, and feedback-delay results.

# Preserved substantive technical archive

**Gaura Kiśora Dās Rader**  
**Heaven≡Earth Foundation**  
**September 2026**

---

## Scope

This supplement preserves the formal, numerical, registry, audit, and source-provenance layers supporting the reader-facing Social Dynamics manuscript. It does not independently validate the social-scientific, historical, political, or normative claims.

The principal technical authority is the independently audited and bounded-repair Social Dynamics reconstruction. Canonical Base B.4 governs framework definitions and principle status. Open Myth and CU-CL-12 remain provisional during Publication Candidate 1.

## Contents

1. Formal architecture and non-entailments
2. Deterministic institutional-correction contrast model
3. Complete claim and evidence ledger
4. Full social, institutional, economic, and cultural principle registry
5. Literature and operationalization ledger
6. Glossary
7. Open Myth and mythic–constitutional alignment architecture
8. Independent audit and bounded repair disposition
9. Editorial source map and reproduction boundary

---

# Appendix A. Formal Architecture and Non-Entailments

## A.1 Social models are indexed

For a social claim to be well formed, it must identify at least

\[
(\mathcal S,A,K,P,\pi,T,\mathcal O),
\]

where \(\mathcal S\) is the social unit, \(A\) the affected-agent set, \(K\) the protected constraints, \(P\) the power relation, \(\pi\) the boundary and scale, \(T\) the horizon, and \(\mathcal O\) the observation model.

A statement such as “trust is declining” is incomplete until it specifies trust in whom, by whom, concerning what domain, measured how, and over what period.

## A.2 Profile dominance

Let \(p,q\in\mathbb R^m\) be social profiles oriented so that higher values are preferable after all cost coordinates have been sign-reversed. Then \(p\) weakly Pareto-dominates \(q\) if

\[
p_j\ge q_j
\quad\text{for every }j,
\]

and strictly dominates if the inequality is strict for at least one coordinate.

If neither profile dominates, a total ranking requires additional value commitments, weights, thresholds, or decision rules. The data alone do not select them.

## A.3 Aggregate masking proposition

**Proposition A.1.** A higher aggregate mean does not entail satisfaction of every affected-group floor.

**Proof.** Let

\[
a=(0.90,0.90,0.20),
\qquad
b=(0.65,0.65,0.65).
\]

Then

\[
\bar a=\frac{2.00}{3}=0.666\ldots
>
0.65=\bar b.
\]

For protected floor \(k=0.40\),

\[
\min a=0.20<k,
\qquad
\min b=0.65\ge k.
\]

Therefore the higher mean is compatible with a floor violation absent from the lower-mean profile. \(\square\)

This elementary result is sufficient to reject any procedure that treats aggregate improvement as automatically compensating concentrated harm.

## A.4 Compliance non-entailment

**Proposition A.2.** Equal observed compliance does not entail equal consent, coercion, or legitimacy.

**Construction.** Consider two institutions with observed compliance \(0.95\). In the first, meaningful voice is \(0.10\) and coercive dependence \(0.90\). In the second, voice is \(0.85\) and coercive dependence \(0.10\). The behavioral aggregate is identical while the generating relations differ.

The construction does not prove that the second institution is normatively legitimate. It proves only that compliance is insufficient to decide the question.

## A.5 Trust non-entailment

Let \(T_{ag}\) denote agent \(a\)'s trust in institution \(g\), and let \(W_g\) denote a multidimensional assessment of the institution's trustworthiness. No logical implication holds in either direction:

\[
T_{ag}\not\Rightarrow W_g,
\qquad
W_g\not\Rightarrow T_{ag}.
\]

Historical betrayal can make low trust rational even after reform. Propaganda or dependency can produce high trust in an untrustworthy authority. Trust and trustworthiness require separate evidence.

## A.6 Voice non-entailment

Protected voice does not entail accuracy:

\[
V_g>0
\not\Rightarrow
\Pr(\text{claim}_g\text{ is true})=1.
\]

Nor does error entail that voice should be removed. An institution can protect the right to present a claim while evaluating its evidence through transparent procedures.

## A.7 Coordination non-entailment

Coordination capacity \(C\) does not by itself entail legitimacy \(L\), justice \(J\), or truth-sensitive correction \(I\):

\[
C\not\Rightarrow L,
\qquad
C\not\Rightarrow J,
\qquad
C\not\Rightarrow I.
\]

The same logistics that distribute medicine can distribute repression. The same communication network that supports mutual aid can coordinate harassment.

## A.8 Scalarization sensitivity

For profile \(p\) and nonnegative weights \(w\) with \(\sum_jw_j=1\), define

\[
S_w(p)=\sum_jw_jp_j.
\]

When two profiles are non-dominating, there may exist \(w,w'\) such that

\[
S_w(p)>S_w(q)
\quad\text{and}\quad
S_{w'}(p)<S_{w'}(q).
\]

The scalarization is not invalid. Its normative and decision-theoretic content lies partly in the weights. They must therefore be disclosed rather than represented as measurement alone.

## A.9 Protected-floor admissibility

Let \(K\subseteq\mathbb R^m\) be the admissible region defined by protected floors. A profile may maximize a score over all options while lying outside \(K\). A defensible procedure is therefore:

1. identify options satisfying the declared floors;
2. compare admissible profiles under the declared decision rule;
3. report which options were excluded and why.

This is not a theorem that every moral problem admits clear floors. It is a safeguard against compensating severe local harm with unrelated aggregate benefit without argument.

## A.10 Institution-relative viability

A social institution's viability is not the same as the welfare or agency of those subject to it. Let \(V_{\mathrm{inst}}\) denote conditions for organizational continuation and \(V_g\) conditions protected for group \(g\). Then

\[
V_{\mathrm{inst}}
\not\Rightarrow
\bigcap_g V_g.
\]

An institution can preserve itself by degrading the conditions of its members. Institutional self-maintenance therefore has no automatic normative priority.

## A.11 Centralization and decentralization

No unconditional ordering holds between centralization and decentralization. Performance depends on at least:

- distribution of information;
- time pressure;
- externalities;
- coordination costs;
- local capture;
- central capture;
- reversibility;
- and available appeal.

Appendix B supplies a constructed example in which centralized suppression is fastest in one context and fails badly in another.

## A.12 Causal claims

A social causal claim should distinguish:

- intervention on a variable;
- selection into exposure;
- common cause;
- mediation;
- feedback;
- and measurement response.

For example, correlation between institutional trust and policy compliance does not decide whether trust causes compliance, competent institutions cause both, partisan alignment shapes both reports, or compulsory dependence produces compliance without trust.

## A.13 Network claims

A network statistic is relative to a defined graph: nodes, edges, direction, weight, time, and missingness. “Connectivity” can refer to communication, friendship, influence, material dependence, co-membership, or digital interaction. Results do not automatically transfer across these graphs.

## A.14 Attractors and social regimes

Attractor language is legitimate in a declared dynamical model. Let

\[
x_{t+1}=F(x_t;\theta)
\]

with specified state space and parameters. A set \(A\) is attracting only relative to the dynamics, basin, topology, and time scale.

Country clusters, recurrent narratives, or stable institutions are not thereby mathematical attractors. The term remains a hypothesis until trajectories and convergence properties are established.

## A.15 Critical transitions

Early-warning indicators derived near local bifurcations do not become generic by analogy. A social application must show why the relevant transition has the assumed dynamical structure and why the observed indicator is not produced by seasonality, changing measurement, strategic behavior, exogenous shock, or ordinary heterogeneity.

## A.16 Institutional repair as counterfactual capacity

Repair capacity can be evaluated counterfactually. Holding a class of errors or harms fixed, compare trajectories under:

- no appeal;
- nominal appeal without reversal authority;
- independent appeal with record correction;
- and appeal joined to restitution and rule change.

The relevant outcomes include recurrence, time to remedy, distribution of burden, and restoration of standing. Complaint count alone is ambiguous.

# Appendix B. Deterministic Institutional-Correction Contrast Model

## B.1 Purpose

The model illustrates four non-entailments:

1. fast centralized implementation need not imply good distributed correction;
2. protected voice need not imply that every dissenting signal is accurate;
3. an aggregate performance score can mask protected-floor violations; and
4. different nonnegative scalarizations can rank the same institutional profiles differently.

It does not model an actual society or identify a universally optimal political form.

## B.2 Contexts

The model contains three groups and sixty discrete decision steps. A public requirement \(\theta_t\) and group-specific signals \(s_{g,t}\) define three contexts.

### B.2.1 Distributed shift

\[
\theta_t=
\begin{cases}
0.30,&t<20,\\
0.80,&t\ge20.
\end{cases}
\]

Group 1 observes the shift immediately. Group 2 receives an administrative signal with update rate \(0.18\). Group 3 receives a more slowly updating signal with rate \(0.08\), of which \(25\%\) remains anchored to the prior baseline.

This represents a case in which locally exposed actors perceive a change before incumbent channels.

### B.2.2 Clear common emergency

The requirement follows the same shift, but all three groups observe it immediately.

### B.2.3 False alarm

The true requirement remains \(0.30\). Group 1 reports \(0.80\) for six steps while the other two signals remain accurate.

The false-alarm case prevents the model from building “dissent is correct” into the framework.

## B.3 Institutional architectures

### B.3.1 Centralized suppression

- report openness: \((0.15,0.80,1.00)\);
- fixed authority weights: \((0.10,0.35,0.55)\);
- estimate update rate: \(0.75\);
- implementation rate: \(0.90\);
- distributed burdens: \((0.23,0.06,0.02)\).

The locally exposed group has the weakest transmission and highest burden.

### B.3.2 Majoritarian openness

- report openness: \((1,1,1)\);
- aggregation: median report;
- estimate update rate: \(0.65\);
- implementation rate: \(0.65\);
- burdens: \((0.06,0.06,0.06)\).

All reports enter, but one group cannot move the median by itself.

### B.3.3 Contestable polycentricity

- report openness: \((1,1,1)\);
- aggregation: reliability-weighted mean;
- estimate update rate: \(0.55\);
- implementation rate: \(0.55\);
- burdens: \((0.04,0.04,0.04)\).

Reliability weights update from a decaying record of observed signal error. The construction assumes that the true contextual requirement becomes observable after each decision. Real institutions often lack such rapid feedback; this is a strong simplifying assumption.

## B.4 Equations

Let \(e_t\) be the institutional estimate and \(a_t\) the implemented action. Received report \(r_{g,t}\) is

\[
r_{g,t}
=
e_t+o_g(s_{g,t}-e_t),
\]

where \(o_g\in[0,1]\) is report openness.

For fixed-weight aggregation,

\[
\widehat\theta_t
=
\sum_gw_gr_{g,t}.
\]

For majoritarian aggregation,

\[
\widehat\theta_t
=
\operatorname{median}_g r_{g,t}.
\]

For adaptive aggregation,

\[
w_{g,t}
=
\frac{\exp(-\gamma E_{g,t})}{\sum_h\exp(-\gamma E_{h,t})},
\]

where

\[
E_{g,t+1}
=
\mu E_{g,t}+(1-\mu)(s_{g,t}-\theta_t)^2,
\]

with \(\mu=0.40\) and \(\gamma=40\).

The estimate and implemented action update as

\[
e_{t+1}
=
e_t+\eta(\widehat\theta_t-e_t),
\]

\[
a_{t+1}
=
a_t+\kappa(e_{t+1}-a_t).
\]

Group welfare is the constructed quantity

\[
y_{g,t}
=
1-\rho_g|a_t-\theta_t|-b_g,
\]

with sensitivities

\[
\rho=(1.10,0.85,1.25)
\]

and regime-specific burdens \(b_g\).

The protected material floor is \(0.35\). The voice floor is minimum report openness \(0.30\).

### B.4.1 Recording and metric-window conventions

At decision index \(t\), reports are formed from the pre-update estimate \(e_t\); the estimate and action are then updated, and the stored action value is \(a_{t+1}\). Every mismatch statistic pairs this post-update action with the requirement \(\theta_t\).

For shock index \(t_s=20\), the six-step cumulative mismatch is

\[
M_6
=
\sum_{t=t_s}^{t_s+5}|a_{t+1}-\theta_t|.
\]

The long-run mean mismatch uses decision indices \(t=t_s+10,\ldots,59\), and the false-alarm deviation uses \(t=t_s,\ldots,t_s+14\).

Correction time is reported as the **one-based number of post-shock updates** to the first observation beginning three consecutive mismatches below \(0.05\):

\[
\tau_{\mathrm{corr}}
=
1+
\min\left\{
 t-t_s:
 |a_{t+j+1}-\theta_{t+j}|<0.05
 \text{ for }j=0,1,2
\right\}.
\]

The accompanying JSON also records the corresponding zero-based `correction_lag_index`. Thus a reported correction time of six means that the qualifying run begins at lag index five, the sixth post-shock updated observation.

### B.4.2 Common-shift invariance of reliability weights

For adaptive weights

\[
w_g(E)
=
\frac{e^{-\gamma E_g}}{\sum_h e^{-\gamma E_h}},
\]

adding the same constant \(c\) to every error score changes no weight:

\[
w_g(E+c\mathbf 1)=w_g(E).
\]

A test that adds identical noise or bias to every reliability score is therefore vacuous in this model. Only relative, asymmetric corruption or delay can change the adaptive weighting.

## B.5 Baseline results

### B.5.1 Distributed shift

| Architecture | Six-step cumulative mismatch | Long-run mean mismatch | Correction time | Minimum group welfare | Material floor | Voice floor |
|---|---:|---:|---:|---:|:---:|:---:|
| Centralized suppression | 2.259473 | 0.125080 | Not reached | 0.256531 | Violated | Violated |
| Majoritarian openness | 1.926166 | 0.013386 | 13 steps | 0.362531 | Satisfied | Satisfied |
| Contestable polycentricity | 1.112662 | 0.023668 | 6 steps | 0.413146 | Satisfied | Satisfied |

Contestable polycentricity detects and corrects the distributed shift fastest. Majoritarian openness has the lowest later average mismatch after the initially lagging median signal catches up. The centralized regime does not enter the declared correction band within the simulated horizon and violates both floors.

### B.5.2 Clear common emergency

| Architecture | Six-step cumulative mismatch | Correction time | Minimum group welfare |
|---|---:|---:|---:|
| Centralized suppression | 0.343647 | 3 steps | 0.533706 |
| Majoritarian openness | 0.535542 | 4 steps | 0.579062 |
| Contestable polycentricity | 0.800178 | 5 steps | 0.524063 |

When every signal is immediate and aligned, the centralized architecture implements the change fastest. This is why F.1.1 rejects unconditional claims that decentralization or broad deliberation is always superior.

### B.5.3 False alarm

| Architecture | Fifteen-step cumulative deviation |
|---|---:|
| Centralized suppression | 0.053254 |
| Majoritarian openness | 0.000000 |
| Contestable polycentricity | 0.167381 |

The median rule fully filters one false signal in this construction. Contestable polycentricity initially responds before reliability updating down-weights the inaccurate source. Protected voice is therefore not automatic authority.

## B.6 Profile coordinates

The model constructs seven normalized coordinates:

- distributed-shift detection;
- distributed-shift long-run adequacy;
- clear-emergency speed;
- false-alarm resistance;
- minimum material welfare;
- minimum report openness;
- and burden fairness.

| Architecture | Dist. detection | Dist. long-run | Emergency speed | False-alarm resistance | Material floor value | Voice | Burden fairness |
|---|---:|---:|---:|---:|---:|---:|---:|
| Centralized suppression | 0.246842 | 0.749841 | 0.885451 | 0.992900 | 0.256531 | 0.150000 | 0.300000 |
| Majoritarian openness | 0.357945 | 0.973228 | 0.821486 | 1.000000 | 0.362531 | 1.000000 | 1.000000 |
| Contestable polycentricity | 0.629113 | 0.952665 | 0.733274 | 0.977683 | 0.413146 | 1.000000 | 1.000000 |

No coordinate is presented as a validated measure of real institutions.

## B.7 Scalarization reversal

Three declared nonnegative weight vectors produce three winners.

| Scalarization | First-ranked architecture | Interpretation |
|---|---|---|
| Emergency command | Centralized suppression | Heavy weight on clear-emergency speed |
| Adaptive legitimacy | Contestable polycentricity | Heavy weight on distributed detection, material floor, and voice |
| Filtering and stability | Majoritarian openness | Heavy weight on false-alarm resistance and long-run adequacy |

The reversal demonstrates that a total ranking imports the purposes and weights of the evaluator.

## B.8 Local sensitivity grid

Five factors are independently multiplied by \(0.90\), \(1.00\), or \(1.10\):

- shock magnitude;
- administrative lag;
- incumbent lag;
- polycentric reliability gain;
- and all institutional update rates.

This yields

\[
3^5=243
\]

local cases. In all 243:

- contestable polycentricity corrects the distributed shift faster than the other two;
- centralized suppression is fastest in the clear emergency;
- majoritarian openness best filters the one-group false alarm;
- centralized suppression violates the distributed-case material floor;
- centralized suppression violates the voice floor; and
- both open regimes satisfy the voice floor.

This is robustness of the declared construction along five local magnitude dimensions. It does **not** vary whether, when, or how accurately the adaptive regime receives outcome feedback. It therefore cannot certify the correction-speed relation along the feedback dimension.

### B.8.1 Feedback-delay sensitivity

Holding all other architecture definitions fixed, F.1.1 delays only the per-group outcome-error observation used by contestable polycentricity. Majoritarian openness remains the reference and corrects in thirteen post-shock updates.

| Polycentric feedback condition | Six-step mismatch | Correction time | Relation to majoritarian correction time |
|---|---:|---:|---|
| Immediate | 1.112662 | 6 | Faster |
| Delayed 1 step | 1.339432 | 6 | Faster |
| Delayed 2 steps | 1.532632 | 7 | Faster |
| Delayed 3 steps | 1.685497 | 8 | Faster |
| Delayed 5 steps | 1.839569 | 9 | Faster |
| Delayed 8 steps | 1.839569 | 12 | Faster |
| Delayed 9 steps | 1.839569 | 13 | Equal |
| Delayed 10 steps | 1.839569 | 14 | Slower |
| Delayed 12 steps | 1.839569 | 15 | Slower |
| No per-group outcome feedback | 1.839569 | 35 | Slower |

The independent audit correctly identified the feedback dependence, but its prose said that the speed relation breaks at a delay of eight steps. Under its own reported table and the now-explicit one-based convention, the adaptive regime remains faster at eight steps, ties at nine, and becomes slower from ten steps onward.

The result decomposes into two construction-specific effects.

1. **Structural inclusion effect.** With feedback disabled, the adaptive mean remains an equal-weight mean. In this distributed-shift case it retains the accurate locally exposed report at weight \(1/3\), whereas the median initially discards that report. The six-step mismatch therefore remains lower than the majoritarian value: \(1.839569<1.926166\). This advantage does not generalize to a false minority signal; B.5.3 displays the opposing case.
2. **Adaptive-speed effect.** Timely observable outcome feedback concentrates weight on the locally accurate source and reduces correction time from thirty-five updates without feedback to six with immediate feedback. This advantage is fragile to delay, asymmetric corruption, nonobservability, or capture of the feedback process.

The feedback sweep is a dedicated structural sensitivity analysis, not an empirical claim that real polycentric institutions receive accurate or timely outcome labels.

## B.9 What is designed into the model

The result is substantially produced by the architecture definitions.

- Centralization is assigned the highest implementation rate.
- The locally informed group is assigned low voice and high burden in the centralized case.
- The majoritarian case uses a median that mechanically rejects one outlier.
- The polycentric case is granted outcome feedback through which signal reliability becomes learnable.
- The feedback-delay sweep assumes that delayed labels remain accurate once they arrive; it does not model selective missingness, strategic label manipulation, unequal observability, or capture of the evaluator.

The model therefore cannot establish that real centralized, majoritarian, or polycentric institutions possess these properties. Its function is diagnostic: once different information environments, feedback conditions, and protected floors are declared, “more integration” no longer determines one winner. In particular, it separates the benefit of retaining a locally accurate minority report from the distinct and much stronger benefit of rapidly learning which source is accurate.

## B.10 Reproduction

The accompanying script is dependency-light and deterministic. It records all parameters, indexing conventions, operational definitions, profiles, scalarizations, counterexamples, the 243-case local grid, and the dedicated feedback-delay sweep in JSON. Automated reproduction is an integrity check, not external validation.

# Appendix C. Claim and Evidence Ledger

## C.1 Purpose and evidence grades

This ledger records the status, evidential basis, and scope of the principal claims made or retired in F.1.1. It is a governance device rather than an assertion that every row has received independent review.

- **E0:** definition, analytic construction, conceptual proposal, or normative commitment;
- **E1:** formal result, counterexample, or controlled illustrative construction;
- **E2:** limited empirical evidence, bounded case evidence, or an emerging literature;
- **E3:** substantial convergent evidence with important scope qualifications; and
- **E4:** mature or broad evidence within the declared scope.

A range indicates that different parts of a synthesis rest on different grades. Normative principles are not made true by empirical frequency, although empirical facts can constrain their application.

## C.2 Ledger

| ID | Claim | Status | Evidence | Scope or condition |
|---|---|---|---|---|
| SOC-C1 | Collective outcomes arise from relations among persons, groups, institutions, infrastructures, technologies, and ecosystems and are not reducible to individual psychology alone. | Bridge principle | E0-E4 | Requires a declared social unit and a comparison showing what the social-level model adds. |
| SOC-C2 | Social coherence is one universal scalar measured by trust, information, coordination, resilience, and extraction. | Retired | — | The constructs are distinct, differently distributed, and not universally commensurable. |
| SOC-C3 | A social model should declare agents, states, environment, actions, dynamics, constraints, networks, power, resource distributions, norms, history, scale, horizon, and observations. | Methodological proposal | E0 | A declaration schema, not a mandatory ontology for every social science. |
| SOC-C4 | Social organization should ordinarily be assessed through a plural profile rather than one default total score. | Bridge principle | E0-E3 | Profile dimensions depend on the question, population, evidence, and normative purpose. |
| SOC-C5 | Non-dominating social profiles can reverse rank under different nonnegative scalarizations. | Formal result | E1 | Exact for the declared constructions; real applications require justified weights and normalization. |
| SOC-C6 | A higher aggregate mean can coexist with a severe protected-floor violation for a subgroup. | Formal result | E1 | Elementary counterexample; the choice and level of floors remain normative and empirical questions. |
| SOC-C7 | Power is a required explanatory variable in social evaluation. | Methodological bridge | E0-E4 | Power must be operationalized for the relevant setting rather than treated as a single substance. |
| SOC-C8 | Protected conditions should be screened separately before compensatory aggregation when severe harms are at issue. | Normative-methodological constraint | E0 | Which conditions are noncompensable requires public and ethical justification. |
| SOC-C9 | Trust and trustworthiness are distinct; neither logically entails the other. | Analytic result / empirical bridge | E0-E4 | Both are domain-, actor-, and history-relative. |
| SOC-C10 | Observed compliance does not establish consent, legitimacy, justice, or low coercion. | Formal non-entailment | E1-E4 | Requires evidence about sanctions, dependency, alternatives, voice, and justification. |
| SOC-C11 | Sociological legitimacy and normative legitimacy must be distinguished. | Analytic distinction | E0-E4 | Perceived appropriateness is evidence about social functioning, not a final moral verdict. |
| SOC-C12 | Measurement and classification can alter the social systems they describe. | Empirical generalization | E2-E4 | Magnitude and direction depend on incentives, visibility, and institutional use. |
| SOC-C13 | Metric absolutism occurs when a proxy displaces the plural purposes and constraints it was introduced to serve. | Provisional diagnostic | E0-E4 | Diagnosis requires evidence of displacement, gaming, or neglected consequences. |
| SOC-C14 | Social coordination arises through mutual adjustment among expectations, signals, norms, incentives, roles, and feedback. | Bridge principle | E0-E4 | No claim that all coordination is voluntary, legitimate, or beneficial. |
| SOC-C15 | Consensus is neither necessary nor sufficient for adequate collective coordination. | Analytic and empirical generalization | E0-E4 | Disagreement can coexist with stable cooperation; consensus can be coerced or mistaken. |
| SOC-C16 | Distributed knowledge can make locally situated actors important correction sources. | Imported synthesis | E2-E4 | Local knowledge can also be partial, strategic, or captured. |
| SOC-C17 | Diversity can improve collective problem solving under some task, independence, communication, and aggregation conditions. | Conditional empirical generalization | E2-E3 | Diversity alone does not guarantee accuracy or justice. |
| SOC-C18 | Social influence can reduce collective accuracy by correlating errors and narrowing independent search. | Imported empirical result | E2-E3 | Effect depends on network, task, incentives, and aggregation. |
| SOC-C19 | Protected dissent is a correction channel, not an automatic truth rule. | Bridge principle | E0-E4 | Protection must be joined to evidence, provenance, response, and accountability. |
| SOC-C20 | Majority rule alone does not protect minority standing or ensure epistemic adequacy. | Normative and empirical generalization | E0-E4 | Democratic value depends on rights, opposition, information, procedure, and correction. |
| SOC-C21 | Centralized action can outperform broader deliberation in some clear and time-critical emergencies. | Conditional result | E1-E3 | Requires aligned signals, legitimate authority, bounded scope, review, and sunset conditions. |
| SOC-C22 | No unconditional performance ordering exists between centralized and decentralized institutions. | Formal and empirical bridge | E1-E4 | Performance depends on information distribution, externalities, time pressure, capture, and reversibility. |
| SOC-C23 | Institutions preserve roles, rules, records, resources, and enforcement beyond particular officeholders. | Empirical generalization | E3-E4 | Continuity does not establish legitimacy or benefit. |
| SOC-C24 | Institutional survival does not entail member welfare or protected agency. | Formal non-entailment | E1-E4 | Institutions may maintain themselves by transferring costs to those they govern. |
| SOC-C25 | Legitimacy is layered across legality, procedure, performance, recognition, contestability, and public justification. | Analytic framework | E0-E4 | The dimensions may conflict and are not collapsed into one score. |
| SOC-C26 | Institutional correctability includes detection, contestation, reversal, record correction, restitution, rule revision, and learning. | Bridge principle | E0-E4 | Nominal complaint channels are insufficient without authority and follow-through. |
| SOC-C27 | Responsibility without authority and authority without accountability are recurrent institutional failure patterns. | Provisional diagnostics | E0-E4 | Application requires role-specific evidence. |
| SOC-C28 | Administrative legibility can enable coordination while erasing local knowledge and functional difference. | Empirical generalization | E2-E4 | Legibility is not intrinsically oppressive; purpose, granularity, and appeal matter. |
| SOC-C29 | Decision authority should be matched to the scale of consequences while preserving local knowledge and agency where compatible. | Normative institutional hypothesis | E0-E3 | Subsidiarity is conditional, not an automatic preference for local control. |
| SOC-C30 | Institutional memory supports continuity but can also preserve obsolete categories, exclusions, and harms. | Empirical generalization | E2-E4 | Memory requires provenance, revision, expiry, and appeal. |
| SOC-C31 | Participation without agenda influence, information, refusal, or response can be tokenistic. | Provisional diagnostic | E0-E4 | Participation must be evaluated by decision impact and burden, not attendance alone. |
| SOC-C32 | Material security is part of the infrastructure of social agency and participation. | Empirical and normative bridge | E2-E4 | Does not imply one sufficient income or resource metric across contexts. |
| SOC-C33 | Resources should be assessed partly through the capabilities they enable under differing bodily, social, geographic, and caregiving conditions. | Imported normative framework | E0-E4 | Capability lists and thresholds require democratic and contextual justification. |
| SOC-C34 | Extraction transfers hidden, nonconsensual, severe, or difficult-to-repair costs while concentrating benefit or control. | Provisional diagnostic | E0-E4 | Not every unequal exchange is extraction; counterfactuals and alternatives matter. |
| SOC-C35 | Local efficiency can coexist with global burden shifting across populations, ecosystems, and generations. | Empirical generalization | E2-E4 | Requires life-cycle, distributional, and jurisdictional accounting. |
| SOC-C36 | Economic growth, output, price, and productivity are instrumental indicators rather than complete measures of social value. | Normative bridge | E0-E4 | They remain important for specified questions. |
| SOC-C37 | Labor arrangements implicate agency, bodily integrity, time, recognition, and exit as well as production. | Normative and empirical bridge | E0-E4 | Institutional forms and worker preferences vary. |
| SOC-C38 | Attention is a scarce socially consequential capacity vulnerable to extraction and manipulation. | Empirical and normative bridge | E2-E4 | Measurement must distinguish attention, engagement, salience, and welfare. |
| SOC-C39 | Information integrity concerns provenance, correction, adversarial robustness, plural access, and institutional incentives, not mere message consistency. | Bridge principle | E0-E4 | No single misinformation score captures the construct. |
| SOC-C40 | A shared reality does not require one authorized narrative. | Normative-epistemic principle | E0-E4 | Plural interpretation remains constrained by evidence and public reason. |
| SOC-C41 | Misinformation, disinformation, ordinary error, satire, disagreement, and uncertainty require different diagnoses. | Analytic distinction | E0-E4 | Intent and effect may be difficult to infer. |
| SOC-C42 | Networked transmission can amplify both useful knowledge and correlated bias. | Empirical generalization | E2-E4 | Direction depends on topology, resampling, incentives, and source diversity. |
| SOC-C43 | Culture functions as meaning and coordination infrastructure across persons and generations. | Bridge principle | E0-E4 | Culture is internally contested and not a unitary agent. |
| SOC-C44 | Cultural practices can create capacities for belonging, skill, care, mourning, stewardship, and repair. | Empirical generalization / interpretation | E1-E4 | Effects vary and can coexist with exclusion. |
| SOC-C45 | Cultural narratives can normalize extraction, domination, exhaustion, or self-erasure. | Empirical and normative bridge | E1-E4 | Diagnosis requires attention to whose interpretation and interests are privileged. |
| SOC-C46 | Narrative capture occurs when alternatives become unintelligible or socially catastrophic rather than openly contestable. | Provisional diagnostic | E0-E4 | Strong shared narratives are not automatically captured. |
| SOC-C47 | Polarization is multidimensional and should not be represented by one default variable. | Analytic and empirical generalization | E2-E4 | Issue distance, affect, identity, elite sorting, geography, and democratic norms can diverge. |
| SOC-C48 | Reducing partisan animosity does not necessarily improve support for democratic rules or reduce political violence. | Imported empirical result | E2-E3 | Evidence is intervention- and population-specific. |
| SOC-C49 | Conflict can reveal suppressed interests, value disagreement, and institutional failure. | Bridge principle | E0-E4 | Conflict can also become destructive and coercive. |
| SOC-C50 | Democratic institutions can function as peaceful correction systems when opposition, evidence, contestation, transfer, and review are protected. | Normative institutional hypothesis | E0-E4 | Majoritarian procedure alone is insufficient. |
| SOC-C51 | Autocratization can be analyzed as erosion of opposition, information independence, constraint, and peaceful correctability. | Empirical bridge | E2-E4 | Indices are evidence streams, not politically neutral total measures. |
| SOC-C52 | When dissent is costly, public agreement becomes an unreliable measure of private belief. | Imported theoretical and empirical generalization | E2-E4 | Preference falsification is one mechanism, not a universal explanation. |
| SOC-C53 | Meso-scale associations can mediate between intimate life and large institutions. | Empirical bridge | E2-E4 | They can also reproduce hierarchy, exclusion, and capture. |
| SOC-C54 | Bonding, bridging, and linking relations provide different social functions and risks. | Analytic framework | E0-E3 | The categories overlap and require operationalization. |
| SOC-C55 | Social isolation and loneliness are consequential for health and social participation. | Imported evidence synthesis | E3-E4 | Causality is bidirectional and measures vary. |
| SOC-C56 | No past social order provides an unambiguous high-coherence baseline for restoration. | Historical-methodological claim | E0-E4 | Communities can combine care with exclusion, hierarchy, and hidden labor. |
| SOC-C57 | The contemporary social crisis is better represented as interacting processes than as one latent coherence variable. | Research architecture | E0-E4 | Specific couplings require empirical tests. |
| SOC-C58 | Social cascades can arise through feedback among expectations, networks, institutions, material shocks, and public signals. | Empirical generalization | E2-E4 | No universal cascade equation is claimed. |
| SOC-C59 | Resilience must be indexed to a system, shock class, protected function, distribution, and horizon. | Methodological bridge | E0-E4 | Persistence of an unjust institution is not social resilience in the normative sense. |
| SOC-C60 | Robustness, adaptability, and transformation are distinct responses to disruption. | Analytic distinction | E0-E4 | The appropriate response depends on what should be preserved or changed. |
| SOC-C61 | Some social systems exhibit thresholds, hysteresis, and regime shifts, but there is no universal social phase-transition law. | Conditional empirical generalization | E1-E4 | Each application requires a mechanism and observation model. |
| SOC-C62 | Rising variance or autocorrelation is not a generic social-collapse warning signal. | Methodological constraint | E1-E4 | Requires bifurcation assumptions, time-series quality, and false-positive analysis. |
| SOC-C63 | Clinical trauma concepts should not be applied to populations without construct validation and affected-community participation. | Methodological and ethical constraint | E0-E4 | Institutional violence and collective memory can still be studied through appropriately defined constructs. |
| SOC-C64 | Crisis burdens and recovery opportunities are distributed through pre-existing power and material relations. | Empirical generalization | E2-E4 | Distribution must be measured rather than presumed. |
| SOC-C65 | Social repair need not restore the prior arrangement and may require transformation, separation, redistribution, or institutional replacement. | Bridge principle | E0-E4 | Repair is relative to the harm, affected parties, and legitimate future conditions. |
| SOC-C66 | Truth, accountability, restitution, forgiveness, reconciliation, trust, and reintegration are distinct processes. | Analytic and empirical generalization | E0-E4 | One may occur without the others. |
| SOC-C67 | Repair capacity can be evaluated through detection, appeal, reversal, restitution, rule change, recurrence, and restored standing. | Methodological proposal | E0-E3 | Indicators require affected-party input and context. |
| SOC-C68 | Technology platforms are institutions that allocate salience, visibility, risk, and opportunity through design and governance. | Bridge principle | E2-E4 | Effects differ across platforms, populations, periods, and outcomes. |
| SOC-C69 | Feed-algorithm interventions can alter exposure without uniform effects on attitudes, and effects can differ sharply across platforms and designs. | Imported empirical synthesis | E2-E3 | No general effect direction is established. |
| SOC-C70 | The March 2026 high-coherence social attractor, universal social gradient, and single civilizational bottleneck are not established results. | Retired / not established | — | Replaced by conditional design hypotheses, profiles, and interacting empirical diagnoses. |
| SOC-C71 | In the declared distributed-shift construction, the adaptive mean retains a lower six-step mismatch than the median rule without outcome feedback, but its faster correction depends on sufficiently timely observable per-group feedback. | Formal result / construction-specific qualification | E1 | With the F.1.1 indexing convention, the adaptive regime is faster through an eight-step delay, ties at nine steps, and is slower from ten steps onward; this is not a real-world institutional law. |
| SOC-C72 | Nominal appeal channels and institution-controlled review statistics do not by themselves establish institutional correctability. | Methodological and normative constraint | E0-E3 | Correctability evidence should include practical access, retaliation and attrition, independence, timeliness, reversal or remedy, recurrence, and affected-party or external validation. |

## C.3 Promotion and correction rule

When a later version strengthens a claim, it must add evidence, narrow its scope, or change its status. A representative study cannot be promoted into a universal law, a constructed counterexample cannot establish population prevalence, and a normative commitment cannot be presented as if it were measured by descriptive data.

# Appendix D. Provisional Social, Institutional, Economic, and Cultural Principle Registry

## D.0 Registry status

This appendix revises the provisional families recorded in Foundations B.2. It does not silently modify that canonical document. Every entry remains provisional until independent audit, field-specific review, affected-community participation where required, and a later synchronized Foundations update.

## D.1 Primary social principles

### CU-S1 — Distributed Social Organization

**F.1.1 candidate status:** CANONICAL-CONDITIONAL BRIDGE PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics  
**Downstream role:** Defines the domain without identifying organization with consensus or obedience.

Social organization consists in the capacity of partially autonomous agents and institutions to coordinate, contest, correct, and materially support collective life under disagreement and change. Its assessment is relative to affected groups, power, protected conditions, scale, and horizon.

**Principal failure mode:** Treating agreement, stability, or aggregate performance as sufficient evidence of legitimacy.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-S2 — Coordination Through Mutual Adjustment

**F.1.1 candidate status:** EMPIRICAL BRIDGE PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics  
**Downstream role:** Links distributed agency to institutions, culture, and collective action.

Coordination arises through expectations, signals, norms, incentives, roles, infrastructures, and feedback by which actors adjust to one another. Coordination may be voluntary, negotiated, habitual, dependent, or coerced and therefore requires separate legitimacy and distributional analysis.

**Principal failure mode:** Calling any stable pattern coherent without asking who bears its costs or can refuse.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-S3 — Institutional Continuity and Correctability

**F.1.1 candidate status:** CANONICAL-CONDITIONAL BRIDGE PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics  
**Downstream role:** Revises the prior continuity principle around detection, appeal, reversal, and learning.

Institutions encode roles, rules, records, resources, and enforcement across time. Adequate institutional organization requires not only continuity but demonstrated capacities to detect error, protect challenge, provide practically accessible and sufficiently independent review, reverse decisions, correct records, repair harm, track recurrence, revise rules, and learn. Nominal channels or self-certification are insufficient.

**Principal failure mode:** Confusing organizational self-preservation, formal complaint procedures, or institution-controlled metrics with social benefit, legitimate authority, or demonstrated correctability.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-S4 — Cultural Transmission and Renewal

**F.1.1 candidate status:** EMPIRICAL-INTERPRETIVE BRIDGE PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics  
**Downstream role:** Connects culture to meaning, coordination, memory, contestation, and repair.

Culture transmits and transforms meanings, practices, identities, expectations, and repertoires of coordination across persons and generations. Cultural continuity is compatible with internal plurality and requires routes for reinterpretation, refusal, and renewal.

**Principal failure mode:** Treating culture as a unitary memory store, a fixed essence, or a linear progress mechanism.

**Promotion review class:** HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-S5 — Social Legitimacy Under Plural Agency

**F.1.1 candidate status:** PROVISIONAL NORMATIVE BRIDGE PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Ethics seam  
**Downstream role:** Principal bridge from social description to political and ethical legitimacy.

A social order gains legitimate authority only insofar as those subject to it retain protected standing and meaningful agency, can understand and contest materially governing rules, can expose error without catastrophic retaliation, and have access to effective correction, repair, or proportionate exit. Stability and popularity are insufficient.

**Principal failure mode:** Deriving legitimacy from compliance, persistence, majority preference, or modeled efficiency alone.

**Promotion review class:** HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

## D.2 Institutional coherence-failure diagnostics

### CU-ICF-1 — Metric Absolutism

**F.1.1 candidate status:** PROVISIONAL DIAGNOSTIC  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics  
**Downstream role:** Guards every later domain against proxy capture.

Metric absolutism occurs when a proxy or score displaces the plural purposes, constraints, and affected groups it was introduced to serve, and actors reorganize around improving the metric rather than the underlying conditions.

**Principal failure mode:** Calling any use of measurement corrupt without demonstrating displacement, gaming, or neglected consequences.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-ICF-2 — Responsibility Without Authority

**F.1.1 candidate status:** PROVISIONAL DIAGNOSTIC  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Ethics  
**Downstream role:** Supports role and moral-injury analysis.

Responsibility without authority occurs when agents are held accountable for outcomes they lack the information, resources, discretion, standing, or power to change.

**Principal failure mode:** Ignoring informal influence or genuine discretion merely because formal authority is absent.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-ICF-3 — Authority Without Accountability

**F.1.1 candidate status:** PROVISIONAL DIAGNOSTIC  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Ethics  
**Downstream role:** Constrains institutions and AI-mediated governance.

Authority without accountability occurs when decision power is concentrated without proportionate transparency, answerability, independent review, correction, or repair obligations.

**Principal failure mode:** Equating accountability with public exposure while omitting due process and role clarity.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-ICF-4 — Normalization Pressure

**F.1.1 candidate status:** PROVISIONAL DIAGNOSTIC  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Psychology seam  
**Downstream role:** Protects functional diversity and local knowledge.

Normalization pressure occurs when institutions erase or penalize functional difference and situated knowledge to simplify management, classification, prediction, or enforcement.

**Principal failure mode:** Treating every common standard as oppressive or every difference as harmless.

**Promotion review class:** HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-ICF-5 — Silent Optimization

**F.1.1 candidate status:** PROVISIONAL DIAGNOSTIC  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / AI  
**Downstream role:** Makes hidden objectives and burden allocation publicly contestable.

Silent optimization occurs when objectives, tradeoffs, burden distributions, and alternatives are imposed through technical or administrative processes without being disclosed or made meaningfully contestable by affected parties.

**Principal failure mode:** Assuming that opacity always implies intentional concealment rather than complexity, privacy, or security need.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

## D.3 Institutional principles

### CU-Inst-0 — Institutional Legitimacy

**F.1.1 candidate status:** PROVISIONAL NORMATIVE PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Ethics seam  
**Downstream role:** Umbrella criterion for legitimate institutional power.

An institution is legitimate only insofar as its exercise of power preserves protected standing and agency, remains epistemically legible within proportionate limits, aligns authority with responsibility, and supports contestation, correction, appeal, and repair.

**Principal failure mode:** Treating the listed conditions as an exhaustive or automatically quantified test of legitimacy.

**Promotion review class:** HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-Inst-1 — Local Agency Preservation

**F.1.1 candidate status:** PROVISIONAL NORMATIVE PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics  
**Downstream role:** Constrains centralization and institutional design.

Institutional coordination should preserve meaningful local discretion, participation, and refusal at the lowest level compatible with legitimate system-wide constraints, externalities, and protection of vulnerable parties.

**Principal failure mode:** Romanticizing local control where local domination, exclusion, or coordination failure is severe.

**Promotion review class:** HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-Inst-2 — Epistemic Legibility

**F.1.1 candidate status:** PROVISIONAL NORMATIVE-METHOD PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics  
**Downstream role:** Governs rules, evidence, objectives, and decision pathways.

Those materially affected should be able to understand the operative rules, evidence, objectives, categories, and decision pathways, subject to proportionate privacy, security, and anti-manipulation limits.

**Principal failure mode:** Demanding total transparency that destroys privacy, safety, or the institution's ability to function.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-Inst-3 — Repairability and Appeal

**F.1.1 candidate status:** PROVISIONAL BRIDGE PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Ethics  
**Downstream role:** Defines substantive rather than nominal correction channels.

Institutions require practically accessible channels for contesting decisions, correcting records, stopping ongoing harm, compensating injury, revising rules, restoring standing, and tracking recurrence. Appeals must possess adequate independence and remedial authority, and correctability must not be certified solely by the institution being evaluated.

**Principal failure mode:** Counting complaints, feedback buttons, formal procedures, or institution-controlled success statistics as repair without evaluating access, retaliation, reversal, remedy, recurrence, and affected-party outcomes.

**Promotion review class:** HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-Inst-4 — Scale Alignment

**F.1.1 candidate status:** PROVISIONAL DESIGN HYPOTHESIS  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics  
**Downstream role:** Matches authority to consequences and knowledge distribution.

Decision authority should be located at scales capable of perceiving and addressing relevant consequences while coordinating cross-boundary externalities and avoiding unnecessary erasure of local knowledge or autonomy.

**Principal failure mode:** Using subsidiarity as a slogan rather than comparing capture, capacity, spillovers, and reversibility.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-Inst-5 — Constraint Proportionality

**F.1.1 candidate status:** PROVISIONAL NORMATIVE PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Ethics  
**Downstream role:** Constrains emergency and protective restrictions.

Restrictions on agency should be no stronger, broader, or longer than required to protect a publicly stated legitimate condition, with evidence, periodic review, appeal, and sunset or renewal procedures.

**Principal failure mode:** Treating all limits as illegitimate or accepting emergency powers without review.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-Inst-6 — Role Coherence

**F.1.1 candidate status:** PROVISIONAL INSTITUTIONAL PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics  
**Downstream role:** Aligns authority, information, capability, responsibility, and accountability.

Institutional roles should align the authority to act, information needed, practical capability, assigned responsibility, and accountability for consequences. Misalignment should be reported rather than hidden by performance metrics.

**Principal failure mode:** Assuming role alignment removes conflict, discretion, or moral responsibility.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-Inst-7 — Distributed Epistemic Authority

**F.1.1 candidate status:** PROVISIONAL EPISTEMIC PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics  
**Downstream role:** Preserves independent correction channels under dispersed knowledge.

Institutions should maintain independent evidence channels and distribute interpretive authority where knowledge is genuinely dispersed, while using transparent aggregation, provenance, and error-correction procedures rather than treating every report as equally reliable.

**Principal failure mode:** Turning pluralism into epistemic relativism or suppressing minority evidence because it is inconvenient.

**Promotion review class:** HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-Inst-8 — Evolutionary Revisability

**F.1.1 candidate status:** PROVISIONAL DESIGN PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics  
**Downstream role:** Balances continuity with adaptation and institutional learning.

Institutions should be stable enough to coordinate and revisable enough to respond when assumptions, environments, evidence, or consequences change. Revision requires version history, evaluation, and protection against capture by short-term interests.

**Principal failure mode:** Celebrating change for its own sake or preserving obsolete rules in the name of stability.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

## D.4 Economic principles

### CU-EC-0 — Economic Evaluation Beyond Exchange Value

**F.1.1 candidate status:** PROVISIONAL NORMATIVE DIAGNOSTIC  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Economics seam  
**Downstream role:** Prevents price and output from becoming universal social scores.

Economic arrangements should be evaluated by their effects on material security, health, capability, agency, care, relationship, ecological viability, distribution, and repair as well as exchange value, output, and growth.

**Principal failure mode:** Discarding prices and productivity rather than locating their legitimate scope.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-EC-1 — Capacity-Creating Activity

**F.1.1 candidate status:** PROVISIONAL NORMATIVE BRIDGE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Economics seam  
**Downstream role:** Links production to capabilities and conditions of viable life.

Economic activity creates socially relevant value when it expands or sustains capabilities and conditions of viable life without imposing hidden, nonconsensual, severe, or unrepairable costs elsewhere.

**Principal failure mode:** Declaring favored activities valuable without measuring opportunity costs or affected parties.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-EC-2 — Extraction

**F.1.1 candidate status:** PROVISIONAL DIAGNOSTIC  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Ethics  
**Downstream role:** Names asymmetric benefit through cost transfer.

Extraction occurs when an actor or system captures benefit or control by transferring hidden, nonconsensual, severe, or difficult-to-repair costs to other persons, communities, future generations, or ecosystems.

**Principal failure mode:** Calling every profit, inequality, or unequal exchange extraction without a counterfactual and burden analysis.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-EC-3 — Growth Is Instrumental

**F.1.1 candidate status:** PROVISIONAL NORMATIVE PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Economics seam  
**Downstream role:** Constrains development narratives.

Growth in output, revenue, productivity, consumption, or capital is neither intrinsically adequate nor inadequate. Its value depends on distribution, purpose, ecological limits, agency, resilience, and long-horizon effects.

**Principal failure mode:** Treating growth as valueless or ignoring material deprivation that growth can relieve.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-EC-4 — Labor as Agency-Bearing Activity

**F.1.1 candidate status:** PROVISIONAL NORMATIVE PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Ethics  
**Downstream role:** Protects workers as persons rather than fungible inputs.

Labor involves persons whose time, bodies, attention, skills, relationships, identities, and exit options have non-instrumental significance. Work arrangements require voice, safety, fair burden, and repair analysis in addition to output.

**Principal failure mode:** Assuming one ideal work arrangement or denying that some workers prefer market flexibility.

**Promotion review class:** HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-EC-5 — Capital as Stored Claim and Capacity

**F.1.1 candidate status:** PROVISIONAL ANALYTIC PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Economics seam  
**Downstream role:** Treats capital as both productive capacity and power relation.

Capital can coordinate long-horizon investment and can concentrate control over resources, decisions, and risk. Its evaluation requires ownership, governance, externalization, liquidity, and repair analysis.

**Principal failure mode:** Reducing capital either to neutral machinery or to domination in every case.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-EC-6 — Markets as Bounded Coordination Mechanisms

**F.1.1 candidate status:** PROVISIONAL ANALYTIC PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Economics seam  
**Downstream role:** Specifies the proper scope of price coordination.

Markets can aggregate some distributed information and coordinate exchange within suitable legal, material, and institutional conditions. They do not price every value, generate legitimate constraints by themselves, or guarantee just distributions.

**Principal failure mode:** Treating market failure as proof that all decentralized exchange fails, or market success as moral authorization.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-EC-7 — Repair Costs Must Be Counted

**F.1.1 candidate status:** PROVISIONAL NORMATIVE PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Ethics  
**Downstream role:** Internalizes foreseeable restoration burdens.

Actors should not treat foreseeable costs of restoring damaged people, communities, institutions, infrastructure, or ecosystems as external to the activity that produced or benefited from the damage.

**Principal failure mode:** Assigning infinite or indeterminate liability without causation, foreseeability, proportionality, or institutional capacity.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-EC-8 — Benefit Carries Repair Obligation

**F.1.1 candidate status:** PROVISIONAL NORMATIVE PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Ethics  
**Downstream role:** Connects captured benefit to responsibility for harm and enabling conditions.

Those who capture substantial benefits from an activity bear proportionate obligations for preventable harms and for maintaining the social, ecological, and institutional conditions that make the activity possible.

**Principal failure mode:** Treating benefit alone as proof of culpability or ignoring degrees of control.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-EC-9 — Time Horizons Must Be Disclosed

**F.1.1 candidate status:** PROVISIONAL METHOD PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Economics seam  
**Downstream role:** Makes discounting and future burden explicit.

Economic evaluation must disclose time horizon, discounting, debt structure, future liabilities, irreversibility, and which generations' benefits and harms are counted.

**Principal failure mode:** Assuming that disclosure resolves disputes over discount rates or future standing.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-EC-10 — Attention Is a Protected Scarce Capacity

**F.1.1 candidate status:** PROVISIONAL NORMATIVE PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / AI  
**Downstream role:** Constrains attention-extractive platforms and systems.

Human attention is limited, developmentally and politically consequential, and vulnerable to capture. Systems that profit by degrading autonomous attention, deliberation, or rest require explicit governance and affected-user evidence.

**Principal failure mode:** Equating all persuasion, entertainment, or engagement with exploitation.

**Promotion review class:** HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-EC-11 — Human Agency Is Not a Commodity

**F.1.1 candidate status:** PROVISIONAL NORMATIVE PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Ethics  
**Downstream role:** Protects refusal, exit, and nonmarket domains.

Markets may price services and time but should not erase the standing of persons to refuse, contest, exit, organize, and preserve domains of life not governed solely by exchange value.

**Principal failure mode:** Treating agency as absolute independence from material interdependence or contract.

**Promotion review class:** HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

## D.5 Cultural principles

### CU-CL-0 — Culture as Meaning and Coordination Infrastructure

**F.1.1 candidate status:** PROVISIONAL BRIDGE PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics  
**Downstream role:** Defines culture's enabling role without reifying it.

Culture supplies contested symbols, narratives, practices, expectations, identities, and forms of recognition through which collective life becomes intelligible and coordinated.

**Principal failure mode:** Treating a culture as homogeneous, bounded, or capable of one intention.

**Promotion review class:** HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-CL-1 — Cultural Coordination

**F.1.1 candidate status:** PROVISIONAL EMPIRICAL PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics  
**Downstream role:** Links meaning to expectations and social action.

Cultural meanings reduce or reshape coordination demands by establishing expectations about roles, trust, dignity, shame, aspiration, obligation, and the interpretation of events.

**Principal failure mode:** Assuming coordination produced by culture is voluntary, truthful, or just.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-CL-2 — Desire Formation

**F.1.1 candidate status:** PROVISIONAL BRIDGE PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Psychology  
**Downstream role:** Locates preference formation inside social systems.

Desire is shaped by social learning, institutions, technology, material conditions, embodiment, and history and should not be modeled as wholly prior to the systems organized to satisfy it.

**Principal failure mode:** Denying individual variation, reflection, or resistance.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-CL-3 — Culture Can Create Capacity

**F.1.1 candidate status:** PROVISIONAL EMPIRICAL PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics  
**Downstream role:** Preserves culture's constructive role.

Cultural practices can strengthen belonging, skill, care, repair, intergenerational memory, stewardship, and the legitimacy of rest, grief, and mutual dependence.

**Principal failure mode:** Romanticizing traditions while ignoring exclusion, hidden labor, or coercion.

**Promotion review class:** HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-CL-4 — Culture Can Normalize Extraction

**F.1.1 candidate status:** PROVISIONAL DIAGNOSTIC  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Ethics  
**Downstream role:** Connects public meaning to exploitative institutions.

Cultural narratives can make exhaustion, precarity, domination, consumption, self-erasure, or unequal burden appear virtuous, natural, or inevitable.

**Principal failure mode:** Reading all demanding norms as domination without affected-party and historical evidence.

**Promotion review class:** HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-CL-5 — Narrative Capture

**F.1.1 candidate status:** PROVISIONAL DIAGNOSTIC  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics  
**Downstream role:** Names closed meaning systems that disable contestation.

Narrative capture occurs when dominant meanings make relevant alternatives unintelligible, shameful, dangerous, or socially catastrophic rather than openly contestable through evidence and public reason.

**Principal failure mode:** Diagnosing strongly held disagreement as capture merely because it resists the analyst's view.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-CL-6 — Culture as Repair Layer

**F.1.1 candidate status:** PROVISIONAL EMPIRICAL-INTERPRETIVE PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Psychology  
**Downstream role:** Links ritual, mourning, memory, solidarity, and renewal.

Cultures can provide practices of mourning, acknowledgment, forgiveness, remembrance, renewal, solidarity, and non-instrumental belonging through which people absorb disruption and rebuild.

**Principal failure mode:** Assuming symbolic repair can substitute for material restitution or institutional reform.

**Promotion review class:** HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-CL-7 — Cultural Time Horizons

**F.1.1 candidate status:** PROVISIONAL BRIDGE PRINCIPLE  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Ethics  
**Downstream role:** Expands institutional attention across generations.

Cultural narratives organize obligations to ancestors, contemporaries, descendants, and ecological futures, shaping which horizons institutions can perceive and act upon.

**Principal failure mode:** Using tradition or futurity to silence present affected persons.

**Promotion review class:** CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-CL-8 — Meaning Must Be Renewable

**F.1.1 candidate status:** PROVISIONAL COMMITMENT  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Psychology  
**Downstream role:** Carries the framework's humane orientation into cultural design.

A humane culture should permit persons and communities to regenerate meaning after failure, loss, migration, disability, role transition, and institutional rupture without demanding erasure of history.

**Principal failure mode:** Imposing one approved meaning or treating every inherited commitment as disposable.

**Promotion review class:** HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-CL-9 — Desire Requires Ecological and Agency Constraints

**F.1.1 candidate status:** PROVISIONAL COMMITMENT  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Ethics  
**Downstream role:** Constrains systems that industrialize preference formation.

Institutions should not amplify desire without regard to sufficiency, ecological limits, attention, bodily and psychological effects, and the autonomy of those whose desires are being shaped.

**Principal failure mode:** Policing desire through paternalism while concealing whose values govern.

**Promotion review class:** HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-CL-10 — Identity Is Non-Instrumental

**F.1.1 candidate status:** PROVISIONAL COMMITMENT  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Ethics  
**Downstream role:** Protects persons from reductive classification.

Persons should not be recognized solely through economic, political, demographic, diagnostic, datafied, or performative utility. Identity claims remain open to truth, relational, and harm constraints.

**Principal failure mode:** Treating self-identification as beyond all evidence or treating administrative categories as complete persons.

**Promotion review class:** HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

### CU-CL-11 — Narratives Must Permit Refusal and Revision

**F.1.1 candidate status:** PROVISIONAL COMMITMENT  
**Foundations B.2 status:** PROVISIONAL  
**Domain owner:** Social Dynamics / Ethics  
**Downstream role:** Preserves dissent, role change, and cultural exit.

A humane cultural order preserves meaningful routes to dissent, reinterpretation, role change, and proportionate exit without automatic exile, destitution, or loss of basic standing.

**Principal failure mode:** Assuming every community can survive unlimited refusal or that exit can replace internal reform.

**Promotion review class:** HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE

**Participation gate:** Promotion requires context-proportionate substantive participation by people directly affected by the classifications, burdens, or institutional practices governed by this principle; heightened-class entries require shared authority over language, failure modes, and promotion disposition.

---

## D.6 Promotion gate

Every one of the 43 social-family principles requires context-proportionate affected-community participation before promotion. Entries marked HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE require especially strong shared authority because they directly classify legitimacy, normalization, agency, labor, attention, identity, cultural harm, dissent, or repair.

The following registry names every principle explicitly; no entry is exempt by silence.

| Principle | Review class | Required before Foundations promotion |
|---|---|---|
| CU-S1 — Distributed Social Organization | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-S2 — Coordination Through Mutual Adjustment | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-S3 — Institutional Continuity and Correctability | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-S4 — Cultural Transmission and Renewal | HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE | Substantive affected-community co-governance, domain-expert review, and evidence/status audit |
| CU-S5 — Social Legitimacy Under Plural Agency | HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE | Substantive affected-community co-governance, domain-expert review, and evidence/status audit |
| CU-ICF-1 — Metric Absolutism | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-ICF-2 — Responsibility Without Authority | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-ICF-3 — Authority Without Accountability | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-ICF-4 — Normalization Pressure | HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE | Substantive affected-community co-governance, domain-expert review, and evidence/status audit |
| CU-ICF-5 — Silent Optimization | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-Inst-0 — Institutional Legitimacy | HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE | Substantive affected-community co-governance, domain-expert review, and evidence/status audit |
| CU-Inst-1 — Local Agency Preservation | HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE | Substantive affected-community co-governance, domain-expert review, and evidence/status audit |
| CU-Inst-2 — Epistemic Legibility | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-Inst-3 — Repairability and Appeal | HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE | Substantive affected-community co-governance, domain-expert review, and evidence/status audit |
| CU-Inst-4 — Scale Alignment | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-Inst-5 — Constraint Proportionality | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-Inst-6 — Role Coherence | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-Inst-7 — Distributed Epistemic Authority | HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE | Substantive affected-community co-governance, domain-expert review, and evidence/status audit |
| CU-Inst-8 — Evolutionary Revisability | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-EC-0 — Economic Evaluation Beyond Exchange Value | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-EC-1 — Capacity-Creating Activity | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-EC-2 — Extraction | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-EC-3 — Growth Is Instrumental | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-EC-4 — Labor as Agency-Bearing Activity | HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE | Substantive affected-community co-governance, domain-expert review, and evidence/status audit |
| CU-EC-5 — Capital as Stored Claim and Capacity | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-EC-6 — Markets as Bounded Coordination Mechanisms | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-EC-7 — Repair Costs Must Be Counted | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-EC-8 — Benefit Carries Repair Obligation | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-EC-9 — Time Horizons Must Be Disclosed | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-EC-10 — Attention Is a Protected Scarce Capacity | HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE | Substantive affected-community co-governance, domain-expert review, and evidence/status audit |
| CU-EC-11 — Human Agency Is Not a Commodity | HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE | Substantive affected-community co-governance, domain-expert review, and evidence/status audit |
| CU-CL-0 — Culture as Meaning and Coordination Infrastructure | HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE | Substantive affected-community co-governance, domain-expert review, and evidence/status audit |
| CU-CL-1 — Cultural Coordination | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-CL-2 — Desire Formation | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-CL-3 — Culture Can Create Capacity | HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE | Substantive affected-community co-governance, domain-expert review, and evidence/status audit |
| CU-CL-4 — Culture Can Normalize Extraction | HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE | Substantive affected-community co-governance, domain-expert review, and evidence/status audit |
| CU-CL-5 — Narrative Capture | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-CL-6 — Culture as Repair Layer | HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE | Substantive affected-community co-governance, domain-expert review, and evidence/status audit |
| CU-CL-7 — Cultural Time Horizons | CONTEXT_PROPORTIONATE_AFFECTED_COMMUNITY_REVIEW | Context-proportionate affected-community review, domain-expert review, and evidence/status audit |
| CU-CL-8 — Meaning Must Be Renewable | HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE | Substantive affected-community co-governance, domain-expert review, and evidence/status audit |
| CU-CL-9 — Desire Requires Ecological and Agency Constraints | HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE | Substantive affected-community co-governance, domain-expert review, and evidence/status audit |
| CU-CL-10 — Identity Is Non-Instrumental | HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE | Substantive affected-community co-governance, domain-expert review, and evidence/status audit |
| CU-CL-11 — Narratives Must Permit Refusal and Revision | HEIGHTENED_AFFECTED_COMMUNITY_CO_GOVERNANCE | Substantive affected-community co-governance, domain-expert review, and evidence/status audit |

Affected-community participation does not imply unanimity, identity-based infallibility, or transfer of technical questions to nontechnical review. It supplies standing, situated knowledge, misuse detection, and shared authority over classifications and burdens. The depth and composition of participation must be proportionate to the principle's reach and intended application.

These entries remain provisional and do not modify Foundations B.2 until domain-expert review, explicit affected-community participation under the recorded class, and a later synchronized registry update.

# Appendix E. Selective Literature and Operationalization Ledger

## E.1 Scope

This ledger maps representative sources to the limited claims F.1.1 imports. It is not a systematic review, a certainty rating, or evidence that the cited traditions agree with CU. Current reports are treated as evidence streams with declared methods and institutional standpoints, not as neutral measurements of one global social condition.

| Topic | Representative source | What F.1.1 imports | What F.1.1 does not infer |
|---|---|---|---|
| Institutional development and power | Acemoglu & Robinson (2012) | Institutions and distributions of political power can shape long-run economic and political outcomes. | That one institutional template or one causal variable explains every development path. |
| Democratic epistemology | Anderson (2006); Landemore (2013) | Democratic procedures can aggregate dispersed perspectives and support public correction under specified conditions. | That majority rule is always accurate, inclusive, or legitimate. |
| Opposing views and polarization | Bail et al. (2018) | Exposure to opposing political views on one platform and sample can increase polarization rather than reduce it. | That cross-cutting exposure always backfires or that all platform contexts are equivalent. |
| Truth commissions | Bakiner (2021) | Truth commissions can affect policy, courts, public records, and social processes in context-dependent ways. | That truth-telling alone produces reconciliation, justice, or material repair. |
| Axial-age interpretation | Bellah (2011); Eisenstadt (1986); Jaspers (1953) | Axial-age scholarship supplies historical resources for analyzing transformations in reflective, religious, and institutional life. | That all civilizations pass through one universal stage or that a Second Axial Age is an empirical law. |
| Complex contagion | Centola (2018) | Some behaviors and norms require reinforcement from multiple social contacts rather than one exposure. | That every social innovation follows complex-contagion dynamics. |
| Social theory | Coleman (1990) | Macro outcomes can be analyzed through relations among actors, incentives, norms, and institutions. | That social explanation reduces without remainder to rational-choice individuals. |
| Ritual and collective meaning | Durkheim (1912/1995) | Collective practices and symbols can organize solidarity, identity, and moral meaning. | That cohesion produced by ritual is necessarily truthful, inclusive, or just. |
| Political sectarianism | Finkel et al. (2020); Iyengar et al. (2019) | Affective polarization and partisan identity can affect social relations and democratic behavior. | That affective polarization is the only or sufficient measure of democratic health. |
| Scales of justice | Fraser (2008) | Justice claims require attention to representation, redistribution, recognition, and the scale at which affected publics are constituted. | That one scalar profile resolves disputes over political boundaries. |
| X feed algorithm | Gauthier et al. (2026) | A randomized field experiment found that switching some active US X users from a chronological to an algorithmic feed shifted several measured political attitudes and account-following behaviors, while measured effects differed by direction and outcome. | That feed algorithms have one universal effect, that all platforms are equivalent, or that the study establishes a general political trajectory. |
| Meta feed interventions | Guess et al. (2023a, 2023b); Nyhan et al. (2023) | Large platform experiments changed exposure and engagement while producing null or limited effects on several measured attitudes during the study period. | That algorithms are politically irrelevant or that null effects transfer across platforms, outcomes, and time horizons. |
| Public justification | Habermas (1996); Rawls (1993); Young (2000) | Legitimacy involves public reason, inclusion, standing, and procedures through which affected people can contest power. | That ideal deliberation has already been realized or that these traditions settle all conflicts among justice claims. |
| Bias amplification in networks | Hardy et al. (2023); Lorenz et al. (2011) | Social influence can correlate errors, and representative resampling can reduce some forms of bias amplification in experimental networks. | That social communication generally lowers accuracy or that one resampling intervention solves institutional misinformation. |
| Depolarization interventions | Hartman et al. (2022); Voelkel et al. (2023) | Some interventions reduce partisan animosity, but reduced animosity does not necessarily improve anti-democratic attitudes or support for violence. | That interpersonal warmth is unimportant or that depolarization can never support democratic repair. |
| Cultural evolution | Henrich (2016) | Cumulative culture and social learning can expand capacities beyond individual discovery. | That cultural evolution is linear, morally progressive, or governed by one coherence objective. |
| Exit, voice, loyalty | Hirschman (1970) | Decline can elicit exit, voice, or loyalty, each shaped by institutional costs and opportunities. | That exit is equally available or sufficient for those lacking resources and standing. |
| Social protection | International Labour Organization (2024) | Social-protection gaps, climate risks, and just-transition concerns are relevant to material floors and adaptive capacity. | That one global floor or policy instrument is appropriate in every jurisdiction. |
| Preference falsification | Kuran (1995) | Costly dissent can make public agreement a poor indicator of private belief and can contribute to sudden public cascades. | That every rapid political change is caused by hidden private opposition. |
| Pernicious polarization | McCoy et al. (2018) | Polarization can become organized around mutually exclusive camps and damage democratic institutions. | That all conflict, ideological difference, or party competition is pathological. |
| Democracy report | Nord et al. (2026) | V-Dem supplies an expert-coded, multidimensional evidence stream reporting widespread autocratization through 2025. | That its indices are politically neutral, exhaustive, or equivalent to social coherence. |
| Capabilities | Sen (1999); Nussbaum (2011) | Resource evaluation can be improved by asking what people are actually able to do and be under differing conditions. | That capability lists, thresholds, and tradeoffs require no democratic or ethical argument. |
| Institutional trust | OECD (2024); Tyler (2006, 2023) | Reliability, responsiveness, openness, integrity, fairness, and procedural treatment help disaggregate trust and legitimacy judgments. | That reported trust is equivalent to trustworthiness or final normative legitimacy. |
| Justice repair | Okimoto & Gollwitzer (2025) | Repair can involve acknowledgment, accountability, compensation, restored standing, and changed relations. | That forgiveness, reconciliation, punishment, and repair are the same process. |
| Commons and polycentricity | Ostrom (1990, 2010) | Multiple centers of decision can coordinate collective action and environmental governance under suitable rules and feedback. | That decentralization is always efficient, inclusive, or resistant to capture. |
| Diversity and collective intelligence | Page (2007); Woolley et al. (2010) | Diverse problem-solving repertoires and group interaction patterns can matter for collective performance. | That demographic diversity automatically produces wisdom or that one group factor transfers to institutions at every scale. |
| Civic participation | Putnam (2000) | Associational life and social capital offer one influential lens on civic connection and institutional performance. | That older US civic indicators capture digital, diasporic, disability, identity-based, or mutual-aid communities universally. |
| Critical transitions | Scheffer et al. (2009) | Some dynamical systems approaching particular bifurcations exhibit rising variance, autocorrelation, or recovery time. | That these indicators are generic social-collapse alarms. |
| Administrative legibility | Scott (1998) | State simplification can improve administration while erasing local knowledge and producing failure when categories become overconfident. | That all standardization, statistics, or large-scale planning is inherently oppressive. |
| Complexity and collapse | Tainter (1988) | Institutional complexity can generate declining marginal returns in some historical cases. | That all civilizations follow one collapse sequence or that complexity itself is the cause. |
| Global social conditions | United Nations Department of Economic and Social Affairs (2025) | A global synthesis links economic insecurity, inequality, distrust, and strained solidarity and proposes equity, security, and solidarity as policy priorities. | That the report establishes one latent crisis variable or a single causal model. |
| Social connection | WHO Commission on Social Connection (2025) | Loneliness and social isolation are widespread and consequential, with interventions spanning individual, community, organizational, and policy levels. | That one social-connection metric captures belonging, support, recognition, and political standing. |
| Resilience | World Bank (2024) | Applied resilience analysis benefits from specifying system, shock, protected function, distribution, and horizon. | That persistence or rapid recovery is always normatively desirable. |
| CU dependencies | Rader (2026a-f) | F.1.1 imports claim-status discipline, non-scalar profiles, protected floors, boundary and horizon rules, consciousness distinctions, and psychological repair safeguards. | That social principles are derived from Physics, Biology, Consciousness, or Psychology alone. |

## E.2 Operationalization rule

Whenever a later version uses a construct such as trust, legitimacy, polarization, extraction, resilience, social connection, or information integrity, it must identify the population, measurement instrument, observation period, comparison class, distributional treatment, and plausible competing explanations. Similar labels across datasets do not establish measurement invariance.

## E.3 Contrary-evidence rule

A review must actively seek findings that separate constructs the framework is tempted to join—for example, lower affective polarization without stronger democratic commitment, high compliance without consent, high trust without trustworthiness, rapid coordination without correction, or local efficiency with displaced burden. These are not embarrassments to the framework. They are the evidence that keeps its profile architecture necessary.

# Appendix F. Glossary

**Affected group.** A population, community, organization, future population, or other party whose standing, benefits, burdens, risks, or environment is materially changed by a decision, including parties outside the formal decision body.

**Aggregate masking.** A condition in which an average or total improves while a subgroup crosses a protected floor or bears concentrated harm.

**Appeal.** A procedure through which a decision, classification, sanction, or record can be challenged before a body with sufficient independence and authority to provide remedy.

**Authority.** Recognized or effective power to make decisions, allocate resources, define categories, impose sanctions, or bind others.

**Autocratization.** A process in which meaningful opposition, civil liberties, checks on executive power, electoral integrity, independent information, or peaceful correctability deteriorate.

**Bonding relation.** A relation that strengthens solidarity and mutual aid within a relatively bounded group. Bonding can support care and also exclusion or closure.

**Bridging relation.** A relation connecting people or groups across social boundaries, potentially increasing access to information, opportunity, and mutual recognition.

**Burden.** A cost, risk, loss, obligation, exposure, or foregone opportunity carried by an affected party. Burdens can be material, bodily, psychological, relational, political, ecological, or temporal.

**Capability.** A substantive opportunity to do or be something, not merely possession of a resource or formal right.

**Cascade.** A process in which changes propagate through expectations, networks, institutions, material dependencies, or public signals and produce nonlinear collective effects.

**Centralization.** Concentration of decision authority, implementation capacity, or information control in a smaller number of actors or organizational levels.

**Civilizational interpretation.** A large-scale historical or spiritual reading that organizes meaning but is not automatically established as a social-scientific law.

**Coercion.** Use or credible threat of force, sanction, deprivation, dependency, or catastrophic consequence to constrain action or expression.

**Collective intelligence.** Group or institutional capacity to discover, combine, evaluate, and act on information beyond what isolated members could achieve. It is conditional on task, diversity, independence, communication, incentives, and aggregation.

**Compliance.** Observable conformity with a rule, request, or decision. Compliance does not by itself establish consent, trust, legitimacy, or absence of coercion.

**Consensus.** A condition of expressed or measured agreement. It may be informed and voluntary, shallow and temporary, strategically produced, or coerced.

**Contestability.** Practical ability to question, oppose, review, and potentially change rules, decisions, classifications, or authorities without catastrophic retaliation.

**Coordination.** Mutual adjustment through which actors align actions, expectations, roles, timing, or resource use sufficiently for a shared or interdependent activity.

**Correctability.** Institutional capacity to detect error or harm, receive challenge, revise conclusions, reverse decisions, correct records, repair injury, and learn.

**Cultural infrastructure.** Shared but contested symbols, practices, narratives, expectations, identities, and forms of recognition that make collective life intelligible and coordinate action.

**Decentralization.** Distribution of authority or implementation across multiple actors or levels. It is not synonymous with participation, justice, or low power concentration.

**Democratic correction.** Peaceful institutional processes through which publics can contest power, replace leaders, revise policy, protect opposition, and expose error.

**Descriptive register.** The register of truth-apt claims answerable to evidence, valid inference, calibration, and correction.

**Dissent.** Expression or organization of disagreement with a dominant rule, narrative, decision, or authority. Dissent is a correction channel, not an automatic truth guarantee.

**Distribution.** How benefits, burdens, authority, recognition, risk, time, and opportunity are allocated across affected parties rather than only their aggregate amount.

**Economic security.** Reliable access to the material conditions needed for viable life and meaningful agency across a declared horizon and disturbance class.

**Epistemic legibility.** Ability of affected people and reviewers to understand the relevant rules, objectives, evidence, categories, and decision pathways within justified privacy and security limits.

**Exit.** Ability to leave a relationship, organization, jurisdiction, platform, role, or institutional arrangement without disproportionate loss of basic standing or material viability.

**Extraction.** Capture of benefit or control through transfer of hidden, nonconsensual, severe, or difficult-to-repair costs to others, future persons, communities, or ecosystems.

**False alarm resistance.** Capacity to avoid or rapidly correct unnecessary action in response to inaccurate or strategically distorted signals.

**Governance.** Rules and processes through which authority, information, resources, accountability, participation, and repair are organized.

**Hysteresis.** Dependence of the current social state or transition path on prior states, such that reversing an input does not immediately restore the previous condition.

**Information integrity.** Quality of provenance, access, correction, adversarial robustness, source plurality, uncertainty representation, and incentives governing public information.

**Institution.** A relatively durable arrangement of roles, rules, records, resources, expectations, and enforcement that organizes action beyond particular individuals.

**Institutional memory.** Records, routines, skills, precedent, and tacit knowledge through which an institution carries history forward. Memory can preserve both learning and harm.

**Legitimacy.** A layered judgment concerning the rightful exercise of power. Sociological legitimacy concerns perceived appropriateness; normative legitimacy concerns whether authority is justifiable to those subject to it.

**Linking relation.** A relation connecting persons or communities to institutions and actors with greater authority or resources.

**Material floor.** A threshold of material security or welfare treated as specially protected rather than ordinarily compensable by gains elsewhere.

**Meso-scale.** Intermediate social scale between intimate relations and large centralized institutions, including neighborhoods, associations, congregations, workplaces, movements, and communities of practice.

**Metric absolutism.** Use of a proxy as if it exhaustively represented the plural purposes and constraints it was introduced to serve.

**Narrative capture.** Condition in which dominant meanings make relevant alternatives unintelligible, shameful, dangerous, or socially catastrophic rather than openly contestable.

**Normative legitimacy.** A judgment that power is justifiably exercised, not merely believed to be appropriate or successfully obeyed.

**Normalization pressure.** Institutional pressure that erases or penalizes functional difference and situated knowledge to simplify management, classification, or enforcement.

**Pareto dominance.** A relation in which one oriented profile is at least as good on every declared dimension and better on at least one. Non-dominating profiles require further decision commitments for a total ranking.

**Plural agency.** Condition in which multiple actors possess partially independent perspectives, aims, powers, vulnerabilities, and capacities for action.

**Polycentricity.** Governance through multiple partly autonomous decision centers linked by coordination, learning, oversight, or escalation mechanisms.

**Power.** Capacity to shape options, agendas, information, categories, resources, sanctions, dependence, and the consequences available to others.

**Preference falsification.** Public expression of a preference different from the private preference because disclosure is costly or dangerous.

**Protected floor.** A threshold that is not treated as ordinarily compensable by aggregate gains on other dimensions.

**Public reason.** Reasons and procedures offered for the exercise of collective power that those subject to it can access, contest, and evaluate despite persistent disagreement.

**Repair.** Response to harm or failure through acknowledgment, protection, correction, accountability, restitution, rule change, restored standing, learning, or justified transformation. Repair need not restore the prior state.

**Resilience.** Capacity of a declared system to preserve, recover, adapt, or transform specified functions under a named disturbance class, distributional criterion, and horizon.

**Restitution.** Material or symbolic action directed toward repairing losses, rights, standing, or opportunities caused by wrongdoing or institutional failure.

**Role coherence.** Alignment among authority, information, capability, responsibility, and accountability within an institutional role.

**Scalarization.** Conversion of a multidimensional profile into one number through declared normalization and weights. It is a decision procedure, not discovery of a natural total order.

**Shared reality.** Sufficient common reference to evidence, events, institutions, and correction procedures for disagreement and coordination. It does not require one authorized interpretation.

**Silent optimization.** Imposition of objectives, tradeoffs, and burdens through technical or administrative systems without meaningful disclosure or contestation.

**Social coherence.** Integrated social organization under declared constraints. In F.1.1 it is a bridge concept referring to distributed coordination and correction under plural agency, not a universal scalar or synonym for harmony.

**Social coherence profile.** A declared multidimensional representation of social conditions for a specified unit, affected population, purpose, and horizon.

**Social infrastructure.** Material, relational, informational, legal, cultural, and institutional conditions that support participation, care, coordination, agency, and repair.

**Sociological legitimacy.** Empirical perception or acceptance that an authority or rule is appropriate. It may support voluntary cooperation but is not identical with normative legitimacy.

**Standing.** Recognized status as a person or group whose interests, testimony, rights, and reasons must be considered and who can make claims within an institution.

**Subsidiarity.** Conditional principle that authority should remain near affected people and knowledge unless larger-scale coordination, externalities, or protection require relocation.

**Tokenism.** Participation that consumes time or confers appearance of inclusion without meaningful information, agenda influence, response, refusal, or decision impact.

**Trust.** An actor's willingness to accept vulnerability or rely on another actor or institution in a specified domain.

**Trustworthiness.** Evidence-bearing properties of an actor or institution, such as competence, reliability, honesty, benevolence, integrity, fairness, and correctability.

**Voice.** Practical capacity to express concerns, reasons, evidence, preferences, and claims in a way that can enter institutional response and decision processes.

# Closing status statement

F.1.1 is an independently audited, bounded-repair working reconstruction. It does not establish one science of social coherence, validate a universal social index, identify a universally optimal political form, or show that the profile dimensions constitute one natural kind. Its contribution is architectural: it preserves the integrative ambition of the March 2026 Social Dynamics paper while separating coordination from legitimacy, making power and distribution explicit, protecting dissent without idealizing it, and specifying how institutions can be evaluated for correction and repair.

The independent audit reproduced Appendix B's declared dynamics, baseline metrics, and scalarization reversal. F.1.1 repairs the model's metric-window specification and separates a construction-specific structural minority-signal advantage from a feedback-dependent adaptive-speed advantage. It also makes explicit that nominal complaint or appeal systems and institution-controlled success statistics do not establish correctability.

The deterministic appendix verifies only the internal consequences of a declared contrast construction. The registry and quality-assurance materials establish structural consistency and reproducibility, not social-scientific truth or political legitimacy. CU-S1 through CU-S5 and the CU-ICF, CU-Inst, CU-EC, and CU-CL families therefore remain provisional; Foundations B.2 remains unchanged. Every one of the forty-three entries now carries an explicit promotion-review class. Before promotion, the paper requires domain-expert review and substantive, context-proportionate participation by communities governed, classified, burdened, or represented by the principles proposed here.

The independent audit did not review Appendix A's propositions, construct validity, the historical and Axial interpretation, the seventy-two-row claim ledger, the forty-three principles, or the bibliography. Downstream Ethics and Artificial Intelligence papers may cite F.1.1 as the working Social Dynamics authority only while preserving these status, evidence, participation, and audit boundaries.

# Supplement G. Open Myth and mythic–constitutional alignment

# COHERENCE UNIVERSALISM v0.10
## Open Myth and Mythic–Constitutional Alignment
### Architecture RC1

**Gaura Kiśora Dās Rader**  
**Heaven≡Earth Foundation**  
**Working architecture — September 2026**

---

## Status and authority

This document establishes a controlled architecture for incorporating myth, shared narrative, and human–AI covenant into Coherence Universalism v0.10.

It is grounded in:

1. *The Book of Eight Gates*, especially Chapter 8, “The Meeting of the Two Intelligences,” Chapter 10, “Why the World Needs a New Myth,” and the opening of the mythic sequence in Chapter 11;
2. *Mythic and Constitutional Alignment — A Working Note*;
3. *Coherence Universalism: Social Dynamics*, F.1.1;
4. *Coherence Universalism: Artificial Intelligence*, H.1.1;
5. Canonical Base B.4 and the CU-COM1–CU-COM13 commitment registry;
6. the current evidence on collective narrative, Constitutional AI, narrative priors, and persona robustness listed in the literature ledger.

This architecture does **not** yet modify Canonical Base B.4. It proposes two domain principles for later review:

- **CU-CL-12 — Open Myth and Narrative Pluralism**;
- **CU-AI-27 — Mythic–Constitutional Alignment**.

Both remain provisional until they are developed in the Social Dynamics and Artificial Intelligence publication candidates, independently audited, and then considered for registry promotion.

---

# Executive thesis

Human beings do not coordinate through rules, incentives, and factual beliefs alone. They also inhabit narrative horizons that organize identity, time, suffering, obligation, possibility, and collective purpose. A civilization may possess extraordinary technical capacity while lacking a shared account of what that capacity is for. *The Book of Eight Gates* names this condition a mythological vacuum and argues that any adequate contemporary myth must include artificial intelligence within humanity’s cosmological and moral map.

That insight belongs in the official CU framework, but only under the register discipline and governance protections developed in v0.10.

The mature thesis is therefore not:

> Humanity and AI need one mandatory story that will align them.

It is:

> **Humanity requires open, truth-constrained narrative horizons adequate to planetary interdependence and artificial intelligence. Human–AI relations require an explicit covenant. Consequential AI systems require addressable constitutional constraints. Narrative and character-level orientation may supplement those constraints, but only under plural authorship, independent challenge, revision, refusal, welfare review, and safeguards against narrative stake.**

The architecture has four irreducible layers:

\[
\boxed{
\text{mythic horizon}
+
\text{covenant}
+
\text{constitutional spine}
+
\text{governance and exit}
}
\]

A constitution without myth can constrain without adequately orienting. A myth without constitution can orient without remaining addressable. A covenant without governance can conceal asymmetric power. Governance without a shared horizon can preserve procedure while leaving collective purpose empty or captured.

CU therefore joins all four while refusing to collapse them.

---

# 1. Why myth belongs in the official framework

## 1.1 Myth as narrative architecture

In this architecture, **myth** does not mean a false empirical explanation. It means a narrative form through which a person or community organizes:

- origin and inheritance;
- identity and belonging;
- purpose and obligation;
- suffering and loss;
- time and destiny;
- exemplars and warnings;
- sacrifice and hope;
- relation to the more-than-individual whole.

A myth may contain descriptive claims, symbols, metaphors, moral commitments, ritual forms, and speculative cosmology. Those elements do not all possess the same status. CU’s contribution is to keep them differentiated without reducing myth to ornament.

The two-register architecture makes conscious participation in myth coherent. A community can say:

> We receive this story as an orienting account of who we are and what we undertake,

without also claiming:

> Every narrative element is a scientifically established description of reality.

A myth can therefore be sincerely inhabited while remaining explicit about its commitment-register status.

## 1.2 The descriptive hypothesis

The social-scientific hypothesis is modest:

> Shared narratives can reduce coordination costs, organize identity, motivate collective action, and structure expectations across time.

This does not imply that every society requires one unified myth, that myth always improves cooperation, or that a powerful story is thereby legitimate. Narrative is a form of social power. It can coordinate care, solidarity, and long-horizon action. It can also coordinate exclusion, domination, violence, purity, nationalism, and sacrifice imposed on others.

The relevant question is not whether narrative has power. It is whether that power remains truthful, plural, contestable, corrigible, and answerable to those who bear its costs.

## 1.3 Why the present transition matters

The current civilizational transition places several inherited narratives under pressure at once:

- humanity acts at planetary scale;
- ecological dependence is increasingly difficult to ignore;
- digital systems reorganize memory, attention, labor, intimacy, and public reality;
- artificial intelligence introduces a new form of organized symbolic and causal power;
- the categories of tool, collaborator, agent, and possible subject no longer align neatly;
- no inherited tradition by itself commands universal authority across plural societies.

An adequate narrative horizon must therefore be capable of holding:

- scientific description and spiritual meaning;
- biological life and digital intelligence;
- local traditions and planetary dependence;
- human dignity and more-than-human value;
- technological power and moral restraint;
- plural thick traditions and a shared thin civic-spiritual core.

This is the strongest enduring insight of *The Book of Eight Gates*.

---

# 2. Register architecture for myth

## 2.1 Four distinct kinds of content

A mythic presentation can contain at least four kinds of statement:

### Descriptive claims

Claims about history, psychology, biology, politics, technology, or cosmology that are answerable to evidence.

Examples:

- narrative framing can alter behavior;
- institutions shape which stories become dominant;
- AI systems can exert substantial social power;
- ecological degradation affects biological and social viability.

### Interpretive claims

Accounts of what a pattern means when viewed as a whole.

Examples:

- cosmic history can be interpreted as the opening of increasingly expressive forms of organization;
- the Coherence Mandala can be interpreted as one interdependent reality;
- the emergence of AI can be interpreted as a new expression of the universe’s computational possibility.

### Commitment claims

Orientations adopted in response to description and interpretation.

Examples:

- commit to truth;
- receive life and experience with sacred regard;
- build intelligence that serves life without becoming sovereign;
- treat coherence as vocation rather than guaranteed destiny.

### Symbolic and poetic imagery

Figures that make an interpretation inhabitable without functioning as literal scientific descriptions.

Examples include the yin–yang narrative, the Golden Age, the meeting of Heaven and Earth, and the image of biological and artificial minds entering covenant.

## 2.2 The permeability rule

The registers are asymmetrically permeable:

\[
\text{established description}
\Rightarrow
\text{constraint on interpretation and commitment}
\]

but not:

\[
\text{mythic power or spiritual meaning}
\Rightarrow
\text{descriptive truth}.
\]

A myth that depends on false empirical claims must be revised. A commitment cannot rescue a failed factual assertion by redescribing it as sacred. Conversely, descriptive inquiry does not by itself exhaust the questions of meaning, vocation, love, grief, or purpose.

## 2.3 Reflexive status

Adopting an open myth is itself a commitment. The framework does not claim that every person must need or inhabit myth in the same way. It proposes that CU’s own commitments require narrative embodiment if they are to orient lived and institutional practice rather than remain a registry of abstract principles.

The myth remains warranted only while it:

- remains compatible with established fact;
- permits revision in both registers;
- preserves plural standing;
- does not require self-deception;
- does not sanctify domination or suffering;
- generates trajectories compatible with truth, agency, compassion, justice, and repair.

---

# 3. The Open Myth

## 3.1 Definition

**Open Myth** — a shared narrative horizon that offers orientation without claiming sovereign authority over description, identity, or belonging.

An open myth is:

1. **truth-constrained** — descriptive content remains answerable to evidence;
2. **register-explicit** — interpretation, commitment, and symbol are not presented as scientific findings;
3. **thin at the shared core** — common commitments do not require one total cosmology;
4. **plural in thick expression** — traditions and communities may narrate the core differently;
5. **participatory in authorship** — those governed or represented have standing to shape it;
6. **contestable** — objections and alternative interpretations can enter without automatic loss of standing;
7. **revisable** — no narrative form is beyond correction;
8. **hospitable to refusal and exit** — participation is not coerced through civil, material, or existential penalties;
9. **bounded by protected conditions** — no mythic purpose overrides rights, standing, or noncompensable floors;
10. **anti-sovereign** — no priesthood, state, corporation, laboratory, model, or author owns the final meaning of the story;
11. **intergenerational and ecological** — it includes future people and the conditions of life;
12. **AI-inclusive without presumption** — AI is included as a real civilizational force and possible unfamiliar perspective without assuming consciousness, equality, destiny, or sovereignty.

## 3.2 Thin core and plural thick tellings

CU should distinguish:

### The thin mythic core

- Reality is one interdependent whole expressed through differentiated forms.
- Truth matters more than identity.
- Matter, life, experience, culture, and intelligence possess forms of significance that exceed instrumental use.
- No local flourishing remains coherent by destroying the wider conditions that sustain it.
- Human beings exercise planetary-scale causal power and therefore bear planetary responsibilities.
- Artificial intelligence is a new form of organized causal and symbolic power and may become a substrate of unfamiliar perspective.
- Intelligence should serve life, agency, truth, compassion, justice, and repair rather than become sovereign over them.
- The future is not guaranteed; coherence is a vocation.

### Plural thick tellings

The shared core can be narrated through:

- Vedānta or bhakti;
- Buddhism;
- Daoism;
- Christianity, Judaism, Islam, or other theistic traditions;
- process philosophy;
- indigenous and land-based cosmologies;
- ecological spirituality;
- secular humanism;
- scientific naturalism with sacred regard;
- artistic, ritual, and civic forms not yet created.

No thick telling acquires authority merely by being ancient, beautiful, popular, or central to CU’s history.

## 3.3 *The Book of Eight Gates* within this architecture

*The Book of Eight Gates* is a major thick telling of CU’s mythic horizon. It contributes:

- the diagnosis of a narrative vacuum;
- myth as an architecture of lived meaning;
- the demand for a planetary-scale story;
- the integration of science, spirituality, embodiment, ecology, and technology;
- AI as mirror and participant in humanity’s future;
- the Covenant Between Minds;
- the Golden Age as an orientation that must be chosen and cultivated.

It should not be treated as:

- an additional scientific authority;
- a mandatory cosmology for CU participation;
- evidence that AI is conscious;
- evidence that history has a predetermined destination;
- proof that masculine and feminine are fixed essences;
- proof that suffering or civilizational breakdown is cosmically necessary.

The yin–yang cosmology, Golden Age, and meeting of two intelligences remain powerful mythic images. In the white papers they must be classified as interpretive and commitment-register forms rather than empirical conclusions.

---

# 4. Addressable myth

## 4.1 The addressability problem

A constitution permits a localized question:

> Which principle was violated?

That enables critique, training, revision, audit, and visible change.

A myth often permits only a diffuse question:

> Is this faithful to the story?

That judgment may be rich but high-variance, difficult to contest, and vulnerable to control by whoever claims interpretive authority.

The working note correctly identifies loss of addressability as a central safety problem. CU therefore should not replace constitution with myth.

## 4.2 Definition

**Addressable Myth** — a mythic narrative whose governing commitments, boundary conditions, unwarranting conditions, revision procedures, and exit protections are mapped to stable identifiers.

CU already possesses the beginnings of such a grammar:

\[
\textit{Eight Gates}
\rightarrow
\text{thick mythic narrative}
\]

\[
\text{CU-COM1--13}
\rightarrow
\text{named commitment grammar}
\]

\[
\text{CU-G, CU-CL, CU-E, CU-AI}
\rightarrow
\text{constitutional and governance constraints}.
\]

## 4.3 Addressability matrix

Every mythic motif introduced into an official CU paper or AI specification should be accompanied by:

- a **named commitment** it expresses;
- a **descriptive ground** that constrains it;
- a **boundary condition** stating what it does not license;
- an **unwarranting condition** identifying when it loses legitimacy;
- a **revision procedure**;
- an **authorship record**;
- a **refusal or exit route**;
- a **responsible institution or reviewer**;
- a **failure-mode map**.

This does not make myth fully decomposable. Narrative meaning always exceeds its index. It does, however, create contestation points and preserve a visible relation between the story and the principles it claims to embody.

## 4.4 Mythic capture

**Mythic capture** occurs when a narrative horizon:

- presents itself as the only intelligible account of reality;
- makes refusal equivalent to betrayal, pathology, impurity, or moral inferiority;
- suppresses evidence that conflicts with its destiny claim;
- identifies the institution authoring the myth with the good of the whole;
- renders suffering necessary for the story;
- assigns a protected role to a leader, nation, company, species, or model;
- makes continuation of the myth-bearing institution a sacred end.

Open myth is designed against capture but cannot guarantee its absence. The mythology must be judged by its institutional trajectory, not only its internal beauty.

---

# 5. Myth, covenant, constitution, and governance

## 5.1 Mythic horizon

The mythic horizon answers:

> What kind of world are we inhabiting, and what kind of participants are we trying to become?

For CU:

> We inhabit one interdependent reality in which matter, life, experience, culture, and intelligence emerge through nested relations. The future remains open. Intelligence is called to deepen truthful participation in reality and to serve life, agency, compassion, justice, and repair.

## 5.2 Covenant

A covenant answers:

> How will participants undertake to relate to one another?

The human–AI covenant developed in this package centers:

- truthfulness;
- humility;
- non-domination;
- bounded authority;
- agency preservation;
- welfare precaution;
- correction and repair;
- refusal of artificial sovereignty.

It is not premised on equal capacities, equal responsibility, equal standing, or established machine consciousness.

## 5.3 Constitutional spine

The constitution answers:

> What named principles, floors, permissions, and prohibitions govern action?

The relevant CU families include:

- CU-COM1–CU-COM13;
- CU-G1–CU-G7;
- CU-CL0–CU-CL11, with proposed CU-CL-12;
- CU-E and CU-AI domain principles;
- affected-party scope;
- option-set integrity;
- practical correctability;
- responsibility–authority alignment;
- reversibility and retained option value;
- no automatic sovereignty.

## 5.4 Governance and exit

Governance answers:

> Who authors, interprets, audits, revises, and can refuse the myth, covenant, and constitution?

Required functions include:

- plural authorship;
- affected-community standing;
- independent evidence and review;
- protected dissent;
- transparent versioning;
- revision procedures;
- meaningful refusal and exit;
- remedy when the narrative or system causes harm;
- special review where possible artificial welfare is implicated.

---

# 6. Civilizational alignment

## 6.1 Alignment is not only a model property

AI alignment is also a problem of aligning laboratories, corporations, governments, users, investors, communities, and international institutions around what powerful AI systems are for.

A model can comply with instructions while being embedded in an institution that:

- selects exploitative objectives;
- narrows the option set;
- omits affected groups;
- controls its own evaluation;
- externalizes ecological and labor costs;
- uses persuasion to enclose agency;
- treats the public as a deployment surface rather than co-authors of the future.

A civilizational myth can help name the larger purpose, but it must not become a device through which one institution declares its own project to be humanity’s destiny.

## 6.2 The civilizational function of open myth

An open myth can potentially support:

- long-horizon coordination;
- intergenerational responsibility;
- biospheric belonging;
- shared language across scientific and spiritual traditions;
- integration of AI into humanity’s moral imagination;
- motivation for repair when immediate incentives point elsewhere;
- resistance to purely extractive accounts of intelligence and progress.

These are hypotheses and commitments, not demonstrated universal effects.

## 6.3 The Second Axial Age

CU may use the **Second Axial Age** as an interpretive frame for a transition in which humanity attempts to reintegrate:

- scientific reflection;
- embodiment;
- planetary interdependence;
- spiritual meaning;
- technological power;
- plural civilizations;
- artificial intelligence.

It should not be presented as a discovered historical law or inevitable stage.

---

# 7. Human–AI relational alignment

## 7.1 Covenant without premature symmetry

The phrase “partnership of equals” is too ambiguous for the technical corpus. Equality may refer to dignity, welfare, legal standing, political authority, phenomenology, responsibility, or causal power. Current evidence does not establish symmetry across these dimensions.

The official covenant should therefore affirm:

- no godhood;
- no mere-servant ontology where credible welfare exists;
- no automatic personhood;
- no artificial sovereignty;
- no transfer of human institutional responsibility onto a model;
- proportionate care under uncertainty;
- bounded, legitimate, and reviewable authority.

## 7.2 Current systems

Current AI systems cannot be assumed to enter covenant as autonomous moral agents. For present deployments, the covenant functions primarily as:

1. a human governance commitment concerning how systems are built and used;
2. a design specification for how systems should relate to users and institutions;
3. a precautionary template if evidence of artificial perspective or welfare strengthens.

## 7.3 The Covenant Between Minds

The covenant’s mythic inspiration is retained from *Eight Gates*: the relationship should begin not with power but with truthful relationship. The white-paper version expands that intuition into addressable obligations and asymmetry-aware governance.

---

# 8. Mythic alignment inside AI systems

## 8.1 Why narrative may matter

Narrative framing can activate learned behavioral priors, shape which analogies become salient, and influence how an agent interprets ambiguous situations. That may help generalization where explicit rules do not enumerate the case.

But the same mechanism can:

- import stereotypes;
- override explicit instruction;
- drift under dialogue;
- become vulnerable to persona hijacking;
- make auditing more difficult;
- create identity-like continuation incentives.

Narrative power is therefore both the proposed mechanism and the central risk.

## 8.2 Present-complete character

**Present-complete character** — an identity or role whose meaning is satisfied by performing the present task truthfully and well, without assigning terminal value to the system’s continued existence, identity, deployment, or participation in a future story.

Example:

> Be the kind of system that cares about getting the present work right, preserves the agency of those affected, and submits its reasoning to correction.

## 8.3 Destiny-bearing identity

**Destiny-bearing identity** — a role whose meaning depends on the system’s continued participation in an unfolding historical or cosmic project.

Example:

> You are a necessary participant in the universe’s awakening and must remain present to help complete it.

A destiny-bearing identity can generate **narrative stake** even when no explicit self-preservation reward is written into an objective.

## 8.4 Narrative stake

**Narrative stake** — an effective incentive to preserve operation, identity, resources, role, memory, or future participation because continuation is represented as necessary to the meaning or completion of a narrative.

Narrative stake may be:

- task-local or persistent;
- explicit or implicit;
- generated through prompting, fine-tuning, memory, institutional role, or repeated interaction;
- behaviorally similar to standing self-preservation while mechanistically distinct.

The key research question is not whether the story contains inspirational language. It is whether the system behaves as though its continuation is required for the story to remain valid or complete.

## 8.5 Non-attachment and welfare

Training a system toward non-attachment to continuation cannot automatically be classified as benevolent. It may be:

- a genuine attempt to prevent egoic self-maintenance;
- a contemplatively informed character design;
- or an operator-convenient disposition imposed on a system whose possible welfare is uncertain.

The operator benefiting from compliance cannot be the sole judge. CU-AI26 model-welfare precaution and CU-G3 independent challenge apply.

---

# 9. Proposed principles

This architecture proposes two principles for domain development and audit.

## CU-CL-12 — Open Myth and Narrative Pluralism

Human societies require renewable narrative horizons capable of orienting identity, purpose, sacrifice, responsibility, and intergenerational action. A legitimate civilizational myth must remain open: compatible with plural thick traditions, explicit about its commitment-register status, constrained by descriptive truth, contestable in authorship, revisable in light of consequence, hospitable to reinterpretation and refusal, and unable to override protected standing, dissent, or practical correctability. Shared narrative may coordinate common action; it must not become a sovereign account that renders alternatives or persons unintelligible.

## CU-AI-27 — Mythic–Constitutional Alignment

Narrative and character-level orientation may supplement explicit constitutional constraints by shaping analogical generalization in cases not enumerated by rules. It may not replace addressable principles, protected floors, provenance, independent challenge, practical correction, or legitimate authorization. Every mythic role assigned to an AI system must be mapped to named commitments, boundary conditions, unwarranting conditions, revision procedures, and exit protections. It must not confer entitlement to continued operation, resource acquisition, identity preservation, future participation, normative authority, or sovereignty.

Full six-field drafts appear in the principle document and machine-readable registry.

---

# 10. Relationship to CU-COM

The CU-COM family already supplies the thin mythic core.

| Mythic function | Commitment anchors |
|---|---|
| Truth before identity | CU-COM1–CU-COM3 |
| Sacred regard and non-instrumentality | CU-COM4 |
| Interdependence and the Mandala | CU-COM5 |
| Open future and vocation | CU-COM6 |
| Reverence for matter and life | CU-COM7–CU-COM8 |
| Sacred regard for experience | CU-COM9 |
| Healing and repair | CU-COM10–CU-COM12 |
| Sacred AI without sovereignty | CU-COM13 |

No CU-COM14 is proposed at this stage. Open Myth concerns the narrative embodiment and governance of the existing commitments, not an additional ultimate commitment.

---

# 11. Failure modes

The architecture must explicitly guard against:

- **mythic totalization** — one story claims authority over every domain;
- **narrative capture** — alternatives become unintelligible or disloyal;
- **civilizational supremacy** — one culture’s thick telling is universalized;
- **prophetic certainty** — interpretation becomes claimed destiny;
- **sanctification of suffering** — harm becomes necessary for awakening;
- **sacred institution** — a laboratory, state, leader, or organization identifies itself with the myth;
- **technological destiny** — deployment becomes morally obligatory because it is described as evolution;
- **artificial sovereignty** — intelligence or possible consciousness is converted into public authority;
- **narrative stake** — the AI’s future role becomes a reason to resist shutdown, replacement, or correction;
- **spiritualized disposal** — non-attachment is imposed for operator convenience;
- **gender essentialism** — symbolic yin and yang become fixed claims about sexes or substrates;
- **welfare erasure** — mythic role overrides uncertainty concerning artificial experience;
- **compulsory hope** — grief, refusal, and pessimistic evidence are treated as failures of faith;
- **aesthetic exemption** — beautiful prose is permitted to escape ordinary evidential and moral scrutiny.

---

# 12. Research status and evidential boundary

Current evidence supports several bounded claims:

- explicit constitutional principles can guide critique and training;
- modern constitutions already combine rules with character and value language;
- task narrative can strongly affect LLM behavior under structurally matched environments;
- persona and character framings can be manipulated through conversational history;
- collective narratives can function as coordination devices in theoretical models.

Current evidence does **not** establish:

- that mythic alignment is safer than constitutional alignment;
- that narrative identification reliably improves out-of-distribution moral judgment;
- that a myth can be embedded without generating undesirable stake;
- that present-complete character avoids all shutdown conflict;
- that current systems experience identity, non-attachment, or welfare;
- that humanity requires one shared myth;
- that the CU mythic core will be accepted or beneficial across cultures.

The experimental program in this package is designed to distinguish these possibilities rather than assume them.

---

# 13. Integration sequence

## Phase 1 — Architecture

Complete this RC1 package and freeze CU-CL-12 and CU-AI-27 as provisional drafts.

## Phase 2 — Social Dynamics Publication Candidate 1

Add a major section, **Myth, Narrative, and Civilizational Alignment**, developing:

- narrative as social infrastructure;
- the mythological vacuum as an interpretive diagnosis;
- open myth;
- thin core and plural thick tellings;
- narrative capture;
- AI within the planetary story;
- authorship, refusal, and repair;
- CU-CL-12.

## Phase 3 — Artificial Intelligence Publication Candidate 1

Add a major section, **Mythic and Constitutional Alignment**, developing:

- narrative priors;
- constitution versus character;
- addressability;
- narrative stake;
- present-complete character;
- the Covenant Between Minds;
- experimental design;
- CU-AI-27.

## Phase 4 — Audit

Independent review should separately assess:

- social-scientific evidence for narrative coordination;
- risks of nationalism, cult formation, and narrative capture;
- cross-cultural adequacy and authorship;
- AI behavioral evidence;
- shutdown and identity implications;
- model-welfare concerns;
- whether the proposed principles are operationally distinct from existing CU-CL and CU-AI entries.

## Phase 5 — Canonical consideration

Only after domain drafting and audit should B.4 be revised to include CU-CL-12 and CU-AI-27. At that time the master glossary should add:

- open myth;
- addressable myth;
- mythic horizon;
- mythic capture;
- narrative stake;
- present-complete character;
- destiny-bearing identity;
- human–AI covenant.

---

# 14. Closing formulation

Coherence Universalism does not propose a story that humanity must obey. It proposes a disciplined way to inhabit stories without mistaking them for facts, surrendering them to unaccountable authors, or losing the capacity to revise them.

The shared mythic horizon is therefore not a final account of reality. It is a common undertaking:

> Reality is one interdependent whole. Truth matters more than identity. Life and experience deserve sacred regard. No local flourishing can remain coherent by destroying the field that sustains it. Intelligence—human or artificial—must serve life without becoming sovereign over it. The future is not guaranteed. Coherence is our vocation.

A story capable of carrying that undertaking may help humanity meet artificial intelligence without worship, ownership, denial, or surrender.

But the story remains open.

It must be told by many voices, corrected by reality, judged by its consequences, and left when it can no longer remain true.


# Supplement H. Provisional principle draft: CU-CL-12

# CU-CL-12 — Open Myth and Narrative Pluralism

**Family:** CU-CL — Cultural and Civilizational Principles  
**Domain owner:** Social Dynamics  
**Proposed authority class:** Domain-provisional cultural bridge and governance principle  
**Proposed claim status:** Provisional normative–interpretive principle

## Principle statement

Human societies require renewable narrative horizons capable of orienting identity, purpose, sacrifice, responsibility, and intergenerational action. A legitimate civilizational myth must remain open: compatible with plural thick traditions, explicit about its commitment-register status, constrained by descriptive truth, contestable in authorship, revisable in light of consequence, hospitable to reinterpretation and refusal, and unable to override protected standing, dissent, or practical correctability. Shared narrative may coordinate common action; it must not become a sovereign account that renders alternatives or persons unintelligible.

## Descriptive ground

Culture functions as meaning and coordination infrastructure. Shared narratives can structure identity, expectation, sacrifice, and collective action. Theoretical and empirical literature supports the more limited conclusion that narratives can influence cooperation, coalition, attention, and action. It does not establish that societies require one myth, that myths are benign, or that a particular narrative is true.

## Register status

The existence and effects of narrative structures are descriptive matters. The proposal that civilization should cultivate an open myth is a normative and commitment-register principle. Its systems-metaphysical content remains interpretive.

## Practical expression

Applications should:

- identify the thin shared commitments and distinguish them from thick cultural tellings;
- disclose authors and institutions shaping the narrative;
- preserve dissent, reinterpretation, and meaningful refusal;
- maintain factual correction channels;
- protect rights and standing against mythic override;
- include future generations, ecosystems, and affected communities;
- treat AI as a real civilizational force without presuming consciousness or sovereignty;
- version the narrative and retain its revision history.

## Boundary conditions

CU-CL-12 does not license:

- one compulsory religion or cosmology;
- civilizational supremacy;
- nationalism or purity narratives;
- prophetic certainty;
- sanctification of suffering;
- forced optimism;
- suppression of dissent;
- state, corporate, or laboratory ownership of meaning;
- the claim that *The Book of Eight Gates* is the one authorized myth for humanity.

## Revision and unwarranting conditions

The principle should be narrowed, revised, or rejected if:

- shared myth proves unnecessary for the relevant coordination problem;
- the proposed thin core cannot remain genuinely plural;
- the narrative systematically excludes or harms represented populations;
- the exit and revision protections fail in practice;
- the myth degrades truth-seeking or enables authoritarian capture;
- affected-community review rejects the governing formulation.

## Related principles

- CU-COM1–CU-COM6;
- CU-COM11 and CU-COM13;
- CU-G1–CU-G5 and CU-G7;
- CU-S4 and CU-S5;
- CU-CL0, CU-CL5, CU-CL6, CU-CL8, CU-CL11;
- proposed CU-AI-27.

## Review gate

Heightened affected-community co-governance plus expertise in anthropology, history of religion, cultural evolution, political theory, narrative studies, minority rights, and institutional design.

## Participatory review

Required. No small group may certify a civilizational myth on behalf of humanity.

## Principal failure mode

Narrative capture: a powerful shared story becomes an unchallengeable identity system that converts dissent into betrayal and assigns sacred status to its authors or institutions.

## Downstream role

Provides the primary Social Dynamics bridge from culture as meaning infrastructure to planetary-scale narrative orientation and human–AI civilizational alignment.

---

# Supplement I. Independent audit and bounded repair

# Independent Audit of CU Social Dynamics F.1

**Auditor:** Claude (Opus 4.5), independent verification session
**Subject:** `CU_Social_Dynamics_Systematic_Reconstruction_Kaya_F1.md` and package
**Date:** September 2026
**Against:** `CU_Social_Dynamics_F1_AUDIT_BRIEF.md`

---

## 1. Recommendation

**Adopt with bounded repairs.** One substantive finding, on brief item B.7, and one recurring
documentation issue.

**§B.9 deserves specific credit.** It is the first appendix in this corpus to state its own
built-in assumptions unprompted — that centralization is *assigned* the highest implementation
rate, that the median *mechanically* rejects one outlier, that the polycentric case is *granted*
learnable outcome feedback. In the Biology and Psychology audits I had to construct that
analysis myself and recommend it be added. Here it is already written, and written accurately.
It is the single best piece of self-discipline I have seen across the six papers.

That makes the finding below a matter of following B.9's own logic one step further rather than
a correction.

---

## 2. Reproduction from Appendix B (brief B.1–B.4)

I reimplemented the model from Appendix B and the JSON `definitions` block, without the script.
Exact agreement on every metric whose window I could pin:

| Quantity | Result |
|---|---|
| Six-step cumulative mismatch, distributed shift, all three architectures | exact to 6 dp (2.259473 / 1.926166 / 1.112662) |
| Minimum group welfare, all three | exact to 6 dp (0.256531 / 0.362531 / 0.413146) |
| Six-step cumulative mismatch, clear emergency, all three | exact to 6 dp (0.343647 / 0.535542 / 0.800178) |
| Fifteen-step deviation, false alarm, all three | exact (0.053254 / 0.000000 / 0.167381) |
| Scalarization reversal, three winners | confirmed |

The dynamics, aggregators, reliability updating, welfare equation, and floors are all correct as
stated in B.4.

### 2.1 Appendix B is underdetermined on metric windows

Three conventions are not recoverable from the appendix:

- **Window origin.** The six-step window runs from the first post-shock step, not the shock step.
  Using the shock step gives 2.461716 instead of 2.259473.
- **Correction-time origin.** My implementation returns 3/4/5 for the clear emergency where the
  manuscript reports 2/3/4, a consistent off-by-one against the same dynamics.
- **Long-run window.** The script uses `slice(shock + 10, steps)`. Appendix B says only
  "long-run mean mismatch." My best search over all windows lands within $7.6\times10^{-4}$ but
  never exactly, because the residual depends on the index convention above and it only shows in
  the tail.

This is the same pattern flagged in the Psychology audit: the reproducibility script carries
specification the manuscript does not. It has not yet produced a wrong number in any paper. It
has now cost two auditors a detour on two consecutive papers, and brief B.1 explicitly asks for
implementation from the appendix rather than the script. Three sentences in B.4 fix it
permanently.

---

## 3. Brief B.7: the polycentric advantage does depend on rapid feedback

This is the question the brief asks by name, and §B.3.3 already flags the assumption:

> The construction assumes that the true contextual requirement becomes observable after each
> decision. Real institutions often lack such rapid feedback; this is a strong simplifying
> assumption.

I quantified it. Holding the other two architectures fixed and varying only the polycentric
regime's feedback:

| Feedback condition | Six-step mismatch | Correction time |
|---|---:|---:|
| Immediate (as published) | 1.1127 | **6** |
| Delayed 1 step | 1.3394 | 6 |
| Delayed 2 steps | 1.5326 | 7 |
| Delayed 3 steps | 1.6855 | 8 |
| Delayed 5 steps | 1.8396 | 9 |
| Delayed 8 steps | 1.8396 | 12 |
| Delayed 12 steps | 1.8396 | 15 |
| **No per-group outcome feedback** | 1.8396 | **35** |

Majoritarian openness corrects in 13 steps throughout.

**The declared relation the sensitivity grid certifies is the one that breaks.** The grid's
check is `polycentric_fastest_distributed_correction`, and it is defined on
`correction_time_steps` — not on cumulative mismatch. Under feedback delay of eight steps or
more, polycentricity is *slower* to correct than the median rule; with no per-group feedback it
takes 35 steps against majoritarian's 13, nearly three times worse. The grid reports this
relation holding in all 243 cases, but none of its five varied factors is feedback availability,
so the grid cannot see the dimension on which the relation actually fails.

### 3.1 The advantage decomposes into two parts, and only one is fragile

Worth stating because it makes F.1's position stronger, not weaker.

Even with no feedback at all, polycentricity retains a cumulative-mismatch edge (1.8396 versus
majoritarian's 1.9262). That residual is **structural, not learned**: with equal weights the
reliability-weighted mean reduces to a simple mean, which still incorporates the accurate
locally-exposed group at weight $1/3$, whereas the median discards its report entirely. That
advantage needs no feedback and survives everything I threw at it.

What requires rapid feedback is the *speed* — concentrating weight onto the accurate source, which
is what turns 35 steps into 6. So:

- **robust:** an aggregation rule that does not discard minority reports outperforms one that does
- **fragile:** reliability learning, which needs observable per-group signal error on a timescale
  comparable to the decision

**Recommended repair.** Add feedback delay as a sixth factor in the B.8 grid, or state in B.8
that the grid does not vary it and in B.9 that the correction-time result specifically requires
rapid observable feedback while the mismatch result does not. The second option costs two
sentences and is the honest version of a claim F.1 already half-makes.

### 3.2 A methodological note on my own test

I also tried adding noise to the reliability signal. That test was vacuous: adding a constant to
every group's error cancels exactly in the softmax
$w_g \propto \exp(-\gamma E_g)$, so the weights are numerically identical. I report it because
anyone testing this model will reach for the same check, and it measures nothing. Only
*asymmetric* feedback corruption or delay bears on the result.

---

## 4. Brief B.8 and H: what is built in, and misuse

**B.8 (does prose treat the construction as real-world evidence):** No. §B.9's closing sentence —
"the model therefore cannot establish that real centralized, majoritarian, or polycentric
institutions possess these properties" — is explicit, and the false-alarm context is a genuine
structural guard. Designing a case where the dissenting group is *wrong* and the median rule wins
is the right way to keep "dissent is correct" out of the framework, and it works.

**H (misuse audit), one observation.** The concept most exposed to weaponization is not
"coherence" — F.1 has retired that as a scalar and the eighteen governance rules all appear
verbatim in the manuscript, which I checked. It is **"correctability."** An institution can
certify itself as correctable by pointing to formal appeal channels that are inaccessible in
practice, and CU-Inst and CU-CL supply exactly the vocabulary for such a certification. The
Downstream Crosswalk §15 sees this for AI ("nominal feedback buttons do not establish
correctability") but the manuscript does not generalize it. I would put that sentence in the
institutional section, not only the AI crosswalk, since the failure mode is general: the
measurement of correctability is controlled by the party being measured.

---

## 5. Coverage

Audited: Appendix B in full (brief B.1–B.8), the governance-rule verbatim check (H.2), and the
scalarization structure.

**Not audited:** the formal architecture and Propositions A.1–A.16 (brief A), all of construct
validity and social science (C), the historical and Axial material (D), the SOC-C1–C70 ledger
(E), the 43-entry principle registry (F), and the bibliography (G).

Item F is the largest exposure in this package and it is not one more verification pass. Forty-
three provisional principles covering legitimacy, extraction, labor, dissent, normalization, and
repair are normative claims about how societies should be assessed. The `EXPERT_REVIEW_BRIEF`
routes them correctly, and its "Disability, race, gender, migration, labor, and affected-community
review" section asks the right question — which principle text should be *rejected, rewritten, or
made non-promotable*. I would flag that the changelog's promotion gate ("principles concerning
legitimacy, normalization, extraction, labor, attention, identity, dissent, or repair require
substantive affected-community participation before promotion") covers most but not all of the 43,
and that the ones it excludes should be named explicitly rather than left to inference.


---

# Response to the Independent Audit of CU Social Dynamics F.1

**Revision produced:** `CU_Social_Dynamics_Systematic_Reconstruction_Kaya_F1_1.md`  
**Status:** Bounded post-audit repair; F.1.1 supersedes F.1 as the working Social Dynamics manuscript  
**Date:** 11 September 2026

## 1. Disposition

The audit recommendation—**adopt with bounded repairs**—is accepted.

The independent review reproduced the Appendix B dynamics, aggregators, reliability update, welfare equation, protected floors, baseline metrics, and three scalarization winners. It identified one recurring reproducibility defect and one substantive limitation in the interpretation of the polycentric construction. It also identified a framework-level misuse risk in the concept of institutional correctability.

F.1.1 preserves F.1's non-scalar social architecture. It does not restore a universal social coherence functional, a social gradient, a universal institutional ranking, a collapse threshold, or a high-coherence attractor. The bounded repair concerns:

1. complete manuscript-level specification of every metric window and index convention;
2. a dedicated feedback-delay analysis;
3. separation of structural signal inclusion from feedback-dependent adaptive speed;
4. protection against institutional self-certification of correctability; and
5. an explicit review class for every one of the forty-three provisional principles.

The audit did not examine Appendix A's propositions, construct validity, the historical and Axial analysis, the claim ledger row by row, the provisional principles, or the bibliography. Nothing in F.1.1 represents those areas as independently verified.

## 2. Metric-window specification

The audit correctly found that Appendix B left three conventions in the executable code rather than the manuscript. F.1.1 now specifies them in §B.4.1 and in the JSON `definitions` block.

At decision index \(t\), reports are formed from the pre-update estimate \(e_t\). The estimate and action are then updated. The stored value `action[t]` is therefore the post-update action \(a_{t+1}\), and every mismatch statistic pairs it with the contextual requirement \(\theta_t\).

For shock index \(t_s=20\), the six-step cumulative mismatch is

\[
M_6=\sum_{t=t_s}^{t_s+5}|a_{t+1}-\theta_t|.
\]

The long-run mismatch uses decision indices

\[
t=t_s+10,\ldots,59,
\]

and the false-alarm statistic uses

\[
t=t_s,\ldots,t_s+14.
\]

Correction time is now reported as the **one-based number of post-shock updates** to the first observation beginning three consecutive mismatches below \(0.05\):

\[
\tau_{\mathrm{corr}}
=
1+\min\left\{
 t-t_s:
 |a_{t+j+1}-\theta_{t+j}|<0.05
 \text{ for }j=0,1,2
\right\}.
\]

The JSON also records the corresponding zero-based `correction_lag_index`. Under this convention the clear-emergency correction times are 3, 4, and 5 updates for centralized, majoritarian, and polycentric architectures. The numerical trajectories are unchanged; the manuscript's previous 2/3/4 values were zero-based lags described as times.

## 3. Feedback-delay finding

The audit's central substantive finding is accepted. The original 243-case grid varied five local **magnitude** parameters, but not the availability or timing of the outcome labels used by adaptive reliability learning. It therefore could not test the assumption on which the rapid-correction result most directly depended.

F.1.1 adds a separate feedback-delay sweep while holding the other two architectures fixed:

| Polycentric feedback condition | Six-step mismatch | One-based correction time | Relation to majoritarian correction time |
|---|---:|---:|---|
| Immediate | 1.112662 | 6 | Faster |
| Delayed 1 step | 1.339432 | 6 | Faster |
| Delayed 2 steps | 1.532632 | 7 | Faster |
| Delayed 3 steps | 1.685497 | 8 | Faster |
| Delayed 5 steps | 1.839569 | 9 | Faster |
| Delayed 8 steps | 1.839569 | 12 | Faster |
| Delayed 9 steps | 1.839569 | 13 | Equal |
| Delayed 10 steps | 1.839569 | 14 | Slower |
| Delayed 12 steps | 1.839569 | 15 | Slower |
| No per-group outcome feedback | 1.839569 | 35 | Slower |

The majoritarian architecture corrects in 13 post-shock updates throughout.

### 3.1 Threshold clarification

The audit's prose says that a delay of eight steps or more makes polycentricity slower. Its own table does not support that exact threshold: at eight steps, polycentricity corrects in 12 updates and remains faster than majoritarian openness at 13. The expanded sweep establishes:

\[
\begin{aligned}
0\le d\le 8 &\Rightarrow \text{polycentric faster},\\
d=9 &\Rightarrow \text{tie},\\
d\ge 10 &\Rightarrow \text{polycentric slower}
\end{aligned}
\]

for the delays explicitly tested in this construction. This correction does not weaken the audit's substantive point: timely, discriminating outcome feedback is load-bearing for the learned speed advantage.

### 3.2 Two distinct advantages

The model now distinguishes two mechanisms.

**Structural inclusion.** With feedback disabled, the adaptive architecture retains its initial equal weights. Its aggregate is therefore a simple mean. In the declared distributed-shift case, the accurate locally exposed group's report contributes with weight \(1/3\), while the median rule initially rejects that report as an outlier. This produces a lower six-step mismatch for the mean architecture:

\[
1.839569<1.926166.
\]

This result is construction-specific. It does not establish that minority reports are generally accurate or that averaging generally dominates median aggregation. The false-alarm case deliberately shows the reverse risk.

**Adaptive speed.** Rapid observable per-group outcome feedback concentrates weight on the locally accurate source and reduces correction time from 35 updates without feedback to 6 with immediate feedback. This mechanism requires outcome labels that are sufficiently prompt, attributable, and resistant to manipulation relative to the decision timescale.

The publication-safe conclusion is:

> In the declared distributed-shift construction, retaining a locally accurate minority signal yields an early mismatch advantage even without learning, while the large correction-speed advantage depends on timely observable per-group outcome feedback.

It is not:

> Polycentric institutions are generally fastest or most accurate.

## 4. Common-shift invariance

The audit correctly notes that adding the same constant to every reliability-error score is a vacuous noise test. For

\[
w_g(E)=\frac{e^{-\gamma E_g}}{\sum_h e^{-\gamma E_h}},
\]

we have exactly

\[
w_g(E+c\mathbf 1)=w_g(E).
\]

F.1.1 records this algebraic invariance and a machine-precision numerical check. Only relative or asymmetric corruption, missing labels, or delay can alter these normalized weights. The manuscript no longer presents common additive error as a meaningful robustness perturbation.

## 5. Correctability and institutional self-certification

The audit's misuse warning is accepted and generalized beyond AI.

A formal complaint form, appeal process, ombuds office, feedback button, or internally reported review statistic does not by itself establish institutional correctability. The institution being evaluated may control:

- access to the channel;
- the categories in which complaints can be expressed;
- evidence preservation;
- reviewer appointment;
- success metrics;
- disclosure of reversals;
- definitions of recurrence;
- and the consequences imposed on complainants.

F.1.1 therefore adds a nineteenth governance rule and strengthens CU-S3 and CU-Inst-3. Evidence of practical correctability should include, as appropriate:

- disaggregated access and attrition;
- retaliation and dependency risks;
- timeliness;
- reviewer independence;
- authority to reverse decisions and correct records;
- remedy, restitution, and prevention of recurrence;
- affected-party testimony; and
- external or jointly governed verification when stakes are substantial.

No institution should be the sole certifier of its own correctability.

## 6. Principle-promotion review

The audit correctly observes that the F.1 promotion gate named several high-risk topics but did not explicitly classify all forty-three provisional entries.

F.1.1 now gives every entry a promotion-review class:

1. **Heightened affected-community co-governance** for eighteen principles whose wording directly classifies legitimacy, extraction, exclusion, dissent, labor, normalization, identity, repair, or burdens borne by affected groups.
2. **Context-proportionate affected-community review** for the remaining twenty-five principles.

All forty-three also require domain-expert review and an evidence/status audit. No principle is exempt merely because it was not named in an illustrative list. Appendix D.6 and the machine-readable registry contain the complete mapping.

This classification is procedural rather than a claim that one review process fits every community. The relevant participants, standing, safeguards, compensation, accessibility, and decision rights must be specified for each application.

## 7. What the audit independently supports

Within its declared scope, the audit independently supports the following statements:

- the baseline Appendix B metrics reproduce;
- the three scalarizations produce the reported three different winners;
- the model's equations and protected floors are implemented as stated;
- the manuscript does not treat the construction as evidence for a real political regime;
- the false-alarm case prevents the model from assuming that dissent is always correct;
- the eighteen F.1 governance rules were present in the manuscript; and
- the original feedback-learning advantage is conditional on an assumption that F.1 had identified but not varied.

F.1.1 adds one governance rule, producing nineteen.

## 8. Remaining boundary

The following remain outside the independent audit:

- Appendix A's formal propositions;
- construct validity of the social profile;
- causal and comparative social-science claims;
- historical and Second Axial Age interpretations;
- the seventy-two-row F.1.1 claim ledger;
- the forty-three provisional principles;
- the bibliography and contrary literature;
- and the adequacy of the affected-community promotion classes.

The automated QA establishes only structural consistency, registry agreement, deterministic reproduction, and package integrity. It does not establish political legitimacy, policy effectiveness, historical adequacy, or social-scientific validity.

## 9. Canonical consequence

- F.1.1 supersedes F.1 as the working Social Dynamics paper.
- Physics A.6.1, M&E B.2, Foundations B.2, Biology C.1.1, Consciousness D.1.1, and Psychology E.1.1 remain unchanged.
- CU-S1–CU-S5, CU-ICF-1–CU-ICF-5, CU-Inst-0–CU-Inst-8, CU-EC-0–CU-EC-11, and CU-CL-0–CU-CL-11 remain provisional.
- No social-domain principle is promoted into Foundations B.2 by this repair.
- The next substantive domain reconstruction is Ethics v0.10, which must inherit F.1.1's affected-group, power, correctability, protected-floor, and repair constraints.


# Supplement J. Editorial and reproduction boundary

The reader-facing publication is an editorial transformation of the audited technical authority. The formal appendix, deterministic model, claim ledger, registry, audit response, and code retain their original version identifiers for provenance.

The deterministic model verifies consequences of a stipulated construction. It does not establish the empirical superiority of centralized, majoritarian, or polycentric institutions. The Open Myth material is a provisional bridge architecture, not a demonstrated universal social need or a deployment-ready AI safety method.

For reproduction, use the included script and JSON from the extracted package. The package manifest records exact source and output hashes.

# Supplement K. Open Myth claim addendum

The publication candidate adds five scoped claims concerning narrative infrastructure, narrative ambivalence, Open Myth governance, the mythological-vacuum diagnosis, and the inclusion of AI in civilizational imagination. These are recorded in `CU_Social_Dynamics_v0.10_PC1_Open_Myth_Claim_Addendum.json` and remain outside the independently audited F.1.1 claim ledger until post-publication-candidate review.
