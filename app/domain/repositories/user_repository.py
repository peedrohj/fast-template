from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User, session: any = None) -> User: ...

    @abstractmethod
    def list(self, session: any = None) -> List[User]: ...

    @abstractmethod
    def find(self, id: int, session: any = None) -> User: ...

    @abstractmethod
    def delete(self, id: int, session: any = None) -> None: ...
