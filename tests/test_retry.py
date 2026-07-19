import unittest

from src.retry import retry_attempts_remaining, retry_once


class RetryTests(unittest.TestCase):
    def test_returns_the_operation_value(self):
        self.assertEqual(retry_once(lambda: "ok"), "ok")

    def test_reports_remaining_retry_budget(self):
        self.assertEqual(retry_attempts_remaining(3, 1), 2)
        self.assertEqual(retry_attempts_remaining(3, 5), 0)


if __name__ == "__main__":
    unittest.main()
