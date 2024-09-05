from uuid import UUID
from pydantic import BaseModel
from entities.task import TaskStatus
from models.user import UserViewModel

class TaskViewModel(BaseModel):
    id: UUID
    summary: str
    description: str
    status: TaskStatus
    priority: str
    assignee: UserViewModel
    
    class Config:
        from_attributes = True
