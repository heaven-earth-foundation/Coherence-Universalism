# Coherence Universalism: Physics
## RC3 Release-Convergence Wave 4 — Technical Supplement

**Status and authority.** This is the released technical supplement for the Wave 4 cumulative manuscript. The [reader-facing manuscript](../papers/03_CU_Physics_v0.10.md) controls current wording, claim status, and canonical cross-references. This supplement exposes the formal derivations, deterministic contrast constructions, claim ledgers, audit materials, scripts, and source records on which the manuscript relies.

- **Evidence directory:** [03_Physics](../evidence/03_Physics/README.md)
- **Archived source package:** [CU_Physics_v0.10_Publication_PC4.zip](../provenance/archival_source_packages/CU_Physics_v0.10_Publication_PC4.zip)
- **Current supplement path:** `technical_supplements/03_Physics_Technical_Supplement_v0.10.md`

Reproducibility of a construction shows only that its output follows from its declared assumptions and code. It does not convert a toy model or simulation into target-domain empirical validation. Where this preserved archive uses historical identifiers or statuses, the Wave 4 normalized registries and current manuscript control.

# Wave 4 evidence-access addendum

Wave 4 makes previously referenced but inaccessible materials available in one package. It includes the substantive legacy supplement below, the independent audit and check script, recorded audit output where available, source ledgers, deterministic scripts and generated results where they existed, and the complete pre-RC3 source package for provenance.

The software-repository citation in the manuscript now resolves to this released archive rather than to an unspecified external GitHub repository.

# Preserved substantive technical archive

**Gaura Kiśora Dās Rader**  
**Heaven≡Earth Foundation**  
**September 2026**

---

## Purpose and authority

This supplement preserves the formal proofs, complete status ledger, dimensional conventions, principle crosswalk, numerical reproduction record, audit history, and editorial provenance underlying the reader-facing Physics publication candidate.

The principal manuscript is designed for continuous scholarly reading. This supplement is designed for checking. Where wording differs, the systematic A.6.1 authority manuscript controls the exact pre-publication mathematics, while the main publication candidate controls reader-facing presentation. Any substantive discrepancy must be resolved against the frozen source and recorded in a later version.

## Contents

- Supplement A — Classical Sandbox Proofs
- Supplement B — Temporal Structure and Conservative Accessibility Flow
- Supplement C — Quantum Propositions and Counterexamples
- Supplement D — Hamiltonian and Madelung Derivations
- Supplement E — Dimensional and Notation Conventions
- Supplement F — Full Claim and Status Ledger
- Supplement G — Principle Crosswalk and Reconciliation
- Supplement H — Companion-Paper Numerical Reproduction Audit
- Supplement I — A.6 Theorem and Structural Audit
- Supplement J — Independent A.6 Audit Response and A.6.1 Verification
- Supplement K — Editorial and Source Map
- Supplement L — Figure Program
- Publication-Copy Clarifications Added After the A.6.1 Archive

The executable code, generated results, environment declaration, original audits, and integrity records accompany this supplement in the publication package.

---

---

# Supplement A. Classical Sandbox Proofs

## B.1 Range of \(D\)

Since

\[
D(p)
=
\sum_i p_i^2-\frac14,
\]

and

\[
\sum_i p_i^2\geq\frac14
\]

by Cauchy–Schwarz, \(D\geq0\), with equality at \(u\).

On the closed simplex, the convex function \(\sum_i p_i^2\) is maximized at a vertex, where it equals \(1\). Thus

\[
D_{\max}=1-\frac14=\frac34.
\]

## B.2 Supremum of the Euclidean gradient norm

Since

\[
a=2(p-u),
\]

\[
\|a\|_2^2=4D(p).
\]

Therefore

\[
\sup\|a\|_2^2
=
4\cdot\frac34=3,
\]

and

\[
\boxed{
\sup\|a\|_2=\sqrt3.
}
\]

## B.3 Jeffreys-divergence identity

Because

\[
b_i
=
-\log p_i+\frac14\sum_j\log p_j
\]

and \(\sum_i(p_i-\tfrac14)=0\),

\[
\begin{aligned}
a\cdot b
&=
2\sum_i
\left(p_i-\frac14\right)
\left[
-\log p_i+\frac14\sum_j\log p_j
\right]\\
&=
-2\sum_i
\left(p_i-\frac14\right)\log p_i.
\end{aligned}
\]

Now

\[
\begin{aligned}
J(p,u)
&=
\operatorname{KL}(p\|u)+\operatorname{KL}(u\|p)\\
&=
\sum_i(p_i-u_i)\log p_i
-
\sum_i(p_i-u_i)\log u_i.
\end{aligned}
\]

Since \(\log u_i\) is constant and \(\sum_i(p_i-u_i)=0\),

\[
J(p,u)
=
\sum_i\left(p_i-\frac14\right)\log p_i.
\]

Hence

\[
a\cdot b=-2J(p,u)
\]

and

\[
\Pi_E=2J(p,u).
\]

## B.4 Simultaneous growth condition

For

\[
v=\alpha a+\beta b,
\]

\[
\dot D=a\cdot v
=
\alpha\|a\|^2-\beta\Pi_E,
\]

and

\[
\dot S=b\cdot v
=
-\alpha\Pi_E+\beta\|b\|^2.
\]

Assuming \(\alpha,\beta,\Pi_E>0\),

\[
\dot D>0
\iff
\frac{\beta}{\alpha}
<
\frac{\|a\|^2}{\Pi_E},
\]

and

\[
\dot S>0
\iff
\frac{\beta}{\alpha}
>
\frac{\Pi_E}{\|b\|^2}.
\]

The interval is nonempty iff

\[
\Pi_E^2<\|a\|^2\|b\|^2.
\]

The non-strict reverse inequality is Cauchy–Schwarz. Equality means exact collinearity.

## B.5 Exact discrete identity

Let \(p^+=p+h v\). Then

\[
\begin{aligned}
D(p^+)
&=
(p+h v-u)\cdot(p+h v-u)\\
&=
D(p)+2h(p-u)\cdot v+h^2\|v\|^2.
\end{aligned}
\]

Since \(a=2(p-u)\),

\[
\Delta D
=
h a\cdot v+h^2\|v\|^2.
\]

Substituting \(v=\alpha a+\beta b\) gives

\[
\Delta D
=
h(\alpha\|a\|^2-\beta\Pi_E)
+
h^2\|\alpha a+\beta b\|^2.
\]

## B.6 Finite-partition projection and block-averaging theorems

Let \(\{B_b\}\) be a partition of \(\{1,\ldots,N\}\), with \(m_b=|B_b|\) and

\[
q_b=\sum_{i\in B_b}p_i.
\]

Define the block-uniform conditional expectation

\[
[E_\pi p]_i=\frac{q_b}{m_b}
\qquad(i\in B_b).
\]

The block-constant vectors form a Euclidean subspace containing the global uniform distribution \(u\), and \(E_\pi\) is the Euclidean orthogonal projection onto that subspace. Therefore

\[
p-u=(p-E_\pi p)+(E_\pi p-u)
\]

with orthogonal summands. Pythagoras gives

\[
\boxed{
D_N(p)
=
D_N(E_\pi p)
+
\sum_b\sum_{i\in B_b}
\left(p_i-\frac{q_b}{m_b}\right)^2.
}
\]

For the two equal blocks in Section 3,

\[
D_4(E_\pi p)=\bar D(q)
\]

and the residual reduces to

\[
H_\pi^{(D)}
=
\frac12[(p_1-p_2)^2+(p_3-p_4)^2].
\]

For entropy, write \(p_i=q_b r_i^{(b)}\) inside each occupied block. Then

\[
\begin{aligned}
S(p)
&=-\sum_b\sum_{i\in B_b}q_br_i^{(b)}
\log[q_br_i^{(b)}]\\
&=S(q)+\sum_bq_bS(r^{(b)}).
\end{aligned}
\]

This is Shannon’s grouping identity. Because \(E_\pi p\) has uniform conditional distributions,

\[
S(E_\pi p)=S(q)+\sum_bq_b\log m_b.
\]

Subtracting yields

\[
\begin{aligned}
S(E_\pi p)-S(p)
&=
\sum_bq_b[\log m_b-S(r^{(b)})]\\
&=
\sum_bq_b
\operatorname{KL}
\left(r^{(b)}\middle\|\nu_{m_b}\right)
\geq0.
\end{aligned}
\]

Both the differentiation residual and entropy gain vanish exactly when \(p=E_\pi p\), but equality of zero sets does not imply equality of the functionals.

## B.7 Fisher natural gradient

For tangent \(v\),

\[
df(v)=\sum_i\partial_i f\,v_i.
\]

Seek \(X=\operatorname{grad}_Ff\) such that

\[
\sum_i\frac{X_iv_i}{p_i}
=
\sum_i\partial_i f\,v_i
\]

for all \(v\) with \(\sum_iv_i=0\).

Thus

\[
\frac{X_i}{p_i}
=
\partial_i f-\lambda
\]

for some \(\lambda\). Tangency requires

\[
0=\sum_iX_i
=
\sum_ip_i(\partial_i f-\lambda),
\]

so

\[
\lambda=\sum_ip_i\partial_i f.
\]

Hence

\[
X_i
=
p_i\left(
\partial_i f-\sum_jp_j\partial_j f
\right).
\]

## B.8 Natural gradients of \(D\) and \(S\)

For \(D\),

\[
\sum_jp_j\partial_jD
=
2\sum_jp_j\left(p_j-\frac14\right)
=
2\left(\sum_jp_j^2-\frac14\right).
\]

Therefore

\[
A_i
=
2p_i
\left(
p_i-\sum_jp_j^2
\right).
\]

For \(S\),

\[
\sum_jp_j\partial_jS
=
\sum_jp_j(-\log p_j-1)
=
S-1.
\]

Thus

\[
B_i
=
p_i[-\log p_i-1-(S-1)]
=
p_i(-\log p_i-S).
\]

Their Fisher norms and opposition simplify to

\[
\|A\|_F^2
=4\left(\sum_ip_i^3-\left(\sum_ip_i^2\right)^2\right),
\]

\[
\|B\|_F^2
=\operatorname{Var}_p(\log p_i),
\]

and

\[
\Pi_F=2\operatorname{Cov}_p(p_i,\log p_i).
\]

## B.9 Joint-growth wedge and exact two-level degeneracy

Let \(X=\operatorname{grad}_gD\) and \(Y=\operatorname{grad}_gS\) for either geometry, and assume both are nonzero. With

\[
\Pi=-\langle X,Y\rangle_g,
\qquad
\chi=\frac{\Pi}{\|X\|_g\|Y\|_g},
\]

Cauchy–Schwarz gives \(0<\chi\leq1\). The wedge edges are

\[
L=\frac{\Pi}{\|Y\|_g^2}
=
\chi\frac{\|X\|_g}{\|Y\|_g},
\]

\[
U=\frac{\|X\|_g^2}{\Pi}
=
\frac1\chi\frac{\|X\|_g}{\|Y\|_g}.
\]

Thus \(L<U\) if and only if \(\chi<1\), equivalently if and only if \(X\) and \(Y\) are not collinear.

For the Euclidean tangent fields, collinearity implies constants \(c,d\) such that

\[
\log p_i=c p_i+d
\]

for every coordinate value appearing in \(p\). The same condition follows from the Fisher score fields after division by \(p_i>0\). Since \(\log x\) is strictly concave, a line can intersect its graph at no more than two distinct positive values. Therefore three or more distinct coordinate values imply a strict wedge.

Conversely, if the coordinates take exactly two values \(a>b>0\), every centered function of the coordinates is constant on the same two groups and the tangent score space is one-dimensional. Direct subtraction between the two groups gives

\[
Y=-kX,
\qquad
k=\frac{\log(a/b)}{2(a-b)}.
\]

Hence \(\chi=1\) and

\[
L=U=\frac1k
=
\frac{2(a-b)}{\log(a/b)}.
\]

At uniformity both gradients vanish. This proves the degeneracy characterization stated in Section 3.14.2.

Near \(u\), write \(p=u+\delta\) with \(\sum_i\delta_i=0\). For the Fisher fields,

\[
A_i=\frac12\delta_i+O(\|\delta\|^2),
\qquad
B_i=-\delta_i+O(\|\delta\|^2),
\]

so the wedge edges approach \(1/2\) and their width tends to zero.

## B.9.1 Fixed-coupling stationary points and stability of uniformity

Let

\[
\Phi_r(p)=D(p)+rS(p),
\qquad r>0.
\]

An interior constrained critical point satisfies

\[
2\left(p_i-\frac14\right)-r(\log p_i+1)=\lambda
\]

for all \(i\). Define

\[
h_r(x)=2\left(x-\frac14\right)-r(\log x+1).
\]

Because

\[
h_r''(x)=\frac{r}{x^2}>0,
\]

\(h_r\) has one minimum and each horizontal level has at most two positive preimages. Every nonuniform interior critical point therefore has exactly two coordinate values \(a>b\). Subtracting their stationarity equations gives

\[
2(a-b)=r\log(a/b),
\]

or

\[
\boxed{
 r=\frac{2(a-b)}{\log(a/b)}.
}
\]

Suppose the larger value \(a\) has multiplicity \(m\in\{1,2,3\}\), and put \(q=a/b>1\). Normalization gives

\[
a=\frac{q}{mq+4-m},
\qquad
b=\frac{1}{mq+4-m},
\]

so

\[
r_m(q)
=
\frac{2(q-1)}{(mq+4-m)\log q}.
\]

For \(m=2\) and \(m=3\), direct differentiation shows that \(r_m(q)<1/2\) for every \(q>1\), with supremum \(1/2\) only as \(q\downarrow1\). For \(m=1\),

\[
r_1(q)=\frac{2(q-1)}{(q+3)\log q},
\]

and its nonuniform maximum occurs where

\[
q^2+2q-3=4q\log q.
\]

The unique root above one is

\[
q_*=5.115660866489398\ldots,
\]

which gives

\[
r_*=0.621360943645626\ldots .
\]

Thus no nonuniform interior critical point exists for \(r>r_*\). For any fixed \(r\leq r_*\), the scalar equations \(r_m(q)=r\) have only finitely many roots, so the stationary intersection is finite up to permutation. The full geometric wedge-degeneracy set remains continuous because it is defined without fixing \(r\).

At \(u=(1/4,\ldots,1/4)\), the tangent Hessian is

\[
\operatorname{Hess}\Phi_r(u)=(2-4r)I.
\]

It is positive definite for \(r<1/2\) and negative definite for \(r>1/2\). Hence uniformity is respectively a strict local minimum or maximum of the ascent objective. At \(r=1/2\), Taylor expansion of Shannon entropy gives

\[
\Phi_{1/2}(u+\delta)-\Phi_{1/2}(u)
=
\frac43\sum_i\delta_i^3
-
\frac83\sum_i\delta_i^4
+
O(\|\delta\|^5),
\qquad
\sum_i\delta_i=0.
\]

Choosing \(\delta=(3\epsilon,-\epsilon,-\epsilon,-\epsilon)\) and changing the sign of \(\epsilon\) changes the leading sign. The critical point is therefore neither a local maximum nor a local minimum at exact criticality.

## B.10 Global bounds for the Fisher fields

The functions \(\|A\|_F^2\), \(\|B\|_F^2\), and \(\Pi_F\) extend continuously to each face when terms of the form \(p(\log p)^k\) are assigned their limiting value zero. A global maximum therefore exists on the compact closed simplex.

For \(\|A\|_F^2=4(s_3-s_2^2)\), the interior stationarity equation on a fixed face is quadratic in each positive \(p_i\), so an extremizer has at most two distinct positive values.

For \(\|B\|_F^2=\sum_ip_i(\log p_i)^2-\mu^2\), with \(\mu=\sum_ip_i\log p_i\), the stationarity equation is quadratic in \(\log p_i\), again permitting at most two distinct positive values.

For \(\Pi_F/2=\sum_ip_i^2\log p_i-s_2\mu\), the derivative with respect to a positive coordinate is

\[
g(p)
=
2p\log p+p-2\mu p-s_2(\log p+1).
\]

Its second derivative satisfies

\[
g''(p)=\frac{2}{p}+\frac{s_2}{p^2}>0.
\]

Thus \(g\) is strictly convex and the stationarity equation \(g(p_i)=\lambda\) has at most two positive solutions.

It remains to examine every support size \(k=2,3,4\) and multiplicity \(m=1,\ldots,k-1\). Writing total mass \(z\) on one group gives

\[
p=
(\underbrace{z/m,\ldots,z/m}_{m},
\underbrace{(1-z)/(k-m),\ldots,(1-z)/(k-m)}_{k-m}),
\]

so every case reduces to one variable. Exhaustive comparison gives the global maxima stated in Section 3.13.2. All three lie on the full-support one-plus-three family \((x,y,y,y)\).

For \(\|A\|_F\), elementary differentiation yields

\[
x=\frac{7+\sqrt{33}}{16}
\]

and

\[
\sup\|A\|_F^2
=
\frac{23}{128}
+
\frac{11\sqrt{33}}{384}.
\]

For \(\|B\|_F\), the reduced objective is

\[
\sqrt{x(1-x)}
\log\left(\frac{3x}{1-x}\right),
\]

whose interior maximizing equation is

\[
(2x-1)\log\left(\frac{3x}{1-x}\right)=2.
\]

For \(\Pi_F\), the reduced objective is

\[
\frac{2}{3}x(1-x)(4x-1)
\log\left(\frac{3x}{1-x}\right),
\]

and its maximizing equation is

\[
(12x^2-10x+1)
\log\left(\frac{3x}{1-x}\right)=4x-1.
\]

The one-dimensional roots and all boundary cases are reproduced in the A.6.1 verification report.

## B.11 Lyapunov property and absence of cycles

Let

\[
F=\alpha D+\beta S.
\]

The Fisher flow is

\[
\dot p=\operatorname{grad}_FF.
\]

Then

\[
\dot F
=
dF(\dot p)
=
\langle\operatorname{grad}_FF,\dot p\rangle_F
=
\|\operatorname{grad}_FF\|_F^2
\geq0.
\]

A nonconstant periodic orbit would return to its initial value of \(F\) while \(F\) had strictly increased somewhere along the orbit, a contradiction. Therefore nontrivial periodic orbits are excluded.

---

---

# Supplement B. Temporal Structure and Conservative Accessibility Flow

## C.1 Four distinct structures

The manuscript distinguishes:

1. **Transition graph:** \(xRy\).
2. **History:** a chain of realized transitions.
3. **Temporal order:** a precedence relation on events.
4. **Clock:** an order-preserving numerical parameter.

No one of these is identical to thermodynamic irreversibility.

## C.2 Coarse-graining is not automatically a temporal process

A coarse-graining

\[
\pi:\mathcal X\to\bar{\mathcal X}
\]

is a map between descriptions. It can be applied once without anything happening in time.

A temporal coarse-graining process requires a family \(\pi_t\), a trajectory \(x(t)\), or an observer whose accessible algebra changes along a history.

## C.3 Conservative-flow proof

Let

\[
N=\operatorname{grad}_FD,
\qquad
A=\operatorname{grad}_F\bar D.
\]

For \(N\neq0\),

\[
P_N=I-\frac{N\otimes_gN}{\|N\|_F^2}
\]

is the Fisher-orthogonal projector to \(N^\perp\).

The flow

\[
\dot p=-P_NA
\]

satisfies

\[
\dot D
=
\langle N,-P_NA\rangle_F
=
0
\]

because \(P_NA\perp N\).

Since \(P_N\) is self-adjoint and idempotent,

\[
\dot{\bar D}
=
\langle A,-P_NA\rangle_F
=
-\langle P_NA,P_NA\rangle_F
=
-\|P_NA\|_F^2.
\]

Finally,

\[
\dot H_\pi
=
\dot D-\dot{\bar D}
=
\|P_NA\|_F^2.
\]

At \(p=u\), \(N=0\). The flow is defined separately as \(\dot p=0\).

## C.4 Direction choice

The geometry determines the tangent projection but not the sign. Thus the theorem should never be summarized as “geometry alone derives the arrow.”

The sign may be motivated by:

- low-entropy boundary conditions;
- stability;
- environmental elimination;
- retarded rather than advanced response;
- record formation;
- or a principle of dissipative accessibility.

That motivation remains to be supplied.

---

---

# Supplement C. Quantum Propositions and Counterexamples

## D.1 Classical no-purification proposition

In a finite simplex, a pure joint state is a vertex \(e_{ab}\). Marginalization maps it to \(e_a\) and \(e_b\), which are vertices of the local simplices.

Therefore no nontrivial mixed local state is the marginal of a pure classical joint state.

## D.2 Quantum purification construction

Given

\[
\rho_A=\sum_i\lambda_i|i\rangle\langle i|,
\]

let

\[
|\Psi\rangle_{AB}
=
\sum_i\sqrt{\lambda_i}|i\rangle|i\rangle.
\]

Then

\[
\begin{aligned}
\operatorname{Tr}_B|\Psi\rangle\langle\Psi|
&=
\sum_{ij}
\sqrt{\lambda_i\lambda_j}
|i\rangle\langle j|
\operatorname{Tr}(|i\rangle\langle j|)\\
&=
\sum_i\lambda_i|i\rangle\langle i|\\
&=
\rho_A.
\end{aligned}
\]

## D.3 Schmidt criterion

A pure state is separable iff it has one nonzero Schmidt coefficient. If more than one coefficient is nonzero, the reduced density matrix has rank greater than one and is mixed. Thus pure-state entanglement and local mixedness are equivalent.

## D.4 Coherence-to-entanglement conversion

The CNOT example in Section 6 gives

\[
|\phi_\theta\rangle|0\rangle
\mapsto
\cos\theta|00\rangle+\sin\theta|11\rangle.
\]

The dephased input has eigenvalues \(\cos^2\theta,\sin^2\theta\), while the input state is pure. Therefore

\[
C_r=h_2(\sin^2\theta).
\]

The reduced output has the same eigenvalues, so

\[
E=h_2(\sin^2\theta).
\]

## D.5 Why the former hidden-purity functional fails

Consider

\[
H(\rho_{AB})
=
\operatorname{Tr}(\rho_{AB}^2)
-
\operatorname{Tr}(\rho_A^2)
\operatorname{Tr}(\rho_B^2).
\]

This quantity is not always nonnegative.

Let

\[
\rho_{AB}
=
\operatorname{diag}
\left(
0,\frac15,\frac15,\frac35
\right).
\]

Then

\[
\operatorname{Tr}(\rho_{AB}^2)
=
\frac{11}{25},
\]

while

\[
\rho_A=\rho_B=
\operatorname{diag}
\left(
\frac15,\frac45
\right),
\]

so

\[
\operatorname{Tr}(\rho_A^2)
=
\operatorname{Tr}(\rho_B^2)
=
\frac{17}{25}.
\]

Therefore

\[
H
=
\frac{11}{25}
-
\left(\frac{17}{25}\right)^2
=
-\frac{14}{625}<0.
\]

Nor does positive \(H\) imply entanglement. The separable, classically correlated state

\[
\rho_{AB}
=
\operatorname{diag}
\left(
\frac12,0,0,\frac12
\right)
\]

has

\[
H=\frac12-\frac14=\frac14>0.
\]

The functional should therefore not be used as a universal hidden-coherence or entanglement measure.

## D.6 Werner-family comparison

Let

\[
\rho_W(p)
=
p|\Phi^+\rangle\langle\Phi^+|
+
(1-p)\frac I4.
\]

Its purity is

\[
\operatorname{Tr}\rho_W^2
=
\frac14+\frac34p^2,
\]

so its excess purity is

\[
P_{\mathrm{ex}}=\frac34p^2.
\]

This is positive for every \(p>0\).

The two-qubit negativity is

\[
\boxed{
\mathcal N(\rho_W)
=
\max\left\{
0,\frac{3p-1}{4}
\right\}.
}
\]

Thus the family is separable for \(p\leq1/3\) even though excess purity is positive. Purity cannot serve as an entanglement criterion.

## D.7 Reduced states do not identify their preparation

A mixed state \(\rho_A\) may arise from:

- entanglement with an environment;
- classical ignorance over preparations;
- dephasing;
- thermalization;
- or another channel.

No measurement on \(A\) alone can determine which ensemble decomposition or purification was physically used. CU should therefore say that global models can distinguish hidden from destroyed structure, not that the reduced state alone always can.

---

---

# Supplement D. Hamiltonian and Madelung Derivations

## E.1 Covariant Euler–Lagrange equation

For

\[
L=\frac12g_{ij}(q)\dot q^i\dot q^j-V(q),
\]

the coordinate Euler–Lagrange equations are

\[
\frac{d}{dt}(g_{ij}\dot q^j)
-
\frac12\partial_i g_{jk}\dot q^j\dot q^k
+
\partial_iV
=
0.
\]

Multiplication by \(g^{\ell i}\) yields

\[
\ddot q^\ell
+
\Gamma^\ell{}_{jk}\dot q^j\dot q^k
=
-g^{\ell i}\partial_iV.
\]

The right side is \(-\operatorname{grad}V\).

## E.2 Energy conservation

For time-independent \(L\),

\[
E
=
\dot q^i\frac{\partial L}{\partial\dot q^i}-L
=
\frac12g_{ij}\dot q^i\dot q^j+V.
\]

Along solutions,

\[
\frac{dE}{dt}=0.
\]

## E.3 Strong-damping expansion

Consider the normalized deterministic equation on a Riemannian configuration space,

\[
\frac{D\dot q}{dt}+\eta\dot q=F(q),
\]

where \(D/dt=\nabla_{\dot q}\) is the covariant derivative and \(F\) is a smooth vector field. Let \(\varepsilon=\eta^{-1}\). After the initial velocity boundary layer, seek a formal slow-manifold expansion

\[
\dot q
=
\varepsilon F(q)
+
\varepsilon^3G(q)
+
O(\varepsilon^5).
\]

Then

\[
\frac{D\dot q}{dt}
=
\nabla_{\dot q}\dot q
=
\varepsilon^2\nabla_{F}F
+
O(\varepsilon^4).
\]

Substitution gives

\[
G=-\nabla_{F}F.
\]

Thus, under suitable smoothness, scale-separation, and normal-hyperbolicity assumptions,

\[
\boxed{
\dot q
=
\eta^{-1}F(q)
-
\eta^{-3}\nabla_{F}F(q)
+
O(\eta^{-5}).
}
\]

For

\[
F=-\operatorname{grad}V,
\]

the leading slow flow is

\[
\dot q=-\eta^{-1}\operatorname{grad}V.
\]

If \(F=O(1)\), the absolute post-transient velocity correction is \(O(\eta^{-3})\), and its size relative to the leading \(O(\eta^{-1})\) slow velocity is \(O(\eta^{-2})\). Configuration-error scaling is not fixed by this statement alone. Rest initial data can produce an \(O(\eta^{-2})\) absolute position slip through the fast boundary layer. Leading slow-manifold initialization removes that term; for the fixed-time linear-chain test in Appendix J, the remaining state-normalized position error is \(O(\eta^{-3})\), or \(O(\eta^{-2})\) when normalized by the total \(O(\eta^{-1})\) first-order displacement. Other systems, observables, time scalings, and more accurate slow-manifold initializations can change the first visible power.

This is a formal local expansion, not by itself a global invariant-manifold theorem. The distinction is essential when interpreting a numerical comparison: the fitted error, denominator, initialization, time horizon, and treatment of the fast layer must all be stated.

## E.4 Variation of the Fisher-information term

Let

\[
I_F[\rho]
=
\int dx\,\frac{|\nabla\rho|^2}{\rho}.
\]

Its first variation is

\[
\delta I_F
=
\int dx
\left[
\frac{2\nabla\rho\cdot\nabla\delta\rho}{\rho}
-
\frac{|\nabla\rho|^2}{\rho^2}\delta\rho
\right].
\]

Integrating the first term by parts gives

\[
\frac{\delta I_F}{\delta\rho}
=
-2\frac{\nabla^2\rho}{\rho}
+
\frac{|\nabla\rho|^2}{\rho^2}.
\]

Using

\[
\frac{\nabla^2\sqrt\rho}{\sqrt\rho}
=
\frac{1}{2\rho}\nabla^2\rho
-
\frac{1}{4\rho^2}|\nabla\rho|^2,
\]

we obtain

\[
\boxed{
\frac{\delta I_F}{\delta\rho}
=
-4\frac{\nabla^2\sqrt\rho}{\sqrt\rho}.
}
\]

Multiplication by \(\hbar^2/8m\) yields the quantum-potential term

\[
-\frac{\hbar^2}{2m}
\frac{\nabla^2\sqrt\rho}{\sqrt\rho}.
\]

## E.5 Recombination into Schrödinger form

Write

\[
\psi=\sqrt\rho\,e^{i\Theta/\hbar}.
\]

Separating the Schrödinger equation into real and imaginary parts yields respectively:

\[
\partial_t\Theta+\frac{|\nabla \Theta|^2}{2m}+V
-\frac{\hbar^2}{2m}
\frac{\nabla^2\sqrt\rho}{\sqrt\rho}=0
\]

and

\[
\partial_t\rho+\nabla\cdot\left(\rho\frac{\nabla \Theta}{m}\right)=0.
\]

Conversely, where \(\rho>0\) and \(\Theta\) defines an admissible global phase, the two equations recombine into Schrödinger evolution.

---

---

# Supplement E. Dimensional and Notation Conventions

## I.1 Why dimensional discipline matters

A geometric equation may be mathematically well formed while still lacking a physical scale. The probability simplex is dimensionless, so Fisher geometry alone does not determine masses, times, energies, or coupling constants. Those scales enter through inertial coefficients, potentials, environmental rates, lattice spacing, field normalizations, and the unit convention.

This appendix distinguishes normalized mathematical equations from dimensionful physical models.

## I.2 Classical sandbox

The quantities

\[
p_i,\quad D(p),\quad S(p),\quad a,\quad b,\quad A,\quad B,\quad \Pi_E,\quad \Pi_F
\]

are dimensionless when logarithms use dimensionless probability ratios.

If the path parameter \(\lambda\) is dimensionless, \(\alpha\) and \(\beta\) are dimensionless rates per update. If \(\lambda\) is identified with physical time, then

\[
[\alpha]=[\beta]=[\mathrm{time}]^{-1}.
\]

The finite explicit-Euler step is denoted \(h\), not \(\eta\). When \(\lambda\) has time units,

\[
[h]=[\mathrm{time}].
\]

## I.3 Shannon, von Neumann, and thermodynamic entropy

With natural logarithms,

\[
S_{\mathrm{Sh}}=-\sum_i p_i\log p_i
\]

and

\[
S_{\mathrm{vN}}=-\operatorname{Tr}(\rho\log\rho)
\]

are dimensionless and measured in nats. Thermodynamic entropy is dimensionful:

\[
S_{\mathrm{th}}=k_B S_{\mathrm{dimensionless}},
\qquad
[S_{\mathrm{th}}]=[\mathrm{energy}]\,[\mathrm{temperature}]^{-1}.
\]

The symbol \(S\) should therefore always be accompanied by context when information-theoretic and thermodynamic entropy appear in the same argument.

## I.4 Fisher mechanics

The normalized Lagrangian

\[
L
=
\frac12g_\rho(\dot\rho,\dot\rho)-V(\rho)
\]

has units of inverse time squared. A dimensionful physical realization is

\[
L_{\mathrm{phys}}
=
\frac{M_F}{2}g_\rho(\dot\rho,\dot\rho)-U(\rho),
\]

where

\[
[M_F]=[\mathrm{energy}]\,[\mathrm{time}]^2,
\qquad
[U]=[\mathrm{energy}].
\]

The normalized quantities are

\[
V=\frac{U}{M_F},
\qquad
\eta=\frac{\Gamma_F}{M_F},
\qquad
\xi=\frac{\Xi}{M_F},
\]

with

\[
[V]=[\mathrm{time}]^{-2},
\quad
[\eta]=[\mathrm{time}]^{-1},
\quad
[\xi]=[\mathrm{time}]^{-2}.
\]

The paper does not derive \(M_F\), \(U\), or \(\Gamma_F\) from the coherence principle alone.

## I.5 Scalar and lattice fields

For

\[
\partial_t^2\phi-c_\phi^2\nabla^2\phi+\mu^2\phi=0,
\]

\[
[c_\phi]=[\mathrm{length}]\,[\mathrm{time}]^{-1},
\qquad
[\mu]=[\mathrm{time}]^{-1}.
\]

The physical rest mass associated with the gap is

\[
M_\phi=\frac{\hbar\mu}{c_\phi^2}.
\]

For the lattice equation

\[
\ddot\phi_n
=
\kappa_{\mathrm{lat}}
(\phi_{n+1}-2\phi_n+\phi_{n-1}),
\]

\[
[\kappa_{\mathrm{lat}}]=[\mathrm{time}]^{-2},
\qquad
c_{\mathrm{eff}}=\ell\sqrt{\kappa_{\mathrm{lat}}}.
\]

The companion Coherence Field simulation uses a coefficient \(2\kappa\) instead, so its long-wave speed is \(\ell\sqrt{2\kappa}\). Appendix J keeps these two normalizations distinct.

## I.6 Quantum density–phase action

The continuum probability density obeys

\[
[\rho]=[\mathrm{length}]^{-d},
\]

so that

\[
\int d^dx\,\rho=1.
\]

The phase field \(\Theta\) has units of action:

\[
[\Theta]=[\hbar].
\]

Then \(\nabla\Theta/m\) has units of velocity, and every term in

\[
\partial_t\Theta
+
\frac{|\nabla\Theta|^2}{2m}
+
U
-
\frac{\hbar^2}{2m}
\frac{\nabla^2\sqrt\rho}{\sqrt\rho}
=
0
\]

has units of energy.

## I.7 Relativistic scalar action

Section 9.2 uses \(c=\hbar=1\). In that convention \(m_\phi\) is an inverse-length scale. Restoring constants gives a mass term proportional to

\[
\left(\frac{M_\phi c}{\hbar}\right)^2\phi^2.
\]

The overall dimensions of \(\phi\) depend on spacetime dimension and field-action normalization.

## I.8 Symbol discipline

| Symbol | Reserved use |
|---|---|
| \(h\) | finite numerical step |
| \(\eta\) | normalized physical damping rate |
| \(\kappa_{\mathrm p}\) | resource-pump rate in the open quantum model |
| \(\gamma_{\mathrm d}\) | dephasing rate |
| \(\kappa_{\mathrm{lat}}\) | lattice restoring coefficient |
| \(\kappa_H\) | horizon surface gravity or acceleration scale |
| \(\Theta\) | Hamilton principal or phase field |
| \(S\) | entropy, with subscript where ambiguity is possible |
| \(\rho\) | density operator in Sections 5–6; probability density/configuration in Section 7, with type stated locally |
| \(V\) | normalized potential \(U/M_F\) in Fisher mechanics |
| \(U\) | dimensionful potential energy or external quantum potential, as locally specified |

## I.9 Dimensional conclusions

The dimensional audit establishes consistency after scale restoration, but it also identifies an open physical question:

\[
\boxed{
\text{information geometry does not by itself determine the physical inertia and coupling scales}.
}
\]

A completed CU model must derive, constrain, or empirically fit those scales rather than absorbing them silently into normalized units.

---

---

# Supplement F. Full Claim and Status Ledger

The following ledger records the present status of the paper’s main claims.

| Claim | Status |
|---|---|
| Coherence is a transcendental condition of describability | Philosophical argument in companion work |
| Pure structure is logically prior to physical description | Framework commitment |
| Partial separability permits distinct configurations | Bridge principle requiring fuller formalization |
| \(D(p)=\|p-u\|^2\) measures differentiation from uniformity | Definition |
| \(D\) is a complete measure of substantive coherence | Rejected |
| \(\nabla D=2(p-u)\) in Euclidean tangent coordinates | Derived |
| \(\Pi_E=-\langle\nabla D,\nabla S\rangle=2J(p,u)\) | Derived |
| \(D\) and \(S\) may locally increase together | Derived under the joint-growth inequalities |
| The four-state joint-growth wedge is strict at every nonuniform interior point | Rejected |
| The Euclidean and Fisher wedges collapse exactly on nonuniform two-level distributions | Derived |
| At fixed \(r=\beta/\alpha\), every nonuniform interior stationary point is two-level and satisfies \(r=2(a-b)/\log(a/b)\) | Derived |
| For \(r>0.621360943645626\ldots\), uniformity is the only interior stationary point of the four-state combined flow | Derived; model-specific threshold |
| Uniformity changes linear stability at \(r=1/2\); at exact criticality it is nonhyperbolic and neither a local maximum nor minimum on \(\Delta_4\) | Derived; model-specific threshold |
| Fine \(D\) decomposes into block-accessible \(D\) plus within-block differentiation | Derived |
| Shannon entropy decomposes into block entropy plus conditional within-block entropy | Derived/standard grouping identity |
| Within-block entropy equals hidden differentiation | Rejected; the quantities are opposed at fixed two-state block mass |
| Block averaging removes within-block differentiation and raises Shannon entropy by weighted KL divergence | Derived for arbitrary finite partitions |
| Differentiation loss equals entropy gain | Rejected; they share an equality set but use different functionals and weighting |
| The Fisher natural gradient uses the \(p\)-weighted projection | Derived |
| The stated global bounds for \(\|A\|_F\), \(\|B\|_F\), and \(\Pi_F\) hold on \(\Delta_4\) | Derived by KKT/face reduction and independently reproduced numerically |
| A lawful transition relation is conceptually prior to temporal duration | Philosophical bridge |
| Temporal order and temporal arrow are distinct | Conceptual result |
| Directed coarse-grained flow can make accessible \(D\) decrease and hidden \(D\) increase | Derived given the chosen flow; not an entropy theorem |
| Geometry alone selects the arrow | Rejected |
| Classical probability cannot hide correlations | Rejected |
| Classical pure global states have pure marginals | Derived |
| Every finite-dimensional quantum mixed state has a purification | Verified finite-dimensional theorem; uniqueness requires the stated ancilla qualification |
| Purification plus the five stated CDP informational axioms selects finite-dimensional complex quantum theory within that operational-probabilistic framework | Verified conditional reconstruction |
| Quantum contextuality blocks a single classical global refinement in specified measurement scenarios | Verified contextuality result |
| Purity, basis coherence, total correlation, and entanglement are distinct resources | Established distinction/derived examples |
| A CNOT can convert basis coherence into entanglement in the stated pure-state example | Derived |
| Decoherence always equals entanglement production | Rejected |
| A second-order Fisher–Rao mechanical action yields covariant Newton-type motion | Derived |
| Strong damping yields a first-order natural-gradient approximation | Derived under timescale and boundary-layer assumptions |
| The absolute post-transient slow-velocity correction is \(O(\eta^{-3})\), hence \(O(\eta^{-2})\) relative to the leading slow velocity | Formal asymptotic expansion |
| The legacy rest-initialized fixed-time position error diagnoses the post-transient correction | Rejected; it is asymptotically dominated by an \(O(\eta^{-2})\) initial-layer slip |
| In the linear chain, leading slow-manifold initialization gives \(O(\eta^{-3})\) state-normalized position error and \(O(\eta^{-2})\) displacement-normalized error | Independently reproduced by exact modal calculation |
| A positive gradient-penalty field action yields scalar waves | Derived |
| The density–phase Fisher action yields the Madelung equations | Derived |
| Madelung variables are globally equivalent to Schrödinger theory without further conditions | Rejected |
| Strictly positive accessibility edge costs yield a path metric | Derived; nonnegative costs yield a pseudometric unless zero classes are quotiented |
| A generic accessibility metric is physical space | Not established |
| A shortest-path metric is automatically differentiable in state-dependent weights | Rejected; route switching can produce nonsmoothness |
| Entanglement structure can encode geometry in specified holographic models and code subspaces | Verified external result with restricted scope |
| A scalar field carries conventional stress-energy | Derived from the stated action |
| Local-horizon thermodynamics can yield Einstein-type equations under Jacobson’s stated assumptions | Verified conditional result, including the local-equilibrium construction |
| CU independently derives the Einstein equation and \(G\) | Not established |
| Black-hole entropy is literally the sandbox hidden-differentiation residual | Rejected |
| Accessibility language organizes the distinction between hidden and destroyed information | Interpretive contribution |
| CU solves the black-hole information paradox | Not established |
| One universal scalar coherence functional governs every domain | Rejected as a current claim; domain-specific operationalization is required |
| The Double Helix is generated by the fixed autonomous first-order sandbox | Rejected |
| Driven or second-order systems may display alternating variability and consolidation | Model-dependent hypothesis |
| The coherence field is the structure of physical possibility | Metaphysical interpretation/hypothesis |

This ledger should be updated whenever the mathematics changes. It is not merely an appendix to the science; it is a map of what the science currently is.

---

# Supplement G. Principle Crosswalk and Reconciliation

## H.1 Purpose and authority

*CU Foundations* identifies itself as the canonical source for CU principle definitions and numbering. This Physics manuscript therefore does not invent a new physics-only family such as “CU-P1–CU-P5.” Instead, it maps its claims onto the established families—especially CU-FP1 through CU-FP9 and CU-D1 through CU-D10—and records where the present physics supports, qualifies, or does not yet establish the stronger canonical wording.

This appendix is a reconciliation document. It does not silently revise *CU Foundations* or the Introduction paper. Where those texts are stronger than the current physical derivation, the discrepancy is made explicit so that the canonical documents can later be revised deliberately.

## H.2 Status categories

- **Directly aligned:** the reconstructed Physics paper instantiates the principle without material qualification.
- **Aligned with qualification:** the principle is compatible with the paper, but its domain or strength must be narrowed.
- **Bridge principle:** the statement connects the CU framework to the physics but is not derived by the present mathematics.
- **Not established here:** the current paper supplies no general proof of the canonical statement.
- **Revision indicated:** the canonical wording should be reconsidered in light of the reconstructed physics.

## H.3 Foundational principles

| Principle | Canonical role | Physics status | Reconciliation |
|---|---|---|---|
| **CU-FP1 — Coherence as a Transcendental Condition** | Intelligible description presupposes sufficient relational consistency. | **Bridge principle** | The Physics paper accepts this as philosophical background. It is not an empirical theorem or a derivation of a particular physical state space. |
| **CU-FP2 — Coherence Admits of Degree and Direction** | Coherence can vary and systems can move toward or away from it. | **Aligned with qualification** | Degree and direction require a specified functional, metric, scale, and admissible dynamics. The sandbox proves degree and direction only for statistical differentiation \(D\), not for substantive coherence in general. |
| **CU-FP3 — Constraint Is Essential to Coherence** | Coherence is realized through enabling and limiting constraints. | **Directly aligned at the program level** | Constraints enter the state space, potential, admissibility conditions, and coarse-graining. The paper does not derive one universal list of physical coherence constraints. |
| **CU-FP4 — Multi-Scale Coherence** | Local and global organization interact across scales. | **Aligned with qualification** | The coarse-graining decomposition proves scale-relative accessibility for \(D\). A universal Local–Global Coherence Principle for substantive coherence remains to be formalized. |
| **CU-FP5 — Coherence Is Non-Reductive** | No single scale or description exhausts coherence. | **Aligned as an interpretive principle** | The paper supports plural measures and scale-relative descriptions, but non-reduction is not itself a quantitative physical theorem. |
| **CU-FP6 — Accessibility–Entropy Relation** *(replacement for “Entropy as Inaccessible Coherence”)* | Reduced descriptions may omit distinctions, and a specified averaging reconstruction may increase entropy. | **Derived in a restricted finite-state form; broader bridge principle** | For finite block averaging, differentiation loss and Shannon entropy gain are exact, nonnegative, and share an equality set, but they are not equal. Projection, maximum-entropy reconstruction, and physical destruction must be distinguished. Quantum, thermodynamic, and horizon entropies require their own state spaces and reductions. |
| **CU-FP7 — Coherence Collapse** | Systems may cross thresholds at which organized identity fails. | **Not established as a universal physical law** | Phase transitions, loss of stability, and failure thresholds are model-specific. The sandbox does not identify substantive collapse. |
| **CU-FP8 — Identity as Constraint-Preserved Coherence** | Identity is persistence of viability-defining constraints through change. | **Outside the minimal physical sandbox** | This principle applies most naturally to viability-bearing biological or agentive systems. Arbitrary physical configurations need not possess identity in the stronger CU sense. |
| **CU-FP9 — Discovery Principle** | Coherence constraints are objective and discoverable. | **Methodological bridge principle** | Physical constraints are treated as discoverable and fallible. The stronger claim that all cross-domain coherence constraints are objective cannot be proved by this paper alone. |

## H.4 Dynamics principles

| Principle | Physics status | Reconciliation |
|---|---|---|
| **CU-D1 — Universal Flow Equation** | **Revision indicated** | The principle-level claim that persistent systems update under constraint is retained. No single first-order equation universally governs all coherent systems, and global coherence need not increase monotonically. The first-order natural-gradient equation is one effective overdamped realization after state space, metric, potential, and environment are specified. |
| **CU-D2 — Coherence Drive** | **Aligned with qualification** | Persistence creates a selection asymmetry favoring viable organization. This is not a universal force, intention, or guarantee of improvement. |
| **CU-D3 — Biological Coherence Drive** | **Outside scope** | Requires the Biology paper’s viability-bearing systems and is not inferred from the probability sandbox. |
| **CU-D4 — Coherence Gradients** | **Partially instantiated** | The paper derives gradients of \(D\), entropy, and chosen potentials. A gradient of substantive coherence requires an independently grounded \(C_{\mathrm{sub}}\). |
| **CU-D5 — Non-Equilibrium Stability** | **Domain-qualified** | Many complex self-maintaining systems require ongoing throughput, but not every coherent physical system is far from equilibrium. Stable ground states and equilibrium phases are counterexamples to an unrestricted formulation. |
| **CU-D6 — Multi-Timescale Coherence** | **Programmatically aligned** | The Hamiltonian/overdamped distinction and coarse-graining motivate multiple timescales. A general theorem across domains is not supplied. |
| **CU-D7 — Novelty via Constraint Navigation** | **Outside present derivation** | The paper does not prove a general theory of novelty. |
| **CU-D8 — Repair over Optimization** | **Normative/design principle** | Relevant to biology, psychology, institutions, and AI; not a fundamental physical law. |
| **CU-D9 — Multi-Scale Failure Modes** | **Programmatically aligned** | Requires explicit multiscale models and cannot be inferred from the two-block identity alone. |
| **CU-D10 — Memory as Path-Dependent Coherence** | **Aligned with an important distinction** | Second-order dynamics carries local trajectory information through \((\rho,\dot\rho)\), but this enlarged phase-space state is Markovian. Full path-dependent memory requires history to alter constraints, parameters, accessible state space, or hidden variables. Velocity-based “structural memory” is therefore not identical to the stronger CU-D10 notion. |

## H.5 The Three Laws of Coherence

The current Foundations document presents three physics-like laws. The reconstructed Physics paper does not treat them as established universal laws.

### First Law: distinction–entropy accounting under specified reduction

The former coherence–entropy exchange law should be retired as a universal law. It combines two different statements that now need separate status.

**Derived finite-state theorem:**

> For a specified block-uniform conditional expectation \(E_\pi\), within-block statistical differentiation weakly decreases and Shannon entropy weakly increases. The two changes vanish under the same condition but are not identical quantities.

**Imported open-system thermodynamic constraint:**

> In a specified nonequilibrium physical system, sustained maintenance or production of organized structure may require free-energy throughput and may be accompanied by entropy export to an environment, subject to the actual thermodynamic bookkeeping.

Neither statement supplies a universal additive conservation law for substantive coherence. In reversible global models, locally inaccessible distinctions may remain encoded in correlations; in dissipative models, distinctions may genuinely be degraded. The dynamics must decide which case applies.

### Second Law: Goldilocks requirement

No universal function

\[
C\leq f(S,F)
\]

has been derived, and no general theorem shows substantive coherence vanishes at both zero and maximal entropy. The sandbox supplies four narrower ideas: differentiation ascent, state-dependent joint local growth of \(D\) and \(S\), numerical feasibility, and model-dependent developmental balance. The joint-growth wedge is not uniformly open: for the four-state fields it collapses on every nonuniform two-level family.

### Third Law: gradient dynamics

Gradient flow is one important effective dynamical form. Conservative Hamiltonian dynamics, unitary quantum dynamics, constrained flows, driven systems, and non-gradient dynamics are also physically legitimate. The universal statement should therefore be weakened to:

> When an effective scalar objective and compatible metric exist, local relaxation may be represented as motion along a natural gradient.

## H.6 The Coherence–Entropy Double Helix

For fixed \(\alpha\) and \(\beta\),

\[
\dot p
=
\operatorname{grad}_F(\alpha D+\beta S)
\]

is an autonomous gradient flow with Lyapunov function \(\alpha D+\beta S\). It cannot support a nonstationary periodic orbit. Therefore, a recurring Double Helix is not demonstrated by the first-order sandbox.

The idea remains available as a developmental hypothesis if the model includes at least one of:

- time-dependent environmental forcing;
- delayed feedback;
- additional state variables;
- multiscale coupling;
- changing viability constraints;
- or second-order inertial dynamics.

## H.7 The physical Coherence Ladder

The rebuilt paper retains the ladder as an order of logical enablement, with three corrections.

First, lawful transitions and temporal ordering are separated from irreversibility. Reversible histories can be temporally ordered.

Second, entropy is a state functional before it is an entropy rate. Temporal increase becomes meaningful only along an ordered trajectory. A preferred arrow additionally requires directed effective irreversibility or asymmetric boundary conditions.

Third, spacetime and gravity remain conditional research programs. Accessibility networks can define relational metrics; they do not by themselves derive Lorentzian signature, physical dimension, Einstein dynamics, or the equivalence principle.

A revised physical ladder is therefore:

\[
\begin{aligned}
&\text{pure relational structure}\\
&\rightarrow\text{partial separability}\\
&\rightarrow\text{distinguishable configurations}\\
&\rightarrow\text{lawful transition relations}\\
&\rightarrow\text{consistent event order}\\
&\rightarrow\text{clock parameterization}\\
&\rightarrow\text{entropy rates and records}\\
&\rightarrow\text{directed effective irreversibility}\\
&\rightarrow\text{relational geometry hypotheses}\\
&\rightarrow\text{conditional gravity program}.
\end{aligned}
\]

This sequence is not a cosmological chronology and does not claim that each arrow has already been uniquely derived.

## H.8 Canonical-document actions

The following changes should be made when *CU Foundations* and the Introduction are next revised:

1. replace CU-FP6, “Entropy as Inaccessible Coherence,” with a measure- and operation-specific Accessibility–Entropy Relation;
2. distinguish coarse projection \(\pi\), block-uniform reconstruction \(E_\pi\), and physical dynamics;
3. remove any identity equating hidden differentiation, conditional entropy, thermodynamic entropy, or quantum/horizon entropy;
4. recast CU-D1 as a principle-level viability constraint rather than a universal monotonic first-order equation;
5. remove or relabel the Three Laws as a derived restricted theorem, imported thermodynamic constraint, and model templates;
6. classify the Double Helix as an extended-dynamics hypothesis;
7. state that the Goldilocks joint-growth wedge is state-dependent and can collapse, rather than presenting one universal nonzero band;
8. separate temporal ordering from the arrow of time;
9. avoid assigning substantive coherence gradients before a domain-specific coherence functional has been grounded;
10. distinguish velocity-based state extension from full path-dependent memory;
11. retain the canonical CU-FP and CU-D numbering rather than inventing an unsupported CU-P family;
12. update downstream domain papers so that “coherence” is a shared structural concept with domain-specific operational measures, not one already-established scalar across all domains.

---

---

# Supplement H. Companion-Paper Numerical Reproduction Audit

## J.1 Scope

This appendix audits three numerical demonstrations in *The Coherence Field*:

1. lattice-wave dispersion;
2. Madelung residuals under Schrödinger evolution;
3. convergence to the overdamped first-order limit.

The A.6.1 pass reruns these demonstrations in the same deterministic suite used for the block-averaging, wedge-degeneracy, Fisher-bound, fixed-coupling, and extended overdamped checks. The public Coherence Field code reviewed during the earlier reconstruction is treated only as algorithmic lineage; the A.6.1 script is an independent local reconstruction rather than an assumption that the earlier outputs are correct.

The scripts and machine-readable results accompanying this manuscript are:

- `CU_Physics_A6_1_reproducibility.py`;
- `CU_Physics_A6_1_verification_results.json`.

All reported Monte Carlo tests use seed \(20260909\); the exact theorems do not depend on sampling.

## J.2 Lattice-wave dispersion

The public script evolves

\[
\ddot C_i
=
2\kappa
(C_{i+1}-2C_i+C_{i-1})
\]

with periodic boundaries, \(N=128\), \(\kappa=1\), \(T=200\), and \(dt=0.05\). The exact lattice dispersion is

\[
\boxed{
\omega(k)
=
2\sqrt{2\kappa}
\left|\sin\frac{k}{2}\right|.
}
\]

Section 7 uses the convention \(V=(\kappa_{\mathrm{lat}}/2)\sum(\Delta C)^2\), while the companion script uses \(V=\kappa\sum(\Delta C)^2\). They agree under

\[
\boxed{\kappa_{\mathrm{lat}}=2\kappa}.
\]

Independent leapfrog integration and FFT extraction reproduce the reported mode frequencies. Representative results are:

| Mode | \(k/\pi\) | Measured \(\omega\) | Exact \(\omega\) | Relative error |
|---:|---:|---:|---:|---:|
| 3 | 0.046875 | 0.219857 | 0.208072 | \(5.66\times10^{-2}\) |
| 10 | 0.156250 | 0.690978 | 0.687252 | \(5.42\times10^{-3}\) |
| 32 | 0.500000 | 2.010117 | 2.000000 | \(5.06\times10^{-3}\) |
| 63 | 0.984375 | 2.826727 | 2.827575 | \(3.00\times10^{-4}\) |

The low-mode error is dominated by the finite FFT window, as claimed.

### Sign and energy correction

The companion paper and public script describe the stable force as arising from

\[
V=-\kappa\sum_i(C_{i+1}-C_i)^2.
\]

That sign is inconsistent with ordinary Hamiltonian mechanics. The simulated stable equation follows from

\[
\boxed{
V=+\kappa\sum_i(C_{i+1}-C_i)^2
}
\]

for the coefficient convention above. Its conserved physical energy is

\[
\boxed{
E
=
\frac12\sum_i\dot C_i^2
+
\kappa\sum_i(C_{i+1}-C_i)^2.
}
\]

The printed expression with a minus sign oscillates by nearly \(200\%\) relative to its initial magnitude and is not conserved.

For \(T=100\) and \(dt=0.01\), the maximum relative oscillation of the correct leapfrog energy ranges from approximately \(1.2\times10^{-7}\) for mode 1 to \(2.0\times10^{-4}\) for mode 63. The companion claim of a \(3\times10^{-10}\) bound is not reproduced under the stated algorithm and parameters.

The reconstructed Physics paper already uses the stable positive lattice potential and is therefore not dependent on the companion sign error.

## J.3 Madelung residuals

The independent reproduction uses the stated harmonic-oscillator example:

\[
N=512,\quad
L=40,\quad
dt=10^{-3},\quad
T=5,\quad
\hbar=m=\omega=1.
\]

A split-step Fourier solver evolves Schrödinger’s equation. Time derivatives are extracted from the same Schrödinger right-hand side, the continuity flux is differentiated with a second-order central difference, and the quantum potential uses a spectral Laplacian.

The reproduced results are:

| Quantity | Reproduced value |
|---|---:|
| Maximum continuity residual | \(5.58\times10^{-3}\) |
| Median continuity residual | \(2.95\times10^{-3}\) |
| Maximum Hamilton–Jacobi residual | \(3.71\times10^{-11}\) |
| Median Hamilton–Jacobi residual | \(7.51\times10^{-12}\) |

The continuity residual converges by a factor of approximately four when the grid spacing is halved:

| \(N\) | Median continuity residual |
|---:|---:|
| 256 | \(1.17\times10^{-2}\) |
| 512 | \(2.95\times10^{-3}\) |
| 1024 | \(7.38\times10^{-4}\) |

This confirms second-order spatial convergence.

The correct conclusion is:

> The Hamilton–Jacobi identity is satisfied at floating-point residual levels under the chosen substitution, while the continuity residual is \(O(\Delta x^2)\), approximately \(10^{-3}\) at \(N=512\).

It is therefore inaccurate to say that **both** Madelung equations are verified “to machine precision.”

This experiment is a discretization and algebra consistency check, not independent empirical evidence for the Madelung equations, because the time derivatives are extracted from the same Schrödinger right-hand side used to generate the reference evolution.

### Additional sanity checks

Under the stated implementation, the audit finds approximately:

\[
\max_t\left|\frac{\|\psi(t)\|^2}{\|\psi(0)\|^2}-1\right|
\approx
1.95\times10^{-13},
\]

and

\[
\max_t\left|\frac{E(t)}{E(0)}-1\right|
\approx
1.75\times10^{-7}.
\]

The time-averaged kinetic and potential energies over \(T=5\) differ by about \(21\%\). Therefore, stronger companion claims of \(10^{-11}\)-level energy conservation or \(10^{-3}\)-level virial agreement over the stated interval are not reproduced.

## J.4 Overdamped-limit comparison

The companion implementation evolves an open \(N=32\) chain with

\[
\ddot C+\eta\dot C=2\kappa\Delta_{\mathrm{open}}C
\]

and compares it at \(T=5\) with

\[
\dot C
=
\frac{2\kappa}{\eta}\Delta_{\mathrm{open}}C.
\]

A.6 reproduced the legacy rest-initialized, state-normalized \(L^\infty\) position errors:

| \(\eta\) | Legacy relative position error |
|---:|---:|
| 1 | \(8.2630\times10^{-2}\) |
| 3 | \(8.3697\times10^{-3}\) |
| 10 | \(1.7506\times10^{-3}\) |
| 30 | \(3.5520\times10^{-4}\) |
| 100 | \(4.0041\times10^{-5}\) |
| 300 | \(4.7537\times10^{-6}\) |

The fit over \(\eta\geq30\) has slope \(-1.8725\). That reproduction remains correct, but the independent A.6 audit identified a methodological confound: rest initialization creates a fast boundary layer whose one-time position slip is itself \(O(\eta^{-2})\). The fitted slope therefore does not isolate the \(-\eta^{-3}\nabla_FF\) post-transient correction.

A.6.1 diagonalizes the symmetric open-chain Laplacian and evaluates every normal mode analytically. This removes stiff-integration ambiguity and extends the sweep to

\[
\eta\in\{10,30,100,300,1000,3000\}.
\]

Two second-order initializations are compared:

1. **rest:** \(\dot C(0)=0\);
2. **leading slow manifold:** \(\dot C(0)=2\kappa\Delta_{\mathrm{open}}C(0)/\eta\).

All reported norms are \(L^\infty\). Position error in the first two columns is normalized by the first-order state norm at \(T\); velocity error is normalized by the first-order velocity norm.

| \(\eta\) | Position error, rest | Position error, slow manifold | Velocity error, rest | Velocity error, slow manifold |
|---:|---:|---:|---:|---:|
| 10 | \(1.7537\times10^{-3}\) | \(1.4288\times10^{-3}\) | \(1.1925\times10^{-2}\) | \(3.1190\times10^{-3}\) |
| 30 | \(3.5532\times10^{-4}\) | \(7.9485\times10^{-5}\) | \(2.1075\times10^{-3}\) | \(8.7611\times10^{-4}\) |
| 100 | \(4.0041\times10^{-5}\) | \(2.5258\times10^{-6}\) | \(2.2691\times10^{-4}\) | \(1.0795\times10^{-4}\) |
| 300 | \(4.7537\times10^{-6}\) | \(9.8238\times10^{-8}\) | \(2.6591\times10^{-5}\) | \(1.3083\times10^{-5}\) |
| 1000 | \(4.3797\times10^{-7}\) | \(2.6990\times10^{-9}\) | \(2.4388\times10^{-6}\) | \(1.2136\times10^{-6}\) |
| 3000 | \(4.8991\times10^{-8}\) | \(1.0046\times10^{-10}\) | \(2.7245\times10^{-7}\) | \(1.3601\times10^{-7}\) |

Fitting the upper decade \(300\leq\eta\leq3000\) gives:

| Error observable | Rest initialization | Leading slow-manifold initialization |
|---|---:|---:|
| Position error / first-order state norm | \(-1.9868\) | \(-2.9902\) |
| Position error / total first-order displacement | \(-0.9879\) | \(-1.9913\) |
| Velocity error / first-order velocity | \(-1.9894\) | \(-1.9830\) |

The asymptotic interpretation is therefore observable-specific:

- with rest initialization, state-normalized fixed-time position error is \(O(\eta^{-2})\) because of initial-layer slip;
- with leading slow-manifold initialization, state-normalized fixed-time position error is \(O(\eta^{-3})\), exposing the absolute post-transient correction;
- because the total first-order displacement over fixed \(T\) is \(O(\eta^{-1})\), the slow-manifold position error relative to that displacement is \(O(\eta^{-2})\);
- velocity error relative to the first-order velocity is \(O(\eta^{-2})\) under both initializations after the fast transient.

Thus the expansion and the original numerical values were not mathematically inconsistent. The error in A.6 was evidential: it treated a boundary-layer-dominated slope as support for a post-transient term that the chosen test did not isolate.

### Mode and boundary qualification

For the open chain, the lowest nonzero frequency in the stated normalization is

\[
\omega_1=0.1387843410\ldots,
\]

and the highest is

\[
\omega_{\max}=2.8250201604\ldots .
\]

The largest modal critical damping is therefore

\[
\eta_{c,\max}=2\omega_{\max}=5.6500403208\ldots,
\]

so every point in the extended sweep lies in the overdamped regime for every nonzero mode. A multimode profile still has no single dynamically informative damping threshold below this maximum; each mode has its own rate and boundary-layer amplitude.

## J.5 Reproducibility record

The earlier reconstruction used the public Coherence Field scripts then available to identify the intended wave, Madelung, and damping algorithms. A.6.1 retains those historical reproductions but rebuilds the calculations in one independent script with explicit parameters, deterministic sampling, convergence checks, exact modal evaluation for the extended overdamped test, and machine-readable output.

The generated report records:

- Python, NumPy, SciPy, and platform versions;
- the random seed;
- the SHA-256 hash of the executing script;
- every simulation parameter;
- all sampled residual maxima;
- all reduced optimization cases used in the Fisher-bound audit.

The repository copy reviewed during the earlier reconstruction retained a negative lattice-potential sign, placeholder setup text, and a \(1/\eta\) fixed-time error interpretation. Those historical issues do not affect the analytic results in the present Physics manuscript, but any future archival companion release should correct them.

## J.6 Consequences for this manuscript

The reconstructed Physics paper does not rely on the disputed companion numerical claims. It retains only conclusions supported independently:

1. the stable positive gradient potential yields the lattice-wave equation and exact dispersion;
2. the density–phase action yields the Madelung equations analytically, with global phase caveats;
3. the damped second-order equation converges to a first-order slow flow under strong damping;
4. numerical residuals are diagnostic checks rather than empirical confirmation;
5. asymptotic error orders must be stated according to the observable and initial-layer convention.

The companion paper should be revised separately so that its prose, equations, code comments, energy expression, and scaling interpretation agree.

---

---

# Supplement I. A.6 Theorem and Structural Audit

## K.1 Scope

A.6 tests the four areas left exposed after A.5:

1. the exact relation among coarse-graining, hidden differentiation, conditional entropy, and entropy gain;
2. the width and degeneracy of the Fisher/Euclidean joint-growth wedge;
3. the global size of the Fisher vector fields on \(\Delta_4\);
4. the mathematical assumptions added in the second-order, geometry, and gravity sections.

The audit combines symbolic derivation, exhaustive low-dimensional reduction, deterministic numerical reproduction, and comparison with the original Physics manuscript. Numerical sampling is used as a diagnostic, never as the proof of an exact theorem.

## K.2 Block-averaging verification

For \(200{,}000\) samples from the uniform Dirichlet distribution on \(\Delta_4\), the maximum absolute residuals were:

| Identity | Maximum residual |
|---|---:|
| \(D=\bar D+H_\pi^{(D)}\) | \(2.22\times10^{-16}\) |
| \(D(p)-D(E_\pi p)=H_\pi^{(D)}\) | \(2.22\times10^{-16}\) |
| Shannon grouping identity | \(7.77\times10^{-16}\) |
| Entropy-gain KL identity | \(9.44\times10^{-16}\) |

A six-state test with block sizes \((3,2,1)\) reproduced the general differentiation and entropy identities with residuals below \(9\times10^{-16}\).

Sampling-dependent correlations are intentionally not promoted to framework invariants. Under the stated Dirichlet sampling, hidden differentiation correlates negatively with within-block entropy and positively with entropy gain, but the coefficients change with the sampling measure. The exact identities and equality sets are the canonical result.

## K.3 Wedge-degeneracy verification

Two hundred thousand random interior samples produced no violation of the Cauchy–Schwarz wedge ordering under either the Euclidean or Fisher metric. Random sampling, however, almost surely avoids exact two-level states.

Direct construction of all three multiplicity families—one-plus-three, two-plus-two, and three-plus-one—gave

\[
|1-\chi|<5\times10^{-16}
\]

and wedge widths below \(5\times10^{-16}\) in both geometries, confirming exact antiparallelism to floating-point precision.

Along a generic approach to uniformity, the measured widths scaled toward zero while both edges approached \(1/2\). The analytic proof in Appendix B, rather than these samples, establishes the exact degeneracy set.

This finding corrects two tempting but false readings:

- the wedge is not strict at every nonuniform interior state;
- the degeneracy set is not limited to the finitely many distributions uniform on their support.

It contains continuous lower-dimensional families of all interior two-level distributions.

## K.4 Fisher-field bounds

The KKT equations reduce every face extremum to at most two distinct positive coordinate values. Exhaustive support and multiplicity comparison gives:

| Quantity | Global maximum | Maximizing full-support distribution, up to permutation |
|---|---:|---|
| \(\|A\|_F\) | \(0.586724197682029\) | \((0.796535165408627,0.067821611530458,0.067821611530458,0.067821611530458)\) |
| \(\|B\|_F\) | \(1.011677099862651\) | \((0.851495212071545,0.049501595976152,0.049501595976152,0.049501595976152)\) |
| \(\Pi_F\) | \(0.586672264109138\) | \((0.820298289564512,0.059900570145163,0.059900570145163,0.059900570145163)\) |

The report retains every lower-dimensional candidate so the global comparison can be independently inspected.

## K.5 Sections 7–9 audit

The audit supports the principal A.5 derivations but adds four corrections or qualifications.

1. **Strong damping:** the slow-manifold correction must use the covariant derivative \(\nabla_{F}F\). The legacy rest-initialized fixed-time position error is \(O(\eta^{-2})\) because of the fast initial layer and does not isolate that correction. A.6.1’s exact modal test separates initialization and normalization: the post-transient velocity correction is \(O(\eta^{-3})\) absolutely and \(O(\eta^{-2})\) relative to the leading slow velocity.
2. **Lattice waves:** the main-text and companion coefficients agree only after stating \(\kappa_{\mathrm{lat}}=2\kappa\). The stable force derives from a positive gradient potential.
3. **Relational distance:** the logarithmic edge map requires a positive floor for a genuine metric; without it, zero-cost edges produce a pseudometric. State-dependent shortest-path geometry is generally nonsmooth at route switches.
4. **Jacobson route:** the conditional gravity argument requires a local-equilibrium horizon construction in addition to the area law, Unruh temperature, Clausius relation, Raychaudhuri focusing, and stress-energy conservation.

No further algebraic error was found in the natural-mechanical Euler–Lagrange equation, scalar stress-energy tensor, Fisher-information variation, Madelung equations, or Schrödinger recombination subject to the stated global-phase qualification.

## K.6 Reproducibility files and interpretation

The accompanying script generates the JSON report from scratch. Its heavy checks include:

- \(200{,}000\)-sample block and wedge diagnostics;
- exact fixed-coupling threshold and critical-direction checks;
- all reduced Fisher extrema for support sizes two through four;
- the 128-site lattice-wave dispersion test;
- Madelung residuals at \(N=256,512,1024\);
- the legacy overdamped comparison for \(\eta=1,3,10,30,100,300\);
- the exact-modal two-initialization comparison for \(\eta=10,30,100,300,1000,3000\).

The numerical wave and Madelung tests are consistency checks for the discretizations and selected equations. They are not independent evidence that CU uniquely derives those equations or that the equations describe new physics.

---

---

# Supplement J. Independent A.6 Audit Response and A.6.1 Verification

## L.1 Scope and disposition

A separate independent model audit re-derived the headline A.6 results without reading the supplied JSON as its source of truth. It confirmed:

- the finite-partition differentiation and entropy identities;
- the exact two-level wedge-degeneracy characterization in both metrics;
- the critical two-level ratio \(2(a-b)/\log(a/b)\);
- strict wedge width at sampled states with at least three distinct coordinate values;
- the stated global Fisher-field extrema; and
- the covariant strong-damping expansion.

It also reported that the A.6 corrections had propagated consistently: the rejected entropy identity did not survive outside passages explicitly identifying it as rejected, and the wedge theorem was stated consistently across the manuscript and appendices.

This is meaningful independent checking, but it is not represented as human expert peer review. The audit itself states that it did not independently verify Sections 8–10, the Madelung derivation, the lattice and Madelung convergence runs, or the bibliography.

## L.2 Accepted action item: the overdamped diagnostic

The audit correctly identified that the A.6 slope test did not measure what the surrounding prose implied. The six-point rest-initialized table is reproducible, and its large-\(\eta\) state-normalized position error really is \(O(\eta^{-2})\). But that leading term is produced by the fast initial layer. It is not evidence for the post-transient \(-\eta^{-3}\nabla_FF\) velocity correction.

A.6.1 therefore:

1. preserves the legacy table as a reproduction rather than discarding it;
2. extends the sweep through \(\eta=3000\);
3. reports rest and leading slow-manifold initialization separately;
4. states every fitted numerator and denominator;
5. evaluates the linear chain by exact modal decomposition; and
6. replaces one undifferentiated scaling claim with three observable-specific asymptotic statements.

The audit suggested that slow-manifold initialization should reveal \(O(\eta^{-2})\) fixed-time position behavior. For the actual linear-chain observable used here, the more precise result is:

\[
\text{state-normalized position error}=O(\eta^{-3}),
\]

whereas

\[
\text{displacement-normalized position error}=O(\eta^{-2}).
\]

The relative velocity error is \(O(\eta^{-2})\). This is not a disagreement about the formal expansion; it is the consequence of distinguishing absolute/state-normalized position error from error normalized by an \(O(\eta^{-1})\) displacement.

## L.3 Accepted extension with terminological correction: fixed coupling

The audit proposed that at fixed \(r=\beta/\alpha\), the “degeneracy set” becomes discrete and disappears above \(0.6213609436\ldots\). The derived threshold is correct, but “degeneracy set” is ambiguous.

The **geometric wedge-degeneracy set** is independent of the chosen coupling. It remains the continuous union of the nonuniform one-plus-three, two-plus-two, and three-plus-one two-level families.

The **fixed-coupling stationary intersection** consists of those degenerate states whose collapse ratio equals the selected \(r\). That intersection is finite up to permutation, and it is empty for

\[
r>r_*=0.621360943645626\ldots .
\]

A.6.1 adopts the threshold while preserving this distinction. Saying that “no state is wedge-degenerate” above \(r_*\) would be false; the correct statement is that no nonuniform interior state is stationary for that fixed combined flow.

## L.4 Accepted extension with critical-case correction: \(r=1/2\)

The audit correctly identifies \(r=1/2\) as the value at which the tangent Hessian at uniformity changes sign. Therefore uniformity is linearly repelling under ascent for \(r<1/2\) and locally attracting for \(r>1/2\).

At exact equality, however, the Hessian vanishes and the cubic term is generically nonzero. Uniformity is neither a local maximum nor a local minimum on \(\Delta_4\). The audit’s numerical table labelled the \(r=1/2\) run “collapsing,” although its own reported differentiation increased slightly. A.6.1 therefore states a **linear-stability threshold with a nonhyperbolic critical case**, not attraction at equality.

The audit also suggested classifying all other stationary two-level points as maxima or saddles. That fuller Morse-type classification is not imported here because it was not proved across every multiplicity branch and parameter range in the audit. The manuscript records only the stationary-point and uniform-stability results independently secured by the A.6.1 derivation.

## L.5 Canonical consequence

The A.6.1 changes are internal refinements of the four-state sandbox and the overdamped verification. They do not restore a universal scalar coherence measure, a universal Goldilocks coupling, or a universal physical law. The canonical principle dispositions established in Appendix H and the v0.10 M&E/Foundations B.2 base therefore remain unchanged.

Physics A.6.1 supersedes A.6 as the current technical base. A.6 remains part of the correction history together with the independent audit memo, the A.6-to-A.6.1 patch, the executable verification suite, and the machine-readable results.

---

---

# Supplement K. Editorial and Source Map

## F.1 Primary manuscript basis

This reconstruction uses the latest uploaded Physics manuscript as its principal source. It preserves:

- the title and overall physical program;
- the Coherence Ladder;
- the classical \(N=4\) sandbox;
- the coherence–entropy interplay;
- the emergence-of-time program;
- the quantum lift;
- the accessibility-based geometry program;
- the Jacobson-style gravity route;
- horizon and black-hole applications;
- the Universal Flow Equation;
- and the Double Helix hypothesis.

## F.2 Companion CU sources

The reconstruction also draws conceptually on:

- the CU Introduction/Metaphysics and Epistemology paper for the ladder, transcendental framing, and consequence structure;
- CU Foundations for principle-level definitions and numbering;
- The Coherence Field for the second-order Hamiltonian formulation, wave realization, Madelung/Schrödinger construction, gravity consistency program, and overdamped limit;
- The Foundational Substrate for the physical-possibility interpretation;
- the Biology, Consciousness, Psychology, Social Dynamics, AI, and Ethics papers only where necessary to preserve cross-domain terminology.

No companion-paper claim is treated as externally verified merely because it appears elsewhere in the CU corpus. Appendix J independently reproduces the principal numerical examples from *The Coherence Field* and separates successful replication from claims requiring correction.

## F.3 Major retained insights

The reconstruction retains the following ideas in strengthened form:

1. logical emergence should be distinguished from temporal emergence;
2. accessibility is scale- and context-relative;
3. coarse-graining may hide rather than destroy structure;
4. information geometry provides a common state-space language;
5. second-order and first-order dynamics can be related by damping;
6. globally pure quantum states may appear locally mixed;
7. local coherence can become global entanglement;
8. spacetime may be approached through relational accessibility;
9. gravity may admit a thermodynamic/accessibility interpretation;
10. the framework should state explicit abandonment conditions.

## F.4 Major claims narrowed or removed

The reconstruction does not retain as established:

1. non-uniformity as substantive physical coherence;
2. universal monotone Goldilocks bounds from the old sign convention;
3. arithmetic-mean Fisher projection;
4. positive \(\Pi\) as gradient alignment;
5. hidden correlation as a proof of quantum necessity;
6. excess purity as entanglement;
7. a universal quantum Goldilocks band;
8. automatic CPTP status for natural-gradient flows;
9. direct derivation of spacetime from an arbitrary correlation graph;
10. derivation of the equivalence principle from path optimization;
11. derivation of Einstein equations without horizon assumptions;
12. resolution of black-hole information by terminology alone;
13. recurring Double Helix dynamics from an autonomous gradient system.

## F.5 Comparison checklist for a second reconstruction

When the independently reconstructed manuscript is available, compare:

- definition of coherence versus differentiation;
- Euclidean and Fisher gradients;
- sign and meaning of \(\Pi\);
- exact finite-step identity;
- status of Goldilocks results;
- coarse-graining proof;
- time versus arrow;
- conservative flow and direction choice;
- classical purification limitation;
- operational reconstruction assumptions;
- quantum resource measures;
- coherence-to-entanglement conversion;
- quantum-channel admissibility;
- Hamiltonian/overdamped relation;
- Madelung assumptions and Wallstrom caveat;
- metric construction from accessibility;
- Lorentzian and dimensionality gaps;
- Jacobson assumptions;
- black-hole claim strength;
- Double Helix dynamics;
- falsifiability and verification queues.

---

---

# Supplement L. Figure Program

## Figure 1. The physical Coherence Ladder

A dependency diagram separating:

- logical enablement;
- bridge principles;
- physical dynamics;
- and effective emergence.

The figure should visually distinguish solid arrows for derivations from dashed arrows for bridge assumptions.

## Figure 2. Differentiation and entropy on \(\Delta_4\)

A simplex projection showing:

- the uniform point;
- differentiation-gradient directions;
- entropy-gradient directions;
- an open joint-growth wedge at a state with at least three distinct coordinate values;
- a collapsed wedge on a two-level state;
- and the boundary band \(\Delta_4(\epsilon)\).

The figure should display the normalized opposition \(\chi\) and show that the wedge width tends to zero as \(\chi\to1\).

## Figure 3. Projection, grouping, and block-uniform reconstruction

A four-state distribution should be shown in three related representations:

\[
p
\xrightarrow{\ \pi\ }
q=(q_A,q_B),
\]

and

\[
p
\xrightarrow{\ E_\pi\ }
\widetilde p
=
\left(\frac{q_A}{2},\frac{q_A}{2},\frac{q_B}{2},\frac{q_B}{2}\right).
\]

The first panel should display

\[
D(p)=\bar D(q)+H_\pi^{(D)}(p),
\]

and the second

\[
S(E_\pi p)-S(p)
=
\sum_bq_b\operatorname{KL}(r^{(b)}\|\nu_2).
\]

The differentiation loss and entropy gain should share an equality marker but must not be drawn as numerically identical or as a conserved substance.

## Figure 4. Temporal architecture

A four-layer diagram:

\[
\text{transition graph}
\rightarrow
\text{partial order}
\rightarrow
\text{clock}
\rightarrow
\text{arrow}.
\]

## Figure 5. Classical and quantum purification

Side-by-side panels:

- classical pure global state \(\to\) pure marginals;
- quantum pure entangled state \(\to\) mixed marginals.

## Figure 6. Coherence-to-entanglement conversion

The CNOT circuit:

\[
|\phi_\theta\rangle|0\rangle
\rightarrow
\cos\theta|00\rangle+\sin\theta|11\rangle
\]

with equal input basis coherence and output entanglement entropy.

## Figure 7. Dynamical regime map

Axes:

- damping strength;
- state-space/potential choice.

Regions:

- Hamiltonian wave;
- Schrödinger/Madelung;
- damped oscillation;
- overdamped gradient flow.

## Figure 8. Accessibility-to-geometry pipeline

\[
\rho
\rightarrow
w_{ij}[\rho]
\rightarrow
\ell_{ij}
\rightarrow
d_G
\rightarrow
\text{continuum diagnostics}.
\]

Each unresolved bridge should be visibly marked.

## Figure 9. Claim-status map

A summary diagram showing which Physics-paper conclusions are:

- derived;
- conditional;
- hypothetical;
- or interpretive.

## Figure 10. Conditional gravity chain

A dependency diagram:

\[
\text{pre-geometric relations}
\rightarrow
\text{accessibility network}
\rightarrow
\text{Lorentzian continuum}
\rightarrow
\text{horizon entropy}
\rightarrow
\text{Einstein-type equation}.
\]

Each arrow should be labeled either derived, imported, or open.

## Figure 11. Horizon accessibility and recoverability

A triptych showing:

1. global state and exterior reduction;
2. information redistribution into radiation correlations;
3. a recovery map acting on a sufficiently large radiation subsystem.

The figure should distinguish ontological preservation from practical recoverability.

## Figure 12. CU Physics research sequence

A staged roadmap from:

\[
C_{\mathrm{sub}}
\rightarrow
\text{admissible dynamics}
\rightarrow
\text{quantum reconstruction}
\rightarrow
\text{non-geometric network}
\rightarrow
\text{continuum geometry}
\rightarrow
\text{gravity}
\rightarrow
\text{novel prediction}.
\]

Failure branches should be shown explicitly so that the diagram represents a falsifiable program rather than an inevitable ascent.

---

---

# Publication-Copy Clarifications Added After the A.6.1 Archive

## Multiplicity convention

Throughout the fixed-coupling branch analysis, \(q=a/b>1\), so the multiplicity label counts coordinates carrying the larger value \(a\). Exchanging \(a\) and \(b\) relabels the complementary branch. The apparent three-plus-one maximum \(0.6213609436\ldots\) is therefore the same unordered family as the listed one-plus-three branch.

## Three-regime observation

Combining the proved local stability threshold at \(r=1/2\) with the proved nonuniform-stationarity ceiling \(r_*\approx0.621360943645626\) yields three analytically distinguished regions:

1. \(r<1/2\): the uniform state is locally repelling;
2. \(1/2<r\le r_*\): the uniform state is locally attracting while nonuniform interior stationary points exist;
3. \(r>r_*\): uniformity is the only interior stationary point.

Numerical integrations suggest bistability in the middle region and relaxation to uniformity for tested starts in the upper region. Those global statements remain hypotheses rather than theorems pending stationary-branch stability analysis, boundary classification, basin analysis, and a convergence proof.


# Supplement N. Licensed Commitments Architecture

Section 13 implements the corpus-wide Licensed Commitments Architecture RC1.

The statements “All matter is sacred,” “physical law may be received as sacred disclosure,” and “cosmic history may be received as unfinished emergence” are commitment- or interpretation-register claims. They are not entries in the physical claim ledger and are not evidence for any physical model.

The section is constrained by PHYS-A6.1–A6.12, especially the rejection of a universal physical coherence scalar, the conditional status of quantum selection, the incomplete state of accessibility geometry, and the interpretive status of foundational-substrate claims.


# Commitment Principle Crosswalk

CU-COM7 — **Reverence for Matter and Physical Law** is the official commitment anchor for the reader-facing manuscript.

**Statement:** Coherence Universalism commits to receiving matter, energy, physical process, and lawful order with reverence. Scientific inquiry is treated as disciplined attention to a reality human beings did not create.

**Boundary:** This commitment does not imply particle consciousness, equal moral status for every physical configuration, moral prescriptions from equations, or inevitable cosmic progress.

**Revision condition:** Its metaphysical language must be narrowed whenever it misstates physical results, blocks criticism, or treats scientific models as final revelation.
