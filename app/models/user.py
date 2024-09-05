from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class UserClaims(BaseModel):
    sub: str
    username: str = None
    email: str = None
    email_verified: bool = True
    first_name: str
    last_name: str
    is_admin: bool = False
    aud: str = None
    iss: str = None
    iat: int
    exp: int