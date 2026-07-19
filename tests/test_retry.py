import unittest

from src.retry import build_retry_diagnostic, retry_once


class RetryTests(unittest.TestCase):
    def test_returns_the_operation_value(self):
        self.assertEqual(retry_once(lambda: "ok"), "ok")

    def test_builds_structured_retry_diagnostics(self):
        diagnostic = build_retry_diagnostic(TimeoutError("gateway"), 2)
        self.assertEqual(diagnostic.attempts, 2)
        self.assertEqual(diagnostic.error_type, "TimeoutError")
        self.assertEqual(diagnostic.message, "gateway")


if __name__ == "__main__":
    unittest.main()
