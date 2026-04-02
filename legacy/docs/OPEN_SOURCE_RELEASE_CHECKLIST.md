# Open Source Release Checklist

Use this checklist before announcing a public TwinBench release.

## Benchmark Integrity

- `README.md` matches the current benchmark version and scoring model
- `SPECIFICATION.md` matches the implemented harness behavior
- `docs/TRUST_MODEL.md` reflects the actual evidence policy
- `CHANGELOG.md` includes the release
- submission template matches current required artifact fields

## Harness Validation

- `python -m py_compile harness/*.py` passes on supported Python
- `python -m harness.runner --help` passes
- sample artifact schema validation passes in CI
- at least one fresh end-to-end run succeeds against a live runtime

## Reference Artifact Package

- publish one fresh Nullalis run with JSON output
- publish Markdown or HTML report
- attach diagnostics snapshot
- attach metrics snapshot
- include runtime version or commit SHA
- include harness version or commit SHA
- include timeout mode and timing metadata

## Public Positioning

- README explains the personal AI assistant runtime category clearly
- Nullalis is framed as the reference runtime, not the scoring authority
- external comparisons are clearly marked as unverified unless run through the harness
- verified leaderboard and reference comparisons are visually distinct

## Submission Readiness

- issue template asks for verified/projected/coverage fields
- manifest example exists for operators who want reproducibility
- contributing guide explains what makes a result trustworthy

## Launch Assets

- repository description and tags are updated
- first public result artifact is linked from the README
- a short launch post or thread is prepared
- a clear call for external submissions is ready
