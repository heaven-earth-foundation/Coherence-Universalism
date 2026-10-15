# CU v0.10 Audit 08: Ethics

**Reviewer:** Claude (Opus 5.5)
**Date:** 7 October 2026
**Text audited:** `08_CU_Ethics_v0.10_RC3_Methodological_Spine_Propagation_Draft.md` (19,598 words), from the RC3 Methodological Spine Propagation Working Package (SHA-256 `23409d05…1c3a`, verified)
**Comparison texts:** *Foundations* (02), especially the Ethics registry (CU-E-1–E-18), CU-G6, CU-COM12, CU-COM14, CU-COM17, CU-COM19, and the 64-stage table; *Psychology* (06) for the definition of self-deception; the corpus issue log
**Reproducibility:** `cu_et_audit_checks.py`. Every [C] finding cites its check number (T1–T9).
**Status:** Advisory. This audit assesses internal coherence, formal correctness, and sourcing. It does not evaluate whether CU's normative positions are correct (see §7).

---

## 0. Conventions and coverage

The audit uses the seven-check protocol and the labels of the earlier audits. **[S]** marks a finding that is source-supported, **[C]** one computed or checked by the reviewer and reproduced by the script, and **[I]** reviewer inference.

**Coverage.** Sections 1–5, 14–16, and the appendices were read in full. Sections 6–13 were read for their claims, definitions, formulas, and citations, with bulleted lists skimmed. Whole-paper scans covered identifiers, principle and commitment texts against *Foundations*, the two lists of twenty governance rules, citations, notation, and propagation artifacts.

**Sources.** One recent empirical source was checked by search, Lewis et al. (2025) on institutional betrayal in inpatient psychiatry. The paper's other recent sources (Ditto et al., 2025; Silver & Berman, 2024; the 2025 moral-injury reviews) are cited for general points and were checked for bibliographic form only.

**Issues carried from the log.** The handoff asked this audit to check issue #5 (CU-COM14 and CU-COM17 titles), issue #33 (CU-E-17 as a superseded alias), issue #37 (stray "Appendix B" pointers), and issue #32 (principle drift). All four are addressed below.

---

## 1. Summary

*Ethics* is a careful and well-structured paper with no must-fix items. Its central move, treating justificatory integrity as necessary but not sufficient, is argued cleanly; the §4.4 example of the candid tyrant makes the point in three sentences. The distinction between presented and feasible options (\(U^{\mathrm{pres}} \subseteq U^{\mathrm{feas}}\)) is the paper's most original contribution, and it is carried consistently from §2.1 through the twenty governance rules to §9.1. Claim discipline is good: §14.3 says plainly that all eighteen CU-E principles "remain provisional," which matches *Foundations* exactly.

Cross-paper agreement is mostly exact. All 30 identifiers resolve. Sixteen of the eighteen CU-E statements match *Foundations* verbatim in both §14.3 and Appendix A; the other two match in Appendix A (T4). Stages 27–31 and the five later stages named in §1.2 match the *Foundations* table (T7). The two lists of twenty governance rules are identical (T8). Issue #37 does not recur here.

The should-fix items are mostly carried corpus issues, now confirmed with exact locations.

- **Issue #5 is a heading problem [C].** The section headings for CU-COM14 and CU-COM17 use informal titles ("Love as ethical relation"; "Redemption without justification of evil"); the bodies use the correct ones (T6). This is a two-line fix.
- **Issue #33 is confirmed [C].** CU-E-17 is a superseded alias of CU-G6 in *Foundations*, but *Ethics* presents it twice as a live principle and never mentions CU-G6 (T5).
- **Principle and commitment text drifts in three places [C].** The §14.3 boxes for CU-E-15 and CU-E-16 differ from the registry, and three of the four CU-COM12 fields differ from *Foundations* (T4, T6).
- **The self-deception definition is attributed to the wrong text [C].** Section 3.1 quotes "the Psychology paper's definition," but the quoted wording is the *Foundations* registry's, not *Psychology*'s (T7). This is a direct consequence of Audit 06 M1.

**Totals:** 0 must fix, 8 should fix, 3 to consider.

---

## 2. Verified correct

| Item | Check | Result | Label |
|---|---|---|---|
| Identifiers cited | T4 | 30 distinct; all resolve | [C] |
| CU-E-1–E-18 titles | T4 | All match *Foundations* | [C] |
| CU-E statements in Appendix A | T4 | 18 of 18 verbatim with the registry | [C] |
| CU-E statements in §14.3 | T4 | 16 of 18 verbatim (see S1) | [C] |
| CU-E statuses | T4 | All provisional in *Foundations*; §14.3 says "All remain provisional" | [C] |
| Stages 27–31 and stages 56, 57, 62, 63, 64 (§1.2) | T7 | All ten titles match *Foundations* | [C] |
| Twenty governance rules, §2.8 and Appendix A.2 | T8 | Identical | [C] |
| CU-COM12 commitment statement (§15.10) | T6 | Identical to *Foundations* | [C] |
| Aggregate-versus-floor point (§8.3) and weighted reversal (§2.6) | T1 | Both reconstruct | [C] |
| No stray "Appendix B" construction pointer (issue #37) | T8 | None | [C] |
| Lewis et al. (2025), *Psychiatric Services* (§11.5) | search | Exists (N = 814 former inpatients); institutional betrayal associated with lower trust and engagement, as described; see K1 on the first author's initial | [S] |

---

## 3. Must fix

None.

---

## 4. Should fix

### S1. Principle and commitment text drifts in three places [C] (§§14.3, 15.10; issue #32)

**Evidence (T4, T6).**

- **CU-E-15.** The §14.3 box adds "into Foundations" and replaces "unresolved conflict preserves provisional status and public dissent" with "unresolved disagreement among required constituencies keeps the principle provisional, with dissent and dispositions preserved in the public record." Appendix A has the *Foundations* wording.
- **CU-E-16.** The box replaces "declare a context-appropriate reversibility, containment, rollback, staged-exposure, or retained-option floor" with "protect reversibility, containment, rollback, staged exposure, or equivalent option value through a declared floor," and adds that an exception must address "safer alternatives and the harms of delay." Appendix A has the *Foundations* wording.
- **CU-COM12.** The commitment statement matches *Foundations*, but the practical expression, boundary conditions, and revision conditions are all different texts. The *Foundations* boundary condition, for example, reads "Candor does not make domination permissible. Introspection alone does not reveal institutional truth"; *Ethics* says CU-COM12 "does not license mind reading, compulsory confession, diagnosis of opponents…"

In each case the *Ethics* version is arguably the better one; the CU-E-16 box, for instance, carries the substance of the §2.4.2 reversibility rule. But a reader comparing the paper with the registry will find two texts for the same identifier.

**Recommended revision.** Decide which wording controls and make the other verbatim, as recommended under issue #32. If the *Ethics* versions are preferred, update *Foundations* and Appendix A to match them.

### S2. CU-E-17 is a superseded alias presented as live [C] (§14.3; Appendix A; issue #33)

**Evidence (T5).** *Foundations* lists CU-E-17 with authority class "superseded alias" and the disposition "controlling identifier is CU-G6." *Ethics* gives CU-E-17 a full entry in both §14.3 and Appendix A, labels it "[Normative principle]," and never mentions CU-G6. *Consciousness* does the same with CU-V7 (Audit 05 S1).

**Recommended revision.** Keep the entry, add "Superseded alias; controlled by CU-G6," and cite CU-G6 in §7.9 where the distinction is argued.

### S3. Two commitment headings use informal titles [C] (§§15.7, 15.8; issue #5)

**Evidence (T6).** The heading of §15.7 is "CU-COM14 — Love as ethical relation"; the *Foundations* title is "Love as the Ground and Aim of Conscious Life." The heading of §15.8 is "CU-COM17 — Redemption without justification of evil"; the *Foundations* title is "Redemptive Possibility Without Justification of Evil." The body of §15.7 gives the correct COM14 title. Issue #5 recorded these as differences "in substance" and "in wording"; in fact both are headings that pair an identifier with a paraphrase. "Enact Omega here" (§15.9) differs from the registry only in capitalization.

**Recommended revision.** Write the registry titles in the headings, for example "15.7 Love as ethical relation (CU-COM14 — Love as the Ground and Aim of Conscious Life)," or drop the identifiers from the headings and cite them in the text. Issue #5 can then be closed.

### S4. The self-deception definition is attributed to Psychology but quoted from Foundations [C] (§3.1)

**Evidence (T7).** Section 3.1 says "the account inherits the Psychology paper's definition" and quotes "Self-deception is motivated asymmetric information processing in which an identity, attachment, advantage, policy, or other stake is protected by selectively excluding, reframing, discounting, or neutralizing relevant reasons." That is the *Foundations* CU-Ψ11 text. *Psychology*'s own CU-Ψ11 reads "Self-deception is a pattern of motivated, asymmetric information processing in which a person protects an identity, attachment, advantage, policy, or other stake…" The two are close, but the attribution is wrong, and the mismatch exists only because the two Ψ11 texts disagree (Audit 06 M1).

**Recommended revision.** Resolve Audit 06 M1 first; then quote the controlling text and cite CU-Ψ11 by identifier.

### S5. Two floor formulas are written loosely [C] (§§2.4, 8.3)

**Evidence (T1, T2).** Section 2.4 introduces "\(k_j\), a protected floor for dimension \(j\)," and the formula that follows uses \(k_{aj}\), a floor for being \(a\) on dimension \(j\). Section 8.3 writes the floor violation as \(\min_a y_a(u) < k_a\), where \(a\) is bound by the minimum and also indexes the floor; the expression is not well formed when floors differ across parties. The intended claims are correct and reconstruct (T1).

**Recommended revision.** In §2.4, introduce \(k_{aj}\) directly. In §8.3, write "\(y_a(u) < k_a\) for some \(a\), while \(y_a(v) \ge k_a\) for all \(a\)."

### S6. One symbol names two objects [C] (§§2.3, 10.2, 12.2)

**Evidence (T3).** \(R_a\) is a coordinate of the ethical profile ("alignment of responsibility," §2.3) and \(\mathbf R_a(o)\) is the responsibility profile of actor \(a\) (§10.2). The tuple's \(A\) (affected beings) and \(R\) (distributions) also sit beside the profile coordinates \(A_g\), \(R_a\), and \(R_p\), and the repair profile \(\mathbf P_R\) reuses \(Tr\), the trust coordinate of *Social Dynamics*.

**Recommended revision.** Rename the §2.3 coordinate (for example \(\mathit{RA}\)) or the §10.2 profile (for example \(\boldsymbol\rho_a(o)\)).

### S7. Propagation residue [C] (throughout; issues #7, #9)

**Evidence (T8).** Twelve sentences begin with a lowercase stand-in for "This paper": "the account" eight times (lines 459, 558, 1074, 1214, 1683, 1701, 1750, 2042), "this account" twice, "the analysis" once, and "this paper" once (line 1976). The pattern suggests a later pass replaced "This paper" with alternatives without restoring capitals. The Domain Analytic Frame says "RC2 remains the frozen baseline" (#9). Section 14.3 also proposes the principles "for later Foundations consolidation," although *Foundations* already registers them.

**Recommended revision.** Capitalize the twelve sentences. Change "for later Foundations consolidation" to "as registered in *Foundations*."

### S8. Citation practice [C] (References; issue #23)

**Evidence (T9).** Twenty-eight of the 61 non-self entries are never cited by author and year. They include the canonical sources for positions §1.5 summarizes (Kant, Rawls 1971 and 1993, Scanlon, Gilligan, Held, Tronto, Habermas, Forst, Sen); the epistemic-injustice literature the paper's testimony arguments rely on (Fricker, Medina); the restorative-justice sources behind §12 (Zehr, Walker, Herman); and, most notably, Litz et al. (2009) and Shay (1994), the founding works on moral injury, which §11 discusses at length without citing. Three United Nations documents are listed but not cited.

**Recommended revision.** Cite the drawn-on works where they are used, especially Litz et al. and Shay in §11.1, and the philosophers in §1.5; drop the rest.

---

## 5. Consider

**K1. The Lewis entry's first initial [S].** The reference gives "Lewis, A." The article and the senior author's CV list the first author as D. Lewis. Confirm against the article.

**K2. The effective-agency "equation" (§7.7).** The paper writes effective agency as a sum of formal permission, information, material means, social support, and practical safety, and then says "the equation is schematic, not additive measurement." A conjunction or a tuple would say what is meant without needing the disclaimer.

**K3. The Mandala bridge (§1.2).** The claim that ethical relations are "constitutive features of higher-order coexistence" is labeled a systems-metaphysical and normative bridge, which is right. One sentence noting that it presupposes the interpretive reading of the Mandala in M&E §13 (rather than a descriptive result) would close the loop for readers who start with this paper.

---

## 6. Relation to the issue log

- **#5 (COM14, COM17 titles).** Located precisely: the §15.7 and §15.8 headings (S3). Proposed fix; close after the edit.
- **#6 (status vocabulary).** *Ethics* uses one schema consistently ("[Normative principle]" and similar) and states that all are provisional. No new problem.
- **#7 (artifacts).** Twelve sentence-initial lowercase stand-ins for "This paper" (S7). The corpus pattern search counted only "this paper" (one); the other eleven use substitutes. Extend the corpus search accordingly.
- **#9 (RC2 baseline).** Confirmed.
- **#19 (dependency tables).** None in *Ethics*.
- **#23 (citation practice).** Twenty-eight unused entries (S8).
- **#32 (principle drift).** Extended: CU-E-15 and CU-E-16 boxes, and three CU-COM12 fields (S1).
- **#33 (CU-E-17 alias).** Confirmed: two live entries, no CU-G6 reference (S2).
- **#37 (Appendix B pointers).** Not present in *Ethics*.
- **Audit 06 M1.** Has a downstream effect here (S4).

---

## 7. Standing caution

Every finding here concerns internal coherence, formal correctness, or sourcing. The paper is explicitly normative; whether its constraint architecture is the right one is a question for moral and political philosophy, and the paper itself keeps all eighteen of its principles provisional pending that review.

Passing this audit does not show that CU's ethics is correct.
