"""
Reproducibility script for CU v0.10 Audit 05: Consciousness.

Run from the directory that contains the unpacked folder
  CU_v0.10_RC3_Methodological_Spine_Propagation_Working/
Requires numpy and scipy. Every [C] figure in the audit is printed here under
the check number (Q1-Q10) cited in the audit text.
"""
import glob, itertools, re
import numpy as np
from scipy.integrate import solve_ivp

RF = "CU_v0.10_RC3_Methodological_Spine_Propagation_Working/reader_facing/"
CORPUS = {p.split("/")[-1][:2]: open(p, encoding="utf-8").read() for p in sorted(glob.glob(RF + "*.md"))}
CO, FD = CORPUS["05"], CORPUS["02"]
def hr(t): print("\n=== " + t)
def line(t, i): return t[:i].count("\n") + 1

hr("Q1  Second-order dynamics equal a first-order system on the expanded state (§5.4)")
G, V = 0.3, lambda q: np.array([q[0] ** 3 - q[0]])            # dV/dq for V = q^4/4 - q^2/2
def first(t, y): q, v = y[:1], y[1:]; return np.concatenate([v, -G * v - V(q)])
sol = solve_ivp(first, (0, 20), [1.5, 0.0], rtol=1e-11, atol=1e-12, dense_output=True)
t = np.linspace(0, 20, 2001); q = sol.sol(t)[0]
qdd = np.gradient(np.gradient(q, t), t); qd = np.gradient(q, t)
res = qdd + G * qd + (q ** 3 - q)
print("max residual of q'' + Γq' + V'(q) along the first-order solution (finite differences, interior):",
      f"{np.abs(res[5:-5]).max():.2e}")

hr("Q2  A weighted score can reverse the ranking of two profiles (§3.13)")
# coordinates: G, S, C, M, I, tau, W_c, V, P, R  (each normalized to [0,1] for illustration)
access_rich = np.array([.9, .8, .9, .7, .4, .3, .2, .1, .1, .5])
embodied    = np.array([.6, .6, .6, .4, .6, .8, .9, .8, .9, .3])
w1 = np.array([3, 2, 3, 2, 1, 1, 1, 1, 1, 1.]); w2 = np.array([1, 1, 1, 1, 1, 2, 2, 3, 3, 1.])
for w in (w1, w2):
    print("weights", w.astype(int), " access-rich", round(w @ access_rich, 2), " embodied", round(w @ embodied, 2))
print("Pareto: neither profile dominates:", not (access_rich >= embodied).all() and not (embodied >= access_rich).all())

hr("Q3  A causal-attention transformer, unrolled over (layer, position), has no multi-node SCC (§7.11)")
Lyr, Pos = 6, 5
nodes = [(l, p) for l in range(Lyr) for p in range(Pos)]
E = {(a, b) for a in nodes for b in nodes if b[0] == a[0] + 1 and b[1] >= a[1]}   # residual + causal attention
idx = {n: i for i, n in enumerate(nodes)}
A = np.zeros((len(nodes),) * 2, bool)
for a, b in E: A[idx[a], idx[b]] = True
R = A.copy()
for k in range(len(nodes)): R |= R[:, [k]] & R[[k], :]
print("pairs mutually reachable:", int((R & R.T).sum()), " -> every strongly connected component is a single node")

hr("Q4  Identifiers, titles, and principle statements against Foundations")
ids = sorted(set(re.findall(r"\b(?:CU|PHYS)-[A-Za-zΨ]+-?[0-9]+(?:\.[0-9]+)?[a-z]?\b", CO)))
def defined(i):
    pat = re.compile(r"(^#+\s*[\d.]*\s*" + re.escape(i) + r"\b)|(^\*\*" + re.escape(i) + r"\b)|(^\|\s*" + re.escape(i) + r"\s*\|)", re.M)
    return any(pat.search(t) for t in CORPUS.values())
print(len(ids), "identifiers; unresolved:", [i for i in ids if not defined(i)])
rows = {m.group(1): (m.group(2).strip(), m.group(3).strip(), m.group(4).strip())
        for m in re.finditer(r"^\| (CU-[CV]\d) \| ([^|]+) \| ([^|]*) \| ([^|]+) \|$", CO, re.M)}
same_title = same_text = 0; statuses = {}
for k, (title, status, text) in rows.items():
    i = FD.index("### " + k); blk = FD[i:i + 3000].split("\n### ")[0].split("\n## ")[0]
    same_title += blk.split("\n")[0].endswith(title)
    paras = [p.strip() for p in blk.split("\n\n")[2:] if p.strip() and not p.startswith("**")]
    same_text += paras[0] == text
    statuses[k] = re.search(r"Claim/candidate status:\*\* ([^\n]+?)\s*$", blk, re.M).group(1)
print(f"Appendix A rows: {len(rows)}; titles identical {same_title}; statements identical {same_text}")
print("Appendix A status cells that are empty:", sum(1 for v in rows.values() if not v[1]), "of", len(rows))
print("Foundations claim statuses:", statuses)
v7 = FD[FD.index("### CU-V7"):FD.index("### CU-V7") + 800]
print("Foundations CU-V7 authority class:", re.search(r"Authority class:\*\* ([^\n]+?)\s*$", v7, re.M).group(1),
      "| disposition:", re.search(r"Disposition:\*\* ([^\n]+)", v7).group(1))
print("Consciousness says CU-V7 is superseded/alias:", bool(re.search(r"CU-V7[^\n]{0,120}(alias|supersed)", CO)))

hr("Q5  Mandala stages named in Appendix A versus Foundations")
ft = {int(m.group(1)): m.group(2).strip() for m in re.finditer(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|", FD, re.M) if 1 <= int(m.group(1)) <= 64}
named = re.search(r"Stages 16–21—(.+?)—while", CO).group(1).replace(", and ", ", ").split(", ")
print([(16 + i, n == ft[16 + i]) for i, n in enumerate(named)])

hr("Q6  CU-COM9 against Foundations §9.11")
blk = FD[FD.index("CU-COM9 — Sacred"):]; blk = blk[:blk.index("\n## ")]
for lab in ("Commitment statement", "Boundary conditions", "Revision conditions"):
    s = re.search(r"\*\*" + lab + r"\.\*\* (.+)", blk).group(1)
    print(f"{lab} identical: {s in CO}")
print("Foundations cross-references:", re.search(r"Cross-reference:\*\* ([^\n]+)", blk).group(1))
print("Consciousness Appendix A cross-reference names:", sorted(set(re.findall(r"CU-[TG]\d+", CO[CO.index("## Commitment-register cross-reference"):]))))

hr("Q7  Propagation artifacts")
print("sentence- or cell-initial lowercase 'this paper':", len(re.findall(r"(^|[.!?:]\s+|\|\s*|\*\*\s*)this paper", CO, re.M)),
      " all lowercase 'this paper':", len(re.findall(r"\bthis paper\b", CO)))
print("ungrammatical substitutions:", [(line(CO, m.start()), m.group(0)) for m in re.finditer(r"central this paper distinction|this paper assessment", CO)])
print("lowercase defined term:", [(line(CO, m.start()), m.group(0)) for m in re.finditer(r"\*\*\[Definition\] [a-z][^*]*\*\*", CO)])
print("'RC2 remains the frozen baseline':", [line(CO, m.start()) for m in re.finditer("RC2 remains the frozen baseline", CO)])
ab = CO[CO.index("# Abstract"):CO.index("## Relation to the series")]
print("abstract paragraph after the closing rule:", ab.split("\n---\n")[1].strip()[:70] + "…")
print("corpus counts of sentence-initial lowercase 'this paper':",
      {k: len(re.findall(r"(^|[.!?:]\s+|\|\s*)this paper", v, re.M)) for k, v in CORPUS.items()})

hr("Q8  Internal cross-references and threshold language")
for p in (r"Appendix B gives an explicit construction", r"PIH threshold", r"thin threshold", r"does not define a numerical threshold",
          r"dual_disconnected_workspaces", r"several independence results"):
    print(f"{p!r}: lines {[line(CO, m.start()) for m in re.finditer(p, CO)]}")
appB = CO[CO.index("# Appendix B"):CO.index("# Appendix C")]
print("Appendix B contains a construction or weights:", bool(re.search(r"weight|construction|\\\[", appB)))

hr("Q9  Notation reuse")
for name, pat in {"P as probability": r"\\?P\(", "P as persistence coordinate": r"- \\\(P\\\): persistence",
                  "G as causal graph G_t": r"G_t=\(N_t,E_t\)", "G as profile coordinate": r"- \\\(G\\\): global availability",
                  "G as relational organization": r"C_\{\\mathrm\{con\}\}\(x;K,G",
                  "calligraphic R as reflexive process": r"\\mathcal R_t\(m_t", "calligraphic R as reach sets": r"\\mathcal R_i=",
                  "E as environment": r"- \\\(E\\\) is the coupled environment", "E_t as graph edges": r"E_t\)"}.items():
    print(f"{name}: {len(re.findall(pat, CO))}")

hr("Q10 Citations against the reference list")
i = CO.index("# References"); body, refs = CO[:i], CO[i:]
ents = [(re.match(r"([^,(]+)", e).group(1).strip().split()[0], y) for e, y in re.findall(r"^([A-ZČ][^\n]*?)\((\d{4})[a-z]?[,)]", refs, re.M)]
print(len(ents), "entries;", sum(e[0] == "Rader" for e in ents), "are Rader")
print("entries with no author-year mention in the body:",
      sorted({e for e in ents if e[0] != "Rader" and not re.search(re.escape(e[0]) + r"[^\n]{0,60}" + e[1], body)}))
print("Rader year suffixes:", re.findall(r"Rader, G\. K\. D\. \((2026[a-z]?)\)", refs))
print("Gurnee entry carries arXiv:2607.15495:", "2607.15495" in refs)
print("COGITATE named in body without author-year citation:", [line(CO, m.start()) for m in re.finditer(r"COGITATE", body)],
      " 'Cogitate Consortium' in body:", "Cogitate Consortium" in body)

hr("Q11 §10's description of the companion paper against the v0.10 Non-Egoic paper (11)")
NE = CORPUS["11"]
for p in ("externally versioned identity", "write-gated memory", "task-scoped self-model", "externally imposed norms",
          "one architectural switch", "maximum-achievable coherence", "bodhisattva construction"):
    print(f"{p!r}: in Consciousness {len(re.findall(p, CO, re.I))}, in Non-Egoic {len(re.findall(p, NE, re.I))}")
print("Non-Egoic architecture families:", re.findall(r"^# \d+\. (Architecture family [IVX]+: [^\n]+)", NE, re.M))
