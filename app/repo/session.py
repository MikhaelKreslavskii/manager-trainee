from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from dotenv import load_dotenv
import os
from app.schemas import Client, Scenario, User, Message, Dialog

# Подгружаем переменные окружения
load_dotenv()
DB_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME")
DB_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
DB_PORT = os.getenv("MONGO_PORT")
DB_URL = os.getenv("DB_URL")

client: AsyncIOMotorClient = None


async def init_db():
    global client
    client = AsyncIOMotorClient(DB_URL.format(DB_USER, DB_PASSWORD, DB_PORT))

    # Выбираем БД "app_database"
    db = client.app_database

    # Инициализируем Beanie ODM с выбранной БД и списком моделей
    await init_beanie(database=db, document_models=[Client, Scenario, User, Message, Dialog])

