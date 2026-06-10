from storage.json_db import load, save
from models.task import Task
from rich import print
from rich.table import Table


class TaskService:
    FILE = "tasks.json"
    PROJECT_FILE = "projects.json"

    def _find_project(self, project_name):
        projects = load(self.PROJECT_FILE)

        for p in projects:
            if p["title"].lower() == project_name.lower():
                return p

        return None

    
    # CREATE TASK
    
    def add_task_by_name(self, project_name, title):
        tasks = load(self.FILE)

        project = self._find_project(project_name)

        if not project:
            print(f"[red]Project not found:[/red] {project_name}")
            return

        task = Task(title, project["id"])
        tasks.append(task.to_dict())

        save(self.FILE, tasks)

        print("\n[green]Task created successfully[/green]")
        print(f"[cyan]Title:[/cyan] {task.title}")
        print(f"[magenta]Project:[/magenta] {project_name}")
        print(f"[yellow]Status:[/yellow] {task.status}")

    
    # LIST TASKS
    
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
                table.add_row(
                    t["title"],
                    project_title,
                    t["status"]
                )
                found += 1

        if found == 0:
            print("[red]No tasks found[/red]")
            return

        print(table)

    
    # COMPLETE TASK
    
    def complete_task(self, task_title):
        tasks = load(self.FILE)

        updated = False

        for t in tasks:
            if t["title"].lower() == task_title.lower():
                t["status"] = "Done"
                updated = True

        save(self.FILE, tasks)

        if updated:
            print(f"[green]Task completed:[/green] {task_title}")
        else:
            print("[red]Task not found[/red]")

    
    # SEARCH TASK
    
    def search_task(self, keyword):
        tasks = load(self.FILE)
        projects = load(self.PROJECT_FILE)

        project_map = {p["id"]: p["title"] for p in projects}

        table = Table(title=f"Task Search: {keyword}")
        table.add_column("Title", style="green")
        table.add_column("Project", style="magenta")
        table.add_column("Status", style="yellow")

        found = 0

        for t in tasks:
            if keyword.lower() in t["title"].lower():

                project_title = project_map.get(
                    t["project_id"],
                    "Unknown"
                )

                table.add_row(
                    t["title"],
                    project_title,
                    t["status"]
                )

                found += 1

        if found == 0:
            print(f"[red]No tasks found matching '{keyword}'[/red]")
            return

        print(table)