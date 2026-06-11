from storage.json_db import load, save
from models.project import Project
from schemas.project_schema import ProjectSchema
from rich import print
from rich.table import Table


class ProjectService:
    FILE = "projects.json"
    USER_FILE = "users.json"

    def _find_user(self, user_name):
        users = load(self.USER_FILE)

        for u in users:
            if u.get("name", "").strip().lower() == user_name.strip().lower():
                return u

        return None

    def add_project(self, user_name, title):
        projects = load(self.FILE)

        # validate input using Pydantic
        try:
            validated = ProjectSchema(title=title, user_name=user_name)
        except Exception as e:
            print(f"[red]Invalid project input:[/red] {e}")
            return False

        user = self._find_user(validated.user_name)

        if not user:
            print(f"[red]User not found:[/red] {user_name}")
            return False

        project = Project(validated.title, user["id"])

        projects.append(project.to_dict())
        save(self.FILE, projects)

        print("\n[green]Project created successfully[/green]")
        print(f"[cyan]Title:[/cyan] {project.title}")
        print(f"[magenta]User:[/magenta] {user_name}")

        return True

    def list_projects(self, user_name=None):
        projects = load(self.FILE)
        users = load(self.USER_FILE)

        user_map = {u["id"]: u["name"] for u in users}

        table = Table(title="Projects")
        table.add_column("Title", style="green")
        table.add_column("User", style="magenta")

        found = 0

        for p in projects:
            owner = user_map.get(p.get("user_id"), "Unknown")

            if user_name is None or owner.lower() == user_name.lower():
                table.add_row(p["title"], owner)
                found += 1

        if found == 0:
            print("[red]No projects found[/red]")
            return []

        print(table)
        return projects