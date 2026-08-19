# Log Sifter

A small defensive utility for summarizing **local, synthetic authentication-style CSV logs**. It performs no network activity and does not attempt to authenticate to anything.

## Learning objective

Practice turning raw event records into a compact defensive summary that can help with incident review.

## Input format

CSV with this header:

```text
timestamp,status,user,source
```

`status` should be `success` or `failure`.

Example:

```text
2026-08-19T01:00:00Z,failure,alex,lab-client-1
2026-08-19T01:01:00Z,success,alex,lab-client-1
2026-08-19T01:02:00Z,failure,casey,lab-client-2
```

## Usage

```bash
python companion-projects/log-sifter/log_sifter.py sample.csv
```

## Output

The tool prints JSON containing total events, success/failure counts, and per-user failure counts.

## Limitations

This is an educational local parser, not a SIEM, authentication monitor, or live detection agent.

Use only synthetic data or logs you are authorized to process.
