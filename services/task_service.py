from storage.json_db import load, save
from models.task import Task
from rich import print
from rich.table import Table


class TaskService:
    FILE = "tasks.json"
    PROJECT_FILE = "projects.json"

    def __init__(self, project_file=None):
        if project_file:
            self.PROJECT_FILE = project_file

    
    # LOAD PROJECTS 
    
    def _load_projects(self):
        projects = load(self.PROJECT_FILE)
        return projects if projects else []

    
    # FIND PROJECT 
    
    def _find_project(self, project_name):
        projects = self._load_projects()

        target = project_name.strip().lower()

        for p in projects:
            title = p.get("title")

            if isinstance(title, str) and title.strip().lower() == target:
                return p

        return None

    
    # CREATE TASK
    
    def add_task_by_name(self, project_name, title):
        tasks = load(self.FILE)

        project = self._find_project(project_name)

        if not project:
            print(f"[red]Project not found:[/red] {project_name}")
            return False

        project_id = project.get("id")

        if not project_id:
            print("[red]Invalid project (missing id)[/red]")
            return False

        task = Task(title, project_id)
        tasks.append(task.to_dict())

        save(self.FILE, tasks)

        print("\n[green]Task created successfully[/green]")
        print(f"[cyan]Title:[/cyan] {task.title}")
        print(f"[magenta]Project:[/magenta] {project_name}")
        print(f"[yellow]Status:[/yellow] {task.status}")

        return True

    
    # LIST TASKS
    
    def list_tasks(self, project_name=None):
        tasks = load(self.FILE)
        projects = self._load_projects()

        project_map = {
            p.get("id"): p.get("title")
            for p in projects
            if p.get("id") and p.get("title")
        }

        table = Table(title="Tasks")
        table.add_column("Title", style="green")
        table.add_column("Project", style="magenta")
        table.add_column("Status", style="yellow")

        found = 0

        for t in tasks:
            project_title = project_map.get(t.get("project_id"), "Unknown")

            if project_name is None or project_title.lower() == project_name.lower():
                table.add_row(
                    t.get("title", ""),
                    project_title,
                    t.get("status", "")
                )
                found += 1

        if found == 0:
            print("[red]No tasks found[/red]")
            return []

        print(table)
        return tasks

    
    # COMPLETE TASK
    
    def complete_task(self, task_title):
        tasks = load(self.FILE)

        updated = False

        for t in tasks:
            if t.get("title", "").strip().lower() == task_title.strip().lower():
                t["status"] = "Done"
                updated = True

        save(self.FILE, tasks)

        if updated:
            print(f"[green]Task completed:[/green] {task_title}")
            return True

        print("[red]Task not found[/red]")
        return False

    
    # SEARCH TASK
    
    def search_task(self, keyword):
        tasks = load(self.FILE)
        projects = self._load_projects()

        project_map = {
            p.get("id"): p.get("title")
            for p in projects
            if p.get("id") and p.get("title")
        }

        table = Table(title=f"Task Search: {keyword}")
        table.add_column("Title", style="green")
        table.add_column("Project", style="magenta")
        table.add_column("Status", style="yellow")

        found = 0
        keyword = keyword.lower()

        for t in tasks:
            if keyword in t.get("title", "").lower():

                project_title = project_map.get(t.get("project_id"), "Unknown")

                table.add_row(
                    t.get("title", ""),
                    project_title,
                    t.get("status", "")
                )

                found += 1

        if found == 0:
            print(f"[red]No tasks found matching '{keyword}'[/red]")
            return []

        print(table)
        return tasks