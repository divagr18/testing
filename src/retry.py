from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Run one operation without retrying it yet."""
    return operation()


def retry_attempts_remaining(max_attempts: int, attempts_used: int) -> int:
    """Return the remaining retry budget without allowing negative values."""
    return max(0, max_attempts - attempts_used)
