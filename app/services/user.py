import jwt
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from starlette import status

from app.schemas import User
from typing import Union
from bson import ObjectId

# from app.schemas.user import UserInDB

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class UserService:

    async def read_many(self, **kwargs) -> Union[list, str]:
        users = await User.find_all().to_list()
        return users

    async def read_one(self, user_id: str) -> User:
        user = await User.get(ObjectId(user_id))
        return user

    async def create_user(self, user: dict) -> User:
        print("In create user")


        existing_user = await User.find_one({"email": user["email"]})
        print(existing_user)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        print('Not exist user')
        # Хеширование пароля
        hashed_password = pwd_context.hash(user["password"])

        # Создание нового пользователя
        new_user = {
            "name": '',
            "role": '',
            "email": user["email"],
            "hashed_password": hashed_password
        }
        user = User(**new_user)
        # Сохранение пользователя в базе данных
        await user.insert()

        return user

    async def get_current_user(token: str = Depends(oauth2_scheme)):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            print(f'Payload: {payload}')
            email: str = payload.get("sub")
            if email is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Could not validate credentials",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            user = await User.find_one({"email": email})
            if user is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Could not validate credentials",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            return user  # Return a User object
        except jwt.PyJWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

    def hash_password(self,password: str) -> str:
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

