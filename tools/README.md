# Offline Defensive Tools

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

The utilities in this directory operate only on local repository files.

## Analysis helpers

- `risk_priority.py` — ranks fictional/synthetic risk-signal rows for review-priority exercises.
- `evidence_freshness.py` — groups fictional/local control evidence into freshness buckets.
- `control_review.py` — ranks fictional control-evidence records for assurance review.
- `dataset_summary.py` — reports CSV row/column counts, blank cells, and field names.

## Data and metadata validation

- `csv_quality.py` — checks structural quality of synthetic CSV files.
- `dataset_contracts.py` — validates datasets against machine-readable contracts.
- `json_metadata.py` — validates release and dataset-contract JSON structure.
- `synthetic_safety.py` — flags sensitive-looking values such as email, URL, IP, or token-like strings in public synthetic CSV files.

## Documentation and storefront validation

- `doc_accessibility.py` — checks basic Markdown accessibility expectations.
- `markdown_links.py` — checks relative Markdown links.
- `gumroad_presence.py` — enforces the direct official Gumroad URL across core public-facing docs and release metadata.

## Release integrity helpers

- `resource_manifest.py` — generates SHA-256 metadata for public companion resources while excluding commercial publication formats.
- `repo_health.py` — runs the repository's structural validation checks from one command.

## Common commands

```bash
python tools/dataset_summary.py datasets/*.csv
python tools/repo_health.py --root .
python tools/resource_manifest.py --root . --output PUBLIC_RESOURCE_MANIFEST.json
```

## Safety design

These tools intentionally do not include networking, scanning, authentication, account access, device control, exploitation, malware, evasion, persistence, credential extraction, surveillance, or security-control bypass logic.

For the complete publication and current listings, use **https://ramsandesh.gumroad.com**.
