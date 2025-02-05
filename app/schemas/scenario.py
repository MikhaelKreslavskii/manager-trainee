from beanie import Document


class Scenario(Document):
    id: str
    prompt: str
    name: str
