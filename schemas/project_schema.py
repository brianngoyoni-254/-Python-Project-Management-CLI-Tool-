from pydantic import BaseModel


class ProjectSchema(BaseModel):
    title: str
    user_name: str