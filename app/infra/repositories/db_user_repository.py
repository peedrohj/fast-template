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
        user = UserModel(name=user.name, email=user.email)
        session.add(user)
        session.flush()

        return User(**user.to_dict())

    def find(self, id: int, session: Session = next(get_session())) -> User:
        user = session.scalars(select(User).where(UserModel.id == id)).one()
        return User(**user.to_dict())

    def delete(self, id: int, session: Session = next(get_session())) -> None:
        user = session.scalars(select(User).where(UserModel.id == id)).one()
        session.delete(user)
        session.flush()
