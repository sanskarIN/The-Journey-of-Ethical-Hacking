import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("access_review_helper.py")
SPEC = importlib.util.spec_from_file_location("access_review_helper", MODULE_PATH)
access_review_helper = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(access_review_helper)


class AccessReviewHelperTests(unittest.TestCase):
    def test_unapproved_role_is_reported(self) -> None:
        csv_text = "account,role,enabled\nalex,reader,true\ncasey,owner,true\n"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "accounts.csv"
            path.write_text(csv_text, encoding="utf-8")
            result = access_review_helper.review(path, {"reader", "analyst"})

        self.assertEqual(result["accounts"], 2)
        self.assertEqual(len(result["violations"]), 1)
        self.assertEqual(result["violations"][0]["account"], "casey")

    def test_invalid_enabled_value_is_rejected(self) -> None:
        csv_text = "account,role,enabled\nalex,reader,maybe\n"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "accounts.csv"
            path.write_text(csv_text, encoding="utf-8")
            with self.assertRaises(ValueError):
                access_review_helper.review(path, {"reader"})

    def test_empty_role_policy_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "policy.json"
            path.write_text('{"approved_roles": []}', encoding="utf-8")
            with self.assertRaises(ValueError):
                access_review_helper.load_policy(path)


if __name__ == "__main__":
    unittest.main()
