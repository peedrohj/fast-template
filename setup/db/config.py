from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from setup.config import CONFIG

engine = create_engine(CONFIG.DB_URL)

BASE = declarative_base()
