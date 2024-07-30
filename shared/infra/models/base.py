from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, func
from sqlalchemy.orm import Mapped

from setup.db.config import BASE


class BaseModel(BASE):
    __abstract__ = True

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)

    created_at: Mapped[datetime] = Column(
        DateTime, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = Column(
        DateTime, nullable=True, onupdate=func.now()
    )
    deleted_at: Mapped[datetime] = Column(DateTime, nullable=True)
    archived_at: Mapped[datetime] = Column(DateTime, nullable=True)

    def to_dict(self):
        return {
            'id': str(self.id),
            'created_at': self.created_at or None,
            'updated_at': self.updated_at or None,
            'deleted_at': self.deleted_at or None,
            'archived_at': self.archived_at or None,
        }
