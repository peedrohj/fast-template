from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository


class CreateUser:
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def execute(self, user: User) -> User:
        return self.__user_repository.save(user=user)
