# CU v0.10 Audit 06: Psychology

**Reviewer:** Claude (Opus 5.5)
**Date:** 7 October 2026
**Text audited:** `06_CU_Psychology_v0.10_RC3_Methodological_Spine_Propagation_Draft.md` (19,258 words), from the RC3 Methodological Spine Propagation Working Package (SHA-256 `23409d05…1c3a`, verified)
**Comparison texts:** *Foundations* (02), especially the Psychology registry (CU-Ψ1–Ψ12), CU-COM10, and the 64-stage table; *Consciousness* (05) for the definition of ego; *Denying Knowledge* (10) for the §6.8 cross-reference; the corpus issue log
**Reproducibility:** `cu_ps_audit_checks.py`. Every [C] finding cites its check number (Y1–Y9).
**Status:** Advisory. This audit assesses internal coherence, formal correctness, and sourcing. It is not a clinical review and is not evidence that CU's account of psychological life is correct (see §7).

---

## 0. Conventions and coverage

The audit uses the seven-check protocol and the labels of the earlier audits. **[S]** marks a finding that is source-supported, **[C]** one computed or checked by the reviewer and reproduced by the script, and **[I]** reviewer inference.

**Coverage.** The paper was read in full: front matter and the Domain Analytic Frame, §§1–15, Appendices A–C, and the references. Whole-paper scans covered identifiers, principle titles, statuses, and statements against *Foundations*, citations against references, and propagation artifacts.

**Sources.** The paper cites 62 works. Three were checked by search because they are recent and carry specific empirical claims: Clamor, Lincoln, and Schulze (2026), Crompton et al. (2025), and Salkovskis, Sighvatsson, and Sigurdsson (2024). The others are standard works or recent reviews whose use is general, and were checked for bibliographic form only.

**A correction to the handoff.** The handoff mentioned CU-Ψ1–Ψ7. *Psychology* and *Foundations* both define twelve principles, CU-Ψ1–Ψ12, and all twelve were checked.

---

## 1. Summary

*Psychology* is the most carefully sourced paper audited so far. Every one of its 62 references is cited in the text, and every in-text citation has an entry (Y9). That is better than *Physics* and *Biology*. The three recent sources checked exist and are described accurately; in particular, the paper reports the failed replication of the double-empathy transfer result in Crompton et al. (2025) rather than citing only the earlier positive study. Claim discipline is strong throughout. Section 1.4's seven "conceptual prohibitions" set the tone, and nearly every clinical topic is handled by separating constructs (difference, disability, distress, disorder) and naming the evidence each needs. There are no lowercase "this paper" artifacts.

The formal content is light and correct: weak dominance, purpose-bound scalarization, and integration overload as non-membership in a capacity region. The horizon reversal the abstract describes can be reproduced in a simple reconstruction (Y1, Y2). All 24 identifiers resolve, the Mandala stages and CU-COM10 match *Foundations* exactly, and every principle's claim status matches the registry (Y4–Y6).

One item must be fixed.

- **None of the twelve principle statements matches the *Foundations* registry [C].** Appendix A calls its statements "the controlling CU formulations." *Foundations* presents its own registry as synchronized with the domain papers. The two differ in every case, and two differences are substantive: the *Foundations* version of CU-Ψ6 includes the "affected person" among the things a local gain can undermine and *Psychology*'s omits it, and the *Foundations* version of CU-Ψ1 requires coordinates and dimensionality to be declared while *Psychology*'s does not (M1).

The should-fix items are small. Section 2.3 announces "five forms" of meaning map and lists six (S1). The abstract describes an illustrative model, and Appendix C describes "fifteen governance rules," neither of which is in the paper (S2). The paper's paraphrase of the *Consciousness* definition of ego changes its content (S3). And the in-text citation "(Rader, 2026)" cannot be resolved, because six reference entries share that author and year (S4).

**Totals:** 1 must fix, 5 should fix, 6 to consider.

---

## 2. Verified correct

| Item | Check | Result | Label |
|---|---|---|---|
| Identifiers cited | Y4 | 24 distinct; all resolve; all titles match *Foundations* (CU-Ψ6 differs only in hyphen versus en dash) | [C] |
| CU-Ψ1–Ψ12 claim statuses | Y5 | 12 of 12 match the *Foundations* claim/candidate status | [C] |
| Mandala stages 16–21 (Appendix A.1) | Y6 | All six titles identical | [C] |
| CU-COM10 statement, boundary, and revision condition (§14) | Y6 | Identical to *Foundations* | [C] |
| CU-COM14, COM15, COM16, COM17, COM19 titles | Y4 | Identical to *Foundations*; the COM17 title is the *Foundations* form, not the variant flagged in *Ethics* (#5) | [C] |
| Weak dominance and purpose-bound scalarization (§§2.4.1–2.4.2) | Y2 | Two non-dominated nine-coordinate profiles reverse under two weightings | [C] |
| Horizon reversal between suppression and supported engagement (abstract; Appendix C) | Y1 | Reconstructed: suppression preferred under a short, comfort-weighted horizon; engagement under a long, function-weighted one | [C] |
| Nine-coordinate profile (§2.4; Frame row 11) | Y3 | Nine coordinates, as stated | [C] |
| Citations | Y9 | 62 of 62 entries cited; every in-text citation has an entry | [C] |
| "The two widows" in *Denying Knowledge* (§6.8) | read | Present in *Denying Knowledge* | [C] |
| Clamor, Lincoln, and Schulze (2026), *Psychological Bulletin* 152(2) (§4.2) | search | Exists; transdiagnostic regulation difficulties with disorder-specific profiles, as described | [S] |
| Crompton et al. (2025), *Nature Human Behaviour* registered report (§8.3) | search | Exists (N = 311); no mixed-chain transfer deficit; lower rapport and a disclosure effect, as described | [S] |
| Propagation artifacts | Y8 | No lowercase "this paper," no "Version Version," no digit-stripping | [C] |

---

## 3. Must fix

### M1. No principle statement matches the Foundations registry [C] (Appendix A; *Foundations* Psychology registry; issue #32)

**Evidence.** Appendix A.1 says its twelve principles "are the controlling CU formulations for Psychology." *Foundations* reproduces a registry entry for each, under the heading "Domain source: *Coherence Universalism: Psychology*, Version 0.10." Titles and claim statuses agree. The statements do not: none of the twelve is identical, and word-level similarity ranges from 0.50 to 0.82 (Y5). The *Foundations* entries are mostly condensed versions of the *Psychology* text, but two differences change content.

- **CU-Ψ6.** *Foundations*: a pattern may undermine "another subsystem, wider context, **affected person**, or longer horizon." *Psychology*: "another subsystem, wider context, or longer horizon." The omission matters in a paper whose §1.4 forbids individualizing harm and whose CAP record requires affected-person scope.
- **CU-Ψ1.** *Foundations*: "Its coordinates and dimensionality **must be declared**." *Psychology* says only that "no universal dimensionality or fixed axis set is assumed," which removes the declaration requirement.

Three principal failure modes also differ by a word or two (Ψ2, Ψ10, Ψ12).

*Biology* (Audit 04) shows the alternative: its Appendix A is verbatim with *Foundations* in all five cases.

**Recommended revision.** Decide which text is controlling and make the other verbatim. The authority hierarchy points to the domain paper as source, which would mean updating *Foundations* to the *Psychology* wording. In that case, first restore "affected person" to Ψ6 and the declaration requirement to Ψ1 in *Psychology*, since both are improvements the condensed versions introduced. This is the same drift recorded in issue #32, now at registry level.

---

## 4. Should fix

### S1. "Five forms" of meaning map, six listed [C] (§2.3)

**Evidence.** Section 2.3 says "At least five forms should be distinguished" and lists six: propositional, predictive, affective, embodied, narrative and social, and commitment maps (Y3).

**Recommended revision.** "At least six forms."

### S2. The abstract and Appendix C describe material that is not in the paper [C] (abstract; Appendix C; issue #29)

**Evidence.** The abstract says "an illustrative model demonstrates a horizon-sensitive reversal between immediate suppression and supported engagement under declared assumptions." The model appears nowhere in §§1–15 (Y8); only Appendix C describes it, and it is in the technical supplement, which is not in the package. Appendix C also lists "the twelve-principle registry and fifteen governance rules." The paper contains seven numbered prohibitions (§1.4) and a one-paragraph claim-governance summary (A.14), but no list of fifteen rules (Y3).

The reversal itself is sound and easy to exhibit (Y1).

**Recommended revision.** Either add a short paragraph to §2.6 that states the model's two horizons and two weightings and reports the reversal, or change the abstract to "an illustrative model in the technical supplement." Bring Appendix C's count of governance rules into line with what the paper contains, or include the fifteen rules.

### S3. The paraphrase of the Consciousness definition of ego changes it [C] (§5.2)

**Evidence.** Section 5.2 says "Consciousness v0.10 defines ego as a persistent regime that treats the continuation, status, narrative, resources, or authority of a modeled self as an object of defense." *Consciousness* §2.3 actually defines ego as "a persistent self-maintaining organization that treats the continuation, status, integrity, or narrative of a modeled self as an object of defense" (Y7). The paraphrase drops "self-maintaining" and "integrity" and adds "resources" and "authority." The added terms come closer to *Consciousness* §5.9 and the *Non-Egoic* paper, but the sentence attributes them to a definition that does not contain them.

**Recommended revision.** Quote *Consciousness* §2.3 exactly, or write "Consciousness v0.10 treats ego as…" and cite §5.9.

### S4. "(Rader, 2026)" cannot be resolved [C] (§6.8; References; issue #23)

**Evidence.** The reference list has six entries for Rader (2026) with no year suffixes. The one in-text use, "(Rader, 2026)" for *Denying Knowledge* in §6.8, could refer to any of them. *Consciousness* has the opposite problem, a single "2026f" suffix (Audit 05 S4).

**Recommended revision.** Adopt one corpus-wide convention for the series: either suffixes assigned in a fixed order (for example, a = M&E, b = *Foundations*, …), or short-title citation such as "(*Denying Knowledge*, Rader 2026)."

### S5. Status fields use one schema where Foundations uses two [C] (Appendix A; issue #6)

**Evidence.** Each Appendix A entry gives a "Candidate status" that matches the *Foundations* claim/candidate status (Y5). *Foundations* also gives each an authority class (for example, CU-Ψ8 and CU-Ψ12 are "domain-provisional clinical / social bridge," the rest "domain-authority"), which *Psychology* omits. That distinction is the one that tells a reader how settled the domain itself considers the principle.

**Recommended revision.** Add the authority class to each entry, as recommended for *Biology* (Audit 04 S2). Also remove the "RC2 remains the frozen baseline" line under issue #9.

---

## 5. Consider

**K1. The counterfactual clause of the self-deception definition (§5.6).** Component 4 says the pattern "would change if the same evidence supported the preferred conclusion." If the evidence supported the preferred conclusion, there would be nothing to deceive oneself about. The intended test is probably symmetry: whether the same standards would be applied if the same quality of evidence bore on a non-protected conclusion. Suggest "the person would apply different standards to equally strong evidence bearing on a conclusion in which they had no stake."

**K2. Some profile coordinates may not be monotone (§2.4.1).** Weak dominance assumes that more is better on every coordinate. The paper itself says flexibility "does not mean endless openness" (§4.3), and agency and narrative integration can also be excessive in the senses §§5.4–5.5 describe. Either state that each coordinate is scored so that higher is better for the declared purpose, or note that dominance applies only to coordinates with that property.

**K3. The Salkovskis year [S].** The entry gives 2024 with *Behavioural and Cognitive Psychotherapy* 51(6). The journal's volume 53 is 2025, so volume 51 is 2023. Confirm the year against the issue.

**K4. Notation.** The profile coordinate \(G_a\) (agency) sits beside \(G\), the relational organization in the model tuple, and \(F_r\) beside the dynamics \(F\). The meaning space \(\mathcal M_\Psi\) of CU-Ψ1 does not appear in §2.2, which defines the same object without a symbol. None of these causes an error, but aligning them would help.

**K5. Typography for Foundations.** *Foundations* writes the CU-Ψ6 title with hyphens ("Local-Global and Short-Long"), while CU-M13 and *Psychology* use en dashes (Y4).

**K6. Formatting.** The Contents is a bulleted list of numbered items ("- 1. …"), unlike the other papers, and §12 ends with two consecutive horizontal rules (Y8).

---

## 6. Relation to the issue log

- **#6 (status vocabulary).** S5: one schema used where *Foundations* uses two.
- **#9 (RC2 baseline).** Confirmed.
- **#19 (dependency tables).** None in *Psychology*.
- **#22 (register definitions).** *Psychology* uses the registers by function (§3.6 distinguishes descriptive and commitment contents inside one meaning map) and defers definitions to M&E. No change needed here.
- **#23 (citation practice).** *Psychology* is now the model: 62 of 62 entries cited, no citation without an entry. The unsuffixed "Rader (2026)" is a corpus-wide convention problem (S4).
- **#29 (supplements).** Extended: the horizon-reversal model and the "fifteen governance rules" (S2).
- **#32 (principle drift).** Extended from section boxes to the registry itself: all twelve *Psychology* statements differ from *Foundations*, two substantively (M1). The *Foundations* registry entries for each domain should be checked against their domain appendices in the remaining audits.
- **New #35.** Self-citation convention: six or more Rader (2026) entries per paper, cited without suffixes (*Psychology*) or with a stray suffix (*Consciousness*). Adopt one convention for the series (S4).

---

## 7. Standing caution

Every finding here concerns internal coherence, formal correctness, or sourcing. The paper's own standard for itself is that the framework "earns value only if its declared profile and horizon improve measurement, case formulation, or prediction over existing approaches." This audit cannot test that, and the paper says plainly that it is not a clinical tool.

Passing this audit does not show that the profile architecture improves on the constructs it translates.
