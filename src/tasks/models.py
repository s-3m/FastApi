import uuid

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, MetaData, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base, DeclarativeBase
from sqlalchemy.sql import func

from database import Base

Base.metadata.clear()


class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    text: Mapped[str] = mapped_column(String)
    user_id: Mapped[uuid] = mapped_column(ForeignKey("user.id"))
    create: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=func.now())
    is_finished: Mapped[bool] = mapped_column(Boolean, default=False)
