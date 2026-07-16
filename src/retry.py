from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Retry one transient timeout before surfacing it to the caller."""
    try:
        return operation()
    except TimeoutError:
        return operation()
