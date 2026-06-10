from storage.json_db import load, save
from models.project import Project
from rich import print
from rich.table import Table


class ProjectService:
    FILE = "projects.json"

    def add_project(self, user_name, title):
        projects = load(self.FILE)
        users = load("users.json")

        user = None
        for u in users:
            if u["name"].lower() == user_name.lower():
                user = u
                break

        if not user:
            print(f"[red]User not found:[/red] {user_name}")
            return

        project = Project(title, user["id"])
        projects.append(project.to_dict())

        save(self.FILE, projects)

        print("\n[green]Project created successfully[/green]")
        print(f"[cyan]Title:[/cyan] {project.title}")
        print(f"[magenta]User:[/magenta] {user_name}")

    def list_projects(self, user_name=None):
        projects = load(self.FILE)
        users = load("users.json")

        user_map = {u["id"]: u["name"] for u in users}

        table = Table(title="Projects")
        table.add_column("Title", style="green")
        table.add_column("User", style="magenta")

        found = 0

        for p in projects:
            user_name_real = user_map.get(p["user_id"], "Unknown")

            if user_name is None or user_name_real.lower() == user_name.lower():
                table.add_row(p["title"], user_name_real)
                found += 1

        if found == 0:
            print("[red]No projects found[/red]")
            return

        print(table)

    def search_project(self, keyword):
        projects = load(self.FILE)

        table = Table(title=f"Search: {keyword}")
        table.add_column("Title", style="green")

        found = 0

        for p in projects:
            if keyword.lower() in p["title"].lower():
                table.add_row(p["title"])
                found += 1

        if found == 0:
            print("[red]No matches found[/red]")
            return

        print(table)