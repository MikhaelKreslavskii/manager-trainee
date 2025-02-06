from fastapi import APIRouter
from .v1 import dialog, message, scenario, client, user

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(dialog.router)
v1_router.include_router(message.router)
v1_router.include_router(user.router)
v1_router.include_router(scenario.router)
v1_router.include_router(client.router)
