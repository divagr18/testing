from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Retry once when the first operation attempt times out."""
    try:
        return operation()
    except TimeoutError:
        return operation()
