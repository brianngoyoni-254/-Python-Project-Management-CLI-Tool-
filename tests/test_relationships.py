from services.user_service import UserService
from services.project_service import ProjectService
from services.task_service import TaskService
from storage.json_db import load


def test_user_project_task_flow():
    user_service = UserService()
    project_service = ProjectService()
    task_service = TaskService()

    # isolate test files
    user_service.FILE = "test_users.json"
    project_service.FILE = "test_projects.json"
    task_service.FILE = "test_tasks.json"
    task_service.PROJECT_FILE = "test_projects.json"

    # reset files
    from storage.json_db import save
    save(user_service.FILE, [])
    save(project_service.FILE, [])
    save(task_service.FILE, [])

    # 1. Create user
    user_service.add_user("Ngoyoni", "ngoyoni@mail.com")

    users = load(user_service.FILE)
    assert len(users) == 1

    # 2. Create project
    project_service.add_project("Ngoyoni", "Final Project")

    projects = load(project_service.FILE)
    assert len(projects) == 1

    # 3. Create task
    task_service.add_task_by_name("Final Project", "Implement CLI")

    tasks = load(task_service.FILE)
    assert len(tasks) == 1

    # 4. Complete lifecycle
    task_service.complete_task("Implement CLI")

    updated_tasks = load(task_service.FILE)
    assert updated_tasks[0]["status"] == "Done"