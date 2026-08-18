# What Changed

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

### Commit metadata note

The connected GitHub write API still does not expose an author-email field. Therefore `sanskarin@outlook.in` cannot be forcibly written into the API-created commit author metadata. `docs/GIT_COMMIT_IDENTITY.md` contains the requested local Git configuration for future command-line commits.

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
