import dataclasses
from datetime import datetime
from typing import Optional


@dataclasses.dataclass(init=True, slots=True, kw_only=True)
class BaseEntity:
    id: str | None = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    archived_at: Optional[datetime] = None

    def to_json(self, include_null=True) -> dict:
        """Converts this to json.

        Args:
            include_null (bool, optional): Whether null values are included.

        Returns:
            dict: Json dictionary
        """
        return dataclasses.asdict(
            self,
            dict_factory=lambda fields: {
                key: value
                for (key, value) in fields
                if value is not None or include_null
            },
        )
