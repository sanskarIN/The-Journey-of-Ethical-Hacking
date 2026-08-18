from tools.risk_priority import score


def test_high_risk_signals_score_higher():
    low = {
        "criticality": "Low",
        "age_days": "5",
        "open_exception": "No",
        "telemetry_gap": "No",
        "recovery_gap": "No",
    }
    high = {
        "criticality": "High",
        "age_days": "50",
        "open_exception": "Yes",
        "telemetry_gap": "Yes",
        "recovery_gap": "Yes",
    }
    assert score(high) > score(low)


def test_score_is_deterministic():
    row = {
        "criticality": "Medium",
        "age_days": "20",
        "open_exception": "No",
        "telemetry_gap": "Yes",
        "recovery_gap": "No",
    }
    assert score(row) == score(row)
