"""Dashboard-specific grouping helpers."""
from .board import Task


def group_by_status(tasks: list[Task]) -> dict[str, list[Task]]:
    groups = {"todo": [], "doing": [], "done": []}
    for task in tasks:
        groups[task.status].append(task)
    return groups
