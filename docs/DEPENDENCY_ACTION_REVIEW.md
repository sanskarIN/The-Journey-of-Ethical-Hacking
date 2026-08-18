# Dependency and GitHub Actions Review Log

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This file records dependency and workflow-action review decisions for the public companion repository.

## Current CI and development dependencies

The repository currently relies on:

- Python **3.12** as the repository/CI baseline (`.python-version`).
- `pytest==9.1.1` in `requirements-dev.txt`.
- `pytest-cov==7.1.0` in `requirements-dev.txt`.
- `actions/checkout` release **v7.0.1**, pinned to full SHA `3d3c42e5aac5ba805825da76410c181273ba90b1`.
- `actions/setup-python` release **v7.0.0**, pinned to full SHA `5fda3b95a4ea91299a34e894583c3862153e4b97`.
- `actions/upload-artifact` release **v7.0.1**, pinned to full SHA `043fb46d1a93c77aae656e7c1c64a875d1fc6a0a` in the tagged-release manifest workflow.

CI installs the same `requirements-dev.txt` used by contributors so local and GitHub test environments do not silently drift apart.

## Action pinning policy

GitHub documents full-length commit SHAs as the immutable way to reference an action. This repository therefore pins external GitHub-maintained actions to verified full release SHAs and keeps the human-readable release version as an inline comment.

Policy:

1. Resolve the SHA from the official upstream GitHub action repository/release.
2. Use the full 40-character SHA in workflow `uses:` references.
3. Keep a version comment such as `# v7.0.1` on the same line.
4. Let Dependabot monitor GitHub Actions references monthly.
5. Review and validate every proposed action update before merge.
6. Keep workflow `permissions` at the minimum needed for the job.

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
4. Resolve and verify the full upstream SHA for accepted action releases.
5. Run the full test and validation workflow after each change.
6. Document why an upgrade was accepted, deferred, or rejected.
7. Avoid adding unnecessary runtime dependencies when the Python standard library is sufficient.
8. Review Dependabot-generated updates and reject updates that do not fit the repository's compatibility policy.
9. Keep `.python-version`, `requirements-dev.txt`, contributor documentation, and CI installation steps synchronized.

## Decision record

### 2026-08-18 — immutable GitHub Actions references

- Replaced movable v7 action tags in repository workflows with verified full commit SHAs.
- Pinned checkout to the v7.0.1 release commit.
- Pinned setup-python to the v7.0.0 release commit.
- Pinned upload-artifact to the v7.0.1 release commit.
- Retained version comments for human readability and Dependabot maintenance.

### 2026-08-18 — repeatable contributor environment

- Added `.python-version` with Python 3.12.
- Added pinned `requirements-dev.txt` with `pytest==9.1.1` and `pytest-cov==7.1.0`.
- Updated CI to install the pinned development requirements.
- Added monthly Dependabot checks for pip dependencies.
- Added `docs/DEVELOPMENT.md` for reproducible local setup.

### 2026-08-18 — action major-version refresh

- Upgraded `actions/checkout` from v4 to the v7 release line.
- Upgraded `actions/setup-python` from v5 to the v7 release line.
- Added `actions/upload-artifact` v7 release line for tagged public-resource manifests.
- Added monthly Dependabot checks for GitHub Actions.
- Retained Python 3.12 as the CI interpreter for this companion-resource snapshot.
- No runtime networking/security-tool dependencies were introduced.

## Publication boundary

Dependency maintenance must never require committing the commercial manuscript or paid publication assets to the public repository.

**Official publication storefront:** https://ramsandesh.gumroad.com
