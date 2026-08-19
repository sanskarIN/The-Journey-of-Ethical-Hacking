# Companion Release Candidate — 2026.08.19.1

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This document records the repository-side candidate for the current tagged companion release.

## Candidate identity

- Companion version: `2026.08.19.1`
- Intended tag: `companion-v2026.08.19.1`
- Previous frozen candidate: `2026.08.18.6` / `companion-v2026.08.18.6`
- Companion projects: **20**, all current projects offline/local
- Series coverage: Parts 1–200
- Public scope: defensive companion resources only
- Commercial book files in repository: no
- Author avatar/photo/person image: no
- X/Twitter link: intentionally omitted

## Automated pre-tag gate

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

The candidate should not be tagged unless every command succeeds.

## Release branch

Freeze the reviewed candidate on:

```text
release/companion-v2026.08.19.1
```

The earlier `release/companion-v2026.08.18.6` branch remains a historical pre-expansion snapshot and should not be moved to the newer `main` state.

## Tag operation

When the candidate is intentionally frozen, create the tag from the reviewed release-branch commit using GitHub or local Git.

Example local Git flow:

```bash
git fetch origin
git checkout release/companion-v2026.08.19.1
git pull --ff-only
git tag -a companion-v2026.08.19.1 -m "Companion release 2026.08.19.1"
git push origin companion-v2026.08.19.1
```

Before using local Git, configure the requested commit/tag identity as documented in `GIT_COMMIT_IDENTITY.md`.

## After the tag

1. Confirm **Companion Release Manifest** completes successfully in GitHub Actions.
2. Download the generated `PUBLIC_RESOURCE_MANIFEST.json` artifact.
3. Verify it locally:

```bash
python tools/manifest_verify.py --root . PUBLIC_RESOURCE_MANIFEST.json
```

4. Review the artifact using `MANIFEST_REVIEW.md`.
5. Use generated GitHub release notes only for the public companion resources; do not attach the paid manuscript, PDF, EPUB, cover package, or store-delivery archives.

## Storefront

The official commercial publication storefront is **https://ramsandesh.gumroad.com**. The public GitHub repository remains the open companion-resource project and does not replace the paid publication storefront.
