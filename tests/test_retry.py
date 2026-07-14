import unittest

from src.retry import retry_once, retry_summary


class RetryTests(unittest.TestCase):
    def test_returns_the_operation_value(self):
        self.assertEqual(retry_once(lambda: "ok"), "ok")

    def test_formats_retry_summary(self):
        self.assertEqual(retry_summary(2, "recovered"), "retry attempts=2 outcome=recovered")


if __name__ == "__main__":
    unittest.main()
