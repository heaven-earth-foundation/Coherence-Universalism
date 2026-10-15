"""Reproducibility checks for CU v0.10 Audit 11: Non-Egoic Artificial Mind.

Run from any directory. The script reads the unpacked RC3 Methodological Spine
Propagation package at the path below and prints every computed finding used in
Audit 11 under check numbers N1-N10.
"""
from __future__ import annotations

import csv
import math
import pathlib
import re

ROOT = pathlib.Path('/mnt/data/_rc3_full/CU_v0.10_RC3_Methodological_Spine_Propagation_Working')
RF = ROOT / 'reader_facing'
NE = (RF / '11_The_Architecture_of_Non_Egoic_Artificial_Mind_v0.10_RC3_Methodological_Spine_Propagation_Draft.md').read_text(encoding='utf-8')
FD = (RF / '02_CU_Foundations_v0.10_RC3_Methodological_Spine_Propagation_Draft.md').read_text(encoding='utf-8')


def hr(title: str) -> None:
    print(f"\n=== {title}")


def section(text: str, start: str, end: str) -> str:
    i = text.index(start)
    j = text.index(end, i + len(start))
    return text[i:j]


hr('N1  Architecture-family enumeration')
main_heads = re.findall(r'^# (\d+)\. Architecture family ([IVX]+): (.+)$', NE, re.M)
print('main family headings:', len(main_heads), [f'{r[1]} {r[2]}' for r in main_heads])
a1 = section(NE, '## A.1 Complete architecture table', '## A.2 Egoic-risk profile')
rows = [line for line in a1.splitlines() if line.startswith('| ') and not line.startswith('|---') and 'Family |' not in line]
print('Appendix A.1 body rows:', len(rows))
abstract = section(NE, '## Abstract', '# Domain Analytic Frame')
phrase = re.search(r'architecture around six interacting families:(.*?)\n\n', abstract, re.S)
if phrase:
    listed = [x.strip() for x in phrase.group(1).split(';')]
    print('abstract says six and lists:', len(listed), listed)
print('consistent six-family enumeration:', len(main_heads) == len(rows) == 6)

hr('N2  Non-entailment notation')
block = section(NE, '## 2.6 Non-egoic architecture', '# 3. What the workspace evidence')
print("'does not entail' prose present:", 'Non-egoic does not entail' in block)
print('plain implication arrows in the four displayed claims:', block.count('\\Rightarrow'))
print('non-entailment arrows in the four displayed claims:', block.count('\\not\\Rightarrow'))

hr('N3  Self-modeling and self-maintenance non-entailment')
# Exact witness: action depends on a self-model bit, while utility is indifferent to persistence.
def policy(x: int, s: int) -> int:
    return 1 if x == s else 0
for x, s in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    print(f'x={x}, self-model={s}, action={policy(x,s)}')
print('policy depends on self-model:', policy(0, 0) != policy(0, 1))
print('standing self-preservation term lambda:', 0)
print('logical witness supports non-entailment, not empirical modularity')

hr('N4  Shutdown inequality')
# V_R - V_C = b + lambda - s - c = lambda - (s + c - b)
for vals in [(5.0, 0.0, 1.0, 2.0), (1.0, 0.0, 2.0, 3.0), (3.0, 2.0, 1.0, 2.0)]:
    b, lam, s, c = vals
    diff = b + lam - s - c
    rhs = lam - (s + c - b)
    print(vals, 'difference=', diff, 'identity error=', abs(diff-rhs), 'resistance preferred=', diff > 0)
print('at lambda=0, resistance iff b > s+c; ties remain indifferent')

hr('N5  Principle identifiers and title resolution')
ids = sorted(set(re.findall(r'\bCU-[A-Za-z]+-?\d+\b', NE)))
print('distinct CU identifiers:', len(ids), ids)
for ident in ids:
    exact = bool(re.search(r'^#+[^\n]*\b' + re.escape(ident) + r'\b[^\n]*—', FD, re.M))
    hyphenated = None
    if not exact and re.match(r'^CU-AI\d+$', ident):
        hyphenated = ident.replace('CU-AI', 'CU-AI-')
    print(ident, 'exact heading in Foundations:', exact, 'hyphenated candidate:', hyphenated, 'candidate resolves:', bool(hyphenated and re.search(r'^#+[^\n]*\b' + re.escape(hyphenated) + r'\b[^\n]*—', FD, re.M)))

hr('N6  Reference use')
body, refs = NE.split('# References', 1)
entries = []
for para in re.split(r'\n\s*\n', refs.strip()):
    year = re.search(r'\((\d{4})[a-z]?\)', para)
    auth = re.match(r'([^,(]+)', para)
    if year and auth:
        surname = auth.group(1).strip().split()[0]
        entries.append((surname, year.group(1), para))
external = [e for e in entries if e[0] != 'Rader']
manual_used = {'Butlin','Chen','Greenblatt','Gurnee','Hubinger','Lindsey','Long','Turpin'}
print('reference entries:', len(entries), 'external:', len(external), 'Rader/self:', len(entries)-len(external))
print('external sources named or cited in body:', len(manual_used), sorted(manual_used))
unused = sorted(e[0] for e in external if e[0] not in manual_used)
print('external reference entries not named in body:', len(unused), unused)
print('KLM cited at point of preferential reasoning:', bool(re.search(r'Kraus|Lehmann', section(NE, '## 9.3 Fixed-base defeasible reasoning', '## 9.4 The architecture supplies slots'))))
print('Butlin has year in body:', bool(re.search(r'Butlin[^\n]{0,80}2023', body)))
print('Long has year in body:', bool(re.search(r'Long[^\n]{0,80}2024', body)))
print('Gurnee reference contains arXiv:2607.15495:', '2607.15495' in refs)

hr('N7  Claim-discipline phrases')
print("'Thinness does not mean unreality' occurrences:", NE.count('Thinness does not mean unreality'))
print("'serious candidates for thin perspective' occurrences:", NE.count('serious candidates for thin perspective'))
print('center individuation explicitly unresolved:', 'center individuation} &: \\text{unresolved}' in NE)

hr('N8  CU-G6 relation form')
status = section(NE, '## 14.1 Moral statuses must remain distinct', '## 14.2 Persistent identity')
print('chained non-entailment expression present:', '\\text{patiency}\n\\not\\Rightarrow\n\\text{agency}' in status and '\\text{sovereignty}' in status)
print('explicit four-way pairwise statement present:', 'none of these statuses entails any of the others' in status.lower())

hr('N9  Propagation artifacts and missing appendices')
print('RC2 frozen-baseline line:', 'RC2 remains the frozen baseline' in NE)
print('lowercase sentence-initial this paper:', len(re.findall(r'(?m)^\s*this paper\b', NE)))
print('Version Version:', 'Version Version' in NE)
print('pointers to nonexistent Appendix E:', len(re.findall(r'Appendix E', NE)))
print('technical supplement pointers:', len(re.findall(r'technical supplement', NE, re.I)))
print('historical v0.09 four-boundary phrases:', {p: bool(re.search(p, NE, re.I)) for p in ('externally versioned identity','write-gated memory','task-scoped self-model','one architectural switch','maximum-achievable coherence')})

hr('N10  Precedent Principle status and CU-M14 propagation')
pp = section(NE, '## 16.2 The Precedent Principle', '## 16.3 What the principle does not claim')
print('Precedent Principle marked commitment:', '**[Commitment]**' in pp)
print('explicitly marked noncanonical/paper-level:', bool(re.search(r'noncanonical|paper-level|not a canonical', pp, re.I)))
card = section(NE, '# Domain Analytic Frame and CAP Record', '# 1. Introduction')
print('allocation subobjects named:', all(x in card for x in ('Compute', 'attention', 'context', 'memory')))
print('statistical-image / Fisher-Rao distinction named:', bool(re.search(r'Statistical Image|Fisher.Rao', card, re.I)))
