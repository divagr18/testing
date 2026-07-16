from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Retry exactly once when the first call times out."""
    try:
        return operation()
    except TimeoutError:
        return operation()
