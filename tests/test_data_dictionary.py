from tools.data_dictionary import build_markdown, constraint_text


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
