from app.domain.repositories.user_repository import UserRepository
from shared.domain.entities.session import DatabaseSession


class DeleteUser:
    def __init__(
        self, user_repository: UserRepository, session: DatabaseSession
    ):
        self.__user_repository = user_repository
        self.__session = session

    def execute(self, user_id: int):
        try:
            self.__user_repository.delete(
                user_id=user_id, session=self.__session
            )
        except Exception as err:
            self.__session.rollback()
            raise err
        finally:
            self.__session.commit()
