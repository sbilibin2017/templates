from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from uuid import UUID

T = TypeVar("T")


class GenericDBRepositoryABC(Generic[T], ABC):
    @abstractmethod
    def add(self, record: T) -> T:
        raise NotImplementedError()

    @abstractmethod
    def get_by_id(self, id: UUID) -> T | None:
        raise NotImplementedError()

    @abstractmethod
    def get_by_filters(self, **filters) -> list[T]:
        raise NotImplementedError()

    @abstractmethod
    def get_by_fulltext_search(
        self, key: str, value: str | int | float | bool
    ) -> list[T]:
        raise NotImplementedError()

    @abstractmethod
    def update(self, record: T) -> T:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, id: UUID) -> None:
        raise NotImplementedError()
