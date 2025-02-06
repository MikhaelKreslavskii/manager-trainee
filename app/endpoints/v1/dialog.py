from fastapi import APIRouter, HTTPException
from app.services.dialog import DialogService
from app.schemas import Dialog
router = APIRouter(tags=["Dialogs"])


@router.get('/dialogs')
async def get_dialogs() -> list[Dialog]:
    service = DialogService()
    dialogs = await service.read_many()
    return dialogs


@router.get('/dialogs/{dialog_id}')
async def get_dialog(dialog_id: str) -> Dialog:
    service = DialogService()
    dialog = await service.read_one(dialog_id)
    return dialog


@router.post('/dialogs', response_model=Dialog)
async def post_dialog(dialog: Dialog) -> Dialog:
    try:
        service = DialogService()
        dialog = await service.create_dialog(dialog_data=dialog.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return dialog


@router.get('/dialogs/users/{user_id}')
async def get_user_dialogs(user_id):
    try:
        service = DialogService()
        dialogs = await service.read_user_dialog(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    if dialogs is None:
        raise HTTPException(status_code=404, detail="There aren't dialogs")
    return dialogs

import os

from fastapi import APIRouter, Path

from typing import List
import requests
import json
from dotenv import load_dotenv
from pydantic import BaseModel

router = APIRouter(tags=['Dialog'])


class Message(BaseModel):
    role: str
    content: str


class Messages(BaseModel):
    messages: List[Message]


@router.post('/sendMessage/')
async def sendMessage(messages: List[Message]):
    try:
        load_dotenv()
        GIGA_TOKEN = os.getenv("GIGA_TOKEN")
        RqUID = os.getenv("RqUID")

        url_token = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

        payload = {
            'scope': 'GIGACHAT_API_PERS'
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'RqUID': RqUID,
            'Authorization': f'Basic {GIGA_TOKEN}'
        }

        response_token = requests.request("POST", url_token, headers=headers, data=payload, verify=False)
        token = response_token.json()['access_token']
        print(token)
        url_resp = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
        messages_dict = [message.__dict__ for message in messages]
        # print(messages_dict)
        payload = {
            "model": "GigaChat",
            "messages": messages_dict
        }

        payload_json = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.request("POST", url_resp, headers=headers, data=payload_json, verify=False)
        print(response.json())
        return response.json()
    except Exception as e:
        return {
            "status": 500,
            "error": str(e)
        }

