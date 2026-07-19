import unittest

from src.retry import describe_retry_failure, retry_once


class RetryTests(unittest.TestCase):
    def test_returns_the_operation_value(self):
        self.assertEqual(retry_once(lambda: "ok"), "ok")

    def test_describes_a_retry_failure(self):
        self.assertEqual(
            describe_retry_failure(TimeoutError("gateway"), 2),
            "retry failed after 2 attempts: gateway",
        )


if __name__ == "__main__":
    unittest.main()
