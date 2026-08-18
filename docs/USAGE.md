# Companion Resource Usage Guide

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

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

## Example: dataset summary

```bash
python tools/dataset_summary.py datasets/*.csv
```

## Run repository health checks

```bash
python tools/repo_health.py --root .
```

## Run tests

```bash
python -m pip install pytest pytest-cov
python -m pytest --cov=tools --cov-report=term-missing -q
```

## Safety note

The utilities are intentionally limited to local files. They do not scan networks, access accounts, authenticate to services, control devices, exploit vulnerabilities, or bypass security controls.

For the complete publication and current listings, use **https://ramsandesh.gumroad.com**.
