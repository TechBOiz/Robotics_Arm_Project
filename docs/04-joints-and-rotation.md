# Joint module and rotation trade study

## Proposed module boundary

Motor, drive/controller, reducer if needed, load-bearing output support, position sensing, temperature sensing, housing, input/output mounting interfaces and labeled harness. Document serial number, firmware, calibration and gear ratio per module. A housing should transfer external moments through specified bearings, rather than unintentionally loading a motor shaft.

## Actuation alternatives

| Option | Why investigate | Questions to resolve |
|---|---|---|
| Integrated BLDC actuator | Faster first-joint bring-up, fewer integration unknowns | Available control modes, output bearing limits, thermal ratings, protocol, replacement parts |
| Motor + planetary reduction | Modular parts and ratio choices | Backlash, efficiency, noise, output support, controllability |
| Motor + strain-wave reduction | Compact high reduction | Torsional compliance, friction, torque sensing quality, cost, overload limits |
| Low-ratio / quasi-direct drive | Potentially useful force responsiveness | Motor size, continuous current, thermal load, holding load |

These are trade-study categories, not verified product recommendations. Source actual manufacturer data before scoring candidates.

## Continuous rotation is a system property

A shaft that turns 360 degrees is not automatically a continuously rotating wired joint. A routed cable eventually twists. Local processors reduce signal count but do not solve that twist. An absolute single-turn encoder also does not necessarily retain multi-turn position through power loss.

| Routing approach | Use case | Evidence needed |
|---|---|---|
| Bounded cable loop | First joint and limited-angle axes | Bend radius, strain relief, twist limits, cycle test |
| Power + rated data slip ring | Candidate continuous axes | Continuous/peak current, contact resistance, temperature, bus signal integrity, lifetime |
| Contactless rotary power/data | Later option | Power budget, coupling, size, EMI, communication latency and cost |

Do not assume a generic slip ring can carry CAN-FD or EtherCAT reliably. Do not place an unqualified rotary contact in a protective-stop path. Account for hollow bore, bearings, seals if needed, thermal conduction and maintenance access.

## First-joint acceptance evidence

Fixture and load retention reviewed; wiring and current limits checked; calibrated position zero; measured direction/signs; bounded travel; stop, timeout and encoder-fault response; torque-versus-current sweep with reference sensor; backlash/hysteresis; temperature rise under defined duty; commanded versus achieved trajectories. Record both continuous and short-duration performance.

## Sizing workflow

1. Specify reach, total distal load and its center of mass.
2. Estimate every downstream link and actuator mass.
3. Calculate static loads across poses, including output bearing moments.
4. Add trajectory-based inertia, friction and contact loads using a dynamic model.
5. Evaluate output and motor speed/torque envelopes, reducer losses, electrical power and RMS/thermal duty.
6. Select candidate parts, update masses, and iterate from wrist toward shoulder.

The bundled static calculator only supports step 3 for two planar pitch axes in one horizontal pose. A reserve multiplier in that calculator is not a dynamic model or certified safety factor.
