# Dependency and GitHub Actions Review Log

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

This file records dependency and workflow-action review decisions for the public companion repository.

## Current CI dependencies

The repository currently relies on:

- Python 3.12 in CI.
- `pytest` for tests.
- `pytest-cov` for coverage reporting.
- `actions/checkout@v4`.
- `actions/setup-python@v5`.

This document intentionally records what the repository uses rather than claiming that a particular major version is permanently the newest available version.

## Review process

At least during each edition refresh:

1. Check the official upstream release/security information for the actions and test dependencies in use.
2. Review breaking changes before changing a major version.
3. Prefer a dedicated maintenance commit for each dependency/action upgrade.
4. Run the full test and validation workflow after each change.
5. Document why the upgrade was accepted, deferred, or rejected.
6. Avoid adding unnecessary dependencies when the Python standard library is sufficient.

## Decision record

### 2026-08-18

- Retained Python 3.12 as the CI interpreter for this companion-resource snapshot.
- Retained `pytest` and `pytest-cov` as the only Python test dependencies.
- Retained the currently configured GitHub Actions major versions pending a future scheduled review against official upstream documentation.
- No runtime networking/security-tool dependencies were introduced.

## Publication boundary

Dependency maintenance must never require committing the commercial manuscript or paid publication assets to the public repository.

**Official publication storefront:** https://ramsandesh.gumroad.com
