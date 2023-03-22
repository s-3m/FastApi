from datetime import datetime
from typing import List

from sqlalchemy import Column, String, MetaData, Table, Integer, TIMESTAMP, Boolean
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from sqlalchemy.orm import relationship, Mapped, declarative_base, DeclarativeBase
from database import get_db
from database import Base
from tasks.models import Task


class User(SQLAlchemyBaseUserTableUUID, Base):
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    tasks = relationship("Task", backref="user")

    def __repr__(self):
        return f"{self.surname} {self.name}"


async def get_user_db(session: AsyncSession = Depends(get_db)):
    yield SQLAlchemyUserDatabase(session, User)



