# GitHub import metadata for distribution 0.10.1

This GitHub-upload copy preserves all 372 files from `CU_v0.10_Source_Repository_v0.10.1.zip` byte for byte. It adds two directory-local Git metadata overrides and this explanatory note. It is not a new manuscript edition, a replacement PDF build, or a changed scientific release.

The frozen source ZIP has SHA-256: `cad66bee733e471b90cbe67ba6e30f9ceb9db338c9f4e68e3a78d88b9491bedd`.

## Why the two overrides are needed

- The repository-root `build/` ignore pattern would otherwise omit nine required Mandala build-input files during an ordinary first import. The companion-local `.gitignore` explicitly includes that archived directory.
- The root `.gitattributes` requests LF line-ending normalization. Five supplied registry CSV files contain CRLF line endings covered by the source checksum manifest. `registries/.gitattributes` disables Git text conversion for registry CSVs, preserving their exact archived bytes through import and clone.

## Scope

All original manuscripts, mathematical and numerical evidence, registry content, PDF-build sources, release manifests, licenses, version declarations, and other original files remain unchanged. The directory-local overrides affect Git transport and initial file selection only. Existing source-manifest checks continue to validate every original listed file. This note and the two Git metadata additions are not part of the original frozen ZIP.

Use this upload copy to populate the repository, but retain the original source and reader ZIPs as the named distribution assets. The research version remains 0.10, the distribution remains 0.10.1, and the Mandala remains 0.4.
