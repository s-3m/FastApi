import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter
from starlette.staticfiles import StaticFiles

from auth.config import auth_router, register_router
from tasks.routers import task_router
from pages.router import page_router

app = FastAPI(title='My first fastAPI app')

app.mount("/static", StaticFiles(directory='static'), name='static')

main_router = APIRouter()
app.include_router(main_router)
app.include_router(auth_router, prefix="/auth/jwt", tags=["auth"],)
app.include_router(register_router, prefix="/auth", tags=["auth"],)
app.include_router(task_router)
app.include_router(page_router, prefix='/page', tags=['page'],)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
