# Preliminary bill of materials

**Category placeholders, not approved purchases.** Exact manufacturers, part numbers, ratings, suppliers and prices are unset. Quantities below assume the proposed 7R architecture and will change after sizing. `items.json` is the structured source. Unknown quantities/prices are null, never zero cost.

| ID | Category | First joint | Full arm proposal | Selection depends on |
|---|---|---:|---:|---|
| BOM-001 | BLDC motor / actuator core | 1 | 7 | Output torque/speed, winding, thermal envelope |
| BOM-002 | Drive and local control | 1 | 7 | May be bundled in BOM-001; avoid double count |
| BOM-003 | Transmission | 1 | 7 | May be bundled or omitted by direct drive |
| BOM-004 | Output load-bearing assembly | 1 | 7 | Combined load ratings; may be bundled |
| BOM-005 | Motor commutation encoder | 1 | 7 | May be integrated in motor/drive |
| BOM-006 | Output joint encoder | 1 | 7 | Accuracy, packaging, calibration; optional after trade study |
| BOM-007 | Joint housing and mounts | 1 set | 7 sets | Materials, machining, tolerances, cooling |
| BOM-008 | Load retention / brake components | TBD | TBD | Gravity axes and stop analysis |
| BOM-009 | Temperature sensors | TBD | TBD | Motor/driver sensing may be integrated |
| BOM-010 | Structural links and flange | — | 1 set | CAD and stiffness/mass budget |
| BOM-011 | Base and restrained joint fixture | 1 set | 1 set | Overturning moment, load paths |
| BOM-012 | DC supply | 1 | 1 | Voltage, current, duty and regeneration strategy |
| BOM-013 | Protective-stop / disconnect hardware | 1 set | 1 set | Drive and gravity-load behavior |
| BOM-014 | Protection, distribution, regenerative handling | 1 set | 1 set | Power analysis and drive requirements |
| BOM-015 | Host-to-joint bus interface | 1 | 1 | Selected protocol and drive support |
| BOM-016 | Harnesses, connectors and termination | 1 set | 1 set | Current, motion, shielding and pinout |
| BOM-017 | Rotary interconnect | — | TBD | Continuous-axis decision and validation |
| BOM-018 | Reference load cell / torque test fixture | 1 set | 1 set | Calibration and measurement range |
| BOM-019 | Wrist force/torque sensor | — | Optional 1 | Research need, mass, calibration and cost |
| BOM-020 | Camera | — | 1 | Existing device may be reused; latency/timebase |
| BOM-021 | Host computer | 1 | 1 | Existing computer candidate; timing needs |
| BOM-022 | Fasteners, strain relief and guarding | 1 set | 1 set | Final design and test setup |

End-effector parts and tactile/audio devices are deferred. First-joint quantities describe integration needs and may be satisfied by one integrated actuator rather than separate purchases. The BOM stores overlap notes; do not sum lines until sourcing is resolved.

## Cost procedure

Add actual vendor quote URL/date/currency, unit quantity and unit price. Separate hardware, tools, fabrication, shipping/tax and contingency. Reused equipment must be explicitly marked as available and compatible. Total cost is currently **unknown**, not $0. No ordering is authorized by this document.
