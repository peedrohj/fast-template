from app.domain.repositories.user_repository import UserRepository
from setup.db.session import get_session


class DeleteUser:
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def execute(self, user_id: int):
        session = next(get_session())

        try:
            self.__user_repository.delete(user_id=user_id, session=session)
        except Exception as err:
            session.rollback()
            raise err
        finally:
            session.commit()
