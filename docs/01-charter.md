# Project charter

## Objective

Design and build a fixed-base modular electric arm from first principles at the system, joint-housing, linkage, wiring, integration, and controls levels. Use available motors, drives, encoders, bearings, and transmissions where practical. Custom motor electromagnetic design and custom inverter PCB development are optional future work, not required to call this a from-scratch arm.

## Intended inspiration

Working assumption: the electric Atlas arm. Desired qualities are compact integrated joints, broad useful motion, neat internal routing, replaceable modules and rich feedback. Confirm the specific reference with the owner. Public material supports broad/continuous motion claims; it does not reveal the complete internal design. Our joint topology, bus, controller layout and rotary wiring are independent proposals.

## V1 scope

- Requirements and load model; link geometry and mass budget.
- A single joint fixture before full-arm hardware.
- Custom structure, drivetrain integration, encoders, thermal sensing and wiring.
- Motor control interfaces, protective stop behavior and deterministic host control.
- Calibrated kinematic/dynamic model and logging.
- Wrist flange, inert load and future tool-interface envelope.

## Deferred

Dexterous hands, tool changers, production grippers, tactile fingertip design, locomotion, batteries, waterproofing, industrial certification and human-contact operation. Advanced learned controllers follow conventional-control validation.

## Success at this stage

A traceable design package and defensible first-joint experiment, not premature procurement. Build evidence progressively: calculation → simulation → one joint → two links → complete arm → research.

## Owner inputs still needed

Budget ceiling for first joint and complete arm; maximum reach; desired object payload; future tool/sensor mass; speed and duty cycle; preferred Atlas appearance/mechanism; allowable noise; workspace; machine-shop/printing access; available electrical and test equipment. Record answers in planning/decisions.md.
