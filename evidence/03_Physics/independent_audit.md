# CU v0.10 Audit 03: Physics

**Reviewer:** Claude (Opus 5.5)
**Date:** 6 October 2026
**Text audited:** `03_CU_Physics_v0.10_RC3_Methodological_Spine_Propagation_Draft.md` (51,897 words), from the RC3 Methodological Spine Propagation Working Package (SHA-256 `23409d05…1c3a`, verified)
**Comparison texts:** *Foundations* (02), especially Part VI (Physics Constraint Registry); *Metaphysics and Epistemology* (01); the corpus issue log
**Reproducibility:** `cu_ph_audit_checks.py`. Every [C] finding cites its check number (P1–P8).
**Status:** Advisory. This audit assesses internal coherence, formal correctness, and sourcing. It is not evidence that CU's physical program describes nature (see §8).

---

## 0. Conventions and coverage

The audit uses the seven-check protocol and the labels of Audits 01 and 10. **[S]** marks a finding that is source-supported, **[C]** one computed or checked by the reviewer and reproduced by the script, and **[I]** reviewer inference.

**Coverage.** Because the paper is about 52,000 words, the audit was weighted toward the load-bearing mathematics and the claim-status passages. The following were read closely and checked: the abstract and principal contributions; §1.5–1.9; all of §3 (the classical sandbox); §4.11–4.13; §6.2–6.7 and §6.10; §7.6–7.13; the stress-energy, lattice, horizon, and Jacobson passages of §§7–10; §13; §14.1; and Appendices A.5, B, and C. Whole-paper scans covered claim verbs, citations against references, identifiers, cross-paper labels, and propagation artifacts. The remaining sections were not read line by line: §2, §4.1–4.10, most of §5, §6.8–6.17 apart from §6.10, §7.1–7.5, §8.3–8.14, §9.3–9.14, §10 apart from §10.3, §11, and §12. A future pass could cover them, but nothing in the scans suggested a problem there.

As the handoff instructed, the §3.13.3 fixed-coupling results were carried forward from the earlier session and not rederived.

---

## 1. Summary

*Physics* is the most formally substantial paper in the corpus, and it is in very good condition. Every load-bearing mathematical claim the audit checked is correct. That includes the exact constants in the abstract: all three global Fisher-field bounds of §3.13.2 reproduce to twelve digits, the closed form 23/128 + 11√33/384 is exact, and the claim that the joint-growth wedge collapses exactly on two-level states is confirmed. Its claim discipline is the best in the corpus. Fourteen explicit non-claims in §1.9, a status label at every load-bearing step, and careful attribution (the GE(2) decomposition to Shorrocks, the Madelung equivalence to standard sources, Jacobson's assumptions listed in full) leave very little to correct. It is also the only paper so far with complete author-date citation: no in-text citation lacks a reference entry.

There are **no must-fix items.**

The should-fix items are minor. Two concern open items in the issue log, and the audit's findings change how both should be closed.

- **Issue #4 is an apparent conflict, not a real one [S][I].** *Physics* §13.9 says the account does not license "a universal coherence gradient in nature." *Physics* §13.7.1, in the same paper, licenses "Universal Coherence Gradient" as interpretive shorthand, exactly as *Foundations* CU-T11 does. The two are compatible: §13.9 forbids a literal gradient, and §13.7.1 permits a figure of speech. Adding one word to §13.9 ("a *literal* universal coherence gradient in nature") closes the issue. The severity should drop from M to S.
- **Issue #3 is best closed in *Physics* itself [C][S].** The twelve PHYS-A6 constraints in *Foundations* Part VI each match a conclusion this paper actually reaches. But the paper never uses the identifiers, so readers cannot trace them. A crosswalk table in Appendix A.5 would close #3 together with the stage-mismatch correction of Audit 01 M5.

**Totals:** 0 must fix, 8 should fix, 6 to consider.

---

## 2. Verified correct

| Item | Check | Result | Label |
|---|---|---|---|
| §3.3, §3.5 worked examples | D and S values for six distributions | All correct | [C] P1 |
| §3.7 Euclidean opposition | 𝒜_E = −2J(p, u), Jeffreys divergence | Correct (2,000 random states, error < 10⁻¹²) | [C] P1 |
| §3.8 rates and joint-growth wedge | Interval exists iff gradients not antiparallel | Correct (Cauchy–Schwarz) | [I] |
| §3.9 exact Euler step | ΔD = h[α‖a‖² − βΠ_E] + h²‖v‖² | Correct | [C] P1 |
| §3.10 feasibility | \|b_i\| ≤ log(1/ε) on the band; β bound algebra; sup‖a‖ = √3 | Correct; bound is conservative (max ratio 0.74) | [C] P4 |
| §3.11 coarse-graining | Between/within identity; Shannon grouping; KL gain; per-block forms; general N; GE(2) rescaling; §3.11.7 example | All correct; Shorrocks (1980) attribution appropriate | [I] |
| §3.12 Fisher gradients | A, B, ‖A‖², ‖B‖², 𝒜_F = −2Cov_p(p, log p) | Correct | [C] P1 |
| §3.13 gradient-flow consequence | No recurrent cycle for fixed α, β | Correct | [I] |
| §3.13.2 global bounds | ‖A‖_F 0.586724197682…, ‖B‖_F 1.011677099863…, Π_F 0.586672264109…, closed form, root equations | Reproduced; 200,000 random points including faces never exceed them | [C] P3 |
| Abstract, §3.14.2 two-level wedge theorem | Collinear iff at most two distinct values; k and r_c; edges → ½ near uniform | Correct | [C] P2 |
| §3.13.3 fixed coupling | q\*, r\*, threshold at ½, cubic expansion, bistability | Carried forward (verified earlier session) | [S] |
| §4.11 conservative accessibility flow | D conserved, D̄ nonincreasing, H_π nondecreasing | Confirmed by simulation; "conditional on a directed law" correctly stated | [C] P5 |
| §6.2, §6.6, §6.7 quantum examples | Excess purity = D for diagonal states; linear entropy ½sin²2θ; concurrence sin 2θ; CNOT conversion C_r = E = h₂(sin²θ) | All correct | [C] P6 |
| §6.10 recoverability | Junge et al. (2018) bound with unsquared fidelity and σ-dependent recovery map | Correctly stated | [I] |
| §7.6 overdamped expansion | q̇ = η⁻¹F − η⁻³∇_F F + O(η⁻⁵); O(η⁻²) rest-initialization slip | Correct; the paper's own correction of its earlier −1.87 slope is right | [I] |
| §7.9 lattice dispersion | ω² = 4κ_lat sin²(kℓ/2); κ_lat = 2κ convention | Correct | [I] |
| §7.11 Madelung derivation | Variation of the Fisher term equals the quantum potential | Confirmed symbolically | [C] P6 |
| §8 shortest-path metric | Positive symmetric costs on a connected graph give a metric; zero costs a pseudometric | Correct | [I] |
| §9.2 stress-energy tensor | Standard form for the given action (mostly-plus signature) | Correct | [I] |
| §9.6, §10.3 imported formulas | Unruh temperature; Bekenstein–Hawking entropy; Jacobson assumptions | Correctly stated and attributed | [I] |
| §5.10 CDP reconstruction | "Five informational axioms" plus purification | Correct count | [I] |
| Citations | Every parenthetical citation has a reference entry | No missing entries | [C] P7 |
| Reference list | Bibliographic details of most entries | Consistent with standard records (reviewer knowledge; all pre-2026) | [I] |
| Cross-paper | M&E §3.7 and §4.4 describe the block-averaging result accurately | Consistent | [S] |
| Cross-paper | *Foundations* PHYS-A6.1–A6.12 each match a conclusion of this paper | Consistent in content | [S] |
| Appendix A.5 | Stages 1–10 listed with canonical titles | Matches M&E and *Foundations* | [C] P8 |

---

## 3. Must fix

None.

---

## 4. Should fix

### S1. Close issue #4 with one word [S][I] (§13.9)

Section 13.9 lists "a universal coherence gradient in nature" among the things the account does not license. Section 13.7.1 of the same paper says "The phrase **Universal Coherence Gradient** is therefore interpretive shorthand for recurrent domain-relative directionality. It is literal only inside a declared model." *Foundations* CU-T11 says the same.

Read together, the two sections are consistent: one forbids a literal gradient running through nature, and the other licenses a figure of speech. Read alone, §13.9 appears to forbid what §13.7.1 permits, which is what the original issue-log entry recorded. **Recommended revision:** "a literal universal coherence gradient in nature (see §13.7.1 for the licensed interpretive shorthand)." Issue #4 can then close, and its severity should be recorded as S rather than M.

### S2. Add a PHYS-A6 crosswalk to Appendix A.5 [C][S] (Appendix A.5; issue #3)

*Foundations* Part VI defines PHYS-A6.1–A6.12 as "the physical conclusions every downstream paper must respect." Each is a faithful summary of a conclusion this paper reaches. For example, PHYS-A6.4 ("Temporal order is not temporal direction") is §4.8, and PHYS-A6.11 ("Horizon entropy is reduced-description entropy") is §10. But *Physics* never mentions the identifiers [C, P8]. Appendix C says the "full claim and principle crosswalk" is in the technical supplement, which the package does not contain.

**Recommended revision.** Add a twelve-row table to Appendix A.5 mapping each PHYS-A6 identifier to the section that establishes it. Combined with Audit 01 M5 (reassigning the identifiers in the Mandala stages by content rather than position), this closes issue #3.

### S3. Align the §1.5 ladder with Appendix A.5 [C][S] (§1.5; issue #21)

Appendix A.5 lists stages 1–10 with their canonical titles. Section 1.5, the paper's own statement of "the Coherence Ladder in the physical domain," uses different labels for several rungs. Rung 3 is "Comparative gradients among configurations" rather than "Domain-Relative Coherence Directions"; rung 8 is "Directed entropy production and thermodynamic time" rather than "Entropy and Accessibility" [C, P8]. Rungs 5 and 6 also differ in wording.

The differences are partly substantive. Stage 8's canonical title deliberately avoids the claim that entropy production yields thermodynamic time, which §4.8 of this paper shows needs further assumptions. Of the three physical sequences recorded in issue #21, *Physics* §1.5 is closest to the canonical one; M&E §13.3 remains the outlier.

**Recommended revision.** Use the canonical stage titles in §1.5, or add a column giving them. Separately, note that quantum theory, the subject of two of the paper's longest sections, has no rung or stage. That is a choice the paper should state rather than leave implicit.

### S4. The mathematical thesis is labelled "[Derived]" [S][I] (§1.7.2)

Section 1.7.2 labels as "[Derived]" the claim that information-geometric state spaces "provide a common mathematical vocabulary" for six things, including "transfer between accessible and inaccessible structure." The first five are established features of the mathematics the paper imports. The sixth is not derived: §3.11.8 says explicitly that the static decomposition "does not imply that an arbitrary trajectory transfers differentiation into entropy," and §4.11 obtains transfer only conditionally on a chosen directed law.

**Recommended revision.** Relabel the thesis "[Imported mathematical observation]," or keep "[Derived]" and qualify the sixth item as "transfer, under a specified directed law (§4.11)."

### S5. The symbol A means two different things [S] (§3.12, §4.11, §7.7)

Section 3.12 defines A := grad_F D, and §7.7 uses it the same way. Section 4.11 reuses A for grad_F(D̄ ∘ π), the gradient of *coarse* differentiation, and calls the gradient of D "N." A reader moving from §3 to §4.11 will misread the flow. **Recommended revision:** rename the §4.11 field, for example to Ā or G.

### S6. The technical supplement and code repository cannot be reached [S] (Appendix C; References; issue #29)

Appendix C describes a technical supplement holding complete proofs, numerical reproduction records, the independent audit, and deterministic source code. The reference list cites "Heaven≡Earth Foundation. (2026). *Coherence Field Verification* [Computer software repository]. GitHub," with no URL. Neither is in the RC3 package. This audit's independent checks reproduce every result it examined, so nothing here depends on the supplement. But a paper whose principal contribution 14 promises "a deterministic code-and-data record for independent checking" should give the reader a way to reach it. **Recommended revision:** add the repository URL and a version tag or commit hash, and include the supplement in the release package.

### S7. Propagation artifact [C] (§13.7.1; issue #7)

Section 13.7.1 begins with a lowercase "the Version 0.10 canonical registry" [C, P8], the same artifact found in *Denying Knowledge* §13.4.

### S8. Eight references are never cited [C] (References)

Amari (1998), Ay et al. (2017), Connes and Rovelli (1994), Hardy (2001), Jaynes (1957), Masanes and Müller (2011), Schlosshauer (2007), and Wilde (2017) appear in the reference list but nowhere in the body [C, P7]. Several are obviously relevant (Hardy and Masanes–Müller to §5's reconstruction programs, Schlosshauer to §6.8), so the fix is more likely to add citations than to delete entries.

---

## 5. Consider

**K1. State the metric signature.** The §9.2 action and stress-energy tensor are correct for the mostly-plus signature (−, +, +, +), but the paper does not say so. One clause would remove the ambiguity.

**K2. Cite the published version of Lê.** Lê (2016) is cited as an arXiv preprint; the paper was published in *Annals of the Institute of Statistical Mathematics* (2017).

**K3. Fix reference-list order.** Theil (1967) sits between Streltsov and Susskind.

**K4. Drop the self-citation.** The *Physics* paper lists itself in its own "CU corpus" references.

**K5. Remove the duplicated horizontal rule** after the Principal contributions list.

**K6. Consider promoting the §1.9 list.** The fourteen explicit non-claims of §1.9 are the clearest statement of scope anywhere in the corpus. Other papers could adopt the format, and *Foundations* could point to it as a model.

---

## 6. Relation to the issue log

- **#3 (PHYS-A6 identifiers).** The constraints match this paper's conclusions in content. Close by adding the crosswalk (S2) and reassigning the stage identifiers in M&E and *Foundations* (Audit 01 M5).
- **#4 (universal coherence gradient).** An apparent conflict between §13.9 and §13.7.1. Close with S1; record severity as S.
- **#7 (find-and-replace artifacts).** One more instance (S7).
- **#21 (physical sequences).** *Physics* §1.5 differs from its own Appendix A.5 at rungs 3, 5, 6, and 8; quantum theory has no stage (S3).
- **#23 (citation practice).** *Physics* is the model: complete in-text citation, eight unused entries.
- **#29 (supplements).** Extended to *Physics* Appendix C and the GitHub reference (S6).

---

## 7. A note on what the paper achieves

Audits mostly record what is wrong, so it is worth recording plainly what this one found. Every formal result the audit tested reproduced, most to machine precision. The paper's habit of saying exactly what a result does and does not show (the conservative flow "does not derive the direction from geometry alone," the Madelung equivalence "does not show that the Fisher term follows uniquely," Jacobson's route "establishes structural compatibility, not a first-principles derivation") is the claim discipline the rest of the corpus aims at. Where earlier versions overreached, Appendix B records the retreat openly.

---

## 8. Standing caution

Every finding here concerns internal coherence, formal correctness, or sourcing. The results that pass are correct mathematics about declared models: a four-state simplex, chosen functionals, chosen actions, and imported theorems. The paper itself says that these "concern differentiation, entropy, and accessibility—not yet substantive physical coherence," and that whether the architecture is physically fundamental "depends on … novel empirical consequences that distinguish CU from a unifying reinterpretation of existing mathematics."

Passing this audit does not move that question. A clean formal record makes the program easier to test; it is not itself a test.
