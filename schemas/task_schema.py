from pydantic import BaseModel


class TaskSchema(BaseModel):
    title: str
    project_name: str