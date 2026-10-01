# Simulation plan

MuJoCo is the proposed first engine because the project needs articulated dynamics, contacts and configurable sensor observations. Version, rendering backend and installation remain to be selected. No runnable scene is included in v0.1.

Start with a single joint and known inert load, then a two-link gravity model; compare analytic torques before generating full-arm geometry. The 7R model follows only after axes, offsets, limits and mass estimates are defined.

Separate privileged simulation state from policy observations. Implement sensor noise/bias/delay and camera update schedules independently of physics/control steps. Preserve image age and availability masks. Measure actual inference cost rather than assuming cost is proportional to frame-rate reduction.
