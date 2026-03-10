#!/usr/bin/env python3
"""DTaaS-Bench Runner — benchmark any persistent autonomous AI agent runtime.

Usage:
    python -m harness.runner --url http://localhost:8080 --token TOKEN --user-id 1
    python -m harness.runner --url http://localhost:8080 --token TOKEN --user-id 1 --dimensions memory,security
    python -m harness.runner --url http://localhost:8080 --token TOKEN --user-id 1 --output results/run.json --html results/run.html
"""

import argparse
import json
import sys
import time
from datetime import datetime

from rich.console import Console
from rich.table import Table

from .config import BenchConfig
from .scorer import WEIGHTS, DIMENSION_LABELS, composite_score, rating_tier
from .report import generate_markdown, generate_html
from . import dim1_autonomy
from . import dim2_memory
from . import dim3_execution
from . import dim4_crosschannel
from . import dim5_breadth
from . import dim6_security
from . import dim7_scale
from . import dim8_resilience
from . import dim9_latency
from . import dim10_functional

DIMENSION_MAP = {
    "autonomy": ("autonomy_control", dim1_autonomy),
    "memory": ("memory_persistence", dim2_memory),
    "functional": ("functional_capability", dim10_functional),
    "execution": ("autonomous_execution", dim3_execution),
    "crosschannel": ("cross_channel", dim4_crosschannel),
    "breadth": ("integration_breadth", dim5_breadth),
    "security": ("security_privacy", dim6_security),
    "scale": ("scale_cost", dim7_scale),
    "resilience": ("resilience", dim8_resilience),
    "latency": ("latency", dim9_latency),
}

console = Console()


def main():
    parser = argparse.ArgumentParser(
        description="DTaaS-Bench: benchmark a DTaaS runtime"
    )
    parser.add_argument(
        "--url", required=True, help="Runtime base URL (e.g. http://localhost:8080)"
    )
    parser.add_argument("--token", required=True, help="Internal API token")
    parser.add_argument(
        "--user-id", default="1", help="User ID for tenant context (default: 1)"
    )
    parser.add_argument(
        "--dimensions",
        default="all",
        help="Comma-separated dimensions to run (default: all)",
    )
    parser.add_argument("--output", help="Output JSON file path")
    parser.add_argument("--html", help="Output HTML report file path")
    parser.add_argument("--markdown", help="Output Markdown report file path")
    parser.add_argument(
        "--name", default="Unknown Runtime", help="Runtime name for reports"
    )
    parser.add_argument(
        "--timeout", type=int, default=90, help="Chat timeout in seconds (default: 90)"
    )
    parser.add_argument(
        "--skip-schedule-wait",
        action="store_true",
        help="Skip the 3-minute schedule execution wait",
    )
    args = parser.parse_args()

    config = BenchConfig(
        base_url=args.url.rstrip("/"),
        token=args.token,
        user_id=args.user_id,
        timeout=args.timeout,
        schedule_wait_secs=0 if args.skip_schedule_wait else 180,
    )

    # Determine which dimensions to run
    if args.dimensions == "all":
        dims_to_run = list(DIMENSION_MAP.keys())
    else:
        dims_to_run = [d.strip() for d in args.dimensions.split(",")]
        for d in dims_to_run:
            if d not in DIMENSION_MAP:
                console.print(f"[red]Unknown dimension: {d}[/red]")
                console.print(f"Available: {', '.join(DIMENSION_MAP.keys())}")
                sys.exit(1)

    console.print()
    console.print("[bold]DTaaS-Bench v0.1[/bold]", style="blue")
    console.print(f"Runtime: {args.url}")
    console.print(f"User ID: {args.user_id}")
    console.print(f"Dimensions: {', '.join(dims_to_run)}")
    console.print()

    # Run dimensions
    all_results = {
        "benchmark_version": "0.1",
        "runtime_name": args.name,
        "url": args.url,
        "user_id": args.user_id,
        "date": datetime.now().isoformat()[:10],
        "dimension_scores": {},
        "dimension_details": {},
    }

    start_total = time.monotonic()

    for dim_key in dims_to_run:
        dim_id, dim_module = DIMENSION_MAP[dim_key]
        label = DIMENSION_LABELS.get(dim_id, dim_key)
        console.print(f"  Running [bold]{label}[/bold]...", end=" ")

        try:
            result = dim_module.run(config)
            score = result.get("score", 0)
            all_results["dimension_scores"][dim_id] = score
            all_results["dimension_details"][dim_id] = result.get("details", {})
            console.print(f"[green]{score:.0f}/100[/green]")
        except Exception as e:
            console.print(f"[red]ERROR: {e}[/red]")
            all_results["dimension_scores"][dim_id] = 0
            all_results["dimension_details"][dim_id] = {"error": str(e)}

    elapsed = time.monotonic() - start_total

    # Calculate composite
    total = composite_score(all_results["dimension_scores"])
    tier = rating_tier(total)
    all_results["composite_score"] = total
    all_results["rating"] = tier
    all_results["elapsed_seconds"] = round(elapsed, 1)

    # Display results table
    console.print()
    table = Table(title="DTaaS-Bench Results", show_lines=True)
    table.add_column("Dimension", style="bold")
    table.add_column("Weight", justify="right")
    table.add_column("Score", justify="right")
    table.add_column("Weighted", justify="right")

    for dim_id, weight in WEIGHTS.items():
        score = all_results["dimension_scores"].get(dim_id, 0)
        weighted = round(score * weight, 2)
        label = DIMENSION_LABELS.get(dim_id, dim_id)
        score_style = "green" if score >= 80 else "yellow" if score >= 60 else "red"
        table.add_row(
            label,
            f"{weight:.2f}",
            f"[{score_style}]{score:.0f}[/{score_style}]",
            f"{weighted:.2f}",
        )

    table.add_row(
        "[bold]Composite[/bold]", "[bold]1.00[/bold]", "", f"[bold]{total:.1f}[/bold]"
    )
    console.print(table)

    tier_style = (
        "green"
        if total >= 90
        else "blue"
        if total >= 75
        else "yellow"
        if total >= 60
        else "red"
    )
    console.print(
        f"\n  [bold {tier_style}]{total:.0f}/100 — {tier}[/bold {tier_style}]"
    )
    console.print(f"  Elapsed: {elapsed:.1f}s\n")

    # Write outputs
    if args.output:
        with open(args.output, "w") as f:
            json.dump(all_results, f, indent=2)
        console.print(f"  JSON: {args.output}")

    if args.markdown:
        md = generate_markdown(all_results, args.name)
        with open(args.markdown, "w") as f:
            f.write(md)
        console.print(f"  Markdown: {args.markdown}")

    if args.html:
        html = generate_html(all_results, args.name)
        with open(args.html, "w") as f:
            f.write(html)
        console.print(f"  HTML: {args.html}")

    console.print()


if __name__ == "__main__":
    main()
