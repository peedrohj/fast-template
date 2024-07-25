from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(init=True, slots=True, kw_only=True)
class BaseEntity:
    id: str | None = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    archived_at: Optional[datetime] = None
