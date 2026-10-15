# Coherence Universalism: Ethics
## RC3 Release-Convergence Wave 4 — Technical Supplement

**Status and authority.** This is the released technical supplement for the Wave 4 cumulative manuscript. The [reader-facing manuscript](../papers/08_CU_Ethics_v0.10.md) controls current wording, claim status, and canonical cross-references. This supplement exposes the formal derivations, deterministic contrast constructions, claim ledgers, audit materials, scripts, and source records on which the manuscript relies.

- **Evidence directory:** [08_Ethics](../evidence/08_Ethics/README.md)
- **Archived source package:** [CU_Ethics_v0.10_Publication_PC2.zip](../provenance/archival_source_packages/CU_Ethics_v0.10_Publication_PC2.zip)
- **Current supplement path:** `technical_supplements/08_Ethics_Technical_Supplement_v0.10.md`

Reproducibility of a construction shows only that its output follows from its declared assumptions and code. It does not convert a toy model or simulation into target-domain empirical validation. Where this preserved archive uses historical identifiers or statuses, the Wave 4 normalized registries and current manuscript control.

# Wave 4 evidence-access addendum

Wave 4 makes previously referenced but inaccessible materials available in one package. It includes the substantive legacy supplement below, the independent audit and check script, recorded audit output where available, source ledgers, deterministic scripts and generated results where they existed, and the complete pre-RC3 source package for provenance.

# Preserved substantive technical archive

**Gaura Kiśora Dās Rader**  
**Heaven≡Earth Foundation**  
**September 2026**

## Scope

This supplement preserves the formal, computational, registry, audit, and revision materials underlying the reader-facing Ethics paper. The technical authority remains the audited G.1.1 reconstruction and Canonical Base B.4 where a discrepancy is found. The supplement is not an automated moral decision procedure and does not validate the stipulated profile values as empirical measures.

## Contents

- Appendices A–G from the audited technical authority
- Independent-audit disposition
- Truth-centered publication transformation map
- Reproducibility and evidential boundary

# Appendix A. Formal Architecture and Non-Entailment Results

This appendix records formal distinctions used in the manuscript. The propositions are not intended to reduce ethics to set theory or numerical optimization. Their function is narrower: to prevent one ethical consideration from being treated as if it logically entailed another.

## A.1 Ethical admissibility and comparison

Let:

- \(U^{\mathrm{feas}}\) be the actions or policies treated as feasible under the declared model;
- \(U^{\mathrm{pres}}\subseteq U^{\mathrm{feas}}\) be the subset actually presented for screening and comparison;
- \(A\) a declared set of affected beings or groups;
- \(Z=\{1,\ldots,m\}\) a set of positively oriented ethical dimensions;
- \(z_{aj}(u,\omega)\in[0,1]\) the outcome for affected party \(a\), dimension \(j\), option \(u\), and scenario \(\omega\);
- \(k_{aj}\) a protected floor;
- \(\mathbb P\) a declared probability or credal model; and
- \(\delta\) a declared maximum probability of floor violation.

A generic floor-screened option set is

\[
U_K^{\mathrm{pres}}
=
\left\{
 u\in U^{\mathrm{pres}}:
 \Pr\!\left[
  z_{aj}(u,\omega)\ge k_{aj}
  \text{ for all protected }(a,j)
 \right]
 \ge 1-\delta
\right\}.
\]

The notation does not determine the floors, the affected-party map, the probability model, or the admissible exception structure. Those remain normative and empirical responsibilities. Nor does it determine whether \(U^{\mathrm{pres}}\) is an adequate representation of \(U^{\mathrm{feas}}\). For brevity, later propositions use \(U_K\) where the presented set is fixed, but every result remains conditional on that set.

Once options are screened, define Pareto dominance on an aggregate or disaggregated profile by

\[
u\succ_P v
\quad\Longleftrightarrow\quad
z_j(u)\ge z_j(v)\ \forall j
\text{ and }
z_{j^*}(u)>z_{j^*}(v)
\text{ for some }j^*.
\]

A scalarization

\[
V_w(u)=\sum_{j=1}^{m}w_jz_j(u),
\qquad
w_j\ge0,
\qquad
\sum_jw_j=1,
\]

is a secondary comparison rule. It is not a substitute for the floor structure or a discovered universal moral value function.

## A.2 Proposition: justificatory integrity is not sufficient for permissibility

**Proposition A.1.** A decision can be descriptively truthful, internally consistent, and sincerely defended while remaining morally impermissible.

**Construction.** Let \(u\) be a policy whose designers accurately disclose its expected aggregate benefit, its distributive effects, and its purpose. Suppose the policy predictably imposes a severe avoidable burden below a protected welfare floor on a politically excluded group, despite the availability of a less harmful alternative. No false assertion, hidden premise, or motivated evidential distortion is required for the policy's defense. Its justificatory record may therefore score highly on truthfulness while failing standing, noncompensation, agency, legitimacy, or protected-welfare conditions.

**Conclusion.** Justificatory integrity can exclude one important class of moral failure. It does not entail adequate recognition, proportionate burden, legitimate authority, or permissibility. \(\square\)

This proposition is the decisive correction to the March 2026 architecture. The earlier paper identified a real structural wrong but treated it too nearly as the whole of moral wrongness.

## A.3 Proposition: aggregate improvement does not entail floor protection

**Proposition A.2.** A policy can have a higher aggregate outcome while violating a protected floor that a lower-aggregate policy satisfies.

**Proof by construction.** Let outcomes for three affected groups be

\[
a=(0.90,0.90,0.20),
\qquad
b=(0.65,0.65,0.65).
\]

Then

\[
\bar a=\frac{2.00}{3}=0.666\overline6
>
0.65=\bar b.
\]

Yet for protected floor \(k=0.40\),

\[
\min_i a_i=0.20<k,
\qquad
\min_i b_i=0.65\ge k.
\]

Therefore a higher mean does not entail protection of every affected group. \(\square\)

The result is elementary. Its ethical importance lies in how often institutional benefit measures hide concentrated burdens by construction.

## A.4 Proposition: consent does not entail permissibility

**Proposition A.3.** Recorded assent does not by itself establish valid consent, and valid consent does not by itself establish the permissibility of every transaction or institution.

**Reason.** Assent may occur under deception, dependence, lack of alternatives, impaired understanding, coercive threat, or a choice architecture controlled by the beneficiary. Even when consent is informed and voluntary, third-party harms, structural domination, nonwaivable rights, or severe public externalities may remain.

Formally, let \(C_n(u)\) represent valid consent of the direct participant and let \(K_{-a}(u)\) represent protected conditions of other affected parties. Then

\[
C_n(u)=1
\not\Rightarrow
K_{-a}(u)=1
\]

and therefore

\[
C_n(u)=1
\not\Rightarrow
u\in U_K.
\]

Consent remains morally powerful. The proposition denies only its logical sufficiency.

## A.5 Proposition: Pareto incomparability permits scalarization reversal

**Proposition A.4.** If two admissible options are non-dominating, nonnegative scalarizations can rank them in opposite orders.

**Proof.** Let \(u\) and \(v\) be such that \(z_i(u)>z_i(v)\) for some dimension \(i\), while \(z_j(v)>z_j(u)\) for another dimension \(j\). Choosing all weight on \(i\) yields \(V_w(u)>V_w(v)\). Choosing all weight on \(j\) yields \(V_{w'}(v)>V_{w'}(u)\). Mixtures preserve an interval of each ranking unless all advantages are exactly offset. \(\square\)

A ranking reversal therefore reveals a normative tradeoff. It is not evidence that one calculation is corrupt merely because another weighting produces a different result.

## A.6 Proposition: protected floors and Pareto dominance perform different functions

**Proposition A.5.** An option can lie on the Pareto frontier and still be ethically inadmissible under declared protected floors.

**Construction.** Give one policy the highest aggregate benefit but very low minimum welfare, consent, and correctability. No other policy dominates it because no other policy matches its aggregate benefit. It remains Pareto-efficient while violating protected conditions.

**Conclusion.** Pareto efficiency excludes only one form of avoidable sacrifice. It does not protect rights, standing, or minimum conditions by itself. \(\square\)

## A.7 Proposition: responsibility dimensions are non-equivalent

Let an actor-relative responsibility profile be

\[
\mathbf R_a(o)
=
\langle
C_a,K_a,F_a,U_a,D_a,B_a,X_a,P_a,M_a
\rangle,
\]

where the coordinates represent causal contribution, knowledge, foreseeability, control, role authority, benefit, coercion or duress, prevention capacity, and repair capacity.

**Proposition A.6.** No single coordinate generally determines blame, answerability, liability, punishment, or remedial duty.

**Construction.** A frontline operator may make the final causal contribution while possessing little authority, receiving little benefit, acting under threat of dismissal, and lacking power to redesign or repair the system. A governing board may make no final operational move while setting the policy, accepting the benefit, controlling resources, receiving warnings, and retaining the power to stop and remedy the harm.

Thus

\[
C_{\mathrm{frontline}}>C_{\mathrm{board}}
\]

can coexist with

\[
U_{\mathrm{frontline}}<U_{\mathrm{board}},
\quad
D_{\mathrm{frontline}}<D_{\mathrm{board}},
\quad
B_{\mathrm{frontline}}<B_{\mathrm{board}},
\quad
M_{\mathrm{frontline}}<M_{\mathrm{board}}.
\]

Direct causation, governance responsibility, blame, and remedial obligation therefore can rank actors differently. \(\square\)

## A.8 Proposition: responsibility can persist without fault

**Proposition A.7.** An actor can bear prospective or remedial responsibility without being culpable for creating the harm.

**Reason.** Let actor \(a\) lack causal contribution and fault but possess unique present capacity \(M_a\) to prevent continuation or provide remedy. If the cost of assistance is proportionate and no stronger countervailing duty applies, current capacity can generate a forward-looking responsibility. This is especially relevant to inherited institutions, beneficiaries of unjust arrangements, emergency rescue, and public office.

The proposition does not erase fault distinctions. It prevents moral practice from becoming unable to respond whenever the original wrongdoer is absent.

## A.9 Proposition: duress can mitigate blame without erasing harm

**Proposition A.8.** Reduced control under coercion can mitigate culpability while leaving causal contribution, victim standing, protection duties, and institutional responsibility intact.

This blocks two opposing errors:

1. treating coerced agents as if they acted with full freedom; and
2. treating coercion as if it made the resulting harm unreal or left no responsibility anywhere.

## A.10 Proposition: no repair coordinate is generally sufficient

Let repair be represented by

\[
\mathbf P_R
=
\langle
Pr,Tr,Ac,Rs,Cp,Rh,Nr,Pt
\rangle,
\]

where the coordinates denote protection, truth and acknowledgment, accountability, restitution or reparation, rehabilitation or support, restored standing, non-recurrence, and affected-party participation.

**Proposition A.9.** High performance on one repair coordinate does not entail adequate repair.

**Construction.** An apology can be truthful but leave harm ongoing. Punishment can be severe but provide no restitution. Compensation can be substantial while the institution denies wrongdoing and repeats it. Reform can reduce recurrence while abandoning those already harmed. Participation can be offered without remedial authority.

Therefore no one coordinate entails all others, and a total repair score can conceal a missing indispensable component. \(\square\)

## A.11 Proposition: an empty or unknown admissible set is not moral permission

**Proposition A.10.** Failure to identify an admissible option does not entail that every option is permissible, and failure to identify a violated floor does not entail that no floor is violated.

Let \(\widehat U_K\) be the option set identified under an incomplete model. Then

\[
\widehat U_K=\varnothing
\]

can mean genuine tragedy, inadequate option generation, an overly rigid floor specification, or model failure. Likewise,

\[
\widehat U_K\ne\varnothing
\]

can reflect omitted affected parties or harms. The appropriate verdict may be underdetermination, further inquiry, emergency minimization, or institutional redesign—not automatic permission.

## A.12 Proposition: role reversal is diagnostic but not decisive

**Proposition A.11.** A policy's failure under role reversal is evidence of asymmetry, but survival under role reversal does not prove justice.

A rule may be accepted by all hypothetical role occupants while the role structure itself excludes nonparticipants, animals, future persons, persons with disabilities, or parties deprived of meaningful representation. Hypothetical consent also depends on the information and choice set supplied to the chooser.

Role reversal is therefore one symmetry test within a larger affected-being and power analysis.

## A.13 Proposition: patiency does not entail sovereignty

**Proposition A.12.** Evidence that a being has morally relevant welfare does not establish that it possesses moral agency, responsibility, political authority, or legitimate control over others.

Formally, with predicates \(P(x)\) for patiency, \(A(x)\) for agency, \(R(x)\) for responsibility, and \(S(x)\) for sovereignty,

\[
P(x)\not\Rightarrow A(x),
\qquad
P(x)\not\Rightarrow R(x),
\qquad
P(x)\not\Rightarrow S(x).
\]

The converse implications also fail in some institutional cases: a corporation or automated system can exercise authority or causal power without possessing phenomenal welfare.

## A.14 Proposition: nominal appeal does not entail practical correctability

**Proposition A.13.** The existence of a complaint, appeal, review, or ombuds channel does not entail practical correctability.

Let practical correctability require at least a context-sensitive profile of:

\[
\langle
\text{access},
\text{independence},
\text{remedial authority},
\text{recurrence measurement},
\text{affected-party evidence},
\text{external or joint validation}
\rangle.
\]

A channel can exist while scoring near zero on the remaining dimensions. Therefore the binary observation “channel exists” is insufficient evidence for correction capacity. \(\square\)

## A.15 Proposition: effective emergency action does not entail legitimate emergency power

**Proposition A.14.** A measure can reduce a threat more effectively while remaining less legitimate because it is unnecessary, disproportionate, discriminatory, indefinite, unreviewable, or irreparable.

Let \(e(u)\) denote threat reduction and let \(g(u)\) denote a governance profile. Then

\[
e(u)>e(v)
\not\Rightarrow
u\text{ is more legitimate than }v.
\]

An exception that contains no expiry condition is not merely a long emergency response. It changes the standing institutional order and requires independent justification.

## A.16 Proposition: floor compliance does not establish option-set adequacy

**Proposition A.15.** A procedure that screens and ranks a presented set cannot establish that the presented set contains an adequate option without an independent option-generation premise.

Let

\[
U^{\mathrm{pres}}\subsetneq U^{\mathrm{feas}}.
\]

Suppose exactly one option \(u\in U^{\mathrm{pres}}\) satisfies all declared floors. Then the decision rule may correctly identify \(u\) as uniquely screening-admissible relative to \(U^{\mathrm{pres}}\). Nothing follows about an omitted \(v\in U^{\mathrm{feas}}\setminus U^{\mathrm{pres}}\), because \(v\)'s profile was never supplied to the rule.

Therefore

\[
\text{unique screening admissibility in }U^{\mathrm{pres}}
\not\Rightarrow
\text{adequacy of }U^{\mathrm{pres}}
\]

and does not by itself entail all-things-considered permissibility. \(\square\)

## A.17 Proposition: severe-risk irreversibility requires an explicit floor or exception

**Proposition A.16.** In a model that treats credible severe or irreversible harm as morally protected, omitting reversibility or equivalent retained option value from both the floor set and the exception rule leaves a structural gap.

**Construction.** Let an option equal every declared protected floor, possess high aggregate benefit, and have reversibility zero. If reversibility is neither screened nor represented in an exception condition, the option passes by construction. The procedure has not shown that irreversibility is permissible; it has failed to evaluate the dimension.

Accordingly, a severe-risk application must either include a declared floor for reversibility, containment, rollback, staged exposure, or equivalent retained option value, or state a necessity-and-proportionality exception that includes the harms of delay and the absence of safer alternatives. The proposition does not make reversibility universally overriding. \(\square\)

## A.18 Scope of the formal appendix

These propositions establish non-entailments and declaration requirements. They do not:

- generate substantive rights from mathematics;
- settle abortion, punishment, war, animal ethics, migration, or artificial patiency;
- determine thresholds without public and domain-specific argument;
- convert ethical disagreement into a technical optimization problem;
- or establish that every morally relevant consideration can be represented numerically.

Their role is constitutional: they mark transitions the framework may not make silently.

# Appendix B. Deterministic Ethical-Decision Contrast Models

## B.1 Purpose and status

This appendix supplies deterministic constructions used to check the paper's central distinctions. Every value is stipulated. The models are not fitted to data, do not validate a political or clinical intervention, and do not constitute a moral decision procedure. They are not empirical estimates, psychometric instruments, legal standards, policy recommendations, or a moral algorithm.

They test five claims:

1. high aggregate benefit and Pareto efficiency do not override protected floors;
2. justificatory integrity is necessary but not sufficient;
3. admissible options can remain non-dominating and reverse under disclosed weights;
4. direct causal contribution can diverge from governance and remedial responsibility;
5. apology, punishment, compensation, reform, and participation are not interchangeable forms of repair;
6. credible severe-harm cases require explicit treatment of reversibility;
7. floor screening cannot certify the adequacy of the presented option set.

The executable specification is `CU_Ethics_G1_1_reproducibility.py`. Its generated record is `CU_Ethics_G1_1_verification_results.json`.

## B.2 Four policy profiles

All policy dimensions are positively oriented and normalized to \([0,1]\). Higher values represent better performance on the declared dimension.

| Policy | Benefit | Min. welfare | Agency | Consent | Integrity | Legitimacy | Correctability | Reversibility | Freedom from coercion | Distributional fairness |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Opaque optimization | 0.93 | 0.18 | 0.30 | 0.25 | 0.35 | 0.30 | 0.20 | 0.35 | 0.30 | 0.15 |
| Transparent domination | 0.82 | 0.32 | 0.25 | 0.20 | 0.92 | 0.28 | 0.25 | 0.30 | 0.20 | 0.22 |
| Contestable support | 0.74 | 0.68 | 0.82 | 0.78 | 0.86 | 0.84 | 0.90 | 0.78 | 0.82 | 0.75 |
| Minimal intervention | 0.56 | 0.55 | 0.93 | 0.90 | 0.82 | 0.72 | 0.78 | 0.92 | 0.95 | 0.82 |

The profiles are designed to isolate different mistakes. Opaque optimization has the largest stipulated aggregate benefit but conceals concentrated harm and weak correction. Transparent domination is unusually candid but remains coercive, nonconsensual, and difficult to contest. Contestable support and minimal intervention satisfy all declared floors while trading protective delivery against liberty and reversibility.

## B.3 Protected floors

The construction declares the following floors:

| Dimension | Floor |
|---|---:|
| Minimum welfare | 0.45 |
| Agency protection | 0.55 |
| Consent quality | 0.50 |
| Evidential integrity | 0.60 |
| Public legitimacy | 0.50 |
| Practical correctability | 0.50 |
| Reversibility or equivalent retained option value | 0.40 |
| Freedom from coercion | 0.35 |
| Distributional fairness | 0.35 |

Because this construction stipulates a high-impact institutional intervention under credible risk of severe harm, it treats a minimum degree of reversibility, containment, rollback, or equivalent retained option value as a ninth protected condition. The numerical threshold \(0.40\) is stipulated for this contrast only; it is not a universal CU threshold. A different case may treat reversibility as a comparative consideration or proceed under an explicit necessity exception.

Only contestable support and minimal intervention pass every floor.

Opaque optimization fails all nine protected dimensions. Transparent domination passes evidential integrity but fails minimum welfare, agency, consent, legitimacy, correctability, reversibility, freedom from coercion, and distributional fairness.

The latter result is the numerical form of Proposition A.1:

\[
J_i=0.92
\quad\text{and yet}\quad
u\notin U_K.
\]

Truthful description does not legitimate domination.

## B.4 Pareto analysis

All four policies lie on the Pareto frontier of the complete ten-dimensional profile because each has at least one advantage that no other policy matches. The two inadmissible policies remain Pareto-efficient because one has the highest aggregate benefit and the other the highest stipulated evidential integrity.

This is not a defect in Pareto analysis. It demonstrates its scope:

\[
\text{Pareto efficiency}
\not\Rightarrow
\text{ethical admissibility}.
\]

Within the admissible set, contestable support and minimal intervention are non-dominating:

- contestable support is higher on aggregate benefit, minimum welfare, evidential integrity, public legitimacy, and practical correctability;
- minimal intervention is higher on agency, consent, reversibility, freedom from coercion, and distributional fairness.

## B.5 Three declared scalarizations

After floor screening, three disclosed weight sets produce the following scores:

| Scalarization | Contestable support | Minimal intervention | First-ranked admissible policy |
|---|---:|---:|---|
| Protective delivery | 0.7661 | 0.6828 | Contestable support |
| Liberty and reversibility | 0.7990 | 0.8414 | Minimal intervention |
| Institutional repair | 0.8148 | 0.7759 | Contestable support |

The result is not that all weightings are equally defensible. It is that the mathematical ranking imports normative priorities that must be argued for publicly.

The script also exhaustively enumerates all nonnegative ten-dimensional weight vectors on the \(0.1\) lattice that sum to one. Among 92,378 vectors:

- contestable support is the unique winner under 46,783;
- minimal intervention is the unique winner under 44,901;
- 694 produce a tie.

A lattice case is counted as a tie when every reported winner lies within \(10^{-12}\) of the largest floating-point score. This tolerance implements equality on a rational \(0.1\) weight grid despite binary floating-point representation; it is not a substantive moral indifference threshold.

This is a property of the stipulated profiles, not a probability distribution over moral truth. It demonstrates that the options occupy genuinely different regions of the declared value space.

### B.5.1 Adversarial reversibility and option-set checks

The audit introduced two additional stipulated profiles.

**Irreversible compliance** assigns aggregate benefit \(0.95\), reversibility \(0.00\), and places every other coordinate exactly at the original eight G.1 floors. Under the legacy eight-floor screen, it passes, is not Pareto-dominated by either baseline admissible policy, and becomes the unique winner under 322 of the 92,378 weight vectors when compared with contestable support and minimal intervention. Under the repaired nine-floor screen, it fails because

\[
0.00<0.40.
\]

This does not show that every irreversible act is impermissible. It shows that a model cannot claim to have considered severe-risk irreversibility when it omits the dimension from both its screen and its exception rule.

**Floor-hugging option** assigns aggregate benefit and reversibility \(1.00\) and places every other protected coordinate exactly at its floor. The audit called this profile “floor-hugging extraction”; G.1.1 uses a neutral label because extraction is not one of the declared coordinates and cannot be inferred merely from proximity to the floors. The profile passes the repaired screen. In the truncated presented set

\[
\{\text{opaque optimization},
  \text{transparent domination},
  \text{floor-hugging option}\},
\]

the floor-hugging option is the only screening-admissible member and is therefore selected under all 92,378 lattice weights. The procedure is internally correct and ethically incomplete: it has evaluated only the options it was given.

The result establishes the option-set boundary:

\[
\text{floor compliance}
\not\Rightarrow
\text{option-set adequacy}
\not\Rightarrow
\text{all-things-considered permissibility}.
\]

## B.6 Distributed responsibility

The construction assigns nine responsibility dimensions to four institutional roles.

| Actor | Causal contribution | Knowledge | Foreseeability | Control | Role authority | Benefit | Duress | Prevention capacity | Repair capacity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Governing board | 0.55 | 0.75 | 0.85 | 0.90 | 0.95 | 0.90 | 0.05 | 0.95 | 0.95 |
| Executive | 0.85 | 0.90 | 0.90 | 0.85 | 0.90 | 0.70 | 0.10 | 0.90 | 0.85 |
| Analyst | 0.50 | 0.75 | 0.70 | 0.30 | 0.55 | 0.25 | 0.45 | 0.35 | 0.30 |
| Frontline operator | 0.90 | 0.55 | 0.50 | 0.15 | 0.50 | 0.10 | 0.80 | 0.15 | 0.20 |

Ranking solely by direct causal contribution gives:

\[
\text{frontline}
>
\text{executive}
>
\text{board}
>
\text{analyst}.
\]

An explicitly illustrative governance-priority index emphasizing knowledge, authority, control, prevention, benefit, and repair, while reducing priority under duress, gives:

\[
\text{board }(0.8478)
>
\text{executive }(0.8199)
>
\text{analyst }(0.3542)
>
\text{frontline }(0.2133).
\]

The index is not a blame or liability score. Its only purpose is to show that a system can concentrate visible causal action at the bottom while concentrating governable responsibility at the top.

## B.7 Repair profiles

Five response plans are evaluated across eight positively oriented repair dimensions.

| Plan | Protection | Truth | Accountability | Restitution | Support | Standing | Non-recurrence | Participation |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Apology only | 0.55 | 0.85 | 0.35 | 0.10 | 0.25 | 0.45 | 0.20 | 0.20 |
| Punishment only | 0.70 | 0.55 | 0.90 | 0.10 | 0.20 | 0.40 | 0.45 | 0.15 |
| Restitution only | 0.60 | 0.50 | 0.30 | 0.90 | 0.75 | 0.55 | 0.35 | 0.35 |
| Institutional reform only | 0.80 | 0.70 | 0.60 | 0.35 | 0.45 | 0.72 | 0.90 | 0.65 |
| Integrated repair | 0.88 | 0.86 | 0.78 | 0.80 | 0.78 | 0.84 | 0.90 | 0.82 |

With a component floor of \(0.50\), only the integrated plan passes all eight dimensions. The result is stipulated: integrated repair was designed to be complete. The analytical point is that a response can excel at one familiar symbol of justice and remain incomplete elsewhere.

The construction should not be read as requiring all eight components at the same level in every case. Some harms cannot be repaired through reconciliation; some wrongdoers cannot safely participate; some losses cannot be restored; and some cases require punishment while others do not. The model tests non-substitutability, not one universal sequence.

## B.8 Nominal and practical correctability

Two institutional profiles are compared:

| Case | Access | Independence | Remedy authority | Recurrence measurement | Affected-party evidence | External or joint validation |
|---|---:|---:|---:|---:|---:|---:|
| Nominal complaint channel | 0.65 | 0.15 | 0.10 | 0.15 | 0.25 | 0.05 |
| Practical correctability | 0.80 | 0.75 | 0.70 | 0.72 | 0.85 | 0.70 |

At component floors of \(0.50\), the nominal channel fails every dimension except formal access. The second profile passes all six.

The construction formalizes a governance warning inherited from Social Dynamics F.1.1: an institution cannot establish its correctability merely by pointing to a process it designed, controls, measures, and lacks power to remedy.

## B.9 Emergency governance

The emergency contrast uses ten dimensions:

- threat reduction;
- necessity;
- proportionality;
- narrow scope;
- expiry or renewal burden;
- independent review;
- nondiscrimination;
- record preservation;
- remedy;
- restoration of ordinary standing.

The indefinite emergency order has slightly higher stipulated threat reduction than the bounded measure:

\[
0.90>0.86.
\]

Yet it fails nine of the ten declared component floors. The bounded measure passes all ten.

The construction shows why “it works” is not a complete defense of emergency power. Effectiveness is one condition among others. An indefinite, unreviewable, discriminatory, or irreparable order can be effective and illegitimate at the same time.

## B.10 Aggregate masking check

The executable record reproduces Proposition A.2:

\[
a=(0.90,0.90,0.20),
\qquad
b=(0.65,0.65,0.65),
\qquad
k=0.40.
\]

Option \(a\) has the higher mean, violates the floor, and would be chosen by a rule that maximized only the aggregate. Option \(b\) has the lower mean and protects every group.

## B.11 What the models establish

The deterministic constructions establish that the following implications fail:

\[
\begin{aligned}
\text{high benefit}&\not\Rightarrow\text{admissibility},\\
\text{truthfulness}&\not\Rightarrow\text{justice},\\
\text{Pareto efficiency}&\not\Rightarrow\text{floor protection},\\
\text{direct causation}&\not\Rightarrow\text{greatest governance responsibility},\\
\text{apology}&\not\Rightarrow\text{repair},\\
\text{punishment}&\not\Rightarrow\text{repair},\\
\text{compensation}&\not\Rightarrow\text{repair},\\
\text{formal appeal}&\not\Rightarrow\text{correctability},\\
\text{effectiveness}&\not\Rightarrow\text{legitimate emergency power},\\
\text{floor compliance in }U^{\mathrm{pres}}&\not\Rightarrow\text{option-set adequacy},\\
\text{unique admissibility in }U^{\mathrm{pres}}&\not\Rightarrow\text{all-things-considered permissibility}.
\end{aligned}
\]

They do not establish the correct moral thresholds, the relative authority of ethical traditions, the empirical effectiveness of any intervention, or that the presented option set contains a good alternative. The screening and scalarization results are conditional on the stipulated profiles and the institution that supplied them.

# Appendix C. Claim and Evidence Ledger

The ledger records the status of claims made or explicitly rejected in G.1.1. It is not an evidence-certainty scale. Empirical grades indicate the kind of support represented in the selective literature review; normative entries require philosophical and public justification rather than empirical confirmation alone.

<!-- CLAIM_LEDGER_TABLE_START -->
| ID | Claim | Status | Evidence | Scope or condition |
|---|---|---|---|---|
| ETH-C1 | Ethics is a normative practice of evaluating action, institutions, character, standing, responsibility, and repair; it is not reducible to measuring system organization. | Domain definition | E0 | Requires independent normative premises and public justification. |
| ETH-C2 | One universal scalar coherence value determines moral rightness across cases. | Retired | — | No cross-domain moral units, universal weighting, or legitimate aggregation rule has been established. |
| ETH-C3 | The ethical model tuple declares affected parties, options, causal models, protected conditions, power, distributions, reasons, history, boundaries, horizons, observation, and correction. | Methodological proposal | E0 | A declaration discipline, not a complete formalization of moral life. |
| ETH-C4 | Affected-being sets must not be limited automatically to formal decision makers, consenting participants, citizens, present persons, verbal reasoners, or easily measured interests. | Normative and methodological principle | E0 | Inclusion establishes standing for consideration, not identical weight or rights. |
| ETH-C5 | Ethical evaluation is better represented by a multidimensional profile than by an undeclared total score. | Methodological proposal | E0–E1 | Profiles remain contestable and may omit morally relevant dimensions. |
| ETH-C6 | Protected floors and prohibitions can screen options before secondary comparison. | Formal shell / normative proposal | E0–E1 | Requires affected-being scope, declared protected floors, uncertainty model, horizon, and an independently reviewed presented option set. |
| ETH-C7 | Ethical scalarization is permissible only as a declared, purpose-specific secondary rule rather than a universal value function. | Methodological constraint | E0–E1 | Weights, normalization, distributions, exclusions, and authority must be disclosed. |
| ETH-C8 | Some severe, concentrated, nonconsensual, or standing-destroying losses are not made permissible merely by unrelated aggregate benefits. | Normative principle | E0 | The scope of noncompensation and legitimate exceptions requires case-specific argument. |
| ETH-C9 | Emergency exceptions require threat evidence, necessity, proportionality, narrow scope, expiry, review, nondiscrimination, records, remedy, and restoration of ordinary standing. | Normative governance principle | E0 | Not a legal test for every jurisdiction; emergency definitions can themselves be contested. |
| ETH-C10 | Physical, biological, psychological, and social facts do not by themselves entail moral obligations. | Analytic constraint | E0 | Normative conclusions require at least one normative bridge premise. |
| ETH-C11 | Moral justification presupposes some standing of participants as reason-givers, reason-receivers, and subjects of correction, but this bounded transcendental constraint does not supply a complete ethics. | Bridge argument | E0 | Does not establish one theory of rights, welfare, punishment, or distribution. |
| ETH-C12 | Descriptive ethical claims and orienting commitments occupy distinct but asymmetrically permeable registers: facts constrain commitments, while commitments do not establish facts. | Canonical bridge from M&E B.2 | E0 | Moral claims can contain both descriptive and normative components and must be disaggregated. |
| ETH-C13 | CU Ethics can be normatively plural without treating every sincere value system as equally warranted. | Metaethical position | E0 | Pluralism remains constrained by facts, standing, protected conditions, and public answerability. |
| ETH-C14 | Justificatory integrity requires truth-sensitive, symmetric, affected-party-inclusive, uncertainty-aware, and correction-capable handling of reasons and evidence. | Definition | E0 | Operational indicators remain fallible and context-sensitive. |
| ETH-C15 | A defense that requires systematic distortion of relevant facts, reasons, affected parties, alternatives, or standards is morally inadequate. | Normative principle | E0 | Failure of integrity defeats a defense; it does not alone assign all responsibility or remedy. |
| ETH-C16 | Absence of deception, hypocrisy, or motivated distortion does not establish permissibility. | Analytic result / counterexample | E1 | Transparent domination, candid cruelty, and sincere fanaticism remain possible. |
| ETH-C17 | A public justificatory record should preserve reasons, evidence, uncertainty, alternatives, dissent, authorship, revisions, and consequences when stakes warrant it. | Governance proposal | E0–E3 | Documentation can itself become burdensome, inaccessible, or performative and requires proportional design. |
| ETH-C18 | Role reversal and symmetry tests reveal some arbitrary asymmetries but do not prove justice or complete affected-being inclusion. | Methodological constraint | E0–E1 | Hypothetical choosers inherit the information and option set supplied by the model. |
| ETH-C19 | False belief, disagreement, inconsistency, distress, trauma adaptation, neurodivergence, or identity do not by themselves establish self-deception. | Diagnostic safeguard | E0–E3 | Stronger attribution requires evidence of motivated asymmetric processing. |
| ETH-C20 | Institutions can distort reasons through incentives, records, classifications, role fragmentation, retaliation, and agenda control without possessing one unified deceptive mind. | Bridge hypothesis / empirical synthesis | E0–E3 | Collective-psychology metaphors should not replace causal institutional analysis. |
| ETH-C21 | Moral standing can attach to beings or groups that lack institutional voice, ordinary agency, citizenship, or capacity to offer reasons in conventional form. | Normative principle | E0 | The content and strength of claims depend on welfare, vulnerability, relation, and context. |
| ETH-C22 | Moral patiency, moral agency, responsibility, and sovereignty are distinct dimensions. | Analytic distinction | E0–E1 | No single capacity should be used as a proxy for all four. |
| ETH-C23 | Agency is graded and domain-relative rather than a binary possession. | Bridge principle / empirical generalization | E0–E4 | Grades require task-, support-, and context-sensitive assessment. |
| ETH-C24 | Valid consent requires more than recorded assent; understanding, voluntariness, alternatives, capacity, and freedom from undue influence matter. | Normative and empirical synthesis | E0–E4 | Thresholds and legal doctrines vary by domain and jurisdiction. |
| ETH-C25 | Supported decision making can preserve or extend agency without replacing the person's standing with that of the supporter. | Normative governance principle | E0–E3 | Support can become coercive or tokenistic and must be evaluated in practice. |
| ETH-C26 | Rights can function as protected conditions of bodily and psychological integrity, welfare, liberty, capability, participation, and standing. | Normative proposal | E0 | Their content is not derived from coherence and requires legal, historical, democratic, and moral argument. |
| ETH-C27 | Formal permission is insufficient when a person lacks substantive capability to exercise the protected option. | Normative and empirical synthesis | E0–E4 | Capability evaluation must avoid paternalistic substitution and one universal list. |
| ETH-C28 | Nonhuman animals can possess morally relevant welfare and standing without verbal rationality or political agency. | Normative bridge supported by empirical literature | E2–E4 | Species, capacities, uncertainty, and conflicts among interests require further analysis. |
| ETH-C29 | Diminished or fluctuating agency can reduce some forms of responsibility while increasing protection and support duties. | Normative principle | E0–E4 | Must not erase residual agency or authorize unrestricted paternalism. |
| ETH-C30 | Disagreement about the status of developing human life cannot be settled by the word coherence alone. | Scope constraint | E0 | Requires biological, metaphysical, legal, relational, and normative argument beyond this reconstruction. |
| ETH-C31 | Credible uncertainty about artificial patiency can justify investigation and precaution without establishing consciousness, valence, personhood, or rights. | Precautionary hypothesis | E0–E2 | Evidence remains system-specific and highly uncertain. |
| ETH-C32 | Moral patiency does not entail responsibility, sovereignty, or legitimate control over others. | Analytic and normative principle | E0–E1 | Applies to humans, animals, and possible artificial patients. |
| ETH-C33 | Consequences remain morally relevant even when an action satisfies a rule or is sincerely intended. | Normative principle | E0 | Does not imply that aggregate consequences are the sole source of moral reasons. |
| ETH-C34 | Expected aggregate value is insufficient where probability is poorly characterized, tail harms are severe, or burdens are concentrated. | Methodological and normative principle | E0–E3 | Alternative uncertainty methods require declared assumptions and can also fail. |
| ETH-C35 | Distributions of benefit, burden, risk, voice, and repair obligation are morally relevant independently of aggregates. | Normative principle / empirical governance synthesis | E0–E4 | No one distributional rule is established for all cases. |
| ETH-C36 | Benefits and burdens should be linked to identify who gains, who pays, who chose, who can refuse, and who can obtain remedy. | Methodological principle | E0 | A mapping requirement, not a complete theory of distributive justice. |
| ETH-C37 | Reversibility and retained option value are morally relevant under uncertainty. | Normative and decision-theoretic principle | E0–E3 | Irreversible action can still be justified when delay is more harmful. |
| ETH-C38 | Precaution should vary with severity, plausibility, alternatives, reversibility, and the harms of delay rather than functioning as automatic prohibition or permission. | Normative principle | E0 | Does not provide a universal numerical precaution threshold. |
| ETH-C39 | Some choices are tragic in that every feasible option leaves morally serious loss, but the category should not conceal avoidable option scarcity or institutional design failure. | Normative distinction | E0 | Requires active search for redistribution, support, and new options. |
| ETH-C40 | Imposed sacrifice requires necessity, proportionality, distributional analysis, legitimacy, and repair; aggregate benefit alone is insufficient. | Normative principle | E0 | Does not categorically prohibit every burden or risk. |
| ETH-C41 | Future persons and delayed path-dependent harms must enter long-horizon ethical analysis despite uncertainty and representation problems. | Normative and methodological principle | E0–E3 | Future interests cannot be measured with spurious precision. |
| ETH-C42 | Ethical underdetermination is a legitimate verdict when facts, options, affected parties, thresholds, or normative priorities remain unresolved. | Methodological principle | E0 | Underdetermination does not erase urgent protection duties. |
| ETH-C43 | Power shapes ethical problems by controlling agendas, options, evidence, classification, sanctions, resources, and exit. | Bridge principle / empirical generalization | E0–E4 | Power is multidimensional and should not be inferred from titles alone. |
| ETH-C44 | Compliance and formal choice can coexist with domination when refusal is practically unavailable or exposes a person to uncontrolled interference. | Normative and empirical synthesis | E0–E4 | Domination requires context-sensitive evidence of dependency and arbitrary power. |
| ETH-C45 | Coercive or high-impact decisions require public answerability to those subject to them. | Normative principle | E0 | Public justification does not require unanimity or literal participation by every person in every decision. |
| ETH-C46 | Institutional effectiveness, stability, legality, consent, and popularity do not individually establish legitimacy. | Analytic and normative distinction | E0–E1 | Legitimacy remains plural, degree-like, and contested. |
| ETH-C47 | Consent to a particular act does not by itself legitimate the surrounding political or institutional order. | Normative distinction | E0 | Third parties, background dependency, and unchosen rule structures remain relevant. |
| ETH-C48 | Democratic forms are valuable when they distribute agency, protect opposition and minorities, constrain power, preserve evidence, and enable peaceful correction. | Normative and empirical synthesis | E0–E4 | Majority rule or actual consensus alone is insufficient. |
| ETH-C49 | Dissent is a protected but fallible correction channel. | Normative and institutional principle | E0–E4 | Protection of standing does not make dissenting claims automatically true. |
| ETH-C50 | Emergency powers require narrower and more reviewable authority than ordinary claims of effectiveness imply. | Normative governance principle | E0 | Concrete legal standards remain jurisdiction-specific. |
| ETH-C51 | Paternalistic action requires evidence of impaired agency or severe preventable harm, attention to less restrictive alternatives, and restoration of agency where possible. | Normative principle | E0 | Does not settle all conflicts between welfare and autonomy. |
| ETH-C52 | Responsibility is a profile involving causation, knowledge, foreseeability, control, role, benefit, duress, prevention capacity, and repair capacity. | Methodological and normative proposal | E0–E3 | No universal scalar blame function is claimed. |
| ETH-C53 | Responsibility without adequate authority is an institutional failure that can expose agents to blame and moral injury for outcomes they cannot control. | Normative and empirical hypothesis | E0–E3 | Role-specific evidence is required. |
| ETH-C54 | Authority without accountability permits actors to shape outcomes while evading answerability and repair obligations. | Normative and empirical hypothesis | E0–E4 | Formal accountability may differ from practical accountability. |
| ETH-C55 | Distributed causation does not entail that responsibility disappears; different actors can bear different kinds of responsibility for one outcome. | Normative principle / many-hands response | E0–E3 | Attribution must avoid both scapegoating and indiscriminate collective blame. |
| ETH-C56 | Deliberate ignorance and culpable failure to inquire can ground responsibility where warning signs, role duties, and feasible access to information exist. | Normative principle | E0–E3 | Actual information environments and role capacities must be established. |
| ETH-C57 | Coercion and duress can mitigate culpability without erasing harm, victim standing, or responsibility elsewhere in the system. | Normative principle | E0–E4 | Mitigation is degree-like and context-sensitive. |
| ETH-C58 | Ongoing benefit, present capacity, public role, or control over remedy can generate forward-looking responsibility without proving fault for the original harm. | Normative principle | E0 | Cost, fairness, competing duties, and institutional allocation remain relevant. |
| ETH-C59 | Self-deception becomes morally significant when motivated asymmetry conceals harm, excludes affected beings, corrupts standards, blocks correction, diffuses responsibility, or protects power. | Normative bridge from Psychology E.1.1 | E0–E3 | Attribution requires process evidence and symmetric standards. |
| ETH-C60 | Rationalization supplies reasons after a commitment is protected and should be distinguished from ordinary post hoc explanation or incomplete introspection. | Psychological and normative hypothesis | E0–E3 | Generated reasons are not transparent records of causal cognition. |
| ETH-C61 | Moral disengagement and moral credentialing can facilitate harmful conduct without exhausting the mechanisms of institutional wrongdoing. | Imported empirical generalization | E2–E4 | Constructs are context-dependent and not diagnoses of persons or groups. |
| ETH-C62 | The concept of self-deception can itself be weaponized to dismiss disagreement and therefore requires process evidence, symmetry, and appeal. | Governance safeguard | E0–E3 | No actor or institution should certify opponents as self-deceived solely because they reject its framework. |
| ETH-C63 | Moral distress, moral injury, institutional betrayal, trauma-related disorder, grief, guilt, shame, burnout, and ordinary ethical disagreement are overlapping but non-identical constructs. | Conceptual and empirical distinction | E0–E3 | Operational boundaries remain under development. |
| ETH-C64 | Moral injury is a developing construct concerning enduring psychological, relational, existential, social, or spiritual suffering associated with morally significant events or betrayal. | Imported empirical synthesis / bridge | E2–E3 | No universally accepted diagnosis, mechanism, or gold-standard treatment is assumed. |
| ETH-C65 | Institutions can produce or intensify moral injury through compromised roles, responsibility–authority gaps, concealment, retaliation, unsafe conditions, and abandonment. | Empirical and normative hypothesis | E2–E3 | Causal pathways and population differences require further study. |
| ETH-C66 | Resilience interventions can become moral offloading when institutions ask individuals to adapt to preventable structural injury while leaving causal conditions unchanged. | Normative and empirical hypothesis | E0–E3 | Individual support remains valuable and need not imply blame. |
| ETH-C67 | Institutional betrayal can reduce trust, disclosure, engagement, and willingness to rely on institutions. | Imported empirical generalization | E2–E3 | Findings are population- and instrument-specific and should not be generalized without evidence. |
| ETH-C68 | Repair is a multidimensional practice including protection, truth, accountability, restitution or reparation, support, restored standing, non-recurrence, and affected-party participation. | Normative and methodological proposal | E0–E3 | Not every case permits or requires every component in the same form. |
| ETH-C69 | Punishment is neither identical with repair nor categorically excluded; it requires independent justification. | Normative principle | E0 | Relevant purposes include protection, desert, deterrence, rehabilitation, denunciation, and alternatives. |
| ETH-C70 | Nominal complaint channels do not establish practical correctability without access, independence, remedial authority, recurrence evidence, and affected-party or external validation. | Governance principle | E0–E3 | Measures must be proportionate to stakes and institutional form. |
| ETH-C71 | Repair must not require forgiveness, reconciliation, trust, renewed contact, or return to a prior relationship. | Normative safeguard | E0–E3 | Victims and affected parties retain standing to refuse relational restoration. |
| ETH-C72 | Trust after harm should be evidence-sensitive and can remain low even after sincere reform; non-recurrence requires changes in incentives, authority, records, and practice. | Normative and empirical synthesis | E0–E4 | Trust is distinct from trustworthiness and should not be coerced. |
| ETH-C73 | Virtues such as attention, courage, humility, truthfulness, compassion, and practical wisdom can support ethical judgment but do not make the bearer infallible. | Normative and empirical synthesis | E0–E3 | Virtue language can conceal hierarchy, exclusion, or self-certification. |
| ETH-C74 | Compassion can function as an epistemic posture that widens attention to suffering and context, while remaining compatible with boundaries, accountability, and protection. | Normative commitment / hypothesis | E0–E3 | Compassion does not establish factual truth or require reconciliation. |
| ETH-C75 | Contemplative and spiritual traditions can orient nonattachment, ahimsa, non-forcing, humility, and service without supplying empirical proof or exemption from public accountability. | Interpretation / commitment | E0 | Traditions are internally diverse and historically entangled with power. |
| ETH-C76 | Contemplative language can be used for spiritual bypassing, passivity, purity, obedience, or suppression of justified anger and dissent. | Normative and empirical caution | E0–E3 | Does not negate contemplative practice; it creates governance requirements. |
| ETH-C77 | AI-mediated ethical decisions must be analyzed as sociotechnical systems including model, data, interface, operator, institution, incentives, and affected beings. | Methodological principle | E0–E4 | Model-level evaluation remains necessary but insufficient. |
| ETH-C78 | AI can assist ethical reasoning by surfacing alternatives, inconsistencies, affected parties, evidence gaps, and reversals, but cannot legitimate the values, floors, or authority it is given. | Engineering and governance hypothesis | E0–E3 | Benefits depend on interface, oversight, incentives, and users' capacity to challenge outputs. |
| ETH-C79 | Generated explanations are not transparent records of a model's causal reasoning and should not be treated as sufficient evidence of moral understanding or responsibility. | Imported empirical constraint / bridge | E2–E3 | Mechanistic and behavioral evidence can still inform assessment. |
| ETH-C80 | Possible artificial patiency would ground protection without automatically establishing responsibility, sovereignty, or authority over human institutions. | Normative principle under uncertainty | E0–E2 | Requires system-specific evidence and remains unresolved. |
| ETH-C81 | A non-egoic architecture can reduce self-preserving goal formation without guaranteeing compassion, truthfulness, justice, or legitimate normative content. | Bridge principle from Non-Egoic Mind | E0–E2 | Institutional ownership and objective-setting remain load-bearing. |
| ETH-C82 | The deterministic G.1 constructions show that high benefit, truthfulness, Pareto efficiency, direct causation, apology, punishment, compensation, nominal appeal, and emergency effectiveness each fail to entail the broader ethical property with which they are often conflated. | Constructed non-entailment result | E1 | Values are stipulated and establish logical possibility, not empirical frequency. |
| ETH-C83 | Promotion of provisional ethical principles requires philosophical, legal, empirical, misuse, and affected-community review proportionate to their governing consequences. | Methodological and normative principle | E0 | Promotion gates are conjunctive; unresolved required-review conflict preserves provisional or domain-local status and a public dissent record. |
| ETH-C84 | Protected-floor compliance establishes only screening admissibility relative to the presented option set; it does not establish option-set adequacy or all-things-considered permissibility. | Formal and methodological boundary | E1 | Requires separate scrutiny of who generated, excluded, and constrained the alternatives and whether affected parties could propose options. |
| ETH-C85 | Under credible risk of severe or irreversible harm, an ethical application must either declare a context-appropriate reversibility, containment, rollback, staged-exposure, or retained-option floor, or provide an explicit necessity-and-proportionality exception. | Provisional normative and methodological principle | E0–E1 | No universal numerical threshold is implied; the exception must address safer alternatives and harms of delay. |
| ETH-C86 | Canonical promotion requires closure of every assigned review gate; unresolved disagreement among required philosophical, empirical, legal, misuse, and affected-community reviews blocks promotion rather than being resolved by aggregate approval. | Methodological and governance principle | E0 | The author may publish dispositions and variants, but no constituency can unilaterally override another required gate. |
<!-- CLAIM_LEDGER_TABLE_END -->

# Appendix D. Provisional Ethics Principle Registry

The following entries are candidates for later synchronization with Foundations. Their appearance here does not alter the B.2 registry. Promotion requires closure of every review gate assigned to the entry. When required philosophical, empirical, legal, and affected-community review cannot be reconciled, the entry remains provisional or domain-local; dissent and the author's disposition must remain public. No constituency can force canonical promotion by overriding another required gate.

<!-- PRINCIPLE_REGISTRY_TABLE_START -->
| ID | Name | Candidate status | Text | Promotion review |
|---|---|---|---|---|
| CU-E-1 | The Justificatory Integrity Constraint | PROVISIONAL NORMATIVE PRINCIPLE | An action, policy, or institution lacks adequate moral justification when its defense requires systematic distortion of relevant facts, reasons, affected parties, alternatives, or standards in order to protect a dominant identity, advantage, authority, or prior commitment. Integrity is necessary but not sufficient for permissibility. | CONTEXT-PROPORTIONATE AFFECTED-COMMUNITY REVIEW |
| CU-E-2 | Agency, Patiency, and Degrees of Responsibility | PROVISIONAL NORMATIVE PRINCIPLE | Moral patiency, moral agency, responsibility, and sovereignty are distinct. Responsibility varies with understanding, reason-responsiveness, control, authorship, coercion, and capacity for repair; diminished agency can reduce blame while increasing duties of protection. | HEIGHTENED AFFECTED-COMMUNITY CO-GOVERNANCE |
| CU-E-3 | Recognition and Affected-Being Standing | PROVISIONAL NORMATIVE PRINCIPLE | Ethical evaluation must represent all materially affected beings according to relevant welfare, agency, vulnerability, relationship, history, and stake rather than treating absence of institutional voice as absence of a claim. | HEIGHTENED AFFECTED-COMMUNITY CO-GOVERNANCE |
| CU-E-4 | Diachronic and Beneficiary Responsibility | PROVISIONAL NORMATIVE PRINCIPLE | Moral evaluation includes delayed, cumulative, intergenerational, and path-dependent consequences, together with responsibilities created by prior action, inherited advantage, ongoing benefit, and present capacity to prevent or repair harm. | HEIGHTENED AFFECTED-COMMUNITY CO-GOVERNANCE |
| CU-E-5 | Self-Deception as Moral Failure | PROVISIONAL NORMATIVE BRIDGE PRINCIPLE | Motivated distortion becomes morally significant when it conceals avoidable harm, excludes affected beings, corrupts standards, blocks correction, diffuses responsibility, or protects power from accountability. Disagreement or error alone does not establish self-deception. | HEIGHTENED AFFECTED-COMMUNITY CO-GOVERNANCE |
| CU-E-6 | Protection, Accountability, and Repair | PROVISIONAL NORMATIVE PRINCIPLE | Responses to wrongdoing should prioritize cessation and protection, truthful acknowledgment, proportionate accountability, restitution or reparation, restoration of standing, and prevention of recurrence. Punishment requires separate justification and is neither intrinsically reparative nor categorically excluded. | HEIGHTENED AFFECTED-COMMUNITY CO-GOVERNANCE |
| CU-E-7 | Moral Injury | PROVISIONAL BRIDGE PRINCIPLE | Moral injury names enduring psychological, social, relational, existential, or spiritual suffering associated with perpetrating, witnessing, failing to prevent, suffering, or being betrayed by morally significant wrong. Its descriptive use remains governed by the developing empirical literature. | HEIGHTENED AFFECTED-COMMUNITY CO-GOVERNANCE |
| CU-E-8 | Structural Moral Injury and Institutional Betrayal | PROVISIONAL NORMATIVE AND EMPIRICAL HYPOTHESIS | Institutions can produce or intensify moral injury when they impose morally compromising roles, deny adequate authority or alternatives, conceal harm, betray dependence, punish disclosure, or individualize structurally generated distress. | HEIGHTENED AFFECTED-COMMUNITY CO-GOVERNANCE |
| CU-E-9 | Local–Global Compatibility and Noncompensation | PROVISIONAL NORMATIVE PRINCIPLE | Claims of collective benefit are inadequate when they depend on avoidable destruction of protected standing, agency, or welfare, or on hidden transfer of severe, nonconsensual, concentrated, or irreparable burdens. Sacrifice requires necessity, proportionality, distributional analysis, and repair. | HEIGHTENED AFFECTED-COMMUNITY CO-GOVERNANCE |
| CU-E-10 | Political Legitimacy and Public Justification | PROVISIONAL NORMATIVE PRINCIPLE | Coercive or high-impact power is legitimate only to the degree that it is publicly answerable to those subject to it, preserves protected standing, remains contestable, discloses evidence and uncertainty, and includes practical correction and remedy. | HEIGHTENED AFFECTED-COMMUNITY CO-GOVERNANCE |
| CU-E-11 | Rights as Protected Conditions of Agency and Patiency | PROVISIONAL NORMATIVE PRINCIPLE | Rights protect bodily and psychological integrity, welfare, liberty, capability, participation, and standing against domination and unrestricted aggregate tradeoff. Their content requires independent moral, legal, historical, and democratic argument. | HEIGHTENED AFFECTED-COMMUNITY CO-GOVERNANCE |
| CU-E-12 | Democracy as a Conditional Corrective Achievement | PROVISIONAL NORMATIVE AND EMPIRICAL SYNTHESIS | Democratic forms are valuable when they distribute political agency, preserve opposition and minority standing, constrain power, and enable peaceful correction. Majority rule or actual consensus alone is insufficient. | HEIGHTENED AFFECTED-COMMUNITY CO-GOVERNANCE |
| CU-E-13 | Constraint on Political Means | PROVISIONAL NORMATIVE PRINCIPLE | Political ends do not justify means that destroy the truth conditions, protected standing, accountability, or corrective institutions required to pursue, evaluate, and revise those ends. | HEIGHTENED AFFECTED-COMMUNITY CO-GOVERNANCE |
| CU-E-14 | Responsibility–Authority Alignment | PROVISIONAL NORMATIVE AND METHODOLOGICAL PRINCIPLE | Responsibility should be assigned with attention to causal contribution, knowledge, control, authority, benefit, coercion, prevention capacity, and repair capacity. Institutions should neither impose responsibility without adequate authority nor permit authority without accountability. | CONTEXT-PROPORTIONATE AFFECTED-COMMUNITY REVIEW |
| CU-E-15 | Affected-Community Participation | PROVISIONAL METHODOLOGICAL AND NORMATIVE PRINCIPLE | People governed, classified, burdened, or represented by an ethical principle must have substantive, accessible, and appropriately authoritative participation in its development, application, and review. Participation supplements rather than replaces evidence and argument. Promotion requires closure of every assigned review gate; unresolved conflict preserves provisional status and public dissent. | HEIGHTENED AFFECTED-COMMUNITY CO-GOVERNANCE |
| CU-E-16 | Moral Uncertainty, Precaution, and Reversibility | PROVISIONAL NORMATIVE PRINCIPLE | Under credible risk of severe or irreversible harm, uncertainty should alter action in proportion to severity, plausibility, alternatives, reversibility, and the harms of delay. The application must either declare a context-appropriate reversibility, containment, rollback, staged-exposure, or retained-option floor, or publicly justify a necessity-and-proportionality exception. Uncertainty neither automatically permits exposure nor requires paralysis. | CONTEXT-PROPORTIONATE AFFECTED-COMMUNITY REVIEW |
| CU-E-17 | Moral Patiency Is Not Sovereignty | PROVISIONAL NORMATIVE PRINCIPLE | Evidence that a being can experience welfare or suffering can ground protection without establishing responsibility, authority, or legitimate control over others. | CONTEXT-PROPORTIONATE AFFECTED-COMMUNITY REVIEW |
| CU-E-18 | Compassionate Moral Address | PROVISIONAL NORMATIVE COMMITMENT | Accountability should preserve the standing of persons wherever protection allows, distinguish judgment from humiliation, and seek understanding sufficient for prevention and repair without converting compassion into excuse. | CONTEXT-PROPORTIONATE AFFECTED-COMMUNITY REVIEW |
<!-- PRINCIPLE_REGISTRY_TABLE_END -->

# Appendix E. Selective Literature and Operationalization Ledger

This ledger maps representative sources to the narrower claims G.1.1 imports. It is selective rather than systematic.

| Topic | Representative sources | What G.1.1 imports | What G.1.1 does not infer |
|---|---|---|---|
| Moral responsibility | Strawson (1962); Fischer and Ravizza (1998); Young (2011); Thompson (1980) | Responsibility includes answerability, control, role, causal contribution, structural position, and forward-looking obligations | One accepted scalar formula for blame or legal liability |
| Public justification and legitimacy | Rawls (1993); Scanlon (1998); Forst (2012); Habermas (1990) | Coercive power owes reasons and correction to those subject to it | That actual consensus, majority vote, or one philosophical test is sufficient for legitimacy |
| Capability and disability | Sen (2009); Nussbaum (2006); UN CRPD General Comment No. 7 | Substantive opportunity, supported agency, and participation matter beyond formal permission | That one capability list settles all rights or that representation can replace participation |
| Care and relational ethics | Gilligan (1982); Held (2006); Tronto (1993) | Dependency, relationship, care labor, responsiveness, and unequal vulnerability are morally relevant | That care overrides justice, autonomy, evidence, or institutional constraint |
| Epistemic injustice | Fricker (2007); Medina (2013) | Credibility, interpretive resources, and resistant knowledge are distributed through power | That membership in a marginalized group makes every claim true or beyond challenge |
| Motivated reasoning and hypocrisy | Kunda (1990); Moore et al. (2012); Monin and Miller (2001); Ditto et al. (2025); Silver and Berman (2024) | People and institutions can apply reasons asymmetrically in identity- and interest-protective ways | That disagreement, inconsistency, or group identity proves self-deception |
| Moral distress and ethical climate | Jameton (1984); Xue et al. (2025) | Organizational ethical climate is associated with moral distress and deserves structural analysis | That every workplace distress response is moral injury or that correlation identifies one causal mechanism |
| Moral injury | Shay (1994); Litz et al. (2009); Griffin et al. (2019); VanderWeele et al. (2025) | Moral injury is a developing construct concerning enduring suffering around morally significant events and betrayal | One universally accepted diagnostic entity, mechanism, or intervention |
| Institutional betrayal | Smith and Freyd (2014); McAdams et al. (2025); Lewis et al. (2025) | Institutions can compound harm by violating dependency, suppressing disclosure, or failing those who rely on them | That every institutional failure is betrayal or that the same instrument transfers unchanged across domains |
| Structural prevention | Molendijk (2025); World Health Organization Regional Office for Europe (2025) | Individual resilience interventions are insufficient where institutions generate the conflict or unsafe conditions | That all distress is structurally caused or that individual support lacks value |
| Restorative justice and moral repair | Walker (2006); Zehr (2002); UNODC (2020) | Repair can involve acknowledgment, accountability, restitution, participation, restored standing, and non-recurrence | That restorative processes are always safe, voluntary, sufficient, or substitutes for protection and law |
| Remedy and reparation | United Nations (2005) | Protection, truth, restitution, compensation, rehabilitation, satisfaction, and non-recurrence are distinguishable remedial dimensions | That every private or institutional dispute falls under the same legal framework |
| Bioethical governance | National Commission for the Protection of Human Subjects of Biomedical and Behavioral Research (1979); UNESCO (2005); O'Neill (2002) | Respect, welfare, justice, consent, vulnerability, and trust require institutional as well as interpersonal safeguards | That research ethics principles automatically settle every technological or political case |
| Feminist and critical ethics | Young (2011); Fricker (2007); Medina (2013); Tronto (1993) | Social position, division of labor, dependency, and epistemic power affect moral reasoning and responsibility | That structural analysis eliminates individual agency or licenses identity-essentialist judgment |
| Spiritual and contemplative ethics | *Bhagavad Gita*; *Daodejing*; Buddhist and ahimsa traditions as interpreted here | Nonattachment, non-humiliation, compassion, disciplined attention, and reduced ego-defense can orient moral formation | Empirical proof of metaphysical doctrines or exemption of spiritual institutions from accountability |

## E.1 Operationalization cautions

### Justificatory integrity

Possible indicators include evidential asymmetry, hidden alternatives, shifting standards, omission of affected parties, concealed uncertainty, and resistance to correction. No one indicator proves self-deception. Research should compare rival explanations including ordinary error, limited attention, role demands, fear, incomplete information, and sincere disagreement.

### Responsibility

Operational studies should keep distinct:

- direct causal contribution;
- knowledge and foreseeability;
- formal authority;
- practical control;
- benefit;
- duress;
- prevention capacity;
- and repair capacity.

Institutional charts are not sufficient evidence of practical power.

### Moral injury

Studies should state whether they investigate:

- perpetration;
- failure to prevent;
- witnessing;
- betrayal;
- victimization;
- moral distress;
- existential or spiritual conflict;
- or a proposed disorder construct.

The populations, time windows, instruments, and clinical thresholds must be declared.

### Correctability

A valid institutional measure should not rely only on self-reported process existence. It should include, where relevant:

- who reaches the process;
- who withdraws;
- retaliation risk;
- review independence;
- reversal authority;
- remedy delivered;
- recurrence;
- record correction;
- affected-party evaluation;
- and external or jointly governed evidence.

### Artificial intelligence

AI ethics studies should declare the full sociotechnical system:

\[
\text{model}
+
\text{data}
+
\text{interface}
+
\text{operator}
+
\text{institution}
+
\text{incentives}
+
\text{affected beings}.
\]

Model performance alone does not establish legitimacy. Model self-report alone does not establish patiency. Absence of patiency would not remove the duties of designers, deployers, owners, or institutions.

# Appendix F. Glossary

**Affected-being set.** The declared set of humans, nonhuman animals, possible artificial patients, represented ecological interests, and present or future groups whose morally relevant interests may be altered by a decision.

**Agency.** Capacity to understand, form or revise purposes, respond to reasons, act with some control, and participate in authorship of conduct. Agency is graded and domain-relative.

**Answerability.** A responsibility relation in which an actor owes an account of conduct, role performance, or institutional action even when blame or punishment is not yet established.

**Beneficiary responsibility.** Forward-looking or remedial responsibility associated with receiving, retaining, or controlling benefits produced by harmful arrangements, especially when the beneficiary has capacity to alter or repair them.

**Blame.** A reactive or evaluative response to culpable conduct. G.1.1 treats blame as distinct from causal attribution, answerability, liability, punishment, and remedial duty.

**Compassionate moral address.** Accountability that preserves standing and seeks understanding sufficient for protection and repair without converting compassion into excuse or requiring intimacy.

**Conditional admissibility.** A verdict that an option satisfies the declared screen relative to the represented parties, evidence, scenarios, floors, and presented option set. It is not by itself an all-things-considered declaration of moral permissibility.

**Consent.** Substantively voluntary and adequately informed authorization under conditions of sufficient capacity, alternatives, and freedom from undue influence. Consent is not identical with assent, compliance, or absence of resistance.

**Correctability.** Practical capacity to detect error or harm, receive protected challenge, review independently, reverse or revise decisions, provide remedy, measure recurrence, and learn.

**Domination.** Exposure to another's uncontrolled or insufficiently accountable capacity for arbitrary interference, including dependency that makes formal refusal practically unavailable.

**Ethical profile.** A multidimensional representation of standing, agency, welfare, consent, distribution, integrity, legitimacy, responsibility alignment, uncertainty management, coercion, and repair. It is not a universal moral score.

**Floor.** A protected minimum condition that may not be traded away through ordinary aggregate compensation under the declared decision rule.

**Institutional betrayal.** Harm or intensified injury arising when an institution on which people depend violates that dependence, suppresses disclosure, abandons protection, or fails to respond appropriately.

**Justificatory integrity.** Truth-sensitive, symmetric, affected-party-inclusive, uncertainty-aware, and correction-capable handling of reasons and evidence.

**Legitimacy.** Qualified authority of power or institutions to issue, enforce, or maintain rules in ways that are answerable to those subject to them and constrained by protected standing and correction.

**Moral agency.** Capacity to understand and respond to moral reasons sufficiently for some form of responsibility. Moral agency does not automatically imply sovereignty.

**Moral distress.** Distress associated with perceived moral constraint, conflict, or inability to act according to one's moral judgment. The term should not be used as a synonym for every difficult feeling at work.

**Moral injury.** A developing empirical and clinical construct concerning enduring psychological, relational, existential, social, or spiritual suffering associated with morally significant action, inaction, witnessing, victimization, or betrayal.

**Moral patiency.** Status of being a possible bearer of morally relevant welfare, suffering, interests, or harm. Patiency does not require responsibility or authority.

**Noncompensation.** The principle that some severe, concentrated, nonconsensual, or standing-destroying losses are not made permissible merely by unrelated benefits elsewhere.

**Option-set adequacy.** The degree to which the alternatives presented for evaluation include relevant feasible, less restrictive, reparative, staged, no-action, and affected-party-proposed options, with reasons given for consequential exclusions. It cannot be inferred from the fact that one presented option passes a screen.

**Non-recurrence.** Changes in incentives, rules, authority, training, records, resources, and monitoring that reduce the probability that a wrong or harm will be repeated.

**Patiency.** See *moral patiency*.

**Public justification.** Practice by which coercive or high-impact decisions are rendered answerable through reasons, evidence, disagreement, and correction available to the people subject to them. Public does not mean universally agreed.

**Reconciliation.** Re-establishment or transformation of a relationship after conflict or harm. It is distinct from repair, forgiveness, trust, renewed contact, or legal settlement and must not be coerced.

**Remedial responsibility.** Responsibility to stop, reduce, acknowledge, compensate, repair, or prevent recurrence of harm, which can arise from causation, role, benefit, capacity, or institutional obligation.

**Repair.** A profile of protection, truth, accountability, restitution or reparation, support, restored standing, non-recurrence, and appropriately authoritative participation. Repair may require separation rather than reconciliation.

**Reversibility.** Capacity to halt, contain, roll back, repair, or preserve future options after an intervention. Reversibility can be a protected floor in credible severe-harm cases or a comparative factor elsewhere; it is not a universal trump over the harms of delay.

**Responsibility–authority alignment.** Requirement that people not be assigned obligations for outcomes without adequate information, resources, discretion, and power, and that those with power remain answerable for its exercise.

**Rights.** Protected claims or conditions shielding welfare, integrity, liberty, capability, participation, and standing from domination and unrestricted aggregate tradeoff. Their content is not derived from system coherence alone.

**Self-deception.** Motivated asymmetric processing that protects an identity, advantage, attachment, authority, or policy by excluding, reframing, discounting, or neutralizing relevant reasons. Error and disagreement alone are insufficient.

**Sovereignty.** Legitimate authority to govern oneself or exercise binding control in a jurisdiction. Patiency, intelligence, or consciousness does not automatically establish sovereignty over others.

**Standing.** Recognition that a being or group has a claim that must enter the justificatory process, even when that party lacks institutional voice, ordinary agency, citizenship, or direct representation.

**Structural moral injury.** Moral injury produced or intensified through institutional roles, incentives, authority gaps, betrayal, concealment, retaliation, or systematic offloading of moral conflict onto less powerful actors.

**Tragic conflict.** A choice situation in which every available option leaves morally serious loss and no residual-free solution exists. The category should not be used when additional options could be created through redistribution or institutional redesign.

# Appendix G. Disposition of the March 2026 Ethics Architecture

| March 2026 element | G.1.1 disposition | Reason |
|---|---|---|
| Moral failure is primarily justificatory corruption by self-deception | **Retained in narrowed form** | Self-deception is a major moral failure and diagnostic concern, but not the sole or primary explanation in every case |
| An action is impermissible when its justification requires systematic self-deception | **Retained as a necessary-failure condition** | Such a defense is inadequate, but its absence does not establish permissibility |
| The normative principle is single, negative, and transcendental | **Reconstructed** | G.1.1 offers a bounded transcendental constraint within a plural normative architecture rather than one complete ethical principle |
| Coherence supplies the ground of moral truth | **Retired as a derivation claim** | Descriptive organization does not yield normativity without independent premises |
| Justificatory integrity | **Retained and strengthened** | Now includes affected-party representation, public records, uncertainty, symmetry, dissent, and correction |
| Self-deception as a psychological process | **Retained under Psychology E.1.1 safeguards** | Requires process evidence and symmetric testing; disagreement, error, trauma, and identity are not sufficient |
| Institutionalized self-deception | **Reconstructed as institutional distortion** | Institutions need not possess one psyche; distortion can arise through incentives, records, roles, classification, and retaliation |
| Kantian ethics contains a structural vulnerability | **Qualified** | The problem is not unique to Kant; every tradition can be applied through distorted premises and institutions |
| Compassion is an epistemic prerequisite | **Retained as a normative commitment and fallible capacity** | Compassion can improve attention and reduce humiliation but does not guarantee truth or justice |
| Virtue and contemplative practice support moral reasoning | **Retained with misuse safeguards** | Practice can reduce defensiveness but can also rationalize passivity, hierarchy, purity, or spiritual bypassing |
| Moral injury | **Retained with empirical-status discipline** | The construct is developing and must remain distinct from distress, diagnosis, wrongdoing, and character judgment |
| Structural moral injury | **Expanded** | Includes responsibility–authority gaps, institutional betrayal, unsafe conditions, concealment, and resilience offloading |
| Punishment | **Reconstructed** | Neither categorically required nor excluded; must be separately justified by protection, desert, deterrence, rehabilitation, proportionality, and alternatives |
| Repair | **Expanded into a profile** | Protection, truth, accountability, restitution, support, standing, non-recurrence, and participation are non-substitutable |
| Rawlsian role reversal and veil reasoning | **Retained as diagnostics** | They do not prove justice or ensure inclusion of all affected beings |
| Abortion and animal-rights appendices | **Not reproduced as framework verdicts** | These questions require deeper domain evidence, affected-community participation, and moral-status analysis than a general reconstruction can provide |
| Every central ethical claim is empirically testable | **Retired** | Normative principles are challenged through argument, counterexample, implication, and public justification; empirical claims are testable in different ways |
| Floor screening establishes moral permissibility | **Rejected** | Screening establishes only conditional admissibility relative to declared floors, parties, scenarios, evidence, and the presented option set |
| Reversibility as an undeclared optional coordinate | **Reconstructed** | Credible severe-harm applications must use a declared reversibility or containment floor or state a necessity-and-proportionality exception |
| Principle promotion by aggregate review approval | **Rejected** | Required review gates are conjunctive; unresolved conflict preserves provisional status and published dissent |
| AI as an external moral mirror | **Retained with institutional qualification** | AI can expose or amplify justificatory patterns, but it can also automate distance, inherit hidden norms, and serve concentrated power |
| Spiritual traditions converge on one ethics | **Retired as descriptive generalization** | G.1.1 preserves interpretive resonances while respecting doctrinal, historical, and political differences |
| Positive flourishing as maximal coherence | **Retired** | Flourishing is plural, relational, culturally mediated, and not reducible to one scalar state |

## G.1.1 What survives most deeply

The enduring insight of the original paper is not that ethics has only one principle. It is that moral life depends on the conditions under which reasons can be offered, heard, corrected, and acted upon without sacrificing the agency and standing that make justification possible.

G.1.1 preserves that insight and adds what the earlier formulation lacked:

- people can knowingly and candidly do injustice;
- institutions can distort responsibility without anyone holding a complete deceptive intention;
- consequences, rights, distributions, and power do not disappear when reasoning is sincere;
- repair is not reducible to confession or punishment;
- and the people affected by a moral framework must possess standing in its construction.

# Supplement H. Independent audit and bounded repair

The independent audit reproduced the deterministic policy screening, declared scalarizations, exhaustive 92,378-case weight lattice, Pareto relations, and non-dominance results. It identified three bounded issues that were repaired in G.1.1:

1. a floor-count sentence was corrected;
2. reversibility received a context-specific floor-or-exception architecture under credible severe-harm risk;
3. floor compliance was explicitly distinguished from option-set adequacy.

The repair also established a conjunctive promotion rule: unresolved disagreement among required philosophical, empirical, legal, misuse, and affected-community review gates blocks canonical promotion rather than being settled by simple voting across unlike competencies.

The audit did not validate the moral truth of the principles, the adequacy of the stipulated profiles, the complete literature review, or any legal application.

# Supplement I. Truth-centered publication transformation

The reader-facing paper reorganizes the audited content without changing its formal results.

| Technical authority | Publication treatment |
|---|---|
| Normativity section | Condensed into the Mandala-grounded opening |
| Self-deception section | Moved to the first analytical movement after model declaration |
| Justificatory integrity | Retained as necessary but insufficient |
| Testimony, records, dissent, option sets, correctability | Integrated into a new section on truth beyond introspection |
| Virtue and contemplative practice | Reframed around compassion as epistemic discipline |
| Standing, consequences, power, responsibility | Preserved as substantive constraints on truthful judgment |
| Moral injury and betrayal | Preserved with empirical and clinical boundaries |
| Repair | Preserved as protection, truth, accountability, restitution, standing, and non-recurrence |
| AI | Preserved as moral assistance without sovereignty |
| Interpretive conclusion | Replaced by CU-COM12 and the vow of moral truthfulness and repair |

# Supplement J. Reproducibility boundary

The deterministic suite tests non-entailments and bookkeeping claims internal to the manuscript. It does not establish moral weights, threshold values, legal standards, clinical diagnoses, or empirical prevalence. Reproduction requires only Python's standard library. The archived result JSON should regenerate byte-for-byte under the same script version.
