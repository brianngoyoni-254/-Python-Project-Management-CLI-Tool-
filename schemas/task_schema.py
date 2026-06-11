from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime, date


class TaskSchema(BaseModel):
    id: UUID | None = None
    title: str
    project_id: str  
    status: str = "Pending"

    created_at: datetime = Field(default_factory=datetime.utcnow)
    due_date: date | None = None