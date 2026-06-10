from models.task import Task
from models.base_model import BaseModel


def test_create_task():
    task = Task("Build CLI", "123")

    assert task.title == "Build CLI"
    assert task.project_id == "123"
    assert task.status == "Pending"


def test_complete_task():
    task = Task("Build CLI", "123")

    task.complete()

    assert task.status == "Done"


def test_task_inherits_base_model():
    task = Task("Build CLI", "123")

    assert isinstance(task, BaseModel)


def test_task_to_dict():
    task = Task("Build CLI", "123")

    data = task.to_dict()

    assert data["title"] == "Build CLI"
    assert data["project_id"] == "123"
    assert data["status"] == "Pending"