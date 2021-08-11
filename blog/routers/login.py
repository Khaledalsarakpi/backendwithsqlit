from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..schemas import Login
from .. import database,module,hashing
from ..  import token
router=APIRouter(tags=['Authentication'])


@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):

    user=db.query(module.User).filter(module.User.email==request.username).first()
    if not  user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="email not found")

    if not hashing.Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="incorrect password")
    access_token = token.create_access_token(
        data={"sub": user.username})
    return {"access_token":access_token,"token_type":"bearer"}

