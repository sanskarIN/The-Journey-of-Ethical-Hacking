# Secrets Redactor

Redact common secret-like values from local text before logs, configuration excerpts, or diagnostics are shared.

## Learning objective

Practice defensive data minimization and safer troubleshooting workflows.

## Usage

```bash
python companion-projects/secrets-redactor/secrets_redactor.py input.txt --output sanitized.txt
```

Without `--output`, sanitized text is printed to stdout.

## Patterns handled

- Bearer-token style authorization values
- Common `api_key`, `token`, `secret`, and `password` assignments
- PEM-style private-key blocks

The tool uses conservative local pattern matching and never sends content anywhere.

## Limitations

No redactor can identify every secret format. Always manually review output before publishing or committing it.

Never test with real secrets in this public repository; use synthetic placeholders.
