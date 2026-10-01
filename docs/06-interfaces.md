# Interface control draft

All dimensions, connector pinouts, bus IDs, rates and electrical ratings are unassigned. Do not fabricate from this document.

## Mechanical

- Joint input/output: datum definitions, locating features, bolt pattern, fastener grade/engagement, permitted loads, service clearance.
- Link: material, section, mass/COM/inertia, tolerances and harness passage.
- Flange: right-handed tool coordinate frame, locating feature, mounting envelope, allowed mass/COM/inertia and reserved sensor stack height.
- Treat sensor and flange adapters as distal payload until explicitly allocated elsewhere.

## Electrical

Power positive/return, chassis/shield strategy, joint data, drive enable/stop, encoder channels if external, temperature and brake connections. Specify connector current/voltage, wire gauge, flex rating, shielding, termination and keyed mating. Never hot-swap modules unless explicitly designed and validated for it.

## Host-to-joint command fields

`protocol_version`, `joint_id`, `sequence`, `timestamp`, `valid_until`, `control_mode`, `position_rad`, `velocity_rad_s`, `feedforward_torque_Nm`, `kp`, `kd`, `limits`, `enable_request`.

Define which fields apply in each mode, units of gains, byte order, scaling and invalid-value handling before a wire format is frozen. Clock synchronization and validity checking must be specified; timestamp fields alone do not provide synchronization.

## Joint-to-host state fields

`joint_id`, `sequence`, `sample_timestamp`, `receive_timestamp`, `position_rad`, `velocity_rad_s`, `motor_current_A`, `estimated_output_torque_Nm`, `motor_temperature_C`, `driver_temperature_C`, `bus_voltage_V`, `fault_bits`, `state`, `calibration_id`.

Mark missing/invalid sensor values explicitly. Preserve raw measurements beside estimates. Record whether torque is motor-side, estimated output-side or measured output-side.

## Data and model conventions

SI units, right-handed frames, radians internally; frame names `base`, `joint_1`…`joint_7`, `flange`, future `tool`, `camera`. Define transforms and signs with diagrams in CAD/model files. Logs include monotonic timestamps, software commit, hardware revision, calibration version, sensor age/masks, command and achieved state.
