# Synthetic Datasets

All datasets in this directory are fictional and designed for **offline defensive learning**. They must not be treated as real operational records.

## Core samples

- `sample_asset_inventory.csv` — fictional device/asset posture records.
- `sample_control_evidence.csv` — fictional control-evidence freshness and exception records.
- `sample_risk_signals.csv` — fictional risk signals for local prioritization exercises.

## Domain exercise samples

- `sample_cloud_posture.csv` — fictional cloud posture, identity-review, logging, backup, and exception records.
- `sample_privacy_controls.csv` — fictional privacy, retention, minimization, access-review, transfer, and deletion-test records.
- `sample_endpoint_fleet.csv` — fictional endpoint enrollment, patch-age, telemetry, support, and data-classification records.
- `sample_saas_governance.csv` — fictional SaaS tenant identity, admin review, logging, sharing, and backup/export records.
- `sample_resilience_exercises.csv` — fictional recovery objectives, test age, dependencies, communications, and decision-log records.
- `sample_governance_controls.csv` — fictional control ownership, evidence age, exception, review, and board-visibility records.
- `sample_workforce_capability.csv` — fictional staffing, training, exercise, backup-coverage, and development-plan records.

## Safe-use rules

- Keep exercises offline unless you are working inside an explicitly authorized environment.
- Do not replace fictional values with passwords, tokens, API keys, personal data, customer data, or third-party target information.
- Do not use the datasets to drive automated actions against real systems.
- When sharing completed exercises publicly, keep all identifiers fictional and non-sensitive.

The datasets are intentionally small and readable so learners can inspect them manually as well as with local scripts.
