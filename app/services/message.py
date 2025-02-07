from typing import Any
from app.schemas.message import Message


class MessageService:
    async def read_many(self, dialog_id: str, **kwargs: Any) -> list[Message]:
        messages = await Message.find(Message.dialog_id == dialog_id).to_list()
        return messages

    async def read_one(self, message_id: str) -> Message:
        message = await Message.get(document_id=message_id)
        return message

    async def create_message(self, message_data: dict, dialog_id: str) -> Message:
        message_data["dialog_id"] = dialog_id
        message = Message(**message_data)
        await message.insert()
        return message
