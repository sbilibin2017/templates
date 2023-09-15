from api.v1 import movies
from container import Container
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


def create_app() -> FastAPI:
    container = Container()
    app = FastAPI(
        title="Template API Domain Driven Desing(DDD)",
        docs_url="/api/openapi",
        openapi_url="/api/openapi.json",
        default_response_class=ORJSONResponse,
    )
    app.container = container
    app.include_router(movies.router, prefix="/api/v1/movies", tags=["movies"])
    return app


app = create_app()
