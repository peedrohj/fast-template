from typing import List

from pydantic import BaseModel


class PaginationProps(BaseModel):
    class Config:
        from_attributes = True

    current_page: int = 0
    total_records: int = 0
    total_pages: int = 0
    page_size: int = 0


class PaginatedResponse[T](BaseModel):
    class Config:
        from_attributes = True

    data: List[T]
    pagination: PaginationProps
