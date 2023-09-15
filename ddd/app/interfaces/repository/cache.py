from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from uuid import UUID


class CacheRepositoryABC(ABC):
    @abstractmethod
    def set(self, key: str, value: str):
        raise NotImplementedError()

    @abstractmethod
    def get(self, key: str) -> str:
        raise NotImplementedError()
