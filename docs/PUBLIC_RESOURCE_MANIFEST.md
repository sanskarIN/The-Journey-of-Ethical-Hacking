# Public Resource Manifest Workflow

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

A public-resource manifest provides a machine-readable inventory of the files intended to ship with a tagged companion-resource release.

## Generate the manifest

From the repository root:

```bash
python tools/resource_manifest.py --root . --output PUBLIC_RESOURCE_MANIFEST.json
```

## Review before a tag

- [ ] Confirm the generated manifest contains only public companion resources.
- [ ] Confirm commercial `.pdf`, `.epub`, `.docx`, and `.zip` publication files are excluded.
- [ ] Confirm each listed file has a SHA-256 digest.
- [ ] Review additions/removals compared with the previous tagged companion release.
- [ ] Confirm `COMPANION_RELEASE.json` has the intended companion version.
- [ ] Run `python tools/release_consistency.py --root .`.
- [ ] Run `python tools/repo_health.py --root .`.
- [ ] Confirm the official storefront remains `https://ramsandesh.gumroad.com`.
- [ ] Confirm X/Twitter remains omitted from publication-facing files.
- [ ] Confirm no author avatar/photo/person image has been introduced.

## Tagging policy

The committed manifest should describe public repository resources only. It is not a delivery manifest for the paid commercial eBook package.

For each tagged companion release, regenerate the manifest after the final validated commit so hashes represent the exact release contents.

**Publication storefront:** https://ramsandesh.gumroad.com
