from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from shared.domain.entities.session import DatabaseSession


class UpdateUser:
    def __init__(
        self, user_repository: UserRepository, session: DatabaseSession
    ):
        self.__user_repository = user_repository
        self.__session = session

    def execute(self, user: User) -> User:
        try:
            user = self.__user_repository.update(
                user=user, session=self.__session
            )
        except Exception as err:
            self.__session.rollback()
            raise err
        finally:
            self.__session.commit()

        return user
