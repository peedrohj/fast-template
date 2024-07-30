from sqlalchemy.orm import sessionmaker

from setup.db.config import engine

Session = sessionmaker(engine)


def get_session():
    with Session.begin() as session:
        yield session
