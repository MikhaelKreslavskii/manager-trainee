from pydantic import BaseModel


class Client(BaseModel):
    id: str
    prompt: str
    type: str
