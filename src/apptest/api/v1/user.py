from fastapi import APIRouter
from ...dependencies import UserDelegateDependency
from .schemas import UserResponseSchema, UserSchema

router = APIRouter()


@router.get("/users")
async def get_users(user_dependency: UserDelegateDependency) -> list[UserResponseSchema]:
    return await user_dependency.get_users()


@router.post("/users")
async def create_user(
    user_dependency: UserDelegateDependency, user_data: UserSchema
) -> UserResponseSchema:
    return await user_dependency.create_user(name=user_data.name, email=user_data.email)
