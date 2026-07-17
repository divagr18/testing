import unittest

from src.diagnostics import describe_retry_failure


class RetryDiagnosticTests(unittest.TestCase):
    def test_returns_structured_timeout_context(self):
        result = describe_retry_failure("fetch profile", 2, TimeoutError("slow upstream"))
        self.assertEqual(result["operation"], "fetch profile")
        self.assertEqual(result["attempts"], 2)
        self.assertEqual(result["error_type"], "TimeoutError")
        self.assertEqual(result["message"], "slow upstream")


if __name__ == "__main__":
    unittest.main()
