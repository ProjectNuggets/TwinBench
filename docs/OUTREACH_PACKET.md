# Outreach Packet

Use this packet when inviting competitors, adjacent platforms, and major labs to run against TwinBench.

## Short Positioning

TwinBench is an open benchmark for **personal AI assistant runtimes**.

It measures whether a runtime can remember, act, follow up, stay safe, and operate over time. The benchmark is evidence-first, vendor-neutral, and designed for real runtimes rather than one-shot prompt systems.

## Wave Structure

- Wave 1: direct competitors and close runtime peers
- Wave 2: adjacent platforms and memory/runtime infrastructure teams
- Wave 3: frontier labs

Each wave keeps the same benchmark ask while changing the emphasis.

## Competitor Invitation

Subject: Invitation to run your runtime against TwinBench

We think a new benchmark category is needed for personal AI assistant runtimes.

TwinBench is an open, evidence-first benchmark for runtimes that aim to remember, act autonomously, operate across channels, and stay safe over time. We are inviting serious runtime builders to run their systems against it and publish artifacts publicly.

If your runtime can expose the benchmark contract, we would love to include a verified submission from your team. If it cannot yet, we are still happy to work from a documented compatibility path.

Repo: https://github.com/ProjectNuggets/DTaaS-benchmark

Use this when the target is already building something close to a persistent personal AI assistant runtime. Emphasize open challenge, artifact-backed comparison, and the fact that unsupported surfaces are handled explicitly.

## Standards / Research Invitation

Subject: TwinBench: open benchmark for persistent personal AI assistant runtimes

We are publishing TwinBench as a public benchmark for a category we believe is currently under-measured: persistent personal AI assistant runtimes.

The benchmark focuses on memory, autonomous execution, cross-channel behavior, safety, scale, resilience, and latency. All serious results are artifact-backed and evidence-separated into verified and projected components.

We would value feedback, critiques, and independent runs.

Use this when the target is more likely to care about methodology than leaderboard competition.

## Major Lab Invitation

Subject: Invitation to evaluate runtime agents on TwinBench

We believe the benchmark landscape still under-measures runtime behavior for personal AI assistants. TwinBench is an attempt to define that category openly and rigorously.

We would be glad to see your team run a compatible runtime, agent product, or research system against the benchmark and publish an artifact-backed result. The repo is designed to be vendor-neutral, evidence-first, and reproducible.

Use this when the target may not be benchmark-native today, but has enough ecosystem weight that even a response, critique, or partial run would help define the category.

## Follow-Up

Short follow-up after 5 to 7 business days:

TwinBench should now be straightforward to evaluate from the outside. If useful, we can help your team determine whether your runtime is native-contract ready, bootstrap-limited, adapter-needed, or only suitable for a partial benchmark pass.

## FAQ

### Is this a chatbot benchmark?

No. TwinBench is about long-lived assistant runtime behavior.

### Is Nullalis the winner?

No. Nullalis is the reference runtime because it provides the first strong evidence-rich artifact.

### What if a runtime does not support the contract yet?

TwinBench prefers honest compatibility notes and partial results over forced comparisons.
