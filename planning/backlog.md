# Initial issue backlog

Drafts only; these have not been created on GitHub. Structured source: `issues.json`. Milestone definitions: `milestones.json`.

## ISS-001 — Confirm Atlas reference and V1 scope

Milestone: M0 | Labels: decision, documentation
Dependencies: None

- [ ] Record reference URLs/video timestamps and desired features.
- [ ] Confirm custom modules versus integrated-actuator build and deferred end effector.

## ISS-002 — Set reach, distal load, speed, duty and budget

Milestone: M0 | Labels: decision
Dependencies: ISS-001

- [ ] Define load including tool, sensor and adapter mass plus COM offset.
- [ ] Set first-joint/full-arm budget ceilings and fabrication access.
- [ ] Resolve TBD performance targets or explicitly defer them.

## ISS-003 — Compare 6R and 7R kinematic layouts

Milestone: M1 | Labels: mechanical, simulation
Dependencies: ISS-002

- [ ] Create axes/offset diagrams and compare workspace, singularities and collisions.
- [ ] Record selected topology in decision register.

## ISS-004 — Build mass, static and dynamic load budget

Milestone: M1 | Labels: mechanical, controls
Dependencies: ISS-003

- [ ] Include downstream actuator masses, moments and task accelerations.
- [ ] Separate static, peak, RMS and thermal conditions.
- [ ] Review bearing moments and base reactions.

## ISS-005 — Shortlist actuators and transmissions

Milestone: M1 | Labels: procurement, mechanical
Dependencies: ISS-004

- [ ] Compare at least two feasible actuator approaches using official datasheets.
- [ ] Document output torque/speed, inertia, thermal, protocol, bearing and availability limits.
- [ ] Update masses and costs without double-counting integrated parts.

## ISS-006 — Resolve continuous rotation and harness approach

Milestone: M1 | Labels: mechanical, electrical, decision
Dependencies: ISS-003, ISS-005

- [ ] Identify candidate continuous axes and bounded V1 ranges.
- [ ] Document power/data routing, turn tracking, serviceability and endurance test.

## ISS-007 — Define power, stop and gravity-load retention

Milestone: M1 | Labels: electrical, validation
Dependencies: ISS-005

- [ ] Document power budget, protection, regeneration handling and stop sequence.
- [ ] Define supported power-loss test and manual rearm.

## ISS-008 — Freeze first-joint mechanical and electrical interfaces

Milestone: M1 | Labels: mechanical, electrical
Dependencies: ISS-006, ISS-007

- [ ] Publish reviewed drawings/pinouts and fixture plan.
- [ ] Record exact first-joint BOM, quote dates and budget review.

## ISS-009 — Define joint protocol and timing budget

Milestone: M1 | Labels: firmware, controls
Dependencies: ISS-005

- [ ] Select compatible transport; calculate worst-case bus traffic and timing.
- [ ] Define modes, units, limits, sensor validity, timestamps, timeout and fault behavior.

## ISS-010 — Build restrained single-joint fixture

Milestone: M2 | Labels: mechanical, electrical
Dependencies: ISS-008

- [ ] Document assembly, calibrated reference sensor, wiring and load support.
- [ ] Complete unpowered checks before energization.

## ISS-011 — Bring up joint drive and fault handling

Milestone: M2 | Labels: firmware, controls, validation
Dependencies: ISS-009, ISS-010

- [ ] Verify disarmed startup, encoder direction, bounded commands and explicit enable.
- [ ] Record supported stop, communication loss, encoder fault and manual recovery tests.

## ISS-012 — Characterize first-joint torque and thermals

Milestone: M2 | Labels: validation, controls
Dependencies: ISS-011

- [ ] Measure torque/current relation, hysteresis, backlash and temperature rise.
- [ ] Define supported continuous and peak envelopes; revise BOM/design if needed.

## ISS-013 — Build and validate two-link section

Milestone: M3 | Labels: mechanical, controls
Dependencies: ISS-012

- [ ] Update loads with actual part masses before replication.
- [ ] Compare measured gravity torques with model and validate harness and load retention.

## ISS-014 — Assemble full arm through flange

Milestone: M4 | Labels: mechanical, electrical
Dependencies: ISS-013

- [ ] Release remaining joints after updated load review.
- [ ] Record as-built mass, revision, wiring and calibration IDs.

## ISS-015 — Calibrate and verify full-arm motion

Milestone: M4 | Labels: controls, validation
Dependencies: ISS-014

- [ ] Measure zero offsets, repeatability and model error separately.
- [ ] Validate limits, self-collision constraints, stop and thermal duty with inert loads.

## ISS-016 — Build synchronized sensing and logging pipeline

Milestone: M5 | Labels: controls, research
Dependencies: ISS-015

- [ ] Record raw sensors, estimates, command/state, timestamps, image age and configurations.
- [ ] Quantify sensor calibration, delay and fault/missing-data behavior.

## ISS-017 — Build simulation with sensor and actuator limitations

Milestone: M5 | Labels: simulation, controls
Dependencies: ISS-004, ISS-009

- [ ] Validate single-joint and two-link analytic gravity cases.
- [ ] Expose only deployable observations to the policy; isolate privileged state.
- [ ] Document friction, latency, saturation and model discrepancies.

## ISS-018 — Implement intermittent-vision experiment baselines

Milestone: M6 | Labels: simulation, research
Dependencies: ISS-017

- [ ] Compare frequent, fixed-interval, initial-only and event-triggered vision.
- [ ] Include force-feedback and memory ablations plus total-compute measurements.

## ISS-019 — Plan physical research replication and future tool interface

Milestone: M6 | Labels: research, decision
Dependencies: ISS-016, ISS-018

- [ ] Select a simple contact task and separately approve any probe/tool design.
- [ ] Define calibrated sensing, matched baselines and uncertainty/failure reporting.

## ISS-020 — Choose repository visibility and licensing

Milestone: M0 | Labels: decision, documentation
Dependencies: ISS-001

- [ ] Record publication choice and separate code/CAD/electrical licensing decision.
- [ ] Create repository and import milestone/issue drafts without duplicating them.
