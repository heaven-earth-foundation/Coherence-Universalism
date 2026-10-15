"""Reconstruction of the Biology Supplement B viability-control models from their published specification
(04_Biology_Technical_Supplement, §§B.2-B.7). Forward Euler, dt=0.01, T=150."""
import numpy as np
K = [0, .02, .05, .10, .15, .25, .40, .80]

def run(cfg, kappa, dt=0.01, T=150.0, control=True):
    f, x, s, d, B = map(np.array, (cfg["f"], cfg["x0"], cfg["s"], cfg["d"], [0.12]))
    B = 0.12
    n = int(round(T / dt)); mins = []; J = 0.0; late = []; clip = 0; first_fail = None; xmin_state = None
    for k in range(n + 1):
        t = k * dt
        m = x - f
        if m.min() < (mins[-1] if mins else np.inf): xmin_state = (t, x.copy())
        mins.append(min(m.min(), mins[-1]) if mins else m.min())
        if first_fail is None and m.min() < 0: first_fail = t
        y = cfg["y"](t)
        if t >= 130: late.append(((x - y) ** 2).mean())
        if k == n: break
        if control:
            ud = np.maximum(0, 0.5 * (y - x))
            if ud.sum() > B:
                w = np.exp(-8 * (x - f)) * (0.15 + np.maximum(y - x, 0)); u = B * w / w.sum()
            else: u = ud
        else: u = np.zeros(3)
        J += u.sum() * dt
        dx = s - d * x + u + kappa * (x.mean() - x) + cfg["xi"](t)
        nx = x + dt * dx
        if np.any(nx < 0) or np.any(nx > 1): clip += 1
        x = np.clip(nx, 0, 1)
    return dict(Mmin=mins[-1], J=J, rmse=np.sqrt(np.mean(late)), clip=clip, fail=first_fail)

def xi1(t):
    if 20 <= t < 28: return np.array([-.075, 0, 0])
    if 50 <= t < 60: return np.array([-.035, -.055, -.025])
    if 82 <= t < 88: return np.array([0, 0, -.100])
    return np.zeros(3)
C1 = dict(f=[.24]*3, x0=[.72]*3, s=[.065, .055, .060], d=[.11, .09, .10],
          y=lambda t: np.array([.75, .72, .70]) if t < 100 else np.array([.88, .56, .78]), xi=xi1)
C2 = dict(f=[.10, .10, .82], x0=[.60, .60, .90], s=[.18, .18, .036], d=[.30, .30, .04],
          y=lambda t: np.array([.60, .60, .90]), xi=lambda t: np.array([0, 0, -.020]) if 40 <= t < 50 else np.zeros(3))

PUB1 = {0: (0.2811715052, 7.1992430737, 0.0467393362), .8: (0.3527559814, 7.7238403844, 0.1228401182)}
PUB2 = {0: 0.0431278138, .25: -0.0080077450, .8: -0.0470145357}
print("Configuration I  (kappa, Mmin, J, late RMSE, clip)")
for k in K:
    r = run(C1, k); print(f"  {k:4.2f}  {r['Mmin']:.10f}  {r['J']:.10f}  {r['rmse']:.10f}  {r['clip']}" + (f"   published {PUB1[k]}" if k in PUB1 else ""))
r = run(C1, 0, control=False); print(f"  no-control ref: Mmin {r['Mmin']:.10f}, first failure t={r['fail']}   published -0.1009342470, t=26.76")
print("Configuration II (kappa, Mmin, first failure, clip)")
for k in K:
    r = run(C2, k); print(f"  {k:4.2f}  {r['Mmin']:.10f}  {r['fail']}  {r['clip']}" + (f"   published {PUB2[k]}" if k in PUB2 else ""))
