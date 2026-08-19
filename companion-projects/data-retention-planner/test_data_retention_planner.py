import importlib.util
import tempfile
import unittest
from datetime import date
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("data_retention_planner.py")
SPEC = importlib.util.spec_from_file_location("data_retention_planner", MODULE_PATH)
data_retention_planner = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(data_retention_planner)


class DataRetentionPlannerTests(unittest.TestCase):
    def test_due_date_calculation(self) -> None:
        csv_text = (
            "dataset,classification,last_review,review_interval_days\n"
            "synthetic-auth-logs,training,2026-07-01,30\n"
            "synthetic-assets,training,2026-08-10,30\n"
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "register.csv"
            path.write_text(csv_text, encoding="utf-8")
            result = data_retention_planner.review(path, date(2026, 8, 19))

        self.assertEqual(result["due_count"], 1)
        self.assertTrue(result["datasets"][0]["due"])
        self.assertFalse(result["datasets"][1]["due"])

    def test_non_positive_interval_is_rejected(self) -> None:
        csv_text = "dataset,classification,last_review,review_interval_days\na,training,2026-08-01,0\n"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "register.csv"
            path.write_text(csv_text, encoding="utf-8")
            with self.assertRaises(ValueError):
                data_retention_planner.review(path, date(2026, 8, 19))


if __name__ == "__main__":
    unittest.main()
