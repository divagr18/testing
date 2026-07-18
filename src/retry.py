from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Make at most two attempts for a transient timeout."""
    for attempt in range(2):
        try:
            return operation()
        except TimeoutError:
            if attempt:
                raise
    raise RuntimeError("unreachable")
