from beanie import Document
from pydantic import Field


class User(Document):
    name: str
    role: str
    email: str = Field(unique=True)
