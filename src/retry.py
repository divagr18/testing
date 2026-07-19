from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Retry a timeout once and retain the first failure as context."""
    try:
        return operation()
    except TimeoutError as first_error:
        try:
            return operation()
        except TimeoutError as second_error:
            raise TimeoutError("retry failed after two timeout attempts") from first_error
