from pathlib import Path

from tools.control_review import rank_evidence, review_score


def test_review_score_increases_for_exception_and_missing_recovery() -> None:
    base = {
        "criticality": "High",
        "evidence_age_days": "30",
        "exception_open": "No",
        "recovery_tested": "Yes",
    }
    elevated = dict(base, exception_open="Yes", recovery_tested="No")
    assert review_score(elevated) > review_score(base)


def test_rank_evidence_orders_highest_first(tmp_path: Path) -> None:
    csv_path = tmp_path / "evidence.csv"
    csv_path.write_text(
        "evidence_id,control_area,criticality,evidence_age_days,exception_open,recovery_tested,owner\n"
        "EV-A,Logging,Medium,10,No,Yes,Example\n"
        "EV-B,Backup,Critical,80,Yes,No,Example\n",
        encoding="utf-8",
    )
    rows = rank_evidence(csv_path)
    assert rows[0]["evidence_id"] == "EV-B"
