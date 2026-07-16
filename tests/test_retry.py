import unittest

from src.retry import retry_once


class RetryTests(unittest.TestCase):
    def test_returns_the_operation_value(self):
        self.assertEqual(retry_once(lambda: "ok"), "ok")

    def test_retries_only_after_a_timeout(self):
        calls = 0

        def operation():
            nonlocal calls
            calls += 1
            if calls == 1:
                raise TimeoutError("transient")
            return "recovered"

        self.assertEqual(retry_once(operation), "recovered")
        self.assertEqual(calls, 2)


if __name__ == "__main__":
    unittest.main()
