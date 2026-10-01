# Project instructions

- Read README.md, docs/02-requirements.md, and planning/decisions.md before changing the design.
- Preserve the owner’s intent: custom modular robot arm; end-effector design deferred; eventual nonvisual/intermittent-vision research.
- Treat unaccepted architecture and numbers as proposals. Never silently promote them to verified specifications.
- Do not claim Boston Dynamics internals are known. Cite public primary sources and distinguish inspiration from evidence.
- Keep SI units explicit. State whether torque is motor-side or output-side, peak or continuous, measured or estimated.
- Update BOM IDs and requirement IDs without reusing retired IDs. No selected component without an exact datasheet and compatibility checks.
- Keep credentials, large datasets, vendor-controlled files and generated CAD caches out of Git.
- Do not add a license on behalf of the owner without a decision.
- All actuation code must start disarmed. No automatically executed hardware motion in tests or CI.
- Preserve stop behavior, command timeouts, motion limits and manual rearm requirements when control code is introduced.
- Update the decision register and affected interfaces when changing mechanical, electrical or protocol assumptions.
- Validate planning structure with tools/check_project.py. Verify engineering tools with meaningful hand calculations.
