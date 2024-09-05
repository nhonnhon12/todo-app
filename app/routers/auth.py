from datetime import timedelta
from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from settings import ACCESS_TOKEN_EXPIRE_MINUTES

from database import get_db_context
from services import user as UserService
from services.exception import UnAuthorizedError

router = APIRouter(prefix="/auth", tags=["Auth"])
@router.post("/token")
async def login_for_access_token(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db_context)
    ):
        user = UserService.authenticate_user(form_data.username, form_data.password, db)

        if not user:
            raise UnAuthorizedError()

        return {
            "token_type": "bearer",
            "access_token":  UserService.create_access_token(
                user, 
                int(timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES)).total_seconds())
            ),
        }