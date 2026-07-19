from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Run one operation without retrying it yet."""
    return operation()


def is_retryable_timeout(error: Exception) -> bool:
    """Identify the transient timeout failures retry_once may retry."""
    return isinstance(error, TimeoutError)
