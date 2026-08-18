# What Changed

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

## 2026-08-18 — Companion release 2026.08.18.6 and repository policy automation

This phase continued the public companion repository from general quality improvements into a release-ready, policy-checked maintenance model. The repository remains defensive, authorization-first, and intentionally separate from the commercial book delivery files.

### Gumroad storefront visibility

- Retained `https://ramsandesh.gumroad.com` as the canonical publication storefront.
- Added/retained the Gumroad Shields badge on the README and major reader-facing documentation.
- Added the Gumroad badge/direct link to **all 20 learning-stage pages**, covering Parts 1–200.
- Added the storefront to `CITATION.cff`, `.github/FUNDING.yml`, the GitHub issue chooser, release metadata, release snapshot, policy status, and public documentation indexes.
- Expanded `tools/gumroad_presence.py` so CI verifies the official Gumroad URL across core public docs, all 20 learning stages, citation/funding metadata, and `COMPANION_RELEASE.json`.
- Kept URL shorteners and X/Twitter profile links out of the publication-facing repository path.

### Repository release metadata

- Advanced the companion snapshot through `2026.08.18.5` to **`2026.08.18.6`**.
- Synchronized `COMPANION_RELEASE.json`, `CHANGELOG.md`, `docs/RELEASE_SNAPSHOT.md`, and `CITATION.cff`.
- Expanded `tools/release_consistency.py` so `CITATION.cff` must use the same active companion version.
- Added `docs/TAGGED_RELEASES.md` with the `companion-vYYYY.MM.DD.N` tag convention and release checklist.

### Tagged release manifest automation

- Added `.github/workflows/release-manifest.yml`.
- `companion-v*` tags and manual dispatch can run repository health/version checks, generate `PUBLIC_RESOURCE_MANIFEST.json`, and upload it as an Actions artifact.
- Added `docs/PUBLIC_RESOURCE_MANIFEST.md` and release guidance for manifest review.
- Kept commercial publication formats outside the manifest by design.

### Immutable GitHub Actions policy

- Reviewed the official GitHub-maintained Actions used by the repository.
- Upgraded and pinned external workflow actions to verified full release SHAs:
  - `actions/checkout` v7.0.1 → `3d3c42e5aac5ba805825da76410c181273ba90b1`;
  - `actions/setup-python` v7.0.0 → `5fda3b95a4ea91299a34e894583c3862153e4b97`;
  - `actions/upload-artifact` v7.0.1 → `043fb46d1a93c77aae656e7c1c64a875d1fc6a0a`.
- Added `tools/action_pinning.py` with unit tests so movable external action tags/branches fail repository validation.
- Documented the SHA-pinning policy and upgrade decisions in `docs/DEPENDENCY_ACTION_REVIEW.md`.

### Repeatable contributor and CI environment

- Added `.python-version` with Python 3.12.
- Added pinned `requirements-dev.txt` with the repository test dependencies.
- Added `docs/DEVELOPMENT.md` with Windows PowerShell and Linux/macOS setup instructions.
- Updated CI to install the same pinned development requirements used by contributors.
- Added `tools/dev_environment.py` plus tests to enforce workflow Python-version alignment and exact dependency pins.
- Added monthly Dependabot monitoring for both GitHub Actions and pip development dependencies.

### Dataset contracts and generated documentation

- Strengthened `schemas/dataset_contracts.json` to version 2.
- Added approved categorical-value rules, integer ranges, and duplicate primary-ID validation across all ten synthetic datasets.
- Added `tools/data_dictionary.py` and unit tests.
- Added generated `docs/DATA_DICTIONARY.md` covering all synthetic dataset columns/constraints.
- Added `--check` freshness mode so contract changes cannot leave the committed data dictionary stale.
- Wired data-dictionary freshness into CI and `tools/repo_health.py`.

### Documentation freshness and navigation

- Added `tools/docs_toc.py` and tests.
- Added generated `docs/TOC.md`.
- Added `--check` mode so adding/removing/renaming documentation without regenerating the TOC fails validation.
- Expanded `docs/INDEX.md`, README, tools catalog, and test catalog for the current repository structure.
- Added `docs/CONTRIBUTOR_ONBOARDING.md` and `docs/ISSUE_TRIAGE.md`.

### GitHub community and collaboration improvements

- Added `.github/ISSUE_TEMPLATE/dataset_improvement.yml`.
- Added `.github/ISSUE_TEMPLATE/tool_bug.yml`.
- Added `.github/ISSUE_TEMPLATE/config.yml` with Gumroad and security contact links.
- Added `.github/CODEOWNERS` with `@sanskarIN` as the default review owner.
- Added `.github/release.yml` for generated GitHub release-note categorization.
- Added `docs/REPOSITORY_METADATA.md` documenting the recommended GitHub About description, Gumroad website, and topics because the connected maintenance API does not expose About/topics write settings.
- Confirmed there were no open issues or pull requests during this maintenance pass.

### Parts 1–200 integrity

- Added `tools/learning_index_check.py` and unit tests.
- The checker requires exactly 20 learning-stage files, ten parts per stage, and Parts 1–200 exactly once.
- Wired the checker into CI and the consolidated repository health command.

### Public repository boundary automation

- Added `tools/public_repo_policy.py` and tests.
- The policy checker requires core community/governance files.
- It rejects commercial publication/archive formats such as PDF, EPUB, DOCX, MOBI/AZW, and ZIP from the public companion repository.
- It rejects direct X/Twitter URLs from repository text.
- The policy source/test fixtures were adjusted so the repository does not need to store a direct disallowed social URL just to test the rule.
- GitHub code search showed no direct stored `x.com`/`twitter.com` URL matches after cleanup.

### Generated repository policy status

- Added `tools/policy_status.py` and tests.
- Added generated `docs/POLICY_STATUS.md`.
- The report summarizes the release's deterministic policy results for:
  - immutable action references;
  - dev-environment consistency;
  - public repository boundaries;
  - release/citation consistency;
  - Parts 1–200 integrity;
  - Gumroad presence;
  - generated data-dictionary freshness;
  - generated documentation-TOC freshness.
- Added a freshness gate so `POLICY_STATUS.md` must match the live validators.

### CI and repository health

The main CI and `tools/repo_health.py` now cover the policy/release layers in addition to the earlier quality checks. The current gate includes:

- unit tests and coverage;
- immutable Actions SHA validation;
- contributor/CI environment consistency;
- public repository boundary validation;
- CSV structural checks;
- dataset contract validation;
- generated data-dictionary freshness;
- release/schema JSON validation;
- release/citation-version consistency;
- Parts 1–200 learning-index integrity;
- documentation TOC freshness;
- synthetic-data sensitivity checks;
- Markdown accessibility checks;
- relative Markdown-link checks;
- official Gumroad storefront presence;
- generated policy-status freshness;
- public-resource manifest smoke generation.

### Publication/privacy decisions retained

- No author avatar/photo/person image is used by the repository publication-resource design.
- Direct X/Twitter URLs are intentionally excluded.
- The paid master manuscript, commercial PDF/EPUB, cover, certificate, and store-delivery archives are not committed to the public companion repository.
- Companion source code remains Apache-2.0 where the repository license applies; commercial book rights remain separate.

### Commit metadata note

The connected GitHub write API still does not expose an author-email field for content-API commits. Therefore `sanskarin@outlook.in` cannot be forcibly written into these API-created commit author records. `docs/GIT_COMMIT_IDENTITY.md` retains the requested local Git configuration for future command-line commits and tags.

## 2026-08-18 — Continued GitHub repository work

This continuation completed the original repository roadmap and a second repository-quality phase while keeping the public project defensive, authorization-first, and separate from the commercial book files.

### Complete Parts 1–200 learning navigation

- Added 20 dedicated stage files under `resources/learning/`.
- Each stage covers exactly 10 parts.
- The stage files contain the corrected titles for every Part 1–200.
- Updated `resources/learning_stage_index.md` to link all 20 stage files.
- Added safe companion-practice guidance to every stage without reproducing the paid manuscript.

### Expanded synthetic dataset library

Added fictional/offline samples for:

- cloud posture;
- privacy controls;
- endpoint fleet posture;
- SaaS governance;
- resilience exercises;
- governance controls;
- workforce capability.

Updated `datasets/README.md` with the complete dataset catalog and safe-use rules.

### Documentation accessibility

- Added `tools/doc_accessibility.py`.
- Added unit tests for the checker.
- Added `docs/ACCESSIBILITY.md`.
- Added accessibility checking to GitHub Actions CI.

The checker validates basic Markdown accessibility expectations such as a level-1 heading, non-empty image alt text, descriptive link text, and avoidance of tab characters.

### Defensive offline analysis utilities

Added:

- `tools/control_review.py` with tests;
- `tools/csv_quality.py` with tests;
- `docs/OFFLINE_ANALYSIS_EXAMPLES.md`.

The utilities operate only on local fictional CSV files and contain no networking, scanning, authentication, exploitation, device-access, or production-remediation behavior.

### Errata workflow

Added:

- `ERRATA.md` public correction log;
- `docs/ERRATA_PROCESS.md`;
- `resources/errata_submission_template.md`;
- `.github/ISSUE_TEMPLATE/book_errata.md`.

The workflow allows concise correction reports without publishing long passages from the commercial book.

### Link and dataset-contract validation

Added:

- `tools/markdown_links.py` and tests for relative Markdown links;
- `schemas/README.md`;
- `schemas/dataset_contracts.json`;
- `tools/dataset_contracts.py` and tests.

CI now validates CSV structure, dataset contracts, documentation accessibility, and relative Markdown links.

### Repository release quality

Added:

- `COMPANION_RELEASE.json` machine-readable release metadata;
- `docs/RESOURCE_STYLE_GUIDE.md`;
- `docs/RELEASE_CHECKLIST.md`;
- test coverage reporting in GitHub Actions.

### Fictional tabletop exercise packs

Added discussion-only packs under `exercises/` for:

- resilience and recovery;
- governance/control exceptions;
- major-incident coordination.

These exercises do not instruct readers to access, disrupt, bypass, track, exploit, or interfere with real systems or people.

### README and roadmap improvements

- Expanded README quick navigation and local validation commands.
- Marked the original 2026 companion-release roadmap complete.
- Marked the repository-quality phase complete.
- Added a new future-maintenance roadmap.
- Updated `CHANGELOG.md` for the quality expansion.

### Publication/privacy decisions retained

- No author avatar/photo/person image is used by the publication-resource design.
- X/Twitter links remain intentionally omitted.
- The paid master manuscript, commercial PDF/EPUB, cover, certificate, and store assets are not committed to this public repository.
- Companion source code remains under Apache-2.0 where the repository license applies; commercial book rights remain separate.

## 2026-08-18 — Initial companion repository build

This repository was expanded from a license-only repository into the public companion-resource home for **The Journey of Ethical Hacking — 2026 Edition**.

### Repository foundation

- Added `README.md` with the defensive learning scope.
- Added `BOOK_CONTENT_LICENSE.md` and `NOTICE` to separate Apache-2.0 companion resources from the commercial book rights.
- Added `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, and `SUPPORT.md`.
- Added `.gitignore` and `.editorconfig`.

### Defensive learning resources

- Added authorization and lab-safety checklists.
- Added finding, evidence, control-validation, incident-observation, risk-register, and recovery templates.
- Added synthetic asset inventory, control evidence, and risk signal datasets.

### Offline code and validation

- Added `tools/risk_priority.py`.
- Added `tools/evidence_freshness.py`.
- Added unit tests for both helpers.
- Added GitHub Actions CI.

### Documentation

- Added `docs/USAGE.md`.
- Added `ROADMAP.md`.
- Added `CHANGELOG.md`.
