import dataclasses

from shared.domain.entities.entity import BaseEntity


@dataclasses.dataclass
class User(BaseEntity):
    username: str
    email: str
    password: str = None
