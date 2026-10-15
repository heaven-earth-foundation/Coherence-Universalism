# CU Biology C.1.1 Reproducibility and Audit-Repair Package

## Purpose

This package accompanies `CU_Biology_Systematic_Reconstruction_Kaya_C1_1.md`, the bounded post-audit repair of the CU Biology reconstruction under Physics A.6.1 and Canonical Base B.2.

C.1.1 preserves C.1's non-scalar biological architecture and addresses the independent audit's principal findings:

- the viability effect of diffusive mean coupling is configuration-dependent;
- the original homogeneous-floor sweep measures margin movement well inside the viable region rather than coupling-mediated rescue;
- an added heterogeneous-floor configuration exhibits a strict adverse margin trend and a viability crossing;
- clipping is explicitly counted and is inactive in all reported controller runs;
- five claim-governance rules now appear in the manuscript body;
- the designer/as-if/evolutionary distinction is exported to later domain papers; and
- the *Stentor* literature description is expanded within the cited source's scope.

## Principal files

- `CU_Biology_Systematic_Reconstruction_Kaya_C1_1.md` — revised manuscript.
- `CU_Biology_C1_1_CHANGELOG.md` — cumulative reconstruction and audit-repair ledger.
- `CU_Biology_C1_1_AUDIT_RESPONSE.md` — formal disposition of the independent audit.
- `CU_Biology_C1_to_C1_1.patch` — unified manuscript diff.
- `CU_Biology_C1_1_LITERATURE_LEDGER.md` — source-to-claim scope map.
- `CU_Biology_C1_1_claim_ledger.json` — machine-readable Appendix C registry.
- `CU_Biology_C1_1_principle_registry.json` — candidate CU-B1–B5 registry and governance rules.
- `CU_Biology_C1_1_reproducibility.py` — deterministic two-configuration control model.
- `CU_Biology_C1_1_verification_results.json` — generated numerical output.
- `CU_Biology_C1_1_QA.py` and `CU_Biology_C1_1_QA_REPORT.txt` — structural and regression checks.
- `SOURCE_CU_Biology_C1.md` — frozen pre-repair manuscript.
- `SOURCE_CU_Biology_C1_Independent_Audit.md` — frozen independent audit.
- `CU_Biology_C1_1_MANIFEST.sha256` — package integrity hashes.

## Reproduction

From the extracted package directory:

```bash
python CU_Biology_C1_1_reproducibility.py --output reproduced_results.json
python CU_Biology_C1_1_QA.py \
  --manuscript CU_Biology_Systematic_Reconstruction_Kaya_C1_1.md \
  --results reproduced_results.json \
  --report reproduced_QA_REPORT.txt
```

Compare the regenerated output:

```bash
cmp reproduced_results.json CU_Biology_C1_1_verification_results.json
```

Verify archive integrity:

```bash
sha256sum -c CU_Biology_C1_1_MANIFEST.sha256
```

## Numerical scope

Both models use the same diffusive coupling operator and controller but different floors, natural equilibria, targets, and disturbance schedules.

- **Configuration I:** minimum margin rises with coupling while control cost and differentiated target error rise; all controller runs remain viable.
- **Configuration II:** minimum margin falls with coupling and becomes negative at and above the reported sweep threshold.

The models are pedagogical. They are not fitted to biological data, do not identify an organism's optimal coupling, and provide no empirical validation of Coherence Universalism.

## Audit boundary

The independent audit did not comprehensively review the philosophy-of-biology synthesis, most formal propositions, the claim ledger row by row, CU-B1 through CU-B5 on conceptual grounds, or most references. Automated QA establishes internal package consistency, not biological truth or peer review.
