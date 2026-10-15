# CU v0.10 Audit 09: Artificial Intelligence

**Reviewer:** Claude (Opus 5.5)
**Date:** 7 October 2026
**Text audited:** `09_CU_Artificial_Intelligence_v0.10_RC3_Methodological_Spine_Propagation_Draft.md` (24,257 words), from the RC3 Methodological Spine Propagation Working Package (SHA-256 `23409d05…1c3a`, verified)
**Comparison texts:** *Foundations* (02), especially the AI registry (CU-AI-1–26, CU-AI27), CU-COM13, and the 64-stage table; *Metaphysics and Epistemology* (01) for the warrant logic; *Consciousness* (05); *Social Dynamics* (07); the corpus issue log
**Reproducibility:** `cu_ai_audit_checks.py`. Every [C] finding cites its check number (I1–I9).
**Status:** Advisory. This audit assesses internal coherence, formal correctness, and sourcing. It is not an evaluation of any AI system or of whether CU's governance proposals would work (see §7).

**A note on the reviewer.** This paper discusses Anthropic models and research, and lists an uncited working note attributed to Claude. The reviewer is a Claude model. The audit applies the same checks it applied to every other paper; readers should weigh the findings about Anthropic sources with that relationship in mind.

---

## 0. Conventions and coverage

The audit uses the seven-check protocol and the labels of the earlier audits. **[S]** marks a finding that is source-supported, **[C]** one computed or checked by the reviewer and reproduced by the script, and **[I]** reviewer inference.

**Coverage.** Read in full: the front matter, §§1–2, §4.2, §§6.3–6.7, §7, §9.1–9.4, §§12.14–12.15, §13.11, §§15.1–15.3, §§15.10–15.12, and the appendices. The remaining sections (§§3, 5, 8, 10, 11, 12.1–12.13, 13.1–13.10, 14, 16) were covered by whole-paper scans for identifiers, formulas, citations, cross-references, and propagation artifacts, but not read line by line.

**Sources.** Gurnee et al. (2026) and Lindsey (2026) were verified in Audit 05 and are used here consistently with that audit. Anthropic's *Responsible Scaling Policy, Version 3.0* was checked by search. Other sources were checked for bibliographic form only.

**Issue #16.** The handoff asked whether this paper repeats M&E's attribution of the two-stage Or failure to probability thresholds. It does not (§2).

---

## 1. Summary

The paper's central architecture is sound and carefully bounded. Its five non-entailments (§1.5) organize the argument cleanly. The shutdown-incentive analysis of §6.7 is the most useful formal result in the paper, and its algebra is exact: resistance is selected when \(\lambda > s + c - b\), so removing a standing self-preservation reward (\(\lambda = 0\)) still leaves instrumental resistance whenever \(b > s + c\) (I1). The two-stage reasoning section (§12.14) states the fixed-base warrant relation correctly, without the nonemptiness clause that issue #1 corrects and without the probability-threshold misattribution of issue #16 (I2).

Cross-paper agreement is the best in the corpus for a principle family of this size. All 39 identifiers resolve. All 27 AI principles, CU-AI-1 through CU-AI27, match the *Foundations* registry verbatim in title and statement, and the §13.11 CU-AI27 box does too (I4). Stage 59 and stages 32–36 match (I5). The consciousness section is fully consistent with *Consciousness* v0.10's three-clause structure and with the Gurnee et al. self/other ablation result.

One item must be fixed.

- **Seven body sections cite "Appendix B" constructions that do not exist [C].** The paper's non-entailment suite (the floor-hugging option, the institution swap, the three-group feedback case, the shutdown construction, the profile comparison) is cited from §§2.3, 2.6, 6.7, 7.6, 11.3, 11.4, and 12.6 as being in Appendix B. Appendix B is the list of revisions from v0.09. Section 2.8 also points to an "Appendix E" for the twenty-four governance rules; the paper has no Appendix E, and the rules are in Appendix A.2 (M1). This is the most extensive instance of issue #37.

The should-fix items are corpus patterns: propagation residue (S1), uncited references including the KLM and Lehmann–Magidor papers that §12.14 relies on (S3), and the commitment-text drift of issue #32 in CU-COM13 (S5).

**Totals:** 1 must fix, 7 should fix, 4 to consider.

---

## 2. Verified correct

| Item | Check | Result | Label |
|---|---|---|---|
| Shutdown inequality (§6.7; abstract) | I1 | \(V_R > V_C \iff \lambda > s + c - b\); at \(\lambda = 0\), iff \(b > s + c\) | [C] |
| Two-stage warrant relation (§12.14) | I2 | Plain relation \(\operatorname{Min}(W) \subseteq [\![\varphi]\!]\), no nonemptiness clause; no reference to probability thresholds, disjunction, or mixed policies; issue #16 does not recur | [C] |
| Ranked models yield rational monotonicity (§12.14) | read | Correct (Lehmann & Magidor, 1992) | [I] |
| Identifiers cited | I4 | 39 distinct; all resolve | [C] |
| CU-AI-1–26 and CU-AI27, titles and statements | I4 | 27 of 27 verbatim with *Foundations* | [C] |
| CU-AI27 box in §13.11 | I4 | Verbatim | [C] |
| CU-COM13 commitment statement (§15.2) | I4 | Verbatim | [C] |
| Stage 59 and stages 32–36 (§§13.11, 15.11) | I5 | Match *Foundations* | [C] |
| Twenty-four governance rules (Appendix A.2) | I3 | 24, as stated | [C] |
| Consciousness section (§§9.1–9.4) | read | Consistent with *Consciousness* v0.10's three clauses and with Gurnee et al.'s self/other ablation | [I] |
| Second-order to first-order reduction (§9.4) | read | Correct, as in *Consciousness* §5.4 | [I] |
| Appendix C's 92,378-case scalarization lattice | I9 | Equals \(\binom{19}{9}\), the number of weight vectors on a ten-coordinate simplex at step 0.1, matching the ten-coordinate \(\mathbf P_{\mathrm{AI}}\) | [C] |
| Anthropic, *Responsible Scaling Policy, Version 3.0* (2026a) | search | Exists, effective 24 February 2026 (see K1) | [S] |

---

## 3. Must fix

### M1. Seven sections cite Appendix B constructions that do not exist, and one cites a nonexistent Appendix E [C] (§§2.3, 2.6, 2.8, 6.7, 7.6, 11.3, 11.4, 12.6; issues #29, #37)

**Evidence (I3).** The body refers readers to Appendix B for:

- the constructed comparison using \(\mathbf P_{\mathrm{AI}}\) (§2.3);
- "a simple proof by construction" that a floor-hugging option becomes uniquely admissible when better options are withheld (§2.6; again in §11.3);
- "the deterministic construction" behind the shutdown inequality (§6.7);
- a comparison that "holds the model architecture fixed and changes the institution" (§7.6);
- "a three-group construction" in which a controller fits the observed majority perfectly while failing an omitted group (§11.4); and
- "the option-set attack" (§12.6).

Appendix B is the list of twenty revisions from v0.09 and contains none of these. The abstract's sixth paragraph reports the same suite ("A deterministic suite illustrates several non-entailments"), and Appendix C places it in the technical supplement, which is not in the package. Separately, §2.8 says "this paper includes twenty-four application rules in Appendix E"; there is no Appendix E, and the rules are Appendix A.2.

The §6.7 algebra is self-contained and correct (I1), and the other non-entailments are plausible and easy to construct. But as the paper stands, its principal formal demonstrations are cited to a place that does not hold them.

**Recommended revision.** Either add the suite as a new Appendix D (each construction needs a few lines), or change every "Appendix B" pointer to "the technical supplement." Change "Appendix E" to "Appendix A.2." Issue #37 now covers *Consciousness*, *Social Dynamics*, and *AI*; a single global search for "Appendix B" across the corpus would close it.

---

## 4. Should fix

### S1. Propagation residue [C] (throughout; issues #7, #9)

**Evidence (I7).** Eleven sentences or table cells begin with lowercase "this paper"; one sentence has "This paper" capitalized mid-sentence ("For the wider system, This paper uses," §2.3); §9.2 opens with "Consciousness Consciousness v0.10"; three lines (94, 2170, 2556) consist of a lone backslash, which renders as a stray character; and the Domain Analytic Frame carries the RC2 baseline line.

**Recommended revision.** Global fixes for the first two; delete the doubled word and the three backslash lines.

### S2. Identifier format [C] (throughout; issue #8)

**Evidence (I4).** The paper uses CU-AI-1 through CU-AI-26 and CU-AI27 side by side, as *Foundations* does.

**Recommended revision.** Resolve under issue #8 before the registry freezes.

### S3. Citation practice [C] (References; issues #11, #23)

**Evidence (I8).** Twenty of the 45 non-self entries are never cited by author and year. Two matter for the argument: Kraus, Lehmann, and Magidor (1990) and Lehmann and Magidor (1992) supply the KLM representation theorem and the ranked-model result that §12.14 invokes, but the section cites only M&E. Others are drawn on without citation (Butlin et al., 2023, on consciousness indicators; Raji et al., 2020, and Mitchell et al., 2019, on audits and model cards). The list again includes an uncited, unpublished working note attributed to Claude (see Audit 07 S6). The Gurnee et al. entry lacks arXiv:2607.15495 (#11).

**Recommended revision.** Cite KLM (1990) and Lehmann–Magidor (1992) in §12.14; cite the other drawn-on works where used or drop them; remove the Claude entry; add the arXiv number.

### S4. The paper relies on a result that exists only in another paper's supplement [C] (§2.7)

**Evidence (I7).** Section 2.7 says "A result from *Social Dynamics* carries directly into AI: adaptive correction can depend on timely and attributable outcome feedback." In *Social Dynamics*, that result appears only in the abstract and the technical supplement; the body does not contain it (Audit 07 S1). A reader following the cross-reference finds nothing.

**Recommended revision.** State the result in one sentence here as a conditional claim ("in a deterministic model with delayed feedback, the adaptive regime's correction advantage disappears as delay grows"), and resolve Audit 07 S1 so the cross-reference has a target.

### S5. CU-COM13's boundary and revision conditions are paraphrased [C] (§§15.2, 15.12; issue #32)

**Evidence (I4).** The CU-COM13 commitment statement is verbatim. The practical expression, boundary conditions, and revision conditions are not: §15.12 expands the *Foundations* revision condition into an eight-item list, and the *Foundations* boundary conditions ("A model may be sacred and unsafe…") appear only as a section title (§15.6). The content is consistent; the texts are not the same.

**Recommended revision.** Quote the four *Foundations* fields in §15.2, then elaborate. This is the same pattern as CU-COM12 in *Ethics* (Audit 08 S1).

### S6. "Provisional research program" versus canonical principle [C] (abstract; Appendix B; issue #36)

**Evidence (I6).** The abstract (line 32) and Appendix B item 19 call mythic–constitutional alignment "a provisional research program." Section 13.11 and Appendix A call CU-AI27 a "canonical research and governance principle; safety efficacy unestablished." The two can be reconciled (the principle is canonical; the research program testing it is ongoing), but as written they read as a status conflict, like CU-CL12 in *Social Dynamics*.

**Recommended revision.** In both places, write "a research program under CU-AI27, canonical as a research and governance principle whose safety efficacy is unestablished."

### S7. Notation [C] (§§2.1–2.3)

**Evidence.** The system tuple's \(A\) (affected parties), \(E\) (environment), and \(\mathsf S\) (scaffold) sit beside profile coordinates \(A_c\), \(E_p\), \(S_a\), and \(S_c\). \(Tr\) means "transfer" in the capability profile here and "trust" in *Social Dynamics*. Both profiles use \(Q\) for task performance, which is consistent but means the deployment profile cannot be read without the capability profile in mind.

**Recommended revision.** As for the other domain papers: give profile coordinates a distinct naming scheme, and keep corpus-wide abbreviations such as \(Tr\) unambiguous.

---

## 5. Consider

**K1. The RSP v3.0 characterization [S] (§6.3).** The paper cites Anthropic's *Responsible Scaling Policy, Version 3.0* as an example of frameworks that "organize evaluation around capability or risk thresholds that trigger stronger safeguards." Version 3.0 (24 February 2026) restructured that approach around risk reports, a frontier-safety roadmap, and industry-wide recommendations, and dropped the earlier pause commitment. A clause noting that the frameworks themselves are changing would keep the sentence accurate.

**K2. Ties in the shutdown inequality (§6.7).** "Resistance is selected exactly when \(\lambda > s + c - b\)" leaves the case \(V_R = V_C\) unassigned. One phrase ("with ties resolved toward compliance") completes the statement.

**K3. A fix for issue #34 is already in this paper (§§7.4, 7.9).** Section 7 correctly attributes the identity, memory, and norm-source boundaries to the earlier *Architecture of a Coherent Mind* and distinguishes it from the v0.10 *Non-Egoic* paper. *Consciousness* §10 attributes the same four boundaries to the *Non-Egoic* paper (Audit 05 S2). Adopting the AI paper's attribution in *Consciousness* would close issue #34.

**K4. Describe the scalarization lattice (Appendix C).** The 92,378-case lattice is exactly the set of weight vectors on the ten coordinates of \(\mathbf P_{\mathrm{AI}}\) at step 0.1 (I9). Saying so in Appendix C would let readers understand what was enumerated without the supplement.

---

## 6. Relation to the issue log

- **#7 (artifacts).** Eleven lowercase "this paper," one mid-sentence capital, one doubled word, three lone backslashes (S1).
- **#8 (identifier formats).** Confirmed (S2).
- **#9 (RC2 baseline).** Confirmed.
- **#11 (Gurnee arXiv).** Confirmed missing (S3).
- **#16 (two-stage Or failure).** Does not recur; §12.14 is correct. Close for *AI*; the fix remains in M&E and *Foundations*.
- **#19 (dependency tables).** None in *AI*.
- **#23 (citation practice).** Twenty unused entries, including KLM and Lehmann–Magidor (S3).
- **#29 (supplements).** The non-entailment suite (M1).
- **#30 (∼ for consequence).** *AI* §12.14 also writes \(\sim_C\) rather than \(\mid\!\sim_C\).
- **#32 (text drift).** CU-COM13 fields (S5). The 27 AI principles themselves are verbatim, the best result in the corpus.
- **#34 (Non-Egoic description).** *AI* §7 supplies the correct attribution (K3).
- **#36 (provisional versus canonical).** Extended to CU-AI27 (S6).
- **#37 (Appendix B pointers).** Seven more, plus a nonexistent Appendix E (M1). Raise to must-fix.

---

## 7. Standing caution

Every finding here concerns internal coherence, formal correctness, or sourcing. The paper's governance architecture is offered as a proposal, and the paper itself says it "succeeds only if it improves prediction, control, agency, correction, and repair in measured deployments." This audit cannot assess that.

Passing this audit does not show that the proposed architecture would make any AI system safer.
