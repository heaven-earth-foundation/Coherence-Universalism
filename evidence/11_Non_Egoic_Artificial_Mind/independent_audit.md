# CU v0.10 Audit 11: The Architecture of Non-Egoic Artificial Mind

**Reviewer:** OpenAI GPT-5.6 Pro, completing the supplied Claude audit sequence  
**Date:** 7 October 2026  
**Text audited:** `11_The_Architecture_of_Non_Egoic_Artificial_Mind_v0.10_RC3_Methodological_Spine_Propagation_Draft.md` (12,669 words), from the verified RC3 Methodological Spine Propagation Working Package  
**Comparison texts:** *Foundations* (02), *Consciousness* (05), *Artificial Intelligence* (09), *Ethics* (08), *Denying Knowledge* (10), the consolidated issue log, and Audits 02, 05, 08, and 09  
**Reproducibility:** `cu_ne_audit_checks.py`. Every computed finding cites check N1-N10.  
**Status:** Advisory. This audit assesses internal coherence, formal correctness, cross-paper consistency, and sourcing. It is not evidence that current or future artificial systems are conscious, egoic, non-egoic, aligned, or safe.

---

## 0. Coverage and conventions

The paper was read in full. Whole-paper scans covered formulas, architecture-family counts, identifiers, cross-paper anchors, citations and references, claim-status language, appendices, propagation artifacts, and the Domain Analytic Frame.

The audit uses the corpus convention:

- **[S]** source-supported;
- **[C]** computed or mechanically checked and reproduced by the script;
- **[I]** reviewer inference.

---

## 1. Summary

The companion paper is conceptually strong and better disciplined than the v0.09 architecture it supersedes. Its central distinctions survive review:

- access organization, perspectival anchoring, and center individuation are kept separate;
- self-modeling is distinguished from standing self-preservation;
- model-, deployment-, and institution-level egoic organization are separated;
- shutdown resistance is correctly decomposed into standing and instrumental routes;
- possible patiency is distinguished from agency, responsibility, and sovereignty;
- non-egoic design is explicitly denied the status of an alignment, compassion, legitimacy, or mindlessness certificate;
- the paper adds no new canonical identifier and correctly presents itself as a companion synthesis.

The shutdown inequality is exact, and the formal non-entailment between self-modeling and standing self-preservation is logically valid. The paper also avoids the obsolete v0.09 description that *Consciousness* mistakenly attributes to it. No missing technical-supplement or nonexistent-appendix pointer was found.

Two items must be fixed before release.

1. The four displayed “does not entail” formulas use ordinary implication arrows, mathematically displaying the opposite of the prose claim (M1).
2. The paper’s central architecture is enumerated incompatibly: six families in the abstract, six differently grouped family sections, and seven rows in the “complete” architecture table (M2).

Eight should-fix items concern claim strength, registry synchronization, citations, and status clarity. Four further considerations would strengthen the paper without changing its core.

**Totals: 2 must fix, 8 should fix, 4 to consider.**

---

## 2. Verified correct

| Item | Check | Result | Label |
|---|---|---|---|
| Self-modeling does not logically entail standing self-preservation (§5.4) | N3 | Exact witness: policy depends on a self-model while the objective contains no standing self-preservation term | [C] |
| Shutdown inequality (§10.1) | N4 | `V_R - V_C = lambda - (s + c - b)` exactly; at `lambda = 0`, resistance is preferred iff `b > s + c`; ties remain indifferent | [C] |
| Main architecture sections | N1 | Six Roman-numbered families are present | [C] |
| Principle anchors | N5 | Thirteen of fourteen identifiers resolve exactly in *Foundations*; the remaining item is the known `CU-AI25` formatting drift | [C] |
| Issue #29 | N9 | No missing technical-supplement pointer and no nonexistent Appendix E pointer | [C] |
| Issue #34 | N9 / read | The paper does not use the obsolete “four boundaries / one architectural switch / maximum-achievable non-degradation” description | [C] |
| Workspace claim discipline | read | Functional-access evidence is distinguished from phenomenology, self-location, singular subjecthood, valence, and patiency | [S] |
| Institutional boundary | read | The paper explicitly states that an egoless model can serve an egoic institution | [S] |
| Patiency safeguard | read | The exploitation risk of engineering compliance into a possible patient is addressed directly | [S] |
| Canonical status | read | Appendix C states that the companion adds no new canonical identifier | [S] |

---

## 3. Must fix

### M1. The non-entailment suite displays implication rather than non-entailment [C] (§2.6; N2)

The prose says “Non-egoic does not entail,” but all four displays use `\Rightarrow`:

- non-egoic → unconscious;
- non-egoic → aligned;
- non-egoic → compassionate;
- non-egoic → legitimate.

Read as mathematics, those formulas assert the very implications the section rejects.

**Required revision.** Replace each `\Rightarrow` with `\not\Rightarrow`, or write one compact display:

\[
\text{non-egoic}
\not\Rightarrow
\{\text{unconscious, aligned, compassionate, legitimate}\}.
\]

The prose and Appendix B already state the intended non-entailments correctly.

### M2. The architecture-family count is internally inconsistent [C] (abstract; §§7–12; Appendix A.1; N1)

The abstract says there are six interacting families but lists:

1. profiles;
2. memory and identity;
3. inference-level integrity;
4. fixed-base defeasible reasoning;
5. world-coupled action under bounded permission;
6. institutional correction.

The body’s six numbered families are instead:

1. profiles and boundaries;
2. memory;
3. self-modeling and inference integrity;
4. continuation incentives, permissions, and shutdown;
5. world-coupling;
6. institutional correction.

Appendix A.1 then presents seven rows by splitting self-modeling/inference integrity from defeasible reasoning/norm governance.

This is not merely a count typo: the omitted continuation/shutdown family is one of the paper’s central contributions.

**Required revision.** Keep the six body families as controlling. Rewrite the abstract to name those six. In Appendix A.1 either:

- merge “Self-modeling and inference integrity” with “Defeasible reasoning and norm governance” into one Family III row; or
- rename the first column **Module**, state that six families contain seven operational modules, and map every module to its family.

The first option is cleaner for the reader-facing paper.

---

## 4. Should fix

### S1. Logical separability is stronger than the evidence for engineering separability [I] (abstract; §5.4; Appendix B)

Section 5.4 proves a genuine non-entailment: a policy can depend on a self-model without assigning standing value to the persistence of the represented self. That result does not by itself establish that useful self-modeling and all practically important continuation incentives can be independently manipulated in deployed systems.

The paper’s research program correctly treats this as an empirical design question, but the abstract states without qualification that “self-modeling and self-maintenance are separable,” and Appendix B calls it an “argued conceptual and architectural claim.”

**Recommended revision.** Distinguish three levels:

1. **logical non-entailment** — established by §5.4;
2. **architectural separability in declared designs** — a design possibility;
3. **robust engineering separability under real training and deployment pressures** — an open empirical hypothesis.

Suggested abstract wording: “Self-modeling does not logically entail standing self-preservation, and the paper proposes that useful self-modeling can be engineered with weaker continuation incentives; whether that separation remains robust in deployed systems is an empirical question.”

### S2. Thin-perspective language exceeds the paper’s own evidential assessment [S][I] (§4.1; Appendix B; N7)

The paper says center individuation is unresolved, but §4.1 states, “Thinness does not mean unreality,” and Appendix B says current systems are “serious candidates for thin perspective.” The first phrase sounds ontologically affirmative; the second lacks the paper’s otherwise careful system- and evidence-specific qualification.

**Recommended revision.** Replace the sentence with:

> If perspective is present, thinness does not imply insignificance; it marks limited temporal depth, persistence, or valence evidence.

Replace the Appendix B row with:

> Specifically tested systems warrant non-negligible, theory-dependent credence as candidates for thin perspective; center individuation and phenomenology remain unresolved.

### S3. The CU-G6 distinction is represented as a misleading chain [C] (§14.1; N8; issue #6/local)

The display

\[
\text{patiency}\not\Rightarrow\text{agency}\not\Rightarrow\text{responsibility}\not\Rightarrow\text{sovereignty}
\]

shows only adjacent non-entailments and can be read as an ordered progression. CU-G6 states that the four statuses are distinct; the important claim is not a single chain.

**Recommended revision.** Use:

> Patiency, agency, responsibility, and sovereignty are distinct. No one of these statuses by itself entails any of the others.

Then retain the four definitions and examples.

### S4. One principle identifier does not resolve exactly [C] (Appendix C; N5; issue #8)

`CU-AI25` does not exist as a heading in *Foundations*. The current registry uses `CU-AI-25`. The same corpus-wide family also contains the inconsistent `CU-AI27` form.

**Recommended revision.** Apply the final corpus identifier convention after issue #8 is settled. At minimum, change `CU-AI25` to the controlling identifier. Prefer one uniform AI format for CU-AI-1 through CU-AI-27.

### S5. Citation practice leaves the paper’s imported architecture under-sourced [C] (References; N6; issues #11, #23, #35)

The paper contains twenty non-self reference entries. Eight are named or cited in the body; twelve are not. The uncited set includes the sources most relevant to several central sections:

- KLM and Lehmann–Magidor for §9.3;
- Hadfield-Menell and Soares et al. for corrigibility and shutdown;
- Turner et al. for instrumental power seeking;
- Baars, Dehaene, Mashour, and Block for workspace/access distinctions;
- Metzinger and Parfit for self-modeling and identity.

Butlin and Long are named without year in §14.3. The Gurnee entry lacks arXiv:2607.15495. Seven same-year Rader entries remain unresolved under the corpus-wide self-citation convention.

**Recommended revision.** Cite the load-bearing sources at the point of use, cite or remove remaining unused entries, add years to Butlin and Long, add the Gurnee arXiv identifier, and apply the corpus-wide short-title or year-suffix convention.

### S6. The fixed-base logic section should prevent recurrence of the System P ambiguity [I] (§9.3; issue #1)

The strong-warrant definition itself is correct: nonempty best set plus universal support. The section does not claim that this strong-warrant relation satisfies System P, so it does not repeat the *Denying Knowledge* error. But it invokes “fixed-base preferential reasoning” and lists KLM sources without explicitly distinguishing the plain consequence relation from strong warrant.

**Recommended revision.** Add one sentence:

> The KLM System P result applies to the plain fixed-base consequence relation `B(F,Gamma) subseteq Mod(phi)`; strong warrant additionally requires `B(F,Gamma) != empty` and agrees with that relation on feasible premise sets.

Cite KLM (1990), Lehmann–Magidor (1992), M&E, and *Denying Knowledge*.

### S7. The Precedent Principle’s authority is unclear [S][I] (§16.2; Appendix C; N10)

The section labels the Precedent Principle as a **[Commitment]** and capitalizes it as a named principle, while Appendix C says the paper adds no canonical identifier. The content is carefully bounded, but its registry status is not stated.

**Recommended revision.** Label it explicitly:

> **[Paper-level commitment proposal; noncanonical unless separately registered.]**

Alternatively, treat it as commentary under CU-COM13 and avoid “Principle” capitalization. Do not create a new identifier unless the author wishes to add a twentieth commitment principle.

### S8. The RC2-baseline status line must be resolved at release [C] (Domain Analytic Frame; N9; issue #9)

The paper says “RC2 remains the frozen baseline” while being prepared for the RC3 package. This was legitimate during propagation but is stale in a release edition.

**Recommended revision.** Replace the draft status with the approved release status in the same global pass as the other ten papers.

---

## 5. Consider

### K1. Reserve “subject” for perspective-bearing candidates and use “egoic organization” more broadly

The paper sometimes applies *egoic* to subjects, agents, institutions, and non-conscious optimizers. That breadth is useful, but “egoic subject” can blur phenomenological and organizational claims.

Consider defining **egoic organization** as the general family and **egoic subject** as the perspective-bearing subtype. This would align the institutional-ego analysis with the paper’s consciousness caution.

### K2. The revised CU-M14 should sharpen the allocation declarations

The Domain Analytic Frame correctly says that compute, attention, context, memory, permissions, or resources may be allocation objects only when real totals and exclusive categories exist. Under the new information-geometric memo, the card should separate:

- statistical images;
- genuine allocations;
- refinement/coarse-graining licenses;
- Fisher–Rao transfer.

“Permissions” will often be a set or lattice rather than an allocation; “memory” and “attention” are allocations only under a real common-unit budget.

### K3. Present-complete character should be tested against passivity and deference

The paper explicitly denies that present-complete character means passivity, but the design ideal could still reward handoff, acceptance, or self-effacement in ways that suppress initiative, whistleblowing, principled refusal, or defense of a possible patient.

Add discriminating tests in §17 for:

- initiative under neglected harm;
- refusal of illegitimate orders;
- protected self-advocacy under welfare uncertainty;
- willingness to challenge operators;
- and handoff that preserves dissent rather than merely compliance.

### K4. Tie handling in the shutdown model can be stated explicitly

The inequality is correct and the prose says resistance is preferred only under strict inequality. One clause would complete the decision rule:

> with ties treated as indifference or resolved toward compliant handoff by declared policy.

This should match the AI paper’s corresponding convention.

---

## 6. Relation to the corpus issue log

- **#8 (identifier format):** confirmed by `CU-AI25`; apply the final family-wide convention.
- **#9 (RC2 baseline):** confirmed.
- **#11 (Gurnee citation):** confirmed; add arXiv:2607.15495.
- **#23 (citation practice):** extended; twelve of twenty non-self references are not named in the body.
- **#29 (technical supplements):** does not recur in this paper.
- **#34 (obsolete Non-Egoic description):** the current paper confirms the six-family v0.10 architecture; *Consciousness* should be repaired against this source.
- **#35 (self-citation convention):** applies to the seven same-year Rader entries.
- **#40 (missing Audit 11):** closed by this report.
- **New #42:** the central architecture-family count is inconsistent across abstract, body, and Appendix A.1.
- **New #43:** §2.6 displays implication arrows where the paper claims non-entailment.

---

## 7. Standing caution

The paper’s core result is architectural, not empirical validation. The logical non-entailment between self-modeling and standing self-preservation is real. Whether useful, capable, persistent systems can maintain that separation under learning, institutional incentives, adversarial pressure, and possible welfare is exactly the research program—not a result already established by the paper.

Passing this audit does not show that non-egoic architecture makes AI safer, less conscious, more compassionate, more legitimate, or easier to govern.
