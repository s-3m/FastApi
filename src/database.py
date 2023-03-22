from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

engine = create_async_engine('postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/postgres', future=True, echo=True)

async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db():
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()


Base = declarative_base()
