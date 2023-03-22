import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from tasks.schemas import TaskCreate, TaskRead
from tasks.models import Task

task_router = APIRouter(prefix='/task', tags=['task'])


@task_router.post('/create', response_model=TaskRead)
async def create_task(body: TaskCreate, db: AsyncSession = Depends(get_db)):

    new_task = Task(title=body.title, text=body.text, user_id=body.user_id)
    async with db.begin():
        db.add(new_task)
        await db.flush()
        return TaskRead(id=new_task.id,
                        title=new_task.title,
                        text=new_task.text,
                        user_id=new_task.user_id,
                        create=new_task.create,
                        is_finished=new_task.is_finished)
