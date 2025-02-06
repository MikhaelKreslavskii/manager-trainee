from typing import Union
from fastapi import APIRouter, HTTPException
from app.services.message import MessageService
from app.schemas.message import Message

router = APIRouter(tags=["Messages"])


@router.post('/messages', response_model=Message)
async def create_message(message_data: Message):
    try:
        service = MessageService()
        message = await service.create_message(message_data=message_data.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return message


@router.get('/messages')
async def get_messages() -> list[Message]:
    try:
        service = MessageService()
        return await service.read_many()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/messages/{message_id}')
async def get_messages(message_id: str) -> Message:
    try:
        service = MessageService()
        message = await service.read_one(message_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return message
