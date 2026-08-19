# JSONL Event Validator

Validate local JSON Lines security-event records before they are used in defensive labs, demos, or analysis pipelines.

## Required fields

- `timestamp` — timezone-aware ISO 8601 value
- `severity` — `low`, `medium`, `high`, or `critical`
- `category` — non-empty text
- `summary` — non-empty text
- `asset` — non-empty synthetic or authorized asset label

## Usage

```bash
python companion-projects/jsonl-event-validator/jsonl_event_validator.py events.jsonl
```

## Learning objective

Practice defensive data-quality checks and clear validation errors before analysis begins.

## Scope

This project validates only the explicit local file provided to it. It performs no live collection, monitoring, scanning, or network access.
