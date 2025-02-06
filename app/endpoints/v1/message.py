from typing import Union
from fastapi import APIRouter, HTTPException
from app.services.message import MessageService
from app.schemas.message import Message

router = APIRouter(tags=["Messages"])


@router.post('/dialogs/{dialog_id}/messages', response_model=Message)
async def create_message(message_data: Message, dialog_id: str):
    try:
        service = MessageService()
        message = await service.create_message(message_data=message_data.dict(), dialog_id=dialog_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return message


@router.get('/dialogs/{dialog_id}/messages')
async def get_messages(dialog_id: str) -> list[Message]:
    try:
        service = MessageService()
        return await service.read_many(dialog_id=dialog_id)
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
