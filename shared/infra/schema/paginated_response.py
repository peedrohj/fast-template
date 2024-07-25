from typing import List

from pydantic import BaseModel


class PaginatedResponse[T](BaseModel):
    data: List[T]
    page_size: int = 10
    page_count: int = 1
    page_index: int = 1

    class Config:
        from_attributes = True
