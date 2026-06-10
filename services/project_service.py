from storage.json_db import load, save
from models.project import Project
from rich import print
from rich.table import Table


class ProjectService:
    FILE = "projects.json"
    USER_FILE = "users.json"

    # FIND USER 
    
    def _find_user(self, user_name):
        users = load(self.USER_FILE)

        if not users:
            return None

        for u in users:
            name = u.get("name")

            if isinstance(name, str) and name.strip().lower() == user_name.strip().lower():
                return u

        return None

    
    # CREATE PROJECT
    
    def add_project(self, user_name, title):
        projects = load(self.FILE)

        user = self._find_user(user_name)

        if not user:
            print(f"[red]User not found:[/red] {user_name}")
            return False

        user_id = user.get("id")

        if not user_id:
            print("[red]Invalid user data (missing id)[/red]")
            return False

        project = Project(title, user_id)
        projects.append(project.to_dict())

        save(self.FILE, projects)

        print("\n[green]Project created successfully[/green]")
        print(f"[cyan]Title:[/cyan] {project.title}")
        print(f"[magenta]User:[/magenta] {user_name}")

        return True

    
    # LIST PROJECTS
    
    def list_projects(self, user_name=None):
        projects = load(self.FILE)
        users = load(self.USER_FILE)

        user_map = {}

        for u in users:
            if isinstance(u.get("id"), str) and isinstance(u.get("name"), str):
                user_map[u["id"]] = u["name"]

        table = Table(title="Projects")
        table.add_column("Title", style="green")
        table.add_column("User", style="magenta")

        found = 0

        for p in projects:
            project_user_name = user_map.get(p.get("user_id"), "Unknown")

            if user_name is None or project_user_name.lower() == user_name.lower():
                table.add_row(
                    p.get("title", ""),
                    project_user_name
                )
                found += 1

        if found == 0:
            print("[red]No projects found[/red]")
            return []

        print(table)
        return projects

    
    # SEARCH PROJECT
    
    def search_project(self, keyword):
        projects = load(self.FILE)

        table = Table(title=f"Search: {keyword}")
        table.add_column("Title", style="green")
        table.add_column("User ID", style="magenta")

        found = 0

        for p in projects:
            title = p.get("title", "")

            if keyword.lower() in title.lower():
                table.add_row(
                    title,
                    p.get("user_id", "Unknown")
                )
                found += 1

        if found == 0:
            print("[red]No matches found[/red]")
            return []

        print(table)
        return projects