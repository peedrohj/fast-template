from typing import Protocol


class DatabaseSession(Protocol):
    def rollback(self) -> None: ...
    def begin(self) -> None: ...
    def commit(self) -> None: ...