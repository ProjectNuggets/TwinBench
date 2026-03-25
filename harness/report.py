"""Report generation for TwinBench results."""

import json
from datetime import datetime

from .scorer import WEIGHTS, DIMENSION_LABELS, composite_score, rating_tier


def _result_class(results: dict, measured_coverage: float) -> str:
    artifact_type = results.get("artifact_type")
    if artifact_type == "external_estimate":
        return "External Estimate"
    if artifact_type == "live_gateway_run":
        if measured_coverage >= 0.75:
            return "Verified Reference Artifact"
        return "Partial Reference Artifact"
    return "Reference Artifact"


def _interpretation(results: dict, measured_coverage: float) -> str:
    reasons = results.get("dimension_reason_codes") or {}
    if reasons.get("scale_cost") == "multi_user_bootstrap_unavailable":
        return (
            "This run is trustworthy, but scale should be interpreted carefully: "
            "multi-user bootstrap was unavailable, so poor scale should not be inferred from that dimension alone."
        )
    if measured_coverage < 0.5:
        return (
            "This artifact is useful for reference, but too much of the benchmark remained unmeasured "
            "to treat the headline score as a complete runtime picture."
        )
    return (
        "This artifact is strong enough to compare publicly. Use the verified score for evidence-backed comparison "
        "and the projected score only as a clearly labeled estimate."
    )


def _status_for_dimension(results: dict, dim: str, dim_coverage: float) -> str:
    statuses = results.get("dimension_status") or {}
    if dim in statuses and statuses[dim]:
        return statuses[dim]
    if dim_coverage >= 1.0:
        return "measured"
    if dim_coverage > 0:
        return "partially_measured"
    return "unavailable"


def generate_markdown(results: dict, runtime_name: str = "Unknown") -> str:
    """Generate a Markdown report from benchmark results."""
    dim_scores = results.get(
        "dimension_projected_scores", results.get("dimension_scores", {})
    )
    verified_dim_scores = results.get("dimension_verified_scores", dim_scores)
    coverage = results.get("dimension_measured_coverage", {})

    projected_total = results.get("projected_composite_score", composite_score(dim_scores))
    verified_total = results.get("verified_composite_score", composite_score(verified_dim_scores))
    measured_coverage = results.get("measured_coverage", 1.0)
    coverage_adjusted = results.get(
        "coverage_adjusted_verified_score", round(verified_total * measured_coverage, 1)
    )
    tier = rating_tier(coverage_adjusted)
    result_class = results.get("result_class", _result_class(results, measured_coverage))
    interpretation = results.get("interpretation", _interpretation(results, measured_coverage))
    reason_codes = results.get("dimension_reason_codes") or {}

    lines = [
        f"# TwinBench Results: {runtime_name}",
        "",
        f"**Date**: {results.get('date', datetime.now().isoformat()[:10])}",
        f"**Benchmark Version**: TwinBench v{results.get('benchmark_version', '0.2')}",
        f"**Runtime URL**: {results.get('url', 'N/A')}",
        f"**Result Class**: {result_class}",
        "",
        "---",
        "",
        f"## Verified Composite Score: {coverage_adjusted}/100 — {tier}",
        "",
        f"- Verified raw: **{verified_total}/100**",
        f"- Measured coverage: **{round(measured_coverage * 100)}%**",
        f"- Projected composite: **{projected_total}/100**",
        f"- Interpretation: **{interpretation}**",
        "",
        "## Benchmark Principles",
        "",
        "- unsupported is not failure",
        "- missing bootstrap is not poor scale",
        "- same-user contention is diagnostic",
        "- evidence beats claims",
        "",
        "### Dimension Breakdown",
        "",
        "| Dimension | Status | Reason Code | Weight | Verified | Projected | Coverage | V Weighted | P Weighted |",
        "|-----------|--------|-------------|--------|----------|-----------|----------|------------|------------|",
    ]

    for dim, weight in WEIGHTS.items():
        verified_score = verified_dim_scores.get(dim, 0)
        projected_score = dim_scores.get(dim, 0)
        dim_coverage = coverage.get(dim, 1.0)
        dim_status = _status_for_dimension(results, dim, dim_coverage)
        reason_code = reason_codes.get(dim, "")
        weighted_verified = round(verified_score * weight * dim_coverage, 2)
        weighted_projected = round(projected_score * weight, 2)
        label = DIMENSION_LABELS.get(dim, dim)
        lines.append(
            f"| {label} | {dim_status} | {reason_code} | {weight:.2f} | {verified_score:.0f} | {projected_score:.0f} | {dim_coverage:.0%} | {weighted_verified:.2f} | {weighted_projected:.2f} |"
        )

    lines.append(
        f"| **Verified Composite** | **1.00** | **{verified_total:.1f}** |  | **{measured_coverage:.0%}** | **{coverage_adjusted:.1f}** |  |"
    )
    lines.append(
        f"| **Projected Composite** | **1.00** |  | **{projected_total:.1f}** |  |  | **{projected_total:.1f}** |"
    )
    lines.append("")

    # Details per dimension
    details = results.get("dimension_details", {})
    if details:
        lines.append("---")
        lines.append("")
        lines.append("## Dimension Details")
        lines.append("")
        for dim, detail in details.items():
            label = DIMENSION_LABELS.get(dim, dim)
            lines.append(f"### {label}")
            lines.append("")
            if isinstance(detail, dict):
                for k, v in detail.items():
                    if k == "score":
                        continue
                    lines.append(f"- **{k}**: {v}")
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(
        f"*Generated by TwinBench v{results.get('benchmark_version', '0.2')} — {datetime.now().isoformat()[:10]}*"
    )
    return "\n".join(lines)


def generate_html(results: dict, runtime_name: str = "Unknown") -> str:
    """Generate a self-contained HTML report from benchmark results."""
    dim_scores = results.get(
        "dimension_projected_scores", results.get("dimension_scores", {})
    )
    verified_dim_scores = results.get("dimension_verified_scores", dim_scores)
    coverage = results.get("dimension_measured_coverage", {})

    projected_total = results.get("projected_composite_score", composite_score(dim_scores))
    verified_total = results.get("verified_composite_score", composite_score(verified_dim_scores))
    measured_coverage = results.get("measured_coverage", 1.0)
    coverage_adjusted = results.get(
        "coverage_adjusted_verified_score", round(verified_total * measured_coverage, 1)
    )
    tier = rating_tier(coverage_adjusted)
    date = results.get("date", datetime.now().isoformat()[:10])
    result_class = results.get("result_class", _result_class(results, measured_coverage))
    interpretation = results.get("interpretation", _interpretation(results, measured_coverage))
    reason_codes = results.get("dimension_reason_codes") or {}

    tier_color = {
        "Category Leader": "#22c55e",
        "Production-Grade": "#3b82f6",
        "Competitive": "#8b5cf6",
        "Emerging": "#f59e0b",
        "Specialized": "#f97316",
        "Early Stage": "#ef4444",
    }.get(tier, "#6b7280")

    rows = []
    for dim, weight in WEIGHTS.items():
        verified_score = verified_dim_scores.get(dim, 0)
        projected_score = dim_scores.get(dim, 0)
        dim_coverage = coverage.get(dim, 1.0)
        dim_status = _status_for_dimension(results, dim, dim_coverage)
        reason_code = reason_codes.get(dim, "")
        weighted_verified = round(verified_score * weight * dim_coverage, 2)
        weighted_projected = round(projected_score * weight, 2)
        label = DIMENSION_LABELS.get(dim, dim)
        bar_width = max(2, int(verified_score))
        bar_color = (
            "#22c55e"
            if verified_score >= 80
            else "#f59e0b"
            if verified_score >= 60
            else "#ef4444"
        )
        rows.append(f"""
        <tr>
            <td>{label}</td>
            <td>{_escape(dim_status)}</td>
            <td>{_escape(reason_code)}</td>
            <td>{weight:.2f}</td>
            <td>
                <div style="display:flex;align-items:center;gap:8px">
                    <div style="background:{bar_color};height:18px;width:{bar_width}%;border-radius:3px;min-width:4px"></div>
                    <span>{verified_score:.0f}</span>
                </div>
            </td>
            <td>{projected_score:.0f}</td>
            <td>{dim_coverage:.0%}</td>
            <td>{weighted_verified:.2f}</td>
            <td>{weighted_projected:.2f}</td>
        </tr>""")

    detail_sections = []
    details = results.get("dimension_details", {})
    for dim, detail in details.items():
        label = DIMENSION_LABELS.get(dim, dim)
        items = ""
        if isinstance(detail, dict):
            for k, v in detail.items():
                if k == "score":
                    continue
                items += f"<li><strong>{k}</strong>: {_escape(str(v))}</li>\n"
        detail_sections.append(f"<h3>{label}</h3><ul>{items}</ul>")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TwinBench Results — {_escape(runtime_name)}</title>
<style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f8fafc; color: #1e293b; padding: 2rem; max-width: 900px; margin: 0 auto; }}
    h1 {{ font-size: 1.8rem; margin-bottom: 0.5rem; }}
    h2 {{ font-size: 1.3rem; margin: 1.5rem 0 0.8rem; color: #334155; }}
    h3 {{ font-size: 1.1rem; margin: 1rem 0 0.5rem; color: #475569; }}
    .meta {{ color: #64748b; font-size: 0.9rem; margin-bottom: 1.5rem; }}
    .score-card {{ background: white; border-radius: 12px; padding: 2rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 1.5rem; text-align: center; }}
    .score-number {{ font-size: 4rem; font-weight: 800; color: #0f172a; }}
    .score-tier {{ display: inline-block; padding: 0.3rem 1rem; border-radius: 20px; color: white; font-weight: 600; font-size: 1.1rem; margin-top: 0.5rem; }}
    .pill {{ display:inline-block;padding:0.2rem 0.6rem;border-radius:999px;background:#e2e8f0;color:#334155;font-size:0.85rem;font-weight:600; }}
    table {{ width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 1.5rem; }}
    th {{ background: #f1f5f9; text-align: left; padding: 0.75rem 1rem; font-weight: 600; font-size: 0.85rem; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; }}
    td {{ padding: 0.75rem 1rem; border-top: 1px solid #e2e8f0; }}
    tr:hover {{ background: #f8fafc; }}
    .details {{ background: white; border-radius: 8px; padding: 1.5rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 1rem; }}
    .details ul {{ padding-left: 1.5rem; }}
    .details li {{ margin: 0.3rem 0; font-size: 0.9rem; }}
    .footer {{ text-align: center; color: #94a3b8; font-size: 0.8rem; margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #e2e8f0; }}
    .nn {{ font-weight: 600; color: #64748b; }}
</style>
</head>
<body>
<h1>TwinBench Results</h1>
<div class="meta">{_escape(runtime_name)} — {date} — TwinBench v{results.get("benchmark_version", "0.2")}</div>

<div class="score-card">
    <div class="score-number">{coverage_adjusted:.0f}</div>
    <div>/100</div>
    <div class="score-tier" style="background:{tier_color}">{tier}</div>
    <div style="margin-top:0.8rem"><span class="pill">{_escape(result_class)}</span></div>
    <div style="margin-top:0.8rem;color:#475569">Verified raw: {verified_total:.1f} | Coverage: {measured_coverage:.0%} | Projected: {projected_total:.1f}</div>
</div>

<div class="details">
    <h2>Interpretation</h2>
    <p style="line-height:1.6;color:#475569">{_escape(interpretation)}</p>
    <h3 style="margin-top:1rem">Benchmark Principles</h3>
    <ul>
        <li>unsupported is not failure</li>
        <li>missing bootstrap is not poor scale</li>
        <li>same-user contention is diagnostic</li>
        <li>evidence beats claims</li>
    </ul>
</div>

<h2>Dimension Breakdown</h2>
<table>
    <thead>
        <tr><th>Dimension</th><th>Status</th><th>Reason Code</th><th>Weight</th><th>Verified</th><th>Projected</th><th>Coverage</th><th>V Weighted</th><th>P Weighted</th></tr>
    </thead>
    <tbody>
        {"".join(rows)}
        <tr style="font-weight:700;border-top:2px solid #cbd5e1">
            <td>Verified Composite</td><td>1.00</td><td>{verified_total:.1f}</td><td></td><td>{measured_coverage:.0%}</td><td>{coverage_adjusted:.1f}</td><td></td>
        </tr>
        <tr style="font-weight:700;border-top:2px solid #cbd5e1">
            <td>Projected Composite</td><td>1.00</td><td></td><td>{projected_total:.1f}</td><td></td><td></td><td>{projected_total:.1f}</td>
        </tr>
    </tbody>
</table>

{"<h2>Dimension Details</h2>" if detail_sections else ""}
{"".join(f'<div class="details">{s}</div>' for s in detail_sections)}

<div class="footer">
    <span class="nn">TwinBench v{results.get("benchmark_version", "0.2")}</span> — Published by Nova Nuggets — novanuggets.com
</div>
</body>
</html>"""


def _escape(s: str | None) -> str:
    if s is None:
        return ""
    s = str(s)
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )
