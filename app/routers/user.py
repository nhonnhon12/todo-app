from typing import List
from fastapi import APIRouter, Depends
from starlette import status
from services.auth import authorizer
from sqlalchemy.orm import Session

from database import get_db_context
from models import UserViewModel, UserModel
from services import user as UserService
from models.user import UserClaims
from services.exception import AccessDeniedError

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("", status_code=status.HTTP_200_OK, response_model=List[UserViewModel])
async def get_users(
    db: Session = Depends(get_db_context),
    user: UserClaims = Depends(authorizer)):
    return UserService.get_users(db)

# @router.post("", status_code=status.HTTP_201_CREATED, response_model=UserViewModel)
# async def create_user(
#     request: UserModel, 
#     db: Session = Depends(get_db_context),
#     user: UserClaims = Depends(authorizer)):
#     if not user.is_admin:
#         raise AccessDeniedError()
#     return UserService.add_new_user(db, request)

# Update User

# Delete User

# Deactive User
