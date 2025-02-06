from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.endpoints import v1_router

from app.repo.session import init_db

app = FastAPI()
app.include_router(v1_router, prefix="/api")


@app.on_event("startup")
async def on_startup():
    # Инициализируем подключение к Монго и Beani при старте приложения
    await init_db()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)
