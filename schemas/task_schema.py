from pydantic import BaseModel, Field
from datetime import datetime, date


class TaskSchema(BaseModel):
    id: str | None = None
    title: str
    project_id: str

    status: str = "Pending"

    created_at: datetime = Field(default_factory=datetime.utcnow)
    due_date: date | None = None