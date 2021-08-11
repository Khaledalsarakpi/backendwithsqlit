from .. import module,schemas,hashing
from sqlalchemy.orm import Session
from fastapi import Response,HTTPException,status
from ..token import create_access_token

def create(request:schemas.User,db:Session):
    tokenuser= access_token = create_access_token(
        data={"sub": request.name})
    hashedpassword = hashing.Hash.gethashing(request.password)
    new_user = module.User(name=request.name, email=request.email, password=hashedpassword,token=tokenuser)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id:int,response:Response,db:Session):
    usershow = db.query(module.User).filter(module.User.id == id).first()
    if not usershow:
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'deatilse':f"the item is not available {id}"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='the user is not found')
    return usershow