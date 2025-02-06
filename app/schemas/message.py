from beanie import Document
from datetime import datetime
from pydantic import Field
from typing import Optional


class Message(Document):
    dialog_id: Optional[str]
    author: str
    text: str
    created_at: datetime = Field(default_factory=datetime.now)
