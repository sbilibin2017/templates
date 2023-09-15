from uuid import UUID
from pydantic import BaseModel
from repositories.movie import MovieRepository
import http

class MovieService:
    def __init__(self, movie_repository: MovieRepository, schema) -> None:
        self.movie_repository=movie_repository

    async def get_by_id(self, id: UUID, movie_response_schema:MovieResponseSchema) -> MovieResponseSchema:
        movie = await self.movie_repository.get_by_id(id)        
        if movie is not None:            
            data_schema = movie_response_schema.data
            movie_schema = data_schema.parse_raw(**movie)
            return MovieResponseSchema(
                data = movie_schema                
                status=http.HTTPStatus.OK
            )
        else:
            return MovieResponseSchema(
                data = None,
                status=http.HTTPStatus.NOT_FOUND
            )
            
            

    
