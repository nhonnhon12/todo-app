from fastapi import HTTPException, status
from functools import wraps
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, OAuth2PasswordBearer
from typing import Annotated
from fastapi import Depends
from services.exception import UnAuthorizedError
import jwt
from models.user import UserClaims
from settings import JWT_SECRET, JWT_ALGORITHM

security_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

def authorizer(token: Annotated[str, Depends(security_scheme)] = None):
    if not token:
        raise UnAuthorizedError()
    
    try:
        claims = jwt.decode(
            token,
            key=JWT_SECRET,
            algorithms=[JWT_ALGORITHM],
            options={
                "verify_aud": False,
                "verify_iss": False,
                "verify_exp": True,
            }
        )
        return UserClaims(**claims)

    except jwt.PyJWTError as err:
        print(err)
        raise UnAuthorizedError()
    