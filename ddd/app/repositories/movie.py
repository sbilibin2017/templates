from uuid import UUID

from models.movie import Movie
from repositories.cache import CacheRepository
from repositories.db import GenericDBRepository


class MovieRepository:
    def __init__(self, db: GenericDBRepository[Movie], cache: CacheRepository) -> None:
        self.db = GenericDBRepository[Movie](db, Movie)
        self.cache = CacheRepository(cache)

    async def get_by_id(self, id: UUID) -> Movie:
        movie = self._get_from_cache(id)
        if movie is None:
            movie = self._get_from_db(id)
            return movie

    async def _get_from_db(self, id):
        pass

    async def _get_from_cache(self, id):
        pass
