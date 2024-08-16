from . import utils
from ..domain.repository import UserRepositoryInterface
from ..domain.models import UserDomain
from ..stores.models import User
from sqlalchemy.orm import query
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, async_scoped_session
from sqlalchemy import select


class SqlalchemyRepositoryFactory():
    def __init__(
        self,
        session: (
            async_sessionmaker[AsyncSession]
            | async_scoped_session[AsyncSession]
            | AsyncSession
        ),
    ) -> None:
        super().__init__()
        self._session = session

    def user_repository(self) -> UserRepositoryInterface:
        return UserRepository(self._session)

class UserRepository(utils.WithSessionMixin, UserRepositoryInterface):
    async def get_user(self, user_id: int) -> UserDomain:
        async with self.get_session() as session:
            user = session.get(UserDomain, user_id)
            match user:
                case None:
                    raise ValueError(f"User with id {user_id} not found")
                case _:
                    return user
    
    async def create_user(self, name: str, email: str) -> UserDomain:
        async with self.get_session(in_transaction=True) as session:
            item = User(
                name=name,
                email=email
            )
            async with session.begin_nested():
                session.add(item)
                await session.flush()

            return await session.run_sync(lambda _: map_user(item))
    
    async def update_user(self, user_id: int, name: str, email: str) -> UserDomain:
        async with self.get_session() as session:
            user = session.get(User, user_id)
            match user:
                case None:
                    raise ValueError(f"User with id {user_id} not found")
                case _:
                    async with session.begin_nested():
                        if name:
                            user.name = name
                        if email:
                            user.email = email
                        await session.flush()
                
            return await session.run_sync(map_user, user)
    
    async def delete_user(self, user_id: int) -> bool:
        async with self.get_session() as session:
            user = session.get(User, user_id)
            match user:
                case None:
                    return None
                case _:
                    user.mark_deleted()
                    await session.flush()
                    return True
            
    async def get_users(self) -> list[UserDomain]:
        async with self.get_session() as session:
            query_val = select(User).where(~User.is_deleted)
            users = await session.scalars(query_val)
            def transform_users(items: list[User]):
                return [map_user(user) for user in users]

            return await session.run_sync(lambda _: transform_users(users))


def map_user(user: User) -> UserDomain:
    return UserDomain(
        id=user.id,
        name=user.name,
        email=user.email,
        created=user.created,
        updated=user.updated
    )