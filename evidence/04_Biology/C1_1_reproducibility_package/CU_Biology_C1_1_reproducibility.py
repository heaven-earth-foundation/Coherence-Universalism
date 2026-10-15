#!/usr/bin/env python3
"""Deterministic illustrative control models for CU Biology C.1.1.

The primary configuration reproduces C.1's tradeoff: stronger diffusive
coupling improves the sampled minimum viability margin while increasing
control cost and worsening differentiated target tracking. The adverse
configuration shows the opposite viability direction when the binding
component has a high floor and lies above the system mean.

Both configurations are pedagogical. They are not fitted to biological data,
do not estimate an organism's optimal coupling, and do not validate a
universal biological coherence functional.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import numpy as np


@dataclass(frozen=True)
class NumericalParameters:
    dt: float = 0.01
    horizon: float = 150.0
    control_budget: float = 0.12
    controller_gain: float = 0.50
    urgency_slope: float = 8.0
    late_window_start: float = 130.0


@dataclass(frozen=True)
class Scenario:
    name: str
    floor: tuple[float, float, float]
    decay: tuple[float, float, float]
    supply: tuple[float, float, float]
    initial: tuple[float, float, float]
    target_before: tuple[float, float, float]
    target_after: tuple[float, float, float]
    target_shift_time: float
    disturbance_episodes: tuple[
        tuple[float, float, tuple[float, float, float]], ...
    ]
    interpretation: str


PRIMARY_SCENARIO = Scenario(
    name="homogeneous_floor_tradeoff",
    floor=(0.24, 0.24, 0.24),
    decay=(0.11, 0.09, 0.10),
    supply=(0.065, 0.055, 0.060),
    initial=(0.72, 0.72, 0.72),
    target_before=(0.75, 0.72, 0.70),
    target_after=(0.88, 0.56, 0.78),
    target_shift_time=100.0,
    disturbance_episodes=(
        (20.0, 28.0, (-0.075, 0.0, 0.0)),
        (50.0, 60.0, (-0.035, -0.055, -0.025)),
        (82.0, 88.0, (0.0, 0.0, -0.100)),
    ),
    interpretation=(
        "Equal floors make a binding component a minimum-state component. "
        "The direct diffusive contribution therefore cannot drain a unique "
        "binding component at a fixed state, although the global sweep trend "
        "still depends on the complete controlled trajectory."
    ),
)


ADVERSE_SCENARIO = Scenario(
    name="heterogeneous_floor_adverse_coupling",
    floor=(0.10, 0.10, 0.82),
    decay=(0.30, 0.30, 0.04),
    supply=(0.18, 0.18, 0.036),
    initial=(0.60, 0.60, 0.90),
    target_before=(0.60, 0.60, 0.90),
    target_after=(0.60, 0.60, 0.90),
    target_shift_time=150.0,
    disturbance_episodes=((40.0, 50.0, (0.0, 0.0, -0.020)),),
    interpretation=(
        "The third component has the highest state and the tightest floor. "
        "It is therefore the binding component while lying above the mean, "
        "so positive diffusive coupling directly drains it toward components "
        "with slack they do not require."
    ),
)


COUPLING_SWEEP = (0.0, 0.02, 0.05, 0.10, 0.15, 0.25, 0.40, 0.80)
STEP_SIZE_SWEEP = (0.04, 0.02, 0.01, 0.005)


def target_at(t: float, scenario: Scenario) -> np.ndarray:
    values = (
        scenario.target_before
        if t < scenario.target_shift_time
        else scenario.target_after
    )
    return np.asarray(values, dtype=float)


def disturbance_at(t: float, scenario: Scenario) -> np.ndarray:
    disturbance = np.zeros(3, dtype=float)
    for start, stop, vector in scenario.disturbance_episodes:
        if start <= t < stop:
            disturbance += np.asarray(vector, dtype=float)
    return disturbance


def control_action(
    x: np.ndarray,
    target: np.ndarray,
    floor: np.ndarray,
    params: NumericalParameters,
    enabled: bool,
) -> np.ndarray:
    if not enabled:
        return np.zeros(3, dtype=float)

    deficit = target - x
    desired = np.maximum(0.0, params.controller_gain * deficit)
    if float(desired.sum()) <= params.control_budget:
        return desired

    urgency = np.exp(-params.urgency_slope * (x - floor)) * (
        0.15 + np.maximum(deficit, 0.0)
    )
    total = float(urgency.sum())
    if not math.isfinite(total) or total <= 0.0:
        return np.full(3, params.control_budget / 3.0, dtype=float)
    return params.control_budget * urgency / total


def simulate(
    coupling: float,
    params: NumericalParameters,
    scenario: Scenario,
    controller_enabled: bool = True,
) -> dict[str, Any]:
    if coupling < 0.0:
        raise ValueError("coupling must be non-negative")
    if params.dt <= 0.0 or params.horizon <= 0.0:
        raise ValueError("dt and horizon must be positive")

    floor = np.asarray(scenario.floor, dtype=float)
    decay = np.asarray(scenario.decay, dtype=float)
    supply = np.asarray(scenario.supply, dtype=float)
    x0 = np.asarray(scenario.initial, dtype=float)

    steps = int(round(params.horizon / params.dt)) + 1
    times = np.arange(steps, dtype=float) * params.dt
    x = np.empty((steps, 3), dtype=float)
    targets = np.empty((steps, 3), dtype=float)
    controls = np.zeros((steps - 1, 3), dtype=float)
    x[0] = x0

    first_failure_time: float | None = None
    clipped_step_count = 0
    clipped_coordinate_count = 0

    for k in range(steps - 1):
        t = float(times[k])
        target = target_at(t, scenario)
        targets[k] = target
        u = control_action(x[k], target, floor, params, controller_enabled)
        controls[k] = u

        mean_state = float(np.mean(x[k]))
        coupling_flow = coupling * (mean_state - x[k])
        dx = supply - decay * x[k] + u + coupling_flow + disturbance_at(t, scenario)

        raw_next = x[k] + params.dt * dx
        clipped_mask = (raw_next < 0.0) | (raw_next > 1.0)
        if bool(np.any(clipped_mask)):
            clipped_step_count += 1
            clipped_coordinate_count += int(np.count_nonzero(clipped_mask))
        x[k + 1] = np.clip(raw_next, 0.0, 1.0)

        if first_failure_time is None and bool(np.any(x[k + 1] < floor)):
            first_failure_time = float(times[k + 1])

    targets[-1] = target_at(float(times[-1]), scenario)
    margin_matrix = x - floor[None, :]
    margin_series = np.min(margin_matrix, axis=1)
    viable_series = np.all(margin_matrix >= 0.0, axis=1)
    late_mask = times >= params.late_window_start

    flat_index = int(np.argmin(margin_matrix))
    time_index, component_index = np.unravel_index(flat_index, margin_matrix.shape)
    state_at_minimum = x[time_index]
    mean_at_minimum = float(np.mean(state_at_minimum))
    component_at_minimum = float(state_at_minimum[component_index])
    direct_coupling_at_minimum = float(
        coupling * (mean_at_minimum - component_at_minimum)
    )

    binding_indices = np.flatnonzero(
        np.isclose(
            margin_matrix[time_index],
            margin_matrix[time_index, component_index],
            rtol=0.0,
            atol=1e-12,
        )
    )

    total_control_cost = float(np.sum(controls) * params.dt)
    late_tracking_rmse = float(
        np.sqrt(np.mean(np.square(x[late_mask] - targets[late_mask])))
    )

    return {
        "scenario": scenario.name,
        "coupling": float(coupling),
        "controller_enabled": bool(controller_enabled),
        "minimum_viability_margin": float(np.min(margin_series)),
        "minimum_margin_time": float(times[time_index]),
        "minimum_margin_component": int(component_index + 1),
        "binding_components_at_minimum": [int(i + 1) for i in binding_indices],
        "state_at_minimum_margin": [float(v) for v in state_at_minimum],
        "mean_state_at_minimum_margin": mean_at_minimum,
        "direct_coupling_contribution_to_binding_component": direct_coupling_at_minimum,
        "binding_component_above_mean": bool(component_at_minimum > mean_at_minimum),
        "viability_fraction": float(np.mean(viable_series)),
        "first_failure_time": first_failure_time,
        "total_control_cost": total_control_cost,
        "late_tracking_rmse": late_tracking_rmse,
        "clipped_step_count": int(clipped_step_count),
        "clipped_coordinate_count": int(clipped_coordinate_count),
        "final_state": [float(v) for v in x[-1]],
        "final_target": [float(v) for v in targets[-1]],
    }


def scenario_record(scenario: Scenario) -> dict[str, Any]:
    return {
        **asdict(scenario),
        "uncoupled_natural_equilibrium": [
            float(s / d) for s, d in zip(scenario.supply, scenario.decay)
        ],
    }


def run_step_size_sweep(
    scenario: Scenario,
    trend: str,
) -> tuple[list[dict[str, Any]], bool]:
    records: list[dict[str, Any]] = []
    all_pass = True
    for dt in STEP_SIZE_SWEEP:
        params = NumericalParameters(dt=dt)
        runs = [simulate(c, params, scenario, True) for c in COUPLING_SWEEP]
        margins = np.asarray([r["minimum_viability_margin"] for r in runs])
        costs = np.asarray([r["total_control_cost"] for r in runs])
        tracking = np.asarray([r["late_tracking_rmse"] for r in runs])
        if trend == "primary":
            checks = {
                "margin_strictly_increases": bool(np.all(np.diff(margins) > 0.0)),
                "cost_strictly_increases": bool(np.all(np.diff(costs) > 0.0)),
                "late_tracking_error_strictly_increases": bool(
                    np.all(np.diff(tracking) > 0.0)
                ),
                "no_clipping": bool(
                    all(r["clipped_step_count"] == 0 for r in runs)
                ),
            }
        elif trend == "adverse":
            checks = {
                "margin_strictly_decreases": bool(np.all(np.diff(margins) < 0.0)),
                "kappa_0_remains_viable": bool(margins[0] > 0.0),
                "kappa_0_25_is_nonviable": bool(margins[5] < 0.0),
                "no_clipping": bool(
                    all(r["clipped_step_count"] == 0 for r in runs)
                ),
            }
        else:
            raise ValueError(f"unknown trend class: {trend}")

        passed = all(checks.values())
        all_pass = all_pass and passed
        records.append(
            {
                "dt": float(dt),
                "minimum_margin_at_kappa_0": float(margins[0]),
                "minimum_margin_at_kappa_0_8": float(margins[-1]),
                "control_cost_at_kappa_0": float(costs[0]),
                "control_cost_at_kappa_0_8": float(costs[-1]),
                "late_tracking_rmse_at_kappa_0": float(tracking[0]),
                "late_tracking_rmse_at_kappa_0_8": float(tracking[-1]),
                "trend_checks": checks,
            }
        )
    return records, all_pass


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_results() -> dict[str, Any]:
    params = NumericalParameters()
    primary_runs = [
        simulate(c, params, PRIMARY_SCENARIO, controller_enabled=True)
        for c in COUPLING_SWEEP
    ]
    adverse_runs = [
        simulate(c, params, ADVERSE_SCENARIO, controller_enabled=True)
        for c in COUPLING_SWEEP
    ]
    no_controller = simulate(
        0.0, params, PRIMARY_SCENARIO, controller_enabled=False
    )

    primary_margins = np.asarray(
        [r["minimum_viability_margin"] for r in primary_runs]
    )
    primary_costs = np.asarray([r["total_control_cost"] for r in primary_runs])
    primary_tracking = np.asarray([r["late_tracking_rmse"] for r in primary_runs])
    adverse_margins = np.asarray(
        [r["minimum_viability_margin"] for r in adverse_runs]
    )

    primary_sensitivity, primary_sensitivity_pass = run_step_size_sweep(
        PRIMARY_SCENARIO, "primary"
    )
    adverse_sensitivity, adverse_sensitivity_pass = run_step_size_sweep(
        ADVERSE_SCENARIO, "adverse"
    )

    checks = {
        "primary_all_controller_runs_remain_viable": bool(
            np.all(primary_margins >= 0.0)
        ),
        "primary_margin_strictly_increases_over_sweep": bool(
            np.all(np.diff(primary_margins) > 0.0)
        ),
        "primary_cost_strictly_increases_over_sweep": bool(
            np.all(np.diff(primary_costs) > 0.0)
        ),
        "primary_late_tracking_error_strictly_increases_over_sweep": bool(
            np.all(np.diff(primary_tracking) > 0.0)
        ),
        "primary_controller_runs_have_no_clipping": bool(
            all(r["clipped_step_count"] == 0 for r in primary_runs)
        ),
        "primary_no_controller_run_crosses_viability_floor": bool(
            no_controller["minimum_viability_margin"] < 0.0
        ),
        "primary_no_controller_failure_is_recorded": bool(
            no_controller["first_failure_time"] is not None
        ),
        "primary_step_size_sweeps_preserve_reported_trends": bool(
            primary_sensitivity_pass
        ),
        "adverse_margin_strictly_decreases_over_sweep": bool(
            np.all(np.diff(adverse_margins) < 0.0)
        ),
        "adverse_kappa_0_is_viable": bool(adverse_margins[0] > 0.0),
        "adverse_kappa_0_25_is_nonviable": bool(adverse_margins[5] < 0.0),
        "adverse_sweep_contains_viable_and_nonviable_runs": bool(
            np.any(adverse_margins > 0.0) and np.any(adverse_margins < 0.0)
        ),
        "adverse_positive_couplings_drain_binding_component_at_minimum": bool(
            all(
                r["direct_coupling_contribution_to_binding_component"] < 0.0
                for r in adverse_runs[1:]
            )
        ),
        "adverse_binding_component_is_component_3": bool(
            all(r["minimum_margin_component"] == 3 for r in adverse_runs)
        ),
        "adverse_controller_runs_have_no_clipping": bool(
            all(r["clipped_step_count"] == 0 for r in adverse_runs)
        ),
        "adverse_step_size_sweeps_preserve_reported_trends": bool(
            adverse_sensitivity_pass
        ),
    }

    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"Regression checks failed: {failed}")

    equations = {
        "state_update": (
            "x[k+1] = clip(x[k] + dt*(supply - decay*x[k] + u[k] "
            "+ kappa*(mean(x[k])-x[k]) + disturbance[k]), 0, 1)"
        ),
        "unconstrained_control": "u_desired = max(0, gain*(target-x))",
        "budgeted_control": (
            "u_i = B*w_i/sum_j(w_j), w_i = exp(-s*(x_i-floor_i))*"
            "(0.15+max(target_i-x_i,0))"
        ),
        "minimum_margin_directional_derivative": (
            "D M(x)[c] = min_{i in I(x)} kappa*(mean(x)-x_i); "
            "for a unique binding component j this is kappa*(mean(x)-x_j)"
        ),
    }

    result: dict[str, Any] = {
        "artifact": "CU Biology C.1.1 illustrative viability-control models",
        "status": (
            "Pedagogical deterministic models; not fitted to biological data "
            "and not empirical validation of Coherence Universalism."
        ),
        "software": {
            "python": platform.python_version(),
            "numpy": np.__version__,
        },
        "numerical_parameters": asdict(params),
        "coupling_sweep": list(COUPLING_SWEEP),
        "step_size_sweep": list(STEP_SIZE_SWEEP),
        "equations": equations,
        "primary_configuration": {
            "scenario": scenario_record(PRIMARY_SCENARIO),
            "controller_runs": primary_runs,
            "step_size_sensitivity": primary_sensitivity,
            "no_controller_reference": no_controller,
        },
        "adverse_configuration": {
            "scenario": scenario_record(ADVERSE_SCENARIO),
            "controller_runs": adverse_runs,
            "step_size_sensitivity": adverse_sensitivity,
        },
        "regression_checks": checks,
        "interpretation": {
            "supported": [
                "The direct effect of diffusive coupling on a unique binding component has sign kappa*(mean(x)-x_j).",
                "In the homogeneous-floor configuration, sampled minimum margin increases while cost and differentiated tracking error also increase.",
                "The homogeneous-floor sweep remains well inside the viable region and demonstrates margin redistribution, not coupling-mediated rescue.",
                "In the heterogeneous-floor configuration, sampled minimum margin decreases and crosses zero as coupling increases.",
                "The same coupling operator can therefore support or undermine viability depending on the declared floors, state distribution, controller, disturbances, and horizon.",
            ],
            "not_supported": [
                "Neither configuration establishes a universal biological law.",
                "The local directional lemma does not by itself determine monotonicity of a finite controlled trajectory as coupling changes.",
                "The models do not estimate an optimal coupling for any organism.",
                "The models do not validate a universal biological coherence scalar.",
            ],
        },
    }

    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["content_sha256_without_hash_field"] = sha256_text(canonical)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name(
            "CU_Biology_C1_1_verification_results.json"
        ),
        help="Path for deterministic JSON output.",
    )
    args = parser.parse_args()

    result = build_results()
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {args.output}")
    print("All regression checks passed.")


if __name__ == "__main__":
    main()
