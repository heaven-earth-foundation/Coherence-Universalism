"""
Reproducibility script for CU v0.10 Audit 03: Physics.

Run from the directory that contains the unpacked folder
  CU_v0.10_RC3_Methodological_Spine_Propagation_Working/
Requires numpy, scipy, sympy. Every [C] figure in the audit is printed
here under the check number (P1-P8) cited in the audit text.
"""
import glob, re
import numpy as np, sympy as sp
from scipy.optimize import minimize_scalar, brentq

RF = "CU_v0.10_RC3_Methodological_Spine_Propagation_Working/reader_facing/"
PH = open(glob.glob(RF + "03_*.md")[0], encoding="utf-8").read()
FD = open(glob.glob(RF + "02_*.md")[0], encoding="utf-8").read()
def hr(t): print("\n=== " + t)
rng = np.random.default_rng(0)
u = np.full(4, .25)
D = lambda p: ((p - .25) ** 2).sum()
S = lambda p: -(p[p > 0] * np.log(p[p > 0])).sum()
a = lambda p: 2 * (p - u)
def b(p): l = np.log(p); return -l + l.mean()
A = lambda p: 2 * p * (p - (p ** 2).sum())
B = lambda p: p * (-np.log(p) - S(p))
fip = lambda v, w, p: (v * w / p).sum()

hr("P1  Sandbox identities (§3.7 Jeffreys, §3.9 Euler step, §3.12-3.13.2 Fisher forms)")
err = 0
for _ in range(2000):
    p = rng.dirichlet(np.ones(4) * rng.uniform(.3, 3)); m = (p ** 2).sum(); lp = np.log(p)
    J = (p * np.log(4 * p)).sum() + (.25 * np.log(1 / (4 * p))).sum()
    err = max(err, abs(a(p) @ b(p) + 2 * J))
    err = max(err, abs(fip(A(p), A(p), p) - 4 * ((p ** 3).sum() - m * m)))
    err = max(err, abs(fip(B(p), B(p), p) - (p * (lp - (p * lp).sum()) ** 2).sum()))
    err = max(err, abs(fip(A(p), B(p), p) + 2 * (p * (p - m) * (lp + S(p))).sum()))
    al, be, h = rng.uniform(0, 2, 3); v = al * a(p) + be * b(p)
    err = max(err, abs(D(p + h * v) - D(p) - (h * (al * a(p) @ a(p) + be * (a(p) @ b(p))) + h * h * v @ v)))
print("max error:", err)
for p in [(.05, .25, .25, .45), (.1, .2, .2, .5), (.4, .3, .2, .1), (.7, .1, .1, .1)]:
    p = np.array(p); print("  D, S at", p, round(D(p), 4), round(S(p), 4))

hr("P2  Wedge collapse exactly on two-level states (abstract; §3.14.2)")
cos = lambda p: abs(a(p) @ b(p)) / np.linalg.norm(a(p)) / np.linalg.norm(b(p))
print("two-level:", [round(cos(np.array(p)), 12) for p in [(.4, .4, .1, .1), (.7, .1, .1, .1), (.3, .3, .3, .1)]],
      " three-level example:", round(cos(np.array([.4, .3, .2, .1])), 6))

hr("P3  Global Fisher-field bounds on the closed simplex (§3.13.2)")
def nA(p): p = p[p > 1e-15]; m = (p ** 2).sum(); return np.sqrt(4 * ((p ** 3).sum() - m * m))
def nB(p): p = p[p > 1e-15]; l = np.log(p); return np.sqrt((p * (l - (p * l).sum()) ** 2).sum())
def PiF(p): p = p[p > 1e-15]; l = np.log(p); m = (p ** 2).sum(); return 2 * (p * (p - m) * (l - (p * l).sum())).sum()
best = dict(A=0, B=0, Pi=0)
for _ in range(200000):
    k = rng.integers(2, 5); p = np.zeros(4); p[:k] = rng.dirichlet(np.ones(k) * rng.uniform(.2, 2))
    best["A"] = max(best["A"], nA(p)); best["B"] = max(best["B"], nB(p)); best["Pi"] = max(best["Pi"], PiF(p))
line = lambda g: (lambda x: -g(np.array([x] + [(1 - x) / 3] * 3)))
ref = {k: -minimize_scalar(line(g), bounds=(.25, .9999), method="bounded", options={"xatol": 1e-14}).fun
       for k, g in (("A", nA), ("B", nB), ("Pi", PiF))}
print("random search (incl. faces):", {k: round(v, 6) for k, v in best.items()})
print("(x,y,y,y) refinement:       ", {k: round(v, 12) for k, v in ref.items()})
print("paper: A 0.586724197682029  B 1.011677099862651  Pi 0.586672264109138")
x = (7 + np.sqrt(33)) / 16
print("sup|A|^2 =", nA(np.array([x] + [(1 - x) / 3] * 3)) ** 2, " 23/128+11*sqrt(33)/384 =", 23 / 128 + 11 * np.sqrt(33) / 384)
print("B root x:", brentq(lambda x: (2 * x - 1) * np.log(3 * x / (1 - x)) - 2, .3, .999))
print("Pi root x:", brentq(lambda x: (12 * x * x - 10 * x + 1) * np.log(3 * x / (1 - x)) - (4 * x - 1), .5, .99))

hr("P4  Feasibility bound |b_i| <= log(1/eps) on the band (§3.10)")
eps, worst = .02, 0
for _ in range(100000):
    p = eps + (1 - 4 * eps) * rng.dirichlet(np.ones(4) * rng.uniform(.1, 2)); worst = max(worst, np.abs(b(p)).max() / np.log(1 / eps))
print("max |b_i| / log(1/eps):", round(worst, 4))

hr("P5  Conservative accessibility flow (§4.11)")
def Dbar(p): qA, qB = p[0] + p[1], p[2] + p[3]; return .5 * ((qA - .5) ** 2 + (qB - .5) ** 2)
def gradF(f, p, e=1e-7):
    g = np.array([(f(p + e * v) - f(p - e * v)) / (2 * e) for v in np.eye(4)]); return p * (g - (p * g).sum())
p = np.random.default_rng(2).dirichlet(np.ones(4)); tr = []
for _ in range(4000):
    N, G = gradF(D, p), gradF(Dbar, p); PG = G - fip(G, N, p) / fip(N, N, p) * N
    p = p - 1e-3 * PG; tr.append((D(p), Dbar(p), D(p) - Dbar(p)))
t = np.array(tr)
print("D drift (Euler):", round(abs(t[-1, 0] - t[0, 0]), 6), " Dbar nonincreasing:", bool((np.diff(t[:, 1]) <= 1e-12).all()),
      " H nondecreasing:", bool((np.diff(t[:, 2]) >= -1e-12).all()))

hr("P6  Fisher term variation equals the quantum potential (§7.11), and the §6 two-qubit values")
x_ = sp.symbols("x"); r = sp.Function("rho")(x_); hb, m_ = sp.symbols("hbar m", positive=True)
L = hb ** 2 / (8 * m_) * sp.diff(r, x_) ** 2 / r
EL = sp.diff(L, r) - sp.diff(sp.diff(L, sp.diff(r, x_)), x_)
Q = -hb ** 2 / (2 * m_) * sp.diff(sp.sqrt(r), x_, 2) / sp.sqrt(r)
print("dI/drho - Q =", sp.simplify(EL - Q))
th = sp.symbols("theta"); c, s = sp.cos(th), sp.sin(th)
print("linear entropy - sin^2(2th)/2 =", sp.simplify(1 - (c ** 4 + s ** 4) - sp.sin(2 * th) ** 2 / 2))

hr("P7  Citations: parenthetical citations without entries; entries never mentioned")
i = PH.index("# References"); body, refs = PH[:i], PH[i:]
ra = set(re.findall(r"^([A-ZČ][A-Za-zčÀ-ž’'\-]+), ", refs, re.M))
names = set()
for par in re.findall(r"\(([A-ZČ][^()]*?\d{4}[a-z]?)\)", body):
    for part in par.split(";"):
        mm = re.match(r"\s*([A-ZČ][A-Za-zčÀ-ž’'\-]+)", part)
        if mm and re.search(r"\d{4}", part): names.add(mm.group(1))
print("cited without entry:", sorted(n for n in names if n not in ra))
print("entries never mentioned:", sorted(x for x in ra if x not in body and x != "Rader"))

hr("P8  Cross-paper: PHYS-A6 identifiers, Mandala labels, artifacts")
print("PHYS- identifiers in Physics:", len(re.findall("PHYS-", PH)),
      " defined in Foundations Part VI:", len(re.findall(r"^## PHYS-A6\.\d+", FD, re.M)))
print("Physics A.5 lists canonical stage titles:", "Domain-Relative Coherence Directions" in PH)
print("Physics §1.5 rung 3 label:", re.search(r"3\.&\\ \\text\{([^}]*)\}", PH).group(1))
print("Physics §1.5 rung 8 label:", re.search(r"8\.&\\ \\text\{([^}]*)\}", PH).group(1))
print("sentence-initial lowercase 'the Version 0.10':", len(re.findall(r"^the Version 0\.10", PH, re.M)))
