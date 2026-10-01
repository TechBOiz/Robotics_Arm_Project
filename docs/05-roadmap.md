# Roadmap and exit gates

Dates and budgets remain unset until requirements and fabrication access are known. Milestones are sequential evidence gates; documentation and simulation can proceed together.

| Milestone | Deliverable | Exit gate |
|---|---|---|
| M0 — Requirements | Reference study, scope, budget, reach/load targets | Owner decisions recorded; numeric targets explicit |
| M1 — Architecture and sizing | 6R/7R comparison, mass budget, actuator shortlist, interfaces | Calculations and actual datasheets support first-joint design |
| M2 — Single joint | Restrained fixture, local control, calibrated sensing | Stop/fault/thermal/load evidence; no reliance on peak torque for continuous hold |
| M3 — Two-link section | Shoulder/elbow-like structure and model | Gravity compensation, harness routing, power-loss behavior, model agreement |
| M4 — Full arm | Complete structure through wrist flange | Calibration, collision limits, load tests, repeatability and service procedure |
| M5 — Sensing platform | Force feedback, synchronized logs and simulation alignment | Sensor quality and model mismatch quantified |
| M6 — Intermittent-vision study | Baselines, ablations, reproducible results | Compute/performance tradeoff and perturbation recovery measured |

## Procurement sequence

- M0: no component commitments.
- M1: approve an exact first-joint BOM after compatibility and budget review.
- M2: buy/build only first-joint parts and test equipment; revise before replication.
- M3: order enough for a two-link validation assembly.
- M4: complete remaining joints after loads and interfaces have been rechecked.

An end effector is a later independent milestone. M6 contact tests may begin with a simple instrumented probe or rigid fixture after a separate interface decision; grasping/insertion tool design is not included in current V1.
