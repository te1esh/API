
"""
It is my first API by FastAPI
It contains several endpoints 'get' and one 'post'

for use, you can run in terminal on your host:
pip install -m uvicorn    # install module uvicorn
uvicorn app:app --reload --port 8000   # run web server on port 8000
"""

import datetime

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor


# class for Validate endpoint get /post/{id}
class PostResponse(BaseModel):
    id: int
    text: str
    topic: str

    class Config:   # for use syntactic dot (.)
        orm_mode = True


# create object app from class fastAPI
app = FastAPI()


def get_db() -> psycopg2.connect:  # create function for database connection str
    conn = psycopg2.connect(
        "postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml",
        cursor_factory=RealDictCursor
    )
    return conn


# endpoint return info about post from database Postgresql
@app.get("/post/{id}", response_model=PostResponse)  # validate for class PostResponse
def getuser(id, db=Depends(get_db)) -> PostResponse:  # return object type of PostResponse
    with db.cursor() as cursor:  # cursor is object for get data from db PostgreSQL
        cursor.execute("""                   
        SELECT *
        FROM "post"
        WHERE id = %s
        """, (id,))
        results = cursor.fetchone()
    if results is None:
        raise HTTPException(404, "user not found")
    else:
        return PostResponse(**results)


class User(BaseModel):  # create class User
    name: str
    surname: str
    age: int
    registration_date: datetime.date

    class Config:
        orm_mode = True


# endpoint for model add user
@app.post("/user/validate")
def validate1(user: User):
    return f"Will add user: {user.name} {user.surname} with age {user.age}"


# endpoint return sum date
@app.get("/sum_date1")
def sum(current_date: datetime.date, offset: int) -> datetime.date:
    return current_date + datetime.timedelta(days=offset)
