"""Fast API APP"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.infra.controllers.router import app_router
from setup.config import CONFIG
from setup.middleware.exception_handler import exception_handler

from .health import health_router


class Message(BaseModel):
    code: str
    message: str


app = FastAPI(
    title='Fast setup API',
    summary='Summary from fast API',
    description='Description from fast API',
    version='0.1.0',
    responses={
        500: {
            'model': Message,
            'content': {
                'application/json': {
                    'example': [
                        {'code': '500', 'message': 'Internal server error'},
                    ]
                }
            },
        },
        403: {'model': Message},
        422: {'model': Message},
    },
)

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

