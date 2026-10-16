# WebGPU: decide whether to investigate further

Authored illustration. Use tech-research or learn-new-tech.

**Learner:** 'I heard of WebGPU today. I know JavaScript but no GPU programming.
Could it help my photo-filter web app? I have 20 minutes.'

**Tutor:** 'First we need the workload and target environment: are filters applied
to occasional small images or large images in real time, and which browsers and
devices must work? We can decide whether a small experiment is worthwhile before
learning GPU implementation.'

Wait for context before deep research. A short orientation is fine: the
[W3C working group's mission](https://www.w3.org/groups/wg/gpu/) concerns exposing
modern graphics and computation capabilities to the web. That establishes purpose,
not performance or support on the learner's devices.

For this decision, discover only the terms that clarify the architecture:
GPU versus CPU work, shader, resource/buffer, pipeline, and WGSL. Explain their
relevance without making memorization a prerequisite to a fit assessment.

Research route: the [GPUWeb official repository](https://github.com/gpuweb/gpuweb)
links the specification and related work. Then inspect current implementation
documentation for the learner's actual browser/device targets. Do not infer a
support matrix from the existence of a standard.

A brief should separate:

- Known workload and current performance problem.
- Potential fit, explicitly a hypothesis until measured.
- Necessary learning cost and environment constraints.
- What can wait: shader syntax and pipeline implementation until the fit decision.
- Remaining uncertainty: support, transfer/dispatch overhead and measured benefit.
- Next step: compare one representative filter against the current baseline.

Stop if research shows no relevant bottleneck, an unacceptable support gap, or
uncertainty best resolved by a small experiment. Do not generate an implementation
tutorial just because WebGPU is new. If browsing is unavailable, label orientation
provisional and request relevant documentation instead of fabricating sources.
