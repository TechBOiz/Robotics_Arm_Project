# Validation and commissioning plan

This is a design plan, not certification or a complete commissioning procedure. Acceptance limits must be filled before powered tests.

## Main engineering risks

| Risk | Planned response | Evidence |
|---|---|---|
| Gravity drop when drive power is removed | Define brake/counterbalance/support and stop sequence | Restrained power-loss test at representative load |
| Peak torque mistaken for continuous rating | RMS duty and thermal testing | Temperature/time/current logs under defined cooling |
| Current interpreted as exact contact force | Calibrate model, quantify friction and dynamic error | Reference force/torque measurements |
| Encoder fault or wrong sign | Startup plausibility, direction checks and local fault handling | Restrained fault injection |
| Stale command / bus failure | Local timeout, bounded command limits and manual rearm | Disconnect and delayed-command tests |
| Regenerative bus overvoltage | Rated absorption/clamping strategy | Bus-voltage capture during deceleration |
| Continuous rotation damages wiring | Separate rotary-interconnect development gate | Loaded endurance and communication-error records |
| Excess distal mass drives shoulder overload | Iterated mass and inertia budget | As-built masses and model update |
| Link/bearing/fastener failure | Structural and combined-load review | Calculations and defined proof-test plan |
| Pinch/self-collision | Travel and collision limits; guarded fixture/workspace | Simulation and low-energy commissioning records |

## Progression

1. Unpowered assembly and wiring inspection; measure insulation/continuity where applicable.
2. Restrained motor/joint with low-energy limits; verify sensor signs and disarmed startup.
3. Fault and protective-stop checks with gravity loads supported; define reset behavior.
4. Calibrated static loads, backlash and thermal characterization.
5. Two-link and full-arm tests within measured envelopes.
6. Force/impedance and learning experiments only after deterministic limits and reference-control baselines.

Power removal alone can cause a falling arm. The stop architecture must address drive energy and load retention together. A software stop or a normal CAN message must not be represented as a safety-rated system. Never infer collaborative-operation suitability from a compliant control mode.

## Acceptance record fields

Requirement ID, hardware/firmware revision, test fixture, calibration, operating limits, expected result, measured result, raw log path, pass/fail, deviation and reviewer. Use experiments/run-template.md. Record near misses and unexpected motion as failures requiring investigation.
