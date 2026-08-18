# Dependency and GitHub Actions Review Log

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This file records dependency and workflow-action review decisions for the public companion repository.

## Current CI and development dependencies

The repository currently relies on:

- Python **3.12** as the repository/CI baseline (`.python-version`).
- `pytest==9.1.1` in `requirements-dev.txt`.
- `pytest-cov==7.1.0` in `requirements-dev.txt`.
- `actions/checkout@v7`.
- `actions/setup-python@v7`.
- `actions/upload-artifact@v7` in the tagged-release manifest workflow.

CI installs the same `requirements-dev.txt` used by contributors so local and GitHub test environments do not silently drift apart.

## 2026-08-18 upstream review

The official GitHub-maintained action projects were reviewed before upgrading the repository workflows.

- `actions/checkout` uses the v7 major line; the repository CI was upgraded from v4 to v7.
- `actions/setup-python` uses the v7 major line; the repository CI was upgraded from v5 to v7.
- `actions/upload-artifact` uses the v7 major line and is used by the release-manifest workflow.
- The repository continues to explicitly request Python 3.12 for deterministic CI behavior.
- The repository uses GitHub-hosted `ubuntu-latest` runners rather than self-hosted runners.

Official upstream projects:

- https://github.com/actions/checkout
- https://github.com/actions/setup-python
- https://github.com/actions/upload-artifact

## Automated maintenance

`.github/dependabot.yml` requests monthly update checks for:

- GitHub Actions dependencies; and
- Python/pip development dependencies in `requirements-dev.txt`.

Dependency PRs should still be reviewed before merge; automatic discovery does not replace compatibility review.

## Review process

At least during each edition refresh:

1. Check official upstream release/security information for actions and Python test dependencies in use.
2. Review breaking changes before changing a major version.
3. Prefer a dedicated maintenance commit for each dependency/action upgrade.
4. Run the full test and validation workflow after each change.
5. Document why an upgrade was accepted, deferred, or rejected.
6. Avoid adding unnecessary runtime dependencies when the Python standard library is sufficient.
7. Review Dependabot-generated updates and reject updates that do not fit the repository's compatibility policy.
8. Keep `.python-version`, `requirements-dev.txt`, contributor documentation, and CI installation steps synchronized.

## Decision record

### 2026-08-18 — repeatable contributor environment

- Added `.python-version` with Python 3.12.
- Added pinned `requirements-dev.txt` with `pytest==9.1.1` and `pytest-cov==7.1.0`.
- Updated CI to install the pinned development requirements.
- Added monthly Dependabot checks for pip dependencies.
- Added `docs/DEVELOPMENT.md` for reproducible local setup.

### 2026-08-18 — action major-version refresh

- Upgraded `actions/checkout` from v4 to v7.
- Upgraded `actions/setup-python` from v5 to v7.
- Added `actions/upload-artifact@v7` for tagged public-resource manifests.
- Added monthly Dependabot checks for GitHub Actions.
- Retained Python 3.12 as the CI interpreter for this companion-resource snapshot.
- No runtime networking/security-tool dependencies were introduced.

## Publication boundary

Dependency maintenance must never require committing the commercial manuscript or paid publication assets to the public repository.

**Official publication storefront:** https://ramsandesh.gumroad.com
