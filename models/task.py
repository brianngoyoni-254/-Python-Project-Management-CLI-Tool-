from models.base_model import BaseModel
from datetime import date, datetime


class Task(BaseModel):
    def __init__(self, title, project_id, assigned_user_id=None, due_date=None):
        super().__init__()
        self._title = title
        self._project_id = project_id
        self._assigned_user_id = assigned_user_id
        self._status = "Pending"
        self._due_date = due_date

    @property
    def title(self):
        return self._title

    @property
    def project_id(self):
        return self._project_id

    @property
    def assigned_user_id(self):
        return self._assigned_user_id

    @property
    def status(self):
        return self._status

    @property
    def due_date(self):
        return self._due_date

    def complete(self):
        self._status = "Done"
        self.touch()

    def to_dict(self):
        base = super().to_dict()

        return {
            **base,
            "title": self._title,
            "project_id": self._project_id,
            "assigned_user_id": self._assigned_user_id,
            "status": self._status,
            "due_date": (
                self._due_date.isoformat()
                if isinstance(self._due_date, (date, datetime))
                else self._due_date
            )
        }