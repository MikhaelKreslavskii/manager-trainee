from fastapi import FastAPI, APIRouter
from app.repo.session import init_db
from app.endpoints import v1_router

app = FastAPI()
app.include_router(v1_router)


@app.on_event("startup")
async def on_startup():
    # Инициализируем подключение к Монго и Beani при старте приложения
    await init_db()


@app.get('/health')
async def get_health() -> dict:
    return {"status": "Ok"}


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str) -> dict[str, str]:
    return {"message": f"Hello {name}"}
