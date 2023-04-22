from fastapi import Depends
from database.session import get_db, create_db_and_tables

from sqlmodel import Session
from models.users import User, UserModel

from controllers.users import create_user, get_user
from core.config import app


@app.post("/users", status_code=201)
async def create_user_endpoint(usermodel: UserModel, db: Session =  Depends(get_db)):
    return await create_user(usermodel=usermodel, db=db)

@app.get("/users/{user_id}", status_code=200)
async def get_user_by_id_endpoint(user_id: int, db:Session = Depends(get_db)):
    return await get_user(user_id=user_id, db=db)


@app.get("/")
async def root():
    return {"message": "booted up!"}


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
