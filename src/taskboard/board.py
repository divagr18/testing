"""Core domain objects for the demo task board."""

from __future__ import annotations

from dataclasses import dataclass, replace


class TaskNotFoundError(KeyError):
    """Raised when a task id is not present in a board."""


@dataclass(frozen=True, slots=True)
class Task:
    id: int
    title: str
    status: str = "todo"
    priority: str = "normal"


class Board:
    """An in-memory collection of small, well-defined tasks."""

    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def add(self, title: str, *, priority: str = "normal") -> Task:
        title = title.strip()
        if not title:
            raise ValueError("A task title is required.")
        if priority not in {"low", "normal", "high"}:
            raise ValueError("Priority must be low, normal, or high.")
        task = Task(id=self._next_id, title=title, priority=priority)
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def get(self, task_id: int) -> Task:
        try:
            return self._tasks[task_id]
        except KeyError as error:
            raise TaskNotFoundError(task_id) from error

    def list(self, *, status: str | None = None) -> list[Task]:
        tasks = list(self._tasks.values())
        if status is not None:
            tasks = [task for task in tasks if task.status == status]
        return tasks

    def move(self, task_id: int, status: str) -> Task:
        if status not in {"todo", "doing", "done"}:
            raise ValueError("Status must be todo, doing, or done.")
        task = self.get(task_id)
        updated = replace(task, status=status)
        self._tasks[task_id] = updated
        return updated
