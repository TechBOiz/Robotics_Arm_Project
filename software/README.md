# Host software scope

Planned modules: hardware abstraction, command/state protocol, kinematics/dynamics, calibration, reference control, limits, logging, experiment runner and later learned policy adapters. Keep simulation and physical interfaces separate and explicit. Default execution must never connect to or arm hardware.

Direct motor control must not depend on an LLM, network service or nondeterministic inference. ROS integration is optional and undecided; use small documented interfaces so transport can change without rewriting the controller.
