"""Fast API APP"""

from fastapi import FastAPI

from .config import Config

app = FastAPI()


@app.get('/')
def read_root():
    """
    Read root function for fast API
    """
    print(Config().DB_URL)
    return {'message': 'Hello from fast API!'}
