# Static sizing example

`python tools/size_static.py` uses config/static-sizing.json. All masses and geometry are illustrative; none comes from selected parts.

Model: horizontal planar upper link (length a) and forearm (length b); uniform link masses at their midpoints; elbow module lumped at the elbow; wrist modules lumped at the forearm end; all distal load lumped a further distance d away. The elbow module lies on the elbow axis and therefore adds no moment about that axis in this approximation.

Shoulder output gravity torque:

`g * [m_upper*a/2 + m_elbow*a + m_forearm*(a+b/2) + m_wrist*(a+b) + m_load*(a+b+d)]`

Elbow output gravity torque:

`g * [m_forearm*b/2 + m_wrist*b + m_load*(b+d)]`

For the provided numbers, shoulder = **14.0283 Nm**, elbow = **5.37588 Nm**. Multiplying by the illustrative 1.5 reserve gives **21.04245 Nm** and **8.06382 Nm** respectively. These are output-axis estimates; they are not motor-side torque or continuous actuator ratings.

The 0.08 m offset describes the distal-load COM beyond the wrist lump, not a frozen wrist geometry. The 0.60 m shoulder-to-load-COM distance here must not be confused with a validated shoulder-to-flange reach. The 0.60 m flange-reach target is separately provisional.

Missing: other poses/axes, 3D offsets, actual CAD mass distribution, acceleration and inertia, transmission losses and backlash, contact forces, friction, bearing/fastener/structural loads, thermal duty and regeneration. Motor/reducer selection requires these in addition to this estimate.

Verification cases: zero masses → zero gravity moment; doubling all masses → double moments; payload only → ordinary force times lever arm. These were checked during scaffold creation; see planning/validation-record.md.
