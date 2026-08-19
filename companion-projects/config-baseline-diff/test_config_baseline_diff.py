import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("config_baseline_diff.py")
SPEC = importlib.util.spec_from_file_location("config_baseline_diff", MODULE_PATH)
config_baseline_diff = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(config_baseline_diff)


class ConfigBaselineDiffTests(unittest.TestCase):
    def test_added_removed_and_changed_paths(self) -> None:
        baseline = {"logging": {"level": "info"}, "feature": True}
        current = {"logging": {"level": "warning"}, "owner": "lab"}
        result = config_baseline_diff.compare(baseline, current)
        self.assertEqual(result["added"], ["owner"])
        self.assertEqual(result["removed"], ["feature"])
        self.assertEqual(result["changed"], ["logging.level"])

    def test_identical_snapshots_have_no_drift(self) -> None:
        value = {"a": {"b": 1}}
        self.assertEqual(
            config_baseline_diff.compare(value, value),
            {"added": [], "removed": [], "changed": []},
        )


if __name__ == "__main__":
    unittest.main()
