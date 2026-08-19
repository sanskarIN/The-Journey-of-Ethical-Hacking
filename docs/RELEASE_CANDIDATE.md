# Companion Release Candidate — 2026.08.18.6

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This document records the repository-side candidate for the first tagged companion release.

## Candidate identity

- Companion version: `2026.08.18.6`
- Intended tag: `companion-v2026.08.18.6`
- Series coverage: Parts 1–200
- Public scope: defensive companion resources only
- Commercial book files in repository: no
- Author avatar/photo/person image: no
- X/Twitter link: intentionally omitted

## Automated pre-tag gate

Run:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest --cov=tools --cov-report=term-missing -q
python tools/repo_health.py --root .
python tools/policy_status.py --root . --output docs/POLICY_STATUS.md --check
python tools/release_readiness.py --root . --output docs/RELEASE_READINESS.md --check
python tools/tag_preflight.py --root . --tag companion-v2026.08.18.6
```

The candidate should not be tagged unless every command succeeds.

## Tag operation

The connected maintenance API used for repository automation does not expose Git tag creation. When the candidate is intentionally frozen, create the tag from the intended `main` commit using GitHub or local Git.

Example local Git flow:

```bash
git fetch origin
git checkout main
git pull --ff-only
git tag -a companion-v2026.08.18.6 -m "Companion release 2026.08.18.6"
git push origin companion-v2026.08.18.6
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
