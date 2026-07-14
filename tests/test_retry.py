import unittest

from src.retry import retry_once


class RetryTests(unittest.TestCase):
    def test_returns_the_operation_value(self):
        self.assertEqual(retry_once(lambda: "ok"), "ok")

    def test_retries_one_timeout(self):
        calls = []

        def operation():
            calls.append("attempt")
            if len(calls) == 1:
                raise TimeoutError("temporary")
            return "ok"

        self.assertEqual(retry_once(operation), "ok")
        self.assertEqual(calls, ["attempt", "attempt"])


if __name__ == "__main__":
    unittest.main()
