"""Dashboard-specific grouping helpers."""
from .board import Task
from .sorting import by_priority


def group_by_status(tasks: list[Task]) -> dict[str, list[Task]]:
    groups = {"todo": [], "doing": [], "done": []}
    for task in tasks:
        groups[task.status].append(task)
    return {status: by_priority(items) for status, items in groups.items()}


def column_totals(tasks: list[Task]) -> dict[str, int]:
    """Return a compact badge count for each workflow column."""
    return {status: len(items) for status, items in group_by_status(tasks).items()}
