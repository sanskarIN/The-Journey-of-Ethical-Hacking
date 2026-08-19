# Companion Resource Release Checklist

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

Use this checklist before publishing a new public companion-resource snapshot.

## Content boundary

- [ ] Paid master DOCX/PDF/EPUB is not present.
- [ ] Commercial cover/store-delivery assets are not present unless intentionally relicensed.
- [ ] X/Twitter links remain omitted.
- [ ] No author avatar/photo/person image has been introduced.
- [ ] No credentials, secrets, tokens, private personal data, or confidential third-party data is present.
- [ ] Public practical material remains defensive, authorized, fictional/offline where appropriate.

## Companion projects

- [ ] `python -m compileall -q tools tests companion-projects` passes.
- [ ] `python companion-projects/run_tests.py` passes all project-owned tests.
- [ ] `python tools/companion_projects_check.py --root .` reports at least 20 valid projects.
- [ ] `companion-projects/README.md` catalog matches the project directories.
- [ ] `companion-projects/PROJECT_MATRIX.md` has one offline/tested row per project.
- [ ] Every project keeps its README, implementation, and unit tests.
- [ ] `companion-projects/CLI_CONTRACT.md` and `companion-projects/TESTING.md` remain current.
- [ ] Current companion projects perform no network access or live-target discovery.

## Learning resources

- [ ] `python tools/learning_index_check.py --root .` passes.
- [ ] Part/stage indexes reflect the maintained 200-part series exactly once.
- [ ] Part 200 remains the formal series completion.
- [ ] All 20 stage pages retain the official Gumroad link/badge.
- [ ] Safety boundaries remain visible in practical resources.

## Datasets

- [ ] `python tools/csv_quality.py datasets/*.csv` passes.
- [ ] `python tools/dataset_contracts.py schemas/dataset_contracts.json datasets` passes.
- [ ] `python tools/data_dictionary.py schemas/dataset_contracts.json --output docs/DATA_DICTIONARY.md --check` passes.
- [ ] `python tools/synthetic_safety.py datasets/*.csv` passes.
- [ ] `python tools/dataset_summary.py datasets/*.csv` produces expected summaries.
- [ ] New datasets use fictional identifiers and have contracts.

## Documentation and metadata

- [ ] `python tools/json_metadata.py COMPANION_RELEASE.json schemas/dataset_contracts.json` passes.
- [ ] `COMPANION_RELEASE.json` records `companion_projects: 20` and `companion_projects_offline: true`.
- [ ] `python tools/release_consistency.py --root .` passes.
- [ ] `python tools/docs_toc.py --docs-dir docs --output docs/TOC.md --check` passes.
- [ ] `python tools/doc_accessibility.py README.md docs resources schemas exercises examples companion-projects` passes.
- [ ] `python tools/markdown_links.py README.md docs resources schemas exercises examples companion-projects ERRATA.md ROADMAP.md CHANGELOG.md what_changed.md` passes.
- [ ] `python tools/gumroad_presence.py --root .` passes.
- [ ] README and `docs/INDEX.md` navigation are current.
- [ ] Errata process and correction log are current.
- [ ] Official Gumroad URL is exactly `https://ramsandesh.gumroad.com`.

## Repository policy and code quality

- [ ] `python -m pytest --cov=tools --cov-report=term-missing -q` passes.
- [ ] CLI smoke tests cover every public local tool and every companion-project CLI.
- [ ] `python tools/action_pinning.py --root .` passes.
- [ ] `python tools/dev_environment.py --root .` passes.
- [ ] `python tools/public_repo_policy.py --root .` passes.
- [ ] `python tools/policy_status.py --root . --output docs/POLICY_STATUS.md --check` passes.
- [ ] `python tools/repo_health.py --root .` passes.
- [ ] New utilities are local/offline and dependency-light.
- [ ] New behavior has unit tests.

## Release candidate and tag preflight

- [ ] Current candidate is `2026.08.19.1`.
- [ ] `python tools/release_readiness.py --root . --output docs/RELEASE_READINESS.md --check` passes and reports **READY**.
- [ ] `python tools/tag_preflight.py --root . --tag companion-v2026.08.19.1` passes for the intended tag.
- [ ] The reviewed snapshot is frozen on `release/companion-v2026.08.19.1` before tagging.
- [ ] The earlier `release/companion-v2026.08.18.6` branch remains unchanged as historical evidence.
- [ ] The manual **Companion Release Candidate** GitHub Actions workflow passes if used.
- [ ] `docs/RELEASE_CANDIDATE.md` reflects the intended candidate.

## Manifest integrity

- [ ] `python tools/resource_manifest.py --root . --output PUBLIC_RESOURCE_MANIFEST.json` generates a reviewable manifest.
- [ ] `python tools/manifest_verify.py --root . PUBLIC_RESOURCE_MANIFEST.json` passes.
- [ ] `docs/MANIFEST_REVIEW.md` review points are completed for the tagged artifact.
- [ ] The tagged-release workflow verifies the manifest before artifact upload.

## Release metadata and records

- [ ] `COMPANION_RELEASE.json` version is correct.
- [ ] `CHANGELOG.md` describes notable changes.
- [ ] `what_changed.md` records the detailed work.
- [ ] `ROADMAP.md` reflects completed and next tasks.
- [ ] `docs/RELEASE_SNAPSHOT.md` reflects the intended release gate.
- [ ] `CITATION.cff` matches the companion release version and release date.
- [ ] Candidate, readiness, branch, snapshot, and expected-tag documentation are consistent.

## GitHub repository settings

- [ ] Apply the documented About description when the settings UI/API is available.
- [ ] Set the repository website to `https://ramsandesh.gumroad.com`.
- [ ] Apply the recommended topics from `REPOSITORY_METADATA.md`.
- [ ] Keep X/Twitter omitted from the About website/profile metadata.

## Git history

- [ ] Commits are atomic and meaningful.
- [ ] Local command-line commits/tags use the intended Git identity configuration.
- [ ] No generated commercial publication files are accidentally tracked.

For the complete publication and current listings, use **https://ramsandesh.gumroad.com**.
