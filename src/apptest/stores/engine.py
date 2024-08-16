from asyncio import current_task
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)

from ...apptest.config import settings

from . import utils

engine = create_async_engine(
    settings.database.get_db_url(),
    pool_pre_ping=True,
)

SessionLocal = async_sessionmaker(engine, expire_on_commit=True)
session = async_scoped_session(SessionLocal, current_task)


@asynccontextmanager
async def get_session(
    *, in_transaction: bool = False
) -> AsyncGenerator[AsyncSession, None]:
    s = None
    try:
        async with utils.get_session(session, in_transaction=in_transaction) as s:
            yield s
    finally:
        if s is not None:
            await s.close()