# Companion Release Branch

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

The current companion candidate is release `2026.08.19.1` with expected tag `companion-v2026.08.19.1`.

## Current candidate branch policy

Before creating the final tag, preserve the reviewed candidate snapshot on:

```text
release/companion-v2026.08.19.1
```

The final `companion-v2026.08.19.1` tag should point to that intentionally reviewed release commit rather than an unrelated later `main` commit.

## Previous frozen candidate

The existing branch:

```text
release/companion-v2026.08.18.6
```

belongs to the earlier `2026.08.18.6` / `companion-v2026.08.18.6` pre-expansion snapshot. Keep it immutable as historical release evidence; do not move it to the 20-project state.

## Verification

On the current release branch, run the full gate:

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
python tools/resource_manifest.py --root . --output PUBLIC_RESOURCE_MANIFEST.json
python tools/manifest_verify.py --root . PUBLIC_RESOURCE_MANIFEST.json
```

Only after the release branch/snapshot is intentionally accepted should the final tag be created.

## Publication boundary

The branch is for public defensive companion resources only. Commercial master DOCX/PDF/EPUB, cover/store packages, X/Twitter links, and author avatar/photo/person imagery remain outside the public release path.

**Publication storefront:** https://ramsandesh.gumroad.com
