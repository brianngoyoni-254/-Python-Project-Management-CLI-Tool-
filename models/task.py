from models.base_model import BaseModel
from datetime import date, datetime


class Task(BaseModel):
    def __init__(
        self,
        title,
        project_id,
        assigned_user_ids=None,
        due_date=None,
        status="Pending"
    ):
        super().__init__()

        self._title = title
        self._project_id = project_id
        self._assigned_user_ids = list(assigned_user_ids or [])
        self._due_date = due_date
        self._status = status

    # ================= GETTERS =================

    @property
    def title(self):
        return self._title

    @property
    def project_id(self):
        return self._project_id

    @property
    def assigned_user_ids(self):
        return self._assigned_user_ids

    @property
    def status(self):
        return self._status

    @property
    def due_date(self):
        return self._due_date



    def assign_user(self, user_id):
        if user_id not in self._assigned_user_ids:
            self._assigned_user_ids.append(user_id)
            self.touch()

    def remove_user(self, user_id):
        if user_id in self._assigned_user_ids:
            self._assigned_user_ids.remove(user_id)
            self.touch()

    def update_title(self, title):
        self._title = title
        self.touch()

    def update_due_date(self, due_date):
        self._due_date = due_date
        self.touch()

    def complete(self):
        self._status = "Done"
        self.touch()

    # SERIALIZATION 

    def to_dict(self):
        data = super().to_dict()

        return {
            **data,
            "title": self._title,
            "project_id": self._project_id,
            "assigned_user_ids": self._assigned_user_ids,
            "status": self._status,
            "due_date": (
                self._due_date.isoformat()
                if isinstance(self._due_date, (date, datetime))
                else self._due_date
            )
        }

    def __str__(self):
        return f"Task(title='{self._title}', status='{self._status}', project_id='{self._project_id}')"

    def __repr__(self):
        return self.__str__()