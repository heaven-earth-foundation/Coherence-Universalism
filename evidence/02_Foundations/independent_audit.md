# Audit 02 — *Coherence Universalism: Foundations* (v0.10 RC3 Propagation Draft)

**Reviewer:** Claude (Opus 5.5)
**Date:** 26 September 2026
**Document:** `02_CU_Foundations_v0_10_RC3_Methodological_Spine_Propagation_Draft.md` (4,243 lines; about 29,700 words; 214 principle entries)

**Audit protocol.** The seven checks agreed for the series:

1. formal correctness;
2. claim-status discipline;
3. internal consistency;
4. cross-paper consistency;
5. sources;
6. revision residue;
7. editorial.

**Labels.** Each finding is labelled **[S]** source-supported, **[C]** computed or checked by the reviewer, or **[I]** reviewer inference.

**Severity.**

- **Must fix:** an error or contradiction a careful reviewer would catch.
- **Should fix:** a real inconsistency or gap.
- **Consider:** an improvement.

---

## Summary

Foundations is in good shape. It is the most internally consistent paper checked so far.

- **Formal content.** Its formal statements are correct. It states the System P scope *correctly*, which makes it the reference point for fixing *Denying Knowledge*.
- **Identifiers.** Its identifier registry is clean. Every one of 90 principle identifiers that other papers restate carries a matching title, with two exceptions.
- **The Mandala.** The 64 stage titles are identical across Foundations, M&E §13.14, and the v0.19 Ladder status map.

The problems cluster in three places:

1. **Stale bookkeeping from the RC3 propagation.** Appendix A undercounts CU-M. Appendix F omits CU-M11–M14. A registry, PHYS-A6, points to a section of *Physics* that no longer exists.
2. **One interpretive principle, CU-T11, keeps alive a phrase the rest of the corpus retires.** The phrase is "universal coherence gradient."
3. **The status system is uncontrolled.** Three different status schemas are in use, with about 30 authority-class labels against the 11 the document defines, and 57 distinct status labels for 64 Mandala stages. This is the same free-text-label problem the Ladder second pass found (325 labels for 395 objects), recurring in the constitution itself.

There are 5 must-fix items, 9 should-fix items, and 6 to consider.

---

## Verified correct

These checks passed. They are recorded so they need not be repeated.

| Check | Result |
|---|---|
| CU-FP6 block-averaging identities (differentiation loss = within-block residual; entropy gain = Σ q_b · KL(r⁽ᵇ⁾ ‖ u)) | Numerically verified with unequal block sizes, error ≤ 1e-15 [C] |
| CU-L4 / CU-L6 System P scope | Correct: \|∼ is defined without the nonemptiness clause and carries System P; strong warrant adds B ≠ ∅ [C] |
| "Fixed-coefficient gradient flow cannot produce a recurrent cycle" (Double Helix disposition) | Correct: gradient flows admit a Lyapunov function, which rules out nonconstant periodic orbits [C] |
| KLM (1990) and Lehmann–Magidor (1992) bibliographic details | Correct [C] |
| Identifier uniqueness | No duplicate principle headings among 214 entries [C] |
| Family counts in Appendix A: CU-FP 14, CU-L 10, CU-Ep 7, CU-D 10, CU-G 7, PHYS-A6 12, CU-T 13, CU-COM 19 | Correct (CU-M is wrong; see M1) [C] |
| Superseded-alias table (7 rows) | Consistent with the entries it points to [C] |
| Cross-paper principle titles | 90 identifiers restated in other papers; 88 match exactly (exceptions in S6) [C] |
| 64 Mandala stage titles | Identical in Foundations Part X, M&E §13.14, and the v0.19 Ladder status map [C] |
| Retired-claim list (Appendix D) | Consistent with the retirements elsewhere in the corpus [S] |

---

## Must fix

### M1. Appendix A undercounts CU-M, and Appendix F predates the Methodological Spine [C]

Appendix A lists **CU-M: 10**. The document defines **CU-M1–CU-M14**, since the RC3 propagation added CU-M11 (CAP), M12 (Shared Analytic Frame), M13 (local–global), and M14 (allocation license). Appendix F, the Synchronization Checklist, likewise names CU-FP8a–e and CU-G1–G7 but none of CU-M11–M14. Under the current checklist, a paper could be declared "synchronized" without an Analytic Frame card or a local–global declaration.

*Fix:* change the count to 14. Add checklist lines for the Analytic Frame card (CU-M12), the local–global declaration (CU-M13), and the Allocation License Test (CU-M14). If CU-M15 is adopted, add it as well.

### M2. "Physics A.6" and the PHYS-A6 registry do not resolve in *Physics* [C]

Foundations cites "Physics A.6" twice: in the Part IV introduction (line 1393) and in the Former Third Law disposition (line 1698). *Physics* v0.10 has only Appendices A–C (Notation, Revisions, Supplement) and no A.6. The twelve PHYS-A6.x identifiers appear in Foundations (12) and M&E (9) but **never in *Physics* itself**. The registry that "every downstream paper must respect" therefore has no anchor in its owning paper.

*Fix, either:* (a) add a short "Physics constraint registry" table to *Physics* carrying the PHYS-A6.1–A6.12 identifiers and pointing to the sections that establish each; or (b) rename the family to cite *Physics* section numbers directly. Replace "Physics A.6" with the actual section references.

### M3. CU-T11 relicenses the phrase "universal coherence gradient" [S]

CU-T11 (Minimum Teleology), under *Register status*, says: "'Universal coherence gradient' is interpretive shorthand for recurrent directionality." Elsewhere the corpus retires this phrase explicitly:

- *Physics* §13.9 lists "a universal coherence gradient in nature" among the things the account does **not** license.
- CU-FP2's failure modes include "rebuilding a universal coherence scalar from purpose-bound instruments."
- *Biology* states that "no framework-level ∇C governs all living systems."

Keeping the phrase alive as sanctioned shorthand invites exactly the slide the corpus guards against. A reader, or a hostile reviewer, can quote the canonical interpretive principle using the retired phrase.

*Fix:* delete the sentence. "Grain of reality," the principle's own term, already does the work without the gradient connotation.

### M4. The authority hierarchy omits the companion papers, which restate controlling formal content [S][C]

§10.3 ranks "framework definitions, method, and formal scope in M&E/This document" second. It does not place *Denying Knowledge* or *Non-Egoic Artificial Mind*, although §10.7 names both as active companions. *Denying Knowledge* restates CU-L4/L6 and, as found earlier, conflates strong warrant with the System P relation (§3.3), where Foundations and M&E state them correctly. When they conflict, the hierarchy does not say which controls.

*Fix:* add the companions to §10.3, below Foundations and M&E for any content that restates a registered principle. Separately, correct *Denying Knowledge* §3.3 to match CU-L4/L6. The label also contains a find-and-replace artifact, "M&E/This document"; it should read "M&E and Foundations."

### M5. Orphaned patch text in Part VI [S]

After PHYS-A6.12, a subsection titled "Publication clarification on two-level multiplicities" refers to "the four-state stationary-branch table." No such table exists in Foundations; it is in *Physics* §3.13.3, which already contains the same clarification. This appears to be a patch applied to the wrong file.

*Fix:* delete it from Foundations.

---

## Should fix

### S1. The status system is not controlled [C]

The document's own Status Vocabulary defines 11 authority classes and a claim-status list, and says every principle carries both. In practice there are three separate schemas:

| Schema | Where used | Count |
|---|---|---:|
| `Authority class` (+ `Claim status` or `Claim/candidate status`) | Parts I, II, V, VII | 146 |
| `Registry status` (+ sometimes `Claim status`) | Parts I–IV, VIII | 49 |
| `Class` + `Status` | Part IX (commitments) | 19 |

The schemas are mixed *within* Parts I–IV. The `Authority class` field takes about 30 distinct values, such as "DOMAIN-PROVISIONAL POLITICAL-ECONOMY PRINCIPLE" and "FRAMEWORK-CANONICAL as a schema," against 11 defined. `Registry status` takes 9 values, none defined in the Status Vocabulary ("CANONICAL–CONDITIONAL," "CANONICAL as a research schema"). Twenty-one principles in Parts II–IV carry a registry status but no claim status.

The Mandala table in Part X uses **57 distinct status labels for 64 stages**. This is the same pattern the Ladder second pass corrected in its own registry, where 325 free-text labels became 11 types. The constitution should hold itself to the discipline it asks of the Ladder.

*Fix:* adopt one two-field schema, **authority class × claim status**, each drawn from a closed list defined in the Status Vocabulary. Domain and topic qualifiers ("political-economy," "clinical") go in the existing `Domain owner` field. For the Mandala table, map stage statuses onto the same closed list. The v0.19 object types, revised as in the Ladder review, are a natural source for the stage-level list.

### S2. CU-FP6 uses undefined symbols [S][C]

The formula is correct (see Verified). But r⁽ᵇ⁾ and D_N are never defined in the principle. The reader must infer r⁽ᵇ⁾ᵢ = pᵢ/q_b for i ∈ B_b and D_N(p) = ‖p − u_N‖². The KL term is also undefined for blocks with q_b = 0.

*Fix:* define both symbols inline and add the convention that blocks with q_b = 0 contribute zero. For a canonical formal statement, the reader should not have to consult *Physics* to parse it.

### S3. CU-L6's list of underdetermination causes conflicts with *Denying Knowledge* and with the formal definitions [S][C]

CU-L6 lists "incomplete ordering" among the causes of underdetermination. In a strict partial order, incomparability does not block a verdict. It simply enlarges the best set, which is exactly what makes *mere admissibility* distinguishable from strong warrant. *Denying Knowledge* §3.7 says this directly: "Ties do not by themselves create underdetermination."

More generally, the five verdicts as stated are not a partition. The three best-set verdicts already partition every case with B ≠ ∅. Infeasibility covers W = ∅. The only remaining *formal* case is W ≠ ∅ with B = ∅ (non-attainment). The other listed causes (unsettled facts, omitted affected parties, disputed floors) are judgments that the *model* is inadequate. They are a reason to withhold any verdict, not a sixth region of the formal space.

*Fix:* replace "incomplete ordering" with "unspecified or contested ordering." Split underdetermination into (a) *formal non-attainment* and (b) *model-adequacy abstention*, and state that (b) is a pre-verdict judgment.

### S4. Imported results lack in-text sources, contrary to the document's own rules [S][I]

CU-M2 and CU-M13 require every imported theorem to name its source and assumptions. Foundations itself contains no in-text citations. The following results are imported but unattributed:

| Location | Imported result | Source to cite |
|---|---|---|
| CU-L4 | System P for preferential consequence | Kraus, Lehmann & Magidor (1990) — in the reference list but not cited in text |
| CU-L4 | Rational Monotony for ranked models | Lehmann & Magidor (1992) — same |
| CU-M13 (1) | Exact between/within decomposition | Shorrocks (1980) / the generalized-entropy decomposition literature; *Physics* already credits GE(2) |
| CU-M14 | Refinement-invariant uniqueness of Fisher–Rao | Čencov (1982), via Markov morphisms; this is what the "refinement license" is protecting |
| PHYS-A6.9 | Einstein equations from horizon thermodynamics | Jacobson (1995) |
| Double Helix disposition | No periodic orbits in gradient flows | Standard dynamical-systems result; a textbook citation suffices |

The reference list also omits *Denying Knowledge* and *Non-Egoic Artificial Mind*, although §10.7 designates both as active companions.

*Fix:* add in-text citations at each location and add the two companions to the references. A constitution that requires source-naming should model it.

### S5. Superseded aliases still carry live claim statuses [S]

CU-V7 and CU-E-17 are correctly marked `SUPERSEDED ALIAS` → CU-G6. Yet their entries still show `Claim/candidate status: CANONICAL BRIDGE PRINCIPLE` and `PROVISIONAL NORMATIVE PRINCIPLE`. A superseded alias should carry only its disposition and controlling identifier. Otherwise it appears to hold authority.

*Fix:* replace the claim-status line in alias entries with "— (see CU-G6)."

### S6. Two commitment-principle titles differ in *Ethics* [C]

| ID | Foundations | *Ethics* |
|---|---|---|
| CU-COM14 | Love as the Ground and Aim of Conscious Life | Love as ethical relation |
| CU-COM17 | Redemptive Possibility Without Justification of Evil | Redemption without justification of evil |

COM17 differs only in wording. COM14 differs in substance. "Ethical relation" is a normative claim, while "ground and aim of conscious life" is a much stronger, quasi-metaphysical one. Appendix F requires domain papers to use controlling wording.

*Fix:* align the *Ethics* titles with Foundations, or revise Foundations if the *Ethics* wording is the intended one. See S8 on COM14.

### S7. The Appendix C review-gate tally is unnormalized [C]

Several rows are the same gate with different hyphenation: "context proportionate affected community review" (25) and "context-proportionate affected-community review" (5); "heightened affected community co governance" (18) and "heightened affected-community co-governance" (13). One label is truncated: "heightened public and affected community" (10). The table appears to have been generated from raw strings.

*Fix:* normalize the labels and merge the rows. Also reconcile with the text's claim that "every principle retains its named expert review gate": the table totals 89 entries against 214 principles, so the text should say whether the table covers participatory gates only.

### S8. CU-COM14's "descriptive ground" states a contested empirical claim as settled [S][I]

The descriptive ground reads: "flourishing and durable common life cannot be explained adequately through competition and self-interest alone." Whether cooperation is fully explicable through kin selection, reciprocity, and reputation (self-interest broadly construed) is an open debate in evolutionary biology and behavioral economics. Under CU-L3, a descriptive ground must be *established* fact.

Separately, "the highest practical expression of coherence" presupposes an ordering over expressions of coherence. That is in tension with CU-FP2's "no natural total ordering."

These are the author's commitments, and the aspiration is not in question. But the wording sits on the register line the corpus polices elsewhere.

*Suggested revision:* "…flourishing and durable common life depend substantially on care, cooperation, and repair, and are poorly described by competition alone." And: "CU commits to love as its highest practical aim."

### S9. Minor residue [S]

- Appendix A: "Version 0.10 retains the eleven Version 0.10 additions" does not say which eleven. Name them or cite the ledger.
- "M&E/This document" in §10.3 (see M4).
- The front-matter status ("RC2 remains the frozen baseline") versus the RC3 filename is intentional for a propagation draft. It should be resolved when RC3 is approved.

---

## Consider

### C1. The Analytic Frame card on a non-model document [I]

On Foundations, 5 of the card's 14 slots are "not applicable" or "none": state space, dynamics, equilibria, scalar, and allocation. The card was designed for domain models. Applied to a constitution, it reads as ritual, which slightly undercuts the method's credibility. Consider a short-form card for Foundations, M&E, and *Denying Knowledge* that keeps identity, claim status, translation status, and open gaps.

### C2. CU-G1–G7 already form the "service layer" the Mandala needs [I]

The Ladder review recommended moving the v0.19 merge families into a separate service layer. Foundations already contains most of that layer:

| Ladder family (v0.19) | Existing governance principle |
|---|---|
| MF01 Irreversibility and option value | CU-G7 |
| MF02 + MF03 Affected-party and future-party standing | CU-G1 (with CU-G5) |
| MF04 Option-set adequacy and authorship | CU-G2 |
| MF05 + MF13 Challenge, remedy, repair | CU-G3 |
| MF07 Distributed responsibility | CU-G4 |
| MF14 Patiency and welfare uncertainty | CU-G6 |

That is 8 of the 16 families. Anchoring the Mandala's services to the G-principles, rather than to new family identifiers, would link the formal Mandala directly to the constitution. It would also explain *why* those services recur across stages: they are framework-wide governance rules instantiated locally. This is the most useful connection between this audit and the Mandala work.

### C3. Notation in CU-D4 [S]

CU-D4 writes an unsubscripted C and "differentiable coherence functional." For consistency with CU-FP1 and FP2, write C_𝒟 and "a declared scalar of a type licensed under CU-FP2."

### C4. Add the fixed-coupling result to PHYS-A6 [I]

*Physics* §3.13.3 now shows that r = ½ is a stability threshold of one toy objective. A downstream paper could be tempted to cite it as a general threshold. A one-line PHYS-A6.3 addition would prevent that: "the stability change at β/α = ½ and the stationary bound r\* ≈ 0.621 are properties of the four-state sandbox objective, not cross-domain constants."

### C5. CU-COM15 commits to a descriptive thesis [I]

"CU commits to meaning realism" makes the object of a commitment a metaphysical claim, which CU-T10 already holds as an *interpretation*. That is permissible under the two-register discipline, since one can commit to living by a content whose truth is unsettled. It reads more cleanly as: "CU commits to inquiring into meaning as something discovered as well as made (see CU-T10)."

### C6. CU-T11's comparative [I]

"More stable, viable, generative, integrative, and capable of further development" puts heterogeneous properties into one comparative, which suggests one ordering. Consider "more stable, or more viable, or more generative…" or "better along one or more of these dimensions."

---

## Carry-forward to the corpus issue log

The following items concern other papers and are logged in `CU_v0.10_Corpus_Issue_Log.md`:

- *Physics*: no PHYS-A6 table (M2).
- *Denying Knowledge*: correct §3.3 to match CU-L4/L6 (M4).
- *Ethics*: COM14 and COM17 titles (S6).
- M&E: check that M&E §13 status labels use the controlled vocabulary once S1 is adopted.
