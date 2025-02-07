from beanie import Document


class Scenario(Document):
    prompt: str
    name: str
