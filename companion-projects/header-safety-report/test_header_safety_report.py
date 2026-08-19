import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("header_safety_report.py")
SPEC = importlib.util.spec_from_file_location("header_safety_report", MODULE_PATH)
header_safety_report = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(header_safety_report)


class HeaderSafetyReportTests(unittest.TestCase):
    def test_authentication_and_domain_mismatch(self) -> None:
        text = (
            "From: Lab Sender <sender@example.test>\n"
            "Reply-To: Help <reply@different.test>\n"
            "Return-Path: <bounce@example.test>\n"
            "Received: from lab-a by lab-b\n"
            "Authentication-Results: lab.local; spf=pass; dkim=pass; dmarc=fail\n"
            "\n"
        )
        result = header_safety_report.analyze(text)
        self.assertEqual(result["received_hops"], 1)
        self.assertTrue(result["from_reply_domain_mismatch"])
        self.assertEqual(result["authentication"]["spf"], "pass")
        self.assertEqual(result["authentication"]["dmarc"], "fail")

    def test_missing_authentication_is_reported(self) -> None:
        result = header_safety_report.analyze("From: user@example.test\n\n")
        self.assertEqual(result["authentication"]["dkim"], "not-found")


if __name__ == "__main__":
    unittest.main()
