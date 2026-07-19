import unittest

from src.retry import is_retryable_timeout, retry_once


class RetryTests(unittest.TestCase):
    def test_returns_the_operation_value(self):
        self.assertEqual(retry_once(lambda: "ok"), "ok")

    def test_identifies_timeout_as_retryable(self):
        self.assertTrue(is_retryable_timeout(TimeoutError("temporary")))
        self.assertFalse(is_retryable_timeout(ValueError("permanent")))


if __name__ == "__main__":
    unittest.main()
