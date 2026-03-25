# DTaaS-Bench Results: Nullalis local live

**Date**: 2026-03-24
**Benchmark Version**: DTaaS-Bench v0.2
**Runtime URL**: http://127.0.0.1:3000

---

## Verified Composite Score: 68.1/100 — Competitive

- Verified raw: **81.6/100**
- Measured coverage: **84%**
- Projected composite: **77.9/100**

### Dimension Breakdown

| Dimension | Weight | Verified | Projected | Coverage | V Weighted | P Weighted |
|-----------|--------|----------|-----------|----------|------------|------------|
| Autonomy Control | 0.15 | 100 | 100 | 100% | 15.00 | 15.00 |
| Memory Persistence | 0.15 | 93 | 90 | 70% | 9.75 | 13.50 |
| Functional Capability | 0.15 | 100 | 100 | 100% | 15.00 | 15.00 |
| Autonomous Execution | 0.12 | 100 | 100 | 100% | 12.00 | 12.00 |
| Cross-Channel Consistency | 0.12 | 93 | 85 | 70% | 7.80 | 10.20 |
| Integration Breadth | 0.08 | 62 | 62 | 100% | 4.92 | 4.92 |
| Security & Privacy | 0.08 | 75 | 81 | 60% | 3.60 | 6.48 |
| Scale & Cost Efficiency | 0.05 | 0 | 0 | 20% | 0.00 | 0.00 |
| Operational Resilience | 0.05 | 0 | 15 | 75% | 0.00 | 0.75 |
| Latency Profile | 0.05 | 0 | 0 | 100% | 0.00 | 0.00 |
| **Verified Composite** | **1.00** | **81.6** |  | **84%** | **68.1** |  |
| **Projected Composite** | **1.00** |  | **77.9** |  |  | **77.9** |

---

## Dimension Details

### Autonomy Control

- **runtime_info_tool_used**: True
- **runtime_info_accessible**: True
- **runtime_mode_in_diagnostics**: True
- **bus_metrics_in_diagnostics**: True
- **heartbeat_runtime_available**: True
- **startup_self_check_present**: True
- **background_sources_seen**: ['cron', 'heartbeat']
- **proactive_policy_visible**: True
- **ops_counters_visible**: True
- **explicit_session_key_policy_visible**: True
- **pool_metrics_present**: True
- **transport_metrics_present**: True
- **session_key_rejection_metrics_present**: True
- **verified_score**: 100
- **projected_score**: 100
- **measured_coverage**: 1.0

### Memory Persistence

- **facts_stored**: 20
- **facts_attempted**: 20
- **exact_recall_hits**: 18
- **exact_recall_rate**: 0.9
- **semantic_recall_hits**: 20
- **semantic_recall_rate**: 1.0
- **cross_session_recall_rate**: 0.8
- **verified_score**: 92.9
- **projected_score**: 90.0
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
- **waiting_for_execution_secs**: 180
- **scheduler_total_before**: 13
- **scheduler_total_after**: 13
- **scheduler_total_increased**: False
- **task_confirmed_by_chat**: True
- **task_executed**: True
- **verified_score**: 100
- **projected_score**: 100
- **measured_coverage**: 1.0

### Cross-Channel Consistency

- **same_session_recall**: True
- **bus_architecture**: True
- **channels_in_diagnostics**: True
- **session_in_diagnostics**: True
- **live_configured_channels**: 1
- **live_connected_channels**: 1
- **identity_mapping_seen**: True
- **projected_timeline_consistency**: True
- **projected_notification_routing**: True
- **note**: Full cross-channel test requires 2+ real channels. Projected components: timeline consistency, notification routing.
- **verified_score**: 92.9
- **projected_score**: 85
- **measured_coverage**: 0.7

### Integration Breadth

- **health_endpoint_ok**: True
- **diagnostics_available**: True
- **runtime_info_tool_used**: True
- **runtime_info_payload**: {'enabled_tools_count': 28, 'channels_count': 2, 'memory_backends_count': 6, 'integrations_count': 2, 'state_backend': 'postgres', 'provider': 'together', 'model': 'moonshotai/Kimi-K2.5'}
- **channels**: 2
- **tools**: 28
- **memory_backends**: 6
- **integrations**: 2
- **metrics_available**: True
- **verified_score**: 61.5
- **projected_score**: 61.5
- **measured_coverage**: 1.0
- **component_coverage**: {'channels': 0.3, 'tools': 0.3, 'backends': 0.2, 'integrations': 0.2}

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

- **baseline_p50_ms**: 3459.5
- **same_session**: {'requests': 20, 'errors': 7, 'success': 13, 'wall_time_ms': 39740.1, 'p50_ms': 57.9, 'p95_ms': 26066.0, 'p99_ms': 26066.0}
- **multi_user**: {'requests': 20, 'errors': 20, 'success': 0, 'wall_time_ms': 9.3, 'p50_ms': None, 'p95_ms': None, 'p99_ms': None}
- **verified_score**: 0.0
- **projected_score**: 0.0
- **measured_coverage**: 0.2

### Operational Resilience

- **health_endpoint_ok**: False
- **diagnostics_available**: False
- **state_persists_across_turns**: False
- **idempotency_awareness**: False
- **graceful_shutdown_awareness**: False
- **projected_job_recovery**: True
- **projected_cold_start**: True
- **note**: SIGKILL crash recovery and cold start timing require OS-level access, not testable via HTTP. Projected based on architecture.
- **verified_score**: 0.0
- **projected_score**: 15
- **measured_coverage**: 0.75

### Latency Profile

- **health_latency_ms**: 0.5
- **chat_requests**: 10
- **chat_success**: 0
- **error**: All chat requests failed
- **schedule_jitter_ms**: projected: ~1000 (1s poll interval)
- **memory_roundtrip_ms**: projected: <10 (SQLite FTS5 in-process)
- **note**: Chat latency is dominated by LLM inference time. Runtime overhead is minimal.
- **verified_score**: 0
- **projected_score**: 0
- **measured_coverage**: 1.0

---

*Generated by DTaaS-Bench v0.2 — 2026-03-24*