# How to Read a TwinBench Artifact

TwinBench artifacts are designed to stay trustworthy even when a runtime only supports part of the category.

## High-Signal Fields

- `verified_composite_score`: score from directly measured evidence
- `projected_composite_score`: score including clearly labeled assumptions
- `measured_coverage`: fraction of benchmark weight directly exercised
- `coverage_adjusted_verified_score`: leaderboard-facing score
- `dimension_status`: measured, partially measured, unavailable, or error
- `dimension_reason_codes`: short reason codes for unavailable or partial dimensions

## What “Unavailable” Means

Unavailable does **not** always mean weak product capability.

It can mean:

- contract mismatch
- missing diagnostics surface
- bootstrap unavailable
- runtime unavailable during probe
- environment setup missing

## What “Partially Measured” Means

Partially measured means the benchmark saw some real evidence, but not enough to fully exercise the dimension.

Examples:

- only one live channel was connected for cross-channel checks
- only a subset of benchmark users could be provisioned for scale
- architectural signals were available, but not all live behaviors were exercised

## Worked Example: Scale

Bad interpretation:

- “This runtime has poor scale.”

Correct interpretation:

- “This runtime did not expose fair multi-user bootstrap for this run, so multi-user scale readiness was only partially measurable.”

## Why This Matters

TwinBench is strongest when readers can tell the difference between:

- true capability failure
- missing runtime surface
- upstream outage
- setup or bootstrap limitation
