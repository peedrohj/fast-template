from abc import ABC

from app.domain.entities.user import User


class UserRepository(ABC):
    def save(self, user: User, session: any = None) -> User: ...
