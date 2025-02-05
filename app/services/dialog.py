from typing import Any

from app.schemas.dialog import Dialog


class DialogService:
    async def read_many(self, **kwargs: Any) -> list[Dialog]:
        dialogs = await Dialog.all().to_list()
        print(dialogs)
        return dialogs

    async def read_one(self, id: str) -> Dialog:
        print(id)
        dialog = await Dialog.find_one({"id": id})
        print(dialog.dict())
        return dialog

    async def create_dialog(self, dialog_data: dict) -> Dialog:
        dialog = Dialog(**dialog_data)
        await dialog.insert()
        return dialog
