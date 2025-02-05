from beanie import Document


class Client(Document):
    id: str
    prompt: str
    type: str
