# Synthetic Dataset Contracts

This directory contains machine-readable contracts for the fictional CSV datasets used by the public companion repository.

The contracts are intentionally simple. Each dataset entry identifies:

- the expected primary identifier column;
- the required column names;
- whether additional columns are allowed.

They are used only for local validation of repository exercise files. They do not describe production security data models and should not be treated as an enterprise schema standard.

Run the validator with:

```bash
python tools/dataset_contracts.py schemas/dataset_contracts.json datasets
```

The validator performs no network access and does not modify the CSV files.
