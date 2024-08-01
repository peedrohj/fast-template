from typing import List

from pydantic import BaseModel, computed_field


class PaginatedResponse[T](BaseModel):
    class Config:
        from_attributes = True

    data: List[T]
    number_of_pages: int = 1
    total_items: int = 0
    page_number: int = 1

    @computed_field
    @property
    def page_size(self) -> int:
        return len(self.data)
