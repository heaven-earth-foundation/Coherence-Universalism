# GitHub Pages: Mandala and publication links

This new docs folder publishes a static navigation/citation page and the existing interactive Mandala. It does not change the Foundation's WordPress site or require a custom domain.

## One-time setup

After this folder has been committed and pushed to main, open repository Settings > Pages. Under Build and deployment, choose Deploy from a branch, then main and /docs, then Save. Leave Custom domain blank unless an independently planned domain setup already exists. Confirm the actual published URL shown by GitHub and test it before enabling the graph button on WordPress.

Expected default address: https://heaven-earth-foundation.github.io/Coherence-Universalism/
Expected graph address: https://heaven-earth-foundation.github.io/Coherence-Universalism/mandala/

The .nojekyll file disables an unnecessary Jekyll build. Copy the entire docs folder so this hidden file is included. GitHub may run a separate pages build and deployment job as well as the existing Verify release job.

## Files and provenance

- index.html: navigation and twelve-work DOI directory.
- mandala/index.html: an exact byte copy of [the existing graph](../companions/mandala/Mandala_v0.4_Interactive_Graph.html).
- CITATIONS.bib: byte-identical copy of [the repository bibliography](../CITATIONS.bib).
- publication-links.json: supplied record URLs and DOIs, plus planned graph address and source provenance.
- .nojekyll: static publishing marker.

Graph SHA-256: 17ecf2a3d2955eb3e4d253f9d851351e420094c5703fd8dd32af132acdebc8ed

The graph embeds its nodes, edges, styles, and JavaScript. It does not fetch a library or data service. Neither its typed data nor its filtering code was altered. The landing page's offline button downloads that same HTML.

Identifiers come from the author's completed progress export of 21 October 2026. All twelve individual records have supplied version-specific DOIs. The complete collection retains its supplied record URL; no collection DOI was invented. No live DOI metadata or GitHub Pages deployment was independently verified during preparation.

## References

- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

This metadata/hosting update is maintenance on main. It does not move the v0.10.1 tag, replace its downloads, or modify the published Zenodo records.
