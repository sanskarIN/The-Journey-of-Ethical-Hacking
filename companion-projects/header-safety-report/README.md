# Header Safety Report

Inspect a **saved email header file** and produce a small local JSON report about authentication signals and address alignment hints.

## Learning objective

Practice reading email metadata used in defensive phishing triage without opening links, downloading attachments, or contacting external services.

## Usage

```bash
python companion-projects/header-safety-report/header_safety_report.py headers.txt
```

## Report fields

- From address
- Reply-To address
- Return-Path address
- Number of Received headers
- Whether Authentication-Results mentions SPF, DKIM, or DMARC pass/fail
- Whether From and Reply-To domains differ

## Important limitation

This tool is an educational local parser. It does not prove a message is safe or malicious and performs no network or reputation lookups.

Use saved headers you are authorized to inspect. Avoid committing real private email headers to this public repository.
