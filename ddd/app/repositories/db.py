from abc import ABC
from typing import Protocol, Type, TypeVar

from interfaces.repositories.db import GenericDBRepositoryProtocol

T = TypeVar("T")


from uuid import UUID


class GenericDBRepository(GenericDBRepositoryProtocol[T]):
    def __init__(self, db, model_cls: Type[T]) -> None:
        self.db = db
        self.model_cls = model_cls

    async def add(self, record: T) -> T:
        pass

    async def get_by_id(self, id: UUID) -> T | None:
        pass

    async def get_by_filters(self, **filters) -> list[T]:
        pass

    async def get_by_fulltext_search(self):
        pass

    async def update(self, record: T) -> T:
        pass

    async def delete(self, id: UUID) -> None:
        pass
