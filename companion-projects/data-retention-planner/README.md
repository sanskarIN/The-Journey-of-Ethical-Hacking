# Data Retention Planner

Review a local CSV retention register and calculate which datasets are due for review as of an explicit date.

## Input format

```text
dataset,classification,last_review,review_interval_days
synthetic-auth-logs,training,2026-07-01,30
```

Dates use `YYYY-MM-DD` and review intervals must be positive integers.

## Usage

```bash
python companion-projects/data-retention-planner/data_retention_planner.py register.csv --as-of 2026-08-19
```

## Learning objective

Practice defensive data-governance review without connecting to storage systems or deleting any data.

## Scope

This utility is advisory only. It reads an explicit local register and reports calculated due dates; it never deletes, moves, uploads, or changes files.
