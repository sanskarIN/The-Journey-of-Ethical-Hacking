# Tests

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This directory validates the repository's local-only defensive and release-integrity utilities.

Run the test suite from the repository root:

```bash
python -m pip install pytest pytest-cov
python -m pytest --cov=tools --cov-report=term-missing -q
```

## Current coverage areas

The suite includes tests for:

- risk prioritization;
- evidence freshness;
- control-review scoring;
- CSV structure quality;
- richer dataset contracts and duplicate-ID checks;
- release/schema JSON metadata;
- release-version consistency;
- dataset summaries;
- Parts 1–200 learning-index integrity;
- documentation TOC generation;
- Markdown accessibility;
- relative Markdown links;
- repository health orchestration;
- public-resource manifest generation;
- synthetic-data sensitivity linting;
- Gumroad storefront presence across core docs and all learning stages;
- CLI `--help` smoke coverage for local tools.

The tests use deterministic local data and do not require network access, accounts, credentials, devices, or external services.

For the complete publication and current listings, use **https://ramsandesh.gumroad.com**.
