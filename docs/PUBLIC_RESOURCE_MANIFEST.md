# Public Resource Manifest Workflow

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

A public-resource manifest provides a machine-readable inventory of the files intended to ship with a tagged companion-resource release.

## Generate the manifest

From the repository root:

```bash
python tools/resource_manifest.py --root . --output PUBLIC_RESOURCE_MANIFEST.json
```

## Verify the manifest

Verify that the artifact still matches the exact repository snapshot:

```bash
python tools/manifest_verify.py --root . PUBLIC_RESOURCE_MANIFEST.json
```

The verifier checks resource count, duplicate/unsafe paths, excluded commercial formats, missing or unexpected files, byte sizes, and SHA-256 hashes.

## Review before a tag

- [ ] Confirm the generated manifest contains only public companion resources.
- [ ] Confirm commercial `.pdf`, `.epub`, `.docx`, and `.zip` publication files are excluded.
- [ ] Confirm every listed file passes byte-size and SHA-256 verification.
- [ ] Review additions/removals compared with the previous tagged companion release.
- [ ] Confirm `COMPANION_RELEASE.json` has the intended companion version.
- [ ] Run `python tools/release_consistency.py --root .`.
- [ ] Run `python tools/release_readiness.py --root . --output docs/RELEASE_READINESS.md --check`.
- [ ] Run `python tools/repo_health.py --root .`.
- [ ] Confirm the official storefront remains `https://ramsandesh.gumroad.com`.
- [ ] Confirm X/Twitter remains omitted from publication-facing files.
- [ ] Confirm no author avatar/photo/person image has been introduced.

## Tagged workflow

The `Companion Release Manifest` workflow generates and verifies the manifest before uploading it. A failed verification prevents the artifact-upload step from being treated as a valid release record.

For manual review after a workflow run, use `MANIFEST_REVIEW.md`.

## Tagging policy

The manifest describes public repository resources only. It is not a delivery manifest for the paid commercial eBook package.

For each tagged companion release, generate the manifest from the final validated tag so hashes represent the exact release contents.

**Publication storefront:** https://ramsandesh.gumroad.com
