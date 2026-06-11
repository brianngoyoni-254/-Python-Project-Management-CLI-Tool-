from storage.json_db import load, save
from models.user import User
from schemas.user_schema import UserSchema
from rich import print
from rich.table import Table


class UserService:
    FILE = "users.json"

    def add_user(self, name, email):
        users = load(self.FILE)

        try:
            validated = UserSchema(name=name, email=email)
        except Exception as e:
            print(f"[red]Invalid user input:[/red] {e}")
            return False

        user = User(validated.name, str(validated.email))
        users.append(user.to_dict())
        save(self.FILE, users)

        print("[green]User created successfully[/green]")
        return True

    def list_users(self):
        users = load(self.FILE)

        table = Table(title="Users")
        table.add_column("Name", style="green")
        table.add_column("Email", style="magenta")

        for u in users:
            table.add_row(u["name"], u["email"])

        print(table)

    

    def delete_user(self, name):
        users = load(self.FILE)

        new_users = [
            u for u in users
            if u.get("name", "").lower() != name.lower()
        ]

        if len(new_users) == len(users):
            print("[red]User not found[/red]")
            return False

        save(self.FILE, new_users)
        print(f"[green]User deleted:[/green] {name}")
        return True

    def edit_user(self, name, new_name=None, new_email=None):
        users = load(self.FILE)

        for u in users:
            if u.get("name", "").lower() == name.lower():

                if new_name:
                    u["name"] = new_name

                if new_email:
                    u["email"] = new_email

                save(self.FILE, users)
                print(f"[green]User updated:[/green] {name}")
                return True

        print("[red]User not found[/red]")
        return False