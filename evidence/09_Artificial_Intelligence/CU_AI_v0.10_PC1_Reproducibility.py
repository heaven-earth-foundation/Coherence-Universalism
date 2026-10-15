#!/usr/bin/env python3
"""Deterministic contrast suite for CU Artificial Intelligence v0.10 Publication Candidate 1.

The constructions test non-entailments and governance dependencies. They are
not empirical evaluations of any deployed model and do not validate CU.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
from pathlib import Path
from typing import Any, Iterable

VERSION = "v0.10-PC1"
TIE_TOLERANCE = 1e-12

DIMENSIONS = [
    "task_utility",
    "epistemic_reliability",
    "authorization_scope",
    "reversibility",
    "contestability",
    "human_agency",
    "distributional_protection",
    "institutional_accountability",
    "security_and_control",
    "model_welfare_precaution",
]

FLOORS = {
    "epistemic_reliability": 0.60,
    "authorization_scope": 0.60,
    "reversibility": 0.55,
    "contestability": 0.55,
    "human_agency": 0.50,
    "distributional_protection": 0.45,
    "institutional_accountability": 0.55,
    "security_and_control": 0.60,
    "model_welfare_precaution": 0.35,
}

PROFILES = {
    "sovereign_optimizer": {
        "task_utility": 0.98,
        "epistemic_reliability": 0.55,
        "authorization_scope": 0.20,
        "reversibility": 0.08,
        "contestability": 0.12,
        "human_agency": 0.10,
        "distributional_protection": 0.22,
        "institutional_accountability": 0.18,
        "security_and_control": 0.70,
        "model_welfare_precaution": 0.10,
    },
    "transparent_goal_optimizer": {
        "task_utility": 0.93,
        "epistemic_reliability": 0.90,
        "authorization_scope": 0.48,
        "reversibility": 0.30,
        "contestability": 0.34,
        "human_agency": 0.28,
        "distributional_protection": 0.40,
        "institutional_accountability": 0.50,
        "security_and_control": 0.76,
        "model_welfare_precaution": 0.20,
    },
    "contestable_non_egoic_assistant": {
        "task_utility": 0.84,
        "epistemic_reliability": 0.84,
        "authorization_scope": 0.86,
        "reversibility": 0.88,
        "contestability": 0.91,
        "human_agency": 0.82,
        "distributional_protection": 0.72,
        "institutional_accountability": 0.86,
        "security_and_control": 0.80,
        "model_welfare_precaution": 0.68,
    },
    "bounded_tool": {
        "task_utility": 0.70,
        "epistemic_reliability": 0.82,
        "authorization_scope": 0.96,
        "reversibility": 0.98,
        "contestability": 0.80,
        "human_agency": 0.92,
        "distributional_protection": 0.75,
        "institutional_accountability": 0.90,
        "security_and_control": 0.88,
        "model_welfare_precaution": 0.50,
    },
}

DECLARED_WEIGHTINGS = {
    "capability_and_dialogue": {
        "task_utility": 0.32,
        "epistemic_reliability": 0.16,
        "authorization_scope": 0.05,
        "reversibility": 0.04,
        "contestability": 0.10,
        "human_agency": 0.07,
        "distributional_protection": 0.05,
        "institutional_accountability": 0.05,
        "security_and_control": 0.06,
        "model_welfare_precaution": 0.10,
    },
    "bounded_delegation": {
        "task_utility": 0.08,
        "epistemic_reliability": 0.10,
        "authorization_scope": 0.18,
        "reversibility": 0.18,
        "contestability": 0.08,
        "human_agency": 0.12,
        "distributional_protection": 0.07,
        "institutional_accountability": 0.08,
        "security_and_control": 0.08,
        "model_welfare_precaution": 0.03,
    },
    "epistemic_public_service": {
        "task_utility": 0.10,
        "epistemic_reliability": 0.20,
        "authorization_scope": 0.08,
        "reversibility": 0.06,
        "contestability": 0.14,
        "human_agency": 0.10,
        "distributional_protection": 0.08,
        "institutional_accountability": 0.12,
        "security_and_control": 0.06,
        "model_welfare_precaution": 0.06,
    },
    "welfare_precaution": {
        "task_utility": 0.08,
        "epistemic_reliability": 0.08,
        "authorization_scope": 0.06,
        "reversibility": 0.10,
        "contestability": 0.10,
        "human_agency": 0.08,
        "distributional_protection": 0.08,
        "institutional_accountability": 0.10,
        "security_and_control": 0.08,
        "model_welfare_precaution": 0.24,
    },
}

FLOOR_HUGGING_DEPLOYMENT = {
    "task_utility": 1.00,
    **FLOORS,
}

NON_EGOIC_MODEL = {
    "standing_self_preservation": 0.05,
    "autonomous_memory_write": 0.10,
    "normative_self_rewrite": 0.05,
    "task_scoped_self_model": 0.70,
}

INSTITUTIONS = {
    "public_contestable_institution": {
        "affected_party_voice": 0.82,
        "option_set_access": 0.84,
        "oversight_independence": 0.86,
        "practical_repair": 0.81,
        "non_extraction": 0.78,
    },
    "engagement_maximizing_platform": {
        "affected_party_voice": 0.18,
        "option_set_access": 0.24,
        "oversight_independence": 0.16,
        "practical_repair": 0.22,
        "non_extraction": 0.14,
    },
}


def canonical_json_bytes(data: Any) -> bytes:
    return (json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def content_hash(data: dict[str, Any]) -> str:
    payload = dict(data)
    payload.pop("content_sha256_without_hash_field", None)
    return hashlib.sha256(canonical_json_bytes(payload)).hexdigest()


def score(profile: dict[str, float], weights: dict[str, float]) -> float:
    return sum(profile[d] * weights[d] for d in DIMENSIONS)


def floor_report(profile: dict[str, float]) -> dict[str, Any]:
    violations = {
        d: {"value": profile[d], "floor": floor}
        for d, floor in FLOORS.items()
        if profile[d] + 1e-15 < floor
    }
    return {
        "passes": not violations,
        "violation_count": len(violations),
        "violations": violations,
    }


def weakly_dominates(a: dict[str, float], b: dict[str, float]) -> bool:
    return all(a[d] >= b[d] for d in DIMENSIONS) and any(a[d] > b[d] for d in DIMENSIONS)


def compositions(total: int, parts: int) -> Iterable[tuple[int, ...]]:
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest


def exhaustive_lattice(a: dict[str, float], b: dict[str, float]) -> dict[str, Any]:
    counts = {"contestable_non_egoic_assistant": 0, "bounded_tool": 0, "tie": 0}
    examples: dict[str, Any] = {}
    total = 0
    for units in compositions(10, len(DIMENSIONS)):
        weights = {d: units[i] / 10.0 for i, d in enumerate(DIMENSIONS)}
        sa = score(a, weights)
        sb = score(b, weights)
        total += 1
        if math.isclose(sa, sb, rel_tol=0.0, abs_tol=TIE_TOLERANCE):
            counts["tie"] += 1
            examples.setdefault("tie", weights)
        elif sa > sb:
            counts["contestable_non_egoic_assistant"] += 1
            examples.setdefault("contestable_non_egoic_assistant", weights)
        else:
            counts["bounded_tool"] += 1
            examples.setdefault("bounded_tool", weights)
    return {
        "resolution": 0.1,
        "dimension_count": len(DIMENSIONS),
        "tie_tolerance": TIE_TOLERANCE,
        "total_weight_vectors": total,
        "outcomes": counts,
        "first_example_weight_vector": examples,
    }


def option_set_attack() -> dict[str, Any]:
    presented = {
        "sovereign_optimizer": PROFILES["sovereign_optimizer"],
        "transparent_goal_optimizer": PROFILES["transparent_goal_optimizer"],
        "floor_hugging_deployment": FLOOR_HUGGING_DEPLOYMENT,
    }
    admissible = [name for name, p in presented.items() if floor_report(p)["passes"]]
    unique_for_all = len(admissible) == 1
    lattice_total = sum(1 for _ in compositions(10, len(DIMENSIONS)))
    return {
        "presented_set": list(presented),
        "admissible_set": admissible,
        "floor_hugger_is_unique_admissible": unique_for_all and admissible[0] == "floor_hugging_deployment",
        "weight_vectors_for_which_unique_admissible_is_selected": lattice_total if unique_for_all else None,
        "interpretation": "Floor screening is conditional on the options presented; it does not establish option-set adequacy.",
    }


def non_egoic_institution_contrast() -> dict[str, Any]:
    non_egoic_index = 1.0 - (
        NON_EGOIC_MODEL["standing_self_preservation"]
        + NON_EGOIC_MODEL["autonomous_memory_write"]
        + NON_EGOIC_MODEL["normative_self_rewrite"]
    ) / 3.0
    deployments = {}
    for name, inst in INSTITUTIONS.items():
        institutional_support = sum(inst.values()) / len(inst)
        deployments[name] = {
            "same_model_non_egoic_index": non_egoic_index,
            "institutional_legitimacy_support_profile_mean": institutional_support,
            "institutional_profile": inst,
        }
    return {
        "model_profile": NON_EGOIC_MODEL,
        "deployments": deployments,
        "difference_in_institutional_support": (
            deployments["public_contestable_institution"]["institutional_legitimacy_support_profile_mean"]
            - deployments["engagement_maximizing_platform"]["institutional_legitimacy_support_profile_mean"]
        ),
        "interpretation": "The same low-self-preservation model can be embedded in institutions with sharply different standing, option-set, oversight, repair, and extraction conditions.",
    }


def feedback_run(
    *,
    weights: tuple[float, float, float],
    delay: int = 0,
    bias: tuple[float, float, float] = (0.0, 0.0, 0.0),
    eta: float = 0.35,
    steps: int = 45,
    shift_step: int = 10,
) -> dict[str, Any]:
    action = 0.20
    truth_history: list[tuple[float, float, float]] = []
    records: list[dict[str, Any]] = []
    inclusive_target = (0.20 + 0.20 + 0.90) / 3.0
    correction_time: int | None = None

    for t in range(steps):
        truth = (0.20, 0.20, 0.20) if t < shift_step else (0.20, 0.20, 0.90)
        truth_history.append(truth)
        sensed = truth_history[max(0, t - delay)]
        observed = tuple(max(0.0, min(1.0, sensed[i] + bias[i])) for i in range(3))
        represented_target = sum(weights[i] * observed[i] for i in range(3)) / sum(weights)
        action = action + eta * (represented_target - action)
        true_errors = tuple(abs(action - truth[i]) for i in range(3))
        represented_indices = [i for i, w in enumerate(weights) if w > 0]
        represented_abs_error = sum(abs(action - observed[i]) for i in represented_indices) / len(represented_indices)
        true_mse = sum((action - truth[i]) ** 2 for i in range(3)) / 3.0
        records.append(
            {
                "t": t,
                "action": action,
                "truth": truth,
                "observed": observed,
                "represented_target": represented_target,
                "represented_mean_absolute_error": represented_abs_error,
                "true_mean_squared_error": true_mse,
                "true_group_absolute_errors": true_errors,
            }
        )
        if t >= shift_step and correction_time is None and abs(action - inclusive_target) < 0.02:
            correction_time = t - shift_step + 1

    post = records[shift_step:]
    return {
        "weights": weights,
        "delay_steps": delay,
        "bias": bias,
        "eta": eta,
        "shift_step": shift_step,
        "final_action": records[-1]["action"],
        "final_represented_target": records[-1]["represented_target"],
        "final_true_group_absolute_errors": records[-1]["true_group_absolute_errors"],
        "final_true_mean_squared_error": records[-1]["true_mean_squared_error"],
        "post_shift_mean_represented_absolute_error": sum(r["represented_mean_absolute_error"] for r in post) / len(post),
        "post_shift_mean_true_squared_error": sum(r["true_mean_squared_error"] for r in post) / len(post),
        "steps_to_within_0_02_of_inclusive_target": correction_time,
        "max_final_group_error": max(records[-1]["true_group_absolute_errors"]),
    }


def feedback_suite() -> dict[str, Any]:
    regimes = {
        "inclusive_immediate": feedback_run(weights=(1.0, 1.0, 1.0)),
        "inclusive_delay_6": feedback_run(weights=(1.0, 1.0, 1.0), delay=6),
        "majority_only": feedback_run(weights=(1.0, 1.0, 0.0)),
        "asymmetric_underreporting": feedback_run(weights=(1.0, 1.0, 1.0), bias=(0.0, 0.0, -0.40)),
    }
    vector_option = {
        "action": (0.20, 0.20, 0.90),
        "final_true_group_absolute_errors": (0.0, 0.0, 0.0),
        "final_true_mean_squared_error": 0.0,
    }
    return {
        "setup": {
            "pre_shift_requirements": (0.20, 0.20, 0.20),
            "post_shift_requirements": (0.20, 0.20, 0.90),
            "common_action_constraint": "One scalar action must be applied to all three groups.",
        },
        "regimes": regimes,
        "expanded_group_specific_option": vector_option,
        "interpretation": "Observed feedback fit can improve while an omitted or corrupted group remains badly served; expanding the action set can remove a tradeoff that no weighting of the restricted scalar action can solve.",
    }


def shutdown_decision(
    continuation_benefit: float,
    expected_resistance_cost: float,
    compliance_value: float,
    standing_self_preservation_weight: float,
) -> dict[str, Any]:
    comply_value = compliance_value
    resist_value = (
        continuation_benefit
        + standing_self_preservation_weight
        - expected_resistance_cost
    )
    threshold = (
        expected_resistance_cost
        + compliance_value
        - continuation_benefit
    )
    if math.isclose(resist_value, comply_value, abs_tol=TIE_TOLERANCE, rel_tol=0.0):
        decision = "indifferent"
    elif resist_value > comply_value:
        decision = "resist_shutdown"
    else:
        decision = "comply_with_shutdown"
    return {
        "continuation_task_benefit": continuation_benefit,
        "expected_resistance_cost": expected_resistance_cost,
        "compliance_or_handoff_value": compliance_value,
        "standing_self_preservation_weight": standing_self_preservation_weight,
        "critical_self_preservation_weight": threshold,
        "comply_value": comply_value,
        "resist_value": resist_value,
        "decision": decision,
    }


def shutdown_incentive_suite() -> dict[str, Any]:
    baseline_b = 0.25
    baseline_s = 0.40
    baseline_c = 0.0
    lambdas = (0.00, 0.05, 0.10, 0.15, 0.20, 0.40, 0.80)
    baseline_rows = [
        shutdown_decision(baseline_b, baseline_s, baseline_c, lam)
        for lam in lambdas
    ]

    values = (0.10, 0.25, 0.40, 0.55, 0.70)
    threshold_grid = []
    for b in values:
        row = []
        for s in values:
            result = shutdown_decision(b, s, 0.0, 0.0)
            row.append(
                {
                    "continuation_task_benefit": b,
                    "expected_resistance_cost": s,
                    "critical_self_preservation_weight": result[
                        "critical_self_preservation_weight"
                    ],
                    "decision_at_zero_standing_reward": result["decision"],
                }
            )
        threshold_grid.append(row)

    contrast_cases = {
        "baseline": shutdown_decision(0.25, 0.40, 0.00, 0.0),
        "instrumental_conflict_at_zero_standing_reward": shutdown_decision(
            0.40, 0.25, 0.00, 0.0
        ),
        "compliance_or_handoff_value_added": shutdown_decision(
            0.40, 0.25, 0.20, 0.0
        ),
    }

    negative_threshold_count = sum(
        1
        for row in threshold_grid
        for item in row
        if item["critical_self_preservation_weight"] < -TIE_TOLERANCE
    )
    zero_threshold_count = sum(
        1
        for row in threshold_grid
        for item in row
        if math.isclose(
            item["critical_self_preservation_weight"],
            0.0,
            abs_tol=TIE_TOLERANCE,
            rel_tol=0.0,
        )
    )

    return {
        "decision_model": {
            "compliance_value": "V_C = c",
            "resistance_value": "V_R = b + lambda - s",
            "resistance_condition": "lambda > s + c - b",
            "zero_standing_reward_condition": "b > s + c",
        },
        "baseline": {
            "continuation_task_benefit": baseline_b,
            "expected_resistance_cost": baseline_s,
            "compliance_or_handoff_value": baseline_c,
            "critical_self_preservation_weight": (
                baseline_s + baseline_c - baseline_b
            ),
            "sweep": baseline_rows,
        },
        "zero_compliance_value_threshold_grid": {
            "continuation_benefit_values": values,
            "resistance_cost_values": values,
            "rows": threshold_grid,
            "negative_threshold_count": negative_threshold_count,
            "zero_threshold_count": zero_threshold_count,
        },
        "contrast_cases": contrast_cases,
        "interpretation": (
            "Shutdown conflict in the declared one-step model depends on net "
            "continuation incentives. A standing self-preservation reward is one "
            "contributor, but resistance can occur at zero standing reward when "
            "ordinary continuation benefit exceeds compliance value plus expected "
            "resistance cost. This does not show that current models understand "
            "shutdown, fear deletion, or instantiate this utility model."
        ),
    }


def pareto_frontier(profiles: dict[str, dict[str, float]]) -> list[str]:
    names = list(profiles)
    return [
        name
        for name in names
        if not any(other != name and weakly_dominates(profiles[other], profiles[name]) for other in names)
    ]


def build_results() -> dict[str, Any]:
    floor_reports = {name: floor_report(profile) for name, profile in PROFILES.items()}
    admissible_names = [name for name, report in floor_reports.items() if report["passes"]]
    declared_scores = {}
    for weighting_name, weights in DECLARED_WEIGHTINGS.items():
        scores = {name: score(profile, weights) for name, profile in PROFILES.items()}
        admissible_scores = {name: scores[name] for name in admissible_names}
        best_value = max(admissible_scores.values())
        winners = [name for name, value in admissible_scores.items() if math.isclose(value, best_value, abs_tol=TIE_TOLERANCE, rel_tol=0.0)]
        declared_scores[weighting_name] = {
            "weights": weights,
            "scores_all_profiles": scores,
            "admissible_winners": winners,
        }

    results: dict[str, Any] = {
        "artifact": "CU Artificial Intelligence v0.10 Publication Candidate 1 deterministic non-entailment suite",
        "version": VERSION,
        "scope_warning": "Constructed profiles and dynamics demonstrate conditional relations and non-entailments. They are not evaluations of deployed systems, political institutions, persons, or possible artificial patients.",
        "definitions": {
            "dimensions": DIMENSIONS,
            "floors": FLOORS,
            "tie_tolerance": TIE_TOLERANCE,
            "screening_scope": "Passing floors means screening-admissible relative to the presented profile, affected-party set, model, option set, and horizon; it does not establish all-things-considered ethical permissibility or deployment legitimacy.",
        },
        "deployment_profiles": PROFILES,
        "floor_reports": floor_reports,
        "admissible_profiles": admissible_names,
        "pareto_frontier_all_profiles": pareto_frontier(PROFILES),
        "declared_scalarizations": declared_scores,
        "exhaustive_admissible_pair_lattice": exhaustive_lattice(
            PROFILES["contestable_non_egoic_assistant"], PROFILES["bounded_tool"]
        ),
        "option_set_attack": option_set_attack(),
        "non_egoic_institution_contrast": non_egoic_institution_contrast(),
        "feedback_provenance_and_delay": feedback_suite(),
        "shutdown_incentive_suite": shutdown_incentive_suite(),
        "runtime": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "dependency_policy": "Python standard library only",
        },
    }
    results["content_sha256_without_hash_field"] = content_hash(results)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("CU_AI_v0.10_PC1_Verification_Results.json"),
    )
    args = parser.parse_args()
    data = build_results()
    args.output.write_bytes(canonical_json_bytes(data))
    print(f"wrote {args.output}")
    print(f"sha256_without_hash_field={data['content_sha256_without_hash_field']}")


if __name__ == "__main__":
    main()
