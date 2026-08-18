# Tests

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This directory validates the repository's local-only defensive, release-integrity, and repository-policy utilities.

## Repeatable test environment

The repository baseline is Python **3.12** (`.python-version`) with pinned development dependencies from `requirements-dev.txt`.

Install them with:

```bash
python -m pip install -r requirements-dev.txt
```

Run the test suite from the repository root:

```bash
python -m pytest --cov=tools --cov-report=term-missing -q
```

## Current coverage areas

The suite includes tests for:

- risk prioritization;
- evidence freshness;
- control-review scoring;
- CSV structure quality;
- richer dataset contracts and duplicate-ID checks;
- generated dataset data dictionaries and freshness;
- release/schema JSON metadata;
- release-version and citation-version consistency;
- dataset summaries;
- Parts 1–200 learning-index integrity;
- documentation TOC generation and freshness;
- immutable GitHub Actions SHA pinning;
- contributor/CI Python and dependency consistency;
- public repository governance/publication boundaries;
- generated repository policy status;
- Markdown accessibility;
- relative Markdown links;
- repository health orchestration;
- public-resource manifest generation;
- synthetic-data sensitivity linting;
- Gumroad storefront presence across core docs, citation/funding metadata, and all learning stages;
- CLI `--help` smoke coverage for local tools.

The tests use deterministic local data and do not require network access, accounts, credentials, devices, or external services.

For the complete publication and current listings, use **https://ramsandesh.gumroad.com**.
