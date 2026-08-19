import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("jsonl_event_validator.py")
SPEC = importlib.util.spec_from_file_location("jsonl_event_validator", MODULE_PATH)
jsonl_event_validator = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(jsonl_event_validator)


class JsonlEventValidatorTests(unittest.TestCase):
    def test_valid_event(self) -> None:
        lines = [
            '{"timestamp":"2026-08-19T01:00:00Z","severity":"medium","category":"auth","summary":"Synthetic event","asset":"lab-1"}'
        ]
        result = jsonl_event_validator.validate_lines(lines)
        self.assertEqual(result, {"valid_events": 1, "errors": []})

    def test_naive_timestamp_and_bad_severity_are_rejected(self) -> None:
        lines = [
            '{"timestamp":"2026-08-19T01:00:00","severity":"urgent","category":"auth","summary":"Synthetic event","asset":"lab-1"}'
        ]
        result = jsonl_event_validator.validate_lines(lines)
        self.assertEqual(result["valid_events"], 0)
        self.assertEqual(len(result["errors"]), 1)


if __name__ == "__main__":
    unittest.main()
