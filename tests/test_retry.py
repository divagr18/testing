import unittest

from src.retry import retry_once


class RetryTests(unittest.TestCase):
    def test_returns_the_operation_value(self):
        self.assertEqual(retry_once(lambda: "ok"), "ok")

    def test_retries_timeout_once_then_returns_the_second_value(self):
        attempts = 0

        def operation():
            nonlocal attempts
            attempts += 1
            if attempts == 1:
                raise TimeoutError("temporary outage")
            return "restored"

        self.assertEqual(retry_once(operation), "restored")
        self.assertEqual(attempts, 2)


if __name__ == "__main__":
    unittest.main()
