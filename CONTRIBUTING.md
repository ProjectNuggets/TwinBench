# Contributing to DTaaS-Bench

We welcome contributions from the community. Here's how you can help.

## Submit Benchmark Results

The most impactful contribution is running DTaaS-Bench against your runtime and submitting verified results.

1. Run the harness: `python3.10 -m harness.runner --url YOUR_URL --token YOUR_TOKEN --user-id 1 --name "Your Runtime" --output results/your-runtime.json`
2. Open an issue using the **Submit Results** template
3. Attach your `results/your-runtime.json`

We publish all verified results in the leaderboard.

Required v0.2 fields for leaderboard eligibility:
- `verified_composite_score`
- `projected_composite_score`
- `measured_coverage`
- `coverage_adjusted_verified_score`

## Propose New Dimensions

If you believe an important DTaaS capability is not covered by the current 10 dimensions, open an issue with:

- What the dimension measures
- Why it matters for DTaaS
- A proposed test protocol
- How it would be scored

## Improve the Harness

Bug fixes, better test coverage, and improved scoring logic are welcome.

- Fork the repo
- Create a feature branch
- Submit a PR with a clear description
- Include test output showing the change works

## Adjust Weights or Scoring

Weight discussions are welcome. Open an issue with:

- Which weights you propose changing
- Your rationale
- How it affects the leaderboard

We treat weight calibration as a community decision, not an editorial one.

## Code Style

- Python 3.10+
- Type hints where practical
- No external dependencies beyond `requirements.txt`
- Keep scripts self-contained (one file per dimension)

## License

By contributing, you agree that your contributions will be licensed under Apache-2.0.
