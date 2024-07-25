from pydantic import EmailStr, Field
from pydantic.dataclasses import dataclass

from shared.infra.schema.base_schema import BaseSchema


@dataclass
class CreateUserSchema:
    username: str = Field(
        description='Username that will be used for the user'
    )
    email: EmailStr = Field(description='Email that will be used for the user')
    password: str = Field(
        description='Password that will be used for the user'
    )


@dataclass
class UserSchema(BaseSchema):
    username: str = Field(
        description='Username used by the user'
    )
    email: EmailStr = Field(description='Email used by the user')
