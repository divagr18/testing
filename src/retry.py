from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Retry a timed-out operation once before surfacing its result."""
    try:
        return operation()
    except TimeoutError as timeout_error:
        return operation()
