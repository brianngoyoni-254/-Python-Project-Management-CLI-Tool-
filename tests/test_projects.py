from models.project import Project
from models.base_model import BaseModel


def test_create_project():
    project = Project("CLI Tool", "123")

    assert project.title == "CLI Tool"
    assert project.user_id == "123"
    assert project.id is not None


def test_project_inherits_base_model():
    project = Project("CLI Tool", "123")

    assert isinstance(project, BaseModel)


def test_project_to_dict():
    project = Project("CLI Tool", "123")

    data = project.to_dict()

    assert data["title"] == "CLI Tool"
    assert data["user_id"] == "123"