# Incident Timeline Builder

Turn local JSON Lines event records into a chronologically sorted Markdown timeline for defensive incident review.

## Input

One JSON object per line with:

- `timestamp` — ISO 8601 timestamp
- `category` — short event category
- `summary` — concise event description
- `asset` — synthetic or authorized asset label

Example:

```json
{"timestamp":"2026-08-19T01:02:00Z","category":"auth","summary":"Synthetic failed sign-in event","asset":"lab-host-1"}
```

## Usage

```bash
python companion-projects/incident-timeline/incident_timeline.py events.jsonl
```

## Learning objective

Practice evidence ordering, timestamp validation, and concise incident documentation.

## Privacy

Do not commit real incident records, credentials, buyer data, or sensitive evidence to this public repository. Use synthetic examples or authorized local data.
