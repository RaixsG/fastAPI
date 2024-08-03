from fastapi import APIRouter
from config.database import conn
from models.users import users
from schema.users import UserGet, UserCreate
from fastapi.responses import Response

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()

@user.get("/users")
def get_users():
    result = conn.execute(users.select()).fetchall()
    return Response(result, status_code=200)

@user.post("/users")
def create_user(user: UserCreate):
    new_user = {
        "name": user.name,
        "email": user.email,
        "password": f.encrypt(user.password.encode('utf-8'))
    }
    result = conn.execute(users.insert().values(new_user))
    print(result.lastrowid)
    return Response(result, status_code=201)

@user.put("/users")
def hello_world():
    return {"Hello World"}

@user.delete("/users")
def hello_world():
    return {"Hello World"}
