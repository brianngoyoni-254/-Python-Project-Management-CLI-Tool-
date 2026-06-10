from storage.json_db import load
from rich import print
from rich.table import Table


class DashboardService:

    def show_dashboard(self):
        users = load("users.json")
        projects = load("projects.json")
        tasks = load("tasks.json")

        print("\n[bold cyan]PROJECT MANAGEMENT DASHBOARD[/bold cyan]\n")

        
        # SUMMARY STATS
        
        total_users = len(users)
        total_projects = len(projects)
        total_tasks = len(tasks)

        completed_tasks = len([t for t in tasks if t.get("status") == "Done"])
        pending_tasks = total_tasks - completed_tasks

        summary = Table(title="Summary")
        summary.add_column("Metric", style="cyan")
        summary.add_column("Value", style="green")

        summary.add_row("Users", str(total_users))
        summary.add_row("Projects", str(total_projects))
        summary.add_row("Tasks", str(total_tasks))
        summary.add_row("Completed Tasks", str(completed_tasks))
        summary.add_row("Pending Tasks", str(pending_tasks))

        print(summary)

        
        # USER LOOKUP MAP 
        
        user_map = {u["id"]: u["name"] for u in users}

        
        # USERS
        
        user_table = Table(title="Users")
        user_table.add_column("ID", style="magenta")
        user_table.add_column("Name", style="green")

        if not users:
            print("[yellow]No users found[/yellow]")
        else:
            for u in users:
                user_table.add_row(u["id"], u["name"])

            print(user_table)

        
        # PROJECTS 
        project_table = Table(title="Projects")
        project_table.add_column("ID", style="magenta")
        project_table.add_column("Title", style="green")
        project_table.add_column("User", style="cyan")

        if not projects:
            print("[yellow]No projects found[/yellow]")
        else:
            for p in projects:
                user_name = user_map.get(p["user_id"], "Unknown")
                project_table.add_row(p["id"], p["title"], user_name)

            print(project_table)

        
        # TASKS
        
        task_table = Table(title="Tasks")
        task_table.add_column("ID", style="magenta")
        task_table.add_column("Title", style="green")
        task_table.add_column("Status", style="yellow")

        if not tasks:
            print("[yellow]No tasks available yet[/yellow]")
        else:
            for t in tasks:
                task_table.add_row(
                    t.get("id", "N/A"),
                    t.get("title", "N/A"),
                    t.get("status", "Pending")
                )

            print(task_table)