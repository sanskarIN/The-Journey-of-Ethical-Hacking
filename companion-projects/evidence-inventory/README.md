# Evidence Inventory

Create a deterministic CSV inventory of local evidence files for defensive incident-response exercises.

## Learning objective

Practice documenting what files were collected without embedding file contents in the inventory.

## Usage

```bash
python companion-projects/evidence-inventory/evidence_inventory.py ./evidence inventory.csv
```

## Inventory fields

- Relative path
- File size in bytes
- UTC modification time
- SHA-256 digest

## Scope

This utility only reads files from the explicit directory you provide. It performs no network access and does not collect files from elsewhere on the device.

Use synthetic evidence or files you are authorized to inventory. Keep real incident evidence and personal data out of this public repository.
