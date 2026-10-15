# CU v0.10 Audit 04: Biology

**Reviewer:** Claude (Opus 5.5)
**Date:** 7 October 2026
**Text audited:** `04_CU_Biology_v0.10_RC3_Methodological_Spine_Propagation_Draft.md` (26,193 words), from the RC3 Methodological Spine Propagation Working Package (SHA-256 `23409d05…1c3a`, verified)
**Comparison texts:** *Foundations* (02), especially the Biology domain registry, CU-D3, CU-COM8, and the 64-stage table; *Consciousness* (05) for the §8.14 cross-reference; the corpus issue log
**Reproducibility:** `cu_bi_audit_checks.py`. Every [C] finding cites its check number (B1–B10).
**Status:** Advisory. This audit assesses internal coherence, formal correctness, and sourcing. It is not evidence that CU's account of life describes living systems (see §7).

---

## 0. Conventions and coverage

The audit uses the seven-check protocol and the labels of the earlier audits. **[S]** marks a finding that is source-supported, **[C]** one computed or checked by the reviewer and reproduced by the script, and **[I]** reviewer inference.

**Coverage.** At about 26,000 words the paper could be read in full, and it was: front matter, the Domain Analytic Frame, §§1–13, Appendices A–C, and the references. Section 12 (the eight research programs) was read for structure, outcomes, and narrowing conditions rather than checked sentence by sentence. Whole-paper scans covered identifiers, principle wording against *Foundations*, citations against references, notation reuse, math delimiters, and propagation artifacts.

**Sources.** Seven citations were checked by web search, chosen because they are recent or carry specific empirical claims: Rajan et al. (2026), Giessler et al. (2026), Cortés-Poza (2026), Herrera-Álvarez, Patton, and Thornton (2025), Doulcier et al. (2024), Kolchinsky (2024), and Rohner, Hu, and Moczek (2022). The older canonical references (Aubin, Varela–Maturana–Uribe, Maynard Smith–Szathmáry, Losos, Travisano, Blount, Huang, Schaper–Louis, Aoki, Kriegman) are standard and were checked for bibliographic form only. Shi et al. (2025), Shirt-Ediss et al. (2025), Simões et al. (2019), Storz et al. (2019), and Ciriello et al. (2024) were not checked this session.

**A correction to the handoff.** The handoff asked for a check of "stage 11–16 identifiers and titles." The biological branch of the Mandala is stages 11–15, which is exactly what *Biology* §13.11 says. Stage 16 in *Foundations* is "Representational Organization," a psychological and consciousness bridge (B5).

---

## 1. Summary

*Biology* is in good condition. The v0.10 rewrite did what Appendix B says it did: the universal scalar \(C = AI\), the universal gradient, the single abiogenesis threshold, and the toy-model validation claim are all gone, and the paper says plainly what replaced each. Its claim discipline is strong. Every principle carries a status label, interpretations and commitments are marked as such, §13 opens with a register note, and nearly every section ends by saying what its result does not show. Its citation practice matches *Physics*: all 35 non-self references are cited in the text, and no in-text citation lacks an entry (B10). All seven sampled sources exist and support the use made of them, including the three from 2026.

The formal architecture of §3 (viability region, finite-horizon and robust viability kernels, intervention-based maintenance contribution, value of information) is stated correctly, and the quantifier order in the robust kernel is the right one. The §6.8 counterexample to recurrence dominance is correct (B1). The paper's central formal claim about coupling, that one diffusive law can raise or lower viability depending on floors and state, reproduces in an independent reconstruction (B2).

Two items must be fixed.

- **The §6.8 counterexample does not render [C].** In four places the conditional bar is written `$\mid$` inside an expression that is already in math mode. This is the only occurrence in the corpus, and §§4–6 are the only sections in the corpus that use `$` delimiters at all. A delimiter conversion appears to have broken the paper's own counterexample (M1).
- **The aging formula in §10.7 does not say what the text says [C].** The text describes aging as a "contraction or reshaping" of the robust viability kernel, but the formula only says the later kernel is not a superset of the earlier one. An organism whose kernel nearly triples while losing one marginal state satisfies it (M2).

The should-fix items are mostly about consistency. The principle boxes in §§6.13, 7.13, and 8.13 differ in wording from the canonical text, which Appendix A reproduces correctly (S1). The status labels on the five principles use two different schemas (S2). Several symbols are reused for unrelated objects, most notably \(\mathcal U\), which has four meanings (S6). And the paper's one constructive formal demonstration, the two diffusive-coupling configurations, is in a supplement that is not in the package (S8).

**Totals:** 2 must fix, 9 should fix, 8 to consider.

---

## 2. Verified correct

| Item | Check | Result | Label |
|---|---|---|---|
| Mandala stages 11–15 named in §13.11 | B5 | All five titles identical to *Foundations*; stage 16 is not biological | [C] |
| Identifiers cited in *Biology* | B7 | 20 distinct; all resolve | [C] |
| CU-COM8 commitment statement, boundary, and revision condition | B7 | Identical to *Foundations* §9.10 | [C] |
| Appendix A principle texts (CU-B1–B5) | B6 | All five identical to the *Foundations* registry | [C] |
| CU-B4 claim status | B6 | "Canonical–conditional empirical generalization" matches the *Foundations* status field | [C] |
| CU-D3 as gateway to CU-B1 (§1.3, A.1) | read | Matches *Foundations* CU-D3 exactly in substance | [S] |
| §6.8 recurrence-dominance counterexample | B1 | 0.99 > 0.10; a passive two-state chain satisfies the criterion | [C] |
| Diffusive coupling can reverse the viability effect (§3.16, D4, P5) | B2 | Under \(\dot x_i = k(\bar x - x_i)\), viable time rises from 0 to 0.99 in one configuration and falls from 1.0 to 0.01 in another as \(k\) grows | [C] |
| Robust viability kernel quantifier order (§3.4) | read | ∃ρ ∀d is the correct non-anticipative order; the text explains why | [I] |
| §8.14 cross-reference to *Consciousness* | B7 | "access organization," "perspectival anchoring," and "center individuation" all occur in 05 | [C] |
| Citations | B10 | 35 of 35 non-self entries cited; no citation without an entry | [C] |
| Rajan et al. (2026), *Current Biology* 36(9) | search | Exists. Protein-synthesis inhibitors sped habituation rather than blocking it, memory works by modifying existing proteins, and daughter cells inherited it, as §8.6 says | [S] |
| Giessler et al. (2026), *Angewandte* | search | Exists; ribozyme-driven dissolution, segregation, and genetically encoded regrowth of RNA droplets, as §6.5 says | [S] |
| Cortés-Poza (2026), *J. Math. Biol.* 93(3):43 | search | Exists (31 Aug 2026); couples bioelectric, gene-regulatory, and slow tissue-memory layers, as §7.10 says | [S] |
| Herrera-Álvarez et al. (2025), *Nat. Ecol. Evol.* 9:1656–1669 | search | Exists; supports the anisotropy claim (see K3 on one sentence) | [S] |
| Doulcier et al. (2024), *Nat. Commun.* 15:6566 | search | Exists; ecological scaffolding stabilized through evolutionary hysteresis, as §9.13 says | [S] |
| Kolchinsky (2024), arXiv:2404.01130 | search | Exists; argues England's bound is not a universal replicator law, as §5.4 says | [S] |
| Rohner, Hu, and Moczek (2022), *Proc. R. Soc. B* 289:20221441 | search | Exists; "developmental lines of least resistance" in beetle horn shape, as §9.6 says | [S] |
| Digit-stripping, doubled `\\text`, lowercase "this paper" | B9 | None found | [C] |

---

## 3. Must fix

### M1. The §6.8 counterexample does not render [C] (§6.8, lines 1153–1170; §§4–6 generally)

**Evidence.** The display reads `$$ P(L_{t+1}$\mid$L_t) > P(L_{t+1}$\mid$\neg L_t) $$`, and the inline sentence after the transition matrix has the same pattern twice (B9). Inside `$$…$$`, each inner `$` closes and reopens math mode, so the expression breaks wherever it is rendered. No other paper contains `$\mid$`, and *Biology* §§4–6 are the only sections in the eleven papers that use `$` delimiters (the rest of *Biology* and every other paper use `\(…\)` and `\[…\]`). The most likely cause is a delimiter conversion that turned `|` into `$\mid$` to protect Markdown tables.

**Recommended revision.** Replace `$\mid$` with `\mid` in all four places. Then convert §§4–6 to the `\(…\)` and `\[…\]` delimiters used everywhere else, so the corpus has one convention. Re-render §6.8 to confirm.

### M2. The aging formula does not express contraction [C] (§10.7)

**Evidence.** The text says aging "is modeled as a time-dependent contraction or reshaping of viable and recoverable trajectories," and gives

\[
\operatorname{RViab}_{T}^{(a+\Delta a)} \not\supseteq \operatorname{RViab}_{T}^{(a)}.
\]

This says only that at least one previously viable state is no longer viable. It is satisfied by a kernel of 29 states that replaces one of 10 (B4). It does not say the kernel got smaller in any sense, and the qualifier "for many—but not necessarily all—challenge classes" does not repair that.

**Recommended revision.** State the intended claim directly. If the claim is contraction, write \(\operatorname{RViab}_{T}^{(a+\Delta a)} \subsetneq \operatorname{RViab}_{T}^{(a)}\) for many challenge classes, or use a measure, \(\mu(\operatorname{RViab}_{T}^{(a+\Delta a)}) < \mu(\operatorname{RViab}_{T}^{(a)})\). If the claim is the weaker "loss of some formerly recoverable states," say that in words and keep \(\not\supseteq\), but drop "contraction."

---

## 4. Should fix

### S1. Three principle boxes differ from the canonical text [C] (§§6.13, 7.13, 8.13)

**Evidence.** Appendix A reproduces all five Biology principles verbatim from *Foundations*. The boxes in the main text do not, for three of them (B6):

- CU-B1, §6.13: "The degree and kind of autonomy **must be assessed** relative to" where the canonical text has "Degree and kind of autonomy **are** relative to."
- CU-B2, §8.13: "The degree **of agency** must be established" where the canonical text has "Degree must be established."
- CU-B3, §7.13: "is **biologically** explanatory" where the canonical text has "is explanatory."

The CU-B4 and CU-B5 boxes match. The changes are small, but the first one is substantive: "must be assessed relative to" is a method rule, while "are relative to" is a claim about autonomy.

**Recommended revision.** Make each box verbatim with the *Foundations* registry. Recorded as issue #32, because the same drift may exist in the other domain papers.

### S2. The status labels use two schemas [C][S] (§§4.10, 6.13, 7.13, 8.13, 9.17; Appendix A; issue #6)

**Evidence.** The section boxes label each principle with something close to the *Foundations* authority class: "[Domain-authority bridge principle]" for B1, B3, and B5, and "[Domain-authority conditional empirical claim]" for B2 (B6). But the B4 box reads "[Domain-authority conditional empirical generalization]," which joins the authority class to the claim status. In Appendix A, four principles have "Status: Domain Authority," which is an authority class, while B4 alone has a claim status. *Foundations* gives each principle both fields: B1, B3, and B5 are "canonical bridge principle," B2 is "canonical–conditional empirical hypothesis," and B4 is "canonical–conditional empirical generalization."

**Recommended revision.** Give every principle both fields, in both places, using the *Foundations* values: for example, "Authority: domain-authority bridge principle. Status: canonical bridge principle." This is a local instance of issue #6.

### S3. The Contents title of Section 9 does not match the heading [C] (Contents; §9)

**Evidence.** The Contents lists "9. Evolution, Constraint, and Major Transitions"; the heading reads "Section 9. Evolution, structured possibility, and major transitions" (B9). The heading reflects the v0.10 revision, which replaced "constraint" with **structured evolutionary possibility** as the section's organizing idea. Headings also use sentence case where the Contents uses title case, in every section except 13.

**Recommended revision.** Change the Contents entry to "Evolution, Structured Possibility, and Major Transitions," and use one capitalization style for headings and Contents.

### S4. A profile cannot be "less than zero" [I] (§9.16)

**Evidence.** The section writes \(\Delta W_i > 0,\ \Delta \mathbf C_j < 0\), where \(\mathbf C_j\) is a coherence profile. A vector inequality is undefined unless its order is stated, and the paper's own position (§§2.6, 5.5) is that profiles are compared by Pareto dominance and are often incomparable. The display also uses indices \(i\) and \(j\) after introducing levels as \(\ell\).

**Recommended revision.** Write the claim in the paper's own terms: "\(\Delta W_i > 0\) while \(\mathbf C_j\) after the change is Pareto-dominated by \(\mathbf C_j\) before it, or declines on a protected coordinate," with \(i, j\) declared as levels.

### S5. Six dimensions of individuality, seven components in the profile [C] (§§4.2–4.3)

**Evidence.** Section 4.2 announces "at least six dimensions" and gives six subsections (boundary, metabolic, regulatory, reproductive, evolutionary, historical). The profile \(\mathbf I_B\) in §4.3 has seven components; the extra one, \(I_C\) for conflict mediation, has no subsection (B8). Conflict is discussed later, in §4.8.

**Recommended revision.** Add a short §4.2.7 on conflict mediation that points forward to §4.8, and change "six" to "seven."

### S6. Several symbols mean unrelated things [C] (§§2.7, 3, 6.2, 7.7, 8.9, 9.4, 9.14, 11.3)

**Evidence (B8).**

- \(\mathcal U\) is the admissible intervention class (§2.7), the set of control functions (§3.3), the set of policies (§7.7), and the history-update map (§3.15, and \(\mathcal U_k\) in §9.14).
- \(\mathcal D\) is the disturbance class (§§2.7, 3.4) and the genotype–phenotype map \(\mathcal D_{h,e}\) (§9.4).
- \(\mathcal A\) is an invariant set (§3.13) and \(\mathcal A_T\) the viable adaptation set (§3.10). \(\mathcal V\) is the value of information (§8.9) and the variation map (§9.4).
- The autonomy-transition profile \(\mathbf A_P = (B,E,K,R,H,V,X)\) (§6.2) reuses all seven letters of the system tuple \((X,E,U,F,K,G,R,H,\pi,T)\) and the viability region \(V\), with different meanings.
- Externally supplied costs are \(J_{\mathrm{imported}}\) in §5.6 and \(J_{\mathrm{ext}}\) in §11.3.

None of these produces a wrong result, but a reader working across sections will misread several displays.

**Recommended revision.** Rename the history-update map (for example \(\Phi_H\)), the genotype–phenotype map (\(\mathcal G_{h,e}\)), and the variation map (\(\mathcal M\)). Give the components of \(\mathbf A_P\) subscripted names (\(a_{\mathrm{bdry}}, a_{\mathrm{energy}}, \ldots\)). Use \(J_{\mathrm{imported}}\) in §11.3.

### S7. "E1" names both an evidence grade and a prediction [C] (§§9.18, 12.13)

**Evidence.** Section 9.18 labels six evolutionary predictions E1–E6. Section 12.13 labels five evidence grades E0–E4 (B8). "E2" therefore means both "conflict-control threshold" and "single-system empirical support." No other paper defines evidence grades, so the collision is local.

**Recommended revision.** Rename the evidence grades (for example G0–G4) or the predictions (EV1–EV6, matching the PTH prefix of §10.13).

### S8. The paper's constructive formal results are not in the package [S] (Principal contributions 13; §§3.16, 7.14 D4, 12.6 P5, 12.14; Appendix C; issue #29)

**Evidence.** Contribution 13 says the paper "shows through two deterministic constructions" that one coupling law can reverse its viability effect. Sections 7.14 and 12.6 cite "Supplement B" for them, §3.16 says the supplement "proves several bounded propositions," and §12.14 refers to "the accompanying reproducibility package." None of this is in the RC3 package. The reference to "Supplement B" is also ambiguous, since the paper's own Appendix B is the revision table.

The qualitative claim is sound. An independent reconstruction (B2) produces both directions with the mean-conserving law \(\dot x_i = k(\bar x - x_i)\): coupling rescues a threatened component below the mean, and drains a high-floor component above it. But the specific constructions and any numerical thresholds cannot be checked.

**Recommended revision.** Either include the two constructions as a short Appendix D (each needs only a state vector, floors, and the coupling law), or reword contribution 13 and §3.16 so they describe the supplement rather than claim results for the paper. In either case, write "Technical Supplement B" so it cannot be confused with Appendix B.

### S9. Propagation residue [C] (§13.4; Domain Analytic Frame; issues #7, #9)

**Evidence.** Section 13.4 begins a sentence with lowercase "the Version 0.10 canonical registry records this synthesis" (B9; issue #7). The Domain Analytic Frame says "RC2 remains the frozen baseline" in an RC3 file (issue #9).

**Recommended revision.** Capitalize the sentence; resolve #9 with the global fix at RC3 approval.

---

## 5. Consider

**K1. The closure-core definition has a redundant clause [C] (§3.9).** A strongly connected subgraph with two or more nodes already gives every member an incoming and an outgoing edge; all 1,625 strongly connected digraphs on two to four nodes satisfy the clause (B3). The clause only matters for a single node, where it requires a self-loop. Say so, or drop the clause and add "with at least two members, or one member with a self-maintaining loop."

**K2. "The former product AI" (License summary).** In a corpus with an *Artificial Intelligence* paper, "AI" reads as the acronym. Write "the former product \(A\cdot I\)."

**K3. One sentence overstates Herrera-Álvarez et al. [S] (§9.5).** The paper says that "in both reconstructed maps" the inherited structure "causally steered evolution toward lineage-specific phenotypes that later evolved historically." In the source, the older map (AncSR1) biased outcomes toward *conserving* the ancestral specificity, and the younger one (AncSR2) favored the new specificity that actually evolved. Suggested wording: "The older map biased evolution toward conserving the ancestral specificity; the younger map favored the new specificity that later evolved."

**K4. Balance the *Stentor* summary [S] (§8.6).** The study's headline finding was a parallel with animals: the CaMKII inhibitor KN-93 reduced habituation as it does in metazoa. The paper's statement that the findings "do not show that the cell uses a metazoan memory mechanism" is fair, but a reader should also learn that one step looks conserved. One added clause would do it.

**K5. Add CU-T6 to Appendix A.9 [C].** *Foundations* lists CU-T5 and CU-T6 as the interpretations for CU-COM8; A.9 names only CU-T5 (B7).

**K6. Thermodynamic wording (§§5.1, 5.10).** In §5.1, entropy production is nonnegative for the *isolated* system-plus-environment, not the "closed" one. Item 1 of §5.10 ("without compensating matter, energy, or entropy exchange in a closed system") mixes the two senses; "in an isolated system" or "without compensating exchange with the environment" is clearer.

**K7. Editorial.** "Heaven–Earth" in §13.5 should be "Heaven≡Earth." Section 13.10 says "description register" and §13.14 "descriptive register"; pick one. The §10.12 heading names neurodiversity, which the body never mentions. Three reference pairs are out of alphabetical order: Aubin/Aoki, Rajan/Rader, and Rohner after Walker (B10).

**K8. The death definition leaves time unquantified (§10.10).** The display asks that \(x_t^i \in V_B\) with closure restored "for a sustaining interval," but does not say over which \(t\). Write "for all \(t \in [t_0, t_0 + \tau]\) for some \(t_0 \le T\)," and note that \(\mathcal I\) here plays the role \(\mathcal U\) plays in §2.7.

---

## 6. Relation to the issue log

- **#6 (status vocabulary).** S2 adds a clear local case: authority class and claim status are mixed across the five principles.
- **#7 (find-and-replace artifacts).** One more instance (S9). Separately, a sentence-initial regex finds about 51 lowercase "this paper" in *Consciousness* and about 11 in *Artificial Intelligence*, more than the log records (about 20 and 1). Confirm at those audits.
- **#9 (RC2 baseline).** Confirmed in *Biology*.
- **#19 (dependency tables).** *Biology* has none (B7).
- **#22 (register definitions).** *Biology* does not define the registers itself; it defers to M&E (§1.7), and its §13 register note is use-based. No change beyond the M&E fix and K7.
- **#23 (citation practice).** *Biology* joins *Physics* as a model, and does slightly better: no unused entries.
- **#25 (digit-stripping).** None in *Biology*.
- **#29 (supplements).** Extended to *Biology* (S8).
- **New #31.** *Foundations* gives CU-B4 the status "canonical–conditional empirical generalization," but its research-status boundary list calls it "a conditional empirical synthesis." *Biology* follows the status field. Align the boundary line (C).
- **New #32.** Principle boxes in domain-paper sections can drift from the canonical registry text even when the paper's appendix is correct (S1). Check the box-versus-registry wording in the remaining domain papers (S).

The `$\mid$` and delimiter problem (M1) is confined to *Biology*, so it is not logged as a corpus issue.

---

## 7. Standing caution

Every finding here concerns internal coherence, formal correctness, or sourcing. The results that pass are correct statements about declared models: viability kernels, a two-state Markov chain, a three-component coupling law. The paper itself says that its scientific value "will depend on whether these variables improve explanation and prediction beyond established models," and §12 sets out the experiments that would decide that.

Passing this audit does not move that question. A clean formal record makes the program easier to test; it is not itself a test.
