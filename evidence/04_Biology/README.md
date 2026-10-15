# Evidence directory — Coherence Universalism: Biology

This directory makes the paper's audit, scripts, machine-readable results, source ledger, and historical verification materials reachable from the same release package.

The current reader-facing manuscript controls wording and claim status. Legacy files retain their original identifiers for provenance and do not override later Wave 1–3 corrections.

## Included files

- `Biology_v0.10_PC4_MANIFEST.sha256`
- `Biology_v0.10_PC4_QA_REPORT.txt`
- `Biology_v0.10_PC4_README.md`
- `Biology_v0.10_PC4_Source_Ledger.json`
- `Biology_v0.10_PC4_Synchronization_Ledger.md`
- `independent_audit.md`
- `independent_audit_checks.py`
- `independent_audit_output.txt`

## Deterministic model scripts

- `C1_1_reproducibility_package/CU_Biology_C1_1_reproducibility.py` — the original script that generates every number in Supplement B; it writes `CU_Biology_C1_1_verification_results.json` and ends with "All regression checks passed." Requires NumPy. The package's `CU_Biology_C1_1_MANIFEST.sha256` verifies its files.
- `independent_reconstruction/` — an independent implementation written from the supplement's text alone, which reproduces the same values to ten decimal places.

## Scope boundary

Reproducibility establishes that declared formulas or constructed models produce their reported outputs. It does not establish that CU's domain interpretation is empirically correct, normatively authoritative, or suitable for consequential deployment.
