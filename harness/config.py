"""DTaaS-Bench configuration."""

from dataclasses import dataclass, field


@dataclass
class BenchConfig:
    """Connection and runtime configuration for the benchmark harness."""

    base_url: str = "http://localhost:8080"
    token: str = ""
    user_id: str = "1"
    timeout: int = 90  # seconds per chat request (LLM can be slow)

    # Endpoints
    chat_endpoint: str = "/api/v1/chat/stream"
    health_endpoint: str = "/health"
    ready_endpoint: str = "/ready"
    diagnostics_endpoint: str = "/internal/diagnostics"
    metrics_endpoint: str = "/metrics"

    # Benchmark tuning
    memory_sample_size: int = 20  # facts to test (of 100 stored)
    scale_concurrency: int = 20  # concurrent requests for scale test
    latency_requests: int = 10  # requests for latency measurement
    schedule_wait_secs: int = 180  # wait time for schedule execution test

    @property
    def headers(self) -> dict:
        h = {"Content-Type": "application/json"}
        if self.token:
            h["X-Internal-Token"] = self.token
        if self.user_id:
            h["X-Zaki-User-Id"] = self.user_id
        return h

    def chat_url(self) -> str:
        return f"{self.base_url}{self.chat_endpoint}"

    def health_url(self) -> str:
        return f"{self.base_url}{self.health_endpoint}"

    def diagnostics_url(self) -> str:
        return f"{self.base_url}{self.diagnostics_endpoint}"

    def metrics_url(self) -> str:
        return f"{self.base_url}{self.metrics_endpoint}"
