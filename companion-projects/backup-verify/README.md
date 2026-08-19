# Backup Verify

Compare two explicitly selected local directories and report missing, unexpected, and changed files using SHA-256 hashes.

## Learning objective

Practice a simple defensive backup-verification workflow and understand why successful copy operations should still be independently checked.

## Usage

```bash
python companion-projects/backup-verify/backup_verify.py ./primary ./backup
```

## Output

JSON containing:

- `matching`
- `missing_from_backup`
- `unexpected_in_backup`
- `changed`

## Scope

The tool performs no backup creation, deletion, synchronization, or network activity. It only compares files beneath the two directories you explicitly provide.

Use directories you own or are authorized to verify.
