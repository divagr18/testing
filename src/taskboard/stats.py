"""Small, serializable board metrics."""
from collections import Counter
from .board import Task


def status_counts(tasks: list[Task]) -> dict[str, int]:
    counts = Counter(task.status for task in tasks)
    return {status: counts.get(status, 0) for status in ("todo", "doing", "done")}
