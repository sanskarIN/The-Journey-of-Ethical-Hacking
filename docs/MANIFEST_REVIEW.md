# Public Resource Manifest Review

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This guide explains how to review the `PUBLIC_RESOURCE_MANIFEST.json` artifact generated for a tagged companion release.

## Automated verification

From the repository root, place the downloaded manifest at `PUBLIC_RESOURCE_MANIFEST.json` and run:

```bash
python tools/manifest_verify.py --root . PUBLIC_RESOURCE_MANIFEST.json
```

The verifier checks:

- manifest format version;
- declared resource count;
- duplicate paths;
- unsafe or parent-traversal paths;
- excluded commercial/archive formats;
- missing or unexpected public files;
- byte-size equality;
- SHA-256 equality for every manifested file.

## Manual review

After automated verification passes, review these points:

- The manifest belongs to the intended `companion-v*` tag.
- No `.pdf`, `.epub`, `.docx`, or `.zip` commercial/store-delivery artifact is listed.
- The manifest contains repository companion resources only.
- `COMPANION_RELEASE.json`, `CITATION.cff`, release snapshot, policy status, and release-readiness files are present where expected.
- Gumroad promotion points to **https://ramsandesh.gumroad.com**.
- No author avatar/photo/person image has been introduced for storefront promotion.
- Direct X/Twitter links remain absent.

## Retention

The release workflow currently uploads the manifest artifact with a 90-day retention period. Download and retain a reviewed copy with the private publication/release records if a longer audit trail is desired.

## Publication boundary

The public manifest is a companion-repository integrity artifact. It is not a delivery manifest for the commercial master DOCX, PDF, EPUB, cover package, certificate, or store archives.
