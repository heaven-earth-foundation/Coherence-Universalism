"""
Reproducibility script for CU v0.10 Audit 01: Metaphysics and Epistemology.

Run from the directory that contains the unpacked folder
  CU_v0.10_RC3_Methodological_Spine_Propagation_Working/
Requires only the Python standard library and numpy.

Every figure labelled [C] in the audit is printed by this script, under the
check number (E1-E12) cited in the audit text.
"""
import collections, glob, itertools, random, re
import numpy as np

RF = "CU_v0.10_RC3_Methodological_Spine_Propagation_Working/reader_facing/"
def read(prefix): return open(glob.glob(RF + prefix + "_*.md")[0], encoding="utf-8").read()
ME, FD, PH, DK = read("01"), read("02"), read("03"), read("10")
CORPUS = {p.split("/")[-1][:2]: open(p, encoding="utf-8").read() for p in sorted(glob.glob(RF + "*.md"))}
def hr(t): print("\n=== " + t)

# ---------------------------------------------------------------- formal checks
hr("E1  Two-stage Or counterexample (M&E §10.4) with certainty feasibility")
POL = {"piA": ({"a1": 1.0}, 10), "piB": ({"b1": 1.0}, 10), "piM": ({"a2": .5, "b2": .5}, 1)}
A, B, G = {"a1", "a2"}, {"b1", "b2"}, {"a1", "b1"}          # G is the conclusion gamma
supp = lambda p: {w for w, x in p.items() if x > 0}
def Pi(ev, delta=0.0):
    return {k for k, (p, r) in POL.items() if sum(p.get(w, 0) for w in ev) >= 1 - delta - 1e-12}
def f(ev):
    F = Pi(ev)
    if not F: return set()
    m = min(POL[k][1] for k in F); return {k for k in F if POL[k][1] == m}
def cons(ev, concl):                                       # typicality = support inside the event
    return all(supp(POL[k][0]) & ev <= concl for k in f(ev))
print("f(A), f(B), f(AvB):", f(A), f(B), f(A | B))
print("A=>g:", cons(A, G), " B=>g:", cons(B, G), " AvB=>g:", cons(A | B, G))

hr("E2  Support feasibility (M&E §10.7): conjunction identity restored, disjunction not")
W4 = ["a1", "a2", "b1", "b2"]
ev = [set(s) for r in range(5) for s in itertools.combinations(W4, r)]
print("Pi(A v B) == Pi(A) | Pi(B):", Pi(A | B) == Pi(A) | Pi(B), " Pi(A v B) =", sorted(Pi(A | B)))
print("Pi(X & Y) == Pi(X) & Pi(Y) for all events:", all(Pi(x & y) == Pi(x) & Pi(y) for x in ev for y in ev))

hr("E3  Verdict facts (M&E §8.3-8.4), exhaustive over 5 worlds")
U = set(range(5)); subs = [set(s) for r in range(6) for s in itertools.combinations(U, r)]
eq = part = single = True
for Bst in subs:
    if not Bst: continue
    for phi in subs:
        eq &= (not (Bst & phi)) == (Bst <= U - phi)
        v = [Bst <= phi, bool(Bst & phi) and not Bst <= phi, not (Bst & phi)]
        part &= sum(v) == 1
        if len(Bst) == 1: single &= not v[1]
print("exclusion == strong warrant for not-phi:", eq)
print("strong / merely admissible / excluded partition nonempty best sets:", part)
print("no mere admissibility with a singleton best set:", single)

hr("E4  Maximum preservation == admissibility (M&E §8.5)")
random.seed(0); ok = True
for _ in range(20000):
    c = {w: random.randint(0, 3) for w in range(6)}; phi = {w for w in c if random.random() < .5}
    if not phi: continue
    M = max(c.values()); ok &= (max(c[w] for w in phi) == M) == bool({w for w in c if c[w] == M} & phi)
print(ok)

hr("E5  Countermodel B.13 (premise-responsive base defeats Cautious Monotony)")
lab = {"w1": {"b", "g"}, "w2": {"g"}, "w3": {"b"}}; prec = {("w1", "w2"), ("w3", "w2")}
mn = lambda S: {x for x in S if not any((y, x) in prec for y in S)}
b0 = mn({"w1", "w2"}); b1 = mn({w for w in {"w3"} if "b" in lab[w]})
print("best at empty premises:", b0, " best after adding b:", b1,
      " CM fails:", all({"b", "g"} <= lab[w] for w in b0) and not all("g" in lab[w] for w in b1))

hr("E6  Block averaging (M&E §3.7): D falls by within-block squares, H rises by KL; unequal")
rng = np.random.default_rng(1)
for _ in range(3):
    p = rng.dirichlet(np.ones(4)); q = p.copy()
    for blk in ([0, 1], [2, 3]): q[blk] = p[blk].mean()
    D = lambda x: ((x - .25) ** 2).sum(); H = lambda x: -(x * np.log(x)).sum()
    print(f"dD={D(p)-D(q):.6f}  sum sq={sum(((p[b]-p[b].mean())**2).sum() for b in ([0,1],[2,3])):.6f}"
          f"  dH={H(q)-H(p):.6f}  KL={(p*np.log(p/q)).sum():.6f}")

# ---------------------------------------------------------------- corpus checks
hr("E7  Mandala stages: M&E §13.14 versus the Foundations stage table")
stages, cur = {}, None
sec = ME[ME.index("## 13.14"):ME.index("## 13.15")]
for l in sec.split("\n"):
    m = re.match(r"\*\*(\d+)\. (.+?)\*\*", l)
    if m: cur = int(m.group(1)); stages[cur] = {"title": m.group(2)}
    m = re.match(r"\*(Status|Related):\*\s*(.*?)\s*$", l)
    if m and cur: stages[cur][m.group(1)] = m.group(2).rstrip(".")
ft = {int(m.group(1)): m.groups()[1:] for m in
      re.finditer(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|$", FD, re.M)
      if 1 <= int(m.group(1)) <= 64}
t = sum(stages[i]["title"] == ft[i][0] for i in range(1, 65))
s = sum(stages[i]["Status"] == ft[i][1] for i in range(1, 65))
rel = [i for i in range(1, 65) if stages[i]["Related"].replace(" ", "") != ft[i][2].replace(" ", "").rstrip(".")]
print(f"titles identical: {t}/64  statuses identical: {s}/64  related lists differ at stages: {rel}")
labels = collections.Counter(v["Status"] for v in stages.values())
print("distinct status labels across 64 stages:", len(labels))

hr("E8  Identifier resolution: every CU-/PHYS- identifier cited in M&E")
ids = set(re.findall(r"\b(?:CU|PHYS)-[A-Za-zΨ]+-?[0-9]+(?:\.[0-9]+)?[a-z]?\b", ME))
def defined(i):
    pat = re.compile(r"(^#+\s*[\d.]*\s*" + re.escape(i) + r"\b)|(^\*\*" + re.escape(i) + r"\b)|(^\|\s*" + re.escape(i) + r"\s*\|)", re.M)
    return any(pat.search(t) for t in CORPUS.values())
und = sorted(i for i in ids if not defined(i))
print(len(ids), "distinct identifiers; unresolved:", und)
print("PHYS- identifiers anywhere in Physics:", len(re.findall(r"PHYS-", PH)))
reg = dict(re.findall(r"^## (PHYS-A6\.\d+) — (.+)$", FD, re.M))
print("PHYS-A6 items defined in Foundations (Part VI, Physics Constraint Registry):", len(reg))
for i in range(1, 11):
    cited = re.findall(r"PHYS-A6\.\d+", stages[i]["Related"])
    print(f"  stage {i:2d} {stages[i]['title'][:40]:40s} -> " +
          "; ".join(f"{c} '{reg.get(c, '?')}'" for c in cited))

hr("E9  §13.12 dependency tables (header 'Source node') per paper")
print({k: len(re.findall(r"^\|\s*Source node", v, re.M)) for k, v in CORPUS.items()})

hr("E10 Double-escaped LaTeX ('\\\\text') per paper")
print({k: v.count("\\\\text") for k, v in CORPUS.items() if v.count("\\\\text")})

hr("E11 Revision and propagation artifacts in M&E")
for pat in [r"Version Version", r"navigation from to", r"^## Version 0\.10 ", r"\b[01]{6}\b"]:
    print(f"{pat!r}: {len(re.findall(pat, ME, re.M))}")

hr("E12 Overlap with Denying Knowledge (shared 8-grams) and section word counts")
def secs(t):
    out, cur = {}, None
    for l in t.split("\n"):
        m = re.match(r"^# (\d+)\. ", l)
        if m: cur = int(m.group(1)); out[cur] = []; continue
        if l.startswith("# "): cur = None
        if cur: out[cur].append(l)
    return {k: " ".join(v) for k, v in out.items()}
def grams(s): w = re.findall(r"[a-z]+", s.lower()); return {tuple(w[i:i+8]) for i in range(len(w)-7)}, len(w)
dk = set().union(*[grams(v)[0] for v in secs(DK).values()])
for k, v in secs(ME).items():
    g, n = grams(v); print(f"§{k:2d}  words {n:5d}  shared 8-grams {len(g & dk)/max(1,len(g)):4.0%}")
s13 = ME[ME.index("## 13.14"):ME.index("## 13.15")]
print("words in §13.14:", len(s13.split()))
