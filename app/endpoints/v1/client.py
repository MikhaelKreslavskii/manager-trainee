from fastapi import APIRouter, HTTPException
from app.schemas.client import Client
from app.services.client import ClientService


router = APIRouter(tags=["Request settings"])


@router.get('/clients')
async def get_clients() -> list[Client]:
    try:
        service = ClientService()
        clients = await service.read_many()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    return clients


@router.get('/clients/{client_id}')
async def get_client(client_id: str) -> Client:
    try:
        service = ClientService()
        client = await service.read_one(client_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    return client


@router.post('/clients', response_model=Client)
async def create_client(client_data: Client):
    try:
        service = ClientService()
        client = await service.create_client(client_data=client_data.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    return client
