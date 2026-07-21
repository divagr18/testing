"""A compact weekly update for the demo board."""
from .board import Task
from .stats import status_counts


def progress_line(tasks: list[Task]) -> str:
    counts = status_counts(tasks)
    return f"{counts['done']}/{len(tasks)} complete · {counts['doing']} in progress"
