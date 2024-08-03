from fastapi import APIRouter
from config.database import conn
from models.users import users

user = APIRouter()

@user.get("/users")
def users():
    return conn.execute(users.select()).fetchall()

@user.post("/users")
def hello_world():
    return {"Hello World"}

@user.put("/users")
def hello_world():
    return {"Hello World"}

@user.delete("/users")
def hello_world():
    return {"Hello World"}
