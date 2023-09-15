from abc import ABC
from typing import Type

from interfaces.repository.cache import CacheRepositoryABC

T = TypeVar("T")


from uuid import UUID


class CacheRepository(CacheRepositoryABC):
    def __init__(self, cache) -> None:
        pass

    async def set(self):
        pass

    async def get(self, id: str):
        pass
