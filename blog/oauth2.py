from fastapi import Depends, status, HTTPException
from .repository import users
from .database import get_db
from .module import User
from sqlalchemy.orm import Session

from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)

import blog.token as tokenuser

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login", )


def get_current_user(
        token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": token},
    )
    return tokenuser.verify_token(token, credentials_exception)


def get_active_user(tokenuser: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    usershow = db.query(User).filter(User.token == tokenuser).first()
    print(tokenuser)
    print("User", usershow)
    if not usershow:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='not found any user active')
    return usershow
