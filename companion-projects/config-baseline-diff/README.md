# Configuration Baseline Diff

Compare two local JSON configuration snapshots and report added, removed, and changed paths.

## Learning objective

Practice defensive configuration-drift detection without connecting to live systems.

## Usage

```bash
python companion-projects/config-baseline-diff/config_baseline_diff.py baseline.json current.json
```

## Output

JSON containing:

- `added` paths
- `removed` paths
- `changed` paths

Nested objects are represented with dotted paths such as `logging.level`.

## Scope

The utility only reads the two explicit local files provided to it. It does not discover configuration files, connect to services, or modify settings.

Use synthetic snapshots or configurations you are authorized to review. Sanitize secrets before storing examples in this public repository.
