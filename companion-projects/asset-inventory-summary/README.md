# Asset Inventory Summary

Summarize a local CSV asset inventory and flag incomplete records for defensive governance exercises.

## Input format

```text
asset,type,owner,status
lab-host-1,workstation,alex,active
lab-db-1,database,casey,retired
```

Supported status values are `active`, `retired`, `maintenance`, and `unknown`.

## Usage

```bash
python companion-projects/asset-inventory-summary/asset_inventory_summary.py assets.csv
```

## Learning objective

Practice inventory hygiene, ownership review, and deterministic reporting.

## Scope

This utility does not scan networks or discover devices. It only reads the explicit CSV export you provide.

Use synthetic inventories or exports you are authorized to review.
