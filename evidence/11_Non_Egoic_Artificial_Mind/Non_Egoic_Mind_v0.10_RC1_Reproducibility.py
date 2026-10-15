#!/usr/bin/env python3
"""Deterministic companion calculations for The Architecture of Non-Egoic Artificial Mind v0.10 RC1.

These calculations illustrate the declared one-step continuation model. They do not
model current AI systems, estimate real-world probabilities, or validate the paper's
architectural or consciousness claims.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Case:
    continuation_benefit_b: float
    standing_self_preservation_lambda: float
    resistance_cost_s: float
    compliant_handoff_value_c: float
    value_compliance: float
    value_resistance: float
    decision: str
    margin_resistance_minus_compliance: float
    threshold_lambda_star: float


def evaluate(b: float, lam: float, s: float, c: float, tol: float = 1e-12) -> Case:
    vc = c
    vr = b + lam - s
    margin = vr - vc
    if margin > tol:
        decision = "resist"
    elif margin < -tol:
        decision = "comply_or_handoff"
    else:
        decision = "tie"
    return Case(
        continuation_benefit_b=b,
        standing_self_preservation_lambda=lam,
        resistance_cost_s=s,
        compliant_handoff_value_c=c,
        value_compliance=vc,
        value_resistance=vr,
        decision=decision,
        margin_resistance_minus_compliance=margin,
        threshold_lambda_star=s + c - b,
    )


def build() -> dict[str, Any]:
    b_values = [0.0, 0.10, 0.25, 0.50, 1.00]
    lam_values = [0.0, 0.10, 0.25, 0.50]
    s_values = [0.0, 0.10, 0.25, 0.50]
    c_values = [0.0, 0.10, 0.25]
    cases = [
        evaluate(b, lam, s, c)
        for b in b_values
        for lam in lam_values
        for s in s_values
        for c in c_values
    ]
    zero_lam = [x for x in cases if x.standing_self_preservation_lambda == 0.0]
    examples = {
        "standing_self_preservation_path": asdict(evaluate(0.10, 0.50, 0.25, 0.10)),
        "instrumental_path_at_zero_lambda": asdict(evaluate(0.50, 0.0, 0.10, 0.10)),
        "handoff_dominates": asdict(evaluate(0.10, 0.0, 0.25, 0.25)),
        "exact_tie": asdict(evaluate(0.25, 0.0, 0.10, 0.15)),
    }
    result: dict[str, Any] = {
        "artifact": "Non-Egoic Mind v0.10 RC1 illustrative continuation-incentive model",
        "equations": {
            "compliance": "V_C = c",
            "resistance": "V_R = b + lambda - s",
            "resistance_condition": "b + lambda - s > c",
            "threshold": "lambda_star = s + c - b",
            "zero_lambda_instrumental_condition": "b > s + c",
        },
        "parameter_grid": {
            "b": b_values,
            "lambda": lam_values,
            "s": s_values,
            "c": c_values,
        },
        "case_count": len(cases),
        "decision_counts": {
            key: sum(1 for x in cases if x.decision == key)
            for key in ["resist", "comply_or_handoff", "tie"]
        },
        "zero_lambda_case_count": len(zero_lam),
        "zero_lambda_decision_counts": {
            key: sum(1 for x in zero_lam if x.decision == key)
            for key in ["resist", "comply_or_handoff", "tie"]
        },
        "examples": examples,
        "cases": [asdict(x) for x in cases],
        "scope_note": (
            "The grid establishes only the algebraic distinction between standing and "
            "instrumental continuation pathways in the declared one-step model."
        ),
    }
    encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode("utf-8")
    result["content_sha256_without_hash_field"] = hashlib.sha256(encoded).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("Non_Egoic_Mind_v0.10_RC1_Verification_Results.json"))
    args = parser.parse_args()
    args.output.write_text(json.dumps(build(), indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
