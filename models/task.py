from models.base_model import BaseModel

class Task(BaseModel):

    def __init__(self, title, project_id):
        super().__init__()

        self.title = title
        self.project_id = project_id
        self.status = "Pending"

    def complete(self):
        self.status = "Done"