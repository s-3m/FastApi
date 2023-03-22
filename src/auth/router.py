# from fastapi import APIRouter, Depends
# from sqlalchemy.ext.asyncio import AsyncSession
# from src.auth.schemas import ShowUser, UserCreate
# from src.database import get_db
# from src.auth.dals import UserDAL
#
# user_router = APIRouter(prefix='/user', tags=['user'])
#
#
# async def _create_new_user(body: UserCreate, db) -> ShowUser:
#     async with db as session:
#         async with session.begin():
#             user_dal = UserDAL(session)
#             user = await user_dal.create_user(name=body.name,
#                                               surname=body.surname,
#                                               email=body.email)
#
#             return ShowUser(id=user.id,
#                             name=user.name,
#                             surname=user.surname,
#                             email=user.email,
#                             is_active=user.is_active)
#
#
# @user_router.post('/', response_model=ShowUser)
# async def create_user(body: UserCreate, db: AsyncSession = Depends(get_db)) -> ShowUser:
#     return await _create_new_user(body, db)
