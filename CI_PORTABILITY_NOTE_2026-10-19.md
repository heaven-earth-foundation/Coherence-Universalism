# Post-release verification maintenance: Physics numeric portability

Date: 2026-10-19
Status: maintenance proposal after the v0.10.1 tag; confirm with a new GitHub Actions run after applying.
Scope: verifier and documentation only. No manuscript, numerical model, reference JSON, registry, release asset, published DOI, or scientific claim is changed. Do not move the existing release tag or overwrite its archived files.

## Observed failure and reproduction

GitHub Actions run 38789659798 passed core verification and five saved-result suites, but Physics failed ten numeric comparisons. Nine were the a, b, and total_mass_a coordinates in the bounded optimizer's support scan. One was a Madelung continuity refinement ratio. The largest coordinate difference was 4.45462219889059e-9; the ratio differed by 3.287769123616613e-8 (about 8.23e-9 relative).

Using the same Python code and pinned NumPy 2.3.5 / SciPy 1.17.0 / SymPy 1.14.0, local experiments reproduced the nine coordinate differences exactly by selecting OpenBLAS's Haswell code path. Restricting NumPy's AVX-512 paths reproduced the ratio difference exactly. A combined experiment reproduced all ten differences in one Physics run. This is an experimentally demonstrated CPU-dispatch sensitivity; it is not an identification of the original GitHub machine's precise processor or OS.

## Why one tolerance was insufficient

The original wrapper compared every floating-point field using rel_tol=1e-9 and abs_tol=1e-9. SciPy's bounded minimizer does not promise that its final x coordinate is accurate to its requested xatol alone: in SciPy 1.17.0, tol1 includes sqrt(2.2e-16)*abs(xf) + xatol/3. Near a smooth optimum, tiny changes in objective evaluation can change its final location much more than its objective value. The decisive exact/root-based constants and the scanned objective values did not fail the original comparison in the reported run.

The Madelung diagnostic divides two small discretization residual medians. Small accepted differences in those inputs can be amplified in their ratio. The exact same ratio difference was reproduced in a local CPU-dispatch experiment.

## Explicit comparison contract

- All ordinary floating-point paths: retain rel_tol=1e-9 and abs_tol=1e-9.
- Physics only, all_reduced_cases/{norm_A,norm_B,Pi_F}/0..5/{a,b,total_mass_a} and sup_{norm_A,norm_B,Pi_F}/scan_argmax/{a,b,total_mass_a}: absolute tolerance 5e-8; relative tolerance zero. These are numerical scan coordinates, not the canonical exact/root-based argmax coordinates.
- Physics only, continuity_median_refinement_factors/0..1: rel_tol=1e-7 and abs_tol=1e-9.
- Every newly accepted deviation exceeding the original tolerance is printed and included in the optional JSON report. No affected numeric field is ignored or silently removed.
- New internal checks require valid probabilities and support sizes, normalization, objective values consistent with the two-level formulas, and refinement ratios consistent with the actual raw residual medians. These internal identities use relative and absolute tolerances of 1e-12. Raw residual medians retain the original comparison tolerance.
- Exact/root-based constants, scanned objective values, model parameters, scientific time, seeds, text, booleans and data shapes retain their original checks. Integer-versus-integer comparisons are now exact.
- NaN and infinities, missing outputs, nonzero script exits, false regression outcomes and missing suites still fail. The environment/hash exclusion list is unchanged.

These are bounded numeric-regression tolerances, not formal error certificates for arbitrary machines or empirical validation of Physics.

## Tests and required follow-up

Eighteen comparator regression tests run automatically before the six suites. They verify that the ten reported differences are covered, that the other five suites receive no relaxed tolerances, and that meaningful perturbations and inconsistent probability/objective/ratio records still fail. Local CPU-dispatch probes and the detailed delivery report accompany this patch.

Run both existing commands after applying:

```sh
python scripts/verify_release.py --core
python scripts/run_reproducibility.py --report /tmp/cu-reproduction-report.json
```

The original workflow file is unchanged. A new push will run the updated verifier, including its required comparator tests. Re-running the historical failing commit alone will still use the historical script. Preserve the old run as provenance; do not claim the GitHub failure resolved until the new commit passes there.

## Reference sources

- SciPy 1.17.0 bounded minimizer implementation: https://github.com/scipy/scipy/blob/v1.17.0/scipy/optimize/_optimize.py
- SciPy bounded minimizer options: https://docs.scipy.org/doc/scipy-1.17.0/reference/optimize.minimize_scalar-bounded.html
- NumPy runtime CPU dispatch: https://numpy.org/doc/stable/reference/simd/build-options.html
- Python approximate-comparison rule: https://docs.python.org/3.13/library/math.html#math.isclose

## Baseline provenance

The GitHub-upload ZIP used for this repair has SHA-256 `62f547f99f6fe7c702db6c3af046731a5833afaf7f21080b504b66364e5918a9`.
The old runner has SHA-256 `049427547d9912a63f3f436daa6319b9cd5710b4c3dc958cc3f4a17527074fd9`.
The old source-manifest file has SHA-256 `33e9767a6fc00bf4c7feb8a1393a8ec874a69f47ab9d2ec9f4c1ebe934a0fdea`.

Only run_reproducibility.py, REPRODUCIBILITY.md, and the source-manifest file are replaced. This note and test_reproducibility_portability.py are added. Every other original file is preserved byte for byte. The source manifest changes only the two affected original-file hashes and adds the two new files; unrelated expected hashes are retained.
