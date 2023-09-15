import functools
import logging
from contextlib import AbstractAsyncContextManager, asynccontextmanager
from typing import Callable

from interfaces.storage import StorageABC
from redis.asyncio import Redis


class CacheConnectionError(Exception):
    "Raises exception if cache is not responding."


class Cache(StorageABC):
    def __init__(self, host: str, port: int, db: int, logger: logging.Logger):
        self.host = host
        self.port = port
        self.session = Redis.from_url(
            f"redis://{host}:{port}/{db}", encoding="utf-8", decode_responses=True
        )
        self.logger = logger

    @asynccontextmanager
    async def session(
        self,
    ) -> Callable[..., AbstractAsyncContextManager[Redis]]:
        session: Redis = self.session
        try:
            self.logger.info("Successfully connected to elastic")
            yield session, None
        except CacheConnectionError("Cant connect to cache") as e:
            self.logger.error(str(e))
            yield None, str(e)
        finally:
            self.logger.info("Successfully connected to database")
            await session.close()


@functools.lru_cache()
def get_cache(host: str, port: int, db: int, logger: logging.Logger) -> Cache:
    return Cache(host, port, db, logger)
