from typing import Union
from datetime import datetime
from beanie import Document


class Dialog(Document):
    id: str
    user_id: str
    model_id: str
    completionOptions: dict[Union[str, int], Union[str, bool, int]]
    created_at: datetime
    updated_at: datetime
    messages: dict[str, Union[str, bool, int]]
    evaluation: str
