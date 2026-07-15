from collections.abc import Callable


def retry_summary(attempts: int, outcome: str) -> str:
    """Return a stable, human-readable retry event for observability."""
    if attempts < 1:
        raise ValueError("attempts must be positive")
    return f"retry attempts={attempts} outcome={outcome}"


def retry_once(operation: Callable[[], object]) -> object:
    """Run one operation without retrying it yet."""
    return operation()
