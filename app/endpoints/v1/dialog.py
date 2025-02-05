from fastapi import APIRouter, HTTPException
from app.services.dialog import DialogService
from app.schemas import Dialog
from typing import Annotated
# from app.repo.session import client
router = APIRouter(tags=["Dialogs"])


@router.get('/dialogs')
async def get_dialogs() -> list[dict]:
    service = DialogService()
    return await service.read_many()


@router.get('/dialogs/{dialog_id}')
async def get_dialog(id: str):
    service = DialogService()
    return await service.read_one(id)

@router.post('/dialogs', response_model=Dialog)
async def post_dialog(dialog: Dialog) -> Dialog:
    try:
        new_dialog = DialogService()
        await new_dialog.create_dialog(dialog_data=dialog.dict())

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return new_dialog
