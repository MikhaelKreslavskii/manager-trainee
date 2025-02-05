from fastapi import APIRouter
from .v1 import dialog

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(dialog.router)
