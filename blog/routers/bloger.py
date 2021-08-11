from typing import List
from fastapi import APIRouter,status,Response,HTTPException
from .. import schemas,database
from .. import schemas,module,oauth2
from fastapi import Depends
from sqlalchemy.orm import Session
from ..repository import blog
router=APIRouter(
    prefix='/blog',
    tags=['blog'])

@router.get('/',response_model=List[schemas.showblog])
def all(db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
     return blog.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.create(request,db)

@router.get('/{id}',status_code=200,response_model=schemas.showblog,)
def show(id:int,response:Response,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    blogshow=db.query(module.Blog).filter(module.Blog.id==id).first()
    if not blogshow:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='the item is not found')
    return blogshow


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id ,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.delete(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)





