from uuid import UUID
from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import DateTime


class TaskCreate(BaseModel):
    title: str
    text: str
    user_id: UUID


class TaskRead(BaseModel):
    id: int
    title: str
    text: str
    user_id: UUID
    create: datetime
    is_finished: bool
