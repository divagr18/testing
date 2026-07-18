from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Run an operation again if its first call raises TimeoutError."""
    try:
        first_value = operation()
    except TimeoutError as first_error:
        try:
            return operation()
        except TimeoutError:
            raise first_error
    return first_value
