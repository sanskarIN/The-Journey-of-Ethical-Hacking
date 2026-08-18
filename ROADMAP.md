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

## Long-term repository quality phase

- [ ] Add a generated dataset data dictionary from `schemas/dataset_contracts.json`.
- [ ] Add automated freshness validation for `docs/TOC.md`.
- [ ] Add dedicated issue forms for dataset improvements and tool/test bugs.
- [ ] Add a contributor-facing development environment file for repeatable local test setup.
- [ ] Add a GitHub release-note category configuration for companion releases.
- [ ] Add CODEOWNERS/review-boundary documentation if repository collaboration expands.
- [ ] Evaluate SHA-pinning policy for third-party/GitHub Actions while preserving maintainability.
- [ ] Add periodic maintenance evidence to each future companion release snapshot.

The public repository will continue to exclude the paid master manuscript and commercial publication files.

For the complete publication and current listings, use **https://ramsandesh.gumroad.com**.
