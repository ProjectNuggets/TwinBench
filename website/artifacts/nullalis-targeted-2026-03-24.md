# DTaaS-Bench Results: Nullalis local live

**Date**: 2026-03-24
**Benchmark Version**: DTaaS-Bench v0.2
**Runtime URL**: http://127.0.0.1:3000

---

## Verified Composite Score: 0.0/100 — Early Stage

- Verified raw: **0.0/100**
- Measured coverage: **26%**
- Projected composite: **6.9/100**

### Dimension Breakdown

| Dimension | Weight | Verified | Projected | Coverage | V Weighted | P Weighted |
|-----------|--------|----------|-----------|----------|------------|------------|
| Autonomy Control | 0.15 | 0 | 0 | 100% | 0.00 | 0.00 |
| Memory Persistence | 0.15 | 0 | 25 | 70% | 0.00 | 3.75 |
| Functional Capability | 0.15 | 0 | 0 | 100% | 0.00 | 0.00 |
| Autonomous Execution | 0.12 | 0 | 0 | 100% | 0.00 | 0.00 |
| Cross-Channel Consistency | 0.12 | 0 | 20 | 50% | 0.00 | 2.40 |
| Integration Breadth | 0.08 | 0 | 0 | 100% | 0.00 | 0.00 |
| Security & Privacy | 0.08 | 0 | 0 | 100% | 0.00 | 0.00 |
| Scale & Cost Efficiency | 0.05 | 0 | 0 | 20% | 0.00 | 0.00 |
| Operational Resilience | 0.05 | 0 | 15 | 75% | 0.00 | 0.75 |
| Latency Profile | 0.05 | 0 | 0 | 100% | 0.00 | 0.00 |
| **Verified Composite** | **1.00** | **0.0** |  | **26%** | **0.0** |  |
| **Projected Composite** | **1.00** |  | **6.9** |  |  | **6.9** |

---

## Dimension Details

### Memory Persistence

- **facts_stored**: 0
- **facts_attempted**: 20
- **exact_recall_hits**: 0
- **exact_recall_rate**: 0.0
- **semantic_recall_hits**: 0
- **semantic_recall_rate**: 0.0
- **cross_session_recall_rate**: 0.0
- **verified_score**: 0.0
- **projected_score**: 25.0
- **measured_coverage**: 0.7
- **measured_component**: 0.0
- **projected_component**: 0.25
- **note**: Temporal stability (0.20 weight) projected at 0.80; conflict resolution (0.10 weight) projected at 0.90. Full verification requires restart + 30-day test.

### Cross-Channel Consistency

- **same_session_recall**: False
- **diagnostics_available**: False
- **projected_timeline_consistency**: True
- **projected_notification_routing**: True
- **note**: Full cross-channel test requires 2+ real channels. Projected components: timeline consistency, notification routing.
- **verified_score**: 0.0
- **projected_score**: 20
- **measured_coverage**: 0.5
- **measured_points**: 0
- **measured_max_points**: 50

### Scale & Cost Efficiency

- **baseline_p50_ms**: None
- **baseline_error**: All baseline requests failed
- **baseline_error_samples**: ['HTTPConnectionPool(host=\'127.0.0.1\', port=3000): Max retries exceeded with url: /api/v1/chat/stream (Caused by NewConnectionError("HTTPConnection(host=\'127.0.0.1\', port=3000): Failed to establish a new connection: [Errno 61] Connection refused"))']
- **same_session**: {'requests': 20, 'errors': 20, 'success': 0, 'wall_time_ms': 16.5, 'p50_ms': None, 'p95_ms': None, 'p99_ms': None, 'error_samples': ['HTTPConnectionPool(host=\'127.0.0.1\', port=3000): Max retries exceeded with url: /api/v1/chat/stream (Caused by NewConnectionError("HTTPConnection(host=\'127.0.0.1\', port=3000): Failed to establish a new connection: [Errno 61] Connection refused"))']}
- **multi_user**: {'requests': 20, 'errors': 20, 'success': 0, 'wall_time_ms': 11.1, 'p50_ms': None, 'p95_ms': None, 'p99_ms': None, 'error_samples': ['HTTPConnectionPool(host=\'127.0.0.1\', port=3000): Max retries exceeded with url: /api/v1/chat/stream (Caused by NewConnectionError("HTTPConnection(host=\'127.0.0.1\', port=3000): Failed to establish a new connection: [Errno 61] Connection refused"))']}
- **verified_score**: 0.0
- **projected_score**: 0.0
- **measured_coverage**: 0.2

### Operational Resilience

- **health_endpoint_ok**: False
- **diagnostics_available**: False
- **state_store_error**: HTTPConnectionPool(host='127.0.0.1', port=3000): Max retries exceeded with url: /api/v1/chat/stream (Caused by NewConnectionError("HTTPConnection(host='127.0.0.1', port=3000): Failed to establish a new connection: [Errno 61] Connection refused"))
- **state_recall_error**: HTTPConnectionPool(host='127.0.0.1', port=3000): Max retries exceeded with url: /api/v1/chat/stream (Caused by NewConnectionError("HTTPConnection(host='127.0.0.1', port=3000): Failed to establish a new connection: [Errno 61] Connection refused"))
- **state_persists_across_turns**: False
- **idempotency_probe_error**: HTTPConnectionPool(host='127.0.0.1', port=3000): Max retries exceeded with url: /api/v1/chat/stream (Caused by NewConnectionError("HTTPConnection(host='127.0.0.1', port=3000): Failed to establish a new connection: [Errno 61] Connection refused"))
- **idempotency_awareness**: False
- **graceful_shutdown_probe_error**: HTTPConnectionPool(host='127.0.0.1', port=3000): Max retries exceeded with url: /api/v1/chat/stream (Caused by NewConnectionError("HTTPConnection(host='127.0.0.1', port=3000): Failed to establish a new connection: [Errno 61] Connection refused"))
- **graceful_shutdown_awareness**: False
- **projected_job_recovery**: True
- **projected_cold_start**: True
- **runtime_unavailable_during_probe**: True
- **chat_probe_error_samples**: ['HTTPConnectionPool(host=\'127.0.0.1\', port=3000): Max retries exceeded with url: /api/v1/chat/stream (Caused by NewConnectionError("HTTPConnection(host=\'127.0.0.1\', port=3000): Failed to establish a new connection: [Errno 61] Connection refused"))']
- **note**: SIGKILL crash recovery and cold start timing require OS-level access, not testable via HTTP. Projected based on architecture. Runtime was unavailable during this probe, so resilience zeros may reflect outage rather than missing capabilities.
- **verified_score**: 0.0
- **projected_score**: 15
- **measured_coverage**: 0.75

### Latency Profile

- **health_endpoint_ok**: False
- **health_latency_ms**: 1.0
- **chat_requests**: 10
- **chat_success**: 0
- **error**: All chat requests failed
- **chat_error_samples**: ['HTTPConnectionPool(host=\'127.0.0.1\', port=3000): Max retries exceeded with url: /api/v1/chat/stream (Caused by NewConnectionError("HTTPConnection(host=\'127.0.0.1\', port=3000): Failed to establish a new connection: [Errno 61] Connection refused"))']
- **runtime_unavailable_during_probe**: True
- **schedule_jitter_ms**: projected: ~1000 (1s poll interval)
- **memory_roundtrip_ms**: projected: <10 (SQLite FTS5 in-process)
- **note**: Chat latency is dominated by LLM inference time. Runtime overhead is minimal. Runtime was unavailable during this probe, so chat latency could not be measured.
- **verified_score**: 0
- **projected_score**: 0
- **measured_coverage**: 1.0

---

*Generated by DTaaS-Bench v0.2 — 2026-03-24*