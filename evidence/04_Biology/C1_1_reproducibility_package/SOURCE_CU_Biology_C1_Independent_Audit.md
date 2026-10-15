# Independent Audit of CU Biology C.1

**Auditor:** Claude (Opus 4.5), independent verification session
**Subject:** `CU_Biology_Systematic_Reconstruction_Kaya_C1.md` and reproducibility package
**Date:** September 2026
**Against:** `CU_Biology_C1_AUDIT_BRIEF.md`
**Companion memos:** `CU_Physics_A6_Independent_Audit.md`, `CU_v010_B1_Independent_Audit.md`

---

## 1. Recommendation

**Adopt with bounded repairs.** The reconstruction discipline holds throughout, not only in the
abstract and appendices. I looked specifically for the failure mode the brief names in A.4 — a
universal scalar creeping back after being retired — and found none. Every occurrence of
"coherence gradient," "maximizes coherence," or "total coherence" in the manuscript is either a
retirement, a scoping restriction, or an explicit denial. §A.18's three-way separation of
optimization language (designer / as-if / evolutionary) is the strongest single piece of
discipline in the document and I would point other domain papers at it.

One substantive repair is needed, in the toy model's framing rather than its mathematics.

---

## 2. Toy model: brief items B.1–B.4 answered

**B.1 — independent reproduction.** I reimplemented the model from the equations recorded in the
JSON, not from the bundled script, and it reproduces exactly:

| $\kappa$ | min margin | control cost | late RMSE |
|---:|---|---|---|
| 0.0 | $\Delta = 0.0$ | $\Delta = 7.3\times10^{-14}$ | $\Delta = 0.0$ |
| 0.1 | $\Delta = 0.0$ | $\Delta = 6.5\times10^{-14}$ | $\Delta = 0.0$ |
| 0.8 | $\Delta = 0.0$ | $\Delta = 6.3\times10^{-14}$ | $\Delta = 0.0$ |

The cost differences are float-summation-order artifacts at machine epsilon. Margins and RMSE
agree bit-for-bit.

**B.2 — update, clipping, budget, disturbance, floor, late window.** All match the recorded
equations.

**B.4 — does clipping drive any trend?** **No.** The clip to $[0,1]$ is never active in any
controller run at any $\kappa$ in the sweep: zero clipped steps at $\kappa = 0, 0.1, 0.8$. This
is a clean negative and worth stating in the manuscript, since it forecloses the most obvious
artifact objection.

**B.3 — monotonic trends.** Confirmed, and more robust than I expected. I tried to break the
margin monotonicity with a uniform rather than localized disturbance class, with heterogeneous
decay rates producing spread equilibria, and with heterogeneous floors. All three preserved it.

---

## 3. The repair: the margin result is configuration-dependent, and the paper does not say which

Diffusive coupling $\kappa(\bar x - x)$ pulls every component toward the mean. It therefore
raises the minimum margin **if and only if the binding component sits below the mean.**

In the C.1 configuration this is guaranteed rather than discovered. The floors are identical
$(0.24, 0.24, 0.24)$ and the natural equilibria $x^* = \text{supply}/\text{decay} =
(0.5909, 0.6111, 0.6000)$ span only $0.0202$. So the binding component is always whichever was
most recently shocked, which is always below the mean. Coupling cannot do anything but help.

Reverse the condition and the result reverses. Take three components with
$x^* = (0.60, 0.60, 0.90)$ — achieved with decay $(0.30, 0.30, 0.04)$, supply
$(0.18, 0.18, 0.036)$ — and floors $(0.10, 0.10, 0.82)$, so the high-sitting third component is
the binding one. A small disturbance to it at $t \in [40, 50)$:

| $\kappa$ | 0.0 | 0.02 | 0.05 | 0.10 | 0.15 | 0.25 | 0.40 | 0.80 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| min margin | $0.0431$ | $0.0369$ | $0.0286$ | $0.0168$ | $0.0071$ | $-0.0080$ | $-0.0238$ | $-0.0470$ |
| viable | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ |

Strictly *decreasing*, and the system is viable at $\kappa = 0$ but has breached its floor by
$\kappa = 0.25$. **Integration destroys viability here.** The mechanism is direct: coupling
drains the high-requirement component toward a low mean, while the low-requirement components
gain slack they do not need.

**Why this matters, and why it is additive rather than corrective.** Proposition A.15 claims
only that stronger coupling "need not improve every profile component," and the existing sweep
establishes that — cost and late tracking both worsen. The proposition is sound. But the model
as configured shows only the weaker of two failure modes: integration helping viability while
hurting differentiation. It does not show integration *destroying* viability, which is the more
biologically consequential case and arguably the one the framework most needs on record. Loss of
compartmentalization harming a specialized tissue is a recognizable pattern; "integration
improves robustness but costs adaptability" is closer to a design truism.

**Recommended repair**, cheap:

1. Add the one-line characterization to §A.15 or Appendix B: *diffusive coupling raises the
   minimum margin exactly when the binding component lies below the mean; the C.1 configuration
   satisfies this by construction, since the floors are homogeneous and the equilibria nearly
   coincident.*
2. Add the reversed configuration as a second run in the sweep. It costs a few lines in the
   reproducibility script and strengthens A.15 from "need not improve every component" to "can
   strictly worsen the component the framework cares most about."
3. State that the margin monotonicity is a property of the declared configuration, not of
   coupling.

---

## 4. A second observation on the same model

In every controller run, the minimum margin lies between $0.281$ and $0.353$. The floor is
$0.24$ and the state never drops below roughly $0.52$. **Viability is never in question in any
run in the sweep.** The quantity described as "worst-case viability margin" is a metric that
moves but never binds.

This does not make the result false, and the no-controller reference at $-0.101$ does show a
genuine breach. But a reader may take "stronger coupling improves the worst-case viability
margin" to mean coupling rescues a system that would otherwise fail, and nothing in the sweep
demonstrates that. Either add a run where the margin actually crosses zero as $\kappa$ varies —
the configuration in §3 above does exactly this — or note that the sweep measures margin
movement well inside the viable region.

---

## 5. Bibliography spot-check (brief item G)

The three citations postdating my training data all verify:

| Citation | Status |
|---|---|
| Rajan et al. (2026), single-cell *Stentor* learning | Real. *Current Biology* 36:2367–2381.e9, doi 10.1016/j.cub.2026.03.080. Rajan, Albright, Kim, Diaz, Hudnall, Steube, Dey, Liu, Marshall |
| Cortés-Poza (2026), hybrid morphogenesis | Real. *Journal of Mathematical Biology*, doi 10.1007/s00285-026-02459-2 |
| Giessler et al. (2026), genetically encoded RNA droplets | Real. *Angew. Chem. Int. Ed.* 65(7):e19002, doi 10.1002/anie.202519002 |

One substantive note on the Rajan result, since the literature ledger's characterization is
thinner than the finding. The headline is counterintuitive: protein-synthesis inhibitors
(puromycin, cycloheximide) *accelerate* habituation and *prolong* memory retention in *Stentor*,
the opposite of the metazoan pattern, and the authors' reading is that protein synthesis
maintains the responsive baseline rather than encoding the memory. The habituated state also
propagates to daughter cells across division. Both details strengthen C.1's use of the source —
they make the case that this is history-dependent regulation rather than a metazoan-learning
analogy — and the ledger currently leaves them on the table. The "does not infer" column is
correctly conservative.

I did not verify the remaining twenty-one references.

---

## 6. Smaller items

**6.1 The governance rules exist only in the JSON.** The principle registry carries five rules —
name the candidate unit, name the horizon, name the disturbance class, declare weights and
floors, don't promote stake to phenomenal value. Three of the five appear nowhere in the
manuscript: "names the candidate unit," "names the horizon," and "names the disturbance class"
each return zero hits. §D of the manuscript says the five rules "need not become separate
Foundations principles," which is a reasonable call, but rules that govern the paper's own
claims should be stated in the paper. The disturbance-class rule is the one my §3 finding turns
on, and C.1 would have caught that problem itself had the rule been in force in the body.

**6.2 Proposition 3 (A.6) is correct.** The passive Markov counterexample to recurrence
dominance is valid: the two-state chain with $P(L|L) = 0.99 > 0.10 = P(L|N)$ has no endogenous
regulation, so the inequality is not sufficient. Clean and minimal.

**6.3 §A.18 should be cited elsewhere in the corpus.** The designer / as-if / evolutionary
separation is exactly the distinction the AI and Consciousness papers will need when they reach
optimization language, and it is better stated here than anywhere I have seen in the CU
material.

---

## 7. Coverage

I audited: the toy model (full independent reimplementation, clipping, step-size behaviour, and
four alternative configurations), Propositions 3 and 10, §A.18, the scalar-restoration sweep
across the whole manuscript, the governance-rule propagation, and three bibliography entries.

I did **not** audit: Propositions 1, 2, and 4–9 in detail; the philosophy-of-biology sections
(brief item C, including the life criterion against flames, storms, and servomechanisms); the
domain reviews in brief item D; the claim ledger row by row against the body; the candidate
principles CU-B1 through CU-B5 on conceptual grounds; or twenty-one of the twenty-four
references. Brief items C, D, E, and F remain substantially open and need a biologist rather
than another verification pass.
