from typing import Any
from app.schemas.client import Client


class ClientService:
    async def create_client(self, client_data: dict) -> Client:
        client = Client(**client_data)
        await client.insert()
        return client

    async def read_one(self, client_id: str) -> Client:
        client = await Client.get(document_id=client_id)
        return client

    async def read_many(self, **kwargs: Any) -> list[Client]:
        clients = await Client.find_all().to_list()
        return clients
