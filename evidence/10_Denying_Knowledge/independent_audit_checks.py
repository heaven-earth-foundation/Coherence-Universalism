"""
Reproducibility script for CU v0.10 Audit 10: Denying Knowledge to Make Room for Commitment.

Run from the directory that contains the unpacked folder
  CU_v0.10_RC3_Methodological_Spine_Propagation_Working/
Standard library only. Every [C] figure in the audit is printed here under
the check number (D1-D6) cited in the audit text.

The finite model used throughout is the one the paper's own regression
appears to use: three worlds, all 19 strict partial orders, every viability
base V, every premise extension G, and every conclusion extension phi
(19 x 8 x 8 x 8 = 9,728 cases).
"""
import glob, itertools, re

RF = "CU_v0.10_RC3_Methodological_Spine_Propagation_Working/reader_facing/"
DK = open(glob.glob(RF + "10_*.md")[0], encoding="utf-8").read()
def hr(t): print("\n=== " + t)

W = [0, 1, 2]
pairs = [(a, b) for a in W for b in W if a != b]
ORDERS = []
for r in range(len(pairs) + 1):
    for S in itertools.combinations(pairs, r):
        S = set(S)
        if any((b, a) in S for a, b in S): continue                       # asymmetric
        if any((a, c) not in S for a, b in S for b2, c in S if b == b2 and a != c): continue  # transitive
        ORDERS.append(S)
SUBS = [frozenset(s) for r in range(4) for s in itertools.combinations(W, r)]
def best(o, X): return {w for w in X if not any((v, w) in o for v in X)}

hr("D1  Regression counts (DK §3.4, §3.7)")
c = dict(cases=0, empty_best=0, strong=0, merely=0, merely_nonsingleton=0, excluded=0)
for o in ORDERS:
    for V in SUBS:
        for G in SUBS:
            X = V & G; B = best(o, X)
            for phi in SUBS:
                c["cases"] += 1
                if not X: c["empty_best"] += 1; continue
                if B <= phi: c["strong"] += 1
                elif B & phi: c["merely"] += 1; c["merely_nonsingleton"] += len(B) > 1
                else: c["excluded"] += 1
print("strict partial orders on three worlds:", len(ORDERS))
print(c)
print("paper reports 294 merely admissible, all non-singleton, and 4,104 empty-best cases")

hr("D2  System P rules: plain relation (A.1) versus strong warrant (§3.3)")
for strong in (False, True):
    fails = dict.fromkeys(["Refl", "RW", "And", "Or", "CM", "Cut"], 0)
    for o in ORDERS:
        for V in SUBS:
            def r(a, b):
                m = best(o, V & a)
                return (bool(m) if strong else True) and m <= b
            for a in SUBS:
                fails["Refl"] += not r(a, a)
                for b in SUBS:
                    for d in SUBS:
                        fails["RW"] += r(a, b) and b <= d and not r(a, d)
                        fails["And"] += r(a, b) and r(a, d) and not r(a, b & d)
                        fails["Or"] += r(a, d) and r(b, d) and not r(a | b, d)
                        fails["CM"] += r(a, b) and r(a, d) and not r(a & b, d)
                        fails["Cut"] += r(a & b, d) and r(a, b) and not r(a, d)
    print("strong warrant (nonemptiness clause):" if strong else "plain relation (A.1):", fails)
print("infeasible (order, V, alpha) triples = 19 x 27 =", 19 * 27)

hr("D3  Admissibility fails And (§3.4 construction)")
B = {"w1", "w2"}; phi = {"w1"}; psi = {"w2"}
print("phi admissible:", bool(B & phi), " psi admissible:", bool(B & psi), " phi&psi admissible:", bool(B & phi & psi))

hr("D4  In-text author mentions versus the reference list")
body = DK[:DK.index("# References")]
refs = DK[DK.index("# References"):]
authors = sorted(set(re.findall(r"^([A-Z][a-zA-Z]+),", refs, re.M)))
print({a: len(re.findall(r"\b" + a + r"\b", body)) for a in authors})
print("Schroeder citations in body:", re.findall(r"Schroeder, 2008[ab]?", body),
      " reference entries:", re.findall(r"Schroeder, M\. \(2008[ab]?\)", refs))

hr("D5  Notation and propagation artifacts")
print("Real_R uses:", DK.count("operatorname{Real}_R"), " Mod_R uses:", DK.count("operatorname{Mod}_R"))
print("sentence-initial lowercase 'the Version 0.10':", len(re.findall(r"\. the Version 0\.10", DK)))
print("garbled sentence shared with M&E §6.4:",
      "can therefore be unwarranted even where the descriptive truth of its content does not settle" in DK)

hr("D6  Identifiers cited")
print(sorted(set(re.findall(r"CU-[A-Z]+-?[0-9]+", DK))))
