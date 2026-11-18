"""Run the ten Project 4 Latin hypercube angles."""


# Question 7 - Ten-Angle CFD Sweep

from scipy.stats import qmc
from run_airfoil_project import run_airfoil

ANGLE_MIN = 0.0
ANGLE_MAX = 20.0

sampler = qmc.LatinHypercube(d=1, rng=123)
sample = sampler.random(n=10)

airfoil_angles_deg = qmc.scale(
    sample, [ANGLE_MIN], [ANGLE_MAX]
).ravel()

for angle_deg in airfoil_angles_deg:
    print(f"Running CAD rotation {angle_deg:.6f} deg...", flush=True)

    drag_N, lift_N = run_airfoil(angle_deg)

    print(f"Drag {drag_N:.4f} N, lift {lift_N:.4f} N", flush=True)
