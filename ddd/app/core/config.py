import pydantic
from dotenv import load_dotenv

load_dotenv(".env.prod")


class Config(pydantic.BaseSettings):
    app_host: str = pydantic.Field(default="0.0.0.0", alias="APP_HOST")
    app_port: int = pydantic.Field(default=8000, alias="APP_PORT")

    db_host: str = pydantic.Field(default="0.0.0.0", alias="DB_HOST")
    db_port: int = pydantic.Field(default=8000, alias="DB_PORT")

    cache_host: str = pydantic.Field(default="0.0.0.0", alias="CACHE_HOST")
    cache_port: int = pydantic.Field(default=8000, alias="CACHE_PORT")
    cache_db: int = pydantic.Field(default=8000, alias="CACHE_DB")

    docker_db_host: str = pydantic.Field(default="db", alias="DOCKER_DB_HOST")
    docker_cache_host: str = pydantic.Field(default="cache", alias="DOCKER_CACHE_HOST")


config = Config()
