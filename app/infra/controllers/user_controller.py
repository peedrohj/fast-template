from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.application.use_case.user.create_user import CreateUser
from app.application.use_case.user.delete_user import DeleteUser
from app.application.use_case.user.update_user import UpdateUser
from app.domain.entities.user import User
from app.infra.repositories.db_user_repository import DbUserRepository
from app.infra.schema.user import CreateUserSchema, UserSchema
from setup.db.session import get_session
from shared.infra.schema.paginated_response import PaginatedResponse

user_router = APIRouter(prefix='/user', tags=['User'])


@user_router.post(path='/', status_code=status.HTTP_201_CREATED)
def create_user(
    user_input: CreateUserSchema, session: Session = Depends(get_session)
) -> UserSchema:
    """
    This route will be used to create a user
    """
    user = User(**user_input.model_dump())

    user_repository = DbUserRepository()
    create_user = CreateUser(user_repository=user_repository, session=session)
    created_user = create_user.execute(user=user)

    return created_user.to_json()


@user_router.get(path='/', status_code=status.HTTP_200_OK)
def list_user(
    offset: int = 0, limit: int = 10, session: Session = Depends(get_session)
) -> PaginatedResponse[UserSchema]:
    """
    This route will be used to get all users
    """
    user_repository = DbUserRepository()
    users = user_repository.list(offset=offset, limit=limit, session=session)

    return users


@user_router.get(path='/{user_id}', status_code=status.HTTP_200_OK)
def find_user(
    user_id: int, session: Session = Depends(get_session)
) -> UserSchema:
    """
    This route will be used to get a user by id
    """
    user_repository = DbUserRepository()
    users = user_repository.find(user_id=user_id, session=session)

    return users


@user_router.put(path='/{user_id}', status_code=status.HTTP_200_OK)
def update_user(
    user_id: int,
    user_input: CreateUserSchema,
    session: Session = Depends(get_session),
) -> None:
    """
    This route will be used to update an user
    """
    user = User(**user_input.model_dump(), id=user_id)

    user_repository = DbUserRepository()
    update_user = UpdateUser(user_repository=user_repository, session=session)
    updated_user = update_user.execute(user=user)

    return updated_user


@user_router.delete(path='/{user_id}', status_code=status.HTTP_200_OK)
def delete_user(user_id: int, session: Session = Depends(get_session)) -> None:
    """
    This route will be used to create a user
    """
    user_repository = DbUserRepository()
    delete_user = DeleteUser(user_repository=user_repository, session=session)
    delete_user.execute(user_id=user_id)
