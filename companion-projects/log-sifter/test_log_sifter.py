import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("log_sifter.py")
SPEC = importlib.util.spec_from_file_location("log_sifter", MODULE_PATH)
log_sifter = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(log_sifter)


class LogSifterTests(unittest.TestCase):
    def test_summary_counts(self) -> None:
        data = (
            "timestamp,status,user,source\n"
            "2026-08-19T01:00:00Z,failure,alex,lab-1\n"
            "2026-08-19T01:01:00Z,success,alex,lab-1\n"
            "2026-08-19T01:02:00Z,failure,casey,lab-2\n"
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "events.csv"
            path.write_text(data, encoding="utf-8")
            result = log_sifter.summarize(path)

        self.assertEqual(result["events"], 3)
        self.assertEqual(result["successes"], 1)
        self.assertEqual(result["failures"], 2)
        self.assertEqual(result["failures_by_user"], {"alex": 1, "casey": 1})

    def test_invalid_status_is_rejected(self) -> None:
        data = "timestamp,status,user,source\n2026-08-19T01:00:00Z,unknown,alex,lab-1\n"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "events.csv"
            path.write_text(data, encoding="utf-8")
            with self.assertRaises(ValueError):
                log_sifter.summarize(path)


if __name__ == "__main__":
    unittest.main()
