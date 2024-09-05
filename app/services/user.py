from typing import Optional
from datetime import timedelta

import jwt
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.user import UserClaims, UserModel
from entities.user import User, verify_password
from services.utils import get_current_timestamp
from services import utils
from entities.user import get_password_hash
from settings import JWT_ALGORITHM, JWT_SECRET


def create_access_token(user: User, expires: Optional[int] = None):
    claims = UserClaims(
        sub=str(user.id),
        username=user.username,
        email=user.email,
        email_verified=True,
        first_name=user.first_name,
        last_name=user.last_name,
        is_admin=user.is_admin,
        aud='FastAPI',
        iss='FastAPI',
        iat=get_current_timestamp(),
        exp=get_current_timestamp() + expires if expires else get_current_timestamp() + int(timedelta(minutes=10).total_seconds())
    )
    return jwt.encode(claims.model_dump(), JWT_SECRET, algorithm=JWT_ALGORITHM)

def authenticate_user(username: str, password: str, db: Session):
    user = db.scalars(select(User).filter(User.username == username)).first()

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def get_users(db: Session) -> list[User]:
    result = db.scalars(select(User).order_by(User.created_at))
    
    return result.all()

# def add_new_user(db: Session, data: UserModel) -> User:
#     # del data.password
#     user = User(**data.model_dump())

#     user.created_at = utils.get_current_utc_time()
#     user.updated_at = utils.get_current_utc_time()
    
#     db.add(user)
#     db.commit()
#     db.refresh(user)
    
#     return user
