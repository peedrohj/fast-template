from dataclasses import dataclass

from shared.domain.entities.entity import BaseEntity


@dataclass
class User(BaseEntity):
    username: str
    email: str
    password: str = None
