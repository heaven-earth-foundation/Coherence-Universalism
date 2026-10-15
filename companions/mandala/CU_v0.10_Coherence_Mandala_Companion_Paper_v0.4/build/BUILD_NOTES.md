# Build and verification notes

The release package contains the final reader-facing Markdown, DOCX, PDF, figures, machine-readable registries, and a portable DOCX rebuild script.

## Rebuild DOCX editions

Run from any location:

```bash
python build/rebuild_documents.py
```

The script uses the included reference DOCX and post-processing helper under `build/support/`.

## Convert to PDF

The final PDFs were produced with LibreOffice through the OpenAI PDF skill conversion helper. A local rebuild may use LibreOffice directly or an equivalent DOCX-to-PDF workflow, followed by visual rendering checks.

## Structural verification

```bash
python build/verify_wave7.py
```

The final package omits raw per-page render images because they are internal QA intermediates. The full visual-review result is preserved in `qa/CU_v0.10_Coherence_Mandala_Two_Volume_QA_Report_v0.4.txt` and the independent verification record.

## Registry provenance

The v0.4 registry layer was generated from the frozen v0.3 Mandala set, the v0.20 architecture repair, and the cumulative RC3 Wave 6 corpus. Their hashes are recorded in `provenance/SOURCE_PACKAGE_HASHES.sha256`.
