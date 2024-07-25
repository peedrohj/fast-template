from pydantic import BaseModel, EmailStr, Field

from shared.infra.schema.base_schema import BaseSchema


class CreateUserSchema(BaseModel):
    username: str = Field(
        description='Username that will be used for the user'
    )
    email: EmailStr = Field(description='Email that will be used for the user')
    password: str = Field(
        description='Password that will be used for the user'
    )


class UserSchema(BaseSchema):
    username: str = Field(description='Username used by the user')
    email: EmailStr = Field(description='Email used by the user')
