from typing import Protocol
from .models import UserDomain
import uuid

class UserRepositoryInterface(Protocol):
    def get_user(self, user_id: uuid.UUID) -> UserDomain:
        ...

    def create_user(self, name: str, email: str) -> UserDomain:
        ...

    def update_user(self, user_id: uuid.UUID, name: str, email: str) -> UserDomain:
        ...

    def delete_user(self, user_id: uuid.UUID) -> bool:
        ...

    def get_users(self) -> list[UserDomain]:
        ...
