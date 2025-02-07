from datetime import datetime
from beanie import Document
from pydantic import Field
from typing import Optional


class Dialog(Document):
    user_id: str
    scenario_id: str
    client_id: str
    messages: Optional[list[str]]
    evaluation: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
