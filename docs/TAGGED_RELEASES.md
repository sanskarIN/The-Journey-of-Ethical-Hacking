# Tagged Companion Releases

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This guide explains the public companion-resource tag workflow. It applies only to the open repository resources; the commercial manuscript and store-delivery files remain outside GitHub.

## Tag format

Use:

```text
companion-vYYYY.MM.DD.N
```

For the current repository snapshot, the matching tag is:

```text
companion-v2026.08.18.6
```

The version must match `COMPANION_RELEASE.json`, `CHANGELOG.md`, `docs/RELEASE_SNAPSHOT.md`, and `CITATION.cff` before the tag is pushed.

## Before tagging

Run:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest --cov=tools --cov-report=term-missing -q
python tools/repo_health.py --root .
python tools/policy_status.py --root . --output docs/POLICY_STATUS.md --check
python tools/release_readiness.py --root . --output docs/RELEASE_READINESS.md --check
python tools/tag_preflight.py --root . --tag companion-v2026.08.18.6
```

The generated readiness report should show **READY** before tagging.

You can also run the manual **Companion Release Candidate** workflow in GitHub Actions. It runs tests, repository health, readiness checks, manifest generation, manifest verification, and uploads a candidate evidence bundle without creating a tag.

Then verify:

- the official Gumroad storefront is `https://ramsandesh.gumroad.com`;
- X/Twitter links remain omitted;
- no author avatar/photo/person image was introduced;
- no commercial PDF/EPUB/DOCX/store-delivery archive is public;
- synthetic datasets contain no real sensitive data;
- Parts 1–200 appear exactly once in the learning-stage index;
- the changelog, release snapshot, citation metadata, and companion metadata describe the intended version.

## Create and push a tag locally

```bash
git tag -a companion-v2026.08.18.6 -m "Companion release 2026.08.18.6"
git push origin companion-v2026.08.18.6
```

Use the requested local Git identity before creating command-line commits or tags:

```bash
git config user.email "sanskarin@outlook.in"
```

## Automatic manifest artifact

Pushing a `companion-v*` tag triggers `.github/workflows/release-manifest.yml`.

That workflow:

1. checks out the tagged repository;
2. sets up Python 3.12;
3. validates the pushed tag against `COMPANION_RELEASE.json`;
4. runs repository health checks;
5. validates release-version consistency;
6. generates `PUBLIC_RESOURCE_MANIFEST.json` with SHA-256 hashes for public resources;
7. verifies the manifest against the tagged repository snapshot;
8. uploads the verified manifest as a GitHub Actions artifact for release review.

The manifest intentionally excludes `.pdf`, `.epub`, `.docx`, and `.zip` publication formats.

## Review after tagging

- Download the manifest artifact from the workflow run.
- Confirm the workflow completed successfully.
- Run `python tools/manifest_verify.py --root . PUBLIC_RESOURCE_MANIFEST.json` against the same tag checkout.
- Follow `MANIFEST_REVIEW.md` for the manual review points.
- Retain the artifact with the release record if useful.
- Publish companion release notes without attaching paid book files.

## API limitation

The connected repository-maintenance API used for this project does not currently expose Git tag creation or GitHub repository About/topics writes. Those final GitHub operations remain manual; the repository-local release gate is automated and documented.

For current publication listings and purchasing, use **https://ramsandesh.gumroad.com**.
