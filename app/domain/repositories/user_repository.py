from abc import ABC, abstractmethod

from app.domain.entities.user import User
from shared.domain.repositories.base_repository import PaginatedResponse


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User, session: any = None) -> User: ...

    @abstractmethod
    def list(
        self, session: any = None, offset: int = 0, limit: int = 10
    ) -> PaginatedResponse[User]: ...

    @abstractmethod
    def find(self, user_id: int, session: any = None) -> User: ...

    @abstractmethod
    def delete(self, user_id: int, session: any = None) -> None: ...
