#!/usr/bin/env python3
"""Structural, registry, citation, and deterministic checks for CU Biology C.1.1.

These checks establish internal consistency of the supplied artifacts. They do
not establish the biological truth of the manuscript or replace expert review.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def check(condition: bool, message: str, failures: list[str], passes: list[str]) -> None:
    (passes if condition else failures).append(message)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manuscript",
        type=Path,
        default=Path(__file__).with_name(
            "CU_Biology_Systematic_Reconstruction_Kaya_C1_1.md"
        ),
    )
    parser.add_argument(
        "--results",
        type=Path,
        default=Path(__file__).with_name(
            "CU_Biology_C1_1_verification_results.json"
        ),
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path(__file__).with_name("CU_Biology_C1_1_QA_REPORT.txt"),
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    manuscript = args.manuscript.resolve()
    results_path = args.results.resolve()
    repro_script = root / "CU_Biology_C1_1_reproducibility.py"
    claim_path = root / "CU_Biology_C1_1_claim_ledger.json"
    principle_path = root / "CU_Biology_C1_1_principle_registry.json"
    literature_path = root / "CU_Biology_C1_1_LITERATURE_LEDGER.md"
    changelog_path = root / "CU_Biology_C1_1_CHANGELOG.md"
    audit_response_path = root / "CU_Biology_C1_1_AUDIT_RESPONSE.md"

    passes: list[str] = []
    failures: list[str] = []

    required_files = (
        manuscript,
        results_path,
        repro_script,
        claim_path,
        principle_path,
        literature_path,
        changelog_path,
        audit_response_path,
    )
    for path in required_files:
        check(path.exists(), f"required file exists: {path.name}", failures, passes)
    if failures:
        args.report.write_text("\n".join(["FAILED", *failures]) + "\n")
        raise SystemExit(1)

    text = manuscript.read_text(encoding="utf-8")
    lines = text.splitlines()
    lowered = text.lower()

    check(text.startswith("# COHERENCE UNIVERSALISM: BIOLOGY"), "expected title present", failures, passes)
    check("Systematic Reconstruction Draft — Version C.1.1" in text, "C.1.1 version line present", failures, passes)
    check("Literature horizon:" in text, "literature horizon declared", failures, passes)
    check(text.count("# References") == 1, "exactly one References section", failures, passes)

    section_numbers = [int(x) for x in re.findall(r"^# Section (\d+)\.", text, flags=re.MULTILINE)]
    check(section_numbers == list(range(1, 14)), "Sections 1–13 appear once and in order", failures, passes)
    appendix_letters = re.findall(r"^# Appendix ([A-F])\.", text, flags=re.MULTILINE)
    check(appendix_letters == list("ABCDEF"), "Appendices A–F appear once and in order", failures, passes)

    check(text.count(r"\[") == text.count(r"\]"), "display-math bracket counts balance", failures, passes)
    check(text.count("$$") % 2 == 0, "double-dollar math delimiters balance", failures, passes)
    check(text.count("```") % 2 == 0, "code-fence count is even", failures, passes)
    check("\t" not in text and "\r" not in text and "\x00" not in text, "no tabs, CRs, or NULs", failures, passes)
    controls = [ch for ch in text if ord(ch) < 32 and ch != "\n"]
    check(not controls, "no unexpected ASCII control characters", failures, passes)
    check(not re.search(r"\b(?:TODO|TBD|FIXME|PLACEHOLDER)\b", text), "no editorial placeholder tokens", failures, passes)

    required_phrases = [
        "Claim-governance protocol",
        "Boundary rule",
        "Horizon rule",
        "Disturbance rule",
        "Profile rule",
        "Register rule",
        "the viability effect of diffusive coupling is configuration-dependent",
        r"D M(x;c)=\kappa(\bar x-x_j)",
        "homogeneous-floor configuration",
        "specialized high-requirement component",
        "does not demonstrate coupling-mediated rescue from failure",
        "clipping counter is zero",
        "designer optimization",
        "as-if control analysis",
        "evolutionary outcome",
        "accelerated habituation and prolonged memory retention",
        "maintenance of habituation memory in progeny following cell division",
        "not fitted to biological data",
        "does not establish that biological integration generally destroys viability",
    ]
    for phrase in required_phrases:
        check(phrase.lower() in lowered, f"required repair phrase present: {phrase}", failures, passes)

    forbidden_active_phrases = [
        "simulation validates the framework",
        "all living systems maximize coherence",
        "fitness is identical with coherence",
        "life violates the second law",
        "integration destroys viability here",
        "coupling universally improves viability",
    ]
    for phrase in forbidden_active_phrases:
        check(phrase not in lowered, f"prohibited active overclaim absent: {phrase}", failures, passes)

    claims = json.loads(claim_path.read_text(encoding="utf-8"))
    claim_items = claims.get("claims", [])
    claim_ids = [x.get("id") for x in claim_items]
    expected_claim_ids = [f"BIO-C{i}" for i in range(1, 38)]
    check(claim_ids == expected_claim_ids, "claim registry contains BIO-C1–BIO-C37 in order", failures, passes)
    check(len(set(claim_ids)) == len(claim_ids), "claim registry identifiers are unique", failures, passes)
    check(claims.get("authority", "").endswith("Kaya_C1_1.md"), "claim-ledger authority names C.1.1 manuscript", failures, passes)
    for claim_id in expected_claim_ids:
        check(f"| {claim_id} |" in text, f"manuscript contains ledger row {claim_id}", failures, passes)

    principles = json.loads(principle_path.read_text(encoding="utf-8"))
    principle_ids = [x.get("id") for x in principles.get("principles", [])]
    check(principle_ids == ["CU-B1", "CU-B2", "CU-B3", "CU-B4", "CU-B5"], "principle registry contains CU-B1–CU-B5", failures, passes)
    check(principles.get("version") == "C.1.1", "principle registry version is C.1.1", failures, passes)
    check("do not modify Foundations B.2" in principles.get("promotion_rule", ""), "principle promotion guard present", failures, passes)
    check("did not assess CU-B1 through CU-B5" in principles.get("audit_boundary", ""), "principle audit boundary recorded", failures, passes)
    governance_markers = ["candidate unit and scale", "temporal horizon", "perturbation or disturbance class", "weights, protected floors", "phenomenal or moral value"]
    for marker in governance_markers:
        check(marker.lower() in lowered, f"governance rule appears in manuscript: {marker}", failures, passes)

    reference_text = text.split("# References", 1)[1]
    expected_reference_keys = {
        "Aubin": 1991,
        "Aoki": 2019,
        "Chernet": 2016,
        "Ciriello": 2024,
        "Cortés-Poza": 2026,
        "Doulcier": 2024,
        "Dufour": 2014,
        "Durant": 2019,
        "Friston": 2013,
        "Giessler": 2026,
        "Hordijk": 2011,
        "Kolchinsky": 2024,
        "Kriegman": 2020,
        "Maynard Smith": 1995,
        "Montévil": 2015,
        "Mossio": 2009,
        "Rajan": 2026,
        "Ruiz-Mirazo": 2004,
        "Schreiber": 2000,
        "Shi": 2025,
        "Shirt-Ediss": 2025,
        "Varela": 1974,
        "Walker": 2013,
        "West": 2015,
    }
    for author, year in expected_reference_keys.items():
        check(author in reference_text and f"({year})" in reference_text, f"reference present: {author} {year}", failures, passes)

    result = json.loads(results_path.read_text(encoding="utf-8"))
    checks = result.get("regression_checks", {})
    check(bool(checks) and all(checks.values()), "all numerical regression checks are true", failures, passes)
    check(result.get("artifact", "").startswith("CU Biology C.1.1"), "results identify C.1.1", failures, passes)

    primary = result.get("primary_configuration", {})
    adverse = result.get("adverse_configuration", {})
    primary_runs = primary.get("controller_runs", [])
    adverse_runs = adverse.get("controller_runs", [])
    check(len(primary_runs) == 8, "eight primary coupling runs recorded", failures, passes)
    check(len(adverse_runs) == 8, "eight adverse coupling runs recorded", failures, passes)
    check(all(r.get("clipped_step_count") == 0 for r in primary_runs + adverse_runs), "zero clipping in all default controller runs", failures, passes)
    check(primary.get("no_controller_reference", {}).get("first_failure_time") == 26.76, "primary no-controller failure time retained", failures, passes)
    check(len(primary.get("step_size_sensitivity", [])) == 4, "four primary step-size sweeps recorded", failures, passes)
    check(len(adverse.get("step_size_sensitivity", [])) == 4, "four adverse step-size sweeps recorded", failures, passes)

    for run in primary_runs:
        for field in ("minimum_viability_margin", "total_control_cost", "late_tracking_rmse"):
            token = f"{run[field]:.10f}"
            check(token in text, f"manuscript contains primary {field}={token} for kappa={run['coupling']}", failures, passes)
    for run in adverse_runs:
        margin_token = f"{run['minimum_viability_margin']:.10f}"
        check(margin_token in text, f"manuscript contains adverse minimum_viability_margin={margin_token} for kappa={run['coupling']}", failures, passes)
        direct_value = float(run["direct_coupling_contribution_to_binding_component"])
        direct_token = "0.0000000000" if abs(direct_value) < 5e-13 else f"{direct_value:.10f}"
        check(direct_token in text, f"manuscript contains adverse direct coupling={direct_token} for kappa={run['coupling']}", failures, passes)

    for item in primary.get("step_size_sensitivity", []):
        for field in ("minimum_margin_at_kappa_0", "minimum_margin_at_kappa_0_8"):
            token = f"{item[field]:.10f}"
            check(token in text, f"manuscript contains primary step-size {field}={token} at dt={item['dt']}", failures, passes)
    for item in adverse.get("step_size_sensitivity", []):
        for field in ("minimum_margin_at_kappa_0", "minimum_margin_at_kappa_0_8"):
            token = f"{item[field]:.10f}"
            check(token in text, f"manuscript contains adverse step-size {field}={token} at dt={item['dt']}", failures, passes)

    with tempfile.TemporaryDirectory() as td:
        rerun = Path(td) / "rerun.json"
        proc = subprocess.run(
            [sys.executable, str(repro_script), "--output", str(rerun)],
            capture_output=True,
            text=True,
            check=False,
        )
        check(proc.returncode == 0, "reproducibility script exits successfully", failures, passes)
        check(rerun.exists(), "reproducibility script creates output", failures, passes)
        if rerun.exists():
            check(rerun.read_bytes() == results_path.read_bytes(), "reproduced JSON is byte-for-byte identical", failures, passes)

    stats = {
        "manuscript_lines": len(lines),
        "manuscript_words": len(text.split()),
        "manuscript_bytes": len(text.encode("utf-8")),
        "manuscript_sha256": sha256(manuscript),
        "claim_count": len(claim_items),
        "candidate_principle_count": len(principle_ids),
        "primary_controller_run_count": len(primary_runs),
        "adverse_controller_run_count": len(adverse_runs),
        "pass_count": len(passes),
        "failure_count": len(failures),
    }

    report_lines = [
        "CU BIOLOGY C.1.1 QUALITY-ASSURANCE REPORT",
        "===========================================",
        "",
        "Scope: structural, registry, citation, and deterministic regression checks.",
        "This report is not biological peer review or empirical validation.",
        "",
        "SUMMARY",
        "-------",
        *[f"{key}: {value}" for key, value in stats.items()],
        "",
        "FAILURES",
        "--------",
    ]
    report_lines.extend(f"- {item}" for item in failures) if failures else report_lines.append("None.")
    report_lines.extend(["", "PASSES", "------", *[f"- {item}" for item in passes]])
    args.report.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(f"Wrote {args.report}")
    print(json.dumps(stats, indent=2, sort_keys=True))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
