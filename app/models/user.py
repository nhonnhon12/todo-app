from uuid import UUID
from pydantic import BaseModel, Field


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

class UserViewModel(BaseModel):
    id: UUID
    username: str
    email: str | None = None
    first_name: str
    last_name: str
    
    class Config:
        from_attributes = True


class UserModel(BaseModel):
    email: str = Field(min_length=2)
    username: str = Field(min_length=10)
    first_name: str = Field()
    last_name: str = Field()
    # password: str = Field()
