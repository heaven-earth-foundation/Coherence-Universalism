# CU v0.10 Audit 01: Metaphysics and Epistemology

**Reviewer:** Claude (Opus 5.5)
**Date:** 6 October 2026
**Text audited:** `01_CU_Metaphysics_Epistemology_v0.10_RC3_Methodological_Spine_Propagation_Draft.md` (28,416 words), from the RC3 Methodological Spine Propagation Working Package (package SHA-256 `23409d05…1c3a`, verified against the supplied checksum file)
**Comparison texts:** the RC3 drafts of *Foundations* (02), *Physics* (03), and *Denying Knowledge to Make Room for Commitment* (10); the Formal Ladder Review (v0.18–v0.19)
**Reproducibility:** `cu_me_audit_checks.py`. Every [C] finding cites its check number (E1–E12).
**Status:** Advisory. This audit assesses internal coherence, formal correctness, and sourcing. It is not evidence that Coherence Universalism describes the world (see §8).

---

## 0. Conventions and limits

The audit follows the seven-check protocol of the handoff unchanged: formal correctness, claim-status discipline, internal consistency, cross-paper consistency, sources, revision residue, and editorial. Every finding carries one label. **[S]** marks a finding that is source-supported, meaning stated in the texts and quoted or paraphrased from them. **[C]** marks a finding computed or checked by the reviewer and reproduced by the script. **[I]** marks reviewer inference, which can reasonably be disputed.

Two materials named in the handoff were not available for this session: `CU_v0.10_Corpus_Issue_Log.md` and `CU_v0.10_Audit_02_Foundations.md`. Two consequences follow. First, the report format below is taken from the handoff's description rather than from Audit 02 itself. Second, references to issue-log items #3, #4, #10, and #15, and to Audit 02's recommendation S1, rest on the handoff's descriptions of them. A rebuilt issue log accompanies this report. It numbers new items from #16 so that it can be merged into the original without renumbering.

---

## 1. Summary

*Metaphysics and Epistemology* is in good formal health where it matters most. The fixed-base preferential layer, the five-verdict taxonomy, the maximum-preservation result, the Boolean-obstruction counterexample, and the Cautious Monotony countermodel all check out. The paper's agreement with *Foundations* is also unusually close. All 64 Mandala titles and statuses are identical, every one of the 138 identifiers it cites resolves somewhere in the corpus, and the Shared Analytic Frame, Translation License levels, identity subprinciples, and governance family all match their controlling statements.

Five problems need fixing before release.

1. **The diagnosis of the two-stage obstruction is wrong in one respect [C].** The paper attributes the failure of Or to probability *thresholds* and says support-based feasibility restores the Boolean identities. Its own counterexample uses certainty feasibility. Support feasibility restores the conjunction identity but not the disjunction identity, because a policy can randomize across disjuncts. The cause is mixed policies, not thresholds (M1).
2. **Stage 64 breaks the paper's own claim discipline [S][I].** It presents a fundamental-ontology recognition with no interpretive label, and it says the recognition "entails" responsibility. Both conflict with explicit rules elsewhere in the paper (M2).
3. **Two formal cross-references point at nothing [S]** (M3).
4. **The §13.14 Mandala paragraph has three propagation defects and contradicts §13.16 [S]** (M4).
5. **The PHYS-A6 identifiers resolve, but mostly to the wrong constraints [C].** Issue #3 reported that these identifiers do not resolve in *Physics*. They actually resolve to *Foundations* Part VI, the Physics Constraint Registry. In five of the ten physical stages, however, the cited constraint has nothing to do with the stage, which suggests numbering by position rather than by content (M5).

The most consequential should-fix item concerns the Mandala's edge vocabulary. M&E §13.1 defines normative protection so that its arrow points from the protected capacity *up* to the protecting structure. Under that convention a correctly drawn protection edge runs forward in stage order, like every other edge. This qualifies the Formal Ladder Review's finding of "zero downward protection edges": the absence is partly a matter of convention. What is genuinely missing is a *typed* protection relation. Section 5 gives a reconciled vocabulary with explicit direction conventions (S1).

On the open question of whether trimming the overlap with *Denying Knowledge* would solve M&E's length problem, the answer is no, but the overlap is not where the length is [C][I]. The overlapping sections save at most about 2,000 words. Section 13 is about 4,800 words, and 3,100 of them are the stage list in §13.14. Condensing §13 under the agreed companion-paper plan, together with trimming the overlap, would bring the paper to roughly 23,000 words. Splitting M&E is not needed (§6).

**Totals:** 5 must fix, 11 should fix, 11 to consider.

---

## 2. Verified correct

These checks passed. They are recorded so that later audits do not repeat them.

| Item | Check | Result | Label |
|---|---|---|---|
| §7.4–7.5 System P setup | Relation without nonemptiness clause carries System P; strong warrant adds the clause | Correct; matches handoff reference | [S] |
| §7.6, §9.2 Rational Monotony and System R | Ranked order plus attained minima | Correctly conditioned | [S] |
| §8.3 singleton best set | No mere admissibility when the best set is a singleton | Confirmed exhaustively | [C] E3 |
| §8.4 classical negation | Exclusion of φ ⟺ strong warrant for ¬φ, nonempty best set | Confirmed exhaustively | [C] E3 |
| §8.2 verdicts | Strong, merely admissible, and excluded partition the nonempty cases | Confirmed | [C] E3 |
| §8.5, A.7 maximum preservation | Equal maximum ⟺ some old maximizer satisfies φ, i.e. admissibility | Confirmed (20,000 random cases) | [C] E4 |
| §9.7 threshold inequalities | Π₍α∧β₎ ≠ Π_α ∩ Π_β and Π₍α∨β₎ ≠ Π_α ∪ Π_β in general | Correct | [C] E1–E2 |
| §10.2 retained properties | Reflexivity, LLE, RW, And for the two-stage relation | Correct under stated assumptions | [I] |
| §10.4 Or counterexample | Or fails for the two-stage aggregate | Valid; instance constructed | [C] E1 |
| B.13 countermodel | Premise-responsive base defeats Cautious Monotony | Correct | [C] E5 |
| §3.7 block averaging | D falls by within-block squares; H rises by KL; unequal; shared equality set | Confirmed; consistent with *Physics* §3.3 and §3.16 | [C] E6 |
| §3.10 Shared Analytic Frame | Fourteen slots vs CU-M12 | Match (minor wording only) | [S] |
| §§2.5–2.6, §3.11 Translation Licenses | Levels 0–4 and ten translation items vs CU-M2 | Match | [S] |
| §4.6 identity architecture | CU-FP8a–e titles and content | Match | [S] |
| §12 governance family | CU-G1–G7 titles | Match | [S] |
| §15.6 CU-T11 | No residual single-functional language | Clean in M&E; issue #4 lies elsewhere | [S] |
| §16 commitment titles | Twelve CU-COM titles vs *Foundations* | All match | [C] |
| v0.10 proposals | CU-B4, CU-CL12 (stage 51), CU-AI27 (stage 59) statuses | Match *Foundations* exactly | [S] |
| §13.14 stage titles and statuses | All 64 vs the *Foundations* stage table | 64/64 titles and 64/64 statuses identical | [C] E7 |
| Identifier resolution | All 138 distinct CU-, CU-Ψ, and PHYS- identifiers | All resolve somewhere in the corpus | [C] E8 |
| Reference list | Bibliographic details of the ten external references | Consistent with standard records (reviewer knowledge; all pre-2026, so no web check needed) | [I] |

---

## 3. Must fix

### M1. The two-stage obstruction is attributed to the wrong cause [C] (§10.3, §10.5, §10.7, Appendix B.5)

Section 10.3 says that "when feasibility is probability-thresholded," the feasibility map is not a Boolean homomorphism. Section 10.5 says the identities hold for classical model sets "but not for probability-thresholded policy sets." Section 10.7 then offers *classical set feasibility*, Π_α = {π : Supp(P_π) ⊆ ⟦α⟧}, as a route by which "some Boolean identities can be restored."

The paper's own counterexample (§10.4) uses certainty feasibility, and Appendix B.5 states δ = 0 explicitly. For finite outcome spaces, certainty feasibility is exactly the support condition of §10.7. Check E2 confirms both halves of the matter. The support condition does restore the conjunction identity for every pair of events. It does not restore the disjunction identity: the mixing policy π_M belongs to Π₍A∨B₎ without belonging to Π_A or Π_B. The Or failure in §10.4 is therefore an instance of the very feasibility rule that §10.7 presents as a remedy.

The real source of the obstruction is that a policy induces a *distribution*, and a distribution can satisfy a disjunction without satisfying either disjunct. Thresholds make the problem worse, because they also break conjunction, but they are not its cause. The withdrawn v0.09 proof imported valuation-semantics identities into an object whose disjunction behaves differently, and that remains true. Only the diagnosis needs correcting.

**Recommended revision.** In §10.3, replace "When feasibility is probability-thresholded" with "Because feasibility is defined over policy-induced distributions." In §10.7, state that support-based feasibility restores the conjunction identity only, that Or continues to fail whenever policies can randomize across disjuncts, and that restoring Or requires deterministic or point-mass policies, a restricted premise class, or the joint policy–trajectory construction. Retitle B.5 accordingly; with δ = 0 it is not a threshold result. *Foundations* line 1283 uses the same "probability-thresholded" framing and should change with it (issue log #16).

### M2. Stage 64 exceeds the paper's own claim discipline [S][I] (§13.14 stage 64, §13.15)

Stage 64 reads: "Coherence under constraint is recognized as the fundamental organizing principle of reality and inquiry … and it entails responsibility for truthful, loving, corrigible participation in the whole." Its status label is "[Canonical systems-metaphysical recognition / framework identity]." Section 13.15 repeats the assertion and adds that "the stage is the disclosure of the framework to a finite center within the reality it describes."

Five passages of the same paper rule this out as written.

- **§1.8** says the paper "does not prove that coherence is a substance, field, cosmic purpose, or moral agent."
- **§2.3** names "therefore reality is a coherence field" as the paradigm overclaim made without a bridge.
- **§2.8** places fundamental ontology at the top of the burden-of-proof sequence.
- **§13.13** says the Mandala's spiritual recognition "belongs to the interpretive and commitment register unless a stronger ontological argument is supplied."
- **The abstract** says the Mandala is not "a derivation of ethics from cosmology."

"Is recognized as" asserts. "Entails" derives a commitment from a description. Each is exactly what the asymmetric-permeability principle of §6.7 forbids without an explicit bridge. The scan for strong claim verbs (claims, proofs, entailments, validations not under negation) finds no other unbracketed instance in the paper, so stage 64 stands alone [C].

**Recommended revision.** Add the interpretive register to the status label, for example "[Interpretive recognition / framework identity; commitment register]." Replace "is recognized as" with "is interpreted as" or "CU's culminating interpretation holds that." Replace "entails responsibility" with "is taken up as responsibility" or "calls for." The stage's moral grammar, "Recognition becomes responsibility," already uses the right verb. Apply the same changes to §13.15 and to the *Foundations* stage table, which carries an identical status (issue log #17).

### M3. Two formal cross-references point at nothing [S] (Appendix B.4, Appendix B.13)

Appendix B.4 says "Use the two tied best worlds from A.7." Appendix A.7 is a two-sentence prose statement with no worlds in it. Appendix B.13 ends: "The countermodel shows why Theorem A.1 requires a fixed base." There is no Theorem A.1. A.1 contains definitions, and the System P statement is in A.3. The B.13 countermodel itself is correct [C, E5].

**Recommended revision.** Supply the B.4 construction inline. Two tied best worlds w₁ and w₂ with φ true only at w₁ and ψ true only at w₂ suffice: each preserves the maximum, and φ ∧ ψ preserves none. Change "Theorem A.1" to "the System P result of A.3."

### M4. Propagation defects and a contradiction in the §13.14 Mandala paragraph [S][C] (§13.14, §13.16, Appendix B.5)

The handoff's three known defects are confirmed [C, E11]. The paragraph reads "Version Version 0.10." It contains the incomplete clause "a six-bit label is supplied for navigation from to." And it describes the Yi Jing comparison as an open source-recovery task (issue #10). A fourth defect of the same kind is the Appendix B.5 heading, "## Version 0.10 Probability-threshold disjunction failure," where "B.5" should be.

Two further observations change what the right fix is.

First, no six-bit labels appear anywhere in M&E [C, E11]. The clause "from to" most likely once read "from 000000 to 111111," with the digit strings removed during propagation [I]. Restoring the digits would therefore promise labels the paper does not contain.

Second, the paragraph contradicts §13.16. Section 13.14 says the book snapshot "does not contain that appendix," so the comparison cannot yet be made. Section 13.16 describes that same appendix confidently: "Appendix B of that book offers a Yi Jing contemplative traversal through Shao Yong's binary sequence."

**Recommended revision.** Delete the six-bit sentence and the source-recovery sentence. Adopt the *Foundations* wording (its lines 38 and 3973), which keeps the book's Yi Jing traversal as a cross-reference only and makes no claim about labels. Keep §13.16. This also closes issue #10. Correct "Version Version" and the B.5 heading.

### M5. The PHYS-A6 identifiers resolve, but mostly to the wrong constraints [C][I] (§13.14 stages 1–10)

Issue #3 recorded that the nine PHYS-A6 identifiers used in stages 1–10 do not resolve in *Physics*. That is true: *Physics* contains no PHYS- identifiers at all. But all of them resolve in *Foundations* Part VI, the Physics Constraint Registry, which defines PHYS-A6.1 through A6.12 [C, E8]. The problem is not resolution but fit.

| Stage | Cited | Registry title | Fit [I] |
|---|---|---|---|
| 1 Pure Structure | A6.1 | Statistical differentiation is a toy proxy | No |
| 2 Partial Separability | A6.2 | Euclidean and Fisher geometry differ | No |
| 4 Lawful Transitions | A6.3 | Goldilocks conditions are plural | No |
| 5 Ordered Histories | A6.4 | Temporal order is not temporal direction | Yes |
| 6 Temporal Order | A6.4; A6.5 | …; Classical hidden correlation does not force quantum theory | Yes; No |
| 7 Computation | A6.4 | Temporal order is not temporal direction | Weak |
| 8 Entropy and Accessibility | A6.5; A6.6 | …; Quantum selection is conditional | No; No |
| 9 Relational Geometry | A6.9; A6.10 | Standard equations are embeddings…; Accessibility geometry remains incomplete | Yes; Yes |
| 10 Gravitational Dynamics | A6.10; A6.11 | …; Horizon entropy is reduced-description entropy | Yes; Plausible |

The pattern in stages 1–4, A6.1 to A6.3 assigned in sequence, suggests the identifiers were attached by position rather than by content [I]. The *Foundations* stage table carries the same identifiers, since its related-principle lists match M&E's for stages 1–10 [C, E7].

**Recommended revision.** Reassign by content. Stage 1 → A6.12 (fundamental-substrate claims are interpretive). Stage 8 → A6.1 (statistical differentiation is a toy proxy), which fits the entropy-and-accessibility stage. Stages 2 and 4 have no matching registry item. Cite *Physics* §2.3 and §4.3 directly, or add registry items for them. The quantum items A6.5–A6.7 and the second-order item A6.8 have no stage at all, which bears on S2 below. Make the same change in *Foundations*. Issue #3 should be restated accordingly.

---

## 4. Should fix

### S1. The edge vocabulary needs explicit direction conventions [S][I] (§13.1, §13.12; issue #15)

Section 13.1 defines seven edge types. Its definition of normative protection reads: "the target supplies conditions that preserve or govern the source." The other six types are written so that the source is prior and the target depends on it. Under §13.1's own convention, then, a protection edge points *from* the protected lower-stage capacity *to* the higher-stage protecting structure. It runs forward in stage order, like everything else.

This qualifies a finding of the Formal Ladder Review. That review found zero governance-to-capacity edges running backward in stage order and called the downward-protection relation missing. If the v0.19 build followed M&E's convention, a protection edge drawn correctly *would* run forward and could not be distinguished from a presupposition edge by direction alone [I]. The review's substantive point survives: the registry has no edge *typed* as protection. But the remedy is a type with an explicit direction rule, not merely a backward arrow.

The three vocabularies also mix two different things. M&E's list combines kinds of relation (constitutive, enabling, protection) with kinds of warrant (conceptual, formal, empirical, bridge hypothesis). An empirically supported enabling edge has no single correct label under the present list.

**Recommended reconciled vocabulary [I].** Record two fields on every edge.

*Relation type*, with the direction convention stated per type:

| Type | Direction convention | Proof-order acyclicity |
|---|---|---|
| Strict prerequisite | prerequisite → dependent | Required, after adjudication |
| Presupposition (e.g. governance of X presupposes X) | presupposed → presupposing | Required, after adjudication |
| Enabling | enabler → enabled | Required, after adjudication |
| Constitutive or decomposition | part → whole | Within-object only |
| Implementation or representation | implementer → implemented | Exempt |
| **Protection** | **protector → protected** | **Exempt** |
| **Service invocation** | invoking stage or object → shared service, with scope parameters | **Exempt** |
| Feedback or correction | corrector → corrected | Exempt |
| Interpretive bridge | described structure → interpretation or commitment | Exempt |
| Summary membership | member → summary | Exempt |

*Warrant basis:* conceptual, formal, nomological or empirical, practical or normative (matching the four necessities of §2.2), or hypothesized. "Bridge hypothesis" becomes a warrant value rather than a relation type.

Writing protection as protector → protected makes it the one type whose arrows normally run backward in stage order, which is what the Mandala image requires. It also keeps protection visibly distinct from presupposition. The table maps directly onto CU-M15's seven types and the v0.19 registry's six. It should replace the edge lists in §13.1, §13.12, and CU-M15 together, so that only one controlling formulation exists.

### S2. The paper gives two different physical sequences, and *Physics* gives a third [S] (§13.3, §13.14 stages 1–10; *Physics* §1.5)

Section 13.3 lists ten physical steps: relational structure, partial separability, admissible transitions, temporal order, parameterized histories, an arrow of time, access maps, information geometry, quantum theory, and relational geometry with Einstein-type dynamics. Stages 1–10 in §13.14 list a different ten: pure structure, partial separability, coherence directions, lawful transitions, ordered histories, temporal parameterization, computation, entropy and accessibility, relational geometry, and gravity. *Physics* §1.5 lists a third ten that matches the stages closely but not exactly. Quantum theory appears in §13.3 and has three registry items (A6.5–A6.7), but no stage.

**Recommended revision.** Align §13.3 with stages 1–10, or state explicitly that §13.3 is the evidential program and the stages are the traversal, and say where quantum theory sits in the traversal (issue log #21).

### S3. The canonical graph protocol is unmet and too narrow [C][S] (§13.1, §13.12)

Section 13.12 says that "every v0.10 domain paper should provide a dependency table" and that the final Ladder "will be rebuilt from these tables." None of the eleven papers contains such a table; the only one in the corpus is the template in §13.12 itself [C, E9]. The template also restricts both endpoints to "named capacity," and §13.1 defines nodes as "structural capacities or explanatory commitments." CU-M15 and the v0.19 registry use eleven object types, including evaluators and governance relations.

**Recommended revision.** Either supply the tables or soften §13.12 to a stated intention with the v0.19 registry as the interim source. In both §13.1 and §13.12, replace "capacity" with "typed object," following CU-M15 (issue log #19).

### S4. §4.10's three-way distinction conflicts with CU-G6's four [S] (§4.10, §12.7)

Section 4.10 states "causal agency ≠ moral patiency ≠ responsible sovereignty," a three-way distinction "central to later papers." CU-G6, stated in §12.7 and in *Foundations*, distinguishes four properties: patiency, agency, responsibility, and sovereignty. Section 4.10 merges the last two, and its own prose ("may still be a moral patient … its designers and operators may bear responsibility") treats them separately. The chained "≠" is also not transitive, so it does not assert that the first and third differ.

**Recommended revision.** Align §4.10 with the four-way CU-G6 formulation, using the ⇏ notation of §12.7.

### S5. Notation clashes [S] (§7.9, §9.2, §9.6, §9.10, Appendix B.13)

Three notational problems would each confuse a careful reader.

- **⇝ has two meanings.** In §7.9 it denotes model revision. In Appendix B.13 it denotes consequence. B.13 should use the paper's consequence symbol.
- **The trajectory base changes name.** Section 9.2 calls it V_F^Ω. Section 9.10 calls the same object "a fixed trajectory-level viability predicate V_F."
- **§9.6 attaches "P_π-almost surely" to a set inclusion.** An inclusion between sets is not an almost-sure statement. The intended condition is presumably P_π(T_π(⟦α⟧) ∖ ⟦β⟧) = 0.

### S6. Display math is double-escaped and will not render [C] (§12.7)

The CU-G6 display in §12.7 is written with doubled backslashes (`\\text{patiency}\\not\\Rightarrow…`). In LaTeX, `\\` is a line break, so the display renders as broken text. The same artifact appears in *Foundations* in the CU-FP8 schema and the CU-M10 burden sequence. No other paper is affected [C, E10]. It is a propagation artifact and should be fixed corpus-wide with a single replacement (issue log #20).

### S7. Two sentences say something other than what is meant [S] (§12.3, §6.4)

Section 12.3 reads: "A procedure can operate perfectly on U^pres while the institution controlling the menu excludes no action, delay, staged intervention…" "Excludes no action" reads as "excludes nothing." The intended reading is "excludes inaction, delay, staged intervention…"

Section 6.4 ends: "A commitment act can be unwarranted even where the descriptive truth of its content does not settle whether it should be adopted." As written this is close to vacuous. The intended point is presumably: "A commitment act can be unwarranted even when its content is true, because descriptive truth does not settle whether it should be adopted."

### S8. Stage statuses need a controlled vocabulary [C][S] (§13.14; Audit 02 S1)

The 64 stages carry 57 distinct status labels [C, E7]. Appendix C.1 of the same paper already defines a ten-value status vocabulary (definition, formal result, conditional result, imported result, empirical claim, bridge principle, hypothesis, interpretation, commitment, open problem), and the Mandala does not use it. This confirms Audit 02's recommendation S1 as described in the handoff.

**Recommended revision.** Assign each stage a primary status from C.1, with an optional domain qualifier. Doing so would also have caught M2, because stage 64 has no C.1 value that fits its current wording.

### S9. Two definitions of the registers still use v0.09 content language [S] (§1.6, Appendix E)

Section 6.2 and the abstract make the register distinction one of "speech-act force, use, and assessment standard rather than … different semantic kinds." *Denying Knowledge* §2 writes it the same way, as kinds of *use*. Two places in M&E still define the registers by content. Section 1.6 says the description register "contains claims that are truth-apt." The glossary defines the commitment register as discourse that orients action "rather than describe an independently specifiable state of affairs."

**Recommended revision.** Restate both in the use-based form of §6.2 (issue log #22).

### S10. The paper has no in-text citations [C][S] (body and References)

The reference list contains ten external works, but none is cited by author and date anywhere in the body. Five are never mentioned at all: Alchourrón, Gärdenfors, and Makinson (1985); Carnap (1950); Kant; Quine (1951); and Wittgenstein (1953). *Love Letters to Humanity* is also never mentioned. Conversely, *Foundations* is cited four times but is absent from the reference list. The imported results that carry the most weight (KLM System P, Lehmann–Magidor ranked models, Gödel, Tarski, Löb) are named but not cited at the point of use, and the Hilbert–Bernays derivability conditions of §14.7 have no reference.

**Recommended revision.** Add author-date citations at each imported result. Cite or remove the five unused references. Add *Foundations* to the list (issue log #23 tracks whether other papers share this pattern).

### S11. The translation card is out of step with CU-M2 [S] (Appendix C.2)

Section 2.6 and CU-M2 require ten items for a cross-domain translation, including the declared license level, the claim-status change, and the review gate. The Appendix C.2 card has eight rows and lacks all three, while adding a "competing map" row that §2.6 lacks.

**Recommended revision.** Rebuild C.2 from the CU-M2 list and keep "competing map" as an eleventh row.

---

## 5. Consider

**K1. Note that the strong-warrant relation is not itself a KLM relation [C].** The relation ⊨^∀ with the nonemptiness clause fails Reflexivity whenever V_F ∩ Mod(α) is empty. System P belongs to the plain relation |∼ of §7.4. One sentence in §7.4 saying so would make the reference treatment airtight and would serve as the model for fixing *Denying Knowledge* §3.3.

**K2. State the formal partition of verdicts in §8.2 [C].** At the formal level the cases partition cleanly: infeasible (W_{F,Γ} = ∅); unattained (W_{F,Γ} ≠ ∅, B = ∅); and, for nonempty B, strong, merely admissible, or excluded. Underdetermination then has a formal core, non-attainment, plus a model-adequacy overlay. Saying so would make the five verdicts visibly exhaustive.

**K3. Give the conclusion γ in §10.4.** The counterexample says a conclusion "may hold" under π_A and π_B but fail under π_M without exhibiting one. A concrete instance is constructed in check E1 and could be stated in two lines.

**K4. Use the standard consequence symbol.** The paper writes Γ ∼_C φ where the literature writes Γ |∼ φ. The plain tilde is commonly read as negation.

**K5. Mark the formalized Löb display.** The prose of §14.7 states Löb's rule (if ⊢ □φ → φ then ⊢ φ). The display □(□φ → φ) → □φ is the formalized version and should carry a turnstile.

**K6. Keep one notation for the risk functional.** Section 9.5 writes ρ(J; P_π) and §9.8 writes ρ(J; P, π).

**K7. Tidy the glossary.** A second block of entries follows a horizontal rule without being merged alphabetically, which looks like a propagation artifact. The glossary also lacks entries for Translation License, Shared Analytic Frame, Coherence Analysis Protocol, Methodological Spine, and model revision.

**K8. Move the revision history out of the body.** The Note on Version 0.10 says the manuscript "presents the mature framework directly." The body nevertheless carries version-comparison passages, for example in §1.2.1, §10.3 ("the earlier M&E paper"), §10.5, §13.2, §13.10, and §14.4. *Denying Knowledge* collects its equivalents in an Appendix B "Revision and Audit Note," and the same arrangement would suit M&E.

**K9. Add "exit" to §6.10.** Its Open Myth requirements omit "exit," which stage 51 and CU-CL12 include.

**K10. Remove the duplicate necessity list.** The four kinds of necessity are stated twice, in §1.4 and §2.2.

**K11. Condense §13 and point the epistemology sections to *Denying Knowledge*.** See §6 below.

---

## 6. The overlap with *Denying Knowledge* and the length question [C][I]

The handoff left open whether M&E's epistemology sections could summarize and point to *Denying Knowledge* rather than restate it, and whether that would solve the length problem that prompted the idea of splitting M&E.

**Where the overlap is [C, E12].** Shared verbatim eight-word sequences appear only in §6 (17 percent), §7 (23 percent), and §8 (7 percent). Sections 9 and 10, the dynamic, probabilistic, and two-stage material, are not in *Denying Knowledge* at all and must stay in M&E. Appendix D.3 already names *Denying Knowledge* as the "controlling source for the Version 0.10 commitment-logic clarification." That supports making §§6–8 a summary with a pointer.

**What trimming would save [C][I].** Sections 6–8 total about 2,650 words. A summary that keeps the definitions the rest of the paper uses (the realization relation, the fixed base, the five verdicts) would save about 1,500–2,000 words, roughly 7 percent of the paper. That alone does not solve the length problem.

**Where the length is [C].** Section 13 is about 4,800 words, the largest section by a factor of more than two. Of these, 3,100 words are the 64-stage list in §13.14. The agreed plan moves the formal Mandala to a standalone companion paper and leaves the main papers with a condensed §13, a revised CU-M15, and a one-paragraph structural statement. A condensed §13 with a compact stage table instead of 64 prose entries would save about 3,000 words.

**Recommendation [I].** Do both. The result is a paper of roughly 23,000 words that is complete without *Denying Knowledge* for its formal layer and complete without the Mandala companion for its stage register. This reinforces the earlier advice: do not split M&E.

---

## 7. Carry-forward items for the issue log

New items are numbered from #16; see the rebuilt log for full entries.

- **#16 Two-stage obstruction misattributed to thresholds.** M&E §10.3, §10.5, §10.7, B.5; *Foundations* line 1283. Check the *Artificial Intelligence* paper, which also discusses the two-stage architecture, at its audit.
- **#17 Stage 64 claim status.** M&E §13.14–13.15; *Foundations* stage table and Part X.
- **#18 Edge direction convention.** M&E §13.1 and §13.12, CU-M15, v0.19 registry. Extends #15.
- **#19 Dependency tables required by §13.12 are absent from every paper.**
- **#20 Double-escaped LaTeX.** M&E §12.7; *Foundations* CU-FP8 and CU-M10.
- **#21 Three physical sequences.** M&E §13.3, stages 1–10, *Physics* §1.5; quantum theory has no stage.
- **#22 Content-based register definitions.** M&E §1.6 and glossary. Check *Foundations* and the domain papers.
- **#23 Citation practice.** No in-text citations in M&E. Check every paper.
- **#24 Truncated related-principle lists.** The *Foundations* stage table lists fewer related principles than M&E at stages 3, 25, 29, 31, 35, 63, and 64.
- **#25 Possible digit-stripping artifact.** "navigation from to" in M&E §13.14. Search every paper for other places where digit strings may have been removed.
- **Restated #3.** PHYS-A6 identifiers resolve in *Foundations* Part VI but mostly mismatch their stages (M5).
- **#10.** Closed by M4's recommendation, if adopted.
- **#4.** CU-T11 is clean in M&E; the residual lies in another paper.

---

## 8. Standing caution

Every finding in this audit concerns internal coherence, formal correctness, or sourcing. The formal results that pass here, such as System P for the fixed-base relation, are imported mathematics correctly applied to declared models. They say nothing about whether the models' viability bases, orderings, or interpretations are the right ones, and the paper itself is careful to say so (§7.10, §12.9).

Passing this audit does not show that Coherence Universalism describes the world, that the Mandala's stages are real dependencies, or that the interpretive and commitment registers are warranted. Those questions are answerable only through the research program the paper sets out in §17, and this report should not be read as moving the framework closer to them.
