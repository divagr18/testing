import unittest

from src.diagnostics import describe_retry_failure


class RetryDiagnosticsTests(unittest.TestCase):
    def test_retry_failure_has_operation_attempts_and_error_details(self) -> None:
        result = describe_retry_failure("fetch-report", 2, TimeoutError("upstream timed out"))

        self.assertEqual(result["operation"], "fetch-report")
        self.assertEqual(result["attempts"], 2)
        self.assertEqual(result["error_type"], "TimeoutError")
        self.assertTrue(result["retryable"])


if __name__ == "__main__":
    unittest.main()
