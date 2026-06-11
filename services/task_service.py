from storage.json_db import load, save
from models.task import Task
from schemas.task_schema import TaskSchema
from rich import print
from rich.table import Table


class TaskService:
    FILE = "tasks.json"
    PROJECT_FILE = "projects.json"

    def _find_project(self, project_name):
        projects = load(self.PROJECT_FILE)

        for p in projects:
            if p.get("title", "").strip().lower() == project_name.strip().lower():
                return p

        return None

    def add_task_by_name(self, project_name, title):
        tasks = load(self.FILE)

        #  Pydantic validation
        try:
            validated = TaskSchema(title=title, project_name=project_name)
        except Exception as e:
            print(f"[red]Invalid task input:[/red] {e}")
            return False

        project = self._find_project(validated.project_name)

        if not project:
            print(f"[red]Project not found:[/red] {project_name}")
            return False

        task = Task(validated.title, project["id"])

        tasks.append(task.to_dict())
        save(self.FILE, tasks)

        print("\n[green]Task created successfully[/green]")
        print(f"[cyan]Title:[/cyan] {task.title}")
        print(f"[magenta]Project:[/magenta] {project_name}")
        print(f"[yellow]Status:[/yellow] {task.status}")

        return True

    def list_tasks(self, project_name=None):
        tasks = load(self.FILE)
        projects = load(self.PROJECT_FILE)

        project_map = {p["id"]: p["title"] for p in projects}

        table = Table(title="Tasks")
        table.add_column("Title", style="green")
        table.add_column("Project", style="magenta")
        table.add_column("Status", style="yellow")

        found = 0

        for t in tasks:
            project_title = project_map.get(t["project_id"], "Unknown")

            if project_name is None or project_title.lower() == project_name.lower():
                table.add_row(t["title"], project_title, t["status"])
                found += 1

        if found == 0:
            print("[red]No tasks found[/red]")
            return []

        print(table)
        return tasks

    def complete_task(self, task_title):
        tasks = load(self.FILE)

        updated = False

        for t in tasks:
            if t["title"].strip().lower() == task_title.strip().lower():
                t["status"] = "Done"
                updated = True

        save(self.FILE, tasks)

        if updated:
            print(f"[green]Task completed:[/green] {task_title}")
            return True

        print("[red]Task not found[/red]")
        return False