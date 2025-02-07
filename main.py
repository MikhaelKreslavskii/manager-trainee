from fastapi import FastAPI, APIRouter
from app.repo.session import init_db
from app.endpoints import v1_router

app = FastAPI()
app.include_router(v1_router)


@app.on_event("startup")
async def on_startup():
    # Инициализируем подключение к Монго и Beani при старте приложения
    await init_db()

