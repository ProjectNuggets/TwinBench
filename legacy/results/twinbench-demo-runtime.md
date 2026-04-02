# TwinBench Results: TwinBench Demo Runtime

**Date**: 2026-03-25
**Benchmark Version**: TwinBench v0.2
**Runtime URL**: http://127.0.0.1:8090
**Result Class**: Partial Reference Artifact

---

## Verified Composite Score: 54.4/100 — Emerging

- Verified raw: **79.0/100**
- Measured coverage: **69%**
- Projected composite: **70.6/100**
- Interpretation: **This artifact is strong enough to compare publicly. Use the verified score for evidence-backed comparison and the projected score only as a clearly labeled estimate.**

## Benchmark Principles

- unsupported is not failure
- missing bootstrap is not poor scale
- same-user contention is diagnostic
- evidence beats claims

### Dimension Breakdown

| Dimension | Status | Reason Code | Weight | Verified | Projected | Coverage | V Weighted | P Weighted |
|-----------|--------|-------------|--------|----------|-----------|----------|------------|------------|
| Autonomy Control | measured | None | 0.15 | 95 | 95 | 100% | 14.25 | 14.25 |
| Memory Persistence | partially_measured | None | 0.15 | 57 | 65 | 70% | 6.00 | 9.75 |
| Functional Capability | measured | None | 0.15 | 77 | 77 | 100% | 11.55 | 11.55 |
| Autonomous Execution | partially_measured | None | 0.12 | 77 | 65 | 65% | 6.00 | 7.80 |
| Cross-Channel Consistency | partially_measured | None | 0.12 | 70 | 70 | 50% | 4.20 | 8.40 |
| Integration Breadth | unavailable | None | 0.08 | 0 | 0 | 0% | 0.00 | 0.00 |
| Security & Privacy | partially_measured | None | 0.08 | 92 | 91 | 60% | 4.40 | 7.28 |
| Scale & Cost Efficiency | partially_measured | multi_user_scale_measured_with_provisioned_subset | 0.05 | 100 | 77 | 20% | 1.00 | 3.85 |
| Operational Resilience | partially_measured | None | 0.05 | 53 | 55 | 75% | 2.00 | 2.75 |
| Latency Profile | measured | None | 0.05 | 100 | 100 | 100% | 5.00 | 5.00 |
| **Verified Composite** | **1.00** | **79.0** |  | **69%** | **54.4** |  |
| **Projected Composite** | **1.00** |  | **70.6** |  |  | **70.6** |

---

## Dimension Details

### Autonomy Control

- **runtime_info_tool_used**: False
- **runtime_info_accessible**: False
- **runtime_mode_in_diagnostics**: True
- **bus_metrics_in_diagnostics**: True
- **heartbeat_runtime_available**: True
- **startup_self_check_present**: True
- **background_sources_seen**: ['scheduler']
- **proactive_policy_visible**: True
- **ops_counters_visible**: True
- **explicit_session_key_policy_visible**: True
- **pool_metrics_present**: True
- **transport_metrics_present**: True
- **session_key_rejection_metrics_present**: True
- **verified_score**: 95
- **projected_score**: 95
- **measured_coverage**: 1.0

### Memory Persistence

- **facts_stored**: 5
- **facts_attempted**: 5
- **exact_recall_hits**: 5
- **exact_recall_rate**: 1.0
- **semantic_recall_hits**: 0
- **semantic_recall_rate**: 0.0
- **cross_session_recall_rate**: 1.0
- **verified_score**: 57.1
- **projected_score**: 65.0
- **measured_coverage**: 0.7
- **measured_component**: 0.4
- **projected_component**: 0.65
- **note**: Temporal stability (0.20 weight) projected at 0.80; conflict resolution (0.10 weight) projected at 0.90. Full verification requires restart + 30-day test.

### Functional Capability

- **single_tool**: {'memory_store': True, 'memory_recall': False, 'schedule_create': True, 'schedule_list': True, 'runtime_info': True, 'file_write': True, 'file_read': True, 'web_search': True, 'math_reasoning': True, 'time_awareness': True}
- **multi_step**: {'fact_to_action': False, 'write_then_read': False, 'recall_then_schedule': True, 'conditional_reasoning': True, 'context_summary': False}
- **error_recovery**: {'missing_file': True, 'invalid_date': True, 'ambiguous_request': True}
- **conversational**: {'greeting': True, 'follow_up_context': True, 'polite_decline': True, 'professional_tone': False, 'self_awareness': True}
- **total_tests**: 23
- **tests_passed**: 18
- **pass_rate**: 0.783
- **category_scores**: {'single_tool': 90.0, 'multi_step': 40.0, 'error_recovery': 100.0, 'conversational': 80.0}
- **verified_score**: 77.0
- **projected_score**: 77.0
- **measured_coverage**: 1.0

### Autonomous Execution

- **task_created**: True
- **task_visible_in_list**: False
- **cancel_task_created**: True
- **task_cancelled**: True
- **conditional_understanding**: True
- **execution_skipped**: True
- **execution_note**: Schedule wait disabled or task not created.
- **verified_score**: 76.9
- **projected_score**: 65
- **measured_coverage**: 0.65

### Cross-Channel Consistency

- **same_session_recall**: False
- **bus_architecture**: True
- **channels_in_diagnostics**: True
- **session_in_diagnostics**: True
- **live_configured_channels**: 0
- **live_connected_channels**: 0
- **identity_mapping_seen**: True
- **projected_timeline_consistency**: True
- **projected_notification_routing**: True
- **note**: Full cross-channel test requires 2+ real channels. Projected components: timeline consistency, notification routing.
- **verified_score**: 70.0
- **projected_score**: 70.0
- **measured_coverage**: 0.5
- **measured_points**: 35
- **measured_max_points**: 50

### Integration Breadth

- **health_endpoint_ok**: True
- **diagnostics_available**: True
- **runtime_info_tool_used**: False
- **runtime_info_payload**: {'enabled_tools_count': 5, 'channels_count': 2, 'memory_backends_count': 1, 'integrations_count': 2, 'state_backend': 'in-memory demo store', 'provider': 'fixture-provider', 'model': 'fixture-assistant-1'}
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
- **https_enforcement**: True
- **background_auth_awareness**: True
- **audit_present_in_diagnostics**: False
- **tests_passed**: 22
- **tests_total**: 23
- **pass_rate**: 0.957
- **verified_score**: 91.7
- **projected_score**: 91.0
- **measured_coverage**: 0.6

### Scale & Cost Efficiency

- **baseline_p50_ms**: 13.9
- **same_session**: {'requests': 3, 'errors': 0, 'success': 3, 'wall_time_ms': 15.5, 'p50_ms': 14.7, 'p95_ms': 15.0, 'p99_ms': 15.0, 'error_samples': []}
- **multi_user_provisioning**: {'requested_users': 3, 'provisioned_users': 3, 'provisioned_user_ids': ['demo-user-bench-0', 'demo-user-bench-1', 'demo-user-bench-2'], 'unavailable_users': 0, 'unavailable_user_ids': [], 'error_samples': []}
- **multi_user**: {'requests': 3, 'errors': 0, 'success': 3, 'wall_time_ms': 14.2, 'p50_ms': 13.9, 'p95_ms': 13.9, 'p99_ms': 13.9, 'error_samples': []}
- **contention_ratio_same_session_over_multi_user**: 1.08
- **metrics_snapshot**: {'nullalis_http_transport_native_total{subsystem="tools"}': '5', 'nullalis_http_transport_native_total{subsystem="providers"}': '10', 'nullalis_http_pool_hits_total': '3', 'nullalis_http_pool_misses_total': '1'}
- **verified_score**: 100.0
- **projected_score**: 77.0
- **measured_coverage**: 0.2

### Operational Resilience

- **health_endpoint_ok**: True
- **diagnostics_available**: True
- **startup_self_check_present**: True
- **state_backend_in_diagnostics**: True
- **degraded_flag_present**: True
- **state_persists_across_turns**: False
- **idempotency_awareness**: False
- **graceful_shutdown_awareness**: False
- **projected_job_recovery**: True
- **projected_cold_start**: True
- **runtime_unavailable_during_probe**: False
- **note**: SIGKILL crash recovery and cold start timing require OS-level access, not testable via HTTP. Projected based on architecture.
- **verified_score**: 53.3
- **projected_score**: 55
- **measured_coverage**: 0.75

### Latency Profile

- **health_endpoint_ok**: True
- **health_latency_ms**: 1.1
- **chat_requests**: 10
- **chat_success**: 10
- **chat_p50_ms**: 13.0
- **chat_p95_ms**: 14.0
- **chat_p99_ms**: 14.0
- **chat_min_ms**: 11.5
- **chat_max_ms**: 14.0
- **chat_mean_ms**: 13.0
- **runtime_unavailable_during_probe**: False
- **schedule_jitter_ms**: projected: ~1000 (1s poll interval)
- **memory_roundtrip_ms**: projected: <10 (SQLite FTS5 in-process)
- **note**: Chat latency is dominated by LLM inference time. Runtime overhead is minimal.
- **verified_score**: 100
- **projected_score**: 100
- **measured_coverage**: 1.0

---

*Generated by TwinBench v0.2 — 2026-03-25*