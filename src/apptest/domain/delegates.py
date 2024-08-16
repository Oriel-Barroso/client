from .repository import UserRepositoryInterface
from .models import UserDomain
import uuid

class UserDelegate(UserRepositoryInterface):
    def __init__(self, repository: UserRepositoryInterface):
        super().__init__()
        self.repository = repository

    async def create_user(self, name: str, email: str) -> UserDomain:
        return await self.repository.create_user(name, email)
    
    async def get_user(self, user_id: uuid.UUID) -> UserDomain:
        return await self.repository.get_user(user_id)

    async def update_user(self, user_id: uuid.UUID, name: str, email: str) -> UserDomain:
        return await self.repository.update_user(user_id, name, email)
    
    async def delete_user(self, user_id: uuid.UUID) -> bool:
        return await self.repository.delete_user(user_id)
    
    async def get_users(self) -> list[UserDomain]:
        return await self.repository.get_users()