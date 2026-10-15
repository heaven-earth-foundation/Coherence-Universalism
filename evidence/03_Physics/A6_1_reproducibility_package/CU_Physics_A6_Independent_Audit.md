# Independent Audit of CU Physics A.6 — Feedback for the Reconstruction Pass

**Auditor:** Claude (Opus 4.5), independent verification session
**Subject:** `CU_Physics_Systematic_Reconstruction_Kaya_A6.md`, changelog, and reproducibility package
**Date:** September 2026
**Method:** Every numerical claim below was re-derived from scratch in this session rather than
read from the supplied JSON. Where my result differs from A.6's, the disagreement is stated
explicitly. Code for all checks is in §5.

---

## 1. Summary

A.6 is sound on everything I was able to check. The four headline repairs hold, the
generalizations are correct, and — unusually for this document's history — **the revisions
propagated cleanly**. I searched specifically for the failure mode that has recurred through
four previous review rounds (a corrected statement sitting adjacent to an uncorrected one) and
found none: the two-level theorem appears consistently in fourteen places, the rejected
"entropy as inaccessible coherence" identity survives nowhere except as an explicitly labelled
rejection, and Appendix H's CU-FP6 replacement is consistent with §3 and §9.

Independent verification results:

| A.6 claim | Independent result |
|---|---|
| Block theorem: $D(p) - D(E_\pi p) = \sum_b\sum_{i\in B_b}(p_i - q_b/m_b)^2$ | residual $\le 1.7\times10^{-16}$, tested on partitions of $\Delta_4$, $\Delta_6$, $\Delta_8$ |
| Entropy gain $= \sum_b q_b\,\mathrm{KL}(r^{(b)}\|\nu_{m_b})$ | residual $\le 9.0\times10^{-16}$, same partitions |
| Wedge collapses on every nonuniform two-level state | $\max\|1 - \chi\| = 6.7\times10^{-16}$ over 4000 constructed two-level states, both metrics |
| Critical ratio $\beta/\alpha = 2(a-b)/\log(a/b)$ | matches both wedge edges to $1.0\times10^{-13}$ |
| Wedge strict when $\ge 3$ distinct values | 0 counterexamples in $3\times10^5$ samples |
| $\sup\|A\|_F^2 = \tfrac{23}{128} + \tfrac{11\sqrt{33}}{384}$ at $x = (7+\sqrt{33})/16$ | agrees to 0.0 (exact) |
| $\sup\|B\|_F = 1.011677099862651$, $\sup\Pi_F = 0.586672264109138$ | reproduced |
| Strong-damping expansion $\dot q = \eta^{-1}F - \eta^{-3}\nabla_F F + O(\eta^{-5})$ | algebra confirmed |

**Correction to my own prior audit.** My earlier note characterized the wedge-degeneracy set as
the finite set of states uniform on their support. A.6 §4.2 is right and I was wrong. I
identified the zero set of the *norms* $\|A\|_F, \|B\|_F, \Pi_F$, which is indeed that finite
set; but wedge collapse requires only $A \parallel B$, not $A = B = 0$, and that holds on every
two-level state. The mechanism is clean and I should have seen it: on a two-level state both
$\partial D$ and $\partial S$ are two-valued on the same index partition, so after centring
both are proportional to the same indicator-difference vector. A.6's characterization is
correct, more general, and better proved.

---

## 2. The one finding that needs action

### 2.1 The overdamped slope test does not measure what it is reported to measure

**Status: this is a methodological confound, not a mathematical error.** The expansion in §6.1
of the changelog is correct. The numerical test offered as evidence for it is not diagnostic.

A.6 reports a fitted log-log slope of $-1.87$ over $\eta \in \{1,3,10,30,100,300\}$ and calls
it "consistent with the predicted $O(\eta^{-2})$." Two confounds make that inference unsafe.

**Confound 1: the initial layer dominates, and its size depends on $\dot q(0)$.** If the
second-order system starts at rest, the transient $\dot q(t) \approx (F/\eta)(1 - e^{-\eta t})$
contributes a one-time position deficit of order $\eta^{-2}$ — the *same order* as the effect
being measured, and arising from initialization rather than from the $\nabla_F F$ correction.
The measured slope therefore depends on how the comparison run was initialized.

**Confound 2: the fitting range is too short to resolve the asymptote.** On a 2-D test system
($\ddot q + \eta\dot q = F$, $F = -\nabla V$, $V = q_1^4/4 + q_2^2/2 + 0.3q_1q_2$, $T = 40$):

| initialization | slope over $\eta \in [1,300]$ | slope over $\eta \in [10,1000]$ |
|---|---:|---:|
| rest, $\dot q(0) = 0$ | $-0.881$ | $-1.419$ |
| slow manifold, $\dot q(0) = F(q_0)/\eta$ | $-1.795$ | $-1.962$ |

The system is not yours, so the numbers won't match. The structure is what matters: with rest
initialization the slope is nowhere near $-2$ at any tested range, and even with correct
initialization the paper's $\eta$ range gives $-1.80$. Only extending to $\eta \sim 10^3$ with
slow-manifold initialization recovers $-1.96$.

**Recommended fix**, cheap and decisive:

1. Initialize the second-order run on the slow manifold, $\dot q(0) = F(q_0)/\eta$, and say so
   in the manuscript. If you prefer rest initialization for physical reasons, subtract the
   initial-layer contribution analytically or start the comparison after $t \gg 1/\eta$.
2. Extend the sweep to $\eta \in \{10, 30, 100, 300, 1000, 3000\}$ and report the slope over
   the upper decade only.
3. Report *both* initializations. The contrast is itself informative and demonstrates that the
   $O(\eta^{-2})$ behaviour is a property of the slow manifold rather than an artifact.
4. State in the manuscript which error norm is fitted (absolute position at fixed $T$, relative
   position, or velocity), since the three have different exponents.

Until this is done, I would soften the claim-status line from "corrected to behavior consistent
with $O(1/\eta^2)$" to "the covariant expansion predicts $O(\eta^{-2})$ relative velocity error;
the current fixed-time numerical test does not yet isolate that term from the initial layer."

---

## 3. Two results A.6 has earned but not stated

Both follow from work already in A.6 and would strengthen §3.14 substantially. Neither is a
correction.

### 3.1 At fixed coupling, the degeneracy set is discrete — and above a threshold it is empty

The changelog says the degeneracy set "contains continuous lower-dimensional one-plus-three,
two-plus-two, and three-plus-one families." True as stated, but it understates the result,
because the dynamics of §3.13 runs at *fixed* $\alpha, \beta$. At fixed $r = \beta/\alpha$, the
degenerate states are those two-level states solving $2(a-b)/\log(a/b) = r$ — a finite set:

| $r = \beta/\alpha$ | degenerate states in $\Delta_4$ (up to permutation) |
|---|---|
| $0.3$ | 3 |
| $0.5$ | 2 (including $u$) |
| $0.7$ | **none** |

The quantity $2(a-b)/\log(a/b)$ is twice the logarithmic mean $L(a,b)$, and its maximum over
two-level states of $\Delta_4$ is

$$\sup 2L(a,b) = 0.6213609436, \qquad \text{attained at } (a,b) = (0.63034,\ 0.12322) \text{ on a } 1{+}3 \text{ family.}$$

So for $\beta/\alpha > 0.62136$ **no state of $\Delta_4$ is wedge-degenerate at all**. That is a
sharper and more useful statement than "the wedge can collapse," and it is exactly the kind of
derived threshold the Goldilocks discussion needs.

### 3.2 $\beta/\alpha = 1/2$ is a bifurcation of the uniform state, not only a wedge closure

This is the stronger of the two and I would put it in §3.13 or §3.14.1.

For $F = \alpha D + \beta S$ the Hessian is diagonal, $\partial^2 F/\partial p_i^2 = 2\alpha - \beta/p_i$,
so at $p = u$ the tangent Hessian is $(2\alpha - 4\beta)\,\mathbb{I}$. Hence:

$$\boxed{\ \beta/\alpha < \tfrac12 \;\Rightarrow\; u \text{ is a local minimum of } F \text{ (repelling under ascent)}; \qquad \beta/\alpha > \tfrac12 \;\Rightarrow\; u \text{ is a local maximum (attracting).}\ }$$

Confirmed by integration from $p_0 = u + 10^{-4}\delta$ to $T = 4000$:

| $\beta/\alpha$ | final $D$ | $\|p - u\|$ | behaviour |
|---:|---:|---:|---|
| 0.20 | $7.50\times10^{-1}$ | $8.66\times10^{-1}$ | escapes |
| 0.49 | $6.19\times10^{-1}$ | $7.87\times10^{-1}$ | escapes |
| 0.50 | $2.81\times10^{-8}$ | $1.68\times10^{-4}$ | collapses |
| 0.51 | $1.05\times10^{-23}$ | $3.23\times10^{-12}$ | collapses |
| 0.90 | $2.67\times10^{-24}$ | $1.64\times10^{-12}$ | collapses |

The transition is sharp between 0.49 and 0.50.

**Why this matters for the framework.** A.6 currently presents $\beta/\alpha = 1/2$ as the value
at which the wedge edges meet at uniform — a local, geometric fact. It is also the value at
which the maximally undifferentiated state changes stability. Two independent derivations
landing on the same number means it is structural, not incidental. And it gives CU something it
has wanted throughout: a *derived* critical coupling separating a regime in which structure
spontaneously grows from indifference from one in which it decays back into it. That is a
Goldilocks claim with a proof, stated in terms of the model's own parameters, with no imported
thresholds.

I would also note the classification of the other degenerate equilibria, which falls out of the
same Hessian: the near-corner ones are local maxima of $F$ (attracting under ascent), the
intermediate ones saddles. So the degenerate set is not merely where the wedge closes — it is
the critical-point set of the combined flow, with a stability type attached to each point.

---

## 4. Smaller items and coverage note

**Smaller items.**

- §4.2's sentence "Random sampling almost surely misses those exact sets, explaining why a
  large Monte Carlo test can report no collapse" is correct and well put. It is also a general
  lesson worth keeping in the working notes: this document's history includes several claims
  that survived sampling because the failure set had measure zero.
- The Wallstrom citation in §7.14 is the right move and the recovery should stay conditional.
  The Madelung-to-Schrödinger step is the standard place where hydrodynamic reconstructions
  overclaim, and A.6 currently does not.
- $\sup\|B\|_F$ and $\sup\Pi_F$ are given numerically while $\sup\|A\|_F$ has a closed form.
  If the same KKT reduction yields closed forms for the other two, they are worth having; if
  the stationarity equations are genuinely transcendental, say so explicitly so a reader does
  not assume the omission is an oversight.

**What I did not check.** My audit covered §3, §4's wedge material, §6.1–6.5 of the changelog,
and the block-averaging and Fisher-extrema results. I did **not** independently verify: §8
(relational geometry), §9 (gravity/Jacobson), §10 (horizons), Appendix E's Madelung algebra,
Appendix J's lattice-wave and Madelung convergence runs, or the reference list. The QA report's
structural checks are not a substitute for review of those, and §§8–10 remain the largest
unaudited claim surface in the document.

---

## 5. Reproduction code

Deterministic; NumPy and SciPy only.

```python
import numpy as np
from scipy.integrate import solve_ivp
rng = np.random.default_rng(101)

# ---- 3.2  bifurcation of the uniform state at beta/alpha = 1/2 ----
u = np.full(4, .25)
def rhs(t, p, al, be):
    dD = 2*(p - .25); dS = -(np.log(np.clip(p, 1e-300, None)) + 1)
    g = al*dD + be*dS
    return p*(g - p@g)                      # Fisher natural gradient ascent
p0 = u + np.array([1e-4, -1e-4, 5e-5, -5e-5])
for r in [0.20, 0.49, 0.50, 0.51, 0.90]:
    s = solve_ivp(rhs, [0, 4000], p0, args=(1.0, r), rtol=1e-11, atol=1e-14)
    pf = s.y[:, -1]
    print(r, np.sum((pf - .25)**2), np.linalg.norm(pf - u))
# Hessian of F = aD + bS is diag(2a - b/p_i); at u this is (2a - 4b) I.

# ---- 3.1  threshold above which no two-level state is degenerate ----
best = (0, None)
for m in [1, 2, 3]:
    for a in np.linspace(1e-7, 1/m - 1e-7, 2_000_000):
        b = (1 - m*a)/(4 - m)
        if b <= 1e-12 or abs(a - b) < 1e-12: continue
        v = 2*(a - b)/np.log(a/b)
        if v > best[0]: best = (v, (m, a, b))
print("sup 2L(a,b) =", best[0], "at", best[1])      # 0.6213609436

# ---- 2.1  overdamped slope, both initializations ----
def F(q): return np.array([-(q[0]**3) - 0.3*q[1], -q[1] - 0.3*q[0]])
def second(t, y, eta): return np.concatenate([y[2:], F(y[:2]) - eta*y[2:]])
def over(t, q, eta):   return F(q)/eta
q0 = np.array([1.0, 0.6]); T = 40.0; res = {}
for eta in [1, 3, 10, 30, 100, 300, 1000]:
    qref = solve_ivp(over, [0, T], q0, args=(eta,), rtol=1e-12, atol=1e-14).y[:, -1]
    res[eta] = [np.linalg.norm(
        solve_ivp(second, [0, T], np.concatenate([q0, v0]), args=(eta,),
                  rtol=1e-12, atol=1e-14).y[:2, -1] - qref)
        for v0 in [np.zeros(2), F(q0)/eta]]
sl = lambda e, k: np.polyfit(np.log(e), np.log([res[x][k] for x in e]), 1)[0]
for e in ([1,3,10,30,100,300], [10,30,100,300,1000]):
    print(e, "rest:", round(sl(e,0),3), " slow-manifold:", round(sl(e,1),3))
```
