from typing import List
from fastapi import APIRouter, Depends
from starlette import status
from services.auth import authorizer
from sqlalchemy.orm import Session

from database import get_db_context
from models import TaskViewModel
from services import task as TaskService
from models.user import UserClaims

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("", status_code=status.HTTP_200_OK, response_model=List[TaskViewModel])
async def get_users(
    db: Session = Depends(get_db_context),
    user: UserClaims = Depends(authorizer)):
    return TaskService.get_tasks(db)

# Create task

# View task by ID

# Update task

# Delete task