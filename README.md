# Coherence Universalism - Version 0.10

**Distribution package: 0.10.1.** See the [Release Index](RELEASE_INDEX.md), [reproduction instructions](REPRODUCIBILITY.md), and [change record](CHANGELOG.md).

Coherence Universalism (CU) is an integrative philosophical and research framework organized around one recurring question:

> What must be related, constrained, preserved, and made correctable for something to remain itself while it changes?

Start with **[What Is Coherence Universalism?](00_What_Is_Coherence_Universalism_v0.10.md)**. It is the human-facing doorway into the project. The controlling scholarly architecture begins with **[Metaphysics and Epistemology](papers/01_CU_Metaphysics_Epistemology_v0.10.md)** and **[Foundations](papers/02_CU_Foundations_v0.10.md)**.

## Published records and reader access

[Foundation research page](https://heavenearthfoundation.org/theory-research/) | [Complete-release archive](https://zenodo.org/records/23404449) | [GitHub release downloads](https://github.com/heaven-earth-foundation/Coherence-Universalism/releases/tag/v0.10.1)

The eleven papers and Mandala have individual DOI entries in the [citation directory](CITATIONS.md). Use the DOI for the particular work and version being cited.

[Explore the interactive Mandala](https://heaven-earth-foundation.github.io/Coherence-Universalism/mandala/) or [download its original offline ZIP](https://github.com/heaven-earth-foundation/Coherence-Universalism/releases/download/v0.10.1/Mandala_v0.4_Interactive_Graph.zip). GitHub Pages must be enabled for main /docs before the browser address becomes available; see [setup and graph provenance](docs/README.md).

The frozen v0.10.1 release assets remain unchanged. The main branch also contains the [documented verifier portability correction](CI_PORTABILITY_NOTE_2026-10-19.md) and publication-link maintenance. Report the actual commit when using code from main.

## What Version 0.10 contains

- eleven reader-facing papers;
- a 228-record synchronized principle and commitment registry, including CU-M15;
- a sixty-four-stage Coherence Mandala;
- technical supplements and deterministic constructions;
- paper-specific evidence and audit records;
- reproducibility and release-verification scripts;
- an official noncontrolling two-volume Mandala companion and interactive graph distributed as release assets.

## Claim-status caution

Version 0.10 distinguishes definitions, formal results, conditional results, empirical hypotheses, interpretations, commitments, governance proposals, and open problems. Reproducibility shows that a reported computation follows from its code and assumptions. It does not show that the model describes the world. Internal synchronization does not constitute external validation.

The audits include bibliographic checks and selected source verification, especially for recent and load-bearing claims. They are not a comprehensive independent validation of every empirical citation.

## Reading order

1. `00_What_Is_Coherence_Universalism_v0.10.md`
2. `papers/01_CU_Metaphysics_Epistemology_v0.10.md`
3. the domain paper nearest your expertise;
4. `papers/02_CU_Foundations_v0.10.md` for controlling wording and statuses;
5. the Mandala companion for the whole-system architecture.

All papers are designed to be read independently, though cross-references become more meaningful after reading the first two.

## Repository structure

- `papers/` — the nine controlling papers and two noncontrolling scholarly companions.
- `supplements/` — formal derivations, deterministic constructions, and addenda.
- `registries/` — active machine-readable registries only.
- `evidence/` — scripts, results, manifests, and paper-specific evidence.
- `companions/mandala/` — Markdown and digital-source components of the official noncontrolling Mandala companion.
- `scripts/` — release verification and reproducibility runners.
- `provenance/` — RC3 history, external audits, and release-convergence records.
- `docs/` - GitHub Pages graph, DOI directory, and public link registry.
- `release-manifests/` — checksums and external-asset manifests.

## Verification

Create an environment using `requirements-release.txt`, then run:

```bash
python scripts/verify_release.py --core
python scripts/run_reproducibility.py
```

The full gate also verifies separately downloaded Mandala release assets:

```bash
python scripts/verify_release.py --full --assets-dir /path/to/release-assets
```

## AI collaboration and responsibility

ChatGPT and Claude contributed extensively to drafting, formalization, coding, auditing, and publication engineering. The author made the final interpretive, normative, and publication decisions and remains responsible for the release. Machine contributions are documented in provenance and audit records rather than hidden.

## License

Text and figures are released under **CC BY 4.0**. Code is released under the **MIT License**. See `LICENSE.md`, `LICENSE-TEXT-CC-BY-4.0.md`, and `LICENSE-CODE-MIT.txt`.

## Citation

Rader, G. K. D. (2026). *Coherence Universalism: Version 0.10 Research Release (Distribution 0.10.1)*. Heaven≡Earth Foundation. [Archived release](https://zenodo.org/records/23404449).

Use [CITATIONS.md](CITATIONS.md) for the individual-paper and Mandala DOI links. Machine-readable metadata are in [CITATION.cff](CITATION.cff) and [CITATIONS.bib](CITATIONS.bib). The complete-release URL is retained without guessing its DOI.

The root runner executes six required saved-result suites. It does not rerun every historical audit or validate all domain hypotheses. Publication and correction guidance is in [CORRECTIONS.md](CORRECTIONS.md).

## Publication PDF build

The paper PDFs use a source-based, math-safe export after Word-to-PDF conversion defects were found. See [reader-build/README.md](reader-build/README.md). Pagination differs from the earlier download-recovery record; the scientific content is unchanged.
