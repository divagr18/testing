import unittest

from src.retry import RetryPolicy, retry_once


class RetryTests(unittest.TestCase):
    def test_returns_the_operation_value(self):
        self.assertEqual(retry_once(lambda: "ok"), "ok")

    def test_policy_allows_timeout_before_budget_is_used(self):
        policy = RetryPolicy(max_attempts=3)

        self.assertTrue(policy.allows_next_attempt(2, TimeoutError("temporary")))
        self.assertFalse(policy.allows_next_attempt(3, TimeoutError("temporary")))
        self.assertFalse(policy.allows_next_attempt(1, ValueError("not a timeout")))

    def test_policy_rejects_an_empty_attempt_budget(self):
        with self.assertRaises(ValueError):
            RetryPolicy(max_attempts=0)


if __name__ == "__main__":
    unittest.main()
