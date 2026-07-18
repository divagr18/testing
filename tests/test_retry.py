import unittest

from src.retry import retry_once


class RetryTests(unittest.TestCase):
    def test_returns_the_operation_value(self):
        self.assertEqual(retry_once(lambda: "ok"), "ok")

    def test_retries_a_transient_timeout(self):
        results = iter([TimeoutError("temporary"), "recovered"])
        def operation():
            value = next(results)
            if isinstance(value, Exception):
                raise value
            return value
        self.assertEqual(retry_once(operation), "recovered")


if __name__ == "__main__":
    unittest.main()
