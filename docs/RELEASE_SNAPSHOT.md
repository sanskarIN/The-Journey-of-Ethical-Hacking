# Companion Release Snapshot

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This file records the repository-side validation expectations for the current public companion-resource snapshot.

## Snapshot identity

- Project: **The Journey of Ethical Hacking — Companion Resources**
- Edition: **2026 Edition**
- Companion release: **2026.08.18.6**
- Previous companion release: **2026.08.18.5**
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
- CI installs the same pinned development requirements used locally.
- Dependabot checks both GitHub Actions and pip dependencies monthly.

## Validation gate

Before a companion release/tag, run:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest --cov=tools --cov-report=term-missing -q
python tools/repo_health.py --root .
python tools/release_consistency.py --root .
python tools/learning_index_check.py --root .
python tools/docs_toc.py --docs-dir docs --output docs/TOC.md --check
python tools/resource_manifest.py --root . --output PUBLIC_RESOURCE_MANIFEST.json
```

The consolidated health command covers:

- synthetic CSV structural quality;
- richer dataset contract validation;
- release/schema JSON validation;
- release/citation-version consistency;
- Parts 1–200 learning-index integrity;
- documentation TOC freshness;
- synthetic-data sensitivity checks;
- Markdown accessibility basics;
- relative Markdown links;
- official Gumroad storefront presence across core public pages, citation/funding metadata, and all 20 learning stages.

## GitHub Actions and release automation

External GitHub-maintained actions are pinned to verified full release SHAs:

- `actions/checkout` v7.0.1 → `3d3c42e5aac5ba805825da76410c181273ba90b1`
- `actions/setup-python` v7.0.0 → `5fda3b95a4ea91299a34e894583c3862153e4b97`
- `actions/upload-artifact` v7.0.1 → `043fb46d1a93c77aae656e7c1c64a875d1fc6a0a`

Additional release/maintenance controls:

- `.github/workflows/release-manifest.yml` runs for `companion-v*` tags and manual dispatch.
- The release-manifest workflow runs health/version checks, generates `PUBLIC_RESOURCE_MANIFEST.json`, and uploads it as an artifact.
- `.github/release.yml` configures generated GitHub release notes.
- `.github/CODEOWNERS` identifies `@sanskarIN` as the default review owner.
- Dependabot checks GitHub Actions and pip dependencies monthly.

## Manual release checks

- [ ] Review `CHANGELOG.md`.
- [ ] Review `what_changed.md`.
- [ ] Review `ROADMAP.md`.
- [ ] Confirm `COMPANION_RELEASE.json` has the intended version.
- [ ] Confirm `CHANGELOG.md` and this snapshot mention the same companion-release version.
- [ ] Confirm `CITATION.cff` records the intended companion version.
- [ ] Confirm external actions remain pinned to verified full upstream SHAs.
- [ ] Confirm `https://ramsandesh.gumroad.com` is the direct storefront URL.
- [ ] Confirm all 20 learning-stage pages retain the Gumroad badge/direct URL.
- [ ] Confirm Parts 1–200 pass `tools/learning_index_check.py`.
- [ ] Confirm generated documentation indexes are current.
- [ ] Confirm X/Twitter remains omitted.
- [ ] Confirm no author avatar/photo/person image was introduced.
- [ ] Confirm no commercial manuscript/PDF/EPUB/store-delivery file is committed publicly.
- [ ] Confirm synthetic datasets contain no secrets, personal data, real target details, or sensitive-looking values.
- [ ] Confirm release notes describe companion resources only.

## Manifest note

Pushing a `companion-v*` tag automatically generates the public-resource manifest as a GitHub Actions artifact. The generator excludes commercial publication formats (`.pdf`, `.epub`, `.docx`, `.zip`) by design.

See `docs/TAGGED_RELEASES.md` for the release-tag workflow.

**Publication storefront:** https://ramsandesh.gumroad.com
