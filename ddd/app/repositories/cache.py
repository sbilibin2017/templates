from abc import ABC
from typing import Type, TypeVar

from interfaces.repository.cache import CacheRepositoryProtocol

T = TypeVar("T")


from uuid import UUID


class CacheRepository(CacheRepositoryProtocol):
    def __init__(self, cache) -> None:
        pass

    async def set(self):
        pass

    async def get(self, id: str):
        pass
