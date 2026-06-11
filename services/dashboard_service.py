from storage.json_db import load
from rich import print
from rich.table import Table
from datetime import datetime, date, timezone
import json


class DashboardService:

    
    # HELPERS
    
    def _parse_date(self, d):
        if not d:
            return None
        try:
            return datetime.strptime(d, "%Y-%m-%d").date()
        except:
            return None

    def _get_urgency(self, due_date_str):
        due_date = self._parse_date(due_date_str)

        if not due_date:
            return "normal", "green"

        diff = (due_date - date.today()).days

        if diff < 0:
            return "overdue", "red"
        elif diff <= 3:
            return "due soon", "yellow"
        return "normal", "green"

    def _format(self, v):
        if not v:
            return "-"
        if isinstance(v, str):
            return v.split("T")[0]
        return str(v)

    def _productivity(self, tasks):
        if not tasks:
            return 0
        done = len([t for t in tasks if t.get("status") == "Done"])
        return round(done / len(tasks) * 100, 2)

    
    # DASHBOARD
    
    def show_dashboard(self):

        users = load("users.json") or []
        projects = load("projects.json") or []
        tasks = load("tasks.json") or []

        print("\n[bold cyan]PROJECT MANAGEMENT DASHBOARD[/bold cyan]\n")

        user_map = {u["id"]: u["name"] for u in users}
        project_map = {p["id"]: p["title"] for p in projects}

        # SORT BY URGENCY
        def sort_key(t):
            urgency, _ = self._get_urgency(t.get("due_date"))
            return {"overdue": 0, "due soon": 1, "normal": 2}.get(urgency, 2)

        tasks_sorted = sorted(tasks, key=sort_key)

        # SUMMARY
        total = len(tasks)
        done = len([t for t in tasks if t.get("status") == "Done"])

        summary = Table(title="Summary")
        summary.add_column("Metric", style="cyan")
        summary.add_column("Value", style="green")

        summary.add_row("Users", str(len(users)))
        summary.add_row("Projects", str(len(projects)))
        summary.add_row("Tasks", str(total))
        summary.add_row("Completed", str(done))
        summary.add_row("Productivity", f"{self._productivity(tasks)}%")

        print(summary)

        # USERS
        user_table = Table(title="Users")
        user_table.add_column("ID")
        user_table.add_column("Name")

        for u in users:
            user_table.add_row(u.get("id", ""), u.get("name", ""))

        print(user_table)

        # PROJECTS
        project_table = Table(title="Projects")
        project_table.add_column("ID")
        project_table.add_column("Title")
        project_table.add_column("User")

        for p in projects:
            project_table.add_row(
                p.get("id", ""),
                p.get("title", ""),
                user_map.get(p.get("user_id"), "Unknown")
            )

        print(project_table)

        # TASKS SMART VIEW
        task_table = Table(title="Tasks (Smart View)")
        task_table.add_column("Title", style="green")
        task_table.add_column("Project", style="magenta")
        task_table.add_column("Assigned To", style="cyan")
        task_table.add_column("Status", style="yellow")
        task_table.add_column("Created At", style="cyan")
        task_table.add_column("Due Date", style="cyan")
        task_table.add_column("Urgency", style="bold")

        for t in tasks_sorted:
            urgency, color = self._get_urgency(t.get("due_date"))

            task_table.add_row(
                t.get("title", ""),
                project_map.get(t.get("project_id"), "Unknown"),
                user_map.get(t.get("assigned_user_id"), "Unknown"),
                t.get("status", "Pending"),
                self._format(t.get("created_at")),
                self._format(t.get("due_date")),
                f"[{color}]{urgency}[/{color}]"
            )

        print(task_table)

    
    # EXPORT REPORT
    
    def export_weekly_report(self):
        tasks = load("tasks.json") or []

        report = {
            "generated_at": datetime.utcnow().isoformat(),
            "total_tasks": len(tasks),
            "completed": len([t for t in tasks if t.get("status") == "Done"]),
            "pending": len([t for t in tasks if t.get("status") != "Done"]),
            "overdue": len([
                t for t in tasks
                if self._get_urgency(t.get("due_date"))[0] == "overdue"
            ]),
            "tasks": tasks
        }

        with open("weekly_report.json", "w") as f:
            json.dump(report, f, indent=4)

        print("[green]Weekly report exported[/green]")