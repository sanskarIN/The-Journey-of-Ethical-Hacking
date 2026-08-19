# Repository Roadmap

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

## 2026 companion release — completed

- [x] Establish licensing and commercial-book rights boundary.
- [x] Add responsible-use, contribution, support, and conduct policies.
- [x] Add synthetic datasets and offline-only utilities.
- [x] Add defensive templates for authorization, findings, evidence, validation, incident observation, risk, and recovery.
- [x] Add CI tests for the offline utilities.
- [x] Expand the safe learning index for all 200 parts.
- [x] Add synthetic datasets for governance, resilience, privacy, cloud, endpoint, SaaS, and workforce-security exercises.
- [x] Add accessibility checks for documentation.
- [x] Add more unit tests and examples for defensive data-analysis utilities.
- [x] Add an errata workflow for future book corrections.

## Repository quality phase — completed

- [x] Add machine-readable schemas for the synthetic datasets.
- [x] Add coverage reporting for the local Python utilities.
- [x] Add release-version metadata for companion-resource snapshots.
- [x] Add fictional tabletop exercise packs for resilience, governance, and incident coordination.
- [x] Add contributor-facing style guidance for datasets and templates.
- [x] Add automated checks for broken relative Markdown links.
- [x] Add a public release checklist for companion-resource versions.

## Maintenance and contributor phase — completed

- [x] Add JSON-format validation for release/schema metadata.
- [x] Add a small offline dataset-summary utility and tests.
- [x] Add tabletop packs for privacy, SaaS, endpoint, and workforce governance.
- [x] Add a contributor example showing how to add a new synthetic dataset plus contract.
- [x] Add repository release-notes automation guidance.
- [x] Add a maintenance checklist for annual edition refreshes.
- [x] Review dependency/action versions periodically and document upgrade decisions.
- [x] Promote the official Gumroad storefront throughout major public-facing repository documentation.

## Release integrity and discoverability phase — completed

- [x] Add a central documentation index for repository guides and resources.
- [x] Add one repository-health command that runs local structural checks from a single entry point.
- [x] Add a machine-readable public-resource manifest generator and tests.
- [x] Add a synthetic-data privacy/sensitivity linter for accidental email, token-like, URL-like, or IP-like values.
- [x] Add CLI smoke tests for every local tool.
- [x] Add a Gumroad-presence checker for public-facing Markdown and release metadata.
- [x] Add a release snapshot checklist that records validation expectations and companion version context.
- [x] Integrate release-integrity checks into GitHub Actions CI.

## Future maintenance phase — completed in release 2026.08.18.6

- [x] Generate and review a public-resource manifest for tagged companion releases through an automated workflow.
- [x] Add release-version consistency checks across `COMPANION_RELEASE.json`, changelog entries, release snapshots, and `CITATION.cff`.
- [x] Add richer dataset contract constraints for approved categorical values, integer ranges, and duplicate identifiers.
- [x] Add a documentation table-of-contents generator for larger guide sets.
- [x] Add a contributor onboarding checklist for first-time pull requests.
- [x] Add issue-triage guidance for errata, documentation, datasets, tests, and release maintenance.
- [x] Review GitHub repository metadata/topics and document recommended settings; the connected maintenance API still cannot write repository About/topics settings directly.
- [x] Review current GitHub Actions majors against official upstream releases and upgrade CI/release workflows to v7 lines.
- [x] Add monthly Dependabot checks for GitHub Actions.
- [x] Add GitHub-native citation metadata, funding/storefront link, and issue-chooser storefront visibility.
- [x] Add automated Parts 1–200 learning-index integrity validation.

## Long-term repository quality phase — completed

- [x] Add a generated dataset data dictionary from `schemas/dataset_contracts.json`.
- [x] Add automated freshness validation for `docs/TOC.md`.
- [x] Add dedicated issue forms for dataset improvements and tool/test bugs.
- [x] Add a contributor-facing development environment for repeatable local test setup.
- [x] Add a GitHub release-note category configuration for companion releases.
- [x] Add CODEOWNERS/review boundaries for `@sanskarIN`.
- [x] Evaluate and apply full-length SHA pinning for external GitHub Actions while preserving Dependabot maintenance.
- [x] Record maintenance evidence in the current companion release snapshot.
- [x] Add automated freshness validation for the generated dataset data dictionary.

## Repository policy automation phase — completed

- [x] Add a local validator that enforces full-length SHA pinning for external GitHub Actions.
- [x] Add a validator for `.python-version`, workflow Python versions, and pinned dev dependency consistency.
- [x] Add tests for repository-policy validators and wire them into CI/repository health.
- [x] Add a generated repository policy/status summary for release review.
- [x] Add validation that required GitHub community/governance files remain present.
- [x] Add a public-repository boundary check that rejects commercial publication/archive formats.
- [x] Add a direct X/Twitter URL exclusion check without storing disallowed URL literals in policy/test source files.
- [x] Add release-snapshot evidence for the repository policy automation results.
- [x] Enforce generated policy-status freshness in CI and the consolidated health command.

## Pre-tag release hardening phase — completed

- [x] Add exact `companion-vYYYY.MM.DD.N` tag preflight validation and tests.
- [x] Add public-resource manifest verification for path coverage, byte sizes, SHA-256 hashes, duplicates, and excluded commercial formats.
- [x] Add deterministic generated release-readiness reporting and freshness enforcement.
- [x] Validate both the tagged-release workflow and manual release-candidate workflow in the readiness gate.
- [x] Add a manual GitHub Actions release-candidate workflow that uploads pre-tag evidence without creating a tag.
- [x] Validate pushed companion tags against `COMPANION_RELEASE.json` before tagged manifest generation.
- [x] Verify tagged manifests before artifact upload.
- [x] Verify smoke-test manifests and release-readiness freshness in normal CI.
- [x] Add release-candidate, manifest-review, Dependabot-review, and consolidated repository metadata guidance.
- [x] Surface the release-readiness/manifest workflow in README, docs index, release checklist, tagged-release guide, and release snapshot.
- [x] Enforce Gumroad storefront presence across the newly added public release-operation documentation.
- [x] Keep the generated documentation TOC current after the release-operation documentation expansion.
- [x] Record a generated `READY` verdict for `companion-v2026.08.18.6`.

## Defensive companion projects phase — completed 2026-08-19

- [x] Add a dedicated `companion-projects/` suite with 20 offline, authorization-first defensive mini-projects.
- [x] Give every project its own README, focused Python implementation, and deterministic unit tests.
- [x] Add suite architecture, engineering standard, safety boundary, threat model, synthetic-data guidance, contribution guidance, roadmap, changelog, and maintenance checklist.
- [x] Add a centralized runner for all project-owned tests.
- [x] Add a repository-level structure validator that enforces required suite files, a 20-project floor, per-project README files, implementations, and tests.
- [x] Wire companion tests and structure validation into GitHub Actions CI.
- [x] Include the companion suite in repository-health accessibility and relative-link checks.
- [x] Add companion-project navigation to the root README, docs index, tools catalog, and tests catalog.
- [x] Require timezone-aware timestamps in the incident timeline utility.
- [x] Reject empty approved-role policies in the access-review utility.
- [x] Ignore symbolic links in recursive integrity, evidence-inventory, and backup-verification walks.
- [x] Add control/evidence mapping, exception-register validation, patch-register reporting, and recovery-exercise reporting as the 17th–20th projects.
- [x] Keep the complete companion suite local/offline with explicit input paths and synthetic/authorized data.

## Remaining manual and recurring release operations

- [ ] Create the first `companion-v2026.08.18.6` tag when the release snapshot is intentionally ready to freeze.
- [ ] Review the generated manifest artifact from the tagged-release workflow after the first tag.
- [ ] Apply the documented GitHub About description, Gumroad website, and recommended topics manually if repository-settings API support remains unavailable.
- [ ] Review future Dependabot PRs for Actions and pip updates before merging.
- [ ] Record future errata and edition-refresh changes without publishing paid manuscript text.
- [ ] Re-run the complete policy/test/release gate before every tagged companion release.

The public repository will continue to exclude the paid master manuscript and commercial publication files.

For the complete publication and current listings, use **https://ramsandesh.gumroad.com**.
