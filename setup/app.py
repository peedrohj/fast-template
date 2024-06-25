""" Fast API APP """

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """
    Read root function for fast API
    """
    return {"message": "Hello from fast API!"}
