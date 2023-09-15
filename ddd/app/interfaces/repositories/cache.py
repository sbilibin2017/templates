from abc import ABC, abstractmethod
from typing import Generic, Protocol, TypeVar
from uuid import UUID


class CacheRepositoryProtocol(Protocol):
    def set(self, key: str, value: str):
        pass

    def get(self, key: str) -> str:
        pass
