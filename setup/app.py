"""Fast API APP"""

from fastapi import FastAPI
from pydantic import BaseModel

from .config import Config


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


@app.get('/')
def read_root():
    """
    Read root function for fast API
    """
    print(Config().DB_URL)
    return {'message': 'Hello from fast API!'}
