import pydantic
from datetime import datetime


class _Base(pydantic.BaseModel):
    created: datetime = datetime.now()
    updated: datetime | None


class UserSchema(pydantic.BaseModel):
    name: str | None
    email: str

class UserResponseSchema(UserSchema):
    id: int
    created: datetime = datetime.now()
    updated: datetime | None