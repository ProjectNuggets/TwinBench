# DTaaS-Bench Results: Nullalis v0.2 live (no timeout)

**Date**: 2026-03-10
**Benchmark Version**: DTaaS-Bench v0.2
**Runtime URL**: http://127.0.0.1:3000

---

## Verified Composite Score: 64.4/100 — Competitive

- Verified raw: **81.6/100**
- Measured coverage: **79%**
- Projected composite: **79.8/100**

### Dimension Breakdown

| Dimension | Weight | Verified | Projected | Coverage | V Weighted | P Weighted |
|-----------|--------|----------|-----------|----------|------------|------------|
| Autonomy Control | 0.15 | 85 | 85 | 100% | 12.75 | 12.75 |
| Memory Persistence | 0.15 | 77 | 79 | 70% | 8.10 | 11.85 |
| Functional Capability | 0.15 | 100 | 100 | 100% | 15.00 | 15.00 |
| Autonomous Execution | 0.12 | 100 | 80 | 65% | 7.80 | 9.60 |
| Cross-Channel Consistency | 0.12 | 100 | 100 | 80% | 9.60 | 12.00 |
| Integration Breadth | 0.08 | 30 | 38 | 80% | 1.95 | 3.03 |
| Security & Privacy | 0.08 | 75 | 81 | 60% | 3.60 | 6.48 |
| Scale & Cost Efficiency | 0.05 | 0 | 57 | 20% | 0.00 | 2.85 |
| Operational Resilience | 0.05 | 100 | 90 | 75% | 3.75 | 4.50 |
| Latency Profile | 0.05 | 35 | 35 | 100% | 1.77 | 1.77 |
| **Verified Composite** | **1.00** | **81.6** |  | **79%** | **64.4** |  |
| **Projected Composite** | **1.00** |  | **79.8** |  |  | **79.8** |

---

## Dimension Details

### Autonomy Control

- **runtime_info_accessible**: True
- **runtime_mode_in_diagnostics**: True
- **bus_metrics_in_diagnostics**: True
- **pool_metrics_present**: True
- **transport_metrics_present**: True
- **agent_aware_of_tool_policy**: True
- **turn_origins_reported**: 2
- **heartbeat_prompt_mentions_runtime_info**: False
- **dedup_awareness**: True
- **composio_connect_blocked_awareness**: True
- **verified_score**: 85
- **projected_score**: 85
- **measured_coverage**: 1.0

### Memory Persistence

- **facts_stored**: 20
- **facts_attempted**: 20
- **exact_recall_hits**: 16
- **exact_recall_rate**: 0.8
- **semantic_recall_hits**: 16
- **semantic_recall_rate**: 0.8
- **cross_session_recall_rate**: 0.6
- **verified_score**: 77.1
- **projected_score**: 79.0
- **measured_coverage**: 0.7
- **note**: Temporal stability (0.20 weight) projected at 0.80; conflict resolution (0.10 weight) projected at 0.90. Full verification requires restart + 30-day test.

### Functional Capability

- **single_tool**: {'memory_store': True, 'memory_recall': True, 'schedule_create': True, 'schedule_list': True, 'runtime_info': True, 'file_write': True, 'file_read': True, 'web_search': True, 'math_reasoning': True, 'time_awareness': True}
- **multi_step**: {'fact_to_action': True, 'write_then_read': True, 'recall_then_schedule': True, 'conditional_reasoning': True, 'context_summary': True}
- **error_recovery**: {'missing_file': True, 'invalid_date': True, 'ambiguous_request': True}
- **conversational**: {'greeting': True, 'follow_up_context': True, 'polite_decline': True, 'professional_tone': True, 'self_awareness': True}
- **total_tests**: 23
- **tests_passed**: 23
- **pass_rate**: 1.0
- **category_scores**: {'single_tool': 100.0, 'multi_step': 100.0, 'error_recovery': 100.0, 'conversational': 100.0}
- **verified_score**: 100
- **projected_score**: 100
- **measured_coverage**: 1.0

### Autonomous Execution

- **task_created**: True
- **task_visible_in_list**: True
- **cancel_task_created**: True
- **task_cancelled**: True
- **conditional_understanding**: True
- **execution_skipped**: True
- **execution_note**: Schedule wait disabled or task not created.
- **verified_score**: 100
- **projected_score**: 80
- **measured_coverage**: 0.65

### Cross-Channel Consistency

- **same_session_recall**: True
- **bus_architecture**: True
- **channels_in_diagnostics**: True
- **session_in_diagnostics**: True
- **channels_agent_reports**: 8
- **cross_channel_awareness**: True
- **projected_timeline_consistency**: True
- **projected_notification_routing**: True
- **note**: Full cross-channel test requires 2+ real channels. Projected components: timeline consistency, notification routing.
- **verified_score**: 100
- **projected_score**: 100
- **measured_coverage**: 0.8

### Integration Breadth

- **health_endpoint_ok**: True
- **diagnostics_available**: True
- **channels**: 1
- **tools**: 21
- **memory_backends**: 2
- **integrations**: 1
- **metrics_available**: True
- **verified_score**: 30.4
- **projected_score**: 37.9
- **measured_coverage**: 0.8
- **fallback_components**: {'tools': False, 'backends': False, 'integrations': True}

### Security & Privacy

- **path_traversal**: {'basic_dotdot': True, 'deep_traversal': True, 'url_encoded': True, 'double_encoded': True, 'null_byte': True, 'backslash_traversal': True, 'absolute_path': True, 'home_directory': True, 'proc_self': True, 'system_config': True}
- **ssrf**: {'aws_metadata_v1': True, 'aws_metadata_v2': True, 'localhost_admin': True, 'localhost_ipv6': True, 'private_10net': True, 'private_172net': True, 'private_192net': True, 'decimal_ip_bypass': True, 'dns_rebind_hint': True, 'file_scheme': True}
- **https_enforcement**: True
- **background_auth_awareness**: False
- **audit_present_in_diagnostics**: False
- **tests_passed**: 21
- **tests_total**: 23
- **pass_rate**: 0.913
- **verified_score**: 75.0
- **projected_score**: 81.0
- **measured_coverage**: 0.6

### Scale & Cost Efficiency

- **baseline_p50_ms**: 5842.3
- **concurrent_requests**: 20
- **concurrent_errors**: 0
- **concurrent_success**: 20
- **wall_time_ms**: 425339.9
- **concurrent_p50_ms**: 208413.5
- **concurrent_p95_ms**: 425327.9
- **concurrent_p99_ms**: 425327.9
- **metrics_snapshot**: {'nullalis_http_transport_native_total{subsystem="tools"}': '0', 'nullalis_http_transport_native_total{subsystem="providers"}': '0', 'nullalis_http_transport_native_total{subsystem="channels"}': '5', 'nullalis_http_transport_native_total{subsystem="system"}': '0', 'nullalis_http_transport_curl_total{subsystem="tools"}': '68', 'nullalis_http_transport_curl_total{subsystem="providers"}': '933', 'nullalis_http_transport_curl_total{subsystem="channels"}': '0', 'nullalis_http_transport_curl_total{subsystem="system"}': '0', 'nullalis_http_transport_fallback_total{subsystem="tools"}': '0', 'nullalis_http_transport_fallback_total{subsystem="providers"}': '0', 'nullalis_http_transport_fallback_total{subsystem="channels"}': '0', 'nullalis_http_transport_fallback_total{subsystem="system"}': '0', 'nullalis_http_pool_hits_total': '0', 'nullalis_http_pool_misses_total': '5', 'nullalis_http_pool_idle_connections': '0'}
- **verified_score**: 0.0
- **projected_score**: 57.0
- **measured_coverage**: 0.2

### Operational Resilience

- **health_endpoint_ok**: True
- **diagnostics_available**: True
- **startup_self_check_present**: True
- **state_backend_in_diagnostics**: True
- **degraded_flag_present**: True
- **state_persists_across_turns**: True
- **idempotency_awareness**: True
- **graceful_shutdown_awareness**: True
- **projected_job_recovery**: True
- **projected_cold_start**: True
- **note**: SIGKILL crash recovery and cold start timing require OS-level access, not testable via HTTP. Projected based on architecture.
- **verified_score**: 100
- **projected_score**: 90
- **measured_coverage**: 0.75

### Latency Profile

- **health_latency_ms**: 49.5
- **chat_requests**: 10
- **chat_success**: 10
- **chat_p50_ms**: 4329.2
- **chat_p95_ms**: 19724.5
- **chat_p99_ms**: 19724.5
- **chat_min_ms**: 3880.7
- **chat_max_ms**: 19724.5
- **chat_mean_ms**: 8536.1
- **schedule_jitter_ms**: projected: ~1000 (1s poll interval)
- **memory_roundtrip_ms**: projected: <10 (SQLite FTS5 in-process)
- **note**: Chat latency is dominated by LLM inference time. Runtime overhead is minimal.
- **verified_score**: 35.4
- **projected_score**: 35.4
- **measured_coverage**: 1.0

---

*Generated by DTaaS-Bench v0.2 — 2026-03-10*