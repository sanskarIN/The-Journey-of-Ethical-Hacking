import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("ioc_normalizer.py")
SPEC = importlib.util.spec_from_file_location("ioc_normalizer", MODULE_PATH)
ioc_normalizer = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(ioc_normalizer)


class IocNormalizerTests(unittest.TestCase):
    def test_classification_and_normalization(self) -> None:
        lines = [
            "192.0.2.10",
            "EXAMPLE.COM.",
            "d41d8cd98f00b204e9800998ecf8427e",
            "example.com",
            "not an indicator",
        ]
        result = ioc_normalizer.normalize_lines(lines)
        self.assertEqual(len(result["indicators"]), 3)
        self.assertEqual(result["rejected"], ["not an indicator"])

    def test_ipv6_is_canonicalized(self) -> None:
        result = ioc_normalizer.classify("2001:0db8:0:0:0:0:0:1")
        self.assertEqual(result, ("ipv6", "2001:db8::1"))


if __name__ == "__main__":
    unittest.main()
