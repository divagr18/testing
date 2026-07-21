"""Dashboard-specific grouping helpers."""
from .board import Task
from .sorting import by_priority


def group_by_status(tasks: list[Task]) -> dict[str, list[Task]]:
    groups = {"todo": [], "doing": [], "done": []}
    for task in tasks:
        groups[task.status].append(task)
    return {status: by_priority(items) for status, items in groups.items()}
