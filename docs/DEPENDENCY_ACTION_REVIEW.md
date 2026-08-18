# Dependency and GitHub Actions Review Log

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This file records dependency and workflow-action review decisions for the public companion repository.

## Current CI dependencies

The repository currently relies on:

- Python 3.12 in CI.
- `pytest` for tests.
- `pytest-cov` for coverage reporting.
- `actions/checkout@v7`.
- `actions/setup-python@v7`.
- `actions/upload-artifact@v7` in the tagged-release manifest workflow.

## 2026-08-18 upstream review

The official GitHub-maintained action projects were reviewed before upgrading the repository workflows.

- `actions/checkout` currently publishes the v7 major line; the repository CI was upgraded from v4 to v7.
- `actions/setup-python` currently publishes the v7 major line; the repository CI was upgraded from v5 to v7.
- `actions/upload-artifact` currently publishes the v7 major line and is used by the release-manifest workflow.
- `setup-python` v7 keeps the existing action inputs/behavior while modernizing its implementation; the repository continues to explicitly request Python 3.12 for deterministic CI behavior.
- The repository uses GitHub-hosted `ubuntu-latest` runners rather than self-hosted runners.

Official upstream projects:

- https://github.com/actions/checkout
- https://github.com/actions/setup-python
- https://github.com/actions/upload-artifact

## Automated maintenance

`.github/dependabot.yml` now requests monthly GitHub Actions update checks. Dependency PRs should still be reviewed before merge; automatic discovery does not replace compatibility review.

## Review process

At least during each edition refresh:

1. Check official upstream release/security information for the actions and test dependencies in use.
2. Review breaking changes before changing a major version.
3. Prefer a dedicated maintenance commit for each dependency/action upgrade.
4. Run the full test and validation workflow after each change.
5. Document why the upgrade was accepted, deferred, or rejected.
6. Avoid adding unnecessary dependencies when the Python standard library is sufficient.
7. Review Dependabot-generated action updates and close/reject updates that do not fit the repository's compatibility policy.

## Decision record

### 2026-08-18 — action major-version refresh

- Upgraded `actions/checkout` from v4 to v7.
- Upgraded `actions/setup-python` from v5 to v7.
- Added `actions/upload-artifact@v7` for tagged public-resource manifests.
- Added monthly Dependabot checks for GitHub Actions.
- Retained Python 3.12 as the CI interpreter for this companion-resource snapshot.
- Retained `pytest` and `pytest-cov` as the only Python test dependencies.
- No runtime networking/security-tool dependencies were introduced.

## Publication boundary

Dependency maintenance must never require committing the commercial manuscript or paid publication assets to the public repository.

**Official publication storefront:** https://ramsandesh.gumroad.com
