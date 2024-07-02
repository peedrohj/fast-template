"""Fast API APP"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from setup.config import CONFIG


class Message(BaseModel):
    code: str
    message: str


app = FastAPI(
    title='Fast setup API',
    summary='Summary from fast API',
    description='Description from fast API',
    version='0.1.0',
    responses={
        500: {'model': Message},
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
