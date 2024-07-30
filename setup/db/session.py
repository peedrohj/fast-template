from sqlalchemy.orm import Session

from setup.db.config import engine


def get_session():
    with Session(engine) as session, session.begin():
        yield session
