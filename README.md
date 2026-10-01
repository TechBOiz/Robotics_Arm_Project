# Robotics Arm Project

An independent, from-scratch electric robot-arm research project inspired by the broad motion range and integrated design of Boston Dynamics Atlas. Repository: [`TechBOiz/Robotics_Arm_Project`](https://github.com/TechBOiz/Robotics_Arm_Project).

**Status: concept / architecture v0.1 — 2026-10-01.** No hardware has been selected, purchased, built, or validated. Numerical values are provisional design-study inputs, not specifications. This is not an Atlas replica or an affiliated project.

## Purpose

Build a serviceable, instrumented arm that can eventually manipulate using intermittent vision, proprioception, force feedback, touch, and audio. Establish reliable mechanics and control before introducing learned policies.

The end effector is deferred. V1 ends at a wrist flange and inert test load; reserve a mass allowance, sensor mounting space, and future electrical interface now.

## Working proposal

| Item | Proposal | Status |
|---|---|---|
| Kinematics | 7 revolute joints: 3 shoulder, 1 elbow, 3 wrist | Proposed; compare 6 axes before freeze |
| Mounting | Rigid fixed bench mount | Proposed |
| Reach | Approximately 0.60 m from shoulder reference to flange | Study value; verify in CAD |
| Distal load | 1.0 kg total including future tooling, sensors, adapters and object | Study value; no object-only rating |
| Actuation | Purchased BLDC motors/drives and transmissions in custom joint modules | Proposed definition of from scratch |
| Electronics | Local joint controllers, central host, separate protective stop path | Proposed |
| Rotation | Evaluate continuous roll axes; bounded travel on first joint prototype | Open; wiring feasibility gate |
| Simulation | MuJoCo candidate for dynamics and sensor experiments | Proposed; no simulator implementation yet |
| First physical deliverable | One restrained, instrumented joint on a test fixture | Planned |

## Start here

1. [Project charter](docs/01-charter.md) — scope and decisions needed.
2. [Requirements](docs/02-requirements.md) — targets and evidence required.
3. [System architecture](docs/03-architecture.md) — mechanics, electronics, controls, sensing.
4. [Joint and rotation trade study](docs/04-joints-and-rotation.md).
5. [Roadmap](docs/05-roadmap.md) and [issue backlog](planning/backlog.md).
6. [Preliminary BOM](bom/README.md) — category-level only; no shopping list yet.
7. [GitHub setup](docs/10-github-setup.md).

## Repository map

```text
docs/          Requirements, architecture, interfaces, validation, research
bom/           Human-readable preliminary BOM and structured item records
planning/      Milestones, issue drafts, labels, decision register
config/        Provisional sizing inputs
tools/         Offline sizing and validation utilities
mechanical/    CAD conventions and planned outputs
electrical/    Schematics and harness planning conventions
firmware/      Joint controller scope and state machine
software/      Host application and control scope
simulation/    Digital model and sensing experiment plan
experiments/   Run-record template
.github/       Issue and pull request templates
```

## Offline tools

Python 3.10+; standard library only:

```bash
python tools/size_static.py
python tools/check_project.py
```

The first command calculates a simple horizontal-arm gravity load. It does not select motors or establish safe operating limits. The second checks planning-data integrity. Neither commands hardware.

## Immediate decisions

- Confirm that electric Atlas is the intended reference, and provide images/video timestamps for preferred details.
- Set prototype and total budget ceilings, reach, distal load and fabrication access.
- Decide whether continuous rotation is mandatory for V1 or a later module variant.
- Compare buying integrated actuator modules with assembling motors, drives and reducers into our own modules.

See [decisions](planning/decisions.md). Licensing for code, CAD, and electronics remains undecided; no open-source license is asserted by this scaffold.
