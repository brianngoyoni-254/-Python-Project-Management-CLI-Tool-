from datetime import datetime
from utils.id_generator import generate_id


class BaseModel:
    def __init__(self):
        self._id = generate_id()
        self._created_at = datetime.now().isoformat()
        self._updated_at = self._created_at

    # getters (encapsulation)
    @property
    def id(self):
        return self._id

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at

    # lifecycle tracking
    def touch(self):
        self._updated_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self._id,
            "created_at": self._created_at,
            "updated_at": self._updated_at
        }