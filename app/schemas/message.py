from beanie import Document
from datetime import datetime


class Message(Document):
    id: str
    dialog_id: str
    author: str
    text: str
    created_at: datetime
