from sqlalchemy import Column, String

from shared.infra.models.base import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'users'

    name = Column(String)
    email = Column(String)

    def to_dict(self):
        return {
            **super().to_dict(),
            'name': self.name,
            'email': self.email,
        }
