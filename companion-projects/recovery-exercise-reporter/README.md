# Recovery Exercise Reporter

Summarize results from local tabletop recovery exercises into deterministic JSON metrics.

## Input format

```text
exercise_id,objective,result,duration_minutes,observations
REC-001,Restore training service,pass,35,Synthetic exercise completed
```

Supported result values are `pass`, `partial`, and `fail`. Duration must be a non-negative integer.

## Usage

```bash
python companion-projects/recovery-exercise-reporter/recovery_exercise_reporter.py exercises.csv
```

## Learning objective

Practice resilience-exercise measurement, result aggregation, and documentation from local tabletop data.

## Scope

This utility is reporting-only. It does not access backup systems, restore services, modify infrastructure, or perform network activity.

Use fictional exercises or records you are authorized to review.
