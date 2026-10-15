#!/usr/bin/env python3
"""Deterministic finite-model regression checks for Denying Knowledge v0.10 PC2.

These checks protect the paper's fixed-base preferential architecture and the
revised five-verdict taxonomy. They do not establish the KLM representation
theorems, supply a semantics for commitment language, determine the normative
content of a model, or replace independent philosophical review.
"""
from __future__ import annotations

import argparse
import json
from itertools import product
from pathlib import Path
from typing import FrozenSet

W: FrozenSet[int] = frozenset({0, 1, 2})
SUBSETS = [frozenset(i for i in W if mask & (1 << i)) for mask in range(1 << len(W))]
PAIRS = [(i, j) for i in W for j in W if i != j]


def is_strict_partial_order(rel: FrozenSet[tuple[int, int]]) -> bool:
    if any((x, x) in rel for x in W):
        return False
    for x, y in rel:
        for y2, z in rel:
            if y != y2:
                continue
            if x == z:
                return False
            if (x, z) not in rel:
                return False
    return True


def all_strict_partial_orders() -> list[FrozenSet[tuple[int, int]]]:
    orders: list[FrozenSet[tuple[int, int]]] = []
    for bits in range(1 << len(PAIRS)):
        rel = frozenset(PAIRS[k] for k in range(len(PAIRS)) if bits & (1 << k))
        if is_strict_partial_order(rel):
            orders.append(rel)
    return orders


def min_elements(xset: FrozenSet[int], rel: FrozenSet[tuple[int, int]]) -> FrozenSet[int]:
    return frozenset(x for x in xset if not any((y, x) in rel for y in xset))


def candidate_set(
    antecedent: FrozenSet[int],
    viable: FrozenSet[int],
) -> FrozenSet[int]:
    return viable & antecedent


def best_set(
    antecedent: FrozenSet[int],
    viable: FrozenSet[int],
    rel: FrozenSet[tuple[int, int]],
) -> FrozenSet[int]:
    return min_elements(candidate_set(antecedent, viable), rel)


def entails_fixed(
    antecedent: FrozenSet[int],
    consequent: FrozenSet[int],
    viable: FrozenSet[int],
    rel: FrozenSet[tuple[int, int]],
) -> bool:
    # This is the standard KLM-style semantic relation. As usual, empty
    # premise-compatible sets make the subset condition vacuously true. The
    # practical-verdict layer below adds explicit non-vacuity guards.
    return best_set(antecedent, viable, rel) <= consequent


def practical_verdict(
    candidates: FrozenSet[int],
    best: FrozenSet[int],
    phi: FrozenSet[int],
    *,
    model_adequate: bool = True,
) -> str:
    if not candidates:
        return "infeasible"
    if not model_adequate or not best:
        return "underdetermined"
    if best <= phi:
        return "strong_warrant"
    if best & phi:
        return "merely_admissible"
    return "excluded"


def check_system_p_finite() -> dict[str, object]:
    orders = all_strict_partial_orders()
    rule_evaluations = 0
    for rel in orders:
        for viable in SUBSETS:
            for a in SUBSETS:
                rule_evaluations += 1
                if not entails_fixed(a, a, viable, rel):
                    return {"pass": False, "orders": len(orders), "failure": {"rule": "Reflexivity"}}
                for b in SUBSETS:
                    for c in SUBSETS:
                        ab = entails_fixed(a, b, viable, rel)
                        ac = entails_fixed(a, c, viable, rel)
                        rule_evaluations += 5
                        if b <= c and ab and not ac:
                            return {"pass": False, "orders": len(orders), "failure": {"rule": "Right Weakening"}}
                        if ab and ac and not entails_fixed(a, b & c, viable, rel):
                            return {"pass": False, "orders": len(orders), "failure": {"rule": "And"}}
                        if entails_fixed(a, c, viable, rel) and entails_fixed(b, c, viable, rel) and not entails_fixed(a | b, c, viable, rel):
                            return {"pass": False, "orders": len(orders), "failure": {"rule": "Or"}}
                        if ab and ac and not entails_fixed(a & b, c, viable, rel):
                            return {"pass": False, "orders": len(orders), "failure": {"rule": "Cautious Monotony"}}
                        if ab and entails_fixed(a & b, c, viable, rel) and not ac:
                            return {"pass": False, "orders": len(orders), "failure": {"rule": "Cut"}}
    return {"pass": True, "orders": len(orders), "rule_evaluations": rule_evaluations, "failure": None}


def ranked_relation(ranks: tuple[int, int, int]) -> FrozenSet[tuple[int, int]]:
    return frozenset((i, j) for i in W for j in W if ranks[i] < ranks[j])


def check_ranked_rational_monotony() -> dict[str, object]:
    cases = 0
    for ranks in product(range(3), repeat=3):
        rel = ranked_relation(ranks)
        for viable in SUBSETS:
            for a in SUBSETS:
                for b in SUBSETS:
                    for c in SUBSETS:
                        cases += 1
                        if (
                            entails_fixed(a, b, viable, rel)
                            and not entails_fixed(a, W - c, viable, rel)
                            and not entails_fixed(a & c, b, viable, rel)
                        ):
                            return {
                                "pass": False,
                                "cases": cases,
                                "failure": {
                                    "ranks": ranks,
                                    "V": sorted(viable),
                                    "A": sorted(a),
                                    "B": sorted(b),
                                    "C": sorted(c),
                                },
                            }
    return {
        "pass": True,
        "cases": cases,
        "minimum_attainment_note": "All relevant nonempty definable sets attain minima in these finite ranked models.",
        "failure": None,
    }


def check_premise_responsive_countermodel() -> dict[str, object]:
    # 0=w1: b,g; 1=w2: not-b,g; 2=w3: b,not-g.
    b = frozenset({0, 2})
    g = frozenset({0, 1})
    rel = frozenset({(0, 1), (2, 1)})
    v_empty = frozenset({0, 1})
    v_b = frozenset({2})
    empty_entails_b = entails_fixed(W, b, v_empty, rel)
    empty_entails_g = entails_fixed(W, g, v_empty, rel)
    after_b_entails_g = entails_fixed(W, g, v_b, rel)
    return {
        "pass": empty_entails_b and empty_entails_g and not after_b_entails_g,
        "empty_entails_b": empty_entails_b,
        "empty_entails_g": empty_entails_g,
        "after_b_entails_g": after_b_entails_g,
        "interpretation": "Cautious Monotony can fail when viability is recomputed non-intersectively from the premise.",
    }


def check_fixed_base_control() -> dict[str, object]:
    b = frozenset({0, 2})
    g = frozenset({0, 1})
    rel = frozenset({(0, 1), (2, 1)})
    viable = W
    empty_entails_b = entails_fixed(W, b, viable, rel)
    empty_entails_g = entails_fixed(W, g, viable, rel)
    b_entails_g = entails_fixed(b, g, viable, rel)
    cm_triggered = empty_entails_b and empty_entails_g
    return {
        "pass": (not cm_triggered) or b_entails_g,
        "empty_entails_b": empty_entails_b,
        "empty_entails_g": empty_entails_g,
        "b_entails_g": b_entails_g,
        "interpretation": "The same worlds and order do not violate Cautious Monotony under intersective premise filtering.",
    }


def check_credulous_conjunction_failure() -> dict[str, object]:
    best = frozenset({0, 1})
    phi = frozenset({0})
    psi = frozenset({1})
    adm_phi = bool(best & phi)
    adm_psi = bool(best & psi)
    adm_and = bool(best & (phi & psi))
    return {
        "pass": adm_phi and adm_psi and not adm_and,
        "admissible_phi": adm_phi,
        "admissible_psi": adm_psi,
        "admissible_conjunction": adm_and,
    }


def check_max_preservation_equivalence() -> dict[str, object]:
    cases = 0
    for scores in product(range(-1, 2), repeat=3):
        for s in SUBSETS:
            if not s:
                continue
            max_s = max(scores[i] for i in s)
            argmax_s = frozenset(i for i in s if scores[i] == max_s)
            for phi in SUBSETS:
                s_phi = s & phi
                if not s_phi:
                    continue
                cases += 1
                preservation = max(scores[i] for i in s_phi) >= max_s
                existential = bool(argmax_s & phi)
                if preservation != existential:
                    return {
                        "pass": False,
                        "cases": cases,
                        "failure": {"scores": scores, "S": sorted(s), "phi": sorted(phi)},
                    }
    return {"pass": True, "cases": cases, "failure": None}


def check_subset_max_antitonicity() -> dict[str, object]:
    cases = 0
    for scores in product(range(-1, 2), repeat=3):
        for s in SUBSETS:
            if not s:
                continue
            for t in SUBSETS:
                if not t or not t <= s:
                    continue
                cases += 1
                if max(scores[i] for i in t) > max(scores[i] for i in s):
                    return {"pass": False, "cases": cases, "failure": {"scores": scores, "S": sorted(s), "T": sorted(t)}}
    return {"pass": True, "cases": cases, "failure": None}


def check_verdict_partition_and_classical_negation() -> dict[str, object]:
    cases = 0
    counts = {
        "strong_warrant": 0,
        "merely_admissible": 0,
        "excluded": 0,
        "infeasible": 0,
        "underdetermined": 0,
    }
    for rel in all_strict_partial_orders():
        for viable in SUBSETS:
            for antecedent in SUBSETS:
                candidates = candidate_set(antecedent, viable)
                best = min_elements(candidates, rel)
                for phi in SUBSETS:
                    cases += 1
                    verdict = practical_verdict(candidates, best, phi)
                    counts[verdict] += 1
                    if verdict == "infeasible" and candidates:
                        return {"pass": False, "cases": cases, "failure": {"kind": "false_infeasible"}}
                    if verdict == "underdetermined":
                        return {"pass": False, "cases": cases, "failure": {"kind": "finite_model_should_attain_minimum"}}
                    if best:
                        excluded = verdict == "excluded"
                        strong_neg = best <= (W - phi)
                        if excluded != strong_neg:
                            return {
                                "pass": False,
                                "cases": cases,
                                "failure": {"kind": "classical_negation_duality", "best": sorted(best), "phi": sorted(phi)},
                            }
    expected = {
        "strong_warrant": 2665,
        "merely_admissible": 294,
        "excluded": 2665,
        "infeasible": 4104,
        "underdetermined": 0,
    }
    return {
        "pass": counts == expected,
        "cases": cases,
        "counts": counts,
        "expected_counts": expected,
        "finite_model_note": "Every nonempty subset of a finite strict partial order has a minimal element; therefore all no-best-set cases here are infeasible, not underdetermined.",
        "classical_negation_note": "Within the Boolean fragment, exclusion of phi is extensionally equivalent to strong warrant for not-phi; PC2 treats this as an adopted modeling choice, not a complete phenomenology of practical refusal.",
        "failure": None if counts == expected else {"kind": "unexpected_counts"},
    }


def check_non_singleton_best_stratum() -> dict[str, object]:
    configurations = 0
    counts = {"strong_warrant": 0, "merely_admissible": 0, "excluded": 0}
    cases = 0
    for rel in all_strict_partial_orders():
        for viable in SUBSETS:
            for antecedent in SUBSETS:
                candidates = candidate_set(antecedent, viable)
                best = min_elements(candidates, rel)
                if len(best) < 2:
                    continue
                configurations += 1
                for phi in SUBSETS:
                    cases += 1
                    verdict = practical_verdict(candidates, best, phi)
                    if verdict not in counts:
                        return {"pass": False, "cases": cases, "failure": {"verdict": verdict}}
                    counts[verdict] += 1
    expected = {"strong_warrant": 145, "merely_admissible": 294, "excluded": 145}
    return {
        "pass": configurations == 73 and cases == 584 and counts == expected,
        "best_set_configurations": configurations,
        "cases": cases,
        "counts": counts,
        "expected_counts": expected,
        "interpretation": "The middle verdict occurs exactly where tied or incomparable best realizations divide on the commitment content.",
        "failure": None if configurations == 73 and cases == 584 and counts == expected else {"kind": "unexpected_non_singleton_stratum"},
    }


def check_underdetermination_guard() -> dict[str, object]:
    candidates = frozenset({0, 1})
    best = frozenset({0, 1})
    phi = frozenset({0})
    verdict = practical_verdict(candidates, best, phi, model_adequate=False)
    return {
        "pass": verdict == "underdetermined",
        "verdict": verdict,
        "interpretation": "Underdetermination is a model-adequacy verdict, not an empty-feasible-set verdict in the finite complete regressions.",
    }


def check_empty_best_practical_guards() -> dict[str, object]:
    candidates: FrozenSet[int] = frozenset()
    best: FrozenSet[int] = frozenset()
    phi = frozenset({0})
    verdict = practical_verdict(candidates, best, phi)
    strong = bool(best) and best <= phi
    admissible = bool(best) and bool(best & phi)
    excluded = bool(best) and not bool(best & phi)
    return {
        "pass": verdict == "infeasible" and not strong and not admissible and not excluded,
        "strong_warrant": strong,
        "admissible": admissible,
        "excluded": excluded,
        "verdict": verdict,
    }


def build_results() -> dict[str, object]:
    results = {
        "fixed_base_system_p_exhaustive_three_worlds": check_system_p_finite(),
        "ranked_rational_monotony_exhaustive_three_worlds": check_ranked_rational_monotony(),
        "premise_responsive_cautious_monotony_countermodel": check_premise_responsive_countermodel(),
        "fixed_base_countermodel_control": check_fixed_base_control(),
        "credulous_admissibility_conjunction_failure": check_credulous_conjunction_failure(),
        "maximum_preservation_equivalence_finite_regression": check_max_preservation_equivalence(),
        "subset_maximum_antitonicity": check_subset_max_antitonicity(),
        "practical_verdict_partition_and_classical_negation": check_verdict_partition_and_classical_negation(),
        "non_singleton_best_set_verdict_stratum": check_non_singleton_best_stratum(),
        "underdetermination_model_adequacy_guard": check_underdetermination_guard(),
        "empty_candidate_set_practical_guards": check_empty_best_practical_guards(),
    }
    return {
        "title": "Denying Knowledge v0.10 PC2 logic regression",
        "scope": "Finite deterministic checks of the fixed-base consequence architecture and revised verdict taxonomy; not a semantics of commitment, a KLM representation proof, a source of normative content, or peer review.",
        "overall_pass": all(bool(v.get("pass")) for v in results.values()),
        "results": results,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    root = Path(__file__).resolve().parent
    parser.add_argument("--json", type=Path, default=root / "Denying_Knowledge_v0.10_PC2_Logic_Results.json")
    parser.add_argument("--text", type=Path, default=root / "Denying_Knowledge_v0.10_PC2_Logic_Results.txt")
    args = parser.parse_args()

    payload = build_results()
    args.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    lines = [
        str(payload["title"]),
        "=" * len(str(payload["title"])),
        "",
        f"OVERALL: {'PASS' if payload['overall_pass'] else 'FAIL'}",
        "",
        str(payload["scope"]),
        "",
    ]
    for name, result in payload["results"].items():
        lines.append(f"{name}: {'PASS' if result.get('pass') else 'FAIL'}")
        for key, value in result.items():
            if key != "pass":
                lines.append(f"  {key}: {value}")
        lines.append("")
    args.text.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    if not payload["overall_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
