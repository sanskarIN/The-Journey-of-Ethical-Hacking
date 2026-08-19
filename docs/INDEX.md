# Documentation Index

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This page is the central index for public companion-repository documentation.

## Start here

- [`TOC.md`](TOC.md) — generated table of contents for files in `docs/`.
- [`../README.md`](../README.md) — repository overview and quick start.
- [`COMPANION_PROJECTS.md`](COMPANION_PROJECTS.md) — overview of the 20-project offline defensive companion suite.
- [`../companion-projects/PROJECT_MATRIX.md`](../companion-projects/PROJECT_MATRIX.md) — project-by-project skill, input, network, and test matrix.
- [`GUMROAD.md`](GUMROAD.md) — official storefront and GitHub badge guidance.
- [`USAGE.md`](USAGE.md) — companion-resource usage guidance.
- [`DEVELOPMENT.md`](DEVELOPMENT.md) — repeatable contributor environment and validation setup.
- [`POLICY_STATUS.md`](POLICY_STATUS.md) — generated repository policy/release review status.
- [`RELEASE_READINESS.md`](RELEASE_READINESS.md) — generated deterministic pre-tag release verdict.
- [`OFFLINE_ANALYSIS_EXAMPLES.md`](OFFLINE_ANALYSIS_EXAMPLES.md) — local-only analysis examples.
- [`../resources/learning_stage_index.md`](../resources/learning_stage_index.md) — complete Parts 1–200 learning navigation.

## Safety, accessibility, and contribution

- [`../SECURITY.md`](../SECURITY.md) — responsible-use and private security reporting.
- [`../CONTRIBUTING.md`](../CONTRIBUTING.md) — safe contribution requirements.
- [`../companion-projects/SAFETY.md`](../companion-projects/SAFETY.md) — companion-suite authorization and data-handling boundary.
- [`../companion-projects/THREAT_MODEL.md`](../companion-projects/THREAT_MODEL.md) — companion-suite threat model and non-goals.
- [`../companion-projects/CONTRIBUTING.md`](../companion-projects/CONTRIBUTING.md) — project proposal and testing requirements.
- [`../companion-projects/SYNTHETIC_DATA_GUIDE.md`](../companion-projects/SYNTHETIC_DATA_GUIDE.md) — safe synthetic fixture guidance.
- [`../companion-projects/MAINTENANCE_CHECKLIST.md`](../companion-projects/MAINTENANCE_CHECKLIST.md) — suite maintenance checklist.
- [`../companion-projects/CHANGELOG.md`](../companion-projects/CHANGELOG.md) — dedicated companion-project history.
- [`CONTRIBUTOR_ONBOARDING.md`](CONTRIBUTOR_ONBOARDING.md) — first-time contributor checklist.
- [`ISSUE_TRIAGE.md`](ISSUE_TRIAGE.md) — issue classification and maintenance guidance.
- [`ACCESSIBILITY.md`](ACCESSIBILITY.md) — Markdown accessibility guidance.
- [`RESOURCE_STYLE_GUIDE.md`](RESOURCE_STYLE_GUIDE.md) — dataset/template writing style.
- [`../CODE_OF_CONDUCT.md`](../CODE_OF_CONDUCT.md) — community conduct.
- [`GIT_COMMIT_IDENTITY.md`](GIT_COMMIT_IDENTITY.md) — requested local commit-email configuration.

## Data and validation

- [`../datasets/README.md`](../datasets/README.md) — synthetic dataset catalog.
- [`../schemas/README.md`](../schemas/README.md) — machine-readable dataset contracts.
- [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md) — generated field/constraint documentation for all synthetic datasets.
- [`../tools/README.md`](../tools/README.md) — local-only analysis and release-integrity utility catalog.
- [`../tests/README.md`](../tests/README.md) — unit and CLI smoke-test guidance.
- [`../companion-projects/ARCHITECTURE.md`](../companion-projects/ARCHITECTURE.md) — companion-suite architecture and testing model.
- [`../companion-projects/PROJECT_STANDARD.md`](../companion-projects/PROJECT_STANDARD.md) — engineering baseline for every companion project.
- [`../examples/new_dataset_contribution/README.md`](../examples/new_dataset_contribution/README.md) — worked contributor dataset example.

Key validation entry points:

```bash
python -m pytest --cov=tools --cov-report=term-missing -q
python companion-projects/run_tests.py
python tools/companion_projects_check.py --root .
python tools/repo_health.py --root .
python tools/action_pinning.py --root .
python tools/dev_environment.py --root .
python tools/public_repo_policy.py --root .
python tools/policy_status.py --root . --output docs/POLICY_STATUS.md --check
python tools/release_consistency.py --root .
python tools/learning_index_check.py --root .
python tools/docs_toc.py --docs-dir docs --output docs/TOC.md --check
python tools/data_dictionary.py schemas/dataset_contracts.json --output docs/DATA_DICTIONARY.md --check
python tools/tag_preflight.py --root . --tag companion-v2026.08.18.6
python tools/release_readiness.py --root . --output docs/RELEASE_READINESS.md --check
python tools/resource_manifest.py --root . --output PUBLIC_RESOURCE_MANIFEST.json
python tools/manifest_verify.py --root . PUBLIC_RESOURCE_MANIFEST.json
```

## Exercises and learning resources

- [`../exercises/README.md`](../exercises/README.md) — seven fictional tabletop exercise packs.
- [`../resources/README.md`](../resources/README.md) — templates, checklists, mastery resources, and glossary seed.
- [`../companion-projects/README.md`](../companion-projects/README.md) — 20 local defensive mini-projects with independent documentation, code, and tests.
- [`../companion-projects/ROADMAP.md`](../companion-projects/ROADMAP.md) — safe future project and quality roadmap.

## Corrections, release, and maintenance

- [`../ERRATA.md`](../ERRATA.md) — public correction log.
- [`ERRATA_PROCESS.md`](ERRATA_PROCESS.md) — correction workflow.
- [`RELEASE_BRANCH.md`](RELEASE_BRANCH.md) — stable release-branch policy before creating the final tag.
- [`RELEASE_CANDIDATE.md`](RELEASE_CANDIDATE.md) — current `2026.08.18.6` candidate and manual tag procedure.
- [`RELEASE_CHECKLIST.md`](RELEASE_CHECKLIST.md) — companion release gate.
- [`RELEASE_READINESS.md`](RELEASE_READINESS.md) — generated pre-tag readiness report.
- [`RELEASE_SNAPSHOT.md`](RELEASE_SNAPSHOT.md) — current release-integrity expectations.
- [`TAGGED_RELEASES.md`](TAGGED_RELEASES.md) — tag naming and automatic release-manifest workflow.
- [`PUBLIC_RESOURCE_MANIFEST.md`](PUBLIC_RESOURCE_MANIFEST.md) — manifest generation guidance.
- [`MANIFEST_REVIEW.md`](MANIFEST_REVIEW.md) — downloaded manifest verification and review steps.
- [`RELEASE_NOTES_AUTOMATION.md`](RELEASE_NOTES_AUTOMATION.md) — release-note workflow guidance.
- [`ANNUAL_EDITION_MAINTENANCE.md`](ANNUAL_EDITION_MAINTENANCE.md) — yearly refresh checklist.
- [`DEPENDENCY_ACTION_REVIEW.md`](DEPENDENCY_ACTION_REVIEW.md) — dependency/action review decisions.
- [`DEPENDABOT_REVIEW.md`](DEPENDABOT_REVIEW.md) — review procedure for future dependency PRs.
- [`REPOSITORY_METADATA.md`](REPOSITORY_METADATA.md) — recommended GitHub About description, Gumroad website, and topics.
- [`REPOSITORY_STRUCTURE.md`](REPOSITORY_STRUCTURE.md) — current public repository layout.
- [`../CITATION.cff`](../CITATION.cff) — repository and book citation metadata.
- [`../COMPANION_RELEASE.json`](../COMPANION_RELEASE.json) — machine-readable release/storefront metadata.
- [`../CHANGELOG.md`](../CHANGELOG.md) — notable repository changes.
- [`../ROADMAP.md`](../ROADMAP.md) — completed and future phases.
- [`../what_changed.md`](../what_changed.md) — detailed implementation audit.

## Publication boundary

The commercial master manuscript, paid PDF/EPUB, cover, certificate, and store-delivery files are not stored in this public repository.

For the complete publication and current listings, use **https://ramsandesh.gumroad.com**.
