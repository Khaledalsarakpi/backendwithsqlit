import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import blog.module
from blog.schemas import Blog
from blog.database import engine,SessionLocal,get_db
from blog.module import  Base
from sqlalchemy.orm import Session
from .routers import bloger,users,login

app=FastAPI()
app.include_router(login.router)
app.include_router(bloger.router)
app.include_router(users.router)
Base.metadata.create_all(engine)







