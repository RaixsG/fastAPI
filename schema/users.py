from pydantic import BaseModel

class UserGet(BaseModel):
    id: int
    name: str
    email: str

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

