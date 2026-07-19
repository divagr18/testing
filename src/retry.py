from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Run one operation without retrying it yet."""
    return operation()


def describe_retry_failure(error: TimeoutError, attempts: int) -> str:
    """Return a stable, human-readable retry diagnostic."""
    return f"retry failed after {attempts} attempts: {error}"
