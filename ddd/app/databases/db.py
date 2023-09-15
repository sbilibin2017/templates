import functools
import logging
from contextlib import AbstractAsyncContextManager, asynccontextmanager
from typing import Callable

from elasticsearch import AsyncElasticsearch
from interfaces.storage import StorageABC


class DatabaseConnectionError(Exception):
    "Raises exception if database is not responding."


class Database(StorageABC):
    def __init__(self, host: str, port: int, logger: logging.Logger):
        self.host = host
        self.port = port
        self.session = AsyncElasticsearch(hosts=[f"http://{host}:{port}"])
        self.logger = logger

    @asynccontextmanager
    async def session(
        self,
    ) -> Callable[..., AbstractAsyncContextManager[AsyncElasticsearch]]:
        session: AsyncElasticsearch = self.session
        try:
            self.logger.info("Successfully connected to elastic")
            yield session, None
        except DatabaseConnectionError("Cant connect to database") as e:
            self.logger.error(str(e))
            yield None, str(e)
        finally:
            self.logger.info("Successfully connected to database")
            await session.close()


@functools.lru_cache()
def get_db(host: str, port: int, logger: logging.Logger) -> Database:
    return Database(host, port, logger)
