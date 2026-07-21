"""Portable board exports without a runtime dependency."""
import json
from dataclasses import asdict
from .board import Task


def to_json(tasks: list[Task]) -> str:
    return json.dumps([asdict(task) for task in tasks], indent=2, sort_keys=True)
