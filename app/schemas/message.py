from pydantic import BaseModel
from datetime import datetime


class Message(BaseModel):
    id: str
    dialog_id: str
    author: str
    text: str
    created_at: datetime
