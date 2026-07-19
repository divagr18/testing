from collections.abc import Callable
from dataclasses import dataclass


@dataclass(frozen=True)
class RetryPolicy:
    """Describe when a caller may make another timeout attempt."""

    max_attempts: int = 2

    def __post_init__(self) -> None:
        if self.max_attempts < 1:
            raise ValueError("max_attempts must be at least one")

    def allows_next_attempt(self, completed_attempts: int, error: BaseException) -> bool:
        """Return whether one more attempt is allowed for this result."""
        return isinstance(error, TimeoutError) and completed_attempts < self.max_attempts


def retry_once(operation: Callable[[], object]) -> object:
    """Run one operation without retrying it yet."""
    return operation()
