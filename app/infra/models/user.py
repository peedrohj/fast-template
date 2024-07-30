from sqlalchemy import Column, String

from shared.infra.models.base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    name = Column(String)
    email = Column(String)
