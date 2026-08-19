# Security Checklist Tracker

Summarize Markdown task checklists used in defensive reviews, tabletop exercises, hardening plans, or incident follow-up.

## Usage

```bash
python companion-projects/security-checklist-tracker/checklist_tracker.py review.md
```

Supported task syntax:

```text
- [ ] Pending item
- [x] Completed item
- [X] Completed item
```

## Output

JSON containing total, completed, pending, completion percentage, and the pending item text.

## Learning objective

Practice turning human-readable defensive checklists into measurable progress without introducing a database or external service.

The tool only reads the explicit local Markdown file you provide.
