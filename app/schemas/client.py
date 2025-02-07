from beanie import Document


class Client(Document):
    name: str
    prompt: str
    type: str
    name: str
