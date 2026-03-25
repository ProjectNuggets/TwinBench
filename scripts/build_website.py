#!/usr/bin/env python3
"""Build a static TwinBench website from checked-in result artifacts."""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from harness.scorer import DIMENSION_LABELS
RESULTS_DIR = ROOT / "results"
WEBSITE_DIR = ROOT / "website"
WEBSITE_RESULTS_DIR = WEBSITE_DIR / "results"
WEBSITE_ASSETS_DIR = WEBSITE_DIR / "assets"
DATA_DIR = WEBSITE_DIR / "data"
ARTIFACTS_DIR = WEBSITE_DIR / "artifacts"

CANONICAL_SLUG = "nullalis-live-2026-03-25-openended"
EXCLUDE_SLUGS = {"nullalis-smoke-autonomy", "nullalis-v0.1", "nullalis-v0.2"}


def _load_results() -> list[dict]:
    items = []
    for path in sorted(RESULTS_DIR.glob("*.json")):
        slug = path.stem
        if slug in EXCLUDE_SLUGS:
            continue
        data = json.loads(path.read_text())
        if "coverage_adjusted_verified_score" not in data:
            continue
        item = {
            "slug": slug,
            "runtime_name": data.get("runtime_name", slug),
            "date": data.get("date", ""),
            "coverage_adjusted_verified_score": data.get("coverage_adjusted_verified_score", 0),
            "verified_composite_score": data.get("verified_composite_score", 0),
            "projected_composite_score": data.get("projected_composite_score", 0),
            "measured_coverage": data.get("measured_coverage", 0),
            "rating": data.get("rating", "Unknown"),
            "artifact_type": data.get("artifact_type", ""),
            "result_class": data.get("result_class") or (
                "Reference Runtime" if slug == CANONICAL_SLUG else "Supporting Artifact"
            ),
            "details": data.get("dimension_details", {}),
            "dimension_status": data.get("dimension_status", {}),
            "dimension_reason_codes": data.get("dimension_reason_codes", {}),
        }
        if slug == "twinbench-demo-runtime":
            item["result_class"] = "Demo Fixture"
            item["headline_note"] = "Fast fixture runtime used for the one-click TwinBench demo path."
        elif slug == CANONICAL_SLUG:
            item["headline_note"] = (
                "Current public reference result. Scale interpretation is conservative relative to the later provisioning-aware scale fix."
            )
        elif "auth-poisoned" in slug or slug.endswith("2026-03-25"):
            item["headline_note"] = "Supporting degraded artifact preserved for audit."
        elif "scale-probe" in slug:
            item["headline_note"] = "Supporting fairness probe, not a replacement full-run score."
        else:
            item["headline_note"] = "Supporting TwinBench artifact."
        items.append(item)
    items.sort(key=lambda x: (x["coverage_adjusted_verified_score"], x["verified_composite_score"]), reverse=True)
    return items


def _mkdirs() -> None:
    if WEBSITE_RESULTS_DIR.exists():
        shutil.rmtree(WEBSITE_RESULTS_DIR)
    if DATA_DIR.exists():
        shutil.rmtree(DATA_DIR)
    if ARTIFACTS_DIR.exists():
        shutil.rmtree(ARTIFACTS_DIR)
    for section in ("methodology", "faq", "submit", "compare"):
        page_dir = WEBSITE_DIR / section
        if page_dir.exists():
            shutil.rmtree(page_dir)
    WEBSITE_RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    WEBSITE_ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)


def _copy_assets() -> None:
    for asset in [
        "benchmark-score-card.png",
        "benchmark-score-card.svg",
        "ten-dimensions.svg",
        "what-current-benchmarks-miss.svg",
    ]:
        shutil.copy2(ROOT / "assets" / asset, WEBSITE_ASSETS_DIR / asset)
    (WEBSITE_DIR / ".nojekyll").write_text("")


def _copy_result_artifacts(slug: str) -> dict[str, str]:
    copied = {}
    for suffix in ("json", "md", "html"):
        src = RESULTS_DIR / f"{slug}.{suffix}"
        if src.exists():
            dst = ARTIFACTS_DIR / src.name
            shutil.copy2(src, dst)
            copied[suffix] = f"../../artifacts/{src.name}"
    return copied


def _site_css() -> str:
    return """
:root {
  --bg: #f6f1e8;
  --paper: #fffaf1;
  --ink: #17212b;
  --muted: #5f6b75;
  --accent: #0f7b6c;
  --accent-2: #f49e27;
  --line: #dccfb7;
  --good: #198754;
  --warn: #d97706;
  --bad: #d83b3b;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: Georgia, "Iowan Old Style", "Palatino Linotype", serif;
  background:
    radial-gradient(circle at top left, rgba(244,158,39,0.18), transparent 24rem),
    radial-gradient(circle at right, rgba(15,123,108,0.14), transparent 28rem),
    var(--bg);
  color: var(--ink);
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
.shell { max-width: 1120px; margin: 0 auto; padding: 24px; }
.hero, .panel {
  background: rgba(255,250,241,0.88);
  border: 1px solid var(--line);
  border-radius: 22px;
  box-shadow: 0 12px 30px rgba(37, 29, 15, 0.08);
}
.hero { padding: 36px; margin-bottom: 24px; }
.eyebrow {
  display: inline-block;
  margin-bottom: 14px;
  font: 600 12px/1.2 ui-monospace, SFMono-Regular, Menlo, monospace;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
}
h1, h2, h3 { margin: 0 0 14px; line-height: 1.05; }
h1 { font-size: clamp(2.4rem, 5vw, 4.6rem); max-width: 12ch; }
h2 { font-size: clamp(1.4rem, 2vw, 2rem); }
h3 { font-size: 1.1rem; }
p { color: var(--muted); font-size: 1.04rem; line-height: 1.65; }
.lede { font-size: 1.16rem; max-width: 60ch; }
.actions, .nav, .stats, .grid { display: flex; gap: 12px; flex-wrap: wrap; }
.nav { margin-bottom: 18px; }
.nav a {
  padding: 8px 12px;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: rgba(255,255,255,0.65);
  color: var(--ink);
}
.button {
  display: inline-block;
  padding: 12px 16px;
  border-radius: 999px;
  border: 1px solid var(--accent);
  background: var(--accent);
  color: white;
  font-weight: 700;
}
.button.secondary {
  background: transparent;
  color: var(--accent);
}
.stats { margin-top: 22px; }
.stat, .card, .tile {
  background: rgba(255,255,255,0.68);
  border: 1px solid var(--line);
  border-radius: 18px;
}
.stat { padding: 14px 16px; min-width: 170px; }
.stat strong { display: block; font-size: 1.8rem; color: var(--ink); }
.section { margin: 26px 0; }
.grid { align-items: stretch; }
.card { padding: 18px; flex: 1 1 280px; }
.card ul, .prose ul { color: var(--muted); line-height: 1.7; }
.leaderboard { overflow-x: auto; }
table {
  width: 100%;
  border-collapse: collapse;
  background: rgba(255,255,255,0.72);
  border-radius: 18px;
  overflow: hidden;
}
th, td { padding: 14px 16px; border-bottom: 1px solid var(--line); text-align: left; }
th {
  font: 700 12px/1.2 ui-monospace, SFMono-Regular, Menlo, monospace;
  text-transform: uppercase;
  letter-spacing: 0.09em;
  color: var(--muted);
}
.score {
  font: 800 1.8rem/1 ui-monospace, SFMono-Regular, Menlo, monospace;
  color: var(--ink);
}
.pill {
  display: inline-block;
  padding: 6px 10px;
  border-radius: 999px;
  font: 700 12px/1.2 ui-monospace, SFMono-Regular, Menlo, monospace;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  background: rgba(15,123,108,0.1);
  color: var(--accent);
}
.pill.warn { background: rgba(217,119,6,0.12); color: var(--warn); }
.pill.bad { background: rgba(216,59,59,0.12); color: var(--bad); }
.tile { padding: 18px; }
.tile .score { margin-bottom: 8px; }
.two-col { display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 18px; }
.prose, .panel { padding: 24px; }
.footer {
  margin: 34px 0 12px;
  color: var(--muted);
  font-size: 0.95rem;
}
code, pre {
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
}
pre {
  background: #1d2330;
  color: #f8fafc;
  padding: 16px;
  border-radius: 16px;
  overflow: auto;
}
@media (max-width: 860px) {
  .two-col { grid-template-columns: 1fr; }
}
""".strip()


def _page(title: str, body: str, depth: int = 0) -> str:
    prefix = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="stylesheet" href="{prefix}site.css">
</head>
<body>
  <div class="shell">
    <div class="nav">
      <a href="{prefix}index.html">Home</a>
      <a href="{prefix}methodology/index.html">Methodology</a>
      <a href="{prefix}faq/index.html">FAQ</a>
      <a href="{prefix}submit/index.html">Submit</a>
      <a href="{prefix}compare/index.html">Compare</a>
      <a href="https://github.com/ProjectNuggets/DTaaS-benchmark">GitHub</a>
    </div>
    {body}
    <div class="footer">
      TwinBench is published by Nova Nuggets, an AI innovation company building toward personal, secure, sovereign AI for everyone.
    </div>
  </div>
</body>
</html>"""


def _render_home(results: list[dict]) -> str:
    top = results[0]
    rows = []
    for item in results[:8]:
        score = item["coverage_adjusted_verified_score"]
        coverage = round(item["measured_coverage"] * 100)
        rows.append(
            f"<tr><td><a href='results/{item['slug']}/index.html'>{item['runtime_name']}</a></td>"
            f"<td><span class='pill'>{item['result_class']}</span></td>"
            f"<td>{item['rating']}</td>"
            f"<td class='score'>{score:.1f}</td>"
            f"<td>{coverage}%</td>"
            f"<td>{item['date']}</td></tr>"
        )
    return _page(
        "TwinBench — The benchmark for personal AI assistants",
        f"""
<section class="hero">
  <div class="eyebrow">The open benchmark for personal AI assistants</div>
  <h1>TwinBench</h1>
  <p class="lede">TwinBench measures whether an AI system can behave like a real personal AI assistant: remember, act, follow up, stay safe, and operate over time.</p>
  <div class="actions">
    <a class="button" href="results/{top['slug']}/index.html">See the Reference Result</a>
    <a class="button secondary" href="submit/index.html">Submit Your Assistant</a>
  </div>
  <div class="stats">
    <div class="stat"><strong>{len(results)}</strong> Checked-in artifacts</div>
    <div class="stat"><strong>{top['coverage_adjusted_verified_score']:.1f}</strong> Current top score</div>
    <div class="stat"><strong>{round(top['measured_coverage'] * 100)}%</strong> Reference coverage</div>
  </div>
</section>

<section class="two-col section">
  <div class="panel">
    <div class="eyebrow">Leaderboard</div>
    <h2>Current public board</h2>
    <p>The board is one place, but every result keeps its class, coverage, and evidence story. Trust comes from artifacts, not claims.</p>
    <div class="leaderboard">
      <table>
        <thead><tr><th>Assistant</th><th>Class</th><th>Tier</th><th>Score</th><th>Coverage</th><th>Date</th></tr></thead>
        <tbody>{''.join(rows)}</tbody>
      </table>
    </div>
  </div>
  <div class="panel">
    <div class="eyebrow">Why it matters</div>
    <h2>What current benchmarks miss</h2>
    <p>Most AI benchmarks still measure chat quality, coding skill, or one-shot tasks. TwinBench focuses on the missing category: personal AI assistants that persist and operate over time.</p>
    <img src="assets/what-current-benchmarks-miss.svg" alt="What current benchmarks miss" style="width:100%;border-radius:16px;border:1px solid var(--line)">
  </div>
</section>

<section class="grid section">
  <div class="card">
    <div class="eyebrow">Run it</div>
    <h3>10-minute path</h3>
    <p>Use the repo, the demo runtime, or hand TwinBench to Codex, Claude Code, or Cursor with one prompt.</p>
    <pre>make demo
make site</pre>
  </div>
  <div class="card">
    <div class="eyebrow">Trust</div>
    <h3>Evidence-first by design</h3>
    <ul>
      <li>unsupported is not failure</li>
      <li>missing bootstrap is not poor scale</li>
      <li>same-user contention is diagnostic</li>
      <li>measured coverage matters</li>
    </ul>
  </div>
  <div class="card">
    <div class="eyebrow">Challenge</div>
    <h3>Can your assistant beat this?</h3>
    <p>Every serious result should be artifact-backed, shareable, and easy to challenge in public.</p>
    <img src="assets/benchmark-score-card.png" alt="TwinBench score card" style="width:100%;border-radius:16px;border:1px solid var(--line)">
  </div>
</section>

<section class="grid section">
  <div class="card">
    <div class="eyebrow">Community</div>
    <h3>GitHub first</h3>
    <p>TwinBench starts with Discussions, issues, and submissions on GitHub. That keeps the benchmark legible and searchable while the ecosystem is still forming.</p>
    <p><a class="button secondary" href="https://github.com/ProjectNuggets/DTaaS-benchmark/discussions">Open Discussions</a></p>
  </div>
  <div class="card">
    <div class="eyebrow">Challenge loop</div>
    <h3>Monthly challenge shape</h3>
    <p>Reference Runtime, Top Score This Month, Most Improved, and Verified Artifact are the first public loops. The goal is recognition without hype.</p>
    <p><a href="https://github.com/ProjectNuggets/DTaaS-benchmark/blob/main/docs/MONTHLY_CHALLENGE.md">Read the challenge shape</a></p>
  </div>
</section>
""",
    )


def _render_result(item: dict) -> str:
    details = item["details"]
    artifact_links = item["artifact_links"]
    detail_items = []
    for dim, info in details.items():
        verified = info.get("verified_score", info.get("score", 0)) if isinstance(info, dict) else 0
        reason = item["dimension_reason_codes"].get(dim) or ""
        status = item["dimension_status"].get(dim, "measured")
        label = DIMENSION_LABELS.get(dim, dim)
        detail_items.append(
            f"<div class='tile'><strong>{label}</strong><div class='score'>{verified:.1f}</div><div><span class='pill'>{status}</span> {reason}</div></div>"
        )
    links = []
    if "json" in artifact_links:
        links.append(f"<a href='{artifact_links['json']}'>JSON artifact</a>")
    if "md" in artifact_links:
        links.append(f"<a href='{artifact_links['md']}'>Markdown report</a>")
    if "html" in artifact_links:
        links.append(f"<a href='{artifact_links['html']}'>HTML report</a>")
    return _page(
        f"{item['runtime_name']} — TwinBench result",
        f"""
<section class="hero">
  <div class="eyebrow">{item['result_class']}</div>
  <h1>{item['runtime_name']}</h1>
  <p class="lede">{item['headline_note']}</p>
  <div class="stats">
    <div class="stat"><strong>{item['coverage_adjusted_verified_score']:.1f}</strong> Coverage-adjusted verified</div>
    <div class="stat"><strong>{item['verified_composite_score']:.1f}</strong> Verified raw</div>
    <div class="stat"><strong>{round(item['measured_coverage'] * 100)}%</strong> Measured coverage</div>
  </div>
</section>

<section class="two-col section">
  <div class="panel">
    <div class="eyebrow">Interpretation</div>
    <h2>{item['rating']}</h2>
    <p>{item['headline_note']}</p>
    <p>{' · '.join(links)}</p>
  </div>
  <div class="panel">
    <div class="eyebrow">Share</div>
    <h2>Share this result</h2>
    <p>Use this page as the canonical public result URL for quoting, screenshots, or side-by-side comparison.</p>
    <p><a class="button secondary" href="../../compare/index.html?left={CANONICAL_SLUG}&right={item['slug']}">Compare with reference</a></p>
  </div>
</section>

<section class="section">
  <div class="eyebrow">Dimension tiles</div>
  <div class="grid">{''.join(detail_items)}</div>
</section>
""",
        depth=2,
    )


def _render_methodology() -> str:
    return _page(
        "TwinBench Methodology",
        """
<section class="hero">
  <div class="eyebrow">Methodology</div>
  <h1>How TwinBench works</h1>
  <p class="lede">TwinBench is one benchmark family for personal AI assistants. It reports verified evidence, projected score, measured coverage, and dimension-level reason codes so weak coverage stays visible.</p>
</section>

<section class="grid section">
  <div class="card"><h3>One board, clear classes</h3><p>TwinBench should become a public board, but every result must keep its class, coverage, and evidence basis.</p></div>
  <div class="card"><h3>Coverage matters</h3><p>The headline ranking number is coverage-adjusted verified score, not the most flattering number in the artifact.</p></div>
  <div class="card"><h3>Trust over hype</h3><p>Unsupported surfaces, missing bootstrap, and partial measurement are reported explicitly instead of flattened into a false failure.</p></div>
</section>
""",
    )


def _render_faq() -> str:
    return _page(
        "TwinBench FAQ",
        """
<section class="hero">
  <div class="eyebrow">FAQ</div>
  <h1>Common questions</h1>
  <p class="lede">TwinBench is meant to be understandable by experts and normal builders alike.</p>
</section>

<section class="panel prose">
  <h2>Is this a chatbot benchmark?</h2>
  <p>No. TwinBench is about long-lived assistant behavior, not just one-turn chat quality.</p>
  <h2>Is this only for Nullalis?</h2>
  <p>No. Nullalis is the current reference runtime because it produced the first strong public artifact.</p>
  <h2>Can I run TwinBench quickly?</h2>
  <p>Yes. Use the demo path from the repo or run against a native runtime with one command.</p>
  <h2>What if my assistant only supports part of the benchmark?</h2>
  <p>That is still useful. TwinBench prefers honest partial artifacts over fake comparability.</p>
</section>
""",
    )


def _render_submit() -> str:
    return _page(
        "Submit to TwinBench",
        """
<section class="hero">
  <div class="eyebrow">Submit</div>
  <h1>Submit your assistant</h1>
  <p class="lede">TwinBench should be easy to challenge. A good submission is artifact-backed, honest about coverage, and easy for others to inspect.</p>
</section>

<section class="panel prose">
  <h2>Minimum submission pack</h2>
  <ul>
    <li>benchmark JSON artifact</li>
    <li>Markdown or HTML report</li>
    <li>runtime version or commit SHA</li>
    <li>harness version or commit SHA</li>
    <li>short incident notes if the run degraded</li>
  </ul>
  <h2>Start here</h2>
  <p><a href="https://github.com/ProjectNuggets/DTaaS-benchmark/blob/main/docs/HOW_TO_SUBMIT.md">Submission guide</a></p>
  <p><a href="https://github.com/ProjectNuggets/DTaaS-benchmark/issues/new?template=submit-results.md">Open a results submission</a></p>
</section>
""",
    )


def _render_compare(results: list[dict]) -> str:
    options = "".join(
        f"<option value='{item['slug']}'>{item['runtime_name']} ({item['slug']})</option>"
        for item in results
    )
    return _page(
        "Compare TwinBench results",
        f"""
<section class="hero">
  <div class="eyebrow">Compare</div>
  <h1>Compare two results</h1>
  <p class="lede">Use this page when you want a clean side-by-side view instead of two tabs and a screenshot.</p>
</section>

<section class="panel prose">
  <label for="left">Left</label>
  <select id="left">{options}</select>
  <label for="right">Right</label>
  <select id="right">{options}</select>
  <p><button class="button" id="run-compare" type="button">Compare</button></p>
  <div id="compare-out"></div>
</section>
<script>
async function loadData() {{
  const response = await fetch('../data/results.json');
  return await response.json();
}}
function bySlug(items, slug) {{
  return items.find((item) => item.slug === slug);
}}
function render(item) {{
  if (!item) return '<p>Missing item.</p>';
  return `<div class="tile"><h3>${{item.runtime_name}}</h3><p class="score">${{item.coverage_adjusted_verified_score.toFixed(1)}}</p><p>${{item.result_class}} · coverage ${{Math.round(item.measured_coverage * 100)}}%</p></div>`;
}}
document.getElementById('run-compare').addEventListener('click', async () => {{
  const data = await loadData();
  const left = bySlug(data.results, document.getElementById('left').value);
  const right = bySlug(data.results, document.getElementById('right').value);
  document.getElementById('compare-out').innerHTML = `<div class="grid">${{render(left)}}${{render(right)}}</div>`;
}});
</script>
""",
    )


def build() -> None:
    _mkdirs()
    _copy_assets()
    results = _load_results()
    for item in results:
        item["artifact_links"] = _copy_result_artifacts(item["slug"])
    (WEBSITE_DIR / "site.css").write_text(_site_css())
    (DATA_DIR / "results.json").write_text(json.dumps({"results": results}, indent=2))

    (WEBSITE_DIR / "index.html").write_text(_render_home(results))

    for folder, html in {
        "methodology": _render_methodology(),
        "faq": _render_faq(),
        "submit": _render_submit(),
        "compare": _render_compare(results),
    }.items():
        p = WEBSITE_DIR / folder
        p.mkdir(parents=True, exist_ok=True)
        (p / "index.html").write_text(html)

    for item in results:
        p = WEBSITE_RESULTS_DIR / item["slug"]
        p.mkdir(parents=True, exist_ok=True)
        (p / "index.html").write_text(_render_result(item))


if __name__ == "__main__":
    build()
