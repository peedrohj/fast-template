from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.infra.models.user import UserModel
from setup.db.session import get_session


class DbUserRepository(UserRepository):
    def list(
        self,
        session: Session = next(get_session()),
        offset: int = 0,
        limit: int = 10,
    ) -> List[User]:
        users = session.scalars(
            select(UserModel).offset(offset).limit(limit)
        ).all()

        return [User(**user.to_dict()) for user in users]

    def save(self, user: User, session: Session = next(get_session())) -> User:
        return super().save(user, session)

    def find(self, id: int, session: Session = next(get_session())) -> User:
        return super().find(id, session)

    def delete(self, id: int, session: Session = next(get_session())) -> None:
        return super().delete(id, session)
