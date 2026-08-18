# Companion Resource Usage Guide

These resources are designed for safe, local, defensive learning.

## Requirements

- Python 3.10+ for the small offline utilities.
- No network access is required by the included tools.
- Use only the synthetic CSV files included in this repository unless you have explicit permission to use another dataset.

## Example: risk prioritization

```bash
python tools/risk_priority.py datasets/sample_risk_signals.csv
```

## Example: evidence freshness

```bash
python tools/evidence_freshness.py datasets/sample_control_evidence.csv
```

## Run tests

```bash
python -m pip install pytest
python -m pytest -q
```

## Safety note

The utilities are intentionally limited to local files. They do not scan networks, access accounts, authenticate to services, control devices, exploit vulnerabilities, or bypass security controls.
