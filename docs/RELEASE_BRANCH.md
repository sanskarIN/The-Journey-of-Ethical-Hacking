# Companion Release Branch

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

The first tagged companion release is prepared around release `2026.08.18.6` and expected tag `companion-v2026.08.18.6`.

## Candidate branch policy

Before creating the final tag, use a dedicated release branch to preserve the reviewed candidate snapshot while `main` can continue receiving future work.

Recommended branch:

```text
release/companion-v2026.08.18.6
```

The final tag should point to the intentionally reviewed release commit rather than an unrelated later `main` commit.

## Verification

On the release branch, run the full gate:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest --cov=tools --cov-report=term-missing -q
python tools/repo_health.py --root .
python tools/policy_status.py --root . --output docs/POLICY_STATUS.md --check
python tools/release_readiness.py --root . --output docs/RELEASE_READINESS.md --check
python tools/tag_preflight.py --root . --tag companion-v2026.08.18.6
python tools/resource_manifest.py --root . --output PUBLIC_RESOURCE_MANIFEST.json
python tools/manifest_verify.py --root . PUBLIC_RESOURCE_MANIFEST.json
```

Only after the release branch/snapshot is intentionally accepted should the final tag be created.

## Publication boundary

The branch is for public defensive companion resources only. Commercial master DOCX/PDF/EPUB, cover/store packages, X/Twitter links, and author avatar/photo/person imagery remain outside the public release path.

**Publication storefront:** https://ramsandesh.gumroad.com
