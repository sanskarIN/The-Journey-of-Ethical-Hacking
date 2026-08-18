# Tests

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This directory validates the repository's local-only defensive utilities.

Run the test suite from the repository root:

```bash
python -m pip install pytest pytest-cov
python -m pytest --cov=tools --cov-report=term-missing -q
```

The suite covers offline analysis helpers, CSV quality checks, dataset contracts, JSON metadata, Markdown accessibility, relative-link validation, and dataset summaries.

The tests use deterministic local data and do not require network access, accounts, credentials, devices, or external services.

For the complete publication and current listings, use **https://ramsandesh.gumroad.com**.
