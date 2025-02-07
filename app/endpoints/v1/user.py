from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from app.schemas.user import User
from app.services.user import UserService


router = APIRouter(tags=["Users"])


@router.get('/users')
async def get_users() -> list[User]:
    try:
        service = UserService()
        users = await service.read_many()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    return users


@router.get('/user')
async def get_user(user_id: Optional[str] = Query(None), user_name: Optional[str] = Query(None)) -> User:
    if (user_id is None and user_name is None) or (user_id is not None and user_name is not None):
        raise HTTPException(status_code=400, detail="Specify only one parameter: user_id OR user_name")
    try:
        service = UserService()
        user = await service.read_one(user_id, user_name)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    if user is None:
        raise HTTPException(status_code=404, detail='The user has not been found')
    return user


@router.post('/users', response_model=User)
async def create_user(user_data: User):
    try:
        service = UserService()
        user = await service.create_user(user_data=user_data.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    return user
