"""
Reproducibility script for CU v0.10 Audit 06: Psychology.

Run from the directory that contains the unpacked folder
  CU_v0.10_RC3_Methodological_Spine_Propagation_Working/
Requires numpy. Every [C] figure in the audit is printed here under the
check number (Y1-Y9) cited in the audit text.
"""
import difflib, glob, re
import numpy as np

RF = "CU_v0.10_RC3_Methodological_Spine_Propagation_Working/reader_facing/"
CORPUS = {p.split("/")[-1][:2]: open(p, encoding="utf-8").read() for p in sorted(glob.glob(RF + "*.md"))}
PS, FD, CO = CORPUS["06"], CORPUS["02"], CORPUS["05"]
def hr(t): print("\n=== " + t)
def line(t, i): return t[:i].count("\n") + 1

hr("Y1  Horizon reversal: suppression vs supported engagement (abstract; Appendix C) -- reconstruction, not the supplement's model")
T = 20
supp = dict(comfort=lambda t: 0.8, function=lambda t: 0.6 - 0.02 * t)          # relief now, slow erosion of function
engage = dict(comfort=lambda t: 0.3 + 0.03 * t, function=lambda t: 0.5 + 0.02 * t)  # early cost, growing capacity
def score(s, H, wc, wf): return sum(wc * s["comfort"](t) + wf * s["function"](t) for t in range(H)) / H
for H, wc, wf, lab in ((2, .8, .2, "short horizon, comfort-weighted"), (T, .3, .7, "long horizon, function-weighted")):
    a, b = score(supp, H, wc, wf), score(engage, H, wc, wf)
    print(f"{lab:34s} suppression {a:.3f}  engagement {b:.3f}  -> {'suppression' if a > b else 'engagement'} preferred")

hr("Y2  Profile dominance and weighted reversal (§§2.4.1–2.4.2)")
p = np.array([.8, .4, .6, .7, .5, .6, .4, .7, .5]); q = np.array([.5, .7, .6, .5, .7, .5, .7, .5, .7])
print("p weakly dominates q:", bool((p >= q).all()), " q weakly dominates p:", bool((q >= p).all()))
w1 = np.array([3, 1, 1, 2, 1, 1, 1, 2, 1.]); w2 = np.array([1, 3, 1, 1, 3, 1, 3, 1, 2.])
print("S_w1(p), S_w1(q):", round(w1 @ p, 2), round(w1 @ q, 2), "  S_w2(p), S_w2(q):", round(w2 @ p, 2), round(w2 @ q, 2))

hr("Y3  Counting statements against the lists that follow them")
s = PS[PS.index("At least five forms should be distinguished"):]
blk = s[:s.index("\n\nA person can explicitly")]
print("§2.3 says 'at least five forms'; bullets listed:", len(re.findall(r"^- \*\*", blk, re.M)))
prof = re.search(r"\\mathbf P_\{\\Psi\}\s*=\s*\\langle(.*?)\\rangle", PS, re.S).group(1)
print("§2.4 profile coordinates:", len([x for x in prof.split(",") if x.strip()]), " Frame row 11 says nine:", "nine-coordinate profile" in PS)
print("Appendix C 'fifteen governance rules':", "fifteen governance rules" in PS,
      "| numbered prohibitions in §1.4:", len(re.findall(r"^\d\. \*\*No ", PS, re.M)))

hr("Y4  Identifiers and titles")
ids = sorted(set(re.findall(r"\b(?:CU|PHYS)-[A-Za-zΨ]+-?[0-9]+(?:\.[0-9]+)?[a-z]?\b", PS)))
def defined(i):
    pat = re.compile(r"(^#+\s*[\d.]*\s*" + re.escape(i) + r"\b)|(^\*\*" + re.escape(i) + r"\b)|(^\|\s*" + re.escape(i) + r"\s*\|)", re.M)
    return any(pat.search(t) for t in CORPUS.values())
print(len(ids), "identifiers; unresolved:", [i for i in ids if not defined(i)])
for n in range(1, 13):
    k = f"CU-Ψ{n}"
    ft = re.search(r"^### " + k + r" — (.+)$", FD, re.M).group(1); xt = re.search(r"^## " + k + r" — (.+)$", PS, re.M).group(1)
    if ft != xt: print(f"  title differs: {k}: Foundations '{ft}' vs Psychology '{xt}'")

hr("Y5  CU-Ψ1–Ψ12 statements and statuses: Psychology Appendix A versus the Foundations registry")
def xblk(k): i = PS.index("## " + k + " —"); return PS[i:PS.index("\n## ", i + 5)]
def fblk(k):
    i = FD.index("### " + k + " —"); j = min(x for x in (FD.find("\n### ", i + 5), FD.find("\n## ", i + 5)) if x > 0); return FD[i:j]
identical = 0
for n in range(1, 13):
    k = f"CU-Ψ{n}"; xb, fb = xblk(k), fblk(k)
    xs = re.search(r"\*\*Candidate status:\*\* ([^\n]+)", xb).group(1).rstrip(".")
    fs = re.search(r"Claim/candidate status:\*\* ([^\n]+?)\s*$", fb, re.M).group(1)
    xt = " ".join(q.strip() for q in xb.split("\n\n")[2:] if q.strip() and not q.startswith("**Principal"))
    ft = " ".join(q.strip() for q in fb.split("\n\n")[1:] if q.strip() and not q.startswith("**"))
    xt, ft = re.sub(r"\*\*|\\\[.*?\\\]", "", xt, flags=re.S).split(), ft.split()
    r = difflib.SequenceMatcher(None, ft, xt).ratio(); identical += r == 1
    fm_x = re.search(r"Principal failure mode:\*\* ([^\n]+)", xb).group(1); fm_f = re.search(r"Principal failure mode:\*\* ([^\n]+)", fb).group(1)
    if fm_x != fm_f: print(f"   failure mode {k}: Foundations '{fm_f}' | Psychology '{fm_x}'")
    print(f"{k:7s} status match {xs.lower().replace('-', '–') == fs.lower().replace('-', '–')}  "
          f"statement similarity {r:.2f}  failure mode identical {fm_x == fm_f}")
print("statements identical:", identical, "of 12")
f6 = fblk("CU-Ψ6"); x6 = xblk("CU-Ψ6")
print("Ψ6 'affected person' in Foundations:", "affected person" in f6, " in Psychology:", "affected person" in x6)
print("Ψ1 Foundations requires coordinates/dimensionality 'must be declared':", "must be declared" in fblk("CU-Ψ1"),
      " Psychology Ψ1:", "must be declared" in xblk("CU-Ψ1"))

hr("Y6  Stages 16–21 and CU-COM10")
ft = {int(m.group(1)): m.group(2).strip() for m in re.finditer(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|", FD, re.M) if 1 <= int(m.group(1)) <= 64}
named = re.search(r"Stages 16–21: (.+?)\. ", PS).group(1).replace(", and ", ", ").split(", ")
print([(16 + i, n == ft[16 + i]) for i, n in enumerate(named)])
blk = FD[FD.index("CU-COM10 — Healing"):]; blk = blk[:blk.index("\n## ")]
for lab in ("Commitment statement", "Boundary conditions", "Revision conditions"):
    s = re.search(r"\*\*" + lab + r"\.\*\* (.+)", blk).group(1); print(f"COM10 {lab} identical: {s in PS}")

hr("Y7  Cross-paper wording: the definition of ego")
print("Psychology §5.2:", re.search(r"Consciousness v0\.10 defines ego as ([^.]+)\.", PS).group(1))
print("Consciousness §2.3:", re.search(r"\*\*\[Definition\] Ego\*\* is ([^.]+)\.", CO).group(1))

hr("Y8  Propagation artifacts and supplement pointers")
print("sentence-initial lowercase 'this paper':", len(re.findall(r"(^|[.!?:]\s+|\|\s*)this paper", PS, re.M)),
      " 'RC2 remains the frozen baseline':", [line(PS, m.start()) for m in re.finditer("RC2 remains the frozen baseline", PS)])
print("illustrative/horizon-reversal model described in the body (outside abstract and Appendix C):",
      bool(re.search(r"suppression wins|horizon-reversal model", PS[PS.index("# 1."):PS.index("# Appendix C")])))
print("consecutive horizontal rules:", [line(PS, m.start()) for m in re.finditer(r"\n---\n\n---\n", PS)])

hr("Y9  Citations against the reference list")
i = PS.index("# References"); body, refs = PS[:i], PS[i:]
ents = [(re.match(r"([^,(.]+)", e).group(1).strip().split()[0], y) for e, y in re.findall(r"^([A-ZČ][^\n]*?)\((\d{4})\)", refs, re.M)]
print(len(ents), "entries")
print("entries never cited (author-year):", sorted({e for e in ents if e[0] not in ("Rader", "U.S.", "U") and not re.search(re.escape(e[0]) + r"[^\n]{0,80}" + e[1], body)}))
cited = set(re.findall(r"([A-Z][A-Za-zÀ-ž\-]+)(?: et al\.)?(?:,? (?:&|and) [A-Z][^,()]*?)?,? \(?(\d{4})[,;)]", body))
cited |= set(re.findall(r"([A-Z][A-Za-zÀ-ž\-]+)(?:, [A-Z][A-Za-zÀ-ž\-]+)*,? (?:&|and) [A-Z][A-Za-zÀ-ž\-]+,? (\d{4})", body))
keys = {(e[0], e[1]) for e in ents}
print("author-year citations whose name and year appear in no entry:", sorted(c for c in cited if 1900 < int(c[1]) < 2030
      and not re.search(re.escape(c[0]) + r"[^\n]*\(" + c[1], refs) and c[0] not in ("September", "In", "The", "A", "Version")))
print("entry 'U.S. Department of Veterans Affairs' cited as 'VA/DoD, 2023':", "VA/DoD, 2023" in body)
print("Salkovskis entry:", re.search(r"Salkovskis[^\n]{0,220}", refs).group(0)[:200])
