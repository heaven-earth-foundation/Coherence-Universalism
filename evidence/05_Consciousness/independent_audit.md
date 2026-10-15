# CU v0.10 Audit 05: Consciousness

**Reviewer:** Claude (Opus 5.5)
**Date:** 7 October 2026
**Text audited:** `05_CU_Consciousness_v0.10_RC3_Methodological_Spine_Propagation_Draft.md` (22,771 words), from the RC3 Methodological Spine Propagation Working Package (SHA-256 `23409d05…1c3a`, verified)
**Comparison texts:** *Foundations* (02), especially the Consciousness and Valence registry, CU-COM9, CU-G6, and the 64-stage table; *Biology* (04); *Non-Egoic Artificial Mind* (11); M&E (01) for the §10.4 taxonomy; the corpus issue log
**Reproducibility:** `cu_co_audit_checks.py`. Every [C] finding cites its check number (Q1–Q11).
**Status:** Advisory. This audit assesses internal coherence, formal correctness, and sourcing. It is not evidence about whether any system discussed in the paper is conscious (see §7).

---

## 0. Conventions and coverage

The audit uses the seven-check protocol and the labels of the earlier audits. **[S]** marks a finding that is source-supported, **[C]** one computed or checked by the reviewer and reproduced by the script, and **[I]** reviewer inference.

**Coverage.** The paper was read in full: front matter and the Domain Analytic Frame, §§1–15, Appendices A–C, and the references. Section 11 (the ten research programs) was read for structure and discriminating outcomes rather than sentence by sentence. Whole-paper scans covered identifiers, principle titles and statements against *Foundations*, citations, notation, and propagation artifacts.

**Sources.** The paper's most consequential empirical claims rest on two 2026 interpretability studies, so those were checked closely. Gurnee et al. (2026) was read through its §3 in the arXiv version (2607.15495), and every figure the paper quotes from §§2–3 of that source was compared. Lindsey (2026) and the Cogitate Consortium (2025) were checked by search. The remaining references are standard works and were checked for bibliographic form only. Two figures the paper attributes to Gurnee et al. come from the source's §4, which the fetched text did not reach, and were not verified (K2).

---

## 1. Summary

*Consciousness* is a careful paper on a hard subject, and its handling of the empirical evidence is a strength. Its central bridge hypothesis (PIH) is stated with three separately evidenced clauses and an explicit rule against counting evidence for one clause toward another. It then applies that rule to its own best evidence: §7.4.1 reports the experiential-report ablation result that cuts against the self-location clause, and the paper lowers its own assessment to match. Every figure it quotes from §§2–3 of Gurnee et al. is accurate, including the 90-prompt swap result (61, 60, 28, and 6 percent), the 6–7 percent median variance, and the models tested. The paper also reports the source authors' own disclaimers accurately: they take no position on phenomenal experience and do not claim the full neuronal workspace architecture. The Lindsey and Cogitate descriptions are accurate too.

Cross-paper agreement is excellent. All 27 identifiers resolve, all 27 titles match *Foundations*, all 14 principle statements in Appendix A match the registry verbatim, the six Mandala stages named in Appendix A match, and the CU-COM9 commitment, boundary, and revision condition match exactly (Q4–Q6). The §10.4 restatement of the warrant taxonomy is consistent with M&E's fixed-base result and with the issue #1 fix, and it does not repeat the Or-failure misattribution of issue #16.

Three items must be fixed.

- **Appendix A has an empty Status column [C].** All fourteen principles have a blank status cell, although *Foundations* records a claim status for each (M1).
- **A cross-reference points to nothing [C].** Section 3.13 says "Appendix B gives an explicit construction" of a ranking reversal. Appendix B is the revision list and contains no construction (M2).
- **The paper both denies and asserts a PIH threshold [C].** Section 4.2 says PIH "does not define a numerical threshold," and §§1.3 and 15 reject threshold thinking. But §4.9 refers to "the PIH threshold," and the principle box in §10.8 begins "Because the thin threshold may already have been crossed in some systems" (M3).

The should-fix items are mostly corpus hygiene. The paper has 52 sentence-initial lowercase "this paper" artifacts and two ungrammatical ones (S5). It lists CU-V7 as a live principle, although *Foundations* records it as a superseded alias of CU-G6 (S1). Section 10 describes features of the companion non-egoic paper that do not appear in that paper's v0.10 text (S2). And 14 of its 33 non-self references are never cited in the text, while the Cogitate study, which it discusses three times, is never cited by author and year (S4).

**Totals:** 3 must fix, 7 should fix, 6 to consider.

---

## 2. Verified correct

| Item | Check | Result | Label |
|---|---|---|---|
| Identifiers cited | Q4 | 27 distinct; all resolve; all titles match *Foundations* | [C] |
| Appendix A principle statements (CU-C1–C7, CU-V1–V7) | Q4 | 14 of 14 identical to the registry | [C] |
| Mandala stages 16–21 named in Appendix A | Q5 | All six titles identical | [C] |
| CU-COM9 statement, boundary, and revision condition (§14) | Q6 | Identical to *Foundations* | [C] |
| §5.4: a second-order equation is a first-order system on the expanded state | Q1 | The first-order solution satisfies the second-order equation to finite-difference error (3×10⁻⁴) | [C] |
| §3.13: weights can reverse a ranking between non-dominated profiles | Q2 | Reconstructed (10.0 vs 9.9 under one weighting, 5.8 vs 11.6 under another) | [C] |
| §7.11: static strongly connected components cannot settle unity in a time-unfolded causal-attention computation | Q3 | The unrolled (layer, position) graph is acyclic; every component is a single node | [C] |
| §10.4 warrant taxonomy | read | Consistent with M&E's fixed-base System P result and the issue #1 fix; no Or-failure misattribution (#16) | [I] |
| Gurnee et al. (2026): 90 two-hop prompts; probe J-space swap 61%, raw J-lens swap 60%, non-J-space 28%, clamped 6% | source | All four figures match the source's §3.3 | [S] |
| Gurnee et al.: concept-vector J-space component carries a median 6–7% of variance; J-space never above 10%; about 25 active vectors | source | Match §§2.3 and 3.1 | [S] |
| Gurnee et al.: default model Sonnet 4.5, corroboration on Haiku 4.5 and Opus 4.5, some analyses on Opus 4.6 | source | Matches §2.5 | [S] |
| Gurnee et al.: experiential-report ablation is not self-specific; story-writing control; possible access/selfhood dissociation (§7.4.1) | source | Matches §3.5.3 | [S] |
| Gurnee et al.: authors take no position on phenomenal consciousness, and do not claim the full workspace architecture (§7.4) | source | Matches §§1.1 and 1.3 | [S] |
| Lindsey (2026), arXiv:2601.01828 (§7.5) | search | Exists; injected-concept detection, prefill discrimination, unreliability and post-training sensitivity as described | [S] |
| Cogitate Consortium (2025), *Nature* 642 (§§4.6, 6.4, 6.9) | search | n = 256; fMRI, MEG, iEEG; sustained posterior synchronization and offset ignition both challenged, as described | [S] |

---

## 3. Must fix

### M1. Appendix A gives no status for any principle [C] (Appendix A; issue #6)

**Evidence.** The Appendix A table has four columns: ID, Principle, Status, and Controlling statement. The Status cell is empty for all fourteen rows (Q4). The principles appear nowhere else in the paper with a status, so a reader cannot tell from this paper that, for example, CU-C2 is a "canonical bridge hypothesis," CU-C4 a "canonical methodological principle," and CU-V6 a "canonical correction / provisional hypothesis." *Foundations* supplies all fourteen values (Q4). The paper's own claim-governance rules (§2.10) require the status of a claim to be declared.

**Recommended revision.** Fill the column from the *Foundations* "claim/candidate status" field. Mark CU-V7 as described in S1.

### M2. Section 3.13 cites a construction that is not in Appendix B [C] (§§3.13–3.14)

**Evidence.** Section 3.13 says weights can reverse rankings between an access-rich and an embodied system, and that "Appendix B gives an explicit construction." Appendix B is the list of revisions from v0.09 and contains no construction, weights, or formula (Q8). Section 3.14 adds that the architecture "establishes several independence results through constructed counterexamples," and none appear in the paper. Appendix C places the "formal counterexamples" in the technical supplement, which is not in the package (issue #29).

The claim itself is correct and easy to show (Q2).

**Recommended revision.** Put a short worked example in the text of §3.13, for instance two ten-coordinate profiles of which neither dominates, and two weight vectors that order them differently. Change §3.14 to "the technical supplement gives constructed counterexamples," or move one of them into the paper.

### M3. The paper denies a PIH threshold and then invokes one [C] (§§4.2, 4.9, 10.8)

**Evidence.** Section 4.2 says "PIH does not define a numerical threshold at which phenomenology is stipulated into existence," §1.3 makes candidate status graded, and §15 opens by rejecting compression into "one threshold." Section 4.9 then says "the PIH threshold requires a specific organization." The bolded design and ethical principle of §10.8 begins "Because the thin threshold may already have been crossed in some systems" (Q8). The §10.8 sentence is a principle statement, so readers will quote it, and as written it asserts a crossing that the paper's own method says cannot be a threshold event.

**Recommended revision.** In §4.9, write "PIH requires a specific organization." In §10.8, write "Because some tested systems may already warrant non-negligible credence as hosts of thin perspective, developers should not wait for certainty…" This states the same precautionary point in the paper's graded terms.

---

## 4. Should fix

### S1. CU-V7 is presented as a live principle [C] (Appendix A)

**Evidence.** *Foundations* records CU-V7 ("Moral Patiency Is Not Sovereignty") with authority class "superseded alias" and the disposition "controlling identifier is CU-G6" (Q4). M&E says the same. *Consciousness* lists CU-V7 in its principle table as a controlling statement without saying it is an alias. Its cross-reference paragraph does mention CU-G6, but not the relation between them.

**Recommended revision.** Keep the row for continuity, with Status "superseded alias; controlled by CU-G6." *Ethics* carries the parallel alias CU-E-17 as a section heading, twice; recorded as issue #33.

### S2. Section 10 describes a version of the companion paper that no longer exists [C] (§§10.1, 10.4, 10.5)

**Evidence.** Section 10.1 says *The Architecture of Non-Egoic Artificial Mind* identifies a correction to "four boundaries" (externally versioned identity, write-gated memory, task-scoped self-models, externally imposed norms). Section 10.5 says "the companion paper describes the fork … as one architectural switch," and §10.4 discusses its "superseded 'maximum-achievable coherence non-degradation' clause." None of these phrases occurs in the v0.10 *Non-Egoic* paper, which is organized instead around six architecture families (Q11). Only "bodhisattva construction" survives. The passages read as a description of the v0.09 companion.

**Recommended revision.** Say "the v0.09 companion paper" where the earlier design is meant, and point to the v0.10 paper's six families (profiles and boundaries; memory; self-modeling and inference integrity; continuation incentives and shutdown; world-coupling; institutional correction) as the current design. Recorded as issue #34 for the *Non-Egoic* audit.

### S3. Several symbols mean unrelated things [C] (§§2.9, 3)

**Evidence (Q9).** \(P\) is a profile coordinate (persistence, §3.2) and also probability, three times, including in §3.12, the section on persistence. \(G\) is the relational organization in \(C_{\mathrm{con}}(x;K,G,\pi,T)\) (§2.9), the profile coordinate for global availability (§3.2), and the causal graph \(G_t\) (§3.3). \(\mathcal R\) is the reflexive process \(\mathcal R_t\) (§3.7) and the reach sets \(\mathcal R_i\) (§3.8), on consecutive pages. \(E\) is the environment and \(E_t\) the edge set of \(G_t\). The profile coordinates \(M\) and \(C\) also sit beside the specialist set \(\mathcal M\) and the coherence object \(C_{\mathrm{con}}\), and \(A\) is both the admission relation in the system tuple and the admission map \(A_t\) of §3.4, which is harmless but adds to the load.

**Recommended revision.** Give the profile coordinates subscripted names (\(p_G, p_S, \ldots, p_R\)) or a distinct letter family. Write the causal graph as \(\Gamma_t = (N_t, \mathcal E_t)\), and the reach sets as \(\mathrm{Reach}_i\).

### S4. Citation practice [C] (References; issue #23)

**Evidence (Q10).**

- **Unused entries.** Fourteen of the 33 non-self entries are never cited by author and year: Bayne (2010, 2016), Blanke and Metzinger, Chalmers (1995, 2023), Cleeremans et al., the Cogitate Consortium, Damasio, Letheby and Gerrans, Metzinger, Nagel, Parfit, Shea and Frith, and Varela. Some are clearly being drawn on: §9.10 calls its lesson "Parfitian," §2.1 uses Nagel's phrase, §6.1 names neurophenomenology.
- **COGITATE.** The Cogitate study is described in three places (§§4.6, 6.4, 6.9) and never cited, although its entry is in the list.
- **The second-order companion paper.** Section 5.4 refers to "the second-order companion paper" without citation. That paper is the "Rader (2026f)" entry, the only Rader entry with a year suffix.
- **Gurnee et al.** The entry lacks arXiv:2607.15495 (issue #11).

**Recommended revision.** Cite the Cogitate study at each of its three appearances and the companion paper in §5.4, either cite or drop the other unused entries, regularize the Rader suffixes, and add the arXiv number to Gurnee et al.

### S5. Propagation residue [C] (throughout; issues #7, #9)

**Evidence (Q7).**

- **Lowercase "this paper."** The paper has 52 sentence- or cell-initial lowercase "this paper," and 59 lowercase instances in all. Two substitutions are ungrammatical: "That observation supports a central this paper distinction" (§7.8) and the table header "this paper assessment" (§7.10). Both probably replaced "v0.10" or "CU."
- **Lowercase definition head.** The defined term in §2.5 begins in lowercase ("**[Definition] responsible sovereignty**").
- **Stray paragraph.** A paragraph beginning "The paper concludes by distinguishing…" sits after the abstract's closing rule, outside the abstract, before "Relation to the series."
- **RC2 line.** The Domain Analytic Frame says "RC2 remains the frozen baseline" (#9).

**Recommended revision.** A global replacement of sentence-initial "this paper" with "This paper" fixes most cases. The two ungrammatical ones need hand edits ("a central v0.10 distinction"; "CU assessment"). Fold the stray paragraph into the abstract or move it to the end of §1.

### S6. The constructed contrast cases are not in the package [S] (§§3.14, 7.11; Appendix C; issue #29)

**Evidence.** Section 7.11 relies on "this paper's constructed `dual_disconnected_workspaces` architecture" as a limiting case, and §3.14 and Appendix C refer to formal counterexamples and deterministic contrast cases. None are in the RC3 package, and the code-style name in §7.11 reads as a pointer to a file the reader cannot see.

**Recommended revision.** Describe the dual-workspace contrast in one sentence of prose in §7.11 ("two workspaces with no causal path between them, feeding one output channel"), and resolve the supplement under issue #29.

### S7. "Thin perspective" has two definitions [I] (§§1.4, 4.5)

**Evidence.** Section 1.4 defines a thin perspective positively: "a candidate episode with selected access, a task-relative self-frame, and some degree of causal unity, but limited temporal depth…" Section 4.5, marked **[Definition]**, defines it only by what is sparse: "limited temporal depth, weak or absent endogenous self-maintenance, little established world-coupling, and unresolved or absent phenomenal valence." On the §4.5 definition, a system with no access organization at all would qualify.

**Recommended revision.** Make §4.5 the single controlling definition and include the positive features from §1.4, then have §1.4 refer to it.

---

## 5. Consider

**K1. The overlap statistic is undefined for empty reach sets (§3.8).** \(O_{ij}\) is a Jaccard index and is 0/0 when neither coalition reaches any specialist. Define it as 0 in that case, or restrict it to coalitions with nonempty reach.

**K2. Two quoted figures and one layer range need checking against the source's §4 [S] (§7.3).** The figures "approximately six [list items] … across the layer band, but only about one or two at a single workspace layer," and the upper end of "approximately L38–L92," come from the part of Gurnee et al. this audit did not reach. The source reindexes layers to 0–100, so write "layers 38–92 on the source's 0–100 normalized scale" once the bound is confirmed.

**K3. Hypothesis H1 omits one PIH clause [I] (§5.12).** H1 says global availability plus causal self-modeling increases the probability of thin perspective. PIH requires center individuation as well, and §4.2 says evidence for two clauses may not stand in for the third. Add "and center individuation," or note that H1 tests only two clauses.

**K4. Unrolling produces tied weights (§5.5).** A finite recurrent computation unrolls into a feedforward network whose layers share weights. "Untied" describes the more general feedforward class that contains it. Suggest "with weights tied across depth, a special case of feedforward depth."

**K5. Cross-references for CU-COM9 (Appendix A).** *Foundations* lists CU-T3, CU-T5, and CU-T8 as interpretations for CU-COM9, and CU-G1, CU-G6, and CU-G7 as related governance. The paper's commitment cross-reference names CU-T9, CU-T12, CU-T13, and CU-G6 (Q6). These are not wrong, since they cover COM14 and COM19 too, but adding the three interpretations *Foundations* names would make the anchor complete.

**K6. Abstract length.** At about 1,000 words in seven paragraphs, plus the stray paragraph of S5, the abstract is about twice the length of a typical one. The third through fifth paragraphs could each lose a sentence without losing a claim.

---

## 6. Relation to the issue log

- **#6 (status vocabulary).** M1 is the clearest instance so far: the status column is present but empty.
- **#7 (find-and-replace artifacts).** Counts confirmed with one pattern across the corpus: *Consciousness* 52 sentence- or cell-initial (59 lowercase in all, two ungrammatical), *Artificial Intelligence* 11, *Ethics* 1, all others 0 (Q7). The log's earlier estimates (about 20 and 1) were low.
- **#9 (RC2 baseline).** Confirmed.
- **#11 (Gurnee arXiv number).** Confirmed missing; the paper and arXiv versions match on every figure checked.
- **#16 (two-stage Or failure).** Not repeated here; §10.4 restates the taxonomy correctly.
- **#19 (dependency tables).** None in *Consciousness*.
- **#23 (citation practice).** Fourteen unused entries; the Cogitate study discussed but never cited (S4).
- **#29 (supplements).** Extended: the §3.14 counterexamples and the `dual_disconnected_workspaces` construction (M2, S6).
- **#32 (box drift).** Not applicable; *Consciousness* has no principle boxes in its sections, and its Appendix A statements are verbatim.
- **New #33.** CU-V7 and CU-E-17 are superseded aliases of CU-G6 in *Foundations*, but *Consciousness* lists CU-V7 as live and *Ethics* has CU-E-17 as a section heading twice (S1).
- **New #34.** *Consciousness* §10 describes the v0.09 *Non-Egoic* companion (four boundaries, one architectural switch, a non-degradation clause) rather than the v0.10 paper's six architecture families (S2). Check from the *Non-Egoic* side at Audit 11.

---

## 7. Standing caution

Every finding here concerns internal coherence, formal correctness, or sourcing. The paper's empirical claims about language models are reported accurately from their sources, and its inferences from them are hedged at about the strength the sources support. That is a statement about the paper's fidelity to its evidence, not about the evidence's bearing on experience. As the paper itself says, there is "no independent oracle for phenomenal consciousness in novel systems," and both the workspace and introspection studies come from one institution and one method family.

Passing this audit does not move the question the paper is about.
