import repositories
import services
from core.config import config
from core.logger import get_logger
from databases.cache import get_cache
from databases.db import get_db
from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    # load config with database, cache connections
    config = providers.Configuration(pydantic_settings=[config])

    # load configured logger
    logger = providers.Resource(get_logger)

    # load redis instance with logger injection
    cache = providers.Resource(
        get_cache,
        host=config.docker.cache_host,
        port=config.cache.port,
        db=config.cache.db,
        logger=logger,
    )

    # load elastic instance with logger injection
    db = providers.Resource(
        get_db,
        host=config.docker.db_host,
        port=config.db.port,
        logger=logger,
    )

    # # load elastic repository with db and logger injections
    # db_repository = providers.Factory(
    #     repositories.db.DBRepository,
    #     db=db,
    #     logger=logger,
    # )
    # # load cache repository with redis and logger injections
    # cache_repository = providers.Factory(
    #     repositories.cache.CacheRepository,
    #     cache=cache,
    #     logger=logger,
    # )

    # # load movies service with elastic, redis, logger injections
    # movies_service = providers.Factory(
    #     services.movies.MoviesService,
    #     db_repository=db_repository,
    #     cache_repository=cache_repository,
    #     logger=logger,
    # )
