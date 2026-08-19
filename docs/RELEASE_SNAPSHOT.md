# Companion Release Snapshot

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This file records the repository-side validation expectations for the current public companion-resource snapshot.

## Snapshot identity

- Project: **The Journey of Ethical Hacking — Companion Resources**
- Edition: **2026 Edition**
- Companion release: **2026.08.19.1**
- Previous companion release/candidate: **2026.08.18.6**
- Intended tag: **`companion-v2026.08.19.1`**
- Previous frozen tag target: **`companion-v2026.08.18.6`**
- Companion projects: **20**
- Current companion projects offline/local: **Yes**
- Series coverage: **Parts 1–200**
- Gumroad highlighted in all 20 learning-stage pages: **Yes**
- Public companion release metadata: `COMPANION_RELEASE.json`
- Code/resource license boundary: Apache-2.0 where the repository license applies
- Commercial book rights: Copyright © 2026 Ram Sandesh. All rights reserved.
- Commercial manuscript in public repository: **No**
- Author avatar/photo/person image used: **No**
- X/Twitter link included: **No**
- Official publication storefront: **https://ramsandesh.gumroad.com**

## Contributor and CI environment

- Python baseline: **3.12** via `.python-version`.
- Pinned development dependencies: `requirements-dev.txt`.
- CI compiles all Python sources before running tests.
- CI installs the same pinned development requirements used locally.
- The main pytest suite smoke-tests every discovered repository and companion-project CLI.
- The project-owned test runner executes all 20 companion-project test files.
- Dependabot checks both GitHub Actions and pip dependencies monthly.

## Repository policy automation evidence

The current release includes deterministic local validators for:

- Python source compilation (`python -m compileall -q tools tests companion-projects`);
- immutable full-SHA external GitHub Actions references (`tools/action_pinning.py`);
- local/CI Python and exact development dependency consistency (`tools/dev_environment.py`);
- required community/governance files, commercial publication-file exclusion, and direct X/Twitter URL exclusion (`tools/public_repo_policy.py`);
- 20-project suite structure, catalog, project matrix, required documentation, implementations, and tests (`tools/companion_projects_check.py`);
- release/citation/candidate/readiness/branch version consistency (`tools/release_consistency.py`);
- exact Parts 1–200 learning-stage coverage (`tools/learning_index_check.py`);
- generated data dictionary freshness (`tools/data_dictionary.py --check`);
- generated docs TOC freshness (`tools/docs_toc.py --check`);
- official Gumroad storefront presence (`tools/gumroad_presence.py`);
- generated repository policy summary freshness (`tools/policy_status.py --check`);
- expected companion tag naming (`tools/tag_preflight.py`);
- generated manifest content/hash integrity (`tools/manifest_verify.py`);
- generated pre-tag release readiness (`tools/release_readiness.py --check`).

`docs/POLICY_STATUS.md` provides the generated reviewer-facing policy summary. `docs/RELEASE_READINESS.md` provides the deterministic pre-tag verdict.

## Validation gate

Before a companion release/tag, run:

```bash
python -m pip install -r requirements-dev.txt
python -m compileall -q tools tests companion-projects
python -m pytest --cov=tools --cov-report=term-missing -q
python companion-projects/run_tests.py
python tools/companion_projects_check.py --root .
python tools/repo_health.py --root .
python tools/policy_status.py --root . --output docs/POLICY_STATUS.md --check
python tools/release_readiness.py --root . --output docs/RELEASE_READINESS.md --check
python tools/release_consistency.py --root .
python tools/tag_preflight.py --root . --tag companion-v2026.08.19.1
python tools/learning_index_check.py --root .
python tools/docs_toc.py --docs-dir docs --output docs/TOC.md --check
python tools/data_dictionary.py schemas/dataset_contracts.json --output docs/DATA_DICTIONARY.md --check
python tools/resource_manifest.py --root . --output PUBLIC_RESOURCE_MANIFEST.json
python tools/manifest_verify.py --root . PUBLIC_RESOURCE_MANIFEST.json
```

The consolidated health command covers:

- Python source compilation;
- immutable action references;
- contributor/CI environment consistency;
- public repository publication/governance boundaries;
- 20-project companion-suite structure and documentation consistency;
- synthetic CSV structural quality;
- richer dataset contract validation;
- generated data dictionary freshness;
- release/schema JSON validation;
- complete release/citation/candidate/readiness/branch version consistency;
- Parts 1–200 learning-index integrity;
- documentation TOC freshness;
- synthetic-data sensitivity checks;
- Markdown accessibility basics;
- relative Markdown links;
- official Gumroad storefront presence across core public pages, citation/funding metadata, and all 20 learning stages;
- generated policy-status freshness;
- generated release-readiness freshness.

## GitHub Actions and release automation

External GitHub-maintained actions are pinned to verified full release SHAs:

- `actions/checkout` v7.0.1 → `3d3c42e5aac5ba805825da76410c181273ba90b1`
- `actions/setup-python` v7.0.0 → `5fda3b95a4ea91299a34e894583c3862153e4b97`
- `actions/upload-artifact` v7.0.1 → `043fb46d1a93c77aae656e7c1c64a875d1fc6a0a`

Additional release/maintenance controls:

- `.github/workflows/ci.yml` compiles Python, runs the main tests, runs all companion-project tests, validates the suite, verifies generated release readiness, and verifies a smoke-test public manifest on normal `main`/PR CI.
- `.github/workflows/release-candidate.yml` can be dispatched manually before tagging; it runs tests, repository health, policy/readiness checks, generates and verifies the manifest, then uploads a candidate evidence bundle.
- `.github/workflows/release-manifest.yml` runs for `companion-v*` tags and manual dispatch.
- Tagged runs validate the pushed tag against `COMPANION_RELEASE.json`.
- The tagged workflow generates `PUBLIC_RESOURCE_MANIFEST.json`, verifies every path/size/hash, and uploads the verified artifact.
- `.github/release.yml` configures generated GitHub release notes.
- `.github/CODEOWNERS` identifies `@sanskarIN` as the default review owner.
- Dependabot checks GitHub Actions and pip dependencies monthly.

## Manual release checks

- [ ] Review `CHANGELOG.md`.
- [ ] Review `what_changed.md`.
- [ ] Review `ROADMAP.md`.
- [ ] Confirm `COMPANION_RELEASE.json` has the intended version and `companion_projects: 20`.
- [ ] Confirm `CHANGELOG.md` and this snapshot mention the same companion-release version.
- [ ] Confirm `CITATION.cff` records the intended companion version and release date.
- [ ] Confirm `docs/RELEASE_CANDIDATE.md`, `docs/RELEASE_READINESS.md`, and `docs/RELEASE_BRANCH.md` match the intended release/tag.
- [ ] Confirm `docs/RELEASE_READINESS.md` reports **READY**.
- [ ] Confirm `tools/tag_preflight.py` accepts the intended tag.
- [ ] Confirm `python -m compileall -q tools tests companion-projects` succeeds.
- [ ] Confirm `python companion-projects/run_tests.py` succeeds.
- [ ] Confirm `tools/companion_projects_check.py` reports 20 valid projects.
- [ ] Confirm external actions remain pinned to verified full upstream SHAs.
- [ ] Confirm `.python-version`, workflow Python versions, and `requirements-dev.txt` remain aligned.
- [ ] Confirm `docs/POLICY_STATUS.md`, `docs/TOC.md`, and `docs/DATA_DICTIONARY.md` pass their freshness checks.
- [ ] Confirm `https://ramsandesh.gumroad.com` is the direct storefront URL.
- [ ] Confirm all 20 learning-stage pages retain the Gumroad badge/direct URL.
- [ ] Confirm Parts 1–200 pass `tools/learning_index_check.py`.
- [ ] Confirm direct X/Twitter URLs remain absent.
- [ ] Confirm no author avatar/photo/person image was introduced.
- [ ] Confirm no commercial manuscript/PDF/EPUB/store-delivery file is committed publicly.
- [ ] Confirm synthetic datasets contain no secrets, personal data, real target details, or sensitive-looking values.
- [ ] Confirm release notes describe companion resources only.

## Manifest note

Pushing a `companion-v*` tag automatically generates and verifies the public-resource manifest before uploading it as a GitHub Actions artifact. The generator excludes commercial publication formats (`.pdf`, `.epub`, `.docx`, `.zip`) by design.

See `docs/RELEASE_CANDIDATE.md`, `docs/TAGGED_RELEASES.md`, and `docs/MANIFEST_REVIEW.md` for the pre-tag, tag, and post-tag workflows.

## Remaining manual operations

The previous `release/companion-v2026.08.18.6` branch remains a frozen historical candidate. The current `2026.08.19.1` candidate should be frozen on `release/companion-v2026.08.19.1` before tagging. Repository About/topics settings still require explicit GitHub UI or supported API operations.

**Publication storefront:** https://ramsandesh.gumroad.com
