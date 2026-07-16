from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Retry a transient timeout once, then return the second result."""
    try:
        return operation()
    except TimeoutError:
        return operation()
