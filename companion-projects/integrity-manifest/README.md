# Integrity Manifest

Create and verify SHA-256 manifests for local files. This project demonstrates a basic blue-team integrity-checking workflow without network access.

## Learning objective

Understand how cryptographic hashes can help detect accidental or unexpected file changes.

## Create a manifest

```bash
python companion-projects/integrity-manifest/integrity_manifest.py create ./sample-data manifest.json
```

## Verify a manifest

```bash
python companion-projects/integrity-manifest/integrity_manifest.py verify ./sample-data manifest.json
```

The manifest stores relative file paths, byte sizes, and SHA-256 digests. Verification reports `ok`, `missing`, `changed`, and `unexpected` files.

## Safety and privacy

Use this only on directories you own or are authorized to inspect. The tool reads file contents locally only to calculate hashes and never transmits data.
