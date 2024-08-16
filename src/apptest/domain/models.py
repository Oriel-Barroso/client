from dataclasses import dataclass
from datetime import datetime
import uuid


@dataclass(frozen=True, kw_only=True)
class _DTTimestamps:
    created: datetime
    updated: datetime | None

@dataclass(frozen=True, kw_only=True)
class UserDomain(_DTTimestamps):
    id: uuid.UUID
    name: str
    email: str