# Changelog

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

All notable companion-repository changes are recorded here.

## 2026-08-19 — Companion release 2026.08.19.1

### Added

- Dedicated `companion-projects/` suite with **20 complete offline defensive mini-projects**.
- Project-specific README, focused Python implementation, and deterministic unit tests for every project.
- Suite architecture, project engineering standard, authorization/safety policy, threat model, synthetic-data guide, contribution guide, maintenance checklist, dedicated changelog, and roadmap.
- `companion-projects/CLI_CONTRACT.md` for shared CLI, output, error, and exit-code conventions.
- `companion-projects/TESTING.md` for the full local validation workflow.
- Central `companion-projects/run_tests.py` runner for project-owned tests.
- `tools/companion_projects_check.py` plus unit tests to enforce required suite files, a 20-project minimum, README catalog consistency, project-matrix consistency, and per-project README/implementation/test presence.
- Control Evidence Mapper, Exception Register Validator, Patch Register Summary, and Recovery Exercise Reporter as projects 17–20.

### Improved

- Added Python `compileall` validation to normal CI and the consolidated repository-health gate.
- Expanded CLI smoke coverage to every discovered companion-project implementation.
- Added companion-project tests and structure validation to GitHub Actions CI.
- Added the complete companion-project tree to Markdown accessibility and relative-link checks.
- Added companion-suite integrity to the generated repository policy status.
- Strengthened release consistency so candidate, readiness, release-branch, citation-version, and citation-date records must align with `COMPANION_RELEASE.json`.
- Added machine-readable `companion_projects: 20` and `companion_projects_offline: true` release metadata and validator coverage.
- Added companion-suite structure validation to `tools/repo_health.py`.
- Expanded README, docs index, tools catalog, tests catalog, release checklist, release snapshot, and repository roadmap for the 20-project suite.
- Advanced the active `main` candidate to **2026.08.19.1** while preserving `release/companion-v2026.08.18.6` as the earlier frozen candidate.

### Fixed and hardened

- Incident Timeline now requires timezone-aware timestamps.
- Access Review Helper now rejects an empty approved-role policy.
- Integrity Manifest, Evidence Inventory, and Backup Verify ignore symbolic links during recursive file walks.
- Removed an unused import from IOC Normalizer.

### Safety and publication boundary

All companion projects remain local/offline and authorization-first. They intentionally avoid exploit delivery, credential collection, malware behavior, persistence, evasion, destructive actions, live-target discovery, and unauthorized scanning. Commercial manuscript and paid publication files remain outside the public repository.

## 2026-08-18 — Companion release 2026.08.18.6

### Added

- Tagged companion-release workflow that validates the repository and uploads `PUBLIC_RESOURCE_MANIFEST.json` as a release artifact.
- Monthly Dependabot checks for GitHub Actions and pinned pip development dependencies.
- Recommended GitHub About metadata/topics guide with Gumroad as the preferred repository website.
- GitHub `CITATION.cff` metadata for the companion repository and commercial book citation.
- GitHub custom funding/storefront link pointing to `https://ramsandesh.gumroad.com`.
- Issue chooser contact links for the official Gumroad storefront and security policy.
- Dedicated issue forms for synthetic-dataset improvements and local tool/test bugs.
- Parts 1–200 learning-index integrity checker and unit tests.
- Tagged-release workflow documentation.
- Generated synthetic dataset data dictionary plus freshness validation.
- Documentation TOC freshness validation.
- Repeatable Python 3.12 contributor environment with pinned `requirements-dev.txt`.
- `.github/CODEOWNERS` with `@sanskarIN` as the default review owner.
- `.github/release.yml` for generated GitHub release-note categorization.
- Immutable GitHub Actions SHA-pinning validator and tests.
- Contributor/CI environment consistency validator and tests.
- Public repository boundary validator and tests.
- Generated `docs/POLICY_STATUS.md` plus freshness validation.
- Exact `companion-vYYYY.MM.DD.N` tag-preflight validator and tests.
- Public-resource manifest verifier with path, byte-size, SHA-256, duplicate, and excluded-format checks plus tests.
- Deterministic generated `docs/RELEASE_READINESS.md` with repository-policy, tag, manifest, tagged-workflow, and release-candidate workflow gates.
- Manual `.github/workflows/release-candidate.yml` workflow for pre-tag tests, health checks, readiness checks, manifest generation/verification, and candidate evidence upload.
- Release-candidate guide, manifest-review guide, and Dependabot review procedure.

### Improved

- Upgraded `actions/checkout` from v4 to release v7.0.1 and pinned it to full SHA `3d3c42e5aac5ba805825da76410c181273ba90b1`.
- Upgraded `actions/setup-python` from v5 to release v7.0.0 and pinned it to full SHA `5fda3b95a4ea91299a34e894583c3862153e4b97`.
- Added `actions/upload-artifact` release v7.0.1 to tagged-release manifest generation, pinned to full SHA `043fb46d1a93c77aae656e7c1c64a875d1fc6a0a`.
- Strengthened dataset contracts with duplicate-ID, approved categorical-value, and integer-range validation.
- Synchronized `CITATION.cff` with the active companion release and added citation-version checking.
- Updated documentation index, README, tool catalog, test catalog, tagged-release guide, manifest guide, release checklist, release snapshot, and dependency/action review documentation.
- Added learning-index, generated-data-dictionary, documentation-TOC, repository-policy, policy-status, and release-readiness checks to GitHub Actions and the consolidated repository-health command.
- CI now installs the same pinned `requirements-dev.txt` used by contributors.
- CI now verifies the generated smoke-test public-resource manifest instead of only generating it.
- Tagged-release runs now validate the pushed tag against `COMPANION_RELEASE.json` and verify the generated manifest before artifact upload.
- The generated readiness gate now validates both tagged-release and manual release-candidate workflow configuration.
- Gumroad presence enforcement now includes all newly added public release-operation docs plus all 20 learning-stage pages.
- Consolidated duplicate GitHub About/settings guidance into the canonical `docs/REPOSITORY_METADATA.md`.
- Simplified Dependabot configuration so it does not depend on custom repository labels.
- Added direct public-repository enforcement for required governance/community files, commercial publication/archive exclusion, and direct X/Twitter URL exclusion.
- Removed literal disallowed social-URL fixtures from the policy validator/tests so the repository can enforce the no-direct-X/Twitter-URL rule without self-matching.
- Confirmed GitHub code search returned no stored direct X/Twitter URL matches after the policy fixture cleanup.
- Confirmed the live repository had no open issues or pull requests during this maintenance pass.

### Fixed

- Fixed `tools/manifest_verify.py` so direct CLI execution (`python tools/manifest_verify.py ...`) reliably resolves the repository package path as well as module-based unit tests.

### Policy and release automation

Release `2026.08.18.6` enforces deterministic local checks for:

- full-SHA external GitHub Actions references;
- Python/development-environment consistency;
- public repository governance/publication boundaries;
- Parts 1–200 learning-index integrity;
- release/citation version consistency;
- generated data-dictionary freshness;
- generated documentation-TOC freshness;
- Gumroad storefront presence;
- generated repository policy-status freshness;
- generated release-readiness freshness;
- exact companion tag naming;
- public-resource manifest completeness and SHA-256 integrity;
- tagged-release and manual release-candidate workflow configuration;
- synthetic dataset quality/contracts/sensitivity;
- Markdown accessibility and relative links.

The generated release-readiness result for that snapshot was **READY** for `companion-v2026.08.18.6`. Repository About/topics writes remain manual where the connected maintenance API does not expose those operations.

### Storefront and publication boundary

- Gumroad remains the official publication storefront: **https://ramsandesh.gumroad.com**.
- X/Twitter links remain intentionally omitted and direct X/Twitter URLs are policy-checked.
- No author avatar/photo/person image is used.
- Commercial master DOCX/PDF/EPUB/store-delivery files remain outside the public repository.

## 2026-08-18 — Companion release 2026.08.18.5

### Added

- Release-version consistency checker and tests.
- Gumroad storefront badge/direct link on all 20 detailed learning-stage pages covering Parts 1–200.
- Release metadata indicating learning-stage storefront coverage.

### Improved

- Synchronized `COMPANION_RELEASE.json`, `CHANGELOG.md`, and `docs/RELEASE_SNAPSHOT.md` around release `2026.08.18.5`.
- Expanded release validation expectations to include version consistency and learning-stage storefront presence.
- Continued the repository maintenance phase with granular, reviewable commits.

### Storefront

The official publication storefront remains **https://ramsandesh.gumroad.com** and is intentionally preferred over temporary URL shorteners or social-profile links.

### Publication and privacy boundary

- The commercial manuscript/PDF/EPUB/store-delivery files remain outside this public repository.
- X/Twitter links remain omitted.
- No author avatar/photo/person image is used for publication-resource promotion.

## 2026-08-18 — Gumroad visibility and release-integrity completion

### Added

- Central documentation index at `docs/INDEX.md`.
- Consolidated local repository-health command at `tools/repo_health.py` with tests.
- Public-resource SHA-256 manifest generator at `tools/resource_manifest.py` with tests.
- Synthetic-data sensitivity linter at `tools/synthetic_safety.py` with tests.
- Gumroad storefront-presence validator at `tools/gumroad_presence.py` with tests.
- CLI smoke tests covering every current local tool.
- Companion release snapshot checklist at `docs/RELEASE_SNAPSHOT.md`.

### Improved

- Enforced the exact direct storefront URL `https://ramsandesh.gumroad.com` in release metadata and core public-facing repository documentation.
- Highlighted Gumroad with a reusable Shields badge using the Gumroad logo on major reader-facing pages.
- Expanded README, tools, tests, documentation index, release checklist, structure guide, accessibility guide, errata process, usage guide, and resource style guidance.
- Added sensitive-looking-value and Gumroad-presence checks to the consolidated repository health command.
- Added JSON metadata, synthetic-data safety, storefront presence, manifest smoke generation, and consolidated repository-health steps to CI.
- Completed the release-integrity/discoverability roadmap phase and opened a future-maintenance phase.
- Bumped companion release metadata to `2026.08.18.4`.

### Publication and privacy boundary

- The paid master manuscript and commercial PDF/EPUB/store-delivery files remain outside the public repository.
- The public repository continues to omit X/Twitter links.
- No author avatar/photo/person image is used for the publication-resource design or Gumroad promotion.

## 2026-08-18 — Maintenance, storefront, and release-integrity expansion

### Added

- Dedicated Gumroad storefront/badge guidance at `docs/GUMROAD.md`.
- Official Gumroad storefront metadata in `COMPANION_RELEASE.json`.
- JSON metadata validator and unit tests.
- Offline dataset-summary utility and tests.
- Fictional tabletop packs for privacy, SaaS, endpoint, and workforce governance.
- Worked contributor example for adding a synthetic dataset plus contract.
- Release-notes automation guidance.
- Annual edition maintenance checklist.
- Dependency and GitHub Actions review log.

### Improved

- Highlighted the direct Gumroad storefront across major public-facing repository pages and directory indexes.
- Expanded offline-analysis documentation to cover dataset summaries.
- Expanded tools, tests, schemas, datasets, resources, exercises, support, contribution, security, errata, and learning-index documentation.
- Completed the third repository roadmap phase and opened a release-integrity/discoverability phase.
- Added CI validation for release/schema JSON metadata.

### Publication boundary

The paid master manuscript, complete commercial PDF/EPUB, cover, certificate, and store-delivery files remain outside this public repository. The repository continues to omit X/Twitter links and author avatar/photo/person imagery.

## 2026-08-18 — Companion quality expansion

### Added

- Detailed 20-stage learning index covering exact titles for Parts 1–200.
- Seven additional fictional datasets for cloud, privacy, endpoint, SaaS, resilience, governance, and workforce exercises.
- Markdown accessibility checker, tests, authoring guide, and CI enforcement.
- Relative Markdown link checker, tests, and CI enforcement.
- Offline control-review helper with unit tests.
- Offline CSV structure-quality checker with unit tests.
- Machine-readable dataset contracts, contract validator, tests, and CI enforcement.
- Offline analysis example guide.
- Public book errata log, correction process, submission template, and GitHub issue template.
- Machine-readable companion release metadata.
- Contributor resource style guide.
- Public companion release checklist.
- Fictional tabletop packs for resilience, governance, and incident coordination.
- Test coverage reporting in GitHub Actions.

### Improved

- README navigation and quick-start commands.
- Synthetic dataset catalog.
- Repository roadmap now separates completed release/quality phases from future work.

### Publication boundary

The paid master manuscript, complete commercial PDF/EPUB, cover, certificate, and store assets remain outside this public repository. X/Twitter links remain omitted, and no author avatar/photo/person image is used.

## 2026-08-18 — Initial companion repository build

### Added

- Repository overview and publication-rights boundary.
- Responsible-use, contribution, support, and community policies.
- Repository hygiene files.
- Authorization, lab-safety, finding, evidence, control-validation, incident, risk, and recovery templates.
- Synthetic asset, control-evidence, and risk-signal datasets.
- Offline-only Python helpers for risk prioritization and evidence freshness.
- Unit tests and GitHub Actions CI.
- Usage guide and repository roadmap.

### Publication boundary

The paid master manuscript, complete commercial PDF/EPUB, cover, and store assets are not published in this public repository.
