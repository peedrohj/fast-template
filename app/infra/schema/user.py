from pydantic import BaseModel, EmailStr, Field

from shared.infra.schema.base_schema import BaseSchema


class CreateUserSchema(BaseModel):
    name: str = Field(description='Username that will be used for the user')
    email: EmailStr = Field(description='Email that will be used for the user')
    password: str = Field(
        description='Password that will be used for the user'
    )


class UpdateUserSchema(BaseModel):
    name: str = Field(description='Username that will be used for the user')
    email: EmailStr = Field(description='Email that will be used for the user')


class UserSchema(BaseSchema):
    name: str = Field(description='Username used by the user')
    email: str = Field(description='Email used by the user')
