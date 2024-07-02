from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from setup.config import CONFIG

engine = create_engine(CONFIG.DB_URL)


def get_session():
    with Session(engine) as session:
        yield session
