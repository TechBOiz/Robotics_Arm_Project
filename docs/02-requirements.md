# Requirements register

Status meanings: **confirmed** = expressed task scope; **proposed** = draft engineering requirement; **TBD** = not defined. Proposed values need owner acceptance and engineering validation.

| ID | Requirement / target | Status | Verification |
|---|---|---|---|
| REQ-001 | Build one custom electric robot arm | Confirmed | Design and assembly records |
| REQ-002 | End-effector design deferred; terminate scope at flange | Confirmed | Interface drawing and scope review |
| REQ-003 | Boston Dynamics arm as design inspiration | Confirmed | Reference study; model/version still to confirm |
| REQ-004 | 7 axes; compare with 6-axis alternative | Proposed | Reachability/singularity study |
| REQ-005 | 0.60 m shoulder-to-flange reach | Proposed | CAD geometry and measurement |
| REQ-006 | 1.0 kg total distal load, including tool/sensors/object | Proposed | Defined COM, pose and duty-cycle load tests |
| REQ-007 | Replaceable joint modules without destructive assembly | Proposed | Service demonstration |
| REQ-008 | Record position, velocity, current, temperature and faults | Proposed | Calibrated timestamped logs |
| REQ-009 | Quantify force/torque observability; motor current is not ground-truth contact force | Proposed | Reference load-cell comparison |
| REQ-010 | No motion on power-up; explicit arm and manual fault recovery | Proposed | State-machine tests |
| REQ-011 | Define independent protective stop and gravity-load retention | Proposed | Restrained fault tests before free arm motion |
| REQ-012 | Evaluate continuous rotation with power/data routing and lifetime evidence | Proposed | Loaded rotary interconnect endurance test |
| REQ-013 | Future tactile/audio inputs and intermittent camera observations | Proposed | Shared timebase/interface and research experiment |
| REQ-014 | Position repeatability, absolute accuracy and bandwidth targets | TBD | Define distinct procedures before measurement |
| REQ-015 | Maximum speed, acceleration, jerk and contact force | TBD | Load analysis and restrained tests |
| REQ-016 | Supply voltage, peak power and duty cycle | TBD | Drive compatibility, bus energy and thermal analysis |
| REQ-017 | First-joint and full-system budget ceilings | TBD | Owner decision and quoted BOM |
| REQ-018 | Command timeout, bus utilization and latency limits | TBD | Timing budget and fault injection |

No payload rating follows from REQ-006 until COM offset, orientations, speed, thermal conditions and duty cycle are specified. An illustrative 0.25 kg adapter/sensor allowance leaves 0.75 kg for a future tool and object; this allocation is not yet approved.
