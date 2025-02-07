from beanie import Document
from pydantic import Field


class User(Document):
    name: str
    role: str
    email: str = Field(unique=True)
    hashed_password:str


class UserCreate(Document):
    name:str
    email:str
    role:str
    password:str

