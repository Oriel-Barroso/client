from sqlalchemy import func
from sqlalchemy.sql.sqltypes import TIMESTAMP
from datetime import datetime, timezone
import uuid
from sqlalchemy.orm import MappedAsDataclass, DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(DeclarativeBase):
    __abstract__ = True


class BaseEntity(AsyncAttrs, MappedAsDataclass, Base, kw_only=True):
    __abstract__ = True
    created: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.current_timestamp(),
        init=False,
    )
    updated: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=True),
        default=None,
        onupdate=lambda: datetime.now(tz=timezone.utc),
        init=False,
    )

    is_deleted: Mapped[bool] = mapped_column(
        index=True,
        default=False,
    )

    def mark_deleted(self) -> None:
        self.is_deleted = True


class User(BaseEntity):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        init=False,
        server_default=func.gen_random_uuid(),
    )
    name: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
