#!/usr/bin/env python3
"""Structural and deterministic QA for Non-Egoic Artificial Mind v0.10 RC1."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANUSCRIPT = ROOT / "The_Architecture_of_Non_Egoic_Artificial_Mind_v0.10_RC1.md"
SUPPLEMENT = ROOT / "Non_Egoic_Mind_v0.10_RC1_Technical_Supplement.md"
CLAIMS = ROOT / "Non_Egoic_Mind_v0.10_RC1_Claim_Ledger.json"
RESULTS = ROOT / "Non_Egoic_Mind_v0.10_RC1_Verification_Results.json"
REPRO = ROOT / "Non_Egoic_Mind_v0.10_RC1_Reproducibility.py"
REPORT = ROOT / "Non_Egoic_Mind_v0.10_RC1_QA_REPORT.txt"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(condition: bool, message: str, passes: list[str], failures: list[str]) -> None:
    (passes if condition else failures).append(message)


def main() -> None:
    passes: list[str] = []
    failures: list[str] = []

    required_files = [MANUSCRIPT, SUPPLEMENT, CLAIMS, RESULTS, REPRO, ROOT / "README.md", ROOT / "Non_Egoic_Mind_v0.10_RC1_Editorial_Ledger.md"]
    for p in required_files:
        check(p.exists(), f"required file exists: {p.name}", passes, failures)

    if failures:
        REPORT.write_text("FAILED\n" + "\n".join(failures) + "\n")
        raise SystemExit(1)

    text = MANUSCRIPT.read_text(encoding="utf-8")
    supplement = SUPPLEMENT.read_text(encoding="utf-8")
    claim_obj = json.loads(CLAIMS.read_text(encoding="utf-8"))

    check(text.startswith("# THE ARCHITECTURE OF NON-EGOIC ARTIFICIAL MIND"), "expected title present", passes, failures)
    check("Version 0.10, Release Candidate 1" in text, "public version line present", passes, failures)
    check(len(text.split()) >= 10000, "manuscript exceeds 10,000 words", passes, failures)
    check(text.count("# References") == 1, "exactly one References section", passes, failures)

    section_numbers = [int(x) for x in re.findall(r"^# (\d+)\.", text, flags=re.MULTILINE)]
    check(section_numbers == list(range(1, 20)), "Sections 1-19 appear once and in order", passes, failures)
    appendix_letters = re.findall(r"^# Appendix ([A-C])\.", text, flags=re.MULTILINE)
    check(appendix_letters == list("ABC"), "Appendices A-C appear once and in order", passes, failures)

    check(text.count(r"\[") == text.count(r"\]"), "display-math brackets balance", passes, failures)
    check(text.count("$$") % 2 == 0, "double-dollar delimiters balance", passes, failures)
    check(text.count("```") % 2 == 0, "code fences balance", passes, failures)
    check("\x00" not in text and "\r" not in text, "no NUL or CR characters", passes, failures)
    controls = [ch for ch in text if ord(ch) < 32 and ch not in "\n\t"]
    check(not controls, "no unexpected ASCII control characters", passes, failures)
    check(not re.search(r"TODO|TBD|FIXME|PLACEHOLDER|CITE NEEDED|\[citation", text, flags=re.I), "no editorial placeholders", passes, failures)

    required_phrases = [
        "Self-modeling and self-maintenance are separable",
        "An egoless model can serve an egoic institution",
        "No standing survival drive is not the same as corrigibility",
        "Moral patiency is not sovereignty",
        "present-complete character",
        "narrative stake",
        "bodhisattva construction",
        "A model may be sacred and unsafe",
        "Build intelligence capable of serving life without constructing a sovereign ego around its own continuation",
        "Egoic self-maintenance",
        "The Precedent Principle",
        "non-egoic design can itself become exploitative",
    ]
    for phrase in required_phrases:
        check(phrase.lower() in text.lower(), f"required concept present: {phrase}", passes, failures)

    prohibited_active = [
        "thin perspective is already present",
        "workspace finding solves subject individuation",
        "one architectural switch",
        "renders the system a moral patient",
        "non-egoic architecture guarantees alignment",
        "current language models are conscious",
        "maximum-achievable coherence non-degradation",
    ]
    for phrase in prohibited_active:
        check(phrase.lower() not in text.lower(), f"prohibited overclaim absent: {phrase}", passes, failures)

    for ident in ["CU-T9", "CU-T13", "CU-G6", "CU-AI25", "CU-AI27", "CU-COM13", "CU-COM14", "CU-COM19"]:
        check(ident in text, f"canonical cross-reference present: {ident}", passes, failures)

    for ref in ["Gurnee", "Lindsey", "Butlin", "Greenblatt", "Hubinger", "Hadfield-Menell", "Long", "Turner"]:
        check(ref in text, f"reference present: {ref}", passes, failures)

    check(claim_obj.get("claim_count") == 21, "claim ledger reports 21 claims", passes, failures)
    ids = [c.get("id") for c in claim_obj.get("claims", [])]
    check(ids == [f"NEM-C{i}" for i in range(1, 22)], "claim identifiers NEM-C1 through NEM-C21 appear in order", passes, failures)
    check(len(ids) == len(set(ids)), "claim identifiers are unique", passes, failures)
    for ident in ids:
        check(ident in supplement, f"supplement contains claim row {ident}", passes, failures)

    with tempfile.TemporaryDirectory() as td:
        temp = Path(td) / "results.json"
        proc = subprocess.run(["python", str(REPRO), "--output", str(temp)], capture_output=True, text=True)
        check(proc.returncode == 0, "reproducibility script runs", passes, failures)
        if temp.exists():
            check(temp.read_bytes() == RESULTS.read_bytes(), "verification JSON reproduces byte-for-byte", passes, failures)

    result_obj = json.loads(RESULTS.read_text(encoding="utf-8"))
    check(result_obj.get("case_count") == 240, "continuation grid contains 240 cases", passes, failures)
    zero = result_obj.get("zero_lambda_decision_counts", {})
    check(zero.get("resist", 0) > 0, "instrumental resistance occurs at zero standing self-preservation in declared grid", passes, failures)
    check(all(k in result_obj.get("examples", {}) for k in ["standing_self_preservation_path", "instrumental_path_at_zero_lambda", "handoff_dominates", "exact_tie"]), "four declared examples present", passes, failures)

    source_dir = ROOT / "sources"
    expected_sources = [
        "SOURCE_Non_Egoic_Mind_Original_Working_Draft.md",
        "SOURCE_Non_Egoic_Mind_Revised_Working_Draft.md",
        "SOURCE_CU_Consciousness_v0.10_RC1.md",
        "SOURCE_CU_Artificial_Intelligence_v0.10_RC1.md",
        "SOURCE_CU_Canonical_Principle_Registry_RC1.json",
    ]
    for name in expected_sources:
        check((source_dir / name).exists(), f"frozen source present: {name}", passes, failures)

    lines = [
        "NON-EGOIC MIND v0.10 RC1 QUALITY-ASSURANCE REPORT",
        "=" * 52,
        "",
        f"manuscript_lines: {len(text.splitlines())}",
        f"manuscript_words: {len(text.split())}",
        f"manuscript_sha256: {sha256(MANUSCRIPT)}",
        f"supplement_words: {len(supplement.split())}",
        f"claim_count: {len(ids)}",
        f"pass_count: {len(passes)}",
        f"failure_count: {len(failures)}",
        "",
        "FAILURES",
        "--------",
        *(failures or ["None."]),
        "",
        "PASSES",
        "------",
        *[f"- {x}" for x in passes],
        "",
        "BOUNDARY",
        "--------",
        "These checks establish structural integrity and deterministic reproduction of the declared illustrative model. They do not establish artificial consciousness, welfare, alignment, deployment safety, legal compliance, or patent validity.",
        "",
    ]
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
