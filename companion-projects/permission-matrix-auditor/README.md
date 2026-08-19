# Permission Matrix Auditor

Compare a local permission-assignment CSV against an explicit JSON policy and report assignments that are not allowed.

## Assignments CSV

```text
principal,resource,permission
alex,training-reports,read
casey,training-reports,write
```

## Policy JSON

```json
{
  "training-reports": ["read", "write"],
  "training-archive": ["read"]
}
```

## Usage

```bash
python companion-projects/permission-matrix-auditor/permission_matrix_auditor.py assignments.csv policy.json
```

## Learning objective

Practice least-privilege review and policy-as-data concepts using synthetic or authorized exports.

## Scope

This utility is read-only and local. It does not authenticate to systems, enumerate identities, change permissions, or discover resources.
