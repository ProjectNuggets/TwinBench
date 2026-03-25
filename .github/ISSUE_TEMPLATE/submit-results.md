---
name: Submit Benchmark Results
about: Submit DTaaS-Bench results for your runtime
title: "[Results] <Runtime Name> v<Version>"
labels: results
---

## Runtime Information

- **Name**: 
- **Version**: 
- **URL/Repo**: 
- **LLM Provider Used**: 
- **Runtime Commit SHA**: 
- **Harness Commit SHA**: 

## Benchmark Run

- **DTaaS-Bench Version**: 0.2
- **Date**: 
- **Platform**: 
- **Harness Command Used**:

```bash
python -m harness.runner --url <URL> --token <TOKEN> --user-id <ID> --name "<Name>" --output results/<runtime>.json --markdown results/<runtime>.md --html results/<runtime>.html
```

## Results

**Verified Composite Score**: /100
**Projected Composite Score**: /100
**Measured Coverage**: 
**Coverage-Adjusted Verified Score**: /100
**Rating**: 

### Dimension Scores

| Dimension | Verified | Projected | Coverage |
|-----------|----------|-----------|----------|
| Autonomy Control | | | |
| Memory Persistence | | | |
| Functional Capability | | | |
| Autonomous Execution | | | |
| Cross-Channel Consistency | | | |
| Integration Breadth | | | |
| Security & Privacy | | | |
| Scale & Cost Efficiency | | | |
| Operational Resilience | | | |
| Latency Profile | | | |

## Evidence Pack

- **Diagnostics attached**: yes/no
- **Metrics attached**: yes/no
- **Run manifest attached**: yes/no
- **Any runtime/provider incident during run**:
- **Incident attribution**: runtime / upstream dependency / network / unknown
- **Notes on projected components**:

## Attachments

Please attach:
- [ ] `results/<runtime>.json` output from the harness
- [ ] `results/<runtime>.md` or `results/<runtime>.html`
- [ ] Any notes on configuration or setup
- [ ] `/internal/diagnostics` snapshot if available
- [ ] `/metrics` snapshot if available
- [ ] Any incident notes or representative error messages if the run degraded
- [ ] Optional run manifest based on `docs/run-manifest-v0.2.example.json`
