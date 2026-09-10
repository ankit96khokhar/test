"""
Storage layer for persisting tasks to a JSON file.
"""

import json
import os
from typing import List

from task_manager.models import Task


DEFAULT_FILE = "tasks.json"


class Storage:
    """Handles reading and writing tasks to disk."""

    def __init__(self, filepath: str = DEFAULT_FILE):
        self.filepath = filepath

    def load(self) -> List[Task]:
        """Load all tasks from the JSON file."""
        if not os.path.exists(self.filepath):
            return []

        with open(self.filepath, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return []

        return [Task.from_dict(item) for item in data]

    def save(self, tasks: List[Task]) -> None:
        """Save all tasks to the JSON file."""
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in tasks], f, indent=2)

    def clear(self) -> None:
        """Delete all stored tasks."""
        if os.path.exists(self.filepath):
            os.remove(self.filepath)
