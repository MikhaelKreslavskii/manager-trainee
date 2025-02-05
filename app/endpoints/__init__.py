from fastapi import APIRouter
from .v1 import dialog, message

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(dialog.router)
v1_router.include_router(message.router)
