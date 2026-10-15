# Evidence directory — Coherence Universalism: Physics

This directory makes the paper's audit, scripts, machine-readable results, source ledger, and historical verification materials reachable from the same release package.

The current reader-facing manuscript controls wording and claim status. Legacy files retain their original identifiers for provenance and do not override later Wave 1–3 corrections.

## Included files

- `Physics_v0.10_PC4_MANIFEST.sha256`
- `Physics_v0.10_PC4_QA_REPORT.txt`
- `Physics_v0.10_PC4_README.md`
- `Physics_v0.10_PC4_Source_Ledger.json`
- `Physics_v0.10_PC4_Synchronization_Ledger.md`
- `independent_audit.md`
- `independent_audit_checks.py`
- `independent_audit_output.txt`

## Deterministic model scripts

- `A6_1_reproducibility_package/CU_Physics_A6_1_reproducibility.py` — the original script behind the Physics supplement's block-averaging, wedge, Fisher-bound, fixed-coupling, lattice-dispersion, Madelung, and overdamped-limit results; it writes `CU_Physics_A6_1_verification_results.json`. Requires NumPy and SciPy (see `CU_Physics_A6_1_REQUIREMENTS.txt`). The package's `CU_Physics_A6_1_MANIFEST.sha256` verifies its files.

## Scope boundary

Reproducibility establishes that declared formulas or constructed models produce their reported outputs. It does not establish that CU's domain interpretation is empirically correct, normatively authoritative, or suitable for consequential deployment.
