import unittest

from src.retry import retry_once


class RetryTests(unittest.TestCase):
    def test_returns_the_operation_value(self):
        self.assertEqual(retry_once(lambda: "ok"), "ok")

    def test_retries_one_transient_value_error(self):
        attempts = []

        def operation():
            attempts.append("run")
            if len(attempts) == 1:
                raise ValueError("temporary")
            return "recovered"

        self.assertEqual(retry_once(operation), "recovered")
        self.assertEqual(attempts, ["run", "run"])


if __name__ == "__main__":
    unittest.main()
