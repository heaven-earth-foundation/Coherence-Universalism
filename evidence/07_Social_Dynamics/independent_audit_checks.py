"""
Reproducibility script for CU v0.10 Audit 07: Social Dynamics.

Run from the directory that contains the unpacked folder
  CU_v0.10_RC3_Methodological_Spine_Propagation_Working/
Requires numpy. Every [C] figure in the audit is printed here under the
check number (Z1-Z9) cited in the audit text.
"""
import glob, re
import numpy as np

RF = "CU_v0.10_RC3_Methodological_Spine_Propagation_Working/reader_facing/"
CORPUS = {p.split("/")[-1][:2]: open(p, encoding="utf-8").read() for p in sorted(glob.glob(RF + "*.md"))}
SD, FD = CORPUS["07"], CORPUS["02"]
def hr(t): print("\n=== " + t)
def line(t, i): return t[:i].count("\n") + 1
def sec(t, a, b): return t[t.index(a):t.index(b, t.index(a) + 1)]

hr("Z1  §2.3 mean-versus-floor construction")
a, b, k = np.array([.90, .90, .20]), np.array([.65, .65, .65]), .40
print("mean a =", round(a.mean(), 4), " mean b =", round(b.mean(), 4), " min a < k:", a.min() < k, " min b >= k:", b.min() >= k)
appB = sec(SD, "# Appendix B", "# Appendix C")
print("'Appendix B gives the simple construction' in §2.3:", "Appendix B gives the simple construction" in SD,
      "| Appendix B contains the numbers:", "0.90" in appB)

hr("Z2  Profile coordinates and notation (§§2.1–2.2)")
prof = re.search(r"\\mathbf P_\{\\mathrm\{soc\}\}\s*=\s*\\langle(.*?)\\rangle", SD, re.S).group(1)
coords = [c.strip() for c in prof.replace("\n", "").split(",") if c.strip()]
print(len(coords), "coordinates:", coords, "| text says 'first nine' and 'final three':", "The first nine" in SD and "The final three" in SD)
tup = re.search(r"\\mathcal S\s*=\s*\((.*?)\)\.", sec(SD, "## 2.1 The model tuple", "## 2.2"), re.S).group(1).replace("\n", "")
tuple_syms = [s.strip() for s in tup.split(",")]
print("model tuple:", tuple_syms)
print("profile letters reusing tuple letters:", sorted({c for c in coords if c.split("_")[0] in tuple_syms}),
      "| plus A_d, R_p, X_c beside tuple A, R, X; P_soc beside tuple P")

hr("Z3  Nineteen governance rules: §2.9 versus Appendix A.5")
r1 = re.findall(r"^\d+\. (.+)$", sec(SD, "## 2.9 Nineteen", "# 3."), re.M)
r2 = re.findall(r"^\d+\. (.+)$", sec(SD, "## A.5 Nineteen", "# Appendix B"), re.M)
print(len(r1), len(r2), "rules; identical:", sum(x == y for x, y in zip(r1, r2)),
      "| differing:", [(i + 1, x, y) for i, (x, y) in enumerate(zip(r1, r2)) if x != y])

hr("Z4  Identifiers, statuses, and statements against Foundations")
ids = sorted(set(re.findall(r"\b(?:CU|PHYS)-[A-Za-zΨ]+-?[0-9]+(?:\.[0-9]+)?[a-z]?\b", SD)))
def defined(i):
    pat = re.compile(r"(^#+\s*[\d.]*\s*" + re.escape(i) + r"\b)|(^\*\*" + re.escape(i) + r"\b)|(^\|\s*" + re.escape(i) + r"\s*\|)", re.M)
    return any(pat.search(t) for t in CORPUS.values())
print(len(ids), "identifiers; unresolved:", [i for i in ids if not defined(i)])
def fblk(k):
    i = FD.index("### " + k + " —"); j = min(x for x in (FD.find("\n### ", i + 5), FD.find("\n## ", i + 5)) if x > 0); return FD[i:j]
appA = sec(SD, "## A.2 Primary", "## A.3")
for n in range(1, 6):
    k = f"CU-S{n}"; fb = fblk(k)
    ftxt = [q.strip() for q in fb.split("\n\n")[1:] if q.strip() and not q.startswith("**")][0]
    st = re.search(r"Claim/candidate status:\*\* ([^\n]+?)\s*$", fb, re.M).group(1)
    ac = re.search(r"Authority class:\*\* ([^\n]+?)\s*$", fb, re.M).group(1)
    lab = re.search(r"### " + k + r" — [^\n]+\n\n\*\*\[([^\]]+)\]\*\*", SD).group(1)
    print(f"{k}: Appendix A verbatim {ftxt in appA}; §14.4 verbatim {ftxt in sec(SD, '## 14.4', '## 14.5')}; "
          f"§14.4 label '{lab}' | Foundations: {ac} / {st}")
cl = [q.strip() for q in fblk("CU-CL12").split("\n\n")[1:] if q.strip() and not q.startswith("**")][0]
print("CU-CL12 statement verbatim in §13.11:", cl in SD)
for c in ("CU-COM11", "CU-COM18"):
    blk = FD[FD.index(c + " — "):]; blk = blk[:blk.index("\n## ")]
    s = re.search(r"\*\*Commitment statement\.\*\* (.+)", blk).group(1)
    norm = lambda x: re.sub(r"[\'“”\"]", "", x)
    print(f"{c} statement in Social Dynamics (quotation marks normalized): {norm(s) in norm(SD)}")

hr("Z5  CU-CL12 status wording")
print("Appendix B calls Open Myth 'provisional':", "Open Myth as a provisional" in SD)
print("Foundations CU-CL12 status:", re.search(r"Claim/candidate status:\*\* ([^\n]+?)\s*$", fblk("CU-CL12"), re.M).group(1))
print("Foundations CU-COM18 cross-reference:", re.search(r"CU-COM18 — Heaven.*?Cross-reference:\*\* ([^\n]+)", FD, re.S).group(1))
print("'attractor' in Social Dynamics:", [(line(SD, m.start()), SD[m.start() - 40:m.end() + 10].replace("\n", " ")) for m in re.finditer(r"attractor", SD)])

hr("Z6  Abstract's deterministic model in the body")
body = SD[SD.index("# 1. Social"):SD.index("# Appendix C")]
for w in ("delay sweep", "false alarm", "three different regimes", "polycentricity corrects"):
    print(f"{w!r}: abstract {w in SD[:SD.index('# 1. Social')]}, body {w in body}")

hr("Z7  Mandala cross-references")
ft = [(int(m.group(1)), m.group(2).strip()) for m in re.finditer(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|[^|]*\|\s*([^|]*)\|", FD, re.M)
      if 1 <= int(m.group(1)) <= 64 and re.search(r"CU-S\d|CU-CL|COM11|COM18", m.group(3))]
print("Foundations stages citing CU-S, CU-CL, COM11 or COM18:", ft)
print("'Stage N' references in Social Dynamics:", len(re.findall(r"\bStages? \d", SD)),
      "| in Biology, Consciousness, Psychology:", [len(re.findall(r"\bStages? \d", CORPUS[p])) for p in ("04", "05", "06")])

hr("Z8  Identifier formats and artifacts")
print("CU-CL forms used:", sorted(set(re.findall(r"CU-CL-?\d+", SD))), "(issue #8)")
print("sentence-initial lowercase 'this paper':", len(re.findall(r"(^|[.!?:]\s+)this paper", SD, re.M)),
      " RC2 line:", [line(SD, m.start()) for m in re.finditer("RC2 remains the frozen baseline", SD)])

hr("Z9  Citations against the reference list")
i = SD.index("# References"); bd, refs = SD[:i], SD[i:]
ents = [(re.match(r"([^,(.]+)", e).group(1).strip().split()[0], y) for e, y in re.findall(r"^([A-ZČ][^\n]*?)\((\d{4})[a-z]?[/)]", refs, re.M)]
print(len(ents), "entries;", sum(e[0] == "Rader" for e in ents), "Rader")
unc = sorted({e for e in ents if e[0] not in ("Rader", "International") and not re.search(re.escape(e[0]) + r"[^\n]{0,80}" + e[1], bd)})
print(len(unc), "entries never cited by author and year:", unc)
print("named without year in §12.3:", [n for n in ("Jaspers", "Eisenstadt", "Bellah") if n in bd])
print("ILO cited as 'ILO, 2024' against entry 'International Labour Organization':", "ILO, 2024" in bd)
print("entry 'Claude. (2026) … unpublished working note':", bool(re.search(r"^Claude\. \(2026\)", refs, re.M)), " cited in body:", bool(re.search(r"\bClaude\b", bd)))
names = [re.match(r"([^,(]+)", l).group(1) for l in refs.split("\n") if re.match(r"^[A-Z]", l)]
print("alphabetical breaks:", [(names[j], names[j + 1]) for j in range(len(names) - 1) if names[j].lower() > names[j + 1].lower()])
