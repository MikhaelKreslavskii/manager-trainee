from typing import Any, Optional, Union
from app.schemas.user import User


class UserService:
    async def create_user(self, user_data: dict) -> User:
        user = User(**user_data)
        await user.insert()
        return user

    async def read_one(self, user_id: Optional[str] = None, user_name: Optional[str] = None) -> User:
        if user_id:
            user = await User.get(document_id=user_id)
        else:
            user = await User.find_one(User.name == user_name)
        print(user)
        return user

    async def read_many(self, **kwargs: Any) -> Union[list[User], None]:
        users = await User.find_all().to_list()
        return users
