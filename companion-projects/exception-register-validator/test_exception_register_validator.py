import importlib.util
import tempfile
import unittest
from datetime import date
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("exception_register_validator.py")
SPEC = importlib.util.spec_from_file_location("exception_register_validator", MODULE_PATH)
exception_register_validator = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(exception_register_validator)


class ExceptionRegisterValidatorTests(unittest.TestCase):
    def test_expired_and_unapproved_records_are_reported(self) -> None:
        csv_text = (
            "exception_id,owner,expires_on,rationale,approved\n"
            "EX-001,alex,2026-08-01,Training record,true\n"
            "EX-002,casey,2026-09-01,Training record,false\n"
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "exceptions.csv"
            path.write_text(csv_text, encoding="utf-8")
            result = exception_register_validator.validate_register(path, date(2026, 8, 19))

        self.assertEqual(result["exceptions"], 2)
        self.assertEqual(result["findings"][0]["reasons"], ["expired"])
        self.assertEqual(result["findings"][1]["reasons"], ["not-approved"])

    def test_invalid_approval_is_rejected(self) -> None:
        csv_text = "exception_id,owner,expires_on,rationale,approved\nEX-1,alex,2026-09-01,Training,maybe\n"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "exceptions.csv"
            path.write_text(csv_text, encoding="utf-8")
            with self.assertRaises(ValueError):
                exception_register_validator.validate_register(path, date(2026, 8, 19))


if __name__ == "__main__":
    unittest.main()
