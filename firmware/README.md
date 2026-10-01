# Joint firmware scope

No actuation firmware exists yet. Reuse a purchased drive's local control where suitable; custom code may only be needed for integration and telemetry.

Proposed states: BOOT → DISARMED → ARMED → ACTIVE. Any fault enters FAULT with drive-specific controlled response and load retention; recovery requires the cause cleared and explicit manual rearm. A request to enable must not bypass startup checks. Loss of communication must be handled locally without waiting for a host response.

Define sensor validity, motion/current/temperature limits, command age, watchdog behavior, stop behavior and fault logging before ACTIVE can be implemented.
