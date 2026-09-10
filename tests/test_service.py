"""
Unit tests for task_manager.service
"""

import pytest
from unittest.mock import MagicMock

from task_manager.models import Priority, Status
from task_manager.service import TaskService


@pytest.fixture
def service():
    """TaskService backed by an in-memory mock storage."""
    mock_storage = MagicMock()
    mock_storage.load.return_value = []
    svc = TaskService(storage=mock_storage)
    return svc


class TestTaskService:
    def test_add_task(self, service):
        task = service.add("Write docs", priority="high")
        assert task.id == 1
        assert task.title == "Write docs"
        assert task.priority == Priority.HIGH

    def test_add_increments_id(self, service):
        t1 = service.add("Task A")
        t2 = service.add("Task B")
        assert t2.id == t1.id + 1

    def test_list_all(self, service):
        service.add("A")
        service.add("B")
        assert len(service.list_all()) == 2

    def test_filter_by_status(self, service):
        service.add("Pending task")
        t2 = service.add("In-progress task")
        service.update_status(t2.id, "in_progress")
        pending = service.filter_by_status("pending")
        assert len(pending) == 1
        assert pending[0].status == Status.PENDING

    def test_filter_by_priority(self, service):
        service.add("Low pri", priority="low")
        service.add("High pri", priority="high")
        high = service.filter_by_priority("high")
        assert len(high) == 1
        assert high[0].priority == Priority.HIGH

    def test_update_status_done(self, service):
        task = service.add("Deploy app")
        updated = service.update_status(task.id, "done")
        assert updated is not None
        assert updated.status == Status.DONE

    def test_update_status_not_found(self, service):
        result = service.update_status(999, "done")
        assert result is None

    def test_delete_task(self, service):
        task = service.add("Temp task")
        assert service.delete(task.id) is True
        assert len(service.list_all()) == 0

    def test_delete_nonexistent(self, service):
        assert service.delete(42) is False

    def test_clear_all(self, service):
        service.add("A")
        service.add("B")
        service.clear_all()
        assert service.list_all() == []
