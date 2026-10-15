# Building the released paper PDFs

The eleven paper PDFs in distribution 0.10.1 are built directly from the controlling Markdown with Pandoc and XeLaTeX. The first attempted Word-to-PDF export preserved page counts but produced visible parser-error marks and missing parts of several equations. Those rejected intermediate PDFs are not release files. The source-based PDFs have different pagination; the theory and source equations are unchanged.

`build_pdfs.py`, `header.tex`, `fit-display.lua`, and the eleven standalone files in `tex/` preserve the print workflow. The Lua filter constrains display width without replacing the source expression. The header loads double-bracket symbols and defines two printing shims for the run-on Biology tokens `\midL` and `\midN`, displaying them as a conditional bar followed by L or N. These are lexical print repairs, not new formulae.

From the source repository root:

```sh
python reader-build/build_pdfs.py --out /absolute/path/to/new-pdf-build --jobs 2
```

Install Pandoc, XeLaTeX, standard TeX packages including adjustbox and stmaryrd, and the Liberation Serif/Sans and DejaVu Sans Mono fonts through your system's normal package manager. No font files are distributed here. The saved TeX files also compile directly with XeLaTeX. Different TeX/font versions may alter line breaks or PDF bytes.

The editable Word copies retain their native mathematics and original layout. Cross-application equation conversion is not reliable; use the released PDF or this source-based build for publication. The eight-page introduction uses the revised Word export and contains no mathematical expressions. The Mandala PDFs remain the supplied, unchanged companion editions.
