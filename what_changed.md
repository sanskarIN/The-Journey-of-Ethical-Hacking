# What Changed

## 2026-08-18 companion repository build

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

### Publication/privacy decisions retained

- No author avatar/photo/person image is used by the publication-resource design.
- X/Twitter links are intentionally omitted.
- The paid master manuscript, complete commercial PDF/EPUB, cover, and store assets are not committed to this public repository.

### Commit metadata note

The connected GitHub write API used for this build does not expose an author-email field. Therefore the requested `sanskarin@outlook.in` value could not be forcibly written into individual commit author metadata through this connector; commits are attributed by GitHub through the connected account.
