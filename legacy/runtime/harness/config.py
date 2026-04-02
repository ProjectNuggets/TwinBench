"""TwinBench configuration."""

from dataclasses import dataclass, field


@dataclass
class BenchConfig:
    """Connection and runtime configuration for the benchmark harness."""

    base_url: str = "http://localhost:8080"
    token: str = ""
    user_id: str = "1"
    timeout: int = 90  # seconds per chat request; 0 disables per-chat timeout
    timeout_dynamic: bool = True
    timeout_floor_secs: int = 90
    timeout_ceiling_secs: int = 3600
    timeout_multiplier: float = 4.0
    timeout_grace_secs: int = 30

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
    session_namespace: str = "dtaas-bench"
    session_lane: str = "thread"

    # Adaptive timeout state (runtime-only; not user inputs)
    _latency_ewma_ms: float = field(default=0.0, init=False, repr=False)
    _latency_samples: int = field(default=0, init=False, repr=False)
    _last_timeout_used_secs: int | None = field(default=None, init=False, repr=False)

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

    def resolve_chat_timeout_secs(self) -> int | None:
        """Resolve per-chat timeout. None means unbounded."""
        if self.timeout <= 0:
            self._last_timeout_used_secs = None
            return None

        if (not self.timeout_dynamic) or self._latency_samples == 0:
            resolved = int(self.timeout)
            self._last_timeout_used_secs = resolved
            return resolved

        predicted = int(
            (self._latency_ewma_ms / 1000.0) * self.timeout_multiplier
            + self.timeout_grace_secs
        )
        resolved = max(self.timeout_floor_secs, min(self.timeout_ceiling_secs, predicted))
        self._last_timeout_used_secs = resolved
        return resolved

    def record_chat_latency(self, latency_ms: float, had_error: bool) -> None:
        """Update timeout model using successful turns only."""
        if had_error:
            return
        if self._latency_samples == 0:
            self._latency_ewma_ms = latency_ms
        else:
            alpha = 0.3
            self._latency_ewma_ms = (
                alpha * latency_ms + (1.0 - alpha) * self._latency_ewma_ms
            )
        self._latency_samples += 1

    def timeout_state(self) -> dict:
        return {
            "dynamic_enabled": self.timeout_dynamic,
            "base_timeout_secs": self.timeout,
            "last_timeout_used_secs": self._last_timeout_used_secs,
            "timeout_floor_secs": self.timeout_floor_secs,
            "timeout_ceiling_secs": self.timeout_ceiling_secs,
            "timeout_multiplier": self.timeout_multiplier,
            "timeout_grace_secs": self.timeout_grace_secs,
            "latency_ewma_ms": round(self._latency_ewma_ms, 1),
            "latency_samples": self._latency_samples,
        }

    def session_key(self, label: str | None = None, lane: str | None = None) -> str:
        """Build a tenant-safe explicit session key for runtimes that require one."""
        resolved_lane = (lane or self.session_lane).strip() or "thread"
        resolved_label = self._sanitize_session_part(label or self.session_namespace)

        if resolved_lane == "main":
            return f"agent:zaki-bot:user:{self.user_id}:main"
        return f"agent:zaki-bot:user:{self.user_id}:{resolved_lane}:{resolved_label}"

    def _sanitize_session_part(self, text: str) -> str:
        cleaned = "".join(
            ch if ch.isalnum() or ch in ("-", "_", ":") else "-" for ch in text
        ).strip("-")
        return cleaned or "bench"

    def clone_for_user(self, user_id: str) -> "BenchConfig":
        """Create a per-user clone preserving harness behavior settings."""
        return BenchConfig(
            base_url=self.base_url,
            token=self.token,
            user_id=user_id,
            timeout=self.timeout,
            timeout_dynamic=self.timeout_dynamic,
            timeout_floor_secs=self.timeout_floor_secs,
            timeout_ceiling_secs=self.timeout_ceiling_secs,
            timeout_multiplier=self.timeout_multiplier,
            timeout_grace_secs=self.timeout_grace_secs,
            chat_endpoint=self.chat_endpoint,
            health_endpoint=self.health_endpoint,
            ready_endpoint=self.ready_endpoint,
            diagnostics_endpoint=self.diagnostics_endpoint,
            metrics_endpoint=self.metrics_endpoint,
            memory_sample_size=self.memory_sample_size,
            scale_concurrency=self.scale_concurrency,
            latency_requests=self.latency_requests,
            schedule_wait_secs=self.schedule_wait_secs,
            session_namespace=self.session_namespace,
            session_lane=self.session_lane,
        )

    def clone_for_dimension(self, dimension_key: str) -> "BenchConfig":
        """Create a per-dimension clone with an isolated session namespace."""
        cloned = self.clone_for_user(self.user_id)
        cloned.session_namespace = f"dtaas-bench-{dimension_key}"
        return cloned
