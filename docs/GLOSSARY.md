# Glossary

## Personal AI Assistant Runtime

A runtime that aims to behave like a persistent assistant, not just a single-turn chatbot.

## Persistent Personal AI Assistant

An AI assistant that remembers, acts, follows up, and maintains state over time.

## DTaaS

Internal technical term in this repo for the runtime category behind persistent personal AI assistants. Useful for architecture discussions, but not required to understand TwinBench.

## Verified Score

A score based only on behavior or evidence directly measured in the run.

## Projected Score

A score that includes explicit assumptions for components not fully exercised.

## Measured Coverage

The fraction of total benchmark weight that was directly measured in the run.

## Coverage-Adjusted Verified Score

The leaderboard-facing score used for tiering. It prevents partial runs from looking deceptively complete.

## Same-Session Contention

Many requests against the same user/session. Useful as a diagnostic, but not the main claim for multi-user scale readiness.

## Provisioned Multi-User Parallelism

Concurrent requests across users that were successfully provisioned and accepted by the runtime.

## Bootstrap Availability

Whether a tenant-aware runtime can initialize the benchmark users needed for fair multi-user testing.
