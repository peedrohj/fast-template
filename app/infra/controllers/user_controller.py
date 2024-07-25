from fastapi import APIRouter, status

from app.application.use_case.create_user import CreateUser
from app.infra.schema.user import CreateUserSchema, UserSchema
from shared.infra.schema.paginated_response import PaginatedResponse

user_router = APIRouter(prefix='/user', tags=['User'])


@user_router.post(path='/', status_code=status.HTTP_201_CREATED)
def create_user(user_input: CreateUserSchema) -> UserSchema:
    """
    This route will be used to create a user
    """
    user = User(**user_input.dict())

    create_user = CreateUser(user_repository=None)
    created_user = create_user.execute(user=user)

    return created_user.to_json()


