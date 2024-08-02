from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from setup.security import pwd_context
from shared.domain.entities.session import DatabaseSession


class CreateUser:
    def __init__(
        self, user_repository: UserRepository, session: DatabaseSession
    ):
        self.__user_repository = user_repository
        self.__session = session

    def execute(self, user: User) -> User:
        user.password = self.__encrypt_password(user.password)

        try:
            user = self.__user_repository.save(
                user=user, session=self.__session
            )
        except Exception as err:
            self.__session.rollback()
            raise err
        finally:
            self.__session.commit()

        return user

    def __encrypt_password(self, password: str):
        return pwd_context.hash(password)
