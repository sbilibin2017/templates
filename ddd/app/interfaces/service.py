from abc import ABC, abstractmethod
from typing import Generic, Protocol, TypeVar
from uuid import UUID

T = TypeVar("T")


class GenericServiceProtocol(Protocol):
    def add(self, record: T) -> T:
        pass

    def get_by_id(self, id: UUID) -> T | None:
        pass

    def get_by_filters(self, **filters) -> list[T]:
        pass

    def get_by_fulltext_search(
        self, key: str, value: str | int | float | bool
    ) -> list[T]:
        pass

    def update(self, record: T) -> T:
        pass

    def delete(self, id: UUID) -> None:
        pass

    def _make_one_response(self, payload, status):
        pass

    def _make_many_response(self, payload, status):
        pass
