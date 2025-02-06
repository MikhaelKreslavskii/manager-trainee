from typing import Any
from app.schemas.message import Message


class MessageService:
    async def read_many(self, **kwargs: Any) -> list[Message]:
        messages = await Message.find_all().to_list()
        return messages

    async def read_one(self, message_id: str) -> Message:
        message = await Message.get(document_id=message_id)
        return message

    async def create_message(self, message_data: dict) -> Message:
        message = Message(**message_data)
        await message.insert()
        return message
