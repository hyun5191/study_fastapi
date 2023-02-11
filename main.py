from enum import Enum
from typing import Optional

from fastapi import Depends, FastAPI
from mysqlx import Session
from pydantic import BaseModel

from database import crud, models
from database.conn import engine, local_session

class data(BaseModel):
    username: str
    password: str
    full_name: Optional[str] = None

app = FastAPI()
models.base.metadata.create_all(bind=engine)

def get_db():
    db = local_session()

    try:
        yield db
    finally:
        db.close()

class name(str, Enum):
    name1 = "test1"
    name2 = "test2"
    name3 = "test3"

@app.post("/datas/", response_model=data)
async def user(user: data, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user.username)

    if db_user:
        return user
    else:
        crud.create_user(db=db, user=user, datatype=user)
        return {"sa=tatus": "successfully generated"}

@app.post("/datas/", response_model=data)
async def user(user: data):
    return user

@app.get("/")
async def main():
    return {"message": "Hello, world!"}

@app.get("/data/{item_id}")
async def items(item_id):
    return {"item id": item_id}

@app.get("/data2/{names}")
async def is_name(names):
    if names == name.name1:
        return {"first name": names, "message": "test 1"}
    if names == name.name2:
        return {"second name": names, "message": "test 2"}
    else:
        return {"extra": names, "message": "test 3"}