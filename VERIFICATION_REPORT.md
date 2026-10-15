# CU v0.10 / distribution 0.10.1: verification report

Prepared 13 October 2026. This report describes local preparation and testing. It is not a claim that any website, repository, DOI record or preprint submission has been published.

## Input integrity

All seven supplied ZIP archives opened and passed CRC tests. All seven SHA-256 values match the supplied recovery manifest or source-repository verification value. In particular, the original source repository hash is `fffa0d1229c4fd3275fd6118f4efa8335815a92719cd207ee4255f456e04b5b5`. The five Mandala ZIP archives in downloads retain their original bytes, under standardized release filenames. The original input files were not overwritten.

The uploaded set omitted the earlier paper-PDF archives. Their absence was a format-delivery gap, not missing manuscript source: final Word and Markdown copies were present.

## Packaging defects identified and repaired

The v0.10.0 default reproduction runner skipped all six intended suites because its path patterns did not match the repository, then reported PASS. It is replaced by an explicit required-suite runner that fails on missing inputs, missing regenerated results, nonzero exits, mismatches or failed regression outcomes. The numerical model scripts and saved scientific results were not changed.

The initial source check also found 146 unresolved relative-link occurrences, missing Mandala figure dependencies, a false-negative typed-graph wording check, and a release-label check that counted historical references. Current source/supplement/evidence paths have been repaired, 104 unchanged supplied Mandala PNGs restored to their expected paths, and the checks narrowed to the intended controlling text. One stale sentence now says 'This release synchronizes' rather than 'This release candidate synchronizes.' Historical references and archived originals remain available.

The source index, citation records, correction route, PDF build instructions and per-destination upload worksheets have been supplied. The existing CC BY 4.0 text and MIT code license files are unchanged. No DOI, ORCID, contact address or repository location was fabricated.

## Mathematical and computational scope

All six required saved-result suites executed and reproduced their expected results: Physics, Biology, Ethics, Artificial Intelligence, Denying Knowledge, and Non-Egoic Mind. Result: **6 / 6 PASS, 0 FAIL, 0 SKIP**. Each suite ran in an isolated temporary directory and was required to regenerate its result file. Numerical comparisons use absolute and relative tolerances of 1e-9; the runner records the limited environment/hash fields excluded from comparison. This is not a rerun of every historical audit or proof. An absent historical information-geometry script is not counted as a success.

All 148 files under evidence/ are byte-identical to the supplied source. All eleven manuscript bodies match their inputs apart from relative link targets and the declared release-label wording. No theoretical formula, principle or claim status was revised. The actual final source contains 228 principle/commitment records and 64 Mandala stages; the older freeze memo's 227 count should not override that registry.

## PDF export: a necessary functional repair

A first Word-to-PDF attempt reproduced the earlier page counts, but targeted visual inspection found equation-conversion errors that a page-bounds scan had missed: red parser-error marks, broken multi-line alignment, set-difference notation and quantum state expressions. Those intermediate PDFs were rejected and are not in this kit.

The final eleven paper PDFs were rebuilt directly from the unchanged release Markdown with Pandoc and XeLaTeX. This preserves source mathematical content and repairs its printed representation; it necessarily changes pagination. The eight-page introduction is the revised Word export. The Word compatibility copies retain all **2,322 native math objects**, including the Biology footnote expression, unchanged at the XML level. Do not use an arbitrary Word-to-PDF conversion as a replacement for the released PDF.

The source contains the PDF build script, header, display-width filter and all eleven standalone TeX files. The header includes double-bracket support and explicit printing shims for the supplied Biology tokens \midL and \midN; these print the conditional bar and the following variable. No scientific interpretation was added by those lexical repairs.

Every page of the final eleven PDFs was scanned for out-of-page text spans, empty pages and conversion-error/replacement markers; all scans passed. TeX logs have no missing-character warnings. High-resolution visual spot checks covered the corrected alignment and quantum-state examples, introduction and release wording, with additional page overviews. This was targeted visual review, not an exhaustive page-by-page human proof audit. The existing Mandala reader PDFs were retained, not rebuilt or newly comprehensively audited.

### Final paper pagination

| File | Pages |
|---|---:|
| 01_CU_Metaphysics_Epistemology_v0.10.pdf | 84 |
| 02_CU_Foundations_v0.10.pdf | 102 |
| 03_CU_Physics_v0.10.pdf | 175 |
| 04_CU_Biology_v0.10.pdf | 71 |
| 05_CU_Consciousness_v0.10.pdf | 66 |
| 06_CU_Psychology_v0.10.pdf | 54 |
| 07_CU_Social_Dynamics_v0.10.pdf | 54 |
| 08_CU_Ethics_v0.10.pdf | 59 |
| 09_CU_Artificial_Intelligence_v0.10.pdf | 71 |
| 10_Denying_Knowledge_v0.10.pdf | 37 |
| 11_Architecture_Non_Egoic_Artificial_Mind_v0.10.pdf | 43 |

The eleven papers total 816 pages; the introduction adds 8, for 824 main-reader pages. These counts supersede only the pagination of the absent recovery PDFs, not the papers' version identity.

## Agreed editorial changes

The brief October 2026 AI policy statement is preserved in a separate author-commentary archive, outside the core research and notebook bundles. The introduction's corresponding paragraph was replaced with the agreed distinction between framework commitments and specific policy judgment. No new application paper was added; Alignment Across Scales remains the next separate project.

## Interpretation of PASS

Archive integrity establishes intact bytes. Repository checks establish the specified structure, link and registry conditions. Computation establishes reproduction of declared constructions within tolerance. None of these establishes external peer review, the empirical truth of domain hypotheses, the truth of metaphysical interpretation, or authorization for consequential deployment. Public hosting and DOI resolution must still be tested after actual upload.

## Final delivery checks

The final repository check reports **18 PASS / 0 FAIL** in core mode and **22 PASS / 0 FAIL** with the five external Mandala archives. All 371 listed source files matched the current source manifest at this gate. The prepared website's 69 local file links resolve. Twenty-nine contained ZIP copies passed CRC testing, including the seven primary release archives and paper-specific technical downloads. The publishing workspace contains thirteen Zenodo record worksheets and thirty curated notebook source files. These are local checks; no public account action is represented as completed.
