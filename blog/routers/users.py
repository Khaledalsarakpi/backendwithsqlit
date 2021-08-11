from typing import List
from fastapi import APIRouter,status,Response,HTTPException
from .. import schemas,database
from .. import schemas,module
from ..oauth2 import  get_active_user
from ..oauth2 import oauth2_scheme
from fastapi import Depends
from sqlalchemy.orm import Session
from ..repository import users
router=APIRouter(
    prefix='/user',
    tags=['users'])


@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.Showuser)
def create_user(request:schemas.User,db:Session=Depends(database.get_db)):
    return users.create(request,db)


@router.get('/{id}',status_code=200,response_model=schemas.Showuser)
def show(id:int,response:Response,db:Session=Depends(database.get_db)):
    return users.show(id,response,db)



@router.get('/active/user')
def active_user(usr:str=Depends(get_active_user)):
    return  usr

