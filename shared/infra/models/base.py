import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class BaseModel:
    __abstract__ = True

    id: Mapped[int] = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )

    created_at: Mapped[datetime] = Column(
        DateTime, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = Column(
        DateTime, nullable=True, onupdate=func.now()
    )
    deleted_at: Mapped[datetime] = Column(DateTime, nullable=True)
    archived_at: Mapped[datetime] = Column(DateTime, nullable=True)
