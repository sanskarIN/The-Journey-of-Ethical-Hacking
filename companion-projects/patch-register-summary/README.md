# Patch Register Summary

Summarize an explicitly exported local patch-status CSV without scanning hosts or contacting update services.

## Input format

```text
asset,patch_id,status,age_days
lab-host-1,KB-TRAINING-001,installed,5
lab-host-2,KB-TRAINING-002,pending,12
```

Supported status values are `installed`, `pending`, `failed`, and `not-applicable`. `age_days` must be a non-negative integer.

## Usage

```bash
python companion-projects/patch-register-summary/patch_register_summary.py patches.csv
```

## Learning objective

Practice defensive patch-governance reporting, backlog measurement, and local data validation.

## Scope

This utility does not discover systems, query operating systems, download patches, or install updates. It only summarizes the explicit local export supplied to it.
