# Control Evidence Mapper

Map a local defensive evidence-register CSV to an explicit JSON list of recognized control identifiers.

## Evidence CSV

```text
evidence_id,control,status,owner
EV-001,CTRL-LOGGING,current,alex
EV-002,CTRL-BACKUP,stale,casey
```

Supported evidence status values are `current`, `stale`, and `missing`.

## Policy JSON

```json
{"controls":["CTRL-LOGGING","CTRL-BACKUP"]}
```

## Usage

```bash
python companion-projects/control-evidence-mapper/control_evidence_mapper.py evidence.csv controls.json
```

## Learning objective

Practice local control-to-evidence mapping, evidence-state summaries, and identification of records referencing unknown controls.

## Scope

This utility reads only the explicit local files provided to it. It does not collect evidence, query systems, change controls, or connect to external services.
