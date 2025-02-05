from beanie import Document


class User(Document):
    id: str
    name: str
    role: str
    email: str
