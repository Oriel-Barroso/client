from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
)


@asynccontextmanager
async def get_session(
    factory: async_sessionmaker[AsyncSession] | async_scoped_session[AsyncSession],
    *,
    in_transaction: bool = False,
) -> AsyncGenerator[AsyncSession, None]:
    match factory:
        case async_sessionmaker():
            if in_transaction:
                contextmanager = factory.begin()
            else:
                contextmanager = factory()
            async with contextmanager as session:
                yield session
        case async_scoped_session():
            session = factory()
            if in_transaction and not session.in_transaction():
                async with session.begin():
                    yield session
            else:
                yield session


class WithSessionMixin:
    __slots__ = ("_session",)

    def __init__(
        self,
        session: (
            async_sessionmaker[AsyncSession]
            | async_scoped_session[AsyncSession]
            | AsyncSession
        ),
    ) -> None:
        self._session = session

    @asynccontextmanager
    async def get_session(
        self, *, in_transaction: bool = False
    ) -> AsyncGenerator[AsyncSession, None]:
        match self._session:
            case AsyncSession() as session:
                if in_transaction and not session.in_transaction():
                    async with session.begin():
                        yield session
                else:
                    yield session
            case _:
                async with get_session(
                    self._session, in_transaction=in_transaction
                ) as session:
                    yield session