from beanie import Document


class Token(Document):
    access_token: str
    token_type: str

class TokenData(Document):
    username: str | None = None