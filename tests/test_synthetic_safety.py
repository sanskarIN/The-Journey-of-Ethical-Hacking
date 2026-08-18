from pathlib import Path

from tools.synthetic_safety import scan_csv, scan_value


def test_scan_value_detects_sensitive_looking_patterns():
    assert "email" in scan_value("person@example.com")
    assert "url" in scan_value("https://example.com")
    assert "ipv4" in scan_value("192.0.2.5")
    assert "token_like" in scan_value("ghp_abcdefghijklmnopqrstuvwxyz123456")


def test_scan_value_accepts_normal_synthetic_values():
    assert scan_value("Example Operations") == []
    assert scan_value("SV-001") == []
    assert scan_value("Review due") == []


def test_scan_csv_reports_row_and_column(tmp_path: Path):
    path = tmp_path / "sample.csv"
    path.write_text("id,owner\nA-1,person@example.com\n", encoding="utf-8")

    findings = scan_csv(path)

    assert len(findings) == 1
    assert ":2:owner: email" in findings[0]


def test_scan_csv_accepts_fictional_dataset(tmp_path: Path):
    path = tmp_path / "sample.csv"
    path.write_text("id,owner\nA-1,Example Team\n", encoding="utf-8")
    assert scan_csv(path) == []
