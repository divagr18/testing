import unittest

from src.retry import retry_diagnostic_fields, retry_once


class RetryTests(unittest.TestCase):
    def test_returns_the_operation_value(self):
        self.assertEqual(retry_once(lambda: "ok"), "ok")

    def test_returns_log_friendly_retry_diagnostics(self):
        self.assertEqual(
            retry_diagnostic_fields(TimeoutError("gateway"), 2),
            {"attempts": 2, "error_type": "TimeoutError", "message": "gateway", "retryable": True},
        )


if __name__ == "__main__":
    unittest.main()
