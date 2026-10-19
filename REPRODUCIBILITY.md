# Reproducing the released constructions

## Environment

The current verification used Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0 and SymPy 1.14.0, matching requirements-release.txt. Create an isolated environment and install that file before running the commands from the repository root.

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-release.txt
python scripts/verify_release.py --core
python scripts/run_reproducibility.py
```

The runner requires six specific suites: Physics, Biology, Ethics, Artificial Intelligence, Denying Knowledge and Non-Egoic Mind. It copies each suite to a temporary directory, removes the expected output, executes the script and compares the regenerated JSON with the shipped result. A missing script, missing output, nonzero exit, numerical mismatch or false top-level regression outcome fails rather than being skipped. Biology can take several minutes.

The post-release maintenance comparator retains relative and absolute tolerances of 1e-9 for ordinary scientific fields. Physics-only bounded-optimizer scan coordinates use an absolute tolerance of 5e-8, and the two derived continuity-refinement ratios use a relative tolerance of 1e-7 with the original 1e-9 absolute floor. Exact/root-based constants and scanned objective values remain at the original tolerance. Additional probability normalization, objective-consistency and ratio-consistency checks use 1e-12 relative and absolute tolerances. These exceptions address experimentally reproduced CPU-dispatch sensitivity, not changed scientific models or reference results.

The runner executes eighteen comparator regression tests before the six suites and reports deviations accepted under the scoped exceptions. Only the same explicitly listed environment and hash fields are excluded. Model versions, seeds, scientific time variables, text, booleans and data shapes remain compared, with integer pairs compared exactly. Full rationale and scope appear in CI_PORTABILITY_NOTE_2026-10-19.md. A new GitHub run must confirm remote success after the maintenance commit.

To verify the five separate Mandala archives, place them together in one directory, under the filenames recorded in release-manifests/MANDALA_ASSETS.sha256, and run:

```sh
python scripts/verify_release.py --full --assets-dir /absolute/path/to/downloads
```

## Scope

A successful computation is not empirical evidence that a model describes the target domain. These six saved-result suites are not a rerun of every historical audit, a new proof review, or a clinical, ethical or deployment validation. Historical audit scripts may assume older folder structures; they remain provenance, not supported current entry points. A prior upstream wrapper referred to research_inputs/verify_information_geometry.py, which was absent from the supplied repository. No success for that absent check is claimed here.

The former v0.10.0 default command silently skipped every intended suite because of path/pattern errors. Its source and the observed output are preserved under provenance/release-engineering-v0.10.0. This packaging repair fixes that command rather than rewriting the constructions or their expected results.
