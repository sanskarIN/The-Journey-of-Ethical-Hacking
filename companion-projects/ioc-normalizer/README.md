# IOC Normalizer

Normalize defensive indicators from a local text file into deterministic JSON. The utility performs **no DNS, HTTP, WHOIS, or reputation lookups**.

## Supported indicator types

- IPv4 addresses
- IPv6 addresses
- Domain names
- MD5, SHA-1, and SHA-256 hashes

## Usage

```bash
python companion-projects/ioc-normalizer/ioc_normalizer.py indicators.txt
```

Use one value per line. Blank lines and lines beginning with `#` are ignored.

## Learning objective

Practice validation, canonicalization, deduplication, and structured export for defensive incident-response data.

## Limitations

The project does not determine whether an indicator is malicious. It only validates and normalizes values already supplied in the input file.

Use synthetic indicators or data you are authorized to process.
