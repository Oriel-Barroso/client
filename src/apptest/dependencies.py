from .stores.repository import UserRepository, SqlalchemyRepositoryFactory
import fastapi
import typing
from sqlalchemy.ext.asyncio import AsyncSession
from .stores.engine import get_session
from .domain.repository import UserRepositoryInterface
from .domain.delegates import UserDelegate

async def _get_session(
    request: fastapi.Request,
    background_tasks: fastapi.BackgroundTasks,
) -> typing.AsyncGenerator[AsyncSession, None]:
    async with get_session(
        in_transaction=request.method.lower() not in ("get", "head", "options")
    ) as session:
        yield session


Session = typing.Annotated[AsyncSession, fastapi.Depends(_get_session)]


def _get_user_repository(session: Session) -> UserRepositoryInterface:
    return UserRepository(session)

UserDependency = typing.Annotated[UserRepositoryInterface, fastapi.Depends(_get_user_repository)]

def _get_user_delegate(user_dependency: UserDependency) -> UserDelegate:
    return UserDelegate(user_dependency)

UserDelegateDependency = typing.Annotated[UserDelegate, fastapi.Depends(_get_user_delegate)]