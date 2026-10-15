"""
Reproducibility script for CU v0.10 Audit 04: Biology.

Run from the directory that contains the unpacked folder
  CU_v0.10_RC3_Methodological_Spine_Propagation_Working/
Requires numpy. Every [C] figure in the audit is printed here under the
check number (B1-B10) cited in the audit text.
"""
import difflib, glob, itertools, re
import numpy as np

RF = "CU_v0.10_RC3_Methodological_Spine_Propagation_Working/reader_facing/"
def read(prefix): return open(glob.glob(RF + prefix + "_*.md")[0], encoding="utf-8").read()
BI, FD = read("04"), read("02")
CORPUS = {p.split("/")[-1][:2]: open(p, encoding="utf-8").read() for p in sorted(glob.glob(RF + "*.md"))}
def hr(t): print("\n=== " + t)
def line(t, i): return t[:i].count("\n") + 1

hr("B1  Recurrence dominance (§6.8): the two-state chain satisfies the inequality with no maintenance")
P = np.array([[.99, .01], [.10, .90]])
print("P(L|L) =", P[0, 0], " P(L|N) =", P[1, 0], " inequality holds:", P[0, 0] > P[1, 0])
pi = np.linalg.matrix_power(P, 2000)[0]
print("stationary distribution (L, N):", np.round(pi, 4))

hr("B2  Diffusive coupling can raise or lower viability (§3.16, D4, P5) -- reconstruction, not Supplement B")
def run(x0, floors, k, T=50.0, dt=.01):
    x = np.array(x0, float); viable = 0.0
    for _ in range(int(T / dt)):
        x = x + dt * k * (x.mean() - x); viable += dt * (x >= floors).all()
    return viable / T, x
cfgA = dict(x0=[0.2, 1.0, 1.0], floors=np.array([0.5, 0.5, 0.5]))   # threatened component below the mean
cfgB = dict(x0=[1.6, 0.7, 0.7], floors=np.array([1.2, 0.5, 0.5]))   # specialised high-floor component above the mean
for name, c in (("A (threatened low component)", cfgA), ("B (high-requirement component)", cfgB)):
    out = [(k, *run(c["x0"], c["floors"], k)) for k in (0.0, 0.1, 0.5, 2.0)]
    print(name, [(k, round(f, 3)) for k, f, _ in out])
print("mean is conserved by the law dx_i/dt = k(mean - x_i); the sign of the viability effect depends on floors and state")

hr("B3  Closure core (§3.9): strong connectivity already implies the in/out clause except for a singleton")
def sc(nodes, E):
    def reach(s, E2):
        seen, st = {s}, [s]
        while st:
            u = st.pop()
            for a, b in E2:
                if a == u and b not in seen: seen.add(b); st.append(b)
        return seen
    return all(reach(v, E) >= set(nodes) for v in nodes)
viol = 0; total = 0
for n in (2, 3, 4):
    nodes = list(range(n)); pairs = [(a, b) for a in nodes for b in nodes if a != b]
    for r in range(len(pairs) + 1):
        for E in itertools.combinations(pairs, r):
            if sc(nodes, E):
                total += 1
                ok = all(any(b == v for a, b in E) and any(a == v for a, b in E) for v in nodes)
                viol += not ok
print("strongly connected digraphs on 2-4 nodes:", total, " violating the in/out clause:", viol)

hr("B4  Aging formula (§10.7): 'not a superset' is satisfied by a kernel that mostly grows")
K_a = set(range(10)); K_later = (set(range(1, 30)))
print("|K(a)| =", len(K_a), " |K(a+da)| =", len(K_later), " K(a+da) not ⊇ K(a):", not K_later >= K_a,
      " contraction (⊊):", K_later < K_a)

hr("B5  Mandala stages: Biology §13.11 versus the Foundations stage table")
ft = {int(m.group(1)): m.group(2).strip() for m in re.finditer(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|", FD, re.M)
      if 1 <= int(m.group(1)) <= 64 and "Status" not in m.group(2)}
s = BI[BI.index("## 13.11"):BI.index("## 13.12")]
named = re.search(r"Stages 11–15: (.+?)\. ", s).group(1).replace(", and ", ", ").split(", ")
print([(11 + i, n, ft[11 + i], n == ft[11 + i]) for i, n in enumerate(named)])
print("stage 16 in Foundations:", ft[16])

hr("B6  Principle wording: section boxes vs Appendix A vs Foundations registry")
fd_reg = FD.index("## Biology\n")
for k, sec in (("CU-B1", "## 6.13"), ("CU-B2", "## 8.13"), ("CU-B3", "## 7.13"), ("CU-B4", "## 9.17"), ("CU-B5", "## 4.10")):
    blk = BI[BI.index(sec):]; blk = blk[:blk.index("\n\n", blk.index("> **" + k))]
    box = " ".join(l[2:] for l in blk.split("\n")[1:] if l.startswith(">")).replace("  ", " ").strip()
    box = box.split("**] ", 1)[-1].split("]** ", 1)[-1].strip()
    app = BI[BI.index("## A.", BI.index("# Appendix A")):]
    a_txt = re.search(r"> (.+)", app[app.index(k):]).group(1).strip()
    f_i = FD.index("### " + k, fd_reg); f_txt = FD[f_i:].split("\n\n")[2].strip()
    print(f"{k}: box==appendix {box == a_txt}  appendix==Foundations {a_txt == f_txt}")
    if box != a_txt:
        sm = difflib.SequenceMatcher(None, a_txt.split(), box.split())
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op != "equal": print(f"   appendix '{' '.join(a_txt.split()[i1:i2])}' -> box '{' '.join(box.split()[j1:j2])}'")
labels = re.findall(r"\*\*(CU-B\d) — [^*]+\*\* \*\*\[([^\]]+)\]\*\*", BI)
print("section labels:", labels)
print("Appendix A statuses:", re.findall(r"## A\.\d (CU-B\d)[^\n]*\n\n\*\*Status:\*\* ([^\n]+)", BI))
b4 = FD[FD.index("### CU-B4", fd_reg):FD.index("### CU-B5", fd_reg)]
print("Foundations CU-B4 authority class / status:", re.findall(r"\*\*(?:Authority class|Claim/candidate status):\*\* ([^\n]+?)\s*$", b4, re.M),
      " registry boundary wording:", re.findall(r"CU-B4 is canonical as ([^,;]+)", FD))

hr("B7  Identifier resolution and commitment titles")
ids = sorted(set(re.findall(r"\b(?:CU|PHYS)-[A-Za-zΨ]+-?[0-9]+(?:\.[0-9]+)?[a-z]?\b", BI)))
def defined(i):
    pat = re.compile(r"(^#+\s*[\d.]*\s*" + re.escape(i) + r"\b)|(^\*\*" + re.escape(i) + r"\b)|(^\|\s*" + re.escape(i) + r"\s*\|)", re.M)
    return any(pat.search(t) for t in CORPUS.values())
print(len(ids), "identifiers; unresolved:", [i for i in ids if not defined(i)])
fcom8 = re.search(r"CU-COM8 — Reverence.*?\*\*Commitment statement\.\*\* (.+?)\n", FD, re.S).group(1)
print("CU-COM8 statement identical to Foundations:", fcom8 in BI)
print("Foundations CU-COM8 cross-references:", re.search(r"interpretations CU-T5, CU-T6[^\n]*", FD).group(0))
print("Biology A.9 cites CU-T6:", "CU-T6" in BI)
print("§8.14 terms present in Consciousness (05):", {w: len(re.findall(w, CORPUS["05"], re.I)) for w in
      ("access organization", "perspectival anchoring", "center individuation")})
print("§13.12 dependency tables ('Source node' header) in Biology:", len(re.findall(r"^\|\s*Source node", BI, re.M)))
print("'description register' vs 'descriptive register':", BI.count("description register"), BI.count("descriptive register"))

hr("B8  Notation reuse (symbol -> distinct roles found)")
for sym, pats in {
    r"\mathcal U": [r"u\(\\cdot\)\\in\\mathcal U", r"\\rho\\in\\mathcal U", r"H_\{t\+1\}=\\mathcal U", r"\\mathcal U_k", r"\\mathcal U_s"],
    r"\mathcal D": [r"\\mathcal D\\\)? the disturbance|disturbance class \\\(\\mathcal D", r"\\mathcal D_\{h,e\}"],
    r"\mathcal A": [r"invariant set \\\(\\mathcal A", r"\\mathcal A_T"],
    r"\mathcal V": [r"\\mathcal V_T\(s\)", r"\\xrightarrow\{\\;\\mathcal V"],
    "A_P letters": [r"\\mathbf A_P"],
}.items():
    print(sym, [len(re.findall(p, BI)) for p in pats])
print("A_P profile reuses tuple letters B,E,K,R,H,V,X:", "B,\nE,\nK,\nR,\nH,\nV,\nX" in BI)
print("evidence grades E0-E4:", len(re.findall(r"\*\*E[0-4] — ", BI)), "  evolution predictions E1-E6:",
      len(re.findall(r"\*\*Prediction E[1-6]:", BI)))
print("individuality: 'at least six dimensions' stated:", "at least six dimensions" in BI,
      " ### 4.2.x subsections:", len(re.findall(r"^### 4\.2\.\d", BI, re.M)),
      " profile components:", len(re.search(r"\\mathbf I_B\s*=\s*\\bigl\((.*?)\\bigr\)", BI, re.S).group(1).split(",")))

hr("B9  Propagation and formatting artifacts")
for k, p in {"sentence-initial lowercase 'the Version 0.10'": r"(^|[.:]\s+)the Version 0\.10",
             "'$\\mid$' inside math": r"\$\\mid\$", "RC2 frozen-baseline line": r"RC2 remains the frozen baseline",
             "'from to' / 'between and'": r"\bfrom to\b|\bbetween and\b", "'Heaven–Earth' (en dash)": r"Heaven–Earth"}.items():
    print(f"{k}: {[line(BI, m.start()) for m in re.finditer(p, BI, re.M)]}")
print("'$\\mid$' anywhere else in the corpus:", {k: v.count("$\\mid$") for k, v in CORPUS.items() if k != "04" and v.count("$\\mid$")})
for sec in re.split(r"\n(?=# )", BI):
    a, b = sec.count("\\(") + sec.count("\\["), sec.count("$")
    if b: print("  dollar delimiters in:", sec.split("\n")[0][:50], b)
print("papers using $ delimiters at all:", [k for k, v in CORPUS.items() if "$" in v])
toc = re.findall(r"^\d+\. (.+?)\s*$", BI[BI.index("# Contents"):BI.index("# Principal")], re.M)
hd = re.findall(r"^# Section \d+\. (.+)$", BI, re.M)
print("Contents vs headings that differ beyond case:",
      [(i + 1, a, b) for i, (a, b) in enumerate(zip(toc, hd)) if a.lower() != b.lower()])
print("'Supplement B' references:", [line(BI, m.start()) for m in re.finditer("Supplement B", BI)])

hr("B10 Citations against the reference list")
i = BI.index("# References"); body_, refs = BI[:i], BI[i:]
ents = [(re.match(r"([^,(]+)", e).group(1).strip(), y) for e, y in re.findall(r"^([A-ZČ][^\n]*?)\((\d{4})\)", refs, re.M)]
print(len(ents), "entries")
print("entries whose first author is never named in the body:", [e for e in ents if e[0] not in body_ and e[0] != "Rader"])
srt = [e[0] for e in ents]
print("out of alphabetical order:", [(srt[j], srt[j + 1]) for j in range(len(srt) - 1)
                                     if srt[j].lower().replace("á", "a") > srt[j + 1].lower().replace("á", "a")])
