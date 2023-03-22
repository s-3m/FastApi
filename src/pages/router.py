from asyncio import sleep
from sse_starlette.sse import EventSourceResponse

from fastapi import APIRouter, Request, Depends, responses
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from auth.config import current_user
from auth.models import User
from database import get_db
from tasks.models import Task

page_router = APIRouter()

templates = Jinja2Templates(directory='templates')


class Note:
    flag = False

    @classmethod
    def set_flag(cls, position):
        cls.flag = position


@page_router.get('/todo')
async def get_page(request: Request, db: AsyncSession = Depends(get_db)):
    stmt = select(Task)
    tasks_list = [task for task in await db.scalars(stmt)]

    return templates.TemplateResponse('todo.html', {'request': request, 'tasks': tasks_list})

@page_router.get('/todo1')
async def get_page(request: Request, db: AsyncSession = Depends(get_db)):
    stmt = select(Task)
    tasks_list = [task for task in await db.scalars(stmt)]

    return templates.TemplateResponse('todo1.html', {'request': request, 'tasks': tasks_list})


@page_router.get('/todo/add')
async def add_todo(request: Request):
    Note.set_flag(False) if Note.flag else Note.set_flag(True)


@page_router.get('/stream')
def stream(request: Request):

    async def event_generator():
        while True:
            # If client closes connection, stop sending events
            if await request.is_disconnected():
                break

            # Checks for new messages and return them to client if any
            if Note.flag:
                yield {
                    "event": "new_message",
                    "id": "message_id",
                    "retry": 15000,
                    "data": 'Новая запись в БД!!!'
                }
                Note.set_flag(False)

            await sleep(2)

    return EventSourceResponse(event_generator())
