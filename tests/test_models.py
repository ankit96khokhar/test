"""
Unit tests for task_manager.models
"""

import pytest
from task_manager.models import Priority, Status, Task


def make_task(title="Buy groceries", priority="medium") -> Task:
    return Task(title=title, priority=Priority(priority))


class TestTask:
    def test_defaults(self):
        task = make_task()
        assert task.status == Status.PENDING
        assert task.priority == Priority.MEDIUM
        assert task.title == "Buy groceries"

    def test_mark_in_progress(self):
        task = make_task()
        task.mark_in_progress()
        assert task.status == Status.IN_PROGRESS

    def test_mark_done(self):
        task = make_task()
        task.mark_done()
        assert task.status == Status.DONE

    def test_to_dict_roundtrip(self):
        original = make_task("Write tests", "high")
        original.id = 42
        original.mark_in_progress()
        data = original.to_dict()
        restored = Task.from_dict(data)

        assert restored.id == 42
        assert restored.title == "Write tests"
        assert restored.priority == Priority.HIGH
        assert restored.status == Status.IN_PROGRESS

    def test_repr(self):
        task = make_task()
        task.id = 7
        assert "7" in repr(task)
        assert "Buy groceries" in repr(task)
