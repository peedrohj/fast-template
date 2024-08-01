from sqlalchemy.orm import Session

from setup.db.config import engine


def get_session():
    with Session(
        engine, autoflush=True, autobegin=True
    ) as session:
        yield session
