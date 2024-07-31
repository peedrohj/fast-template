from typing import List, Literal

from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ConfigClass(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )

    APP_NAMES: List[str] = Field(default=['app', 'shared'])

    CORS_ALLOW_ORIGINS: List[str] = Field(
        default=[
            'http://localhost',
            'http://localhost:3000',
            '*',
        ]
    )
    CORS_ALLOW_CREDENTIALS: bool = Field(default=True)
    CORS_ALLOW_METHODS: List[str] = Field(
        default=[
            '*',
        ]
    )
    CORS_ALLOW_HEADERS: List[str] = Field(
        default=[
            '*',
        ]
    )

    ENVIRONMENT: Literal['prod', 'dev', 'test'] = Field(default='dev')
    DB_NAME: str = Field(default='fast')
    DB_USERNAME: str = Field(default='user')
    DB_HOST: str = Field(default='localhost:5432')
    DB_PASSWORD: str = Field(default='password')

    def DB_POSTGRES_URL(self) -> str:
        return f'postgresql+psycopg2://{self.DB_HOST}/{self.DB_NAME}?user={self.DB_USERNAME}&password={self.DB_PASSWORD}'

    def DB_SQLITE_URL(self) -> str:
        return f'sqlite:///{self.DB_NAME}.db'

    @computed_field
    @property
    def DB_URL(self) -> str:
        if self.ENVIRONMENT != 'prod':
            return self.DB_SQLITE_URL()

        return self.DB_POSTGRES_URL()


CONFIG = ConfigClass()
