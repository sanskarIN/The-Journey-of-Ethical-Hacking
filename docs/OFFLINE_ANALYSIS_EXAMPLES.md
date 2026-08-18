# Offline Defensive Analysis Examples

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

These examples use only the fictional CSV files committed in this repository. They perform no network access, scanning, authentication, account access, device access, exploitation, or system changes.

## Risk-priority example

```bash
python tools/risk_priority.py datasets/sample_risk_signals.csv
```

Use the output to discuss why criticality, evidence age, open exceptions, telemetry gaps, and recovery gaps can influence **review priority**. The score is an educational heuristic, not a production risk model.

## Evidence-freshness example

```bash
python tools/evidence_freshness.py datasets/sample_control_evidence.csv
```

Use the output to identify fictional evidence records that may need review because of age.

## Control-review example

```bash
python tools/control_review.py datasets/sample_control_evidence.csv
```

The helper ranks fictional control evidence by a simple local review score. It is intended for governance and assurance exercises only.

## CSV-quality example

```bash
python tools/csv_quality.py datasets/*.csv
```

The quality checker looks for structural problems such as blank/duplicate headers, duplicate primary identifiers, blank identifiers, and inconsistent row widths.

## Dataset-summary example

```bash
python tools/dataset_summary.py datasets/*.csv
```

The summary helper reports each fictional dataset's row count, column count, blank-cell count, and field names. It is useful for quick repository review without sending data to an external service.

## Suggested learning workflow

1. Read the CSV manually before running a utility.
2. Predict which fictional records will be prioritized.
3. Run the local helper.
4. Compare the result with your prediction.
5. Document the assumptions behind the score.
6. Change only fictional values and observe how priorities change.
7. Record what the heuristic cannot represent.

## Important limitation

These utilities deliberately avoid production integrations and automated remediation. They are small teaching aids for reasoning about defensive evidence, not enterprise security products.

For the complete publication and current listings, use **https://ramsandesh.gumroad.com**.
