# CU v0.10 Audit 07: Social Dynamics

**Reviewer:** Claude (Opus 5.5)
**Date:** 7 October 2026
**Text audited:** `07_CU_Social_Dynamics_v0.10_RC3_Methodological_Spine_Propagation_Draft.md` (19,823 words), from the RC3 Methodological Spine Propagation Working Package (SHA-256 `23409d05…1c3a`, verified)
**Comparison texts:** *Foundations* (02), especially the Social Dynamics registry (CU-S1–S5, CU-ICF, CU-Inst, CU-EC, CU-CL), CU-COM11, CU-COM18, and the 64-stage table; the corpus issue log
**Reproducibility:** `cu_sd_audit_checks.py`. Every [C] finding cites its check number (Z1–Z9).
**Status:** Advisory. This audit assesses internal coherence, formal correctness, and sourcing. It is not evidence that CU's social account is correct or that any political arrangement it favors is better (see §7).

---

## 0. Conventions and coverage

The audit uses the seven-check protocol and the labels of the earlier audits. **[S]** marks a finding that is source-supported, **[C]** one computed or checked by the reviewer and reproduced by the script, and **[I]** reviewer inference.

**Coverage.** The paper was read in full except §§8–12, which were read for their claims and citations with list items skimmed. Whole-paper scans covered identifiers, principle statements and statuses against *Foundations*, the two lists of governance rules, citations, notation, and propagation artifacts.

**Sources.** Two recent sources carrying specific empirical claims were checked by search: Gauthier et al. (2026) on X's feed algorithm and the V-Dem *Democracy Report 2026* (Nord et al., 2026). The remaining references are standard works or reports whose use is general.

---

## 1. Summary

*Social Dynamics* is in good condition and has no must-fix items. Its formal content is small and correct: the §2.3 construction showing that a higher mean can coexist with a floor violation checks exactly (Z1). Its conceptual discipline is the paper's main strength. It keeps coordination, consent, legitimacy, trust, and trustworthiness apart throughout, insists on distribution before aggregation, and states plainly in §14.6 what it does not establish. Its empirical reporting is careful: the two sources checked are described accurately, including the asymmetry in the X experiment (switching the algorithm on shifted attitudes, switching it off did not).

Cross-paper agreement is exact where it matters. All 25 identifiers resolve. The five CU-S principles appear verbatim in both §14.4 and Appendix A and match the *Foundations* registry, as do CU-CL12, CU-COM11, and CU-COM18 (Z4). The paper's two lists of nineteen governance rules agree except for one hyphen (Z3). There are no lowercase "this paper" artifacts.

The should-fix items are mostly about connections the paper does not make.

- **The abstract's model results are not in the paper [C].** The abstract reports specific results from a deterministic contrast model (which regime wins under which shock, three scalarizations ranking three regimes first, a delay sweep), and none of these appears in the body (S1).
- **The paper never names its Mandala stages [C].** Fourteen *Foundations* stages cite its principles, including stages 22–26 and 51 ("Open Myth and Narrative Pluralism"), but *Social Dynamics* is the only domain paper audited so far that never refers to them (S5).
- **Citation practice is the weakest since M&E [C].** Twenty-five of the 50 non-self references are never cited by author and year, and the list includes an uncited, unpublished "working note" attributed to Claude (S6).

**Totals:** 0 must fix, 7 should fix, 5 to consider.

---

## 2. Verified correct

| Item | Check | Result | Label |
|---|---|---|---|
| §2.3 mean-versus-floor construction | Z1 | Means 0.667 and 0.650; minima 0.20 < 0.40 ≤ 0.65 | [C] |
| Twelve-coordinate profile, nine benefits and three costs (§2.2; Frame row 11) | Z2 | 12 coordinates, as stated | [C] |
| Nineteen governance rules, §2.9 and Appendix A.5 | Z3 | 19 and 19; 18 identical, one differs by a hyphen | [C] |
| Identifiers cited | Z4 | 25 distinct; all resolve; all titles match *Foundations* | [C] |
| CU-S1–S5 statements, §14.4 and Appendix A | Z4 | Verbatim with the registry in both places | [C] |
| CU-CL12, CU-COM11, CU-COM18 statements | Z4 | Verbatim with *Foundations* (quotation marks aside) | [C] |
| Propagation artifacts | Z8 | No lowercase "this paper," no "Version Version," no digit-stripping | [C] |
| In-text citations | Z9 | Every author-year citation has an entry (ILO cited by acronym) | [C] |
| Gauthier et al. (2026), *Nature* 652:416–423 (§11.2) | search | Exists; seven-week randomized experiment; algorithm-on shifted policy and current-event attitudes rightward, algorithm-off did not reverse, no effect on affective polarization or partisanship, as described | [S] |
| Nord et al. (2026), V-Dem *Democracy Report 2026* (§7.5) | search | Exists; documents continued global autocratization through 2025, as described | [S] |

---

## 3. Must fix

None.

---

## 4. Should fix

### S1. The abstract reports model results the paper does not contain [C] (abstract; Appendix C; issue #29)

**Evidence.** The abstract's fourth paragraph reports what a deterministic contrast model shows. Centralized suppression responds fastest to a clear common emergency; contestable polycentricity corrects fastest when a locally exposed group detects a distributed shift; majoritarian openness best filters a one-group false alarm; three scalarizations rank three different regimes first; a delay sweep shows that the adaptive regime's advantage depends on timely feedback. None of these phrases or results occurs in the body (Z6). Appendix C places the model in the technical supplement, which is not in the package. This is the same pattern as *Psychology* (Audit 06 S2), but here the abstract states four specific findings.

**Recommended revision.** Either add a short subsection (for example §3.8) that states the three regimes, the three shock types, and the result table, or reduce the abstract paragraph to one sentence pointing to the supplement.

### S2. Section 2.3 points to Appendix B for a construction it already contains [C] (§2.3)

**Evidence.** Section 2.3 says "Appendix B gives the simple construction" and then gives it. Appendix B is the revision list and does not contain the numbers (Z1). *Consciousness* has the same stray pointer (Audit 05 M2), which suggests a shared propagation template.

**Recommended revision.** Delete "Appendix B gives the simple construction" and write "For example."

### S3. Status labels mix authority class and claim status [C] (§14.4; issue #6)

**Evidence.** The §14.4 labels for CU-S1–S3 read "[Domain authority; conditional bridge principle]." *Foundations* gives CU-S2 the claim status "empirical bridge principle," not "conditional," and gives CU-S4 "empirical-interpretive bridge principle" where §14.4 says "provisional social and normative principle," which is the *Foundations* authority class, not the status (Z4). Appendix A gives no status at all.

**Recommended revision.** Give each principle both *Foundations* fields, as recommended for *Biology* and *Psychology*.

### S4. CU-CL12 is called "provisional" in two places [C] (Appendix B; *Foundations* CU-COM18)

**Evidence.** CU-CL12 is canonical as a design principle in *Foundations*, in §13.11, and in Appendix A.3. But Appendix B says v0.10 "adds Open Myth as a provisional cultural architecture," and the *Foundations* cross-reference under CU-COM18 lists "CU-CL12 (provisional)" (Z5). Both look like residue from before CU-CL12 was promoted.

**Recommended revision.** In Appendix B, write "adds Open Myth (CU-CL12) as a canonical design principle whose universal empirical necessity remains unestablished." Remove "(provisional)" from the *Foundations* COM18 cross-reference. Recorded as issue #36.

### S5. The paper never names its Mandala stages [C] (Appendix A)

**Evidence.** Fourteen stages in the *Foundations* table cite CU-S principles, CU-CL principles, CU-COM11, or CU-COM18. Among them are stages 22–26 (Shared Representations through Culture and Meaning Infrastructure) and stage 51, which is titled "Open Myth and Narrative Pluralism" (Z7). *Biology*, *Consciousness*, and *Psychology* each name their stages in Appendix A; *Social Dynamics* has no stage reference, although its front matter says it uses the shared "Mandala cross-references."

**Recommended revision.** Add one paragraph to Appendix A.1 naming the stages this paper principally develops (22–26) and the later stages that draw on it (37, 41–42, 45, 49–51, 57, 61).

### S6. Citation practice [C] (References; issues #23, #35)

**Evidence (Z9).**

- **Unused entries.** Twenty-five of the 50 non-self entries are never cited by author and year. Among them are works the argument visibly draws on: Habermas, Rawls, Young, and Anderson for legitimacy and democracy; Landemore, Page, Lorenz et al., and Woolley et al. for collective intelligence (§3.4); Scott for legibility (§4.6); Tainter for collapse (§9.10). Jaspers, Eisenstadt, and Bellah are named in §12.3 without years.
- **An uncited working note.** The list includes "Claude. (2026). *Mythic and constitutional alignment—A working note*. Unpublished working note prepared for the Coherence Universalism v0.10 project." It is never cited. An uncited, unpublished, AI-generated note does not belong in a reference list. If it shaped §13, the usual practice is to say so in an acknowledgment or methods note.
- **Smaller points.** The ILO report is cited as "ILO, 2024" against an entry under "International Labour Organization." Three entries are appended after "Young" out of alphabetical order. The seven Rader (2026) entries have no suffixes (issue #35).

**Recommended revision.** Cite the drawn-on works where they are used, and drop the rest. Remove the Claude entry and, if appropriate, acknowledge AI assistance in front matter. Add "(ILO)" to the ILO entry and re-sort.

### S7. Notation and identifier format [C] (§§2.1–2.2; issue #8)

**Evidence.** The profile coordinates \(A_d\), \(R_p\), and \(X_c\) sit beside the tuple's \(A\) (agents), \(R\) (distributions), and \(X\) (state), and the profile is \(\mathbf P_{\mathrm{soc}}\) beside the tuple's \(P\) (power) (Z2). The paper also cites CU-CL-8 beside CU-CL12, the identifier-format drift recorded in issue #8 (Z8).

**Recommended revision.** Rename the profile coordinates (for example \(p_{\mathrm{adapt}}, p_{\mathrm{repair}}, p_{\mathrm{extract}}\)), and resolve the CU-CL format under issue #8.

---

## 5. Consider

**K1. "Attractor" in the CU-COM18 statement (§15.10).** The paper retires the "high-coherence attractor" (Note on v0.10; Frame row 9; §14.6; Appendix B), and CU-COM18 then calls Heaven on Earth "this civilizational attractor" and "a family of revisable social attractors" (Z5). The commitment register and the *Foundations* register status keep this from being a descriptive claim, but readers will notice. "Orienting horizon" would carry the meaning without the reintroduced term. The wording is *Foundations*' own, so the change belongs there.

**K2. The "thin" core is metaphysically thick (§13.5).** The proposed shared core begins "Reality is one interdependent whole expressed through differentiated forms." That is a monist metaphysical claim that some traditions the paper invites in (for example, some theistic and dualist ones) would reject. Labeling the core explicitly as **[Commitment]** and adding one sentence acknowledging that some traditions will accept the ethical clauses without the first sentence would make the claim of thinness easier to defend.

**K3. Make A.5 verbatim (Appendix A.5).** Rule 12 reads "social coherence scalar" in §2.9 and "social-coherence scalar" in A.5 (Z3).

**K4. CU-Inst-0 and CU-EC-0 (§§4.3, Foundations).** The CU-Inst and CU-EC families begin at 0, which is unusual and, combined with issue #8, makes the identifier scheme harder to learn. Worth deciding before the registry freezes.

**K5. Collective-intelligence claims (§3.4).** The section states its points without citation, although Lorenz et al. (2011), Page (2007), Landemore (2013), and Woolley et al. (2010) are in the list for exactly these claims (see S6).

---

## 6. Relation to the issue log

- **#6 (status vocabulary).** S3.
- **#8 (identifier formats).** Confirmed: CU-CL-8 and CU-CL12 in the same paper.
- **#9 (RC2 baseline).** Confirmed.
- **#19 (dependency tables).** None in *Social Dynamics*.
- **#23 (citation practice).** Twenty-five unused entries and an uncited unpublished note (S6).
- **#29 (supplements).** Extended: the abstract's model results (S1).
- **#32 (principle drift).** Not present: all CU-S, CU-CL12, and commitment statements are verbatim.
- **#35 (self-citation).** Seven unsuffixed Rader (2026) entries.
- **New #36.** CU-CL12 is called "provisional" in *Social Dynamics* Appendix B and in the *Foundations* CU-COM18 cross-reference, although it is canonical everywhere else (S4).
- **New #37.** Stray pointers to an "Appendix B" construction in *Consciousness* §3.13 and *Social Dynamics* §2.3; Appendix B is the revision list in both. Check *Ethics* and *AI* for the same template (S2).

---

## 7. Standing caution

Every finding here concerns internal coherence, formal correctness, or sourcing. The paper's own test for itself is whether its distinctions "improve model comparison and generate discriminating experiments," and its §14 research program is where that would be decided. This audit cannot evaluate the normative commitments of §15, which the paper correctly places outside empirical warrant.

Passing this audit does not show that the social architecture explains more than the theories it draws on.
