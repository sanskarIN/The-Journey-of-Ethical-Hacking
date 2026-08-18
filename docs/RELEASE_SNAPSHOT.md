# Companion Release Snapshot

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This file records the repository-side validation expectations for the current public companion-resource snapshot.

## Snapshot identity

- Project: **The Journey of Ethical Hacking — Companion Resources**
- Edition: **2026 Edition**
- Companion release: **2026.08.18.5**
- Series coverage: **Parts 1–200**
- Gumroad highlighted in all 20 learning-stage pages: **Yes**
- Public companion release metadata: `COMPANION_RELEASE.json`
- Code/resource license boundary: Apache-2.0 where the repository license applies
- Commercial book rights: Copyright © 2026 Ram Sandesh. All rights reserved.
- Commercial manuscript in public repository: **No**
- Author avatar/photo/person image used: **No**
- X/Twitter link included: **No**
- Official publication storefront: **https://ramsandesh.gumroad.com**

## Validation gate

Before a companion release/tag, run:

```bash
python -m pytest --cov=tools --cov-report=term-missing -q
python tools/repo_health.py --root .
python tools/release_consistency.py --root .
python tools/resource_manifest.py --root . --output PUBLIC_RESOURCE_MANIFEST.json
```

The consolidated health command covers:

- synthetic CSV structural quality;
- dataset contract validation;
- release/schema JSON validation;
- release-version consistency;
- synthetic-data sensitivity checks;
- Markdown accessibility basics;
- relative Markdown links;
- official Gumroad storefront presence.

## Manual release checks

- [ ] Review `CHANGELOG.md`.
- [ ] Review `what_changed.md`.
- [ ] Review `ROADMAP.md`.
- [ ] Confirm `COMPANION_RELEASE.json` has the intended version.
- [ ] Confirm `CHANGELOG.md` and this snapshot mention the same companion-release version.
- [ ] Confirm `https://ramsandesh.gumroad.com` is the direct storefront URL.
- [ ] Confirm all 20 learning-stage pages retain the Gumroad badge/direct URL.
- [ ] Confirm X/Twitter remains omitted.
- [ ] Confirm no author avatar/photo/person image was introduced.
- [ ] Confirm no commercial manuscript/PDF/EPUB/store-delivery file is committed publicly.
- [ ] Confirm synthetic datasets contain no secrets, personal data, real target details, or sensitive-looking values.
- [ ] Confirm release notes describe companion resources only.

## Manifest note

`PUBLIC_RESOURCE_MANIFEST.json` may be generated for a release snapshot using `tools/resource_manifest.py`. The generator excludes commercial publication formats (`.pdf`, `.epub`, `.docx`, `.zip`) by design.

**Publication storefront:** https://ramsandesh.gumroad.com
