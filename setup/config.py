from typing import Literal

from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )

    ENVIRONMENT: Literal['prod', 'dev', 'test'] = Field(default='dev')
    DB_ADDRESS: str = Field(default='5432')
    DB_NAME: str = Field(default='fast')
    DB_USERNAME: str = Field(default='user')
    DB_HOST: str = Field(default='localhost')
    DB_PASSWORD: str = Field(default='password')

    @computed_field
    def DB_URL(self) -> str:
        return f'postgresql+psycopg2://{self.DB_HOST}/{self.DB_NAME}?user={self.DB_USERNAME}&password={self.DB_PASSWORD}'
