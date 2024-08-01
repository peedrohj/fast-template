from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from setup.db.session import get_session


class CreateUser:
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def execute(self, user: User) -> User:
        session = next(get_session())

        try:
            user = self.__user_repository.save(user=user, session=session)
        except Exception as err:
            session.rollback()
            return err
        finally:
            session.commit()

        return user
