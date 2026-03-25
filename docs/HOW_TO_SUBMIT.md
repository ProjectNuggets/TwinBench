# How to Submit Results

TwinBench should feel lightweight to submit and strict to trust.

## Minimum Submission

Attach:

- `results/<runtime>.json`
- `results/<runtime>.md` or `results/<runtime>.html`
- runtime version or commit SHA
- harness commit SHA

## Strong Submission

Also attach:

- diagnostics snapshot
- metrics snapshot
- run manifest
- one short incident note if anything degraded

## Submission Flow

1. Run the harness.
2. Review the JSON for `verified`, `projected`, and `measured_coverage`.
3. Open the [Submit Results issue template](../.github/ISSUE_TEMPLATE/submit-results.md).
4. Attach the artifact pack.

## What Makes a Result Trusted

- produced by the public harness
- artifact attached
- evidence and notes included
- blocked or unavailable dimensions reported honestly

TwinBench is strongest when runtimes publish artifacts others can challenge and reproduce.
