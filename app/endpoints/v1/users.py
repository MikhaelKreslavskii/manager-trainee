import os

from fastapi import APIRouter, Path, HTTPException, Depends

from typing import List, Annotated
import requests
import json
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from app.schemas.token import Token
from app.schemas.user import UserCreate, User
from app.services.user import UserService
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from app.services.user import UserService as user_utils
from app.services.auth import AuthService as auth_utils



router = APIRouter(tags=['User'])



@router.post('/users/register', response_model=User)
async def create_user(user:UserCreate):
    try:
        service = UserService()
        print(user)
        user = await service.create_user(user=user.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user




@router.get("/users/me", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(user_utils.get_current_user)]):
    return current_user



@router.post("/users/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.find_one({"email": form_data.username})

    service = UserService()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password"
        )
    user = user.dict()
    if not service.verify_password(plain_password=form_data.password, hashed_password=user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password"
        )

    access_token_data = {"sub": user["email"]}
    access_token = auth_utils.create_access_token(data=access_token_data)
    return {"access_token": access_token, "token_type": "bearer"}

