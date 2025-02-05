from pydantic import BaseModel


class Scenario(BaseModel):
    id: str
    prompt: str
    name: str
