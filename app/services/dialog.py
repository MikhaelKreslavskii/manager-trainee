from typing import Any
from app.schemas.dialog import Dialog


class DialogService:
    async def read_many(self, **kwargs: Any) -> list[Dialog]:
        dialogs = await Dialog.all().to_list()
        return dialogs

    async def read_one(self, id: str) -> Dialog:
        dialog = await Dialog.get(document_id=id)
        return dialog

    async def create_dialog(self, dialog_data: dict) -> Dialog:
        dialog = Dialog(**dialog_data)
        await dialog.insert()
        return dialog
