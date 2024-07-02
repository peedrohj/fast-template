from typing import List, Literal

from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ConfigClass(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )

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

    @computed_field
    def DB_URL(self) -> str:
        return f'postgresql+psycopg2://{self.DB_HOST}/{self.DB_NAME}?user={self.DB_USERNAME}&password={self.DB_PASSWORD}'


CONFIG = ConfigClass()
