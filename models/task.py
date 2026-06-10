from models.base_model import BaseModel


class Task(BaseModel):
    def __init__(self, title, project_id):
        super().__init__()
        self._title = title
        self._project_id = project_id
        self._status = "Pending"

    @property
    def title(self):
        return self._title

    @property
    def project_id(self):
        return self._project_id

    @property
    def status(self):
        return self._status

    # 🔹 better OOP behavior method
    def complete(self):
        self._status = "Done"
        self.touch()  # updates updated_at timestamp

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "title": self._title,
            "project_id": self._project_id,
            "status": self._status
        })
        return data