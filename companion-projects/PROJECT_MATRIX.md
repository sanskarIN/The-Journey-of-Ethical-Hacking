# Companion Project Matrix

All projects in this matrix are designed for local files, synthetic data, owned systems, or explicitly authorized data exports.

| Project | Primary defensive skill | Input | Network access | Tests |
|---|---|---|---|---|
| Log Sifter | Log summarization | CSV | No | Yes |
| Integrity Manifest | File integrity | Directory + JSON manifest | No | Yes |
| IOC Normalizer | Indicator data hygiene | Text | No | Yes |
| Incident Timeline | Incident documentation | JSONL | No | Yes |
| Header Safety Report | Email metadata review | Saved headers | No | Yes |
| Secrets Redactor | Data minimization | Text | No | Yes |
| Evidence Inventory | Evidence documentation | Directory | No | Yes |
| Access Review Helper | IAM governance | CSV + JSON policy | No | Yes |
| Configuration Baseline Diff | Drift review | JSON + JSON | No | Yes |
| Asset Inventory Summary | Asset governance | CSV | No | Yes |
| Security Checklist Tracker | Review progress | Markdown | No | Yes |
| Backup Verify | Backup integrity | Two directories | No | Yes |
| JSONL Event Validator | Event data quality | JSONL | No | Yes |
| Data Retention Planner | Data governance | CSV | No | Yes |
| Change Review Notes | Change control | CSV | No | Yes |
| Permission Matrix Auditor | Least-privilege review | CSV + JSON policy | No | Yes |
| Control Evidence Mapper | Control/evidence governance | CSV + JSON policy | No | Yes |
| Exception Register Validator | Exception governance | CSV | No | Yes |
| Patch Register Summary | Patch governance | CSV | No | Yes |
| Recovery Exercise Reporter | Resilience exercises | CSV | No | Yes |

## Design characteristics

- Explicit input paths; no automatic device discovery.
- No live-target scanning.
- No authentication attempts.
- No exploit, persistence, evasion, or destructive behavior.
- No external reputation or enrichment services.
- Python standard library only.
- Synthetic fixtures in tests.

## Completion definition

A project is marked complete in this matrix only when its documentation, focused implementation, and deterministic unit test are present.
