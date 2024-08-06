from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.infra.models.user import UserModel
from shared.domain.repositories.base_repository import (
    BaseRepository,
    PaginatedResponse,
    PaginationProps,
)


class DbUserRepository(UserRepository, BaseRepository[User]):
    def list(
        self,
        session: Session,
        offset: int = 0,
        limit: int = 10,
    ) -> PaginatedResponse[User]:
        users = session.scalars(
            select(UserModel).offset(offset).limit(limit)
        ).all()

        total_records = session.scalar(select(func.count(UserModel.id)))
        pagination = PaginationProps(
            current_page=int(offset / limit) + 1,
            total_records=total_records,
            total_pages=int(total_records / limit) + 1,
            page_size=limit,
        )
        return self._paginate_response(
            data=[User(**user.to_dict()) for user in users],
            pagination=pagination,
        )

    def save(self, user: User, session: Session) -> User:
        created_user = UserModel(name=user.name, email=user.email)

        if user.password:
            created_user.password = user.password

        session.add(created_user)
        session.flush()

        return User(**created_user.to_dict())

    def update(self, user: User, session: Session) -> User:
        updated_user = session.scalars(
            select(UserModel).where(UserModel.id == user.id)
        ).one()

        if user.email:
            updated_user.email = user.email

        if user.name:
            updated_user.name = user.name

        session.add(updated_user)
        session.flush()

        return User(**updated_user.to_dict())

    def find(self, user_id: int, session: Session) -> User:
        user = session.scalars(
            select(UserModel).where(UserModel.id == user_id)
        ).one()
        return User(**user.to_dict())

    def delete(self, user_id: int, session: Session) -> None:
        user = session.scalars(
            select(UserModel).where(UserModel.id == user_id)
        ).one()
        session.delete(user)
        session.flush()
