from fastapi import APIRouter, status

from app.application.use_case.create_user import CreateUser
from app.domain.entities.user import User
from app.infra.repositories.db_user_repository import DbUserRepository
from app.infra.schema.user import CreateUserSchema, UserSchema
from shared.infra.schema.paginated_response import PaginatedResponse

user_router = APIRouter(prefix='/user', tags=['User'])


@user_router.post(path='/', status_code=status.HTTP_201_CREATED)
def create_user(user_input: CreateUserSchema) -> UserSchema:
    """
    This route will be used to create a user
    """
    user = User(**user_input.model_dump())

    user_repository = DbUserRepository()
    create_user = CreateUser(user_repository=user_repository)
    created_user = create_user.execute(user=user)

    return created_user.to_json()


@user_router.get(path='/', status_code=status.HTTP_200_OK)
def list_user(
    offset: int = 0, limit: int = 10
) -> PaginatedResponse[UserSchema]:
    """
    This route will be used to get all users
    """
    user_repository = DbUserRepository()
    users = user_repository.list(offset=offset, limit=limit)

    return users
