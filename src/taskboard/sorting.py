"""Consistent ordering for triage views."""
from .board import Task

_PRIORITY = {"high": 0, "normal": 1, "low": 2}


def by_priority(tasks: list[Task]) -> list[Task]:
    return sorted(tasks, key=lambda task: (_PRIORITY[task.priority], task.id))
