import unittest

from src.retry import retry_once


class RetryTests(unittest.TestCase):
    def test_returns_the_operation_value(self):
        self.assertEqual(retry_once(lambda: "ok"), "ok")

    def test_retries_one_transient_failure(self):
        attempts = 0

        def eventually_succeeds():
            nonlocal attempts
            attempts += 1
            if attempts == 1:
                raise TimeoutError("temporary timeout")
            return "recovered"

        self.assertEqual(retry_once(eventually_succeeds), "recovered")
        self.assertEqual(attempts, 2)


if __name__ == "__main__":
    unittest.main()
