#!/usr/bin/env python3
"""Reproducibility suite for CU Physics systematic reconstruction A.6.1.

This script independently verifies the A.6 results, applies the A.6.1 audit repair, and reconstructs the
numerical checks inherited from the public Coherence Field verification code.
It writes a deterministic JSON report by default.

Requirements: Python 3.10+, NumPy, SciPy.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence

import numpy as np
import scipy
from scipy.fft import fft, fftfreq, ifft
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, minimize_scalar
from scipy.stats import spearmanr

DEFAULT_SEED = 20260909


def _jsonable(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(v) for v in value]
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, (np.floating, np.integer)):
        return value.item()
    return value


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def shannon(p: np.ndarray, axis: int = -1) -> np.ndarray:
    p = np.asarray(p, dtype=float)
    terms = np.where(p > 0.0, -p * np.log(p), 0.0)
    return np.sum(terms, axis=axis)


def differentiation(p: np.ndarray, axis: int = -1) -> np.ndarray:
    p = np.asarray(p, dtype=float)
    n = p.shape[axis]
    return np.sum((p - 1.0 / n) ** 2, axis=axis)


def binary_entropy(t: np.ndarray) -> np.ndarray:
    t = np.asarray(t, dtype=float)
    out = np.zeros_like(t)
    mask = (t > 0.0) & (t < 1.0)
    out[mask] = -t[mask] * np.log(t[mask]) - (1.0 - t[mask]) * np.log(1.0 - t[mask])
    return out


def block_average(p: np.ndarray, blocks: Sequence[Sequence[int]]) -> np.ndarray:
    p = np.asarray(p, dtype=float)
    out = np.zeros_like(p)
    for block in blocks:
        idx = np.asarray(block, dtype=int)
        out[..., idx] = np.sum(p[..., idx], axis=-1, keepdims=True) / len(block)
    return out


def verify_block_theorems(rng: np.random.Generator, samples: int) -> dict[str, Any]:
    p = rng.dirichlet(np.ones(4), size=samples)
    q_a = p[:, 0] + p[:, 1]
    q_b = p[:, 2] + p[:, 3]
    q = np.column_stack([q_a, q_b])
    p_tilde = np.column_stack([q_a / 2.0, q_a / 2.0, q_b / 2.0, q_b / 2.0])

    d_fine = differentiation(p)
    d_coarse_normalized = 0.5 * np.sum((q - 0.5) ** 2, axis=1)
    d_within = 0.5 * ((p[:, 0] - p[:, 1]) ** 2 + (p[:, 2] - p[:, 3]) ** 2)

    t_a = p[:, 0] / q_a
    t_b = p[:, 2] / q_b
    s_within = q_a * binary_entropy(t_a) + q_b * binary_entropy(t_b)
    s_grouped = shannon(q) + s_within
    entropy_gain_formula = np.log(2.0) - s_within

    d_residual_1 = d_fine - d_coarse_normalized - d_within
    d_residual_2 = differentiation(p) - differentiation(p_tilde) - d_within
    s_grouping_residual = shannon(p) - s_grouped
    s_gain_residual = shannon(p_tilde) - shannon(p) - entropy_gain_formula

    corr_hidden_within = float(np.corrcoef(d_within, s_within)[0, 1])
    corr_hidden_gain = float(np.corrcoef(d_within, entropy_gain_formula)[0, 1])
    spearman_hidden_gain = float(spearmanr(d_within, entropy_gain_formula).statistic)

    # General finite-partition theorem on a six-state simplex.
    p6 = rng.dirichlet(np.ones(6), size=samples)
    blocks = ([0, 1, 2], [3, 4], [5])
    e6 = block_average(p6, blocks)
    within6 = np.zeros(samples)
    entropy_gain6 = np.zeros(samples)
    for block in blocks:
        idx = np.asarray(block)
        q_bk = np.sum(p6[:, idx], axis=1)
        mean = q_bk[:, None] / len(block)
        within6 += np.sum((p6[:, idx] - mean) ** 2, axis=1)
        if len(block) > 1:
            r = p6[:, idx] / q_bk[:, None]
            entropy_gain6 += q_bk * (math.log(len(block)) - shannon(r))
    general_d_residual = differentiation(p6) - differentiation(e6) - within6
    general_s_residual = shannon(e6) - shannon(p6) - entropy_gain6

    return {
        "samples": samples,
        "two_block_max_abs_residuals": {
            "differentiation_decomposition": float(np.max(np.abs(d_residual_1))),
            "block_average_differentiation_loss": float(np.max(np.abs(d_residual_2))),
            "shannon_grouping": float(np.max(np.abs(s_grouping_residual))),
            "block_average_entropy_gain": float(np.max(np.abs(s_gain_residual))),
        },
        "minimum_entropy_gain": float(np.min(entropy_gain_formula)),
        "sampling_dependent_correlations_dirichlet_1": {
            "pearson_hidden_differentiation_vs_within_entropy": corr_hidden_within,
            "pearson_hidden_differentiation_vs_entropy_gain": corr_hidden_gain,
            "spearman_hidden_differentiation_vs_entropy_gain": spearman_hidden_gain,
            "note": "These correlations depend on the sampling measure and are not framework invariants.",
        },
        "six_state_partition_max_abs_residuals": {
            "differentiation_loss": float(np.max(np.abs(general_d_residual))),
            "entropy_gain": float(np.max(np.abs(general_s_residual))),
        },
    }


def fisher_fields(p: np.ndarray) -> tuple[np.ndarray, np.ndarray, float, float, float]:
    p = np.asarray(p, dtype=float)
    q2 = float(np.dot(p, p))
    s = float(shannon(p))
    a = 2.0 * p * (p - q2)
    b = p * (-np.log(p) - s)
    aa = float(np.sum(a * a / p))
    bb = float(np.sum(b * b / p))
    pi = float(-np.sum(a * b / p))
    return a, b, aa, bb, pi


def wedge_values(p: np.ndarray) -> tuple[float, float, float, float]:
    _, _, aa, bb, pi = fisher_fields(p)
    if aa <= 0.0 or bb <= 0.0 or pi <= 0.0:
        return math.nan, math.nan, math.nan, math.nan
    chi = pi / math.sqrt(aa * bb)
    lower = pi / bb
    upper = aa / pi
    return lower, upper, chi, upper - lower


def euclidean_fields(p: np.ndarray) -> tuple[np.ndarray, np.ndarray, float, float, float]:
    p = np.asarray(p, dtype=float)
    n = p.size
    x = 2.0 * (p - 1.0 / n)
    y = -np.log(p) + float(np.mean(np.log(p)))
    xx = float(np.dot(x, x))
    yy = float(np.dot(y, y))
    pi = float(-np.dot(x, y))
    return x, y, xx, yy, pi


def euclidean_wedge_values(p: np.ndarray) -> tuple[float, float, float, float]:
    _, _, xx, yy, pi = euclidean_fields(p)
    if xx <= 0.0 or yy <= 0.0 or pi <= 0.0:
        return math.nan, math.nan, math.nan, math.nan
    chi = pi / math.sqrt(xx * yy)
    lower = pi / yy
    upper = xx / pi
    return lower, upper, chi, upper - lower


def two_level_distribution(n: int, multiplicity: int, high_mass: float) -> np.ndarray:
    if not (1 <= multiplicity < n):
        raise ValueError("multiplicity must lie between 1 and n-1")
    a = high_mass / multiplicity
    b = (1.0 - high_mass) / (n - multiplicity)
    return np.array([a] * multiplicity + [b] * (n - multiplicity), dtype=float)


def verify_wedge(rng: np.random.Generator, samples: int) -> dict[str, Any]:
    # Random points almost surely avoid the exact lower-dimensional collapse set.
    ps = rng.dirichlet(np.ones(4), size=samples)
    widths = np.empty(samples)
    chis = np.empty(samples)
    euclidean_widths = np.empty(samples)
    euclidean_chis = np.empty(samples)
    violations = 0
    euclidean_violations = 0
    for i, p in enumerate(ps):
        lower, upper, chi, width = wedge_values(p)
        widths[i] = width
        chis[i] = chi
        if not (lower <= upper + 5e-13 and chi <= 1.0 + 5e-13):
            violations += 1
        e_lower, e_upper, e_chi, e_width = euclidean_wedge_values(p)
        euclidean_widths[i] = e_width
        euclidean_chis[i] = e_chi
        if not (e_lower <= e_upper + 5e-13 and e_chi <= 1.0 + 5e-13):
            euclidean_violations += 1

    # Exact two-level families: A and B are antiparallel and the wedge closes.
    two_level_rows = []
    max_abs_width = 0.0
    max_one_minus_chi = 0.0
    euclidean_max_abs_width = 0.0
    euclidean_max_one_minus_chi = 0.0
    for multiplicity in (1, 2, 3):
        baseline = multiplicity / 4.0
        masses = np.linspace(baseline + 1e-4, 1.0 - (4 - multiplicity) * 1e-4, 250)
        for mass in masses:
            p = two_level_distribution(4, multiplicity, float(mass))
            lower, upper, chi, width = wedge_values(p)
            max_abs_width = max(max_abs_width, abs(width))
            max_one_minus_chi = max(max_one_minus_chi, abs(1.0 - chi))
            e_lower, e_upper, e_chi, e_width = euclidean_wedge_values(p)
            euclidean_max_abs_width = max(euclidean_max_abs_width, abs(e_width))
            euclidean_max_one_minus_chi = max(euclidean_max_one_minus_chi, abs(1.0 - e_chi))
        # Representative row.
        mass = baseline + 0.65 * (1.0 - baseline)
        p = two_level_distribution(4, multiplicity, mass)
        a = p[0]
        b = p[-1]
        lower, upper, chi, width = wedge_values(p)
        critical = 2.0 * (a - b) / math.log(a / b)
        e_lower, e_upper, e_chi, e_width = euclidean_wedge_values(p)
        two_level_rows.append({
            "multiplicity_of_a": multiplicity,
            "a": float(a),
            "b": float(b),
            "fisher_lower": lower,
            "fisher_upper": upper,
            "euclidean_lower": e_lower,
            "euclidean_upper": e_upper,
            "critical_ratio_formula": critical,
            "fisher_chi": chi,
            "euclidean_chi": e_chi,
        })

    # Near the full-support uniform state along a generic direction.
    direction = np.array([1.7, 0.4, -0.8, -1.3], dtype=float)
    direction -= np.mean(direction)
    direction /= np.max(np.abs(direction))
    near_uniform = []
    for eps in (1e-2, 1e-3, 1e-4, 1e-5):
        p = np.full(4, 0.25) + eps * direction
        lower, upper, chi, width = wedge_values(p)
        near_uniform.append({
            "epsilon": eps,
            "lower": lower,
            "upper": upper,
            "width": width,
            "chi": chi,
        })

    # Demonstrate that a commonly used symmetric ray is exactly degenerate.
    symmetric_ray = []
    for x in (0.40, 0.55, 0.70, 0.82, 0.95):
        p = np.array([x, (1.0 - x) / 3.0, (1.0 - x) / 3.0, (1.0 - x) / 3.0])
        lower, upper, chi, width = wedge_values(p)
        rc = 2.0 * (p[0] - p[1]) / math.log(p[0] / p[1])
        symmetric_ray.append({
            "x": x,
            "critical_ratio": rc,
            "lower": lower,
            "upper": upper,
            "width": width,
            "chi": chi,
        })

    return {
        "random_samples": samples,
        "fisher_random_numerical_violations": violations,
        "fisher_random_min_width": float(np.min(widths)),
        "fisher_random_max_chi": float(np.max(chis)),
        "euclidean_random_numerical_violations": euclidean_violations,
        "euclidean_random_min_width": float(np.min(euclidean_widths)),
        "euclidean_random_max_chi": float(np.max(euclidean_chis)),
        "fisher_two_level_family_max_abs_width": max_abs_width,
        "fisher_two_level_family_max_abs_one_minus_chi": max_one_minus_chi,
        "euclidean_two_level_family_max_abs_width": euclidean_max_abs_width,
        "euclidean_two_level_family_max_abs_one_minus_chi": euclidean_max_one_minus_chi,
        "two_level_representatives": two_level_rows,
        "near_uniform_generic_direction": near_uniform,
        "symmetric_one_plus_three_ray": symmetric_ray,
        "theorem": (
            "For nonuniform interior p, the wedge is strict iff p has at least three distinct "
            "probability values. It collapses exactly when p has only two distinct values; "
            "at the uniform point both gradients vanish."
        ),
    }


def verify_fixed_coupling_structure() -> dict[str, Any]:
    """Verify the fixed-coupling stationary-point results added in A.6.1.

    Geometric wedge collapse is independent of the chosen coupling ratio.  At a
    fixed ratio r=beta/alpha, only two-level states whose collapsed edge equals r
    are stationary for the combined ascent field.
    """

    def one_plus_three_stationarity(q: float) -> float:
        return q * q + 2.0 * q - 3.0 - 4.0 * q * math.log(q)

    q_star = float(brentq(one_plus_three_stationarity, 2.0, 10.0, xtol=5e-15, rtol=1e-14))
    a_star = q_star / (q_star + 3.0)
    b_star = 1.0 / (q_star + 3.0)
    r_star = 2.0 * (a_star - b_star) / math.log(a_star / b_star)

    # At the uniform state, the Euclidean tangent linearization is
    # (2 alpha - 4 beta) I and the Fisher linearization is one quarter of it.
    # The critical ratio is therefore exactly 1/2.
    uniform_ratio = 0.5

    # At the critical ratio, the quadratic term cancels.  Along
    # delta=(3e,-e,-e,-e), the leading objective difference is 32 alpha e^3,
    # proving that uniformity is neither a local maximum nor a local minimum.
    eps = 1.0e-5
    u = np.full(4, 0.25)
    delta = eps * np.array([3.0, -1.0, -1.0, -1.0])

    def objective(p_vec: np.ndarray, ratio: float) -> float:
        return float(differentiation(p_vec) + ratio * shannon(p_vec))

    critical_plus = objective(u + delta, uniform_ratio) - objective(u, uniform_ratio)
    critical_minus = objective(u - delta, uniform_ratio) - objective(u, uniform_ratio)

    return {
        "fixed_coupling_distinction": (
            "The geometric wedge-collapse set remains the continuous two-level set. "
            "At fixed beta/alpha, the nonuniform stationary states are only its finite "
            "intersection with r=2(a-b)/log(a/b)."
        ),
        "uniform_linear_stability_threshold": uniform_ratio,
        "uniform_euclidean_linear_rate_for_alpha_1": "2 - 4 r",
        "uniform_fisher_linear_rate_for_alpha_1": "0.5 - r",
        "critical_ratio_classification": (
            "At r=1/2 the Hessian vanishes on the tangent space; for Delta_4 the cubic "
            "term is generically nonzero, so uniformity is neither a local maximum nor minimum."
        ),
        "critical_direction_epsilon": eps,
        "critical_direction_objective_difference_plus": critical_plus,
        "critical_direction_objective_difference_minus": critical_minus,
        "two_level_stationary_threshold": {
            "value": r_star,
            "q_equals_a_over_b": q_star,
            "a": a_star,
            "b": b_star,
            "multiplicity": "one a and three b",
            "stationarity_equation_residual": one_plus_three_stationarity(q_star),
            "interpretation": (
                "For r above this value, the uniform state is the only interior stationary "
                "point of the combined four-state flow. Two-level states still geometrically "
                "collapse the joint-growth wedge, but the fixed-r vector field does not vanish there."
            ),
        },
        "other_multiplicity_suprema": {
            "two_plus_two": {"supremum": 0.5, "attainment": "uniform limit only"},
            "three_plus_one": {"supremum": 0.5, "attainment": "uniform limit only"},
        },
    }


def metric_values_two_level(k: int, m: int, mass_a: float) -> tuple[float, float, float]:
    p = two_level_distribution(k, m, mass_a)
    q2 = float(np.dot(p, p))
    s = float(shannon(p))
    a = 2.0 * p * (p - q2)
    b = p * (-np.log(p) - s)
    aa = float(np.sum(a * a / p))
    bb = float(np.sum(b * b / p))
    pi = float(-np.sum(a * b / p))
    return math.sqrt(max(0.0, aa)), math.sqrt(max(0.0, bb)), pi


def maximize_over_supports(index: int) -> tuple[float, dict[str, Any], list[dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    best_value = -math.inf
    best: dict[str, Any] = {}
    for k in range(2, 5):
        for m in range(1, k):
            result = minimize_scalar(
                lambda z: -metric_values_two_level(k, m, z)[index],
                bounds=(1e-11, 1.0 - 1e-11),
                method="bounded",
                options={"xatol": 1e-14, "maxiter": 2000},
            )
            mass_a = float(result.x)
            value = float(-result.fun)
            a = mass_a / m
            b = (1.0 - mass_a) / (k - m)
            row = {
                "support_size": k,
                "multiplicity_a": m,
                "total_mass_a": mass_a,
                "a": a,
                "b": b,
                "value": value,
            }
            rows.append(row)
            if value > best_value:
                best_value = value
                best = row.copy()
    return best_value, best, rows


def verify_fisher_constants() -> dict[str, Any]:
    # Keep the exhaustive support/multiplicity scan as an independently inspectable
    # global comparison, but evaluate the winning one-plus-three family from its
    # exact or bracketing-root stationarity equation.
    scan_a, scan_arg_a, rows_a = maximize_over_supports(0)
    scan_b, scan_arg_b, rows_b = maximize_over_supports(1)
    scan_pi, scan_arg_pi, rows_pi = maximize_over_supports(2)

    x_a = (7.0 + math.sqrt(33.0)) / 16.0
    y_a = (1.0 - x_a) / 3.0
    a_sq_exact = 23.0 / 128.0 + 11.0 * math.sqrt(33.0) / 384.0
    max_a = math.sqrt(a_sq_exact)

    def b_equation(x: float) -> float:
        return (2.0 * x - 1.0) * math.log(3.0 * x / (1.0 - x)) - 2.0

    def pi_equation(x: float) -> float:
        log_ratio = math.log(3.0 * x / (1.0 - x))
        return (12.0 * x * x - 10.0 * x + 1.0) * log_ratio - (4.0 * x - 1.0)

    x_b = float(brentq(b_equation, 0.75, 0.95, xtol=5e-15, rtol=1e-14))
    y_b = (1.0 - x_b) / 3.0
    max_b = metric_values_two_level(4, 1, x_b)[1]

    x_pi = float(brentq(pi_equation, 0.75, 0.90, xtol=5e-15, rtol=1e-14))
    y_pi = (1.0 - x_pi) / 3.0
    max_pi = metric_values_two_level(4, 1, x_pi)[2]

    return {
        "global_reduction_note": (
            "Interior KKT equations force at most two distinct positive probability values; "
            "all support sizes and multiplicities through n=4 were optimized in one dimension. "
            "The winning one-plus-three family was then evaluated from its exact or bracketing-root equation."
        ),
        "sup_norm_A": {
            "value": max_a,
            "argmax": {
                "support_size": 4,
                "multiplicity_a": 1,
                "total_mass_a": x_a,
                "a": x_a,
                "b": y_a,
                "value": max_a,
            },
            "exact_large_probability": x_a,
            "exact_squared_value": a_sq_exact,
            "scan_value": scan_a,
            "scan_argmax": scan_arg_a,
            "scan_residual": abs(scan_a - max_a),
        },
        "sup_norm_B": {
            "value": max_b,
            "argmax": {
                "support_size": 4,
                "multiplicity_a": 1,
                "total_mass_a": x_b,
                "a": x_b,
                "b": y_b,
                "value": max_b,
            },
            "stationarity_residual": b_equation(x_b),
            "scan_value": scan_b,
            "scan_argmax": scan_arg_b,
            "scan_residual": abs(scan_b - max_b),
        },
        "sup_Pi_F": {
            "value": max_pi,
            "argmax": {
                "support_size": 4,
                "multiplicity_a": 1,
                "total_mass_a": x_pi,
                "a": x_pi,
                "b": y_pi,
                "value": max_pi,
            },
            "stationarity_residual": pi_equation(x_pi),
            "scan_value": scan_pi,
            "scan_argmax": scan_arg_pi,
            "scan_residual": abs(scan_pi - max_pi),
        },
        "all_reduced_cases": {
            "norm_A": rows_a,
            "norm_B": rows_b,
            "Pi_F": rows_pi,
        },
    }


def wave_force(c: np.ndarray, kappa: float = 1.0) -> np.ndarray:
    return 2.0 * kappa * (np.roll(c, -1) - 2.0 * c + np.roll(c, 1))


def wave_leapfrog(c: np.ndarray, momentum: np.ndarray, dt: float, kappa: float = 1.0) -> tuple[np.ndarray, np.ndarray]:
    half = momentum + 0.5 * dt * wave_force(c, kappa)
    c_new = c + dt * half
    p_new = half + 0.5 * dt * wave_force(c_new, kappa)
    return c_new, p_new


def wave_measure_omega(mode: int, n: int, kappa: float, total_time: float, dt: float) -> float:
    k = 2.0 * math.pi * mode / n
    sites = np.arange(n)
    c = np.cos(k * sites)
    momentum = np.zeros(n)
    n_steps = int(total_time / dt)
    record = np.empty(n_steps + 1)
    record[0] = c[0]
    for step in range(n_steps):
        c, momentum = wave_leapfrog(c, momentum, dt, kappa)
        record[step + 1] = c[0]
    amplitudes = np.abs(np.fft.rfft(record))
    frequencies = np.fft.rfftfreq(record.size, d=dt)
    peak = int(np.argmax(amplitudes[1:]) + 1)
    return float(2.0 * math.pi * frequencies[peak])


def wave_energy_audit(mode: int, n: int = 128, kappa: float = 1.0, total_time: float = 100.0, dt: float = 0.01) -> dict[str, float]:
    k = 2.0 * math.pi * mode / n
    sites = np.arange(n)
    c = np.cos(k * sites)
    momentum = np.zeros(n)
    correct = []
    wrong = []
    steps = int(total_time / dt)
    for _ in range(steps + 1):
        diff = np.roll(c, -1) - c
        correct.append(0.5 * np.sum(momentum**2) + kappa * np.sum(diff**2))
        wrong.append(0.5 * np.sum(momentum**2) - kappa * np.sum(diff**2))
        c, momentum = wave_leapfrog(c, momentum, dt, kappa)
    correct = np.asarray(correct)
    wrong = np.asarray(wrong)
    return {
        "mode": mode,
        "correct_max_relative_deviation": float(np.max(np.abs(correct / correct[0] - 1.0))),
        "wrong_max_relative_deviation": float(np.max(np.abs(wrong / wrong[0] - 1.0))),
    }


def verify_wave() -> dict[str, Any]:
    n = 128
    kappa = 1.0
    total_time = 200.0
    dt = 0.05
    modes = [3, 6, 10, 15, 20, 25, 32, 40, 48, 56, 60, 63]
    rows = []
    for mode in modes:
        measured = wave_measure_omega(mode, n, kappa, total_time, dt)
        k = 2.0 * math.pi * mode / n
        exact = 2.0 * math.sqrt(2.0 * kappa) * abs(math.sin(k / 2.0))
        rows.append({
            "mode": mode,
            "k_over_pi": 2.0 * mode / n,
            "measured_omega": measured,
            "exact_omega": exact,
            "relative_error": abs(measured - exact) / exact,
        })
    return {
        "parameters": {"N": n, "kappa": kappa, "T": total_time, "dt": dt},
        "dispersion_rows": rows,
        "max_relative_error": max(r["relative_error"] for r in rows),
        "energy_checks": [wave_energy_audit(1), wave_energy_audit(63)],
        "sign_conclusion": (
            "The stable equation follows from positive potential V=kappa*sum(delta C)^2 "
            "for the companion coefficient convention; the printed negative potential has the wrong sign."
        ),
    }


def madelung_run(n: int, total_time: float = 5.0, dt: float = 0.001, check_every: int = 100) -> dict[str, Any]:
    length = 40.0
    x = np.linspace(-length / 2.0, length / 2.0, n, endpoint=False)
    dx = length / n
    k = 2.0 * math.pi * fftfreq(n, dx)
    hbar = 1.0
    mass = 1.0
    v_ext = 0.5 * x**2

    def grad(f: np.ndarray) -> np.ndarray:
        return (np.roll(f, -1) - np.roll(f, 1)) / (2.0 * dx)

    def lap_fft(f: np.ndarray) -> np.ndarray:
        return np.real(ifft(-(k**2) * fft(f)))

    def rhs(psi: np.ndarray) -> np.ndarray:
        psi_xx = ifft(-(k**2) * fft(psi))
        return (1j * hbar / (2.0 * mass)) * psi_xx - (1j / hbar) * v_ext * psi

    def step(psi: np.ndarray) -> np.ndarray:
        psi = psi * np.exp(-1j * v_ext * dt / (2.0 * hbar))
        psi_k = fft(psi) * np.exp(-1j * hbar * k**2 * dt / (2.0 * mass))
        psi = ifft(psi_k)
        return psi * np.exp(-1j * v_ext * dt / (2.0 * hbar))

    x0, sigma0, k0 = -1.5, 0.8, 0.5
    psi = (1.0 / (2.0 * math.pi * sigma0**2)) ** 0.25 * np.exp(
        -(x - x0) ** 2 / (4.0 * sigma0**2)
    ) * np.exp(1j * k0 * x)
    psi = psi / math.sqrt(float(np.sum(np.abs(psi) ** 2) * dx))

    continuity: list[float] = []
    hj: list[float] = []
    norms: list[float] = []
    energies: list[float] = []
    kinetic_values: list[float] = []
    potential_values: list[float] = []

    n_steps = int(total_time / dt)
    for step_index in range(n_steps + 1):
        if step_index % check_every == 0:
            rho = np.abs(psi) ** 2
            grad_psi = ifft(1j * k * fft(psi))
            psi_reg = psi + 1e-30 * (psi == 0)
            grad_s = hbar * np.imag(grad_psi / psi_reg)
            dpsi_dt = rhs(psi)
            ratio = dpsi_dt / psi_reg
            drho_dt = 2.0 * rho * np.real(ratio)
            ds_dt = hbar * np.imag(ratio)
            continuity_residual = drho_dt + grad(rho * grad_s / mass)
            sqrt_rho = np.sqrt(rho + 1e-20)
            q_potential = -(hbar**2 / (2.0 * mass)) * lap_fft(sqrt_rho) / sqrt_rho
            hj_residual = ds_dt + grad_s**2 / (2.0 * mass) + v_ext + q_potential
            mask = rho > 1e-5
            continuity.append(float(np.max(np.abs(continuity_residual[mask]))))
            hj.append(float(np.max(np.abs(hj_residual[mask]))))

            norm = float(np.sum(rho) * dx)
            kinetic = float((hbar**2 / (2.0 * mass)) * np.sum(np.abs(grad_psi) ** 2) * dx)
            potential = float(np.sum(v_ext * rho) * dx)
            norms.append(norm)
            kinetic_values.append(kinetic)
            potential_values.append(potential)
            energies.append(kinetic + potential)
        psi = step(psi)

    continuity_arr = np.asarray(continuity)
    hj_arr = np.asarray(hj)
    norms_arr = np.asarray(norms)
    energies_arr = np.asarray(energies)
    kinetic_arr = np.asarray(kinetic_values)
    potential_arr = np.asarray(potential_values)
    virial_difference = abs(float(np.mean(kinetic_arr) - np.mean(potential_arr))) / (
        0.5 * float(np.mean(kinetic_arr) + np.mean(potential_arr))
    )
    return {
        "N": n,
        "dx": dx,
        "continuity_max": float(np.max(continuity_arr)),
        "continuity_median": float(np.median(continuity_arr)),
        "HJ_max": float(np.max(hj_arr)),
        "HJ_median": float(np.median(hj_arr)),
        "norm_max_relative_deviation": float(np.max(np.abs(norms_arr / norms_arr[0] - 1.0))),
        "energy_max_relative_deviation": float(np.max(np.abs(energies_arr / energies_arr[0] - 1.0))),
        "time_averaged_kinetic_potential_relative_difference": virial_difference,
    }


def verify_madelung() -> dict[str, Any]:
    rows = [madelung_run(n) for n in (256, 512, 1024)]
    convergence = []
    for left, right in zip(rows[:-1], rows[1:]):
        convergence.append(left["continuity_median"] / right["continuity_median"])
    return {
        "parameters": {
            "L": 40.0,
            "dt": 0.001,
            "T": 5.0,
            "hbar": 1.0,
            "mass": 1.0,
            "potential": "0.5*x^2",
            "initial_packet": {"x0": -1.5, "sigma0": 0.8, "k0": 0.5},
            "mask": "rho > 1e-5",
        },
        "grid_rows": rows,
        "continuity_median_refinement_factors": convergence,
        "interpretation": (
            "The HJ identity is evaluated using derivatives from the same Schrodinger RHS; "
            "the check is algebraic/discretization consistency, not independent empirical confirmation."
        ),
    }


def open_laplacian_force(c: np.ndarray, kappa: float = 1.0) -> np.ndarray:
    force = np.zeros_like(c)
    force[1:-1] = 2.0 * kappa * (c[2:] - 2.0 * c[1:-1] + c[:-2])
    force[0] = 2.0 * kappa * (c[1] - c[0])
    force[-1] = 2.0 * kappa * (c[-2] - c[-1])
    return force


def open_force_matrix(n: int, kappa: float = 1.0) -> np.ndarray:
    matrix = np.zeros((n, n), dtype=float)
    matrix[0, 0] = -2.0 * kappa
    matrix[0, 1] = 2.0 * kappa
    matrix[-1, -2] = 2.0 * kappa
    matrix[-1, -1] = -2.0 * kappa
    for i in range(1, n - 1):
        matrix[i, i - 1] = 2.0 * kappa
        matrix[i, i] = -4.0 * kappa
        matrix[i, i + 1] = 2.0 * kappa
    return matrix


def initial_chain(n: int, width: float = 2.0, amplitude: float = 1.0) -> np.ndarray:
    x = np.arange(n) - n / 2.0 + 0.5
    return amplitude * np.exp(-x**2 / (2.0 * width**2))


def overdamped_error(eta: float, n: int = 32, kappa: float = 1.0, total_time: float = 5.0) -> float:
    """Reproduce the legacy rest-initialized fixed-time comparison."""
    c0 = initial_chain(n)
    y0 = np.concatenate([c0, np.zeros(n)])

    def rhs_damped(_t: float, y: np.ndarray) -> np.ndarray:
        c, velocity = y[:n], y[n:]
        return np.concatenate([velocity, -eta * velocity + open_laplacian_force(c, kappa)])

    def rhs_first(_t: float, c: np.ndarray) -> np.ndarray:
        return open_laplacian_force(c, kappa) / eta

    sol_second = solve_ivp(rhs_damped, (0.0, total_time), y0, method="RK45", rtol=1e-10, atol=1e-12)
    sol_first = solve_ivp(rhs_first, (0.0, total_time), c0, method="RK45", rtol=1e-10, atol=1e-12)
    c_second = sol_second.y[:n, -1]
    c_first = sol_first.y[:, -1]
    difference = float(np.max(np.abs(c_second - c_first)))
    return difference / max(float(np.max(np.abs(c_second))), 1e-12)


def exact_linear_chain_comparison(
    eta: float,
    initialization: str,
    n: int = 32,
    kappa: float = 1.0,
    total_time: float = 5.0,
) -> dict[str, float]:
    """Compare the linear second-order chain with its leading overdamped flow.

    The extended A.6.1 sweep uses eta >= 10, above the critical damping of all
    modes for the stated chain.  A spectral solution avoids stiffness and makes
    the initialization dependence explicit.
    """
    force_matrix = open_force_matrix(n, kappa)
    eigenvalues, eigenvectors = np.linalg.eigh(force_matrix)
    omega_squared = np.maximum(-eigenvalues, 0.0)
    discriminant = eta * eta - 4.0 * omega_squared
    if np.min(discriminant) < -1e-12:
        raise ValueError("exact overdamped branch requires eta above every modal critical value")
    root = np.sqrt(np.maximum(discriminant, 0.0))
    slow_rate = np.where(
        omega_squared == 0.0,
        0.0,
        -2.0 * omega_squared / (eta + root),
    )
    fast_rate = -eta - slow_rate

    c0 = initial_chain(n)
    modal_position_0 = eigenvectors.T @ c0
    if initialization == "rest":
        modal_velocity_0 = np.zeros_like(modal_position_0)
    elif initialization == "leading_slow_manifold":
        modal_velocity_0 = -omega_squared * modal_position_0 / eta
    else:
        raise ValueError(f"unknown initialization: {initialization}")

    denominator = slow_rate - fast_rate
    slow_amplitude = (modal_velocity_0 - fast_rate * modal_position_0) / denominator
    fast_amplitude = (slow_rate * modal_position_0 - modal_velocity_0) / denominator
    exp_slow = np.exp(slow_rate * total_time)
    exp_fast = np.exp(fast_rate * total_time)
    modal_position_second = slow_amplitude * exp_slow + fast_amplitude * exp_fast
    modal_velocity_second = slow_rate * slow_amplitude * exp_slow + fast_rate * fast_amplitude * exp_fast

    modal_position_first = modal_position_0 * np.exp(-omega_squared * total_time / eta)
    modal_velocity_first = (-omega_squared / eta) * modal_position_first

    position_second = eigenvectors @ modal_position_second
    velocity_second = eigenvectors @ modal_velocity_second
    position_first = eigenvectors @ modal_position_first
    velocity_first = eigenvectors @ modal_velocity_first

    position_absolute = float(np.max(np.abs(position_second - position_first)))
    velocity_absolute = float(np.max(np.abs(velocity_second - velocity_first)))
    state_scale = max(float(np.max(np.abs(position_first))), 1e-300)
    displacement_scale = max(float(np.max(np.abs(position_first - c0))), 1e-300)
    velocity_scale = max(float(np.max(np.abs(velocity_first))), 1e-300)
    return {
        "eta": eta,
        "position_absolute_linf": position_absolute,
        "position_relative_to_state_linf": position_absolute / state_scale,
        "position_relative_to_overdamped_displacement_linf": position_absolute / displacement_scale,
        "velocity_absolute_linf": velocity_absolute,
        "velocity_relative_to_first_order_linf": velocity_absolute / velocity_scale,
    }


def fitted_slope(rows: list[dict[str, float]], key: str, minimum_eta: float) -> float:
    selected = [row for row in rows if row["eta"] >= minimum_eta]
    x = np.log([row["eta"] for row in selected])
    y = np.log([row[key] for row in selected])
    return float(np.polyfit(x, y, 1)[0])


def verify_overdamped() -> dict[str, Any]:
    # Preserve the original comparison exactly as a historical reproduction.
    legacy_etas = np.array([1.0, 3.0, 10.0, 30.0, 100.0, 300.0])
    legacy_errors = np.array([overdamped_error(float(eta)) for eta in legacy_etas])
    legacy_slope, legacy_intercept = np.polyfit(
        np.log(legacy_etas[legacy_etas >= 30.0]),
        np.log(legacy_errors[legacy_etas >= 30.0]),
        1,
    )

    extended_etas = [10.0, 30.0, 100.0, 300.0, 1000.0, 3000.0]
    rest_rows = [exact_linear_chain_comparison(eta, "rest") for eta in extended_etas]
    slow_rows = [exact_linear_chain_comparison(eta, "leading_slow_manifold") for eta in extended_etas]

    metric_keys = [
        "position_relative_to_state_linf",
        "position_relative_to_overdamped_displacement_linf",
        "velocity_relative_to_first_order_linf",
    ]
    upper_decade_slopes = {
        "rest": {key: fitted_slope(rest_rows, key, 300.0) for key in metric_keys},
        "leading_slow_manifold": {key: fitted_slope(slow_rows, key, 300.0) for key in metric_keys},
    }

    n = 32
    kappa = 1.0
    exact_lowest_omega = 2.0 * math.sqrt(2.0 * kappa) * math.sin(math.pi / (2.0 * n))
    exact_highest_omega = 2.0 * math.sqrt(2.0 * kappa) * math.cos(math.pi / (2.0 * n))
    return {
        "legacy_reproduction": {
            "parameters": {"N": n, "kappa": kappa, "T": 5.0, "initial_velocity": 0.0},
            "rows": [
                {"eta": float(e), "position_relative_to_state_linf": float(err)}
                for e, err in zip(legacy_etas, legacy_errors)
            ],
            "fit_eta_ge_30": {"slope": float(legacy_slope), "intercept": float(legacy_intercept)},
            "interpretation": (
                "This rest-initialized fixed-time position comparison reproduces A.6 but is "
                "dominated asymptotically by the O(eta^-2) initial-layer slip. It is not a "
                "diagnostic of the O(eta^-3) absolute slow-velocity correction."
            ),
        },
        "extended_exact_modal_comparison": {
            "parameters": {
                "N": n,
                "kappa": kappa,
                "T": 5.0,
                "etas": extended_etas,
                "position_norm": "L-infinity",
                "velocity_norm": "L-infinity",
                "solution_method": "exact eigendecomposition of the linear open chain",
            },
            "rest_initialization_rows": rest_rows,
            "leading_slow_manifold_rows": slow_rows,
            "upper_decade_eta_300_to_3000_slopes": upper_decade_slopes,
        },
        "lowest_open_chain_mode_exact": exact_lowest_omega,
        "highest_open_chain_mode_exact": exact_highest_omega,
        "highest_mode_critical_damping_exact": 2.0 * exact_highest_omega,
        "asymptotic_conclusion": (
            "For the stated linear chain at fixed O(1) time: rest initialization gives an "
            "O(eta^-2) state-normalized position slip from the fast layer; leading slow-manifold "
            "initialization suppresses that term, leaving O(eta^-3) state-normalized position "
            "error. In both cases the velocity error relative to the O(eta^-1) first-order "
            "velocity is O(eta^-2). Relative to the total O(eta^-1) overdamped displacement, "
            "the slow-manifold position error is likewise O(eta^-2)."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("CU_Physics_A6_1_verification_results.json"),
        help="JSON output path",
    )
    parser.add_argument("--samples", type=int, default=200_000, help="Monte Carlo samples")
    parser.add_argument("--skip-heavy", action="store_true", help="Skip Madelung and ODE simulations")
    args = parser.parse_args()

    rng = np.random.default_rng(DEFAULT_SEED)
    report: dict[str, Any] = {
        "metadata": {
            "manuscript_version": "A.6.1",
            "seed": DEFAULT_SEED,
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
        },
        "block_averaging": verify_block_theorems(rng, args.samples),
        "joint_growth_wedge": verify_wedge(rng, args.samples),
        "fixed_coupling_flow": verify_fixed_coupling_structure(),
        "fisher_absolute_constants": verify_fisher_constants(),
    }

    if not args.skip_heavy:
        report["wave_dispersion"] = verify_wave()
        report["madelung"] = verify_madelung()
        report["overdamped_limit"] = verify_overdamped()

    report["metadata"]["script_sha256"] = sha256_file(Path(__file__))
    args.output.write_text(json.dumps(_jsonable(report), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(_jsonable(report), indent=2, sort_keys=True))
    print(f"\nWrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
