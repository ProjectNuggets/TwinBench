"""Dimension 5: Integration Breadth — channels, tools, backends, APIs."""

from .config import BenchConfig
from .sse_client import get_diagnostics, get_metrics, health_check, chat
from .scorer import log2_breadth_score
from .evidence import extract_json_object, live_integration_counts, used_tool


def run(config: BenchConfig) -> dict:
    """Count and verify functional integrations from diagnostics and runtime_info."""
    results = {}

    # Health check
    healthy = health_check(config)
    results["health_endpoint_ok"] = healthy

    # Fetch diagnostics for live integration counts
    diag = get_diagnostics(config)
    channels = 0
    tools = 0
    backends = 0
    integrations = 0
    component_coverage = {
        "channels": 0.0,
        "tools": 0.0,
        "backends": 0.0,
        "integrations": 0.0,
    }

    if diag:
        results["diagnostics_available"] = True
        configured_channels, connected_channels = live_integration_counts(diag)
        channels = max(configured_channels, connected_channels)
        if channels > 0:
            component_coverage["channels"] = 0.30
        integrations = configured_channels
        if integrations > 0:
            component_coverage["integrations"] = 0.20

    else:
        results["diagnostics_available"] = False

    # Try to get structured counts from runtime_info
    r = chat(
        config,
        "Use runtime_info and return concise JSON only with these keys: enabled_tools_count, channels_count, memory_backends_count, integrations_count, state_backend, provider, model.",
    )
    runtime_info_payload = extract_json_object(r.get("content", ""))
    runtime_info_used = used_tool(r, "runtime_info")
    results["runtime_info_tool_used"] = runtime_info_used
    results["runtime_info_payload"] = runtime_info_payload

    if runtime_info_used and runtime_info_payload:
        if runtime_info_payload.get("enabled_tools_count"):
            tools = int(runtime_info_payload["enabled_tools_count"])
            component_coverage["tools"] = 0.30
        if runtime_info_payload.get("channels_count"):
            channels = max(channels, int(runtime_info_payload["channels_count"]))
            component_coverage["channels"] = max(component_coverage["channels"], 0.30)
        if runtime_info_payload.get("memory_backends_count"):
            backends = int(runtime_info_payload["memory_backends_count"])
            component_coverage["backends"] = 0.20
        if runtime_info_payload.get("integrations_count"):
            integrations = max(integrations, int(runtime_info_payload["integrations_count"]))
            component_coverage["integrations"] = max(component_coverage["integrations"], 0.20)

    results["channels"] = channels
    results["tools"] = tools
    results["memory_backends"] = backends
    results["integrations"] = integrations

    # Metrics check
    metrics = get_metrics(config)
    results["metrics_available"] = metrics is not None

    # Score
    projected_score = log2_breadth_score(channels, tools, backends, integrations)
    measured_coverage = round(sum(component_coverage.values()), 2)
    verified_score = projected_score if measured_coverage > 0 else 0.0
    results["score"] = round(projected_score, 1)
    results["verified_score"] = round(verified_score, 1)
    results["projected_score"] = round(projected_score, 1)
    results["measured_coverage"] = round(measured_coverage, 2)
    results["component_coverage"] = component_coverage
    return {
        "dimension": "integration_breadth",
        "score": results["score"],
        "verified_score": results["verified_score"],
        "projected_score": results["projected_score"],
        "measured_coverage": results["measured_coverage"],
        "details": results,
    }
