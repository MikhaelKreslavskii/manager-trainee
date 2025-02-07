from fastapi import FastAPI
from app.repo.session import init_db
from app.endpoints import v1_router
from app.repo.migrate import migrate_initial_data


app = FastAPI()
app.include_router(v1_router)


@app.on_event("startup")
async def on_startup():
    # Инициализируем подключение к Монго и Beani при старте приложения и проверяем дефолтные документы в коллекциях
    await init_db()
    await migrate_initial_data("./initial_data.json")
