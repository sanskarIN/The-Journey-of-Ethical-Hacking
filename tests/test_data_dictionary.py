import json
from pathlib import Path

from tools.data_dictionary import build_markdown, constraint_text, expected_text, is_current


def test_constraint_text_includes_primary_allowed_and_range() -> None:
    contract = {
        "primary_id": "id",
        "allowed_values": {"status": ["Current", "Review-Due"]},
        "integer_ranges": {"age_days": {"min": 0, "max": 365}},
    }
    assert "Primary identifier" in constraint_text(contract, "id")
    assert "Current" in constraint_text(contract, "status")
    assert "0–365" in constraint_text(contract, "age_days")


def test_build_markdown_lists_dataset_and_storefront() -> None:
    contracts = {
        "sample.csv": {
            "primary_id": "id",
            "required_columns": ["id", "status"],
            "allowed_values": {"status": ["Current", "Review-Due"]},
        }
    }
    text = build_markdown(contracts)
    assert "# Synthetic Dataset Data Dictionary" in text
    assert "`sample.csv`" in text
    assert "`id`" in text
    assert "https://ramsandesh.gumroad.com" in text


def write_contracts(path: Path) -> None:
    path.write_text(
        json.dumps(
            {
                "datasets": {
                    "sample.csv": {
                        "primary_id": "id",
                        "required_columns": ["id", "status"],
                        "allowed_values": {"status": ["Current", "Review-Due"]},
                    }
                }
            }
        ),
        encoding="utf-8",
    )


def test_is_current_accepts_generated_dictionary(tmp_path: Path) -> None:
    contracts = tmp_path / "contracts.json"
    output = tmp_path / "dictionary.md"
    write_contracts(contracts)
    output.write_text(expected_text(contracts), encoding="utf-8")
    assert is_current(contracts, output) is True


def test_is_current_rejects_stale_dictionary(tmp_path: Path) -> None:
    contracts = tmp_path / "contracts.json"
    output = tmp_path / "dictionary.md"
    write_contracts(contracts)
    output.write_text("# stale\n", encoding="utf-8")
    assert is_current(contracts, output) is False
