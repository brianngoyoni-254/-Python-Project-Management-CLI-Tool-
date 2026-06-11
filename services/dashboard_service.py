from storage.json_db import load
from rich import print
from rich.table import Table


class DashboardService:

    def show_dashboard(self):
        users = load("users.json")
        projects = load("projects.json")
        tasks = load("tasks.json")

        print("\n[bold cyan]PROJECT MANAGEMENT DASHBOARD[/bold cyan]\n")

        summary = Table(title="Summary")
        summary.add_column("Metric", style="cyan")
        summary.add_column("Value", style="green")

        completed = len([t for t in tasks if t.get("status") == "Done"])
        pending = len(tasks) - completed

        summary.add_row("Users", str(len(users)))
        summary.add_row("Projects", str(len(projects)))
        summary.add_row("Tasks", str(len(tasks)))
        summary.add_row("Completed", str(completed))
        summary.add_row("Pending", str(pending))

        print(summary)

        user_map = {u["id"]: u["name"] for u in users}

        user_table = Table(title="Users")
        user_table.add_column("ID")
        user_table.add_column("Name")

        for u in users:
            user_table.add_row(u["id"], u["name"])

        print(user_table)

        project_table = Table(title="Projects")
        project_table.add_column("Title")
        project_table.add_column("User")

        for p in projects:
            project_table.add_row(
                p["title"],
                user_map.get(p["user_id"], "Unknown")
            )

        print(project_table)

        task_table = Table(title="Tasks")
        task_table.add_column("Title")
        task_table.add_column("Status")

        for t in tasks:
            task_table.add_row(t["title"], t["status"])

        print(task_table)