from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Retry a transient TimeoutError exactly once and return the retry result."""
    try:
        return operation()
    except TimeoutError:
        return operation()
