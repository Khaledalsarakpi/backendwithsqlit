from sqlalchemy.orm import Session
from ..schemas import Blog
from .. import module
def get_all(db:Session):
    blogs = db.query(module.Blog).all()
    return blogs


def create(request:Blog,db:Session):
    new_blog = module.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id ,db:Session):
    blogitem = db.query(module.Blog).filter(module.Blog.id == id);
    if not blogitem.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'blog with thes item is not avaible {id} not found')
    blogitem.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id,request:Blog,db:Session):
    blogitem=db.query(module.Blog).filter(module.Blog.id==id);
    if not blogitem.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with thes item is not avaible {id} not found')
    blogitem.update(request.dict())
    db.commit()
    return 'update'