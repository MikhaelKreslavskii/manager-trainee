from fastapi import APIRouter, HTTPException
from app.services.dialog import DialogService
from app.schemas import Dialog
from typing import Annotated
# from app.repo.session import client
router = APIRouter(tags=["Dialogs"])


@router.get('/dialogs')
async def get_dialogs() -> list[Dialog]:
    service = DialogService()
    dialogs = await service.read_many()
    return dialogs


@router.get('/dialogs/{dialog_id}')
async def get_dialog(id: str) -> Dialog:
    service = DialogService()
    dialog = await service.read_one(id)
    return dialog

@router.post('/dialogs', response_model=Dialog)
async def post_dialog(dialog: Dialog) -> Dialog:
    try:
        service = DialogService()
        dialog = await service.create_dialog(dialog_data=dialog.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return dialog
