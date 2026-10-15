#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ME = ROOT / 'CU_Metaphysics_Epistemology_v0.10_Publication_Candidate_5.md'
FD = ROOT / 'CU_Foundations_v0.10_Publication_Candidate_5.md'
MANDALA_JSON = ROOT / 'CU_v0.10_COHERENCE_MANDALA_64_STAGE_REGISTRY_B5_1.json'
CANON_JSON = ROOT / 'CU_v0.10_Canonical_Principle_Registry_B5_1.json'
REPORT = ROOT / 'CU_v0.10_Canonical_Pair_PC5_QA_REPORT.txt'

passes: list[str] = []
failures: list[str] = []

def check(cond: bool, msg: str) -> None:
    (passes if cond else failures).append(msg)

for p in [ME, FD, MANDALA_JSON, CANON_JSON]:
    check(p.exists(), f'required file exists: {p.name}')

if not failures:
    me = ME.read_text(encoding='utf-8')
    fd = FD.read_text(encoding='utf-8')
    mandala = json.loads(MANDALA_JSON.read_text(encoding='utf-8'))
    canon = json.loads(CANON_JSON.read_text(encoding='utf-8'))

    check('Publication Candidate 5' in me, 'M&E PC5 label present')
    check('Publication Candidate 5' in fd, 'Foundations PC5 label present')
    check('Systematic Reconstruction Draft' not in me, 'M&E reconstruction label absent')
    check('Systematic Reconstruction Draft' not in fd, 'Foundations reconstruction label absent')

    sec_nums = [int(x) for x in re.findall(r'^# (\d+)\.', me, flags=re.M)]
    check(sec_nums[:17] == list(range(1, 18)), 'M&E Sections 1-17 present in order')
    for ident in [f'CU-T{i}' for i in range(9,14)]:
        check(ident in me and ident in fd, f'{ident} present in both manuscripts')
    for ident in [f'CU-COM{i}' for i in range(1,20)]:
        check(ident in me or ident in fd, f'{ident} represented in canonical pair')
    for ident in ['CU-B4', 'CU-CL12', 'CU-AI27']:
        check(ident in me and ident in fd, f'{ident} included in complete proposal')

    stages_me = re.findall(r'^\*\*(\d+)\.\s+(.+?)\*\*', me, flags=re.M)
    check(len(stages_me) == 64, 'M&E contains exactly 64 bold numbered Mandala stages')
    if stages_me:
        check([int(n) for n,_ in stages_me] == list(range(1,65)), 'M&E Mandala stages run 1-64')
        check(stages_me[-1][1].startswith('Coherence Universalism'), 'M&E Stage 64 is Coherence Universalism')

    table_stages = re.findall(r'^\|\s*(\d+)\s*\|', fd, flags=re.M)
    stage_nums = [int(x) for x in table_stages if 1 <= int(x) <= 64]
    # The first complete 1-64 sequence in the document must be present.
    found_seq = any(stage_nums[i:i+64] == list(range(1,65)) for i in range(max(1, len(stage_nums)-63)))
    check(found_seq, 'Foundations contains complete 1-64 Mandala table')
    check('Stage 64 — Coherence Universalism' in fd, 'Foundations Stage 64 subsection present')

    for text, label in [(me,'M&E'),(fd,'Foundations')]:
        check(text.count('```') % 2 == 0, f'{label} code fences balanced')
        check(text.count('\\[') == text.count('\\]'), f'{label} display math brackets balanced')
        check('\x00' not in text and '\r' not in text, f'{label} has no NUL or CR characters')
        check(not re.search(r'\b(?:TODO|TBD|PLACEHOLDER)\b', text), f'{label} has no placeholder tokens')

    check('Shao Yong' in me and 'Shao Yong' in fd, 'Yi Jing book-specific traversal note present')
    check('hexagrams' not in me.lower().split('# 13.')[0], 'Yi Jing material does not enter pre-Mandala argument')
    check(not re.search(r'`[01]{6}`', me), 'Reader-facing M&E omits binary station labels')
    check('䷀' not in fd.split('# Part X')[0] and '䷁' not in fd.split('# Part X')[0], 'Yi Jing figures do not enter principle registry')
    check('not part of the canonical identity' in me or 'not part of the canonical identity' in fd,
          'Yi Jing non-authority boundary explicit')

    # Registry shape checks without assuming one historical schema.
    if isinstance(mandala, dict):
        stages = mandala.get('stages') or mandala.get('entries') or mandala.get('mandala')
    else:
        stages = mandala
    check(isinstance(stages, list) and len(stages) == 64, 'machine Mandala registry contains 64 entries')

    if isinstance(canon, dict):
        entries = canon.get('entries') or canon.get('principles') or canon.get('registry')
    else:
        entries = canon
    check(isinstance(entries, list) and len(entries) >= 220, 'canonical registry contains at least 220 entries')

summary = [
    'CU v0.10 Canonical Publication Pair PC5 QA',
    '=' * 47,
    f'pass_count: {len(passes)}',
    f'failure_count: {len(failures)}',
    '',
    'FAILURES',
    '--------',
]
summary += failures or ['None.']
summary += ['', 'PASSES', '------'] + [f'- {x}' for x in passes]
REPORT.write_text('\n'.join(summary) + '\n', encoding='utf-8')
print('\n'.join(summary[:8]))
if failures:
    raise SystemExit(1)
