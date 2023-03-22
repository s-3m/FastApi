import uuid
from typing import Optional

from pydantic import BaseModel, EmailStr, BaseSettings, Field
from fastapi_users import schemas, models


class UserRead(schemas.BaseUser[uuid.UUID]):
    name: str
    surname: str

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    name: str
    surname: str
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
