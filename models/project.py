from models.base_model import BaseModel


class Project(BaseModel):
    def __init__(self, title, user_id):
        super().__init__()
        self._title = title
        self._user_id = user_id

    @property
    def title(self):
        return self._title

    @property
    def user_id(self):
        return self._user_id

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "title": self._title,
            "user_id": self._user_id
        })
        return data