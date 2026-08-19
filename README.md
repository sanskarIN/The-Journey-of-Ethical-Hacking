# The Journey of Ethical Hacking — Companion Resources

Official defensive, authorization-first companion repository for **The Journey of Ethical Hacking — 2026 Edition**.

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Author:** Ram Sandesh  
**Repository:** https://github.com/sanskarIN/The-Journey-of-Ethical-Hacking  
**Official Gumroad:** https://ramsandesh.gumroad.com  
**Contact:** sanskarin@outlook.in  
**Current companion candidate:** `2026.08.19.1`

## Quick navigation

- [Get the book on Gumroad](https://ramsandesh.gumroad.com)
- [Complete documentation index](docs/INDEX.md)
- [Defensive companion project suite](docs/COMPANION_PROJECTS.md)
- [20-project companion matrix](companion-projects/PROJECT_MATRIX.md)
- [Companion CLI contract](companion-projects/CLI_CONTRACT.md)
- [Companion testing guide](companion-projects/TESTING.md)
- [Repository policy status](docs/POLICY_STATUS.md)
- [Current release readiness](docs/RELEASE_READINESS.md)
- [Current release candidate](docs/RELEASE_CANDIDATE.md)
- [Current release-branch policy](docs/RELEASE_BRANCH.md)
- [Gumroad storefront and badge guide](docs/GUMROAD.md)
- [Complete 200-part learning index](resources/learning_stage_index.md)
- [Contributor development setup](docs/DEVELOPMENT.md)
- [First-time contributor onboarding](docs/CONTRIBUTOR_ONBOARDING.md)
- [Issue triage guidance](docs/ISSUE_TRIAGE.md)
- [Synthetic dataset data dictionary](docs/DATA_DICTIONARY.md)
- [Tagged companion releases](docs/TAGGED_RELEASES.md)
- [Manifest review guide](docs/MANIFEST_REVIEW.md)
- [Recommended GitHub repository metadata](docs/REPOSITORY_METADATA.md)
- [Dependabot review procedure](docs/DEPENDABOT_REVIEW.md)
- [Synthetic dataset catalog](datasets/README.md)
- [Dataset contract schemas](schemas/README.md)
- [Fictional tabletop exercises](exercises/README.md)
- [Worked synthetic-dataset contribution example](examples/new_dataset_contribution/README.md)
- [Offline analysis examples](docs/OFFLINE_ANALYSIS_EXAMPLES.md)
- [Documentation accessibility guide](docs/ACCESSIBILITY.md)
- [Companion resource style guide](docs/RESOURCE_STYLE_GUIDE.md)
- [Public release checklist](docs/RELEASE_CHECKLIST.md)
- [Release snapshot](docs/RELEASE_SNAPSHOT.md)
- [Annual edition maintenance](docs/ANNUAL_EDITION_MAINTENANCE.md)
- [Book errata log](ERRATA.md)
- [Safe contribution guide](CONTRIBUTING.md)
- [Responsible-use and security policy](SECURITY.md)
- [Repository citation metadata](CITATION.cff)
- [Repository roadmap](ROADMAP.md)
- [Detailed change audit](what_changed.md)
- [`COMPANION_RELEASE.json`](COMPANION_RELEASE.json) — machine-readable release metadata

## What this repository contains

This public repository contains safe companion material: synthetic datasets, offline labs, checklists, templates, defensive examples, learning-roadmap files, local analysis helpers, validation tools, unit/CLI tests, fictional tabletop exercises, and contribution/release documentation.

### Learning resources

The series index is split into **20 stages covering Parts 1–200**, with corrected part titles and safe companion-practice guidance for every stage. CI verifies that every Part 1–200 appears exactly once across those stage files.

### Synthetic datasets

The repository contains small fictional datasets for asset posture, control evidence, risk signals, cloud posture, privacy controls, endpoint fleets, SaaS governance, resilience exercises, governance controls, and workforce capability. Machine-readable contracts under `schemas/` define expected columns, primary IDs, approved categorical values, and useful integer constraints. `docs/DATA_DICTIONARY.md` provides a generated human-readable view of those contracts and is freshness-checked by CI.

### Repeatable contributor environment

The local/CI baseline is Python **3.12** with pinned development dependencies in `requirements-dev.txt`. See `docs/DEVELOPMENT.md` for Windows, Linux, and macOS setup commands. CI validates that workflow Python versions match `.python-version`, that development dependencies remain pinned, and that every Python source compiles before the deeper test gates run.

### Defensive companion projects

The repository includes **20 complete offline companion projects** under `companion-projects/`. Each project has its own README, focused Python implementation, and deterministic unit tests.

Current projects cover local log summarization, file integrity, indicator normalization, incident timelines, saved email-header review, secrets redaction, evidence inventory, access review, configuration drift, asset inventories, checklist progress, backup verification, JSONL event validation, data-retention review, change-control notes, permission-matrix auditing, control/evidence mapping, exception-register validation, patch-register reporting, and recovery-exercise reporting.

The suite structure validator checks the 20-project floor, required suite documentation, README catalog coverage, project-matrix row count, offline/tested matrix status, per-project README headings, implementations, and tests.

Compile every Python source:

```bash
python -m compileall -q tools tests companion-projects
```

List the project-owned tests:

```bash
python companion-projects/run_tests.py --list
```

Run every project-owned companion test:

```bash
python companion-projects/run_tests.py
```

Validate the complete 20-project structure:

```bash
python tools/companion_projects_check.py --root .
```

See `docs/COMPANION_PROJECTS.md`, `companion-projects/PROJECT_MATRIX.md`, `companion-projects/CLI_CONTRACT.md`, and `companion-projects/TESTING.md` for the complete project catalog and engineering rules.

### Offline utilities

Current local-only Python helpers include:

- `tools/risk_priority.py`
- `tools/evidence_freshness.py`
- `tools/control_review.py`
- `tools/dataset_summary.py`
- `tools/csv_quality.py`
- `tools/dataset_contracts.py`
- `tools/data_dictionary.py`
- `tools/json_metadata.py`
- `tools/release_consistency.py`
- `tools/learning_index_check.py`
- `tools/action_pinning.py`
- `tools/dev_environment.py`
- `tools/public_repo_policy.py`
- `tools/companion_projects_check.py`
- `tools/policy_status.py`
- `tools/tag_preflight.py`
- `tools/resource_manifest.py`
- `tools/manifest_verify.py`
- `tools/release_readiness.py`
- `tools/synthetic_safety.py`
- `tools/doc_accessibility.py`
- `tools/markdown_links.py`
- `tools/gumroad_presence.py`
- `tools/docs_toc.py`
- `tools/repo_health.py`

Install the pinned development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Run the main pytest suite with coverage reporting and CLI smoke tests:

```bash
python -m pytest --cov=tools --cov-report=term-missing -q
```

Run all repository structural and policy checks from one entry point:

```bash
python tools/repo_health.py --root .
```

Review the generated policy summary and pre-tag release verdict:

```bash
python tools/policy_status.py --root . --output docs/POLICY_STATUS.md --check
python tools/release_readiness.py --root . --output docs/RELEASE_READINESS.md --check
```

Validate the intended companion tag:

```bash
python tools/tag_preflight.py --root . --tag companion-v2026.08.19.1
```

Generate and verify a machine-readable public-resource manifest:

```bash
python tools/resource_manifest.py --root . --output PUBLIC_RESOURCE_MANIFEST.json
python tools/manifest_verify.py --root . PUBLIC_RESOURCE_MANIFEST.json
```

## Release integrity and repository policy

The repository CI and local health tooling validate:

- Python source compilation across `tools/`, `tests/`, and `companion-projects/`;
- main pytest/coverage and CLI smoke tests, including every discovered companion-project CLI;
- all project-owned companion tests;
- immutable full-SHA GitHub Actions references;
- contributor/CI Python and pinned development dependency consistency;
- required public community/governance files;
- exclusion of commercial publication/archive file types from the public repository;
- exclusion of direct X/Twitter URLs;
- the 20-project companion-suite structure, catalog, project matrix, documentation, implementations, and tests;
- synthetic CSV structure and richer dataset contracts;
- generated data-dictionary freshness;
- release/schema JSON metadata, including `companion_projects: 20` and offline scope;
- release/citation/candidate/readiness/release-branch version consistency;
- Parts 1–200 learning-index integrity;
- documentation TOC freshness;
- sensitive-looking values in public synthetic datasets;
- Markdown accessibility basics and relative links;
- the exact official Gumroad storefront URL on core public-facing pages, citation/funding metadata, generated docs, and all 20 learning-stage pages;
- generated repository policy-status freshness;
- generated release-readiness freshness;
- exact `companion-vYYYY.MM.DD.N` tag naming against release metadata;
- public-resource manifest generation and SHA-256 verification.

Both the manual release-candidate workflow and the tagged-release workflow run the strengthened compilation/test/20-project gates before accepting release evidence.

## Current release candidate

The active `main` candidate is **`2026.08.19.1`**, expected tag **`companion-v2026.08.19.1`**. The reviewed candidate should be frozen on **`release/companion-v2026.08.19.1`** before tagging.

The earlier `release/companion-v2026.08.18.6` branch is retained as historical evidence for the pre-expansion snapshot and should not be moved to the newer state.

## Maintenance automation

- External GitHub Actions are pinned to verified full commit SHAs, with release-version comments for readability.
- Dependabot checks GitHub Actions and pip development dependencies monthly.
- CI and contributor machines install the same pinned `requirements-dev.txt`.
- `.github/CODEOWNERS` assigns `@sanskarIN` as the default review owner.
- `.github/release.yml` configures generated release notes.
- `docs/DEPENDENCY_ACTION_REVIEW.md` records accepted/deferred maintenance decisions.
- `docs/DEPENDABOT_REVIEW.md` documents review rules for future dependency PRs.
- `docs/REPOSITORY_METADATA.md` records the recommended About description, Gumroad website, and topics for manual GitHub settings.

## Safety boundary

Use these resources only for lawful, authorized, defensive learning. The repository intentionally excludes credential attacks, malware, stealth/evasion, unauthorized scanning, destructive actions, instructions for bypassing security controls, and sensitive real-world target data.

The `companion-projects/` suite follows the same boundary and is intentionally offline: it accepts explicit local files or directories and does not perform live-target discovery or network access.

## Licensing

- Companion source code and files explicitly covered by the repository license: **Apache License 2.0**.
- Book manuscript, publication PDF/EPUB, cover, diagrams, certificates, and commercial publishing assets: **Copyright © 2026 Ram Sandesh. All rights reserved**, unless a specific file explicitly states otherwise.

The paid master manuscript and complete commercial eBook files are intentionally **not** stored in this public repository.

## Official book storefront

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Direct link:** https://ramsandesh.gumroad.com

## Publication note

The publication and repository do not use an author avatar/photo/person image. X/Twitter links are intentionally omitted to avoid stale profile information.
