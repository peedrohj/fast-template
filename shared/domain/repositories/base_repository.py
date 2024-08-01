import dataclasses
from typing import List


@dataclasses.dataclass
class PaginationProps:
    current_page: int = 0
    total_records: int = 0
    total_pages: int = 0
    page_size: int = 0


@dataclasses.dataclass
class PaginatedResponse[T]:
    data: List[T]
    pagination: PaginationProps = dataclasses.field(
        default_factory=PaginationProps()
    )

    def __post_init__(self):
        self.pagination.page_size = len(self.data)


class BaseRepository[T]:
    def _paginate_response(
        self, data: T, pagination: PaginationProps
    ) -> PaginatedResponse[T]:
        return PaginatedResponse(
            data=data,
            pagination=pagination,
        )
