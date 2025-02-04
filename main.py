import traceback

from fastapi import FastAPI, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from starlette import status
from starlette.responses import JSONResponse

from app.endpoints import v1_router

app = FastAPI()
app.include_router(v1_router, prefix="/api")
@app.get('/health')
async def get_health() -> dict:
    return {"status": "OK"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def internal_server_error_handler(request: Request, exc: Exception) -> JSONResponse:
    traceback.print_exc("Internal server error.")
    print("Internal server error.", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={'detail': "Internal Server Error"},
    )
