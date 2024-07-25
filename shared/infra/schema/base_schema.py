from datetime import datetime

from pydantic import BaseModel, Field


class BaseSchema(BaseModel):
    id: str = Field(
        description='The id of the object',
        default=None,
    )
    created_at: datetime = Field(
        description='Datetime value when the object was created',
        default=None,
    )
    updated_at: datetime = Field(
        description='Datetime value when the object was updated',
        default=None,
    )
    deleted_at: datetime = Field(
        description='Datetime value when the object was deleted',
        default=None,
    )
    archived_at: datetime = Field(
        description='Datetime value when the object was archived',
        default=None,
    )

    class Config:
        from_attributes = True
