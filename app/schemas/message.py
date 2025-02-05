from beanie import Document
from datetime import datetime
from pydantic import Field


class Message(Document):
    dialog_id: str
    author: str
    text: str
    created_at: datetime = Field(default_factory=datetime.now)
