import unittest

from src.retry import retry_once


class RetryTests(unittest.TestCase):
    def test_returns_the_operation_value(self):
        self.assertEqual(retry_once(lambda: "ok"), "ok")

    def test_preserves_the_first_timeout_if_both_attempts_fail(self):
        first = TimeoutError("first")
        def operation():
            raise first
        with self.assertRaisesRegex(TimeoutError, "first"):
            retry_once(operation)


if __name__ == "__main__":
    unittest.main()
