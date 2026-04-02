# Reference Result Policy

TwinBench uses several result classes.

## Canonical Reference Result

A checked-in, artifact-backed run that the repo uses as the main public example.

Requirements:

- public harness artifact
- coherent JSON and report outputs
- clear interpretation notes

## Supporting Artifact

A useful secondary artifact that explains a narrower point.

Examples:

- scale-only probe
- degraded run
- smoke run

## Degraded Artifact

A real run affected by runtime outage, upstream outage, or partial environment failure.

These should not be hidden. They help prove the benchmark is honest.

## External Estimate

A non-ranked comparison row derived from public evidence, not from a verified live harness run.

## Current Policy

- keep the existing Nullalis full run as the canonical reference artifact
- keep the scale-only probe as a supporting artifact
- note publicly that scale interpretation in the canonical full artifact is conservative relative to later provisioning-aware fixes
