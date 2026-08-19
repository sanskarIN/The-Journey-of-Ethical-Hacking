# Companion Project CLI Contract

This document defines the shared command-line behavior expected from the current offline defensive companion projects.

## Input scope

- Tools accept explicit local file or directory paths.
- Tools do not silently search a user's device.
- Current projects do not make network requests.
- Inputs are treated as untrusted and validated before analysis.
- Recursive directory tools should avoid following symbolic links outside the explicitly selected tree.

## Help behavior

Every executable project must support:

```bash
python companion-projects/<project>/<tool>.py --help
```

The command must exit successfully and display `usage:` text. The repository pytest suite smoke-tests this behavior for every discovered companion CLI.

## Output behavior

Prefer deterministic machine-readable output when the project returns structured results:

- JSON for summaries, validations, and policy findings;
- Markdown for human-readable timeline or review-note generators;
- CSV only when the project's explicit purpose is to create an inventory/export.

When practical:

- primary results go to stdout;
- diagnostics and counters go to stderr;
- explicitly requested output files are written only to the provided path.

## Exit status convention

Use these conventions where they fit the project's purpose:

- `0` — command completed successfully and no review/failure condition was found;
- `1` — command completed, but verification failed or review findings remain;
- `2` — invalid command-line arguments or invalid input rejected through `argparse`.

A reporting-only command that intentionally does not classify findings may return `0` after successful processing.

## Error handling

- Reject malformed CSV/JSON/JSONL values with readable messages.
- Reject missing required fields rather than silently inventing values.
- Reject unsupported categorical values.
- Reject impossible negative counts/durations where those fields must be non-negative.
- Validate dates/timestamps before sorting or calculating deadlines.
- Do not print stack traces for ordinary user input errors when a concise CLI error is sufficient.

## Determinism

For the same local input, output ordering should be stable where practical. Sort paths, keys, and aggregate labels when order is otherwise undefined.

## Privacy

The CLI must not transmit user inputs. Examples and tests must use synthetic or explicitly authorized data. Never commit real credentials, secrets, private incident evidence, buyer information, or paid publication content.

## Safety boundary

The shared CLI contract does not permit adding exploit delivery, credential collection, malware behavior, persistence, evasion, destructive actions, live-target discovery, or unauthorized scanning.
