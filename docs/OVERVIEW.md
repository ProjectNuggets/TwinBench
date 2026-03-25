# TwinBench Overview

TwinBench is an open benchmark for **personal AI assistant runtimes**.

It asks a simple question:

**Can this runtime behave like a real personal AI assistant over time?**

That means more than answering one prompt. A serious runtime should be able to:

- remember across sessions and restarts
- carry out tasks autonomously
- keep context coherent across channels
- stay safe during background turns
- operate as real runtime infrastructure

## Category Definition

A personal AI assistant runtime is not just a chatbot. It is a long-lived system that remembers, acts, and stays aligned with one user over time.

## Why TwinBench Exists

Current benchmarks tend to measure:

- coding skill
- task completion
- isolated memory recall

Those are useful, but they do not capture the full runtime behavior expected from persistent personal AI assistants.

TwinBench exists to define and measure that missing category publicly.

For the stronger launch rationale, read [WHY_TWINBENCH.md](WHY_TWINBENCH.md).

## What Makes TwinBench Different

- it measures runtime behavior, not only model answers
- it separates verified and projected evidence
- it publishes raw artifacts
- it treats unsupported dimensions honestly
- it is designed to be vendor-neutral and beatable in public

## What the Benchmark Produces

Each run produces:

- a JSON artifact
- a Markdown report
- an HTML report
- dimension-level evidence and coverage

## Where to Start

- first run: [GETTING_STARTED.md](GETTING_STARTED.md)
- compatibility: [COMPATIBILITY_CHECKLIST.md](COMPATIBILITY_CHECKLIST.md)
- preflight: [PREFLIGHT.md](PREFLIGHT.md)
- public results: [RESULTS_INDEX.md](RESULTS_INDEX.md)
- agent operators: [AGENT_RUN_GUIDE.md](AGENT_RUN_GUIDE.md)
