"""
Reproducibility script for CU v0.10 Audit 08: Ethics.

Run from the directory that contains the unpacked folder
  CU_v0.10_RC3_Methodological_Spine_Propagation_Working/
Requires numpy. Every [C] figure in the audit is printed here under the
check number (T1-T9) cited in the audit text.
"""
import difflib, glob, re
import numpy as np

RF = "CU_v0.10_RC3_Methodological_Spine_Propagation_Working/reader_facing/"
CORPUS = {p.split("/")[-1][:2]: open(p, encoding="utf-8").read() for p in sorted(glob.glob(RF + "*.md"))}
ET, FD, PS = CORPUS["08"], CORPUS["02"], CORPUS["06"]
def hr(t): print("\n=== " + t)
def line(t, i): return t[:i].count("\n") + 1
def sec(t, a, b): return t[t.index(a):t.index(b, t.index(a) + 1)]
def fblk(k):
    i = FD.index("### " + k + " —"); j = min(x for x in (FD.find("\n### ", i + 5), FD.find("\n## ", i + 5)) if x > 0); return FD[i:j]
def ftext(k): return [q.strip() for q in fblk(k).split("\n\n")[1:] if q.strip() and not q.startswith("**")][0]

hr("T1  Aggregate versus floor (§8.3) and weighted reversal (§2.6)")
yu, yv, k = np.array([.95, .95, .30]), np.array([.70, .70, .70]), np.array([.40, .40, .40])
print("sum u > sum v:", yu.sum() > yv.sum(), "| some a with y_a(u) < k_a:", bool((yu < k).any()), "| all y_a(v) >= k_a:", bool((yv >= k).all()))
print("§8.3 writes the floor condition as 'min_a y_a(u) < k_a' (k indexed by the bound variable):",
      "\\min_a y_a(u) < k_a" in ET.replace(" ", "").replace("\\min_ay_a(u)<k_a", "\\min_a y_a(u) < k_a"))
z = {"u": np.array([.9, .3, .8]), "v": np.array([.5, .8, .5])}
for w in (np.array([.6, .2, .2]), np.array([.2, .6, .2])):
    print("weights", w, {o: round(float(w @ s), 2) for o, s in z.items()})

hr("T2  Floor notation in §2.4")
s = sec(ET, "## 2.4 Protected floors", "### 2.4.1")
print("introduces k_j:", "Let \\(k_j\\) be a protected floor for dimension \\(j\\)" in s, "| formula uses k_{aj}:", "k_{aj}" in s)

hr("T3  Notation reuse")
prof = re.search(r"\\mathbf P_E\(u\)\s*=\s*\\langle(.*?)\\rangle", ET, re.S).group(1).replace("\n", "")
print("ethical profile:", [c.strip() for c in prof.split(",")])
print("tuple:", re.search(r"\\mathcal E\s*=\s*\((.*?)\)\.", sec(ET, "## 2.1 The ethical model tuple", "## 2.2"), re.S).group(1).replace("\n", ""))
print("bold R_a(o) responsibility profile defined:", "\\mathbf R_a(o)" in ET, "| R_a also a P_E coordinate:", "- \\(R_a\\): alignment of responsibility" in ET)
print("Tr in repair profile P_R:", bool(re.search(r"\\langle\s*Pr,Tr,", ET)))

hr("T4  CU-E-1..18: §14.3 boxes, Appendix A, Foundations")
s143, appA = sec(ET, "## 14.3", "## 14.4"), sec(ET, "# Appendix A", "## A.2")
for n in range(1, 19):
    kk = f"CU-E-{n}"; ft = ftext(kk)
    box = re.sub(r"^\*\*\[[^\]]+\]\*\* ", "", re.search(r"### " + re.escape(kk) + r" —[^\n]*\n\n(.+?)\n\n", s143, re.S).group(1))
    ab = re.search(r"### " + re.escape(kk) + r" —[^\n]*\n\n(.+?)\n\n", appA, re.S).group(1)
    st = re.search(r"Claim/candidate status:\*\* ([^\n]+?)\s*$", fblk(kk), re.M).group(1)
    if box != ft or ab != ft:
        print(f"{kk}: box==Foundations {box == ft}, appendix==Foundations {ab == ft}")
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ft.split(), box.split()).get_opcodes():
            if op != "equal": print(f"    Foundations '{' '.join(ft.split()[i1:i2])}' -> box '{' '.join(box.split()[j1:j2])}'")
print("others identical in both places; Foundations statuses all provisional:",
      all("PROVISIONAL" in re.search(r"Claim/candidate status:\*\* ([^\n]+)", fblk(f"CU-E-{n}")).group(1) for n in range(1, 19)))

hr("T5  CU-E-17 alias and CU-G6")
e17 = fblk("CU-E-17")
print("Foundations authority class:", re.search(r"Authority class:\*\* ([^\n]+?)\s*$", e17, re.M).group(1),
      "| disposition:", (re.search(r"Disposition:\*\* ([^\n]+)", e17) or [None, None])[1])
print("Ethics headings for CU-E-17:", len(re.findall(r"^### CU-E-17", ET, re.M)), "| CU-G6 mentioned in Ethics:", "CU-G6" in ET)

hr("T6  Commitments: section titles and CU-COM12 text")
for c, t in re.findall(r"^## 15\.\d+ (CU-COM\d+) — (.+)$", ET, re.M):
    f = re.search(r"^## [\d.]+ " + c + r" — (.+)$", FD, re.M).group(1)
    print(f"{c}: heading '{t}' | Foundations '{f}' | same: {t == f}")
blk = FD[FD.index("CU-COM12 — Ethical"):]; blk = blk[:blk.index("\n## ")]
for lab in ("Commitment statement", "Practical expression", "Boundary conditions", "Revision conditions"):
    print(f"COM12 {lab} identical: {re.search(r'[*][*]' + lab + r'[.][*][*] (.+)', blk).group(1) in ET}")

hr("T7  Cross-paper: the self-deception definition and Mandala stages")
q = re.search(r"> \*\*(Self-deception is [^*]+)\*\*", ET).group(1)
print("§3.1 quoted definition identical to Foundations CU-Ψ11:", q.split(" False")[0] in ftext("CU-Ψ11"))
psy = re.search(r"## CU-Ψ11 — [^\n]+\n\n[^\n]+\n\n([^\n]+)", PS).group(1)
print("identical to Psychology's CU-Ψ11:", q in psy, "| Psychology:", psy[:110] + "…")
ft = {int(m.group(1)): m.group(2).strip() for m in re.finditer(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|", FD, re.M) if 1 <= int(m.group(1)) <= 64}
named = re.search(r"Stages 27–31: (.+?)\. ", ET).group(1).replace(", and ", ", ").split(", ")
print("stages 27-31:", [(27 + i, n == ft[27 + i]) for i, n in enumerate(named)])
later = re.search(r"especially (.+?)—show", ET).group(1).replace(", and ", ", ").replace("Stage 64, ", "").split(", ")
print("later stages named:", [(n, [k for k, v in ft.items() if v == n]) for n in later])

hr("T8  Propagation artifacts")
for kname, p in {"the account": r"(^|[.!?:]\s+)the account\b", "this account": r"(^|[.!?:]\s+)this account\b",
                 "the analysis": r"(^|[.!?:]\s+)the analysis\b", "this paper": r"(^|[.!?:]\s+)this paper"}.items():
    print(f"sentence-initial lowercase '{kname}':", [line(ET, m.start()) for m in re.finditer(p, ET, re.M)])
print("RC2 line:", [line(ET, m.start()) for m in re.finditer("RC2 remains the frozen baseline", ET)],
      "| stray 'Appendix B' construction pointer:", bool(re.search(r"Appendix B (gives|contains|shows)", ET)))
r1 = re.findall(r"^\d+\. (.+)$", sec(ET, "## 2.8", "# 3."), re.M); r2 = re.findall(r"^\d+\. (.+)$", sec(ET, "## A.2", "# Appendix B"), re.M)
print("twenty rules, §2.8 vs A.2:", len(r1), len(r2), "identical:", r1 == r2)

hr("T9  Citations")
i = ET.index("# References"); body, refs = ET[:i], ET[i:]
ents = [(re.match(r"([^,(.]+)", e).group(1).strip().split()[0], y) for e, y in re.findall(r"^([A-ZČ][^\n]*?)\((\d{4}|ca\.[^)]*|n\.d\.)[a-z]?[,/)]", refs, re.M)]
nonself = [e for e in ents if e[0] != "Rader"]
unc = sorted({e for e in nonself if not re.search(re.escape(e[0]) + r"[^\n]{0,90}" + re.escape(e[1][:4]), body)})
print(len(nonself), "non-self entries;", len(unc), "never cited by author and year:", unc)
print("moral-injury foundations uncited:", [e for e in unc if e[0] in ("Litz", "Shay")])
print("Lewis entry first author:", re.search(r"^Lewis, ([A-Z])\.", refs, re.M).group(1), "(source lists D. Lewis)")
