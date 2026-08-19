# Change Review Notes

Convert a local CSV of proposed defensive or operational changes into a concise Markdown review sheet and flag entries that are not approved.

## Input format

```text
change_id,system,owner,summary,risk,approved
CHG-001,lab-app,alex,Enable additional audit logging,low,true
```

`risk` must be `low`, `medium`, or `high`; `approved` accepts true/false style values.

## Usage

```bash
python companion-projects/change-review-notes/change_review_notes.py changes.csv
```

## Learning objective

Practice change-control documentation and approval visibility without connecting to ticketing systems or modifying infrastructure.

The project is local and advisory only.
