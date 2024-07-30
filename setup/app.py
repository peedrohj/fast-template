"""Fast API APP"""

from typing import Dict, List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.infra.controllers.router import app_router
from setup.config import CONFIG
from setup.db.config import BASE, engine
from setup.health import health_router
from setup.middleware.exception_handler import exception_handler


class GenericError(BaseModel):
    error: str
    message: str


class SerializationError(BaseModel):
    class DetailError(BaseModel):
        type: str
        loc: List[str]
        msg: str
        input: Dict[str, str]

    detail: List[DetailError]


app = FastAPI(
    title='Fast setup API',
    summary='Summary from fast API',
    description='Description from fast API',
    version='0.1.0',
    responses={
        500: {'model': GenericError},
        403: {'model': GenericError},
        422: {'model': SerializationError},
    },
)

app.router.prefix = '/api/v1'

app.add_middleware(
    CORSMiddleware,
    allow_origins=CONFIG.CORS_ALLOW_ORIGINS,
    allow_credentials=CONFIG.CORS_ALLOW_CREDENTIALS,
    allow_methods=CONFIG.CORS_ALLOW_METHODS,
    allow_headers=CONFIG.CORS_ALLOW_HEADERS,
)

app.add_exception_handler(Exception, exception_handler)
app.include_router(health_router)
app.include_router(app_router)
