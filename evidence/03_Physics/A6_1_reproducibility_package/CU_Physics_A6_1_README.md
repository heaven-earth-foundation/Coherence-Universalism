# CU Physics A.6.1 Reproducibility Package

This package accompanies `CU_Physics_Systematic_Reconstruction_Kaya_A6_1.md` and records the response to the independent audit of A.6.

## Contents

- `CU_Physics_Systematic_Reconstruction_Kaya_A6_1.md` — corrected manuscript.
- `CU_Physics_A6_Independent_Audit.md` — independent audit supplied by the author.
- `CU_Physics_A6_1_AUDIT_RESPONSE.md` — formal disposition of every material audit finding.
- `CU_Physics_A6_1_CHANGELOG.md` — cumulative change ledger and release status.
- `CU_Physics_A6_to_A6_1.patch` — unified textual diff from A.6.
- `CU_Physics_A6_1_reproducibility.py` — deterministic verification suite.
- `CU_Physics_A6_1_verification_results.json` — generated numerical and structural result record.
- `CU_Physics_A6_1_QA_REPORT.txt` — structural, parse, hash, and numerical QA summary.
- `CU_Physics_A6_1_REQUIREMENTS.txt` — package versions used for the recorded run.
- `CU_Physics_A6_1_MANIFEST.sha256` — checksums for every packaged file except the manifest itself.

## Reproduce the report

From the package directory:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r CU_Physics_A6_1_REQUIREMENTS.txt
python CU_Physics_A6_1_reproducibility.py \
  --output CU_Physics_A6_1_verification_results.regenerated.json
```

The full run performs:

- finite-partition differentiation and entropy checks;
- Euclidean and Fisher wedge diagnostics;
- exact two-level degeneracy checks;
- the fixed-coupling stationary threshold and critical-direction check;
- exhaustive reduced Fisher extrema;
- lattice-wave dispersion simulation;
- Madelung residual and convergence checks;
- reproduction of the legacy overdamped table; and
- an exact-modal, two-initialization overdamped comparison through \(\eta=3000\).

For a faster theorem-and-extrema run without the wave, Madelung, and damping calculations:

```bash
python CU_Physics_A6_1_reproducibility.py \
  --skip-heavy \
  --output CU_Physics_A6_1_verification_results.light.json
```

## Compare results

Floating-point residuals and platform metadata may vary slightly across hardware and library versions. The exact formulas, equality sets, threshold equations, and asymptotic classifications should remain unchanged.

The recorded script hash in the JSON must match the packaged script. The QA report checks this condition.

## Verify package integrity

```bash
sha256sum -c CU_Physics_A6_1_MANIFEST.sha256
```

## Audit interpretation

The independent audit confirmed the principal A.6 block, wedge, extrema, and strong-damping results. A.6.1 repairs the evidential interpretation of the original overdamped slope and adds two qualified model-internal results:

- a maximum coupling \(r_*=0.621360943645626\ldots\) above which no nonuniform interior stationary point exists; and
- a uniform-state linear-stability threshold at \(r=1/2\), with a nonhyperbolic critical case.

The geometric wedge-degeneracy set remains continuous at every coupling. The fixed-coupling result concerns only where the chosen combined vector field vanishes.

## Epistemic status

The suite verifies algebraic identities numerically, checks analytic reductions, and tests selected discretizations. These computations do not establish that CU is physically fundamental, do not show that the embedded physical equations are uniquely selected, and do not replace human expert review. The independent audit explicitly did not cover Sections 8–10, the full Madelung derivation, the wave/Madelung numerical runs, or the bibliography.
