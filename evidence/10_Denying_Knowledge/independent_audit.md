# CU v0.10 Audit 10: Denying Knowledge to Make Room for Commitment

**Reviewer:** Claude (Opus 5.5)
**Date:** 6 October 2026
**Text audited:** `10_Denying_Knowledge_v0.10_RC3_Methodological_Spine_Propagation_Draft.md` (12,135 words), from the RC3 Methodological Spine Propagation Working Package (SHA-256 `23409d05…1c3a`, verified)
**Comparison texts:** *Metaphysics and Epistemology* (01) and Audit 01; *Foundations* (02)
**Reproducibility:** `cu_dk_audit_checks.py`. Every [C] finding cites its check number (D1–D6).
**Status:** Advisory. This audit assesses internal coherence, formal correctness, and sourcing. It is not evidence that the account is true of religious or practical life (see §8).

---

## 0. Conventions

The audit uses the seven-check protocol and the labels of Audit 01. **[S]** marks a finding that is source-supported. **[C]** marks a finding computed or checked by the reviewer and reproduced by the script. **[I]** marks reviewer inference.

The paper twice refers to a "technical supplement" holding its proof history, countermodels, regression results, and independent audit. That supplement is not in the RC3 package, so the audit could not consult it. Where the paper reports regression figures, the audit reconstructed them independently (D1).

---

## 1. Summary

*Denying Knowledge* is the most carefully scoped paper in the corpus so far. Its claims are modest and stated at the strength they have earned. Its formal appendix is correct, and its reported regression figures reproduce exactly from an independent reconstruction. It is also the paper against which M&E's epistemology sections should be measured: M&E Appendix D.3 names it the "controlling source" for the commitment-logic clarification, and on the points where the two papers differ, *Denying Knowledge* is usually the better formulation.

One problem needs fixing before release, and it is the one the handoff anticipated.

**Section 3.3 attaches System P to the wrong relation [C].** It defines strong warrant with a nonemptiness clause, introduces Γ |∼_C φ as "the corresponding" relation without defining it, and then claims System P. Exhaustive checking on the paper's own finite model shows that the strong-warrant relation fails Reflexivity in all 513 cases where the premises are infeasible, and satisfies every other System P rule. The relation without the clause, which Appendix A.1 defines correctly, satisfies all of them. The paper is right in A.1 and ambiguous in §3.3 and the abstract (M1).

Eight should-fix items follow. The most substantive is that the two-widows case places theological claims the paper calls "descriptions" inside the commitment language without saying how their descriptive component is handled (S1). The others concern a countermodel the paper relies on but does not present, a garbled sentence shared with M&E, citation gaps (KLM is never cited at the point of use), the missing supplement, and notation.

**Totals:** 1 must fix, 8 should fix, 5 to consider.

---

## 2. Verified correct

| Item | Check | Result | Label |
|---|---|---|---|
| §3.4 regression: 294 merely admissible verdicts, all with non-singleton best sets | Reconstructed: 3 worlds, 19 strict partial orders, all V, G, φ (9,728 cases) | Exact match | [C] D1 |
| §3.7 regression: 4,104 empty-best cases, all infeasible | Same reconstruction (27 disjoint (V, G) pairs × 19 orders × 8 conclusions) | Exact match | [C] D1 |
| A.1 System P for the plain fixed-base relation | Reflexivity, RW, And, Or, CM, Cut, all cases | No failures | [C] D2 |
| §3.4 admissibility fails And | The paper's two-world construction | Confirmed | [C] D3 |
| §3.5, A.3 classical-negation duality | Exclusion ⟺ strong warrant for ¬φ | Confirmed (Audit 01, E3) | [C] |
| A.4 maximum preservation | Equality only, and equivalent to admissibility | Correct; confirmed (Audit 01, E4) | [C] |
| A.5 cross-reference | Points to the §3.4 construction, which exists | Correct | [S] |
| A.2 verdict definitions | Five verdicts, with underdetermination given a formal core (non-attainment) | Correct, and clearer than M&E §8.2 | [S] |
| Register definitions (§1.3, §2.1–2.3) | Use- and force-based throughout | Consistent with M&E §6.2; the target for M&E S9 | [S] |
| §3.9 practical expansion warrant | Twelve conditions vs M&E §8.6 | Match in substance | [S] |
| §13.1–13.3 commitment titles | CU-COM1–COM3 vs *Foundations* | Match | [S] |
| Identifiers | All 15 cited identifiers | All resolve in *Foundations* | [C] D6 |
| §12.1 Kant citation | "Bxxx" for the "deny knowledge to make room for faith" passage | Correct | [I] |
| Reference list | Bibliographic details of all 26 entries, including DOIs | Consistent with standard records (reviewer knowledge; all pre-2026) | [I] |
| KLM (1990) and Lehmann–Magidor (1992) entries | Bibliographic details | Correct (carried forward from the earlier session) | [S] |

---

## 3. Must fix

### M1. System P is attached to the strong-warrant relation in §3.3 and the abstract [C][S]

Section 3.3 defines strong warrant as

  F, Γ ⊨^∀_C φ  ⟺  B(F, Γ) ≠ ∅ and B(F, Γ) ⊆ ⟦φ⟧_R,

then says: "The corresponding metalinguistic consequence relation may be written Γ |∼_C φ." It gives that relation no definition of its own, and continues: "Under the standard definability and smoothness assumptions, fixed-base preferential consequence satisfies the KLM System P rules." Read in sequence, the passage presents |∼_C as notation for strong warrant and claims System P for it. The abstract does the same in summary.

That claim is false for the relation as defined. When V_F ∩ Real_R(Γ) is empty, B is empty, so strong warrant holds for nothing, not even for a member of Γ. Reflexivity therefore fails at every infeasible premise set. Check D2 confirms this exhaustively over the paper's own finite model. The strong-warrant relation fails Reflexivity in exactly 513 cases, which are exactly the 19 × 27 infeasible combinations, and satisfies Right Weakening, And, Or, Cautious Monotony, and Cut everywhere. The plain relation of Appendix A.1, which omits the nonemptiness clause, fails nothing.

The paper is therefore internally inconsistent rather than wrong throughout. Appendix A.1 and §5.4 define |∼_C correctly; §3.3 and the abstract blur it with strong warrant.

**Recommended revision.** Follow M&E §7.4, which handles this correctly. In §3.3, define the two relations separately: the plain relation Γ |∼_C φ ⟺ Min(V_F ∩ Real_R(Γ)) ⊆ ⟦φ⟧_R, which carries System P, and strong warrant as that relation plus feasibility. Add one sentence: "Strong warrant is the practical verdict; it coincides with |∼_C on feasible premises and fails Reflexivity on infeasible ones, which is why infeasibility is reported as a separate verdict." In the abstract, attach System P to "the fixed-base consequence relation" rather than to the verdict. The same sentence would serve as Audit 01's recommendation K1 for M&E.

---

## 4. Should fix

### S1. The two-widows case does not say how its shared beliefs are registered [S][I] (§9.2)

Section 9.2 puts four items into the shared commitment set Γ: "the dead are with God; death is not the end; grief is not despair; trust is an appropriate response to what cannot be understood." The next sentence calls them "theological descriptions" whose truth the paper does not decide. But Γ is a subset of L_R, the commitment language, and the paper's own register discipline (§2.4, §4.4) requires mixed content to be decomposed. Two of the four items are plainly descriptive in form.

The case is the paper's showcase, and a careful critic will ask whether it quietly converts descriptions into commitments to keep them out of F. The paper's answer is presumably that the widows hold these as commitment contents (trust that the dead are with God), while the descriptive claims are left outside F, neither established nor excluded. That answer should be stated.

**Recommended revision.** Add two sentences to §9.2: the items enter Γ as commitment contents; their descriptive counterparts are not in F, because the model treats them as undecided; and the verdicts on φ_s and φ_g therefore hold whatever their truth.

### S2. A countermodel is cited but not shown [S] (§5.3)

Section 5.3 says that "a countermodel shows that premise-responsive viability revision can violate Cautious Monotony; the paired control shows that the same worlds and ordering do not violate it when premises filter one fixed base." Neither the countermodel nor the control appears in the paper. M&E Appendix B.13 contains the countermodel, and it is correct (Audit 01, E5).

There is a related cross-paper finding. M&E B.13 ends by citing "Theorem A.1," which does not exist in M&E (Audit 01, M3). In *Denying Knowledge*, A.1 *is* the System P statement. M&E's dangling reference is almost certainly residue from this paper's appendix numbering [I].

**Recommended revision.** Either reproduce the B.13 countermodel and its control in an appendix here, or cite M&E B.13 explicitly. M&E's reference should then read "the System P result of M&E A.3," or, if B.13 moves here, "*Denying Knowledge* A.1."

### S3. A garbled sentence shared with M&E [S][C] (§2.3)

Section 2.3 ends: "A commitment act can therefore be unwarranted even where the descriptive truth of its content does not settle whether it should be adopted." The identical sentence appears in M&E §6.4 (Audit 01, S7) [C, D5]. The intended point is presumably: "A commitment act can be unwarranted even when its content is true, because descriptive truth does not settle whether it should be adopted." Fix both papers together.

### S4. The formal import is never cited at the point of use [C][S] (body and References)

The paper names "KLM" thirteen times and "System P" eleven times, but Kraus, Lehmann, and Magidor (1990) and Lehmann and Magidor (1992) are never cited by author and date [C, D4]. These are the paper's most load-bearing imported results. Three smaller gaps:

- **Ayer (1936)** is in the reference list but never mentioned.
- **Schroeder** is cited once as "(Schroeder, 2008)," while the list has two 2008 entries, 2008a and 2008b. The citation should say which; given the context in §12.6, probably 2008b.
- **Mitchell** is named in "the Flew–Hare–Mitchell symposium" (§1.2) but has no entry. His contribution appears in the same 1955 volume.

This pattern is milder than in M&E, where no in-text citations exist at all (issue log #23), but it has the same root. **Recommended revision:** cite KLM (1990) at §3.3 and A.1, Lehmann–Magidor (1992) at the Rational Monotony sentence, and resolve the other three.

### S5. The technical supplement is referenced but not supplied [S]

The Note on Version 0.10 and Appendix B both say that the complete proof history, countermodels, regression results, independent audit, and disposition record appear in a "technical supplement." The RC3 package does not contain it. The two regression figures reproduce exactly (D1), so the omission does not undermine the paper's claims. But a reader cannot verify the disposition record, and CU-M6 (reproducibility and provenance) calls for the supplement to travel with the paper. **Recommended revision:** include the supplement in the release package, or replace the references with a stable location.

### S6. The paper's prediction about resistance is unlabelled [S][I] (§11.4)

Section 11.4 ends: "Win the argument while leaving no exit and the framework predicts resistance." This is an empirical claim about how people respond to belief-threatening argument. It is plausible and has a literature behind it (identity-protective cognition, for example), but the paper offers neither a citation nor a claim-status label. A paper whose subject is keeping commitment from impersonating knowledge should not let a framework "predict" without saying on what evidence.

**Recommended revision.** Label the sentence as a hypothesis, or cite the relevant empirical work.

### S7. Notation diverges from M&E [C] (throughout)

*Denying Knowledge* writes the premise extension as Real_R(Γ) (seven uses) where M&E writes Mod_R(Γ); neither paper uses the other's symbol [C, D5]. Both use ∼ for the consequence relation where the literature uses |∼ (Audit 01, K4). Since *Denying Knowledge* is the controlling source, M&E should adopt Real_R, or both should adopt one symbol by agreement.

### S8. Two propagation artifacts [C][S] (§3.2, §13.4)

Section 13.4 has a sentence beginning with a lowercase "the Version 0.10 canonical registry" [C, D5], the same family of artifact as M&E's "Version Version 0.10." And §3.2, the formal definition of evaluation models, ends with a paragraph about the Domain Analytic Frame that belongs with the card, not in the formal section. Move it to the card or to §3.9.

---

## 5. Consider

**K1. Sharpen the fourth claim of §1.4.** It says the consequence relation "distinguishes what every best viable realization supports from what at least one supports." The consequence relation does only the first; the verdict taxonomy does the second.

**K2. Let *Denying Knowledge* control the shared lists, and have M&E point to it.** Several parallel lists differ slightly between the two papers. The bounded-trough conditions number eight here and seven in M&E §8.8 (M&E omits "evidence-sensitive expectations"). The disagreement taxonomies number nine here and eight in M&E §8.10, with different members. The underdetermination causes differ. None of the differences is a contradiction, but once M&E summarizes and points here (Audit 01, §6), the duplication and the drift disappear together.

**K3. Adopt A.2's underdetermination wording in M&E.** Appendix A.2 here gives underdetermination a formal core ("W ≠ ∅ but … non-attainment or model inadequacy"). That is exactly what Audit 01 K2 recommended for M&E §8.2.

**K4. Make the citation years consistent.** The body cites "(Hume, 1748/1777)" and "(Kant, 1781/1787)" against reference entries dated 2000 and 1998. The usual form is "(Hume, 1748/2000)."

**K5. Add a sentence to §3.8 about where the history lives.** The section narrates the earlier maximum-preservation error in the body. Since Appendix B exists to hold revision history, §3.8 could state the corrected result and point there.

---

## 6. Relation to *Metaphysics and Epistemology* [C][I]

Audit 01 recommended that M&E's §§6–8 summarize and point to this paper rather than restate it. This audit supports that recommendation for three reasons.

First, this paper is the better text on every point where the two differ. Its register definitions are consistently use-based where M&E's §1.6 and glossary are not (issue #22). Its A.2 gives underdetermination a formal core that M&E lacks. Its A.5 cross-reference resolves where M&E's B.4 does not.

Second, the one formal defect here (M1) is fixed by importing a single sentence from M&E. The two papers repair each other, and after repair, one controlling statement is enough.

Third, the papers' distinctive contents barely overlap. Material unique to *Denying Knowledge*—the two widows, deferred inquiry, the political case, and the placement in the philosophical literature—is about 3,500 words, a little over a third of the numbered sections [C]. Material unique to M&E—the dynamic and probabilistic extensions and the two-stage architecture—does not appear here at all.

---

## 7. Carry-forward items for the issue log

- **#16 (two-stage obstruction):** not applicable; *Denying Knowledge* does not discuss the two-stage architecture.
- **#22 (register definitions):** this paper is consistently use-based and should be the model for fixing M&E.
- **#23 (citation practice):** extended; here the KLM papers are uncited at the point of use, Ayer is uncited, and the Schroeder citation is ambiguous.
- **New #26 — Strong warrant and System P.** *Denying Knowledge* §3.3 and abstract attach System P to the strong-warrant relation; it fails Reflexivity on infeasible premises (513 of 513 cases). M&E §7.4 is correct but should add the clarifying sentence. **Status:** proposed fix.
- **New #27 — Shared garbled sentence.** *Denying Knowledge* §2.3 and M&E §6.4.
- **New #28 — M&E B.13 "Theorem A.1" is residue of *Denying Knowledge*'s numbering.** Refines Audit 01 M3. The countermodel cited in *Denying Knowledge* §5.3 lives only in M&E B.13.
- **New #29 — Technical supplements referenced but not packaged.** *Denying Knowledge* Note and Appendix B. Check whether other papers refer to supplements that are not in the package.
- **New #30 — Notation for premise extensions.** Real_R in *Denying Knowledge*, Mod_R in M&E.

---

## 8. Standing caution

Every finding here concerns internal coherence, formal correctness, or sourcing. The formal results that pass are imported mathematics correctly applied to declared models, and the regression figures that reproduce show only that the paper's implementation counts what it says it counts. The paper itself says that those frequencies "are not evidence that one practical verdict is common in lived commitment," and this audit agrees.

Whether the two-register account describes how commitment actually works in religious and political life, and whether its verdicts track anything that matters to the people it describes, are questions for philosophical argument and empirical study. Passing this audit does not bear on them.
