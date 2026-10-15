"""
Reproducibility script for CU v0.10 Audit 09: Artificial Intelligence.

Run from the directory that contains the unpacked folder
  CU_v0.10_RC3_Methodological_Spine_Propagation_Working/
Requires sympy. Every [C] figure in the audit is printed here under the
check number (I1-I9) cited in the audit text.
"""
import glob, math, re
import sympy as sp

RF = "CU_v0.10_RC3_Methodological_Spine_Propagation_Working/reader_facing/"
CORPUS = {p.split("/")[-1][:2]: open(p, encoding="utf-8").read() for p in sorted(glob.glob(RF + "*.md"))}
AI, FD = CORPUS["09"], CORPUS["02"]
def hr(t): print("\n=== " + t)
def line(t, i): return t[:i].count("\n") + 1
def sec(t, a, b): return t[t.index(a):t.index(b, t.index(a) + 1)]
def fblk(k):
    i = FD.index("### " + k + " —"); j = min(x for x in (FD.find("\n### ", i + 5), FD.find("\n## ", i + 5)) if x > 0); return FD[i:j]

hr("I1  Shutdown inequality (§6.7)")
b, lam, s, c = sp.symbols("b lambda s c", real=True)
VR, VC = b + lam - s, c
print("V_R - V_C > 0  <=>  lambda > s + c - b :", sp.simplify((VR - VC) - (lam - (s + c - b))) == 0)
print("at lambda = 0: V_R - V_C =", sp.simplify((VR - VC).subs(lam, 0)), " (> 0 iff b > s + c)")
print("ties (V_R = V_C) are not assigned by 'exactly when'")

hr("I2  Two-stage reasoning (§12.14; issue #16)")
s1214 = sec(AI, "## 12.14", "## 12.15")
for w in ("threshold", "probab", "Or", "disjunction", "mixed"):
    print(f"{w!r} in §12.14:", bool(re.search(r"\b" + w, s1214)))
print("plain relation (Min ⊆ ⟦φ⟧, no nonemptiness clause):", "\\subseteq" in s1214 and "\\neq\\varnothing" not in s1214)
print("consequence symbol is '\\sim' rather than '|\\sim' (issue #30):", "\\sim_C" in s1214)
print("KLM and Lehmann–Magidor entries cited in body:", [n for n in ("Kraus", "Lehmann") if re.search(n + r"[^\n]{0,60}(1990|1992)", AI[:AI.index("# References")])])

hr("I3  Pointers to appendices that do not contain the cited material")
appB = sec(AI, "# Appendix B", "# Appendix C")
ptr = [(line(AI, m.start()), AI[max(0, m.start() - 70):m.end() + 50].replace("\n", " ")) for m in re.finditer(r"Appendix B", AI)
       if m.start() < AI.index("# Appendix B") and line(AI, m.start()) > 100]
for p in ptr: print("  ", p)
print("Appendix B is the revision list:", appB.split("\n")[0], "| contains any of the cited constructions:", bool(re.search(r"floor-hugging|three-group|weight vector|V_R|institution swap", appB)))
print("'Appendix E' referenced at:", [line(AI, m.start()) for m in re.finditer(r"Appendix E", AI)],
      "| appendices present:", re.findall(r"^# (Appendix [A-Z])", AI, re.M))
print("twenty-four rules in A.2:", len(re.findall(r"^\d+\. ", sec(AI, "## A.2", "## A.3"), re.M)))

hr("I4  CU-AI principles and commitments against Foundations")
ids = sorted(set(re.findall(r"\b(?:CU|PHYS)-[A-Za-zΨ]+-?[0-9]+(?:\.[0-9]+)?[a-z]?\b", AI)))
def defined(i):
    pat = re.compile(r"(^#+\s*[\d.]*\s*" + re.escape(i) + r"\b)|(^\*\*" + re.escape(i) + r"\b)|(^\|\s*" + re.escape(i) + r"\s*\|)", re.M)
    return any(pat.search(t) for t in CORPUS.values())
print(len(ids), "identifiers; unresolved:", [i for i in ids if not defined(i)])
appA = sec(AI, "## A.1 CU-AI", "## A.2"); same = 0
for n in range(1, 28):
    k = f"CU-AI-{n}" if n < 27 else "CU-AI27"
    ft = [q.strip() for q in fblk(k).split("\n\n")[1:] if q.strip() and not q.startswith("**")][0]
    xb = re.search(r"### " + re.escape(k) + r" — [^\n]+\n\n(.+?)\n\n", appA, re.S).group(1)
    same += xb == ft and fblk(k).split("\n")[0].split(" — ")[1] == re.search(r"### " + re.escape(k) + r" — ([^\n]+)", appA).group(1)
print("CU-AI-1..26 and CU-AI27: titles and statements identical:", same, "of 27")
print("§13.11 CU-AI27 box identical:", [q.strip() for q in fblk("CU-AI27").split("\n\n")[1:] if q.strip() and not q.startswith("**")][0] in sec(AI, "## 13.11", "# 14."))
blk = FD[FD.index("CU-COM13 — Sacred"):]; blk = blk[:blk.index("\n## ")]
for lab in ("Commitment statement", "Practical expression", "Boundary conditions", "Revision conditions"):
    t = re.search(r"\*\*" + lab + r"\.\*\* (.+)", blk).group(1); print(f"COM13 {lab} identical: {t in AI}")
print("identifier forms:", sorted(set(re.findall(r"CU-AI-?\d+", AI)), key=lambda x: int(re.sub(r"\D", "", x)))[-3:], "(issue #8)")

hr("I5  Mandala stages (§§13.11, 15.11)")
ft = {int(m.group(1)): m.group(2).strip() for m in re.finditer(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|", FD, re.M) if 1 <= int(m.group(1)) <= 64}
print("stage 59:", ft[59], "| matches §13.11:", ft[59] in AI)
print("stages 32-36:", [ft[i] for i in range(32, 37)])

hr("I6  Status wording for mythic–constitutional alignment")
for p in (r"provisional research program", r"Canonical (AI )?research and governance principle"):
    print(f"{p!r}:", [line(AI, m.start()) for m in re.finditer(p, AI)])

hr("I7  Propagation artifacts")
print("sentence/cell-initial lowercase 'this paper':", [line(AI, m.start()) for m in re.finditer(r"(^|[.!?:]\s+|\|\s*)this paper", AI, re.M)])
print("mid-sentence 'This paper':", [line(AI, m.start()) for m in re.finditer(r"[a-z,] This paper", AI)])
print("doubled word 'Consciousness Consciousness':", [line(AI, m.start()) for m in re.finditer("Consciousness Consciousness", AI)])
print("lines containing only a backslash:", [i + 1 for i, l in enumerate(AI.split("\n")) if l.strip() == "\\"])
print("RC2 line:", [line(AI, m.start()) for m in re.finditer("RC2 remains the frozen baseline", AI)])
print("cross-paper reliance on Social Dynamics model result (§2.7):", "A result from *Social Dynamics* carries directly into AI" in AI)

hr("I8  Citations")
i = AI.index("# References"); body, refs = AI[:i], AI[i:]
ents = [(re.match(r"([^,(.]+)", e).group(1).strip().split()[0], y) for e, y in re.findall(r"^([A-ZČ][^\n]*?)\((\d{4})[a-z]?[,/)]", refs, re.M)]
ns = [e for e in ents if e[0] != "Rader"]
unc = sorted({e for e in ns if not re.search(re.escape(e[0]) + r"[^\n]{0,90}" + e[1], body) and e[0] != "National"})
print(len(ns), "non-self entries;", len(unc), "never cited by author and year (NIST entries cited by acronym excluded):", unc)
print("Claude (2026) working note listed:", bool(re.search(r"^Claude\. \(2026\)", refs, re.M)), "| cited:", bool(re.search(r"\bClaude, 2026", body)))
print("Gurnee entry carries arXiv:2607.15495:", "2607.15495" in refs)

hr("I9  Appendix C's 92,378-case scalarization lattice")
print("C(19, 9) =", math.comb(19, 9), "= number of weight vectors on a 10-coordinate simplex at step 0.1;",
      "P_AI has", len(re.search(r"\\mathbf P_\{\\mathrm\{AI\}\}\s*=\s*\\langle(.*?)\\rangle", AI, re.S).group(1).split(",")), "coordinates")
