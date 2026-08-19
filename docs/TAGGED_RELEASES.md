# Tagged Companion Releases

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This guide explains the public companion-resource tag workflow. It applies only to the open repository resources; the commercial manuscript and store-delivery files remain outside GitHub.

## Tag format

Use:

```text
companion-vYYYY.MM.DD.N
```

For the current `main` candidate, the matching tag is:

```text
companion-v2026.08.19.1
```

Freeze the reviewed candidate first on:

```text
release/companion-v2026.08.19.1
```

The older `release/companion-v2026.08.18.6` branch belongs to the earlier frozen snapshot and should remain unchanged.

The active version must match `COMPANION_RELEASE.json`, `CHANGELOG.md`, `docs/RELEASE_SNAPSHOT.md`, `docs/RELEASE_CANDIDATE.md`, `docs/RELEASE_READINESS.md`, `docs/RELEASE_BRANCH.md`, and `CITATION.cff` before the tag is pushed.

## Before tagging

Run:

```bash
python -m pip install -r requirements-dev.txt
python -m compileall -q tools tests companion-projects
python -m pytest --cov=tools --cov-report=term-missing -q
python companion-projects/run_tests.py
python tools/companion_projects_check.py --root .
python tools/repo_health.py --root .
python tools/policy_status.py --root . --output docs/POLICY_STATUS.md --check
python tools/release_readiness.py --root . --output docs/RELEASE_READINESS.md --check
python tools/tag_preflight.py --root . --tag companion-v2026.08.19.1
```

The generated readiness report should show **READY** before tagging.

You can also run the manual **Companion Release Candidate** workflow in GitHub Actions. It compiles Python, runs the main pytest/coverage/CLI-smoke suite, runs all project-owned companion tests, validates the 20-project structure, runs repository health/readiness checks, generates and verifies the public manifest, and uploads a candidate evidence bundle without creating a tag.

Then verify:

- `COMPANION_RELEASE.json` records `companion_projects: 20` and `companion_projects_offline: true`;
- the official Gumroad storefront is `https://ramsandesh.gumroad.com`;
- X/Twitter links remain omitted;
- no author avatar/photo/person image was introduced;
- no commercial PDF/EPUB/DOCX/store-delivery archive is public;
- synthetic datasets contain no real sensitive data;
- Parts 1–200 appear exactly once in the learning-stage index;
- the project README catalog and matrix match the 20 current project directories;
- the changelog, snapshot, candidate, readiness, branch guide, citation metadata, and companion metadata describe the intended version.

## Create and push a tag locally

After checking out the reviewed release branch:

```bash
git fetch origin
git checkout release/companion-v2026.08.19.1
git pull --ff-only
git tag -a companion-v2026.08.19.1 -m "Companion release 2026.08.19.1"
git push origin companion-v2026.08.19.1
```

Use the requested local Git identity before creating command-line commits or tags:

```bash
git config user.email "sanskarin@outlook.in"
```

## Automatic manifest artifact

Pushing a `companion-v*` tag triggers `.github/workflows/release-manifest.yml`.

That workflow:

1. checks out the tagged repository;
2. sets up Python 3.12 and installs the pinned development dependencies;
3. compiles all repository Python sources;
4. runs the main pytest/coverage/CLI-smoke suite;
5. runs all project-owned companion tests;
6. validates the 20-project suite structure;
7. validates the pushed tag against `COMPANION_RELEASE.json`;
8. runs repository health checks;
9. validates complete release-version consistency;
10. generates `PUBLIC_RESOURCE_MANIFEST.json` with SHA-256 hashes for public resources;
11. verifies the manifest against the tagged repository snapshot;
12. uploads the verified manifest as a GitHub Actions artifact for release review.

The manifest intentionally excludes `.pdf`, `.epub`, `.docx`, and `.zip` publication formats.

## Review after tagging

- Download the manifest artifact from the workflow run.
- Confirm the workflow completed successfully.
- Run `python tools/manifest_verify.py --root . PUBLIC_RESOURCE_MANIFEST.json` against the same tag checkout.
- Follow `MANIFEST_REVIEW.md` for the manual review points.
- Retain the artifact with the release record if useful.
- Publish companion release notes without attaching paid book files.

## Explicit final operations

The automated repository tools generate and validate the expected tag but do not create the Git tag or change repository About/topics settings. Those final operations remain explicit release actions after the reviewed release branch is frozen.

For current publication listings and purchasing, use **https://ramsandesh.gumroad.com**.
