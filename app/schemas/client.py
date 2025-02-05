from beanie import Document


class Client(Document):
    prompt: str
    type: str
