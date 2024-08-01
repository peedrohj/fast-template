import dataclasses
from typing import List


@dataclasses.dataclass
class PaginatedResponse[T]:
    data: List[T]
    number_of_pages: int = 1
    page_number: int = 1
    total_items: int = 0

    @property
    def page_size(self) -> int:
        return len(self.data)


class BaseRepository[T]:
    def _paginate_response(
        self, data: T, total_items: int, page_number: int
    ) -> PaginatedResponse[T]:
        return PaginatedResponse(
            data=data,
            page_number=page_number,
            number_of_pages=int(total_items / 10) + 1,
            total_items=total_items,
        )
