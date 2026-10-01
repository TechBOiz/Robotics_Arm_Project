# Intermittent-vision research plan

## Hypothesis

A persistent state estimate with proprioceptive/contact feedback can preserve useful manipulation performance while reducing visual processing. Determine when an additional image changes the action enough to justify its computational cost.

## Sequence

1. Calibrated conventional control and state estimation.
2. Simulation with realistic joint, current/torque and camera observations.
3. Small recurrent policy baseline; do not require a VLA to test the hypothesis.
4. Explicit learned latent dynamics or belief model; assess its incremental benefit and compute cost.
5. Event-triggered image requests versus fixed-period images.
6. Physical replication with calibrated sensors and an independently designed simple contact tool.

## Experiments

Frequent vision + joint/contact feedback; 2 Hz vision + feedback; initial image only + feedback; adaptive vision + feedback; 2 Hz vision without contact feedback; memoryless versus recurrent; model-based versus recurrent-only. Match task distributions, training data/budgets and control constraints. Report mean/variation across independent seeds and held-out disturbances.

Log success, duration, peak contact force, recovery, image encoder calls, total inference time/energy if measurable, sensing latency and model inference overhead. Distinguish a camera that keeps streaming from one whose frames are not processed; report both acquisition and inference costs.

The deployed policy must not receive exact hidden object poses or simulator contact labels unavailable on hardware. Training critics/teachers may use privileged state if disclosed and removed from policy inputs at evaluation. Sensor noise, bias, delay, compliance, friction and actuator saturation require explicit treatment.

## Literature starting points

- Reactive Diffusion Policy (RSS 2025): https://reactive-diffusion-policy.github.io/ — slow planning and fast tactile/force correction.
- FuSe / Beyond Sight (ICRA 2025): https://fuse-model.github.io/ — extending generalist robot policies with heterogeneous sensing.
- Learning robust perceptive locomotion in the wild (2022): https://leggedrobotics.github.io/rl-perceptiveloco/ — recurrent belief and unreliable external perception.
- See, Hear, and Feel: https://ai.stanford.edu/~rhgao/see_hear_feel/ — complementary vision, touch and contact audio.

These are related approaches, not evidence that this arm or a fixed 0.5 s interval will succeed. Do not claim novelty without a fuller literature review.
