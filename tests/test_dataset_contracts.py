import json
from pathlib import Path

from tools.dataset_contracts import validate_catalog, validate_dataset


def test_valid_dataset_contract_passes(tmp_path: Path) -> None:
    csv_path = tmp_path / "sample.csv"
    csv_path.write_text("id,status\nA-1,Current\n", encoding="utf-8")
    contract = {
        "primary_id": "id",
        "required_columns": ["id", "status"],
        "allow_extra_columns": False,
    }
    assert validate_dataset(csv_path, contract) == []


def test_missing_required_column_is_reported(tmp_path: Path) -> None:
    csv_path = tmp_path / "sample.csv"
    csv_path.write_text("id\nA-1\n", encoding="utf-8")
    contract = {
        "primary_id": "id",
        "required_columns": ["id", "status"],
        "allow_extra_columns": False,
    }
    issues = validate_dataset(csv_path, contract)
    assert any("missing required columns: status" in issue for issue in issues)


def test_catalog_reports_uncontracted_csv(tmp_path: Path) -> None:
    datasets = tmp_path / "datasets"
    datasets.mkdir()
    (datasets / "sample.csv").write_text("id,status\nA-1,Current\n", encoding="utf-8")
    (datasets / "extra.csv").write_text("id,status\nB-1,Current\n", encoding="utf-8")
    contracts = tmp_path / "contracts.json"
    contracts.write_text(
        json.dumps(
            {
                "datasets": {
                    "sample.csv": {
                        "primary_id": "id",
                        "required_columns": ["id", "status"],
                        "allow_extra_columns": False,
                    }
                }
            }
        ),
        encoding="utf-8",
    )
    issues = validate_catalog(contracts, datasets)
    assert any("extra.csv: no contract defined" in issue for issue in issues)
