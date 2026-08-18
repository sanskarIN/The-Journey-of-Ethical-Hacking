# Synthetic Dataset Data Dictionary

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This file is generated from `schemas/dataset_contracts.json` and documents the public fictional/synthetic dataset fields and validation constraints.

## `sample_asset_inventory.csv`

| Column | Constraint |
|---|---|
| `asset_id` | Primary identifier; values must be unique |
| `asset_class` | No additional contract constraint |
| `criticality` | Allowed: Low, Medium, High, Critical |
| `owner_group` | No additional contract constraint |
| `managed` | Allowed: Yes, Limited |
| `patch_age_days` | Integer range: 0–365 |
| `telemetry_status` | Allowed: Fresh, Partial, Stale, Missing |
| `support_status` | Allowed: Supported, Extended |

## `sample_cloud_posture.csv`

| Column | Constraint |
|---|---|
| `asset_id` | Primary identifier; values must be unique |
| `environment` | No additional contract constraint |
| `criticality` | Allowed: Low, Medium, High, Critical |
| `owner_group` | No additional contract constraint |
| `baseline_status` | Allowed: Aligned, Partial, Review-Due |
| `identity_review_age_days` | Integer range: 0–365 |
| `logging_status` | Allowed: Fresh, Stale, Limited |
| `backup_status` | Allowed: Current, Needs-Test |
| `open_exception` | Allowed: Yes, No |

## `sample_control_evidence.csv`

| Column | Constraint |
|---|---|
| `evidence_id` | Primary identifier; values must be unique |
| `control_area` | No additional contract constraint |
| `criticality` | Allowed: Low, Medium, High, Critical |
| `evidence_age_days` | Integer range: 0–365 |
| `exception_open` | Allowed: Yes, No |
| `recovery_tested` | Allowed: Yes, No |
| `owner` | No additional contract constraint |

## `sample_endpoint_fleet.csv`

| Column | Constraint |
|---|---|
| `device_id` | Primary identifier; values must be unique |
| `device_class` | No additional contract constraint |
| `criticality` | Allowed: Low, Medium, High, Critical |
| `enrollment_status` | Allowed: Managed, Limited |
| `patch_age_days` | Integer range: 0–365 |
| `telemetry_status` | Allowed: Fresh, Partial, Stale, Missing |
| `support_status` | Allowed: Supported, Extended |
| `data_classification` | Allowed: Public, Internal, Confidential, Restricted |

## `sample_governance_controls.csv`

| Column | Constraint |
|---|---|
| `control_id` | Primary identifier; values must be unique |
| `control_domain` | No additional contract constraint |
| `owner_role` | No additional contract constraint |
| `criticality` | Allowed: Low, Medium, High, Critical |
| `evidence_age_days` | Integer range: 0–365 |
| `exception_status` | Allowed: None, Open |
| `review_status` | Allowed: Current, Review-Due |
| `board_visibility` | Allowed: Low, Medium, High |

## `sample_privacy_controls.csv`

| Column | Constraint |
|---|---|
| `record_id` | Primary identifier; values must be unique |
| `data_domain` | No additional contract constraint |
| `data_classification` | Allowed: Public, Internal, Confidential, Restricted |
| `retention_status` | Allowed: Current, Review-Due |
| `minimization_review` | Allowed: Complete, Partial |
| `access_review_age_days` | Integer range: 0–365 |
| `transfer_basis_status` | Allowed: Documented, Review-Due, Not-Applicable |
| `deletion_test_status` | Allowed: Passed, Needs-Retest |

## `sample_resilience_exercises.csv`

| Column | Constraint |
|---|---|
| `exercise_id` | Primary identifier; values must be unique |
| `service` | No additional contract constraint |
| `criticality` | Allowed: Low, Medium, High, Critical |
| `recovery_objective_hours` | Integer range: 0–168 |
| `last_test_age_days` | Integer range: 0–730 |
| `dependency_status` | Allowed: Documented, Partial |
| `communications_status` | Allowed: Ready, Review-Due |
| `decision_log_status` | Allowed: Complete, Partial |

## `sample_risk_signals.csv`

| Column | Constraint |
|---|---|
| `signal_id` | Primary identifier; values must be unique |
| `domain` | No additional contract constraint |
| `criticality` | Allowed: Low, Medium, High, Critical |
| `age_days` | Integer range: 0–365 |
| `open_exception` | Allowed: Yes, No |
| `telemetry_gap` | Allowed: Yes, No |
| `recovery_gap` | Allowed: Yes, No |

## `sample_saas_governance.csv`

| Column | Constraint |
|---|---|
| `tenant_id` | Primary identifier; values must be unique |
| `service_class` | No additional contract constraint |
| `criticality` | Allowed: Low, Medium, High, Critical |
| `identity_integration` | Allowed: Federated, Standalone |
| `admin_review_age_days` | Integer range: 0–365 |
| `logging_status` | Allowed: Fresh, Partial, Stale, Limited |
| `external_sharing_status` | Allowed: Restricted, Review-Due, Open |
| `backup_export_status` | Allowed: Current, Needs-Test, Not-Required |

## `sample_workforce_capability.csv`

| Column | Constraint |
|---|---|
| `role_id` | Primary identifier; values must be unique |
| `role_family` | No additional contract constraint |
| `criticality` | Allowed: Low, Medium, High, Critical |
| `staffing_status` | Allowed: Adequate, Thin |
| `training_age_days` | Integer range: 0–365 |
| `exercise_status` | Allowed: Current, Review-Due |
| `backup_coverage` | Allowed: Full, Partial, Limited |
| `development_plan_status` | Allowed: Current, Review-Due |

## Safety and privacy boundary

These datasets are fictional and intended for offline defensive learning. Do not replace them with credentials, secrets, personal data, real target details, or sensitive production evidence in public contributions.

**Publication storefront:** https://ramsandesh.gumroad.com
