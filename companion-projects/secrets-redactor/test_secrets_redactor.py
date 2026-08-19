import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("secrets_redactor.py")
SPEC = importlib.util.spec_from_file_location("secrets_redactor", MODULE_PATH)
secrets_redactor = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(secrets_redactor)


class SecretsRedactorTests(unittest.TestCase):
    def test_assignment_and_bearer_values_are_redacted(self) -> None:
        text = "api_key=synthetic-value\nAuthorization: Bearer fake.example.token\n"
        sanitized, counts = secrets_redactor.redact(text)
        self.assertNotIn("synthetic-value", sanitized)
        self.assertNotIn("fake.example.token", sanitized)
        self.assertEqual(counts["assignment"], 1)
        self.assertEqual(counts["bearer"], 1)

    def test_private_key_block_is_redacted(self) -> None:
        text = "-----BEGIN PRIVATE KEY-----\nSYNTHETIC\n-----END PRIVATE KEY-----\n"
        sanitized, counts = secrets_redactor.redact(text)
        self.assertEqual(sanitized, "[REDACTED]\n")
        self.assertEqual(counts["private_key"], 1)


if __name__ == "__main__":
    unittest.main()
