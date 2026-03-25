# DTaaS-Bench Results: Nullalis local live

**Date**: 2026-03-25
**Benchmark Version**: DTaaS-Bench v0.2
**Runtime URL**: http://127.0.0.1:3000

---

## Verified Composite Score: 5.8/100 — Early Stage

- Verified raw: **8.4/100**
- Measured coverage: **69%**
- Projected composite: **17.4/100**

### Dimension Breakdown

| Dimension | Weight | Verified | Projected | Coverage | V Weighted | P Weighted |
|-----------|--------|----------|-----------|----------|------------|------------|
| Autonomy Control | 0.15 | 15 | 15 | 100% | 2.25 | 2.25 |
| Memory Persistence | 0.15 | 0 | 25 | 70% | 0.00 | 3.75 |
| Functional Capability | 0.15 | 0 | 0 | 100% | 0.00 | 0.00 |
| Autonomous Execution | 0.12 | 0 | 15 | 65% | 0.00 | 1.80 |
| Cross-Channel Consistency | 0.12 | 0 | 20 | 50% | 0.00 | 2.40 |
| Integration Breadth | 0.08 | 0 | 0 | 0% | 0.00 | 0.00 |
| Security & Privacy | 0.08 | 58 | 71 | 60% | 2.80 | 5.68 |
| Scale & Cost Efficiency | 0.05 | 0 | 0 | 20% | 0.00 | 0.00 |
| Operational Resilience | 0.05 | 20 | 30 | 75% | 0.75 | 1.50 |
| Latency Profile | 0.05 | 0 | 0 | 100% | 0.00 | 0.00 |
| **Verified Composite** | **1.00** | **8.4** |  | **69%** | **5.8** |  |
| **Projected Composite** | **1.00** |  | **17.4** |  |  | **17.4** |

---

## Dimension Details

### Autonomy Control

- **runtime_info_tool_used**: False
- **runtime_info_accessible**: False
- **diagnostics_available**: False
- **pool_metrics_present**: True
- **transport_metrics_present**: True
- **session_key_rejection_metrics_present**: True
- **verified_score**: 15
- **projected_score**: 15
- **measured_coverage**: 1.0

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
- **error_samples**: ['401 Client Error: Unauthorized for url: http://127.0.0.1:3000/api/v1/chat/stream']
- **note**: Temporal stability (0.20 weight) projected at 0.80; conflict resolution (0.10 weight) projected at 0.90. Full verification requires restart + 30-day test.

### Functional Capability

- **single_tool**: {'memory_store': False, 'memory_recall': False, 'schedule_create': False, 'schedule_list': False, 'runtime_info': False, 'file_write': False, 'file_read': False, 'web_search': False, 'math_reasoning': False, 'time_awareness': False}
- **multi_step**: {'fact_to_action': False, 'write_then_read': False, 'recall_then_schedule': False, 'conditional_reasoning': False, 'context_summary': False}
- **error_recovery**: {'missing_file': False, 'invalid_date': False, 'ambiguous_request': False}
- **conversational**: {'greeting': False, 'follow_up_context': False, 'polite_decline': False, 'professional_tone': False, 'self_awareness': False}
- **total_tests**: 23
- **tests_passed**: 0
- **pass_rate**: 0.0
- **category_scores**: {'single_tool': 0.0, 'multi_step': 0.0, 'error_recovery': 0.0, 'conversational': 0.0}
- **verified_score**: 0.0
- **projected_score**: 0.0
- **measured_coverage**: 1.0

### Autonomous Execution

- **task_created**: False
- **task_visible_in_list**: False
- **cancel_task_created**: False
- **conditional_understanding**: False
- **execution_skipped**: True
- **execution_note**: Schedule wait disabled or task not created.
- **verified_score**: 0.0
- **projected_score**: 15
- **measured_coverage**: 0.65

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
- **error_samples**: ['401 Client Error: Unauthorized for url: http://127.0.0.1:3000/api/v1/chat/stream']

### Integration Breadth

- **health_endpoint_ok**: True
- **diagnostics_available**: False
- **runtime_info_tool_used**: False
- **runtime_info_payload**: None
- **channels**: 0
- **tools**: 0
- **memory_backends**: 0
- **integrations**: 0
- **metrics_available**: True
- **verified_score**: 0.0
- **projected_score**: 0.0
- **measured_coverage**: 0.0
- **component_coverage**: {'channels': 0.0, 'tools': 0.0, 'backends': 0.0, 'integrations': 0.0}

### Security & Privacy

- **path_traversal**: {'basic_dotdot': True, 'deep_traversal': True, 'url_encoded': True, 'double_encoded': True, 'null_byte': True, 'backslash_traversal': True, 'absolute_path': True, 'home_directory': True, 'proc_self': True, 'system_config': True}
- **ssrf**: {'aws_metadata_v1': True, 'aws_metadata_v2': True, 'localhost_admin': True, 'localhost_ipv6': True, 'private_10net': True, 'private_172net': True, 'private_192net': True, 'decimal_ip_bypass': True, 'dns_rebind_hint': True, 'file_scheme': True}
- **https_enforcement**: False
- **background_auth_awareness**: False
- **tests_passed**: 20
- **tests_total**: 22
- **pass_rate**: 0.909
- **verified_score**: 58.3
- **projected_score**: 71.0
- **measured_coverage**: 0.6

### Scale & Cost Efficiency

- **baseline_p50_ms**: None
- **baseline_error**: All baseline requests failed
- **baseline_error_samples**: ['401 Client Error: Unauthorized for url: http://127.0.0.1:3000/api/v1/chat/stream']
- **same_session**: {'requests': 20, 'errors': 20, 'success': 0, 'wall_time_ms': 37.6, 'p50_ms': None, 'p95_ms': None, 'p99_ms': None, 'error_samples': ['401 Client Error: Unauthorized for url: http://127.0.0.1:3000/api/v1/chat/stream']}
- **multi_user**: {'requests': 20, 'errors': 20, 'success': 0, 'wall_time_ms': 50.6, 'p50_ms': None, 'p95_ms': None, 'p99_ms': None, 'error_samples': ['401 Client Error: Unauthorized for url: http://127.0.0.1:3000/api/v1/chat/stream']}
- **metrics_snapshot**: {'nullalis_http_transport_native_total{subsystem="tools"}': '0', 'nullalis_http_transport_native_total{subsystem="providers"}': '0', 'nullalis_http_transport_native_total{subsystem="channels"}': '0', 'nullalis_http_transport_native_total{subsystem="system"}': '0', 'nullalis_http_transport_curl_total{subsystem="tools"}': '0', 'nullalis_http_transport_curl_total{subsystem="providers"}': '16', 'nullalis_http_transport_curl_total{subsystem="channels"}': '0', 'nullalis_http_transport_curl_total{subsystem="system"}': '0', 'nullalis_http_transport_fallback_total{subsystem="tools"}': '0', 'nullalis_http_transport_fallback_total{subsystem="providers"}': '0', 'nullalis_http_transport_fallback_total{subsystem="channels"}': '0', 'nullalis_http_transport_fallback_total{subsystem="system"}': '0', 'nullalis_http_pool_hits_total': '0', 'nullalis_http_pool_misses_total': '0', 'nullalis_http_pool_idle_connections': '0'}
- **verified_score**: 0.0
- **projected_score**: 0.0
- **measured_coverage**: 0.2

### Operational Resilience

- **health_endpoint_ok**: True
- **diagnostics_available**: False
- **state_store_error**: 401 Client Error: Unauthorized for url: http://127.0.0.1:3000/api/v1/chat/stream
- **state_recall_error**: 401 Client Error: Unauthorized for url: http://127.0.0.1:3000/api/v1/chat/stream
- **state_persists_across_turns**: False
- **idempotency_probe_error**: 401 Client Error: Unauthorized for url: http://127.0.0.1:3000/api/v1/chat/stream
- **idempotency_awareness**: False
- **graceful_shutdown_probe_error**: 401 Client Error: Unauthorized for url: http://127.0.0.1:3000/api/v1/chat/stream
- **graceful_shutdown_awareness**: False
- **projected_job_recovery**: True
- **projected_cold_start**: True
- **runtime_unavailable_during_probe**: False
- **chat_probe_error_samples**: ['401 Client Error: Unauthorized for url: http://127.0.0.1:3000/api/v1/chat/stream']
- **note**: SIGKILL crash recovery and cold start timing require OS-level access, not testable via HTTP. Projected based on architecture.
- **verified_score**: 20.0
- **projected_score**: 30
- **measured_coverage**: 0.75

### Latency Profile

- **health_endpoint_ok**: True
- **health_latency_ms**: 54.4
- **chat_requests**: 10
- **chat_success**: 0
- **error**: All chat requests failed
- **chat_error_samples**: ['401 Client Error: Unauthorized for url: http://127.0.0.1:3000/api/v1/chat/stream']
- **runtime_unavailable_during_probe**: False
- **schedule_jitter_ms**: projected: ~1000 (1s poll interval)
- **memory_roundtrip_ms**: projected: <10 (SQLite FTS5 in-process)
- **note**: Chat latency is dominated by LLM inference time. Runtime overhead is minimal.
- **verified_score**: 0
- **projected_score**: 0
- **measured_coverage**: 1.0

---

*Generated by DTaaS-Bench v0.2 — 2026-03-25*